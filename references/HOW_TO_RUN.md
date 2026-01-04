# How to Run the WTE News Scraper

## Simple 3-Step Setup

### Step 1: Edit Your Gmail Credentials

Open and edit this file:
```
config_files/config_credentials.txt
```

Change these two lines:
```
EMAIL_SENDER=your-email@gmail.com          ← Put your Gmail here
EMAIL_PASSWORD=your-16-char-app-password   ← Put your App Password here
```

**Where to get Gmail App Password:**
1. Go to: https://myaccount.google.com/apppasswords
2. Create an App Password for "Mail"
3. Copy the 16-character password
4. Paste it in config_files/config_credentials.txt

---

### Step 2: Test It (Without Sending Email)

Run this command:
```bash
python3 scrapper.py -test
```

This will create `output.txt` showing what articles were found.
No email will be sent.

---

### Step 3: Send Real Email

After testing looks good, run:
```bash
python3 scrapper.py
```

This will send the email to: `azlan@net1io.com`

---

## That's It!

You only need to edit `config_files/config_credentials.txt` once.
After that, just run `python3 scrapper.py` anytime to send the latest WTE news.

---

## Configuration Files You Can Edit

All config files are in the `config_files/` folder:

| File | What It Does |
|------|--------------|
| **config_files/config_credentials.txt** | Your Gmail login info |
| **config_files/config_emails.txt** | Who receives the email |
| **config_files/config_keywords.txt** | What news topics to search for |
| **config_files/config_domains.txt** | Which news websites to search |

All files support comments starting with `#`

---

## Troubleshooting

**"Authentication failed"**
- Use Gmail App Password, not your regular password
- Make sure 2FA is enabled on your Google account

**"No email recipients configured"**
- Check `config_files/config_emails.txt` has valid email (no # at start)

**"Credentials not configured"**
- Edit `config_files/config_credentials.txt` with your real Gmail details
- Make sure format is: `KEY=VALUE` (no spaces around =)

---

## Commands Quick Reference

```bash
# Test mode (creates output.txt, no email sent)
python3 scrapper.py -test

# Production mode (sends real email)
python3 scrapper.py

# View test results
cat output.txt
```
