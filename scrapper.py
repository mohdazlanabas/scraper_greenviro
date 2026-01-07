import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import sys
from datetime import datetime, timedelta

# --- HELPER FUNCTIONS ---
def load_config_file(filename):
    """Load configuration from a text file, ignoring comments and empty lines."""
    config_items = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith('#'):
                    config_items.append(line)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using empty list.")
    return config_items

def load_credentials():
    """Load Gmail credentials from config_files/config_credentials.txt file."""
    credentials = {}
    try:
        with open('config_files/config_credentials.txt', 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    credentials[key.strip()] = value.strip()
    except FileNotFoundError:
        print("Warning: config_files/config_credentials.txt not found. Will use environment variables.")
    return credentials

# --- LOAD SETTINGS FROM CONFIG FILES ---
KEYWORDS = load_config_file('config_files/config_keywords.txt')
DOMAINS = load_config_file('config_files/config_domains.txt')
EMAIL_RECIPIENTS = load_config_file('config_files/config_emails.txt')

def fetch_wte_news():
    # Build a powerful search query across all domains
    site_query = " OR ".join([f"site:{d}" for d in DOMAINS])
    keyword_query = " OR ".join([f'"{k}"' for k in KEYWORDS])
    full_query = f"({keyword_query}) ({site_query})"

    # Using Google News RSS to scrape "all pages" indexed by search
    rss_url = f"https://news.google.com/rss/search?q={full_query}&hl=en-MY&gl=MY&ceid=MY:en"

    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(rss_url, headers=headers, timeout=30)
        soup = BeautifulSoup(response.content, features="xml")

        articles = []
        articles_plain = []  # For plain text output
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)

        for item in soup.find_all('item')[:25]: # Limit to top 25 results
            title = item.title.text
            link = item.link.text
            pub_date_str = item.pubDate.text
            
            # Parse the publication date
            try:
                pub_date = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
            except ValueError:
                # Handle cases where the date format might be different
                # For simplicity, we'll skip articles with unparseable dates
                continue

            # Filter articles from today and yesterday only
            if yesterday <= pub_date <= today:
                articles.append(f"<li><b>{title}</b><br><a href='{link}'>{link}</a><br><small>{pub_date_str}</small></li>")
                articles_plain.append({"title": title, "link": link, "date": pub_date_str})
        return articles, articles_plain
    except Exception as e:
        print(f"Error fetching news: {e}")
        return [], []

def send_email(articles):
    if not articles:
        print("No WTE news found today.")
        return

    # Load credentials from file first, fallback to environment variables
    creds = load_credentials()
    sender = creds.get("EMAIL_SENDER") or os.getenv("EMAIL_SENDER")
    password = creds.get("EMAIL_PASSWORD") or os.getenv("EMAIL_PASSWORD")

    if not sender or not password:
        print("Error: Gmail credentials not configured.")
        print("Please edit config_files/config_credentials.txt or set EMAIL_SENDER and EMAIL_PASSWORD environment variables.")
        return

    # Use EMAIL_RECIPIENTS from config file, or fallback to environment variable
    receiver_list = EMAIL_RECIPIENTS if EMAIL_RECIPIENTS else []

    # If config file is empty, try environment variable as fallback
    if not receiver_list:
        receiver_raw = os.getenv("EMAIL_RECEIVER", "")
        if receiver_raw:
            receiver_list = [email.strip() for email in receiver_raw.split(",")]

    if not receiver_list:
        print("Error: No email recipients configured. Please add emails to config_files/config_emails.txt")
        return
    
    # Custom Header Format requested
    formatted_date = datetime.now().strftime("%A, %d %B %Y")
    subject_line = f"Daily WTE News By net1io.com. {formatted_date}"

    msg = MIMEMultipart()
    msg['Subject'] = subject_line
    msg['From'] = f"Net1io WTE Bot <{sender}>"
    msg['To'] = ", ".join(receiver_list)
    
    html_body = f"""
    <html>
        <body style="font-family: sans-serif; color: #333;">
            <div style="max-width: 600px; border: 1px solid #ddd; padding: 20px;">
                <h2 style="color: #2e7d32;">WTE & Green Energy Malaysia Brief</h2>
                <p>Generated for net1io.com and Greenviro management.</p>
                <hr>
                <ul>{''.join([f'<li style="margin-bottom:15px;">{a}</li>' for a in articles])}</ul>
                <p style="font-size: 11px; color: #999;">Keywords: {', '.join(KEYWORDS)}</p>
            </div>
        </body>
    </html>
    """
    msg.attach(MIMEText(html_body, 'html'))
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver_list, msg.as_string())
        print("Email successfully sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def save_test_output(articles_plain):
    """Save test results to output.txt file"""
    formatted_date = datetime.now().strftime("%A, %d %B %Y at %I:%M %p")

    with open('output.txt', 'a') as f:
        f.write("=" * 80 + "\n")
        f.write("WTE MALAYSIA NEWS SCRAPER - TEST OUTPUT\n")
        f.write(f"Generated: {formatted_date}\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Configuration:\n")
        f.write(f"  Keywords ({len(KEYWORDS)}): {', '.join(KEYWORDS)}\n")
        f.write(f"  Domains ({len(DOMAINS)}): {', '.join(DOMAINS)}\n")
        f.write(f"  Email Recipients ({len(EMAIL_RECIPIENTS)}): {', '.join(EMAIL_RECIPIENTS)}\n")
        f.write("\n" + "=" * 80 + "\n\n")

        if not articles_plain:
            f.write("No articles found.\n")
        else:
            f.write(f"FOUND {len(articles_plain)} ARTICLES:\n\n")
            for i, article in enumerate(articles_plain, 1):
                f.write(f"{i}. {article['title']}\n")
                f.write(f"   URL: {article['link']}\n")
                f.write(f"   Date: {article['date']}\n")
                f.write("\n")

        f.write("=" * 80 + "\n")
        f.write("END OF TEST OUTPUT\n")
        f.write("=" * 80 + "\n")

    print(f"\n✓ Test output saved to output.txt ({len(articles_plain)} articles)")

if __name__ == "__main__":
    # Check if running in test mode
    test_mode = "-test" in sys.argv or "--test" in sys.argv

    if test_mode:
        print("=" * 60)
        print("RUNNING IN TEST MODE")
        print("=" * 60)
        print(f"Fetching WTE news from {len(DOMAINS)} Malaysian news sources...")
        print(f"Using {len(KEYWORDS)} keywords...")
        print()

        news_html, news_plain = fetch_wte_news()

        if news_plain:
            print(f"✓ Found {len(news_plain)} articles")
            save_test_output(news_plain)
            print("✓ Results saved to output.txt")
            print("\nTo send real email, run: python scrapper.py")
        else:
            print("✗ No articles found")
            save_test_output(news_plain)
    else:
        print("=" * 60)
        print("RUNNING IN PRODUCTION MODE - SENDING EMAIL")
        print("=" * 60)
        news_html, news_plain = fetch_wte_news()
        print(f"Found {len(news_plain)} articles")
        send_email(news_html)
