# Contributing to feedrank

Thanks for considering a contribution. Some notes on what's welcome and how to navigate the codebase.

## What's welcome

- **New source feeds** — verified working RSS/Atom URLs for security research blogs, advisory databases, or aggregators not currently in `sources.toml`. PRs should include a brief note on why the source is high-signal and a confirmation the URL has been tested.
- **Better topic vocabulary** — the BM25 ranking is only as good as the topic descriptions in `profile.toml`. If you find a phrasing that surfaces relevant results better, send the diff.
- **Clustering improvements** — the distinctive-token regex in `cluster_and_collapse` catches active campaigns; new ones (Mini Shai-Hulud, intercom-client, Bitwarden CLI hijack, etc.) get added there.
- **Bug fixes** — see "Reporting issues" below.
- **Documentation** — README clarity, examples, deployment guides for hosts other than GitHub Pages (e.g. Cloudflare Pages, Vercel).

## What's not

- Pulls that add a single dependency to do something stdlib already handles. The whole point of this project is one Python file with one dep.
- Adding heavy dependencies (numpy, pandas, sentence-transformers, etc.). The pure-Python BM25 was a deliberate choice and reverting that would break Nix/minimal-environment installs.
- Twitter/X-only sources that require API keys or third-party bridges. Bluesky and Mastodon RSS feeds are fine.

## Reporting issues

If something's broken, please include:

1. The output of `python feedrank.py --diagnose` (so the maintainers can see which sources work in your environment).
2. The exact command you ran and the error message.
3. Your Python version (`python --version`) and OS.

For ranking complaints ("X should be higher / Y should be lower"), include the relevant items' `bm25` and `score` from the JSON output. Most ranking issues are fixable by tweaking `profile.toml`, not the code.

## Development

```bash
git clone https://github.com/<you>/feedrank.git
cd feedrank
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python feedrank.py --days 7 --no-filter
```

The codebase is one file (`feedrank.py`, ~900 lines) organized roughly as:

1. `BM25` class — pure-Python Okapi BM25
2. Fetchers — RSS, GHSA REST, CISA KEV JSON, OSV (disabled)
3. Tokenization, severity inference, deduplication
4. Clustering (`cluster_and_collapse`)
5. Ranking (`rank`)
6. HTML / Markdown / JSON renderers
7. CLI (`main`)

No tests are included currently. If you change ranking behavior, please run before/after on real data and include the comparison in the PR description.

## Code style

- Match the existing style: type hints, dataclasses, no abbreviations except where standard (`re`, `cf`).
- Keep the dependency footprint at one (`feedparser`). Pure-Python only.
- HTML/CSS lives inline in `feedrank.py` as f-strings. This is intentional — keeping the project to one Python file means deploys are trivial.

## License

By contributing, you agree your contributions will be licensed under the MIT License (see `LICENSE`).
