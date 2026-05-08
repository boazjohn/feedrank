# feedrank

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

Aggregates 30 verified supply-chain & infra security feeds, filters by your stack keywords, **clusters multi-source reports of the same incident**, ranks with **BM25** against your interest profile (with severity, recency, corroboration, and source weight multipliers), and renders an HTML dashboard.

One Python file. **One dependency** (`feedparser`). Pure Python BM25, no numpy, no compiled extensions, no `libstdc++` issues. Works in Nix shells, Lima VMs, and other minimal environments.

## Install

Requires Python 3.11+ for stdlib `tomllib`.

### Standard

```bash
cd feedrank
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Nix shell

```bash
nix shell nixpkgs#python313 nixpkgs#python313Packages.feedparser
python feedrank.py --days 7 --no-filter
```

That's it — no pip, no venv. `feedparser` is in nixpkgs.

### Nix flake / shell.nix

```nix
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    (pkgs.python313.withPackages (ps: [ ps.feedparser ]))
  ];
}
```

## Run

```bash
python feedrank.py --days 7 --no-filter   # first run, see everything
open out/feedrank.html
```

Then tune `profile.toml` based on what you saw, and run filtered:

```bash
python feedrank.py --days 7
```

## Flags

```
--days N             window in days (default 7)
--top N              keep top N items (default 80)
--no-filter          skip keyword filter
--no-cluster         skip multi-source corroboration clustering
--diagnose           print per-source fetch summary and exit
--slack-webhook URL  POST top 10 to Slack
--out-dir PATH       output directory (default ./out)
```

The normal run also prints per-source fetch counts at the start. Sources marked `X` returned zero items — either dead URL, rate-limited, or no items in the window. Drop or fix them in `sources.toml`.

## How ranking works

```
score = base × recency × source_weight × severity × corroboration

where base depends on BM25 match strength:
  bm25 > 0.1                              → base = bm25
  bm25 ≤ 0.1 but critical/high or ×2+     → base = max(bm25, 0.15)
  otherwise (off-topic, low-sev, single)  → base = 0.01 (buried)
```

- **BM25 against `interests.topics`** — each topic in `profile.toml` is a separate query; an item's BM25 score is the max across all topics. Title is weighted 3× by repetition (standard IR trick).
- **Boost terms** — items containing tokens in `stack.boost_terms` get an additive bonus.
- **Recency** — linear decay 1.0 → 0.3 over 14 days.
- **Source weight** — from `sources.toml`. GHSA sources default to 0.55 (high volume, low signal); vendor research like Wiz/Socket/StepSecurity default 1.1–1.3.
- **Severity** — 1.0–1.95 multiplier from CVSS or inferred severity (critical/high/medium/low). Heuristic catches "credential stealer", "compromised on", "backdoored", "self-propagating worm" etc. when explicit CVSS is missing.
- **Corroboration** — multi-source clusters get 1.0× to 1.55× bonus (1 source → 1.0×, 2 → 1.28×, 3 → 1.44×, 4 → 1.55×).

CVE IDs are extracted via regex. Severity comes from GHSA when available, otherwise inferred from explicit phrases.

The tokenizer handles security-specific patterns: keeps `CVE-2026-12345`, `intercom-client`, `@sap/cds`, `k8s`, and `ci/cd` as single tokens.

## Clustering

Two items are merged into one cluster if any of these match:

1. They share a CVE ID.
2. They share a distinctive token: campaign names (`shai-hulud`), specific packages (`intercom-client`, `pytorch-lightning`, `bitwarden-cli`), known IOCs (`masscan.cloud`).
3. The "lightning incident" heuristic — bare `lightning` paired with words like `compromise`, `backdoor`, `stealer`, `wave`, `2.6.x`.

When merged, one item becomes the representative (highest source weight → advisory > research > government > build > aggregator → most recent). Other items appear as "also covered by" links underneath. CVE lists and severity merge across the cluster — the rep gets the union of CVEs and the highest CVSS.

## Configuration

**`sources.toml`** — 30 verified feed URLs. Each entry: `name`, `url`, `category`, `weight`. Three special schemes:

- `ghsa-api://<ecosystem>` — GitHub Advisory REST API. Unauthenticated 60/hr. Set `GH_TOKEN` env var (no special scopes needed) for 5,000/hr.
- `kev-api://recent` — CISA Known Exploited Vulnerabilities. Every entry treated as critical (KEV = actively exploited).
- `osv-api://recent` — OSV.dev (currently disabled; GHSA ecosystems above cover what it would provide).

**`profile.toml`** has three sections:

- `interests.topics` — one sentence per topic, written with distinctive vocabulary you want surfaced. BM25 query input.
- `stack.keywords` — substrings for the hard filter. Edit this first if results feel off.
- `stack.boost_terms` — additional BM25 boost.

