# Configuration Files

This folder contains all configuration files for the WTE News Scraper.

## Files You Need to Edit

### 1. config_credentials.txt
**Your Gmail login credentials**
- Edit this file with your Gmail address and App Password
- See: `config_credentials.txt.example` for template

### 2. config_emails.txt
**Email recipients who will receive the daily digest**
- Add one email per line
- See: `config_emails.txt.example` for template

## Files You Can Customize

### 3. config_keywords.txt
**Search keywords for finding WTE news**
- Current keywords: Waste to Energy, WTE, Biogas, Biomass, etc.
- Add or remove keywords as needed
- One keyword per line

### 4. config_domains.txt
**Malaysian news websites to search**
- Current: 12 major Malaysian newspapers
- Add or remove news domains
- One domain per line (e.g., thestar.com.my)

## Notes

- Lines starting with `#` are comments and will be ignored
- `config_credentials.txt` and `config_emails.txt` are git-ignored (won't be pushed to GitHub)
- Example files (*.example) are safe to commit to git
