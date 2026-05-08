# Contributing to feedrank

## What's welcome

- **New source feeds** — verified RSS/Atom URLs not already in `sources.toml`. Include a note on why the source is high-signal and confirm the URL works.
- **Better topic vocabulary** — phrasings in `profile.toml` that surface relevant results better.
- **Clustering improvements** — new distinctive-token patterns in `cluster_and_collapse` for active campaigns.
- **Bug fixes.**
- **Documentation** — README clarity, deployment guides for hosts other than GitHub Pages.

## What's not

- Replacing stdlib functionality with a new dependency. The point of the project is one file, one dep.
- Heavy dependencies (numpy, pandas, sentence-transformers). Pure-Python BM25 is a deliberate choice for minimal-environment installs.

## Reporting issues

Include:

1. Output of `python feedrank.py --diagnose`.
2. The exact command and error.
3. `python --version` and OS.

For ranking complaints, include `bm25` and `score` from the JSON output. Most ranking issues are fixable in `profile.toml`, not code.

## Development

```bash
git clone https://github.com/<you>/feedrank.git
cd feedrank
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python feedrank.py --days 7 --no-filter
```

`feedrank.py` is one file (~900 lines): BM25 class, fetchers (RSS/GHSA/KEV), tokenization and severity, clustering, ranking, renderers (HTML/Markdown/JSON), CLI.

No tests yet. If you change ranking, run before/after on real data and include the comparison in the PR.

## Code style

- Match existing style: type hints, dataclasses.
- Keep dependencies at one (`feedparser`).
- HTML/CSS lives inline as f-strings — keeping the project to one file makes deploys trivial.

## License

By contributing, you agree your contributions will be licensed under MIT (see `LICENSE`).
