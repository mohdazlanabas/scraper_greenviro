# WTE News Scraper - Setup Guide

## Quick Start

### 1. Configure Email Recipients
```bash
cp config_files/config_emails.txt.example config_files/config_emails.txt
# Edit config_files/config_emails.txt and add your email addresses (one per line)
```

Example `config_files/config_emails.txt`:
```
manager@net1io.com
team@greenviro.com
ceo@company.com
```

### 2. Customize Keywords (Optional)
Edit `config_files/config_keywords.txt` to add or remove search keywords:
```
Waste to Energy
WTE
Biogas
Your Custom Keywords Here
```

### 3. Customize News Sources (Optional)
Edit `config_files/config_domains.txt` to add or remove Malaysian news domains:
```
thestar.com.my
theedgemalaysia.com
your-news-site.com.my
```

### 4. Local Testing

Install dependencies:
```bash
pip install -r requirements.txt
```

Set your Gmail credentials:
```bash
export EMAIL_SENDER="your-email@gmail.com"
export EMAIL_PASSWORD="your-gmail-app-password"
```

Run the scraper:
```bash
python scrapper.py
```

### 5. Deploy to GitHub Actions

#### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin your-github-repo-url
git push -u origin main
```

#### Step 2: Configure GitHub Secrets
Go to: **Your Repository → Settings → Secrets and variables → Actions**

Add these secrets:
- **EMAIL_SENDER**: Your Gmail address (e.g., `yourname@gmail.com`)
- **EMAIL_PASSWORD**: Your Gmail App Password (16 characters, see below)
- **EMAIL_RECEIVER**: Optional fallback (if config_files/config_emails.txt is empty)

#### Step 3: Get Gmail App Password
1. Enable 2-Factor Authentication: https://myaccount.google.com/security
2. Create App Password: https://myaccount.google.com/apppasswords
3. Select "Mail" and generate password
4. Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)
5. Paste this into GitHub Secrets as `EMAIL_PASSWORD`

#### Step 4: Verify Workflow
- Go to **Actions** tab in your GitHub repository
- You should see "WTE Daily Scraper" workflow
- Click "Run workflow" to test manually
- Check for any errors

### 6. Verify Automation

The scraper will run automatically at **09:00 AM Malaysia Time (01:00 UTC)** every day.

To change the schedule, edit `.github/workflows/scrapper.yml` line 5:
```yaml
- cron: '0 1 * * *'  # Change this line
```

Use https://crontab.guru to generate custom schedules.

## Configuration Files Reference

| File | Purpose | Git Tracked |
|------|---------|-------------|
| `config_files/config_keywords.txt` | Search keywords | Yes ✓ |
| `config_files/config_domains.txt` | News websites | Yes ✓ |
| `config_files/config_emails.txt` | Email recipients (sensitive) | No ✗ |
| `config_files/config_emails.txt.example` | Template for emails | Yes ✓ |

## Troubleshooting

### Email Not Sending
- Verify Gmail App Password (not regular password)
- Check 2FA is enabled on Google Account
- Verify `config_files/config_emails.txt` has valid email addresses

### No News Found
- Check keywords in `config_files/config_keywords.txt` are relevant
- Verify domains in `config_files/config_domains.txt` are active
- Try broader keywords

### GitHub Actions Failing
- Check all 3 secrets are set correctly
- Verify `config_files/config_emails.txt` exists and has valid emails
- Check workflow logs in Actions tab

## File Structure
```
scrapper_greenviro/
├── .github/
│   └── workflows/
│       └── scrapper.yml           # Automation workflow
├── scrapper.py                    # Main Python script
├── requirements.txt               # Dependencies
├── config_files/config_keywords.txt            # Search keywords (edit freely)
├── config_files/config_domains.txt             # News domains (edit freely)
├── config_files/config_emails.txt              # Email recipients (git-ignored)
├── config_files/config_emails.txt.example      # Email template
├── readme.md                      # Project overview
└── SETUP_GUIDE.md                 # This file
```

## Support

For issues or questions:
- Check the [README.md](readme.md) file
- Review GitHub Actions logs
- Verify all configuration files are properly formatted

## Next Steps

1. ✓ Configure `config_files/config_emails.txt` with your recipients
2. ✓ Customize keywords in `config_files/config_keywords.txt` if needed
3. ✓ Test locally with `python scrapper.py`
4. ✓ Push to GitHub and configure secrets
5. ✓ Test with manual workflow trigger
6. ✓ Wait for automated daily run or monitor results