The shipped `profile.toml` is organized around **incident patterns** rather than product names — 10 topic queries covering: supply chain compromise, cloud misconfiguration, identity/auth bypass, exploits in the wild, ransomware/breach, hypervisor/container escape, infrastructure runtime CVEs, CI/CD abuse, DDoS/availability, and vendor advisories. Pattern vocabulary tends to appear in actual reporting, so BM25 ranks well even for products you never explicitly listed. The keyword filter is broader (~255 terms covering AWS/GCP/Azure, Linux/Windows/macOS, common languages, databases, identity providers, virtualization, private cloud, network appliances, observability) so legitimate items aren't dropped just because the topic line didn't mention a specific product.

Customize freely — copy to `profile.local.toml` and edit there if you want to keep your tuning out of git.

### Customizing for your stack (without leaking it to git)

If you want to keep your real interests/stack details out of a public repo, copy the example to a local override:

```bash
cp profile.toml profile.local.toml
$EDITOR profile.local.toml          # add your specific tools, threats, package names
python feedrank.py --profile profile.local.toml --days 7
```

`profile.local.toml` is in `.gitignore` and won't be committed. Same pattern works for `sources.local.toml` if you have private internal feeds you don't want public.

### Sources status

Several sources from earlier versions were dropped because their RSS endpoints 404'd or returned 0 items in real testing. They're commented out in `sources.toml` with notes:

- **404 — URL changed**: Sigstore (still missing)
- **0 items / wrong content**: Semgrep, CyberWire Daily, CERT-IN
- **API limitation**: OSV.dev (requires per-package queries, redundant with GHSA)

PRs adding working URLs welcome.

## Deploy

For free auto-running every 6 hours on GitHub Actions + GitHub Pages, see [DEPLOY.md](DEPLOY.md). Cost on a public repo: $0/month.

For local cron:

```cron
0 7 * * * cd ~/feedrank && .venv/bin/python feedrank.py --slack-webhook $SLACK_URL >> /tmp/feedrank.log 2>&1
```

## When something breaks

- Feed returns 404/timeout → script logs `fetch fail [name]: ...` and continues. Edit `sources.toml`.
- Empty output → run with `--no-filter --days 14`. If still empty, network issue. If items appear, your keyword filter is too narrow.
- GHSA returns 403 → rate limit. Set `GH_TOKEN` env var.
- Ranking feels off → check `bm25` score in the HTML right column. If your top items have low BM25, your topics in `profile.toml` don't match the actual feed vocabulary. Edit them.

## Files

```
feedrank/
├── feedrank.py             # ~900 lines, single file, pure Python BM25
├── sources.toml            # 30 verified feed URLs
├── profile.toml            # generic example interests + keywords
├── profile.local.toml      # your customized profile (gitignored, optional)
├── requirements.txt        # one line: feedparser
├── .github/workflows/      # daily run + GitHub Pages deploy
├── README.md
├── DEPLOY.md               # GitHub Pages setup
├── CONTRIBUTING.md
└── LICENSE                 # MIT
```

## Acknowledgments

feedrank reads RSS/Atom from public feeds published by these organizations and projects. Their work is the substance — feedrank is just an aggregator. If you find an item useful, click through and support the original authors:

**Vulnerability databases**: GitHub Advisory Database, CISA Known Exploited Vulnerabilities, CISA Advisories, RustSec, OpenSSF Malicious Packages, PyPA Security Announcements

**Vendor research**: Wiz, Aqua Nautilus, Sysdig, Datadog Security Labs, ReversingLabs, Snyk, JFrog Security Research, Checkmarx Zero, OX Security, Veracode (Phylum), StepSecurity, Endor Labs, Socket

**Aggregators**: Risky Business News, tl;dr sec, Detection Engineering Weekly, The Hacker News, BleepingComputer

**Build / CI**: GitHub Security Blog, GitHub Changelog

Built with [`feedparser`](https://github.com/kurtmckee/feedparser) (BSD-2-Clause) by Kurt McKee. Display fonts are [Inter](https://rsms.me/inter/), [Recursive](https://www.recursive.design/), [Fraunces](https://fonts.google.com/specimen/Fraunces), and [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) — all open licenses.

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Especially helpful: working URLs for sources currently disabled, better topic vocabulary for `profile.toml`, new distinctive-token patterns for the corroboration clusterer.

## License

MIT — see [LICENSE](LICENSE).

This project aggregates publicly-syndicated RSS/Atom content. It shows item titles, short excerpts (≤280 characters), and links back to the original sources. This is consistent with how RSS is intended to be consumed and falls within standard fair-use aggregation. If you publish a feed and would prefer feedrank not include it, open an issue and we'll remove it.
