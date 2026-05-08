# Deploying feedrank to GitHub Pages

The included `.github/workflows/feedrank.yml` runs feedrank daily on GitHub-hosted runners and publishes the dashboard to GitHub Pages. Free, no infra to maintain.

End state: a URL like `https://<you>.github.io/feedrank/` that auto-refreshes every morning.

---

## Setup

### 1. Push to GitHub

```bash
cd feedrank
git init
git add .
git commit -m "feedrank: initial"

# Create an empty repo on github.com first (private is fine), then:
git remote add origin git@github.com:<you>/feedrank.git
git branch -M main
git push -u origin main
```

### 2. Enable GitHub Pages

Repo → **Settings** → **Pages**:

- **Source**: Deploy from a branch
- **Branch**: `gh-pages` (this branch doesn't exist yet — that's fine, the first workflow run will create it)
- **Folder**: `/ (root)`
- Save

### 3. Add the GHSA token (optional but recommended)

Without a token the GHSA REST API is rate-limited to 60 requests/hour, which is fine for one daily run but tight if you trigger manually. With a token: 5,000/hour.

Create a fine-grained PAT:

- GitHub → **Settings** (your account, not the repo) → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**
- Name: `feedrank GHSA`
- Resource owner: yourself
- Repository access: **Public Repositories (read-only)** is enough
- Permissions: leave all defaults (no extra scopes needed for read-only public advisory access)
- Expiration: 1 year is reasonable
- Generate, copy the token

Add it to the repo:

- Repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
- Name: `GH_TOKEN`
- Value: paste the token
- Add

The workflow already references `${{ secrets.GH_TOKEN }}` — if the secret isn't set, the run still works but stays on the unauthenticated rate limit.

You also need to teach feedrank to use the token. One-line edit in `feedrank.py`, in `fetch_ghsa_api`:

```python
def fetch_ghsa_api(ecosystem: str, source: dict, timeout: int) -> list[Item]:
    name = source["name"]
    api_url = f"https://api.github.com/advisories?ecosystem={ecosystem}&per_page=50"
    headers = {
        "User-Agent": "feedrank/1.0",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    # Use GH_TOKEN if present (lifts rate limit from 60/hr to 5000/hr)
    import os
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
    ...
```

(The current zip already does this — see `fetch_ghsa_api` and the `Authorization` line.)

### 4. Trigger the first run

Either push a commit (any change to `feedrank.py`/`sources.toml`/`profile.toml` triggers it via the `paths:` filter), or:

- Repo → **Actions** → **feedrank** → **Run workflow** → **Run workflow**

Watch the run complete (~30-60 seconds depending on feed response times). When it finishes, the `gh-pages` branch will have been created with `feedrank.html`, `feedrank.md`, `feedrank.json`, and `index.html`.

### 5. Visit the URL

After 1-2 minutes (Pages publish takes a moment), your dashboard is live at:

```
https://<your-username>.github.io/<your-repo-name>/
```

Bookmark it.

---

## Customizing the schedule

Default: every 6 hours at :15 past, with `--days 5` (fetch the last 5 days). Edit the `cron:` and the `--days` value in `.github/workflows/feedrank.yml` to change either:

```yaml
schedule:
  - cron: '15 */6 * * *'     # every 6 hours at :15 past (current default)
  - cron: '0 2 * * *'        # daily at 02:00 UTC
  - cron: '0 9 * * 1-5'      # weekdays at 09:00 UTC
```

```yaml
run: python feedrank.py --days 5    # current default
run: python feedrank.py --days 7    # week's window
run: python feedrank.py --days 1    # last 24h only
```

GitHub's cron has 5–15 min of jitter and occasionally drops runs during peak traffic. Don't rely on exact timing.

For **IST (Bengaluru, UTC+5:30)**: the four daily runs at `15 0/6 * * *` UTC fire at 05:45, 11:45, 17:45, and 23:45 IST.

---

## Cost

**Public repo: free, no caps that matter for this workload.** All numbers below are from GitHub's official documentation as of this writing.

**GitHub Actions** — public repos use standard GitHub-hosted runners for free with no monthly minute cap. (Private repos are limited: 2,000 free minutes/month on GitHub Free, 3,000 on Pro.) feedrank takes 30–90 seconds per run; at four runs per day that's roughly 4–6 minutes per day, ~150 minutes per month. Even on the private-repo free tier you'd use under 8% of your quota.

**GitHub Pages** — free for public repos. Soft limits:

- **Bandwidth**: 100 GB/month. Your dashboard is ~150 KB. You'd need 660,000+ daily views to hit this.
- **Site size**: 1 GB max. Yours will be a few hundred KB.
- **Builds**: 10/hour. Doesn't apply when you deploy via custom Actions workflow (which is what we're doing). Even if it did, four runs/day is a tenth of that.
- **Deploy timeout**: 10 minutes. Yours runs in under 90 seconds.

**Storage** — Actions artifact storage costs apply only to private repos. Not relevant here.

**Practical bottom line for a public repo**: $0/month with realistic headroom for 100× your actual usage.

**Where you'd actually pay something:**

- Make the repo private and exceed 2,000 minutes/month (you won't with this workload)
- Use Cloudflare Access in front of the Pages site for auth (free for up to 50 users)
- Buy a custom domain ($10–15/year, optional)
- Hit the bandwidth ceiling because your dashboard went viral (hasn't happened to anyone running an internal security feed)

---

## Making it private

By default the dashboard is public. For private viewing:

**Option A — Private repo + Pages with Pro account.** GitHub Pages on private repos requires GitHub Pro ($4/month). Anyone with read access to the repo sees the page.

**Option B — Public repo, Cloudflare Access in front.** Free up to 50 users.

1. Add the GitHub Pages site as a custom domain you own (e.g. `feedrank.<yourdomain>`)
2. Cloudflare → **Zero Trust** → **Access** → **Applications** → **Add an application** → **Self-hosted**
3. Application domain: `feedrank.<yourdomain>`
4. Add a policy allowing your email address
5. Save

Visitors hit a Cloudflare Access login page first, then see your dashboard.

**Option C — Use a private gist instead of Pages.** The workflow can post `feedrank.md` to a secret gist. Less polished but truly private with zero auth setup. Ask if you want this version of the workflow.

---

## Troubleshooting

**Workflow run failed with `permission denied` on push to gh-pages**

Repo → Settings → Actions → General → Workflow permissions → "Read and write permissions" → Save. Re-run.

**`gh-pages` branch created but Pages shows 404**

Wait 2 minutes after the first deploy. If still 404, recheck Settings → Pages → confirm Source is "Deploy from a branch" and Branch is `gh-pages` / `/ (root)`.

**Dashboard shows old data**

Browser cache. Hard reload (Cmd-Shift-R / Ctrl-Shift-R), or check the "generated" timestamp in the dashboard header to confirm the workflow ran.

**GHSA returning 0 items**

Probably hit the unauthenticated rate limit. Add the `GH_TOKEN` secret per step 3.

**One specific feed always fails**

Run `python feedrank.py --diagnose` locally to see per-source counts. Edit `sources.toml` to drop or fix the dead URL.

---

## Manual local run still works

The workflow doesn't replace local runs — `python feedrank.py --days 7` still works on your laptop, writing to `out/`. Useful for debugging before pushing changes.
