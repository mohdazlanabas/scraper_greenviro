# WTE Malaysia News Scraper

Daily automated news aggregator for Waste-to-Energy and Green Energy sectors in Malaysia.

## Key Features
- **Custom Header**: Daily WTE News By net1io.com. [Day, Date]
- **Recipients**: Configured via `config_emails.txt`
- **Keywords**: Fully customizable via `config_keywords.txt`
- **News Sources**: 12 major Malaysian newspapers (configurable via `config_domains.txt`)
- **Email Format**: Clean HTML format with headlines, links, and publication dates

## Configuration Files

All settings can be easily edited through configuration files:

### 1. Email Recipients (`config_emails.txt`)
Add recipient email addresses (one per line):
```
john@net1io.com
jane@greenviro.com
management@company.com
```

### 2. Keywords (`config_keywords.txt`)
Customize search keywords (one per line):
```
Waste to Energy
WTE
Biogas
Biomass
Greenviro
KPKT
```

### 3. News Domains (`config_domains.txt`)
List of Malaysian news websites to search (one per line):
```
thestar.com.my
theedgemalaysia.com
bernama.com
```

Lines starting with `#` are treated as comments in all config files.

## Setup Instructions

### Local Testing
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure email recipients:
   ```bash
   cp config_emails.txt.example config_emails.txt
   # Edit config_emails.txt and add your email addresses
   ```

3. Set environment variables:
   ```bash
   export EMAIL_SENDER="your-email@gmail.com"
   export EMAIL_PASSWORD="your-app-password"
   ```

4. Run the scraper:
   ```bash
   python scrapper.py
   ```

### GitHub Actions Deployment

1. Push this repository to GitHub

2. Configure GitHub Secrets (Settings → Secrets and variables → Actions):
   - `EMAIL_SENDER`: Your Gmail address
   - `EMAIL_PASSWORD`: Gmail App Password (see below)
   - `EMAIL_RECEIVER`: Fallback email (optional if using config_emails.txt)

3. Ensure `config_emails.txt` is populated with recipient addresses

4. The workflow will run automatically at 09:00 MYT (01:00 UTC) daily

### Getting Gmail App Password

1. Enable 2-Factor Authentication on your Google Account
2. Go to: https://myaccount.google.com/apppasswords
3. Generate an "App Password" for "Mail"
4. Use this 16-character password (not your regular Gmail password)

## Automation
- Powered by **GitHub Actions**
- Scans 12 major Malaysian news domains daily
- Sends formatted HTML emails at 09:00 MYT (01:00 UTC)
- Manual trigger available for testing

## File Structure
```
.
├── .github/
│   └── workflows/
│       └── scrapper.yml          # GitHub Actions workflow
├── scrapper.py                   # Main scraper script
├── requirements.txt              # Python dependencies
├── config_keywords.txt           # Search keywords (editable)
├── config_domains.txt            # News domains (editable)
├── config_emails.txt             # Email recipients (editable, git-ignored)
├── config_emails.txt.example     # Template for email config
└── readme.md                     # This file
```
