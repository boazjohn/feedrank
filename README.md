# feedrank

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

Aggregates 30 supply-chain and infra security feeds, clusters multi-source reports of the same incident, ranks with BM25 against your interest profile, and renders an HTML dashboard.

One Python file, one dependency (`feedparser`). Pure Python BM25 — no numpy, no compiled extensions.

## Install

Requires Python 3.11+ for stdlib `tomllib`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Or with Nix: `nix shell nixpkgs#python313 nixpkgs#python313Packages.feedparser`.

## Run

```bash
python feedrank.py --days 7 --no-filter   # first run, see everything
open out/feedrank.html
```

Tune `profile.toml` based on what you saw, then run filtered:

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

## Ranking

```
score = base × recency × source_weight × severity × corroboration

base:
  bm25 > 0.1                              → bm25
  bm25 ≤ 0.1 but critical/high or ×2+     → max(bm25, 0.15)
  otherwise                               → 0.01 (buried)
```

- **BM25** against each topic in `profile.toml`; item score is the max across topics. Title weighted 3×.
- **Recency** — linear decay 1.0 → 0.3 over 14 days.
- **Source weight** — from `sources.toml`. GHSA defaults 0.55; vendor research 1.1–1.3.
- **Severity** — 1.0–1.95× from CVSS or inferred from phrases like "credential stealer", "backdoored".
- **Corroboration** — 1.0× / 1.28× / 1.44× / 1.55× for 1/2/3/4 sources.

The tokenizer keeps security-specific patterns intact: `CVE-2026-12345`, `intercom-client`, `@sap/cds`, `k8s`, `ci/cd`.

## Clustering

Items merge into one cluster if they share a CVE ID, a distinctive token (campaign names, package names, IOCs), or match the "lightning incident" heuristic. The highest-weight source becomes the representative; others appear as "also covered by" links. CVE lists and severity merge across the cluster.

## Configuration

**`sources.toml`** — feed URLs with `name`, `url`, `category`, `weight`. Three special schemes:

- `ghsa-api://<ecosystem>` — GitHub Advisory REST API. Set `GH_TOKEN` for 5,000/hr instead of 60/hr.
- `kev-api://recent` — CISA Known Exploited Vulnerabilities (treated as critical).
- `osv-api://recent` — OSV.dev (disabled; redundant with GHSA).

**`profile.toml`** has three sections:

- `interests.topics` — one sentence per topic. BM25 query input.
- `stack.keywords` — substrings for the hard filter.
- `stack.boost_terms` — additive BM25 boost.

To keep your real stack out of git, copy to `profile.local.toml` (gitignored) and run with `--profile profile.local.toml`.

## Deploy

GitHub Actions + GitHub Pages every 6 hours, $0 on public repos — see [DEPLOY.md](DEPLOY.md).

Local cron:

```cron
0 7 * * * cd ~/feedrank && .venv/bin/python feedrank.py --slack-webhook $SLACK_URL >> /tmp/feedrank.log 2>&1
```

## Troubleshooting

- **Feed 404/timeout** — script logs and continues. Edit `sources.toml`.
- **Empty output** — try `--no-filter --days 14`. If still empty, network issue; otherwise your keyword filter is too narrow.
- **GHSA 403** — rate limit. Set `GH_TOKEN`.
- **Ranking feels off** — check `bm25` in the HTML right column. Low scores mean your topics don't match feed vocabulary.

## Acknowledgments

feedrank reads public RSS/Atom feeds — the vulnerability databases, vendor research teams, and aggregators publishing them are the substance. Click through and support the original authors.

Built with [`feedparser`](https://github.com/kurtmckee/feedparser) by Kurt McKee.

## License

MIT — see [LICENSE](LICENSE). Contributions welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).

This project aggregates publicly-syndicated content, showing titles, short excerpts (≤280 chars), and links back to the source. If you publish a feed and would prefer it not be included, open an issue.
