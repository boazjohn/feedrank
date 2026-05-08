#!/usr/bin/env python3
"""
feedrank — aggregate, filter, rank security feeds with BM25.

Pipeline:
  1. Fetch RSS/Atom + GHSA/KEV APIs in parallel
  2. Window by --days
  3. Keyword filter (skip with --no-filter)
  4. Dedupe by URL and normalized title
  5. Rank with BM25 against your interest profile + boost terms,
     multiplied by severity, recency, and source weight
  6. Render: HTML + Markdown + JSON
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import logging
import math
import os
import re
import sys
import time
import tomllib
import urllib.request
from collections import Counter
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

import feedparser

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("feedrank")


# ---------------------------------------------------------------------------
# BM25 — pure Python, no numpy, no compiled deps
# ---------------------------------------------------------------------------
class BM25:
    """Okapi BM25 in pure Python.

    Standard formulation:
        IDF(q) = ln((N - df(q) + 0.5) / (df(q) + 0.5) + 1)
        score(D, Q) = sum over q in Q of:
            IDF(q) * (f(q,D) * (k1+1)) / (f(q,D) + k1*(1 - b + b*|D|/avgdl))
    """

    def __init__(self, corpus: list[list[str]], k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.corpus_size = len(corpus)
        self.doc_lens = [len(d) for d in corpus]
        self.avgdl = sum(self.doc_lens) / self.corpus_size if self.corpus_size else 0.0
        # Per-doc term frequencies
        self.doc_freqs: list[Counter] = [Counter(d) for d in corpus]
        # Document frequency of each term
        df: Counter = Counter()
        for d in corpus:
            df.update(set(d))
        # IDF, clamped to >= 0 (BM25+ style; classic BM25 can go slightly negative
        # for very common terms which is rarely what you want for ranking)
        N = self.corpus_size
        self.idf: dict[str, float] = {
            t: max(math.log((N - n + 0.5) / (n + 0.5) + 1.0), 0.0)
            for t, n in df.items()
        }

    def get_scores(self, query: list[str]) -> list[float]:
        """Score every document in the corpus against the query."""
        scores = [0.0] * self.corpus_size
        if not query or self.corpus_size == 0:
            return scores
        k1, b, avgdl = self.k1, self.b, self.avgdl
        for q in query:
            idf = self.idf.get(q)
            if not idf:
                continue
            for i, freqs in enumerate(self.doc_freqs):
                f = freqs.get(q, 0)
                if not f:
                    continue
                dl = self.doc_lens[i]
                denom = f + k1 * (1.0 - b + b * dl / avgdl) if avgdl else 1.0
                scores[i] += idf * f * (k1 + 1.0) / denom
        return scores


@dataclass
class Item:
    title: str
    link: str
    summary: str
    published: str
    source: str
    category: str
    source_weight: float
    matched_keywords: list[str] = field(default_factory=list)
    score: float = 0.0
    bm25: float = 0.0
    severity: str = ""
    cvss: float = 0.0
    cves: list[str] = field(default_factory=list)
    corroboration: int = 1
    other_sources: list[dict] = field(default_factory=list)
    id: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.sha256(self.link.encode()).hexdigest()[:12]


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------
def _http_get(url: str, timeout: int, accept: str = "*/*",
              extra_headers: dict | None = None) -> bytes:
    headers = {
        "User-Agent": "feedrank/1.0 (+rss reader)",
        "Accept": accept,
    }
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def fetch_ghsa_api(ecosystem: str, source: dict, timeout: int) -> list[Item]:
    name = source["name"]
    api_url = f"https://api.github.com/advisories?ecosystem={ecosystem}&per_page=50"
    # GH_TOKEN env var lifts the unauthenticated rate limit (60/hr) to 5000/hr.
    extra: dict[str, str] = {"X-GitHub-Api-Version": "2022-11-28"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        extra["Authorization"] = f"Bearer {token}"
    try:
        data = json.loads(_http_get(api_url, timeout,
                                     "application/vnd.github+json", extra))
    except Exception as e:
        log.warning(f"fetch fail [{name}]: {e}")
        return []
    items = []
    for adv in data:
        title = (adv.get("summary") or "").strip() or adv.get("ghsa_id", "")
        link = adv.get("html_url", "")
        if not link or not title:
            continue
        summary = re.sub(r"\s+", " ", (adv.get("description") or "")[:600]).strip()
        pkgs = [(v.get("package") or {}).get("name", "")
                for v in (adv.get("vulnerabilities") or [])]
        pkgs = [p for p in pkgs if p]
        if pkgs:
            summary = f"Affected: {', '.join(pkgs[:5])}. " + summary
        cves = [i.get("value", "") for i in (adv.get("identifiers") or [])
                if i.get("type") == "CVE"]
        items.append(Item(
            title=title, link=link, summary=summary,
            published=adv.get("published_at") or adv.get("updated_at") or "",
            source=name, category=source.get("category", "advisory"),
            source_weight=float(source.get("weight", 1.0)),
            severity=(adv.get("severity") or "").lower(),
            cvss=float((adv.get("cvss") or {}).get("score") or 0.0),
            cves=cves,
        ))
    log.info(f"fetched {len(items):3d} from {name}")
    return items


def fetch_kev(source: dict, timeout: int) -> list[Item]:
    name = source["name"]
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    try:
        data = json.loads(_http_get(url, timeout, "application/json"))
    except Exception as e:
        log.warning(f"fetch fail [{name}]: {e}")
        return []
    items = []
    for v in sorted(data.get("vulnerabilities", []),
                    key=lambda x: x.get("dateAdded", ""), reverse=True)[:50]:
        cve = v.get("cveID", "")
        if not cve:
            continue
        title = f"{v.get('vendorProject','')} {v.get('product','')}: {v.get('vulnerabilityName','')}".strip()
        summary = v.get("shortDescription", "")
        if v.get("requiredAction"):
            summary += f" Required action: {v['requiredAction']}"
        date_added = v.get("dateAdded", "")
        if date_added and "T" not in date_added:
            date_added = f"{date_added}T00:00:00+00:00"
        items.append(Item(
            title=title, link=f"https://nvd.nist.gov/vuln/detail/{cve}",
            summary=summary, published=date_added,
            source=name, category=source.get("category", "government"),
            source_weight=float(source.get("weight", 1.0)),
            cves=[cve], severity="critical", cvss=9.0,
        ))
    log.info(f"fetched {len(items):3d} from {name}")
    return items


def fetch_rss(source: dict, timeout: int) -> list[Item]:
    name = source["name"]
    try:
        raw = _http_get(source["url"], timeout)
    except Exception as e:
        log.warning(f"fetch fail [{name}]: {e}")
        return []
    parsed = feedparser.parse(raw)
    items = []
    for e in parsed.entries:
        link = getattr(e, "link", "")
        title = (getattr(e, "title", "") or "").strip()
        if not link or not title:
            continue
        summary = ""
        for attr in ("summary", "description", "content"):
            v = getattr(e, attr, None)
            if isinstance(v, list) and v:
                summary = v[0].get("value", "") if isinstance(v[0], dict) else str(v[0])
            elif isinstance(v, str):
                summary = v
            if summary:
                break
        summary = re.sub(r"<[^>]+>", " ", summary)
        summary = re.sub(r"\s+", " ", summary).strip()[:600]

        pub = ""
        for attr in ("published_parsed", "updated_parsed"):
            t = getattr(e, attr, None)
            if t:
                try:
                    pub = datetime(*t[:6], tzinfo=timezone.utc).isoformat()
                    break
                except Exception:
                    pass
        if not pub:
            pub = datetime.now(timezone.utc).isoformat()

        items.append(Item(
            title=title, link=link, summary=summary, published=pub,
            source=name, category=source.get("category", ""),
            source_weight=float(source.get("weight", 1.0)),
        ))
    log.info(f"fetched {len(items):3d} from {name}")
    return items


def fetch_osv(source: dict, timeout: int) -> list[Item]:
    """OSV.dev — query for vulnerabilities in high-value ecosystems.

    OSV doesn't have a generic "recent" feed. We query a small set of
    ecosystems with an empty query that returns all package vulns; OSV
    sorts by modified date so we get recent ones near the top.
    """
    name = source["name"]
    weight = float(source.get("weight", 1.0))
    category = source.get("category", "advisory")
    ecosystems = ["npm", "PyPI", "Packagist", "crates.io", "Go"]
    items: list[Item] = []
    for eco in ecosystems:
        body = json.dumps({"query": {"package": {"ecosystem": eco}}}).encode()
        req = urllib.request.Request(
            "https://api.osv.dev/v1/query",
            data=body,
            headers={"Content-Type": "application/json",
                     "User-Agent": "feedrank/1.0"},
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read())
        except Exception as e:
            log.warning(f"fetch fail [{name}/{eco}]: {e}")
            continue
        vulns = data.get("vulns", []) or []
        # Sort by modified desc, take 20 per ecosystem
        vulns.sort(key=lambda v: v.get("modified", ""), reverse=True)
        for v in vulns[:20]:
            vid = v.get("id", "")
            if not vid:
                continue
            title = v.get("summary") or vid
            link = f"https://osv.dev/vulnerability/{vid}"
            summary = re.sub(r"\s+", " ", (v.get("details") or "")[:600]).strip()
            pub = v.get("published") or v.get("modified") or ""
            pkgs = []
            for aff in v.get("affected") or []:
                p = (aff.get("package") or {}).get("name")
                if p:
                    pkgs.append(p)
            if pkgs:
                summary = f"Affected: {', '.join(pkgs[:5])}. " + summary
            cves = [a for a in (v.get("aliases") or []) if a.startswith("CVE-")]
            items.append(Item(
                title=title, link=link, summary=summary, published=pub,
                source=f"{name} ({eco})", category=category,
                source_weight=weight, cves=cves,
            ))
    log.info(f"fetched {len(items):3d} from {name}")
    return items


def fetch_one(source: dict, timeout: int = 15) -> list[Item]:
    url = source["url"]
    if url.startswith("ghsa-api://"):
        return fetch_ghsa_api(url.removeprefix("ghsa-api://"), source, timeout)
    if url.startswith("kev-api://"):
        return fetch_kev(source, timeout)
    if url.startswith("osv-api://"):
        return fetch_osv(source, timeout)
    return fetch_rss(source, timeout)


def fetch_all(sources: list[dict], max_workers: int = 8) -> list[Item]:
    items: list[Item] = []
    with cf.ThreadPoolExecutor(max_workers=max_workers) as pool:
        for batch in pool.map(fetch_one, sources):
            items.extend(batch)
    return items


# ---------------------------------------------------------------------------
# Process
# ---------------------------------------------------------------------------
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)
SEVERITY_TERMS = {
    # Explicit severity language
    "critical": 9.5, "rce": 9.0, "0day": 9.0, "zero-day": 9.0, "zero day": 9.0,
    "actively exploited": 9.5, "wormable": 9.5, "unauthenticated": 8.0,
    "remote code execution": 9.0, "arbitrary code execution": 9.0,
    "high severity": 7.5, "high-severity": 7.5,
    "medium severity": 5.0, "moderate": 5.0,
    "low severity": 3.0,
    # Supply-chain attack phrasing — common in research blogs that don't
    # use formal CVSS language but describe genuinely critical incidents
    "credential stealer": 9.0, "credential-stealing": 9.0,
    "credential theft": 8.5, "token stealer": 9.0,
    "supply chain attack": 8.5, "supply-chain attack": 8.5,
    "compromised on": 8.5, "compromised in": 8.5,
    "hijacked": 8.5, "backdoored": 9.0, "backdoor": 8.5,
    "malicious package": 8.5, "malicious version": 8.5,
    "obfuscated payload": 8.5, "obfuscated javascript": 8.0,
    "self-propagat": 9.0, "worm": 8.5,
}

# Tokenizer that preserves security-relevant tokens:
#   CVE-2026-12345  → kept as one token
#   intercom-client → kept as one token (hyphenated package names)
#   @sap/cds        → kept as @sap/cds
#   k8s, ci/cd      → kept as one token
# Everything else split on whitespace and most punctuation, lowercased.
_TOKEN_RE = re.compile(
    r"""
    [Cc][Vv][Ee]-\d{4}-\d{4,7}             # CVE IDs
    | @[a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+      # scoped npm packages
    | [a-zA-Z][a-zA-Z0-9]*(?:[-/][a-zA-Z0-9]+)+   # hyphenated/slash terms
    | [a-zA-Z][a-zA-Z0-9_.]*               # regular words / package names
    """,
    re.VERBOSE,
)
STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "must", "shall", "can", "of", "to", "in",
    "for", "on", "with", "at", "by", "from", "as", "this", "that", "these",
    "those", "it", "its", "and", "or", "but", "if", "then", "than", "so",
    "we", "you", "they", "their", "our", "your", "i", "me", "my",
}


def tokenize(text: str) -> list[str]:
    """Tokenize for BM25. Lowercase, strip stopwords, preserve security tokens."""
    if not text:
        return []
    toks = [m.lower() for m in _TOKEN_RE.findall(text)]
    return [t for t in toks if t not in STOPWORDS and len(t) > 1]


def within_days(item: Item, days: int) -> bool:
    try:
        dt = datetime.fromisoformat(item.published.replace("Z", "+00:00"))
    except Exception:
        return True
    return dt >= datetime.now(timezone.utc) - timedelta(days=days)


def keyword_filter(items: list[Item], keywords: list[str]) -> list[Item]:
    kws = [k.lower() for k in keywords]
    out = []
    for it in items:
        hay = (it.title + " " + it.summary).lower()
        matched = [k for k in kws if k in hay]
        if matched:
            it.matched_keywords = matched
            out.append(it)
    return out


def dedupe(items: list[Item]) -> list[Item]:
    seen_links: set[str] = set()
    seen_titles: set[str] = set()
    out = []
    for it in sorted(items, key=lambda x: x.published, reverse=True):
        if it.link in seen_links:
            continue
        norm = re.sub(r"\W+", "", it.title.lower())[:80]
        if norm in seen_titles:
            continue
        seen_links.add(it.link)
        seen_titles.add(norm)
        out.append(it)
    return out


def enrich(it: Item) -> None:
    text = f"{it.title} {it.summary}"
    if not it.cves:
        it.cves = sorted(set(m.upper() for m in CVE_RE.findall(text)))
    if not it.severity and it.cvss == 0.0:
        text_lc = text.lower()
        for term, cvss in SEVERITY_TERMS.items():
            if term in text_lc:
                it.cvss = max(it.cvss, cvss)
        if it.cvss >= 9.0:   it.severity = "critical"
        elif it.cvss >= 7.0: it.severity = "high"
        elif it.cvss >= 4.0: it.severity = "medium"
        elif it.cvss > 0:    it.severity = "low"


def severity_factor(it: Item) -> float:
    if it.cvss > 0:
        return 1.0 + (it.cvss / 10.0)
    return {"critical": 1.9, "high": 1.6, "medium": 1.3, "low": 1.05}.get(it.severity, 1.0)


# Distinctive tokens that, if shared across items, almost certainly mean
# the items are reporting the same incident. Extends beyond CVE because
# campaigns often don't have a CVE yet (Mini Shai-Hulud, tj-actions, etc.)
_DISTINCTIVE_RE = re.compile(
    r"\b("
    r"shai[\s-]?hulud|"
    r"intercom-client|intercom-php|intercom/intercom-php|"
    r"pytorch[\s-]?lightning|"
    r"tj-actions|reviewdog/action-[a-z0-9-]+|"
    r"@sap/[a-z0-9-]+|"
    r"masscan\.cloud|"
    r"bitwarden[\s-]?cli|"
    r"daemon[\s-]?tools|"
    r"elementary-data|"
    r"xinference|"
    r"pgserve|"
    r"axios@?\d+\.\d+\.\d+|"
    r"gemini[\s-]?cli"
    r")\b",
    re.IGNORECASE,
)

# After matching a distinctive token, normalize it so variations cluster together.
_TOKEN_NORMALIZE = {
    "minishaihulud": "shai-hulud",  # both waves are the same campaign family
    "shaihulud": "shai-hulud",
}


def _normalize_token(t: str) -> str:
    key = re.sub(r"[\s\-/]", "", t.lower())
    return _TOKEN_NORMALIZE.get(key, key)


def cluster_and_collapse(items: list[Item]) -> list[Item]:
    """Detect items reporting the same incident and collapse them.

    An item is in the same cluster as another if they share:
      - a CVE ID, or
      - a distinctive campaign / package name token

    Within a cluster, one item becomes the representative. Selection priority:
      higher source weight -> advisory > research > government > build > aggregator -> recent

    The reps inherit the union of CVEs and the highest CVSS / severity in
    the cluster. The other items become 'other_sources' references on the rep.
    """
    n = len(items)
    if n < 2:
        return items

    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    # CVE-based unions
    cve_groups: dict[str, list[int]] = {}
    for i, it in enumerate(items):
        for cve in it.cves:
            cve_groups.setdefault(cve, []).append(i)
    for idxs in cve_groups.values():
        for j in idxs[1:]:
            union(idxs[0], j)

    # Distinctive-token unions
    token_groups: dict[str, list[int]] = {}
    for i, it in enumerate(items):
        text = f"{it.title} {it.summary}".lower()
        for m in _DISTINCTIVE_RE.findall(text):
            key = _normalize_token(m)
            token_groups.setdefault(key, []).append(i)
        # Lightning-incident detection: bare "lightning" plus context words
        # that indicate a security incident (not just any mention of the
        # framework). Catches "lightning: Obfuscated..." style titles.
        if re.search(r"\blightning\b", text) and re.search(
            r"\b(compromis|backdoor|stealer|hijack|wave|payload|exfiltrat|"
            r"malicious|2\.6\.[23])\b", text
        ):
            token_groups.setdefault("lightning-incident", []).append(i)
    for idxs in token_groups.values():
        if len(idxs) < 2:
            continue
        for j in idxs[1:]:
            union(idxs[0], j)

    # Group by cluster
    from collections import defaultdict
    groups: dict[int, list[int]] = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)

    cat_priority = {"advisory": 0, "research": 1, "government": 2,
                    "build": 3, "aggregator": 4, "": 5}

    def _ts(s: str) -> float:
        try:
            return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
        except Exception:
            return 0.0

    out: list[Item] = []
    for idxs in groups.values():
        members = [items[i] for i in idxs]
        if len(members) == 1:
            out.append(members[0])
            continue
        # Pick rep
        members.sort(key=lambda it: (
            -it.source_weight,
            cat_priority.get(it.category, 9),
            -_ts(it.published),
        ))
        rep = members[0]
        # Merge fields across cluster
        all_cves = set(rep.cves)
        max_cvss = rep.cvss
        sev_order = {"critical": 4, "high": 3, "medium": 2, "low": 1, "": 0}
        best_sev = rep.severity
        seen_sources = {rep.source}  # don't list rep itself
        for other in members[1:]:
            all_cves.update(other.cves)
            max_cvss = max(max_cvss, other.cvss)
            if sev_order.get(other.severity, 0) > sev_order.get(best_sev, 0):
                best_sev = other.severity
            # Dedupe by source name; keep the most recent if same source has multiple
            if other.source in seen_sources:
                continue
            seen_sources.add(other.source)
            rep.other_sources.append({
                "source": other.source,
                "link": other.link,
                "published": other.published,
                "category": other.category,
            })
        rep.cves = sorted(all_cves)
        rep.cvss = max_cvss
        rep.severity = best_sev
        # Corroboration counts distinct sources (more honest signal than total reports)
        rep.corroboration = len(seen_sources)
        out.append(rep)

    return out


def rank(items: list[Item], topics: list[str], boost_terms: list[str]) -> list[Item]:
    if not items:
        return items

    # Build BM25 index over all items. Title gets weighted by repetition
    # (a 3x duplication is the standard trick to boost title matches over body).
    corpus = [
        tokenize(it.title) * 3 + tokenize(it.summary)
        for it in items
    ]
    bm25 = BM25(corpus)

    # Build the query: tokenized topics + boost terms (each topic is a "sub-query"
    # and we take the max BM25 score across them, so an item only needs to match
    # one topic well rather than all of them).
    topic_queries = [tokenize(t) for t in topics]
    boost_query = tokenize(" ".join(boost_terms))

    # Score every item against each topic query, take the max
    raw_scores = [0.0] * len(items)
    for tq in topic_queries:
        if not tq:
            continue
        scores = bm25.get_scores(tq)
        for i, s in enumerate(scores):
            if s > raw_scores[i]:
                raw_scores[i] = float(s)

    # Boost-term query adds an additive bonus
    if boost_query:
        boost_scores = bm25.get_scores(boost_query)
        for i, s in enumerate(boost_scores):
            raw_scores[i] += float(s) * 0.3

    # Normalize raw BM25 to a 0..1 range (max-norm) so it composes with the
    # other multiplicative factors. If the max is 0 (no matches anywhere),
    # everything gets 0 and ranking falls back to recency × severity.
    max_raw = max(raw_scores) if raw_scores else 0.0
    norm_scores = [s / max_raw if max_raw > 0 else 0.0 for s in raw_scores]

    now = datetime.now(timezone.utc)
    for it, bm in zip(items, norm_scores):
        enrich(it)
        it.bm25 = bm
        try:
            dt = datetime.fromisoformat(it.published.replace("Z", "+00:00"))
            age_days = (now - dt).days
            recency = max(0.3, 1.0 - age_days / 14.0)
        except Exception:
            recency = 0.7

        sev = severity_factor(it)
        # Corroboration: 1 source = 1.0x, 2 = 1.28x, 3 = 1.44x, 4 = 1.55x
        corrob = 1.0 + 0.4 * math.log1p(it.corroboration - 1)

        # Score formula:
        # - If item has good BM25 match: standard score
        # - If item has no BM25 match but is critical/high or corroborated:
        #   give it a small base so it can compete
        # - If item has no BM25 match AND is low/no severity AND no corroboration:
        #   bury it (0.01 floor)
        if bm > 0.1:
            base = bm
        elif (it.severity in ("critical", "high")) or it.corroboration > 1:
            # Off-topic but high-severity or multi-source: floor at 0.15
            # so a CVSS 10 RCE outside our stack still appears, just not at top
            base = max(bm, 0.15)
        else:
            base = 0.01  # off-topic, no severity, single source -> bury

        it.score = base * recency * it.source_weight * sev * corrob

    items.sort(key=lambda x: x.score, reverse=True)
    return items


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------
HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>feedrank.security — {date}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT,WONK@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=Recursive:slnt,wght,CASL,CRSV,MONO@-15..0,300..1000,0..1,0..1,0..1&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
<style>
:root {{
  --bg:#f6f1e7; --bg-2:#ede5d3; --ink:#1a2540; --ink-2:#3a4566;
  --rule:#cdbfa3; --accent:#b8331f; --accent-2:#c87633; --good:#4a6b3a;
  --dim:#7a6c54; --hi:#fbe9b7;
  --ft-text:'Inter',system-ui,-apple-system,sans-serif;
  --ft-title:'Fraunces','Iowan Old Style',Georgia,serif;
  --ft-read:'Source Serif 4','Iowan Old Style',Georgia,serif;
  --ft-mono:'Recursive',ui-monospace,'SF Mono',Menlo,monospace;
}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:var(--bg);color:var(--ink)}}
body{{
  font-family:var(--ft-text);
  font-weight:400;line-height:1.55;font-size:15.5px;
  -webkit-font-smoothing:antialiased;
  text-rendering:optimizeLegibility;
  background-image:repeating-linear-gradient(0deg,transparent 0 28px,rgba(26,37,64,0.03) 28px 29px);
}}
.wrap{{max-width:1180px;margin:0 auto;padding:40px 28px 80px}}
header{{border-bottom:2px solid var(--ink);padding-bottom:18px;margin-bottom:28px}}
h1{{font-family:var(--ft-mono);font-variation-settings:"MONO" 1,"wght" 700;font-size:38px;letter-spacing:-0.02em;margin:0 0 4px;line-height:1.1}}
h1 .amp{{color:var(--accent);font-variation-settings:"MONO" 0,"CASL" 1,"CRSV" 1;font-size:42px}}
.tag{{color:var(--dim);font-size:13px;font-family:var(--ft-mono);font-variation-settings:"MONO" 1}}
.meta{{display:flex;gap:18px;flex-wrap:wrap;font-size:12.5px;color:var(--ink-2);margin-top:10px;font-family:var(--ft-mono);font-variation-settings:"MONO" 1}}
.meta b{{color:var(--ink);font-weight:600}}
.controls{{display:flex;gap:8px;flex-wrap:wrap;padding:14px 0 22px;border-bottom:1px dashed var(--rule);margin-bottom:22px}}
.search{{flex:1;min-width:240px;padding:9px 12px;border:1px solid var(--ink);background:var(--bg-2);color:var(--ink);font-family:var(--ft-mono);font-size:14px;font-variation-settings:"MONO" 1}}
.search:focus{{outline:2px solid var(--accent);outline-offset:-1px}}
.chip{{padding:6px 11px;border:1px solid var(--ink-2);background:transparent;color:var(--ink-2);cursor:pointer;font-family:var(--ft-mono);font-size:12px;font-variation-settings:"MONO" 1}}
.chip:hover{{background:var(--bg-2)}}
.chip.active{{background:var(--ink);color:var(--bg);border-color:var(--ink)}}
.sort-row{{display:flex;gap:6px;flex-wrap:wrap;align-items:center;padding:0 0 22px;border-bottom:1px dashed var(--rule);margin-bottom:22px}}
.sort-label{{color:var(--dim);font-family:var(--ft-mono);font-size:11.5px;font-variation-settings:"MONO" 1;letter-spacing:0.05em;text-transform:uppercase;margin-right:4px}}
.sort{{padding:5px 10px;border:1px solid transparent;background:transparent;color:var(--ink-2);cursor:pointer;font-family:var(--ft-mono);font-size:12px;font-variation-settings:"MONO" 1;display:inline-flex;align-items:center;gap:4px}}
.sort:hover{{color:var(--ink);background:var(--bg-2)}}
.sort.active{{color:var(--ink);font-variation-settings:"MONO" 1,"wght" 600;border-color:var(--rule);background:var(--bg-2)}}
.sort .arrow{{display:inline-block;min-width:8px;color:var(--accent);font-size:11px;font-variation-settings:"wght" 700}}
.items[data-sort-key]:not([data-sort-key="score"]) .rank{{visibility:hidden}}
.item{{display:grid;grid-template-columns:56px 1fr auto;gap:20px;padding:20px 0;border-bottom:1px solid var(--rule);align-items:start}}
.item.hidden{{display:none}}
.rank{{font-family:var(--ft-mono);font-variation-settings:"MONO" 1,"wght" 500;font-size:22px;color:var(--ink-2);text-align:right;padding-top:2px;font-feature-settings:"tnum"}}
.rank-1,.rank-2,.rank-3{{color:var(--accent);font-variation-settings:"MONO" 1,"wght" 700}}
.body h2{{margin:0 0 8px;font-family:var(--ft-title);font-size:20px;line-height:1.3;font-weight:600;letter-spacing:-0.012em;font-variation-settings:"opsz" 24,"SOFT" 30}}
.body h2 a{{color:var(--ink);text-decoration:none;border-bottom:1px solid transparent}}
.body h2 a:hover{{border-bottom-color:var(--accent);color:var(--accent)}}
.summary{{color:var(--ink-2);font-family:var(--ft-read);font-size:15px;line-height:1.55;margin:6px 0 10px}}
.kws{{display:flex;gap:5px;flex-wrap:wrap;margin-top:8px;align-items:center}}
.kw{{font-size:11px;padding:2px 7px;background:var(--hi);color:var(--ink);font-family:var(--ft-mono);font-variation-settings:"MONO" 1;border:1px solid var(--rule)}}
.sev{{display:inline-block;font-size:10px;padding:2px 7px;margin-right:6px;font-family:var(--ft-mono);font-variation-settings:"MONO" 1,"wght" 600;letter-spacing:0.05em;text-transform:uppercase;border:1px solid}}
.sev-critical{{background:var(--accent);color:var(--bg);border-color:var(--accent)}}
.sev-high{{background:var(--accent-2);color:var(--bg);border-color:var(--accent-2)}}
.sev-medium{{background:var(--bg-2);color:var(--ink);border-color:var(--ink-2)}}
.sev-low{{background:var(--bg-2);color:var(--dim);border-color:var(--rule)}}
.cve{{font-size:10px;padding:2px 6px;margin-right:4px;font-family:var(--ft-mono);font-variation-settings:"MONO" 1;color:var(--ink-2);border:1px dashed var(--rule);background:transparent}}
.corrob{{display:inline-block;font-size:10px;padding:2px 7px;margin-right:6px;background:var(--ink);color:var(--bg);font-family:var(--ft-mono);font-variation-settings:"MONO" 1,"wght" 600}}
.also{{margin-top:8px;padding-top:6px;border-top:1px dotted var(--rule);font-size:12px;color:var(--dim);font-family:var(--ft-mono);font-variation-settings:"MONO" 1}}
.also-link{{color:var(--ink-2);text-decoration:none;border-bottom:1px dotted var(--rule);margin:0 2px}}
.also-link:hover{{color:var(--accent);border-bottom-color:var(--accent)}}
.also-link.cat-advisory{{color:var(--accent)}}
.also-link.cat-research{{color:var(--ink-2)}}
.also-link.cat-aggregator{{color:var(--accent-2)}}
.also-link.cat-government{{color:var(--good)}}
.right{{text-align:right;font-size:11.5px;color:var(--dim);font-family:var(--ft-mono);font-variation-settings:"MONO" 1;min-width:150px;display:flex;flex-direction:column;gap:4px;padding-top:4px}}
.right .src{{color:var(--ink);font-weight:500}}
.right .src.cat-advisory{{color:var(--accent)}}
.right .src.cat-research{{color:var(--ink-2)}}
.right .src.cat-aggregator{{color:var(--accent-2)}}
.right .src.cat-government{{color:var(--good)}}
.empty{{padding:60px 20px;text-align:center;color:var(--dim);font-family:var(--ft-mono)}}
.items.collapsed .item[data-overflow="true"]{{display:none}}
.show-more{{display:none;margin:24px auto 0;padding:10px 22px;border:1px solid var(--ink);background:transparent;color:var(--ink);font-family:var(--ft-mono);font-size:13px;font-variation-settings:"MONO" 1;cursor:pointer;letter-spacing:0.02em}}
.show-more:hover{{background:var(--ink);color:var(--bg)}}
.show-more-count{{color:var(--dim);margin-left:6px}}
footer{{margin-top:60px;padding-top:18px;border-top:1px solid var(--rule);color:var(--dim);font-size:12px;font-family:var(--ft-mono);font-variation-settings:"MONO" 1;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px}}
@media (max-width:640px){{
  body{{font-size:15px}}
  .wrap{{padding:24px 18px 60px}}
  .item{{grid-template-columns:32px 1fr;gap:14px;padding:16px 0}}
  .right{{grid-column:2;text-align:left;min-width:0;font-size:11.5px}}
  h1{{font-size:30px}}
  .body h2{{font-size:17.5px;letter-spacing:-0.01em}}
  .summary{{font-size:14.5px}}
}}
</style>
</head>
<body><div class="wrap">
<header>
<h1>feedrank<span class="amp">.</span>security</h1>
<div class="tag">supply chain &amp; infra security</div>
<div class="meta">
<span><b>{n}</b> items</span>
<span><b>{ns}</b> sources</span>
<span><b>{days}</b>d window</span>
<span>generated <b>{date}</b></span>
</div>
</header>
<div class="controls">
<input class="search" id="search" placeholder="filter…  (regex: /pattern/)">
<button class="chip active" data-cat="all">all</button>
<button class="chip" data-cat="advisory">advisory</button>
<button class="chip" data-cat="research">research</button>
<button class="chip" data-cat="aggregator">aggregator</button>
<button class="chip" data-cat="government">gov</button>
<button class="chip" data-cat="build">build</button>
<span style="width:1px;background:var(--rule);margin:0 6px"></span>
<button class="chip" data-sev="critical">critical only</button>
<button class="chip" data-sev="high">high+</button>
</div>
<div class="sort-row">
<span class="sort-label">sort:</span>
<button class="sort active" data-sort="score">score <span class="arrow">↓</span></button>
<button class="sort" data-sort="date">date <span class="arrow"></span></button>
<button class="sort" data-sort="sevrank">severity <span class="arrow"></span></button>
<button class="sort" data-sort="corrob">sources <span class="arrow"></span></button>
<button class="sort" data-sort="source">source <span class="arrow"></span></button>
</div>
<div class="items collapsed" id="items">{items}</div>
<button class="show-more" id="show-more">show more <span class="show-more-count" id="show-more-count"></span></button>
<div class="empty" id="empty" style="display:none">no matches</div>
<footer><span>feedrank.security</span><span><a href="feedrank.json">json</a> · <a href="feedrank.md">md</a></span></footer>
</div>
<script>
const items=Array.from(document.querySelectorAll('.item')),search=document.getElementById('search'),chips=document.querySelectorAll('.chip'),empty=document.getElementById('empty');
const itemsContainer=document.getElementById('items'),showMore=document.getElementById('show-more'),showMoreCount=document.getElementById('show-more-count');
const sortButtons=document.querySelectorAll('.sort');
const TOTAL=items.length,INITIAL=10,STEP=20;
let activeCat='all',activeSev=null,reveal=INITIAL;
let sortKey='score',sortDir='desc';

// Sort direction defaults — what makes intuitive sense when picking each key
const DEFAULT_DIR={{score:'desc',date:'desc',sevrank:'desc',corrob:'desc',source:'asc'}};

function isFiltering(){{
  return search.value.trim()!==''||activeCat!=='all'||activeSev!==null;
}}

function applySort(){{
  // Numeric vs string keys
  const numeric={{score:1,date:1,sevrank:1,corrob:1,rank:1}};
  const sorted=[...items].sort((a,b)=>{{
    let av,bv;
    if(numeric[sortKey]){{
      av=parseFloat(a.dataset[sortKey]||0);
      bv=parseFloat(b.dataset[sortKey]||0);
    }}else{{
      av=a.dataset[sortKey]||'';
      bv=b.dataset[sortKey]||'';
    }}
    let cmp=av<bv?-1:av>bv?1:0;
    // Stable secondary sort by score desc — keeps ordering predictable for ties
    if(cmp===0){{
      const as=parseFloat(a.dataset.score||0),bs=parseFloat(b.dataset.score||0);
      cmp=bs-as;
    }}
    return sortDir==='asc'?cmp:-cmp;
  }});
  // Reorder DOM
  const frag=document.createDocumentFragment();
  sorted.forEach(it=>frag.appendChild(it));
  itemsContainer.appendChild(frag);
  itemsContainer.dataset.sortKey=sortKey;
  // Update arrow indicators
  sortButtons.forEach(b=>{{
    const a=b.querySelector('.arrow');
    if(b.dataset.sort===sortKey){{
      b.classList.add('active');
      a.textContent=sortDir==='asc'?'↑':'↓';
    }}else{{
      b.classList.remove('active');
      a.textContent='';
    }}
  }});
}}

function apply(){{
  const q=search.value.trim();let regex=null,plain=q.toLowerCase();
  if(q.startsWith('/')&&q.endsWith('/')&&q.length>2){{try{{regex=new RegExp(q.slice(1,-1),'i');plain='';}}catch(e){{}}}}
  let visible=0;
  items.forEach(it=>{{
    const cat=it.dataset.cat,sev=it.dataset.sev,text=it.dataset.text;
    let show=(activeCat==='all'||cat===activeCat);
    if(show&&activeSev==='critical')show=sev==='critical';
    if(show&&activeSev==='high')show=(sev==='critical'||sev==='high');
    if(show&&q)show=regex?regex.test(text):text.includes(plain);
    it.classList.toggle('hidden',!show);if(show)visible++;
  }});
  empty.style.display=visible===0?'block':'none';
  updateOverflow();
}}

function updateOverflow(){{
  // When filtering OR when sorted by something other than score,
  // show all (overflow gating only makes sense for the default score view).
  if(isFiltering()||sortKey!=='score'){{
    itemsContainer.classList.remove('collapsed');
    showMore.style.display='none';
    return;
  }}
  items.forEach(it=>{{
    const r=parseInt(it.dataset.rank,10);
    it.dataset.overflow=(r>reveal)?'true':'false';
  }});
  if(reveal>=TOTAL){{
    itemsContainer.classList.remove('collapsed');
    showMore.style.display='none';
  }}else{{
    itemsContainer.classList.add('collapsed');
    showMore.style.display='block';
    showMoreCount.textContent='('+(TOTAL-reveal)+' more)';
  }}
}}

showMore.addEventListener('click',()=>{{
  reveal=Math.min(reveal+STEP,TOTAL);
  updateOverflow();
}});

sortButtons.forEach(b=>b.addEventListener('click',()=>{{
  const key=b.dataset.sort;
  if(key===sortKey){{
    // Toggle direction
    sortDir=sortDir==='asc'?'desc':'asc';
  }}else{{
    sortKey=key;
    sortDir=DEFAULT_DIR[key]||'desc';
  }}
  applySort();
  updateOverflow();
}}));

search.addEventListener('input',apply);
chips.forEach(c=>c.addEventListener('click',()=>{{
  if(c.dataset.cat){{chips.forEach(x=>{{if(x.dataset.cat)x.classList.remove('active')}});c.classList.add('active');activeCat=c.dataset.cat;}}
  else if(c.dataset.sev){{if(c.classList.contains('active')){{c.classList.remove('active');activeSev=null;}}else{{chips.forEach(x=>{{if(x.dataset.sev)x.classList.remove('active')}});c.classList.add('active');activeSev=c.dataset.sev;}}}}
  apply();
}}));

document.addEventListener('keydown',e=>{{
  if(e.key==='/'&&document.activeElement!==search){{e.preventDefault();search.focus();}}
  else if(e.key==='Escape'){{
    search.value='';activeCat='all';activeSev=null;
    chips.forEach(x=>{{x.classList.remove('active');if(x.dataset.cat==='all')x.classList.add('active');}});
    sortKey='score';sortDir='desc';reveal=INITIAL;
    applySort();apply();search.blur();
  }}
}});

// Initial state
itemsContainer.dataset.sortKey='score';
updateOverflow();
</script>
</body></html>"""


def render_html(items: list[Item], n_sources: int, days: int) -> str:
    parts = []
    for i, it in enumerate(items, 1):
        try:
            dt = datetime.fromisoformat(it.published.replace("Z", "+00:00"))
            date_str = dt.strftime("%b %d")
        except Exception:
            date_str = it.published[:10]
        sev_html = ""
        if it.severity:
            cvss_str = f" {it.cvss:.1f}" if it.cvss > 0 else ""
            sev_html = f'<span class="sev sev-{escape(it.severity)}">{escape(it.severity)}{cvss_str}</span>'
        corrob_html = ""
        if it.corroboration > 1:
            corrob_html = f'<span class="corrob">×{it.corroboration} sources</span>'
        cve_html = "".join(f'<span class="cve">{escape(c)}</span>' for c in it.cves[:3])
        kw_html = "".join(f'<span class="kw">{escape(k)}</span>' for k in it.matched_keywords[:6])
        also_html = ""
        if it.other_sources:
            links = []
            for o in it.other_sources[:5]:
                src = escape(o.get("source", ""))
                href = escape(o.get("link", ""))
                cat = escape(o.get("category", ""))
                links.append(f'<a href="{href}" target="_blank" rel="noopener" class="also-link cat-{cat}">{src}</a>')
            also_html = f'<div class="also">also: {", ".join(links)}</div>'
        text_idx = (it.title + " " + it.summary + " " + " ".join(it.matched_keywords) +
                    " " + it.source + " " + " ".join(it.cves) + " " + it.severity + " " +
                    " ".join(o.get("source", "") for o in it.other_sources)).lower()
        rank_class = f"rank-{i}" if i <= 3 else ""
        overflow = "true" if i > 10 else "false"
        # Sort keys (numeric where possible so JS can sort directly)
        sev_rank = {"critical": 4, "high": 3, "medium": 2, "low": 1, "": 0}.get(it.severity, 0)
        try:
            ts_iso = datetime.fromisoformat(it.published.replace("Z", "+00:00")).timestamp()
        except Exception:
            ts_iso = 0
        parts.append(f'''<div class="item" data-cat="{escape(it.category)}" data-sev="{escape(it.severity)}" data-rank="{i}" data-overflow="{overflow}" data-score="{it.score:.4f}" data-date="{ts_iso:.0f}" data-sevrank="{sev_rank}" data-corrob="{it.corroboration}" data-source="{escape(it.source.lower())}" data-text="{escape(text_idx)}">
<div class="rank {rank_class}">{i:02d}</div>
<div class="body">
<h2><a href="{escape(it.link)}" target="_blank" rel="noopener">{escape(it.title)}</a></h2>
<div class="summary">{escape(it.summary[:280])}{"…" if len(it.summary) > 280 else ""}</div>
<div class="kws">{sev_html}{corrob_html}{cve_html}{kw_html}</div>
{also_html}
</div>
<div class="right">
<span class="src cat-{escape(it.category)}">{escape(it.source)}</span>
<span>{escape(date_str)}</span>
<span>score {it.score:.3f}</span>
</div></div>''')
    return HTML.format(
        date=datetime.now().strftime("%a %b %d %Y · %H:%M"),
        n=len(items), ns=n_sources, days=days,
        items="\n".join(parts) if parts else '<div class="empty">no items</div>',
    )


def render_md(items: list[Item], days: int) -> str:
    out = [f"# feedrank — {datetime.now():%Y-%m-%d}", "",
           f"_{len(items)} items, {days}d window._", ""]
    for i, it in enumerate(items, 1):
        try:
            dt = datetime.fromisoformat(it.published.replace("Z", "+00:00"))
            date_str = dt.strftime("%b %d")
        except Exception:
            date_str = it.published[:10]
        sev = ""
        if it.severity:
            sev = f" · **{it.severity.upper()}"
            if it.cvss > 0:
                sev += f" {it.cvss:.1f}"
            sev += "**"
        cves = " · " + ", ".join(it.cves[:3]) if it.cves else ""
        corrob = f" · ×{it.corroboration} sources" if it.corroboration > 1 else ""
        out.append(f"### {i}. [{it.title}]({it.link})")
        out.append(f"_{it.source} · {date_str} · score {it.score:.3f}{sev}{corrob}{cves}_")
        if it.summary:
            out.append("")
            out.append(it.summary[:300] + ("…" if len(it.summary) > 300 else ""))
        if it.matched_keywords:
            out.append("")
            out.append(" ".join(f"`{k}`" for k in it.matched_keywords[:5]))
        if it.other_sources:
            also = ", ".join(f"[{o.get('source','')}]({o.get('link','')})"
                             for o in it.other_sources[:5])
            out.append("")
            out.append(f"_also: {also}_")
        out.append("")
    return "\n".join(out)


def post_slack(webhook: str, items: list[Item], top: int = 10) -> None:
    blocks = [{"type": "header", "text": {"type": "plain_text", "text": f"feedrank — top {top}"}}]
    for i, it in enumerate(items[:top], 1):
        try:
            dt = datetime.fromisoformat(it.published.replace("Z", "+00:00"))
            date_str = dt.strftime("%b %d")
        except Exception:
            date_str = it.published[:10]
        blocks.append({"type": "section", "text": {"type": "mrkdwn",
            "text": f"*{i}. <{it.link}|{it.title}>*\n_{it.source} · {date_str} · score {it.score:.2f}_\n{it.summary[:240]}"}})
    payload = json.dumps({"blocks": blocks}).encode()
    req = urllib.request.Request(webhook, data=payload,
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            log.info(f"slack: {resp.status}")
    except Exception as e:
        log.error(f"slack post failed: {e}")


# ---------------------------------------------------------------------------
def main() -> int:
    here = Path(__file__).parent
    p = argparse.ArgumentParser(description="Aggregate, filter, BM25-rank security feeds")
    p.add_argument("--sources", default=str(here / "sources.toml"))
    p.add_argument("--profile", default=str(here / "profile.toml"))
    p.add_argument("--days", type=int, default=7)
    p.add_argument("--top", type=int, default=80)
    p.add_argument("--no-filter", action="store_true")
    p.add_argument("--no-cluster", action="store_true",
                   help="skip multi-source corroboration clustering")
    p.add_argument("--diagnose", action="store_true",
                   help="print per-source fetch summary and exit")
    p.add_argument("--out-dir", default=str(here / "out"))
    p.add_argument("--slack-webhook")
    p.add_argument("--max-workers", type=int, default=8)
    args = p.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(args.sources, "rb") as f:
        sources = tomllib.load(f)["source"]
    with open(args.profile, "rb") as f:
        profile = tomllib.load(f)
    topics = profile.get("interests", {}).get("topics", [])
    keywords = profile["stack"]["keywords"]
    boost_terms = profile["stack"].get("boost_terms", [])

    log.info(f"fetching {len(sources)} sources...")
    t0 = time.time()
    items = fetch_all(sources, max_workers=args.max_workers)
    log.info(f"fetched {len(items)} items in {time.time()-t0:.1f}s")

    # Per-source summary
    from collections import Counter
    by_source = Counter(it.source for it in items)
    fetched_sources = {s["name"] for s in sources if any(
        by_source[name] for name in by_source
        if name == s["name"] or name.startswith(s["name"] + " (")
    )}
    log.info("per-source fetch counts:")
    for src in sources:
        # OSV fetcher emits items with "Name (eco)" suffix; sum those too
        sname = src["name"]
        count = by_source.get(sname, 0)
        for k, c in by_source.items():
            if k != sname and k.startswith(sname + " ("):
                count += c
        marker = "  " if count > 0 else "X "
        log.info(f"  {marker}{count:4d}  {sname}")

    if args.diagnose:
        return 0

    items = [i for i in items if within_days(i, args.days)]
    log.info(f"after {args.days}d window: {len(items)}")

    if not args.no_filter:
        items = keyword_filter(items, keywords)
        log.info(f"after keyword filter: {len(items)}")

    items = dedupe(items)
    log.info(f"after dedupe: {len(items)}")

    # Enrich first so clustering has CVE info
    for it in items:
        enrich(it)

    if not args.no_cluster:
        before = len(items)
        items = cluster_and_collapse(items)
        log.info(f"after cluster: {len(items)} ({before - len(items)} merged)")

    items = rank(items, topics, boost_terms)[:args.top]
    log.info(f"top {len(items)} retained")

    (out_dir / "feedrank.html").write_text(render_html(items, len(sources), args.days))
    (out_dir / "feedrank.md").write_text(render_md(items, args.days))
    (out_dir / "feedrank.json").write_text(json.dumps([asdict(i) for i in items], indent=2))
    log.info(f"wrote {out_dir}/feedrank.{{html,md,json}}")

    if args.slack_webhook:
        post_slack(args.slack_webhook, items)

    return 0


if __name__ == "__main__":
    sys.exit(main())
