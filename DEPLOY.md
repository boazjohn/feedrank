# Deploying feedrank to GitHub Pages

`.github/workflows/feedrank.yml` runs feedrank on a schedule and publishes the dashboard to GitHub Pages. End state: a URL like `https://<you>.github.io/feedrank/` that auto-refreshes.

## Setup

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "feedrank: initial"
git remote add origin git@github.com:<you>/feedrank.git
git branch -M main
git push -u origin main
```

### 2. Enable GitHub Pages

Repo → **Settings** → **Pages**:

- **Source**: Deploy from a branch
- **Branch**: `gh-pages` (will be created by the first workflow run)
- **Folder**: `/ (root)`

### 3. Add a GHSA token (optional)

Lifts the GHSA REST API rate limit from 60/hr to 5,000/hr.

Create a fine-grained PAT (account → Developer settings → Personal access tokens → Fine-grained), with **Public Repositories (read-only)** access — no extra scopes needed.

Add it to the repo: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**, name `GH_TOKEN`. The workflow already references `${{ secrets.GH_TOKEN }}`.

### 4. Trigger the first run

Push a commit, or **Actions** → **feedrank** → **Run workflow**. Takes ~30–60s. The `gh-pages` branch is created on first run.

### 5. Visit the URL

After 1–2 minutes: `https://<your-username>.github.io/<your-repo-name>/`.

## Customizing the schedule

Default: every 6 hours at :15, with `--days 5`. Edit `.github/workflows/feedrank.yml`:

```yaml
schedule:
  - cron: '15 */6 * * *'     # every 6 hours (default)
  - cron: '0 2 * * *'        # daily at 02:00 UTC
  - cron: '0 9 * * 1-5'      # weekdays at 09:00 UTC
```

GitHub's cron has 5–15 min jitter and occasionally drops runs.

## Cost

Public repo: **$0**. GitHub Actions has no monthly minute cap on public repos, and feedrank uses ~150 minutes/month. Pages bandwidth (100 GB/month) and site size (1 GB) are far beyond what a ~150 KB dashboard needs.

Private repo: 2,000 free Actions minutes/month on GitHub Free, 3,000 on Pro. Still well under the cap.

## Making it private

- **Private repo + Pages.** Requires GitHub Pro ($4/month). Anyone with repo read access sees the page.
- **Public repo + Cloudflare Access.** Free up to 50 users. Add the Pages site as a custom domain, then create a Zero Trust → Access self-hosted application with a policy allowing your email.

## Troubleshooting

- **`permission denied` on push to gh-pages** — Settings → Actions → General → Workflow permissions → "Read and write" → Save.
- **`gh-pages` exists but Pages 404s** — wait 2 minutes; recheck Settings → Pages source.
- **Dashboard shows old data** — browser cache. Hard reload, or check the "generated" timestamp.
- **GHSA returning 0 items** — rate limit. Add `GH_TOKEN`.
- **One feed always fails** — `python feedrank.py --diagnose` shows per-source counts; fix or drop in `sources.toml`.

Local runs (`python feedrank.py --days 7`) still work for debugging before pushing.
