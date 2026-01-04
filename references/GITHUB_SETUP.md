# GitHub Actions Setup Guide

## Status: ✅ Workflow File Ready, ⚠️ GitHub Setup Needed

The GitHub Actions workflow is configured in `.github/workflows/scrapper.yml` but you need to push to GitHub and configure secrets.

---

## Step-by-Step Setup

### Step 1: Initialize Git Repository

```bash
cd /Users/rogerwoolie/Downloads/scrapper_greenviro
git init
git add .
git commit -m "Initial commit: WTE News Scraper"
```

---

### Step 2: Create GitHub Repository

1. Go to: https://github.com/new
2. Repository name: `wte-news-scraper` (or your choice)
3. Make it **Private** (recommended - contains email configs)
4. **DO NOT** initialize with README (we already have files)
5. Click "Create repository"

---

### Step 3: Push to GitHub

GitHub will show you commands like this:

```bash
git remote add origin https://github.com/YOUR-USERNAME/wte-news-scraper.git
git branch -M main
git push -u origin main
```

Copy and run those commands in your terminal.

---

### Step 4: Configure GitHub Secrets

1. Go to your repository on GitHub
2. Click: **Settings** → **Secrets and variables** → **Actions**
3. Click: **New repository secret**

Add these 3 secrets:

| Secret Name | Value | Where to Get It |
|-------------|-------|-----------------|
| `EMAIL_SENDER` | `azlan@net1io.com` | Your Gmail address |
| `EMAIL_PASSWORD` | `ooua thnj egoe pflm` | Your Gmail App Password |
| `EMAIL_RECEIVER` | `azlan@net1io.com` | Fallback recipient (optional) |

**Important:**
- Use your actual Gmail App Password from `config_files/config_credentials.txt`
- Keep the spaces in the password - GitHub handles them correctly

---

### Step 5: Update config_files/config_emails.txt on GitHub

Since `config_files/config_emails.txt` is git-ignored (not pushed to GitHub), you need to create it on GitHub Actions:

**Option A: Use GitHub Secrets (Recommended)**
The workflow already uses `EMAIL_RECEIVER` as fallback, so it will work.

**Option B: Create the file in GitHub**
1. In your repo, create a new file: `config_files/config_emails.txt`
2. Add: `azlan@net1io.com`
3. Commit directly to main branch

---

### Step 6: Test the Workflow

1. Go to: **Actions** tab in your GitHub repository
2. Click on: **WTE Daily Scraper**
3. Click: **Run workflow** → **Run workflow**
4. Wait 30-60 seconds
5. Check your email at `azlan@net1io.com`

---

### Step 7: Verify Daily Schedule

The workflow runs automatically at **9:00 AM Malaysia Time (1:00 AM UTC)** every day.

You can change the schedule by editing `.github/workflows/scrapper.yml` line 5:

```yaml
- cron: '0 1 * * *'  # Current: 9:00 AM MYT
```

Use https://crontab.guru to create custom schedules.

---

## What Happens on GitHub Actions

When the workflow runs:
1. ✓ Checks out your code
2. ✓ Installs Python 3.10
3. ✓ Installs dependencies (requests, beautifulsoup4, lxml)
4. ✓ Runs `python scrapper.py`
5. ✓ Uses secrets for Gmail credentials
6. ✓ Sends email to `azlan@net1io.com`

---

## Current Setup Summary

✅ **Already Configured:**
- Workflow file at `.github/workflows/scrapper.yml`
- Daily schedule at 9:00 AM MYT
- Manual trigger option
- Fixed filename (`scrapper.py` not `scraper.py`)

⚠️ **You Need to Do:**
1. Push code to GitHub
2. Configure 3 GitHub Secrets
3. Test with manual workflow run

---

## Important Notes

### Files NOT Pushed to GitHub (git-ignored):
- `config_files/config_emails.txt` - Email recipients (use GitHub Secret instead)
- `config_files/config_credentials.txt` - Gmail credentials (use GitHub Secrets instead)
- `output.txt` - Test output file

### Files Pushed to GitHub:
- `scrapper.py` - Main script
- `config_files/config_keywords.txt` - Search keywords
- `config_files/config_domains.txt` - News domains
- `.github/workflows/scrapper.yml` - GitHub Actions workflow
- All documentation files

---

## Troubleshooting

### "Authentication failed" on GitHub Actions
- Check `EMAIL_PASSWORD` secret is set correctly
- Use Gmail App Password, not regular password
- Ensure 2FA is enabled on Google account

### "No email recipients configured"
- Set `EMAIL_RECEIVER` secret in GitHub
- Or create `config_files/config_emails.txt` in the GitHub repository

### Workflow doesn't run
- Check Actions tab is enabled in repository settings
- Verify secrets are set correctly
- Check workflow file syntax

---

## Quick Commands

```bash
# Initialize and push to GitHub
git init
git add .
git commit -m "Initial commit: WTE News Scraper"
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git push -u origin main

# Update after making changes
git add .
git commit -m "Update configuration"
git push
```

---

## Next Steps

1. [ ] Push code to GitHub (see Step 1-3 above)
2. [ ] Configure GitHub Secrets (see Step 4)
3. [ ] Run manual test (see Step 6)
4. [ ] Wait for daily automated run at 9:00 AM MYT
5. [ ] Check email inbox for WTE news digest

---

**Ready to deploy?** Follow Steps 1-6 above to get your automated daily WTE news emails running!
