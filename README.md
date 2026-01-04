# WTE Malaysia News Scraper

Daily automated news aggregator for Waste-to-Energy and Green Energy sectors in Malaysia.

## 🚀 Quick Start

### 1. Edit Configuration Files

```bash
# Edit your Gmail credentials
nano config_files/config_credentials.txt

# Edit email recipients
nano config_files/config_emails.txt
```

### 2. Test It

```bash
# Test mode (creates output.txt, no email sent)
python3 scrapper.py -test

# Production mode (sends real email)
python3 scrapper.py
```

That's it! ✅

---

## 📁 Project Structure

```
scrapper_greenviro/
├── scrapper.py                  # Main script
├── requirements.txt             # Python dependencies
├── output.txt                   # Test results (generated)
├── config_files/               # ⚙️ All configuration files
│   ├── config_credentials.txt  # Gmail login (EDIT THIS)
│   ├── config_emails.txt       # Email recipients (EDIT THIS)
│   ├── config_keywords.txt     # Search keywords
│   ├── config_domains.txt      # News sources
│   └── *.example               # Example templates
├── references/                 # 📚 All documentation
│   ├── HOW_TO_RUN.md          # Simple 3-step guide
│   ├── quick_start.md         # Quick reference
│   ├── GITHUB_SETUP.md        # GitHub Actions setup
│   └── readme.md              # Full project docs
└── .github/workflows/          # GitHub Actions automation
    └── scrapper.yml           # Daily automation workflow
```

---

## ⚙️ Configuration

All settings are in the `config_files/` folder:

| File | Purpose | Required |
|------|---------|----------|
| `config_credentials.txt` | Gmail login credentials | ✅ Yes |
| `config_emails.txt` | Email recipients | ✅ Yes |
| `config_keywords.txt` | Search keywords | Optional |
| `config_domains.txt` | News domains | Optional |

See [config_files/README.md](config_files/README.md) for details.

---

## 📧 Features

- ✅ Searches 12 major Malaysian newspapers
- ✅ Filters for WTE-related keywords
- ✅ Sends formatted HTML email digest
- ✅ Daily automation via GitHub Actions (9:00 AM MYT)
- ✅ Test mode for safe testing
- ✅ Easy configuration with separate files

---

## 📖 Documentation

- **First time setup:** [references/HOW_TO_RUN.md](references/HOW_TO_RUN.md)
- **Quick reference:** [references/quick_start.md](references/quick_start.md)
- **GitHub automation:** [references/GITHUB_SETUP.md](references/GITHUB_SETUP.md)
- **Full docs:** [references/readme.md](references/readme.md)

---

## 🔧 Requirements

- Python 3.9+
- Gmail account with App Password
- (Optional) GitHub account for automation

---

## 📝 Commands

```bash
# Test mode (no email sent)
python3 scrapper.py -test

# Production mode (sends email)
python3 scrapper.py

# View test results
cat output.txt
```

---

## 🤝 Support

- Check documentation in `references/` folder
- Review `output.txt` for test results
- See GitHub Actions logs for automation issues

---

**Repository:** https://github.com/mohdazlanabas/scraper_greenviro
