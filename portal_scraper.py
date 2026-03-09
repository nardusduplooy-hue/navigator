"""
Navigator Portal Scraper
Scrapes Vanguard-specific pages from cotrugli.online
"""

import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("COTRUGLI_USERNAME")
PASSWORD = os.getenv("COTRUGLI_PASSWORD")
BASE_URL = "https://cotrugli.online"

PAGES_TO_SCRAPE = [
    "/courses/chasing-jarvis/",
    "/courses/vanguard-future-of-work/",
    "/courses/entrepreneurship-2026/",
    "/courses/final-project/",
    "/groups/vanguard/",
    "/groups/vanguard/zoom/",
]

def login():
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"})
    session.cookies.set("wordpress_test_cookie", "WP Cookie check")
    r = session.post(f"{BASE_URL}/wp-login.php", data={
        "log": USERNAME,
        "pwd": PASSWORD,
        "wp-submit": "Log In",
        "testcookie": "1"
    }, allow_redirects=True)
    if USERNAME and BASE_URL in r.url:
        print("✅ Logged in successfully")
        return session
    else:
        print("❌ Login failed — check credentials in .env")
        return None

def scrape_page(session, path):
    url = BASE_URL + path
    print(f"📄 Scraping {url}")
    r = session.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    results = {
        "url": url,
        "path": path,
        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "title": "",
        "deadlines": [],
        "zoom_links": [],
        "lessons": [],
        "content_blocks": []
    }

    # Title
    title = soup.find("h1") or soup.find("title")
    if title:
        results["title"] = title.get_text(strip=True)

    # Lessons / curriculum items
    for tag in soup.find_all(["li", "div"], class_=lambda c: c and any(x in c for x in ["lesson", "topic", "curriculum", "course-item"])):
        text = tag.get_text(strip=True)
        if len(text) > 10:
            results["lessons"].append(text[:200])

    # Zoom links — deduplicated
    seen_urls = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if ("zoom.us" in href or "/zoom/" in href) and href not in seen_urls:
            seen_urls.add(href)
            results["zoom_links"].append({
                "text": a.get_text(strip=True)[:80],
                "url": href
            })

    # Content blocks
    for tag in soup.find_all(["p", "li", "h2", "h3", "h4"]):
        text = tag.get_text(strip=True)
        if len(text) > 20:
            results["content_blocks"].append(text[:300])

    # Deadline detection
    deadline_keywords = ["deadline", "due", "submit", "by ", "before ", "cet", "essay", "assignment", "prework", "upload"]
    for block in results["content_blocks"]:
        if any(kw in block.lower() for kw in deadline_keywords):
            results["deadlines"].append(block)

    return results

def run():
    print("🧭 Navigator Portal Scraper")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    session = login()
    if not session:
        return

    all_data = []
    for path in PAGES_TO_SCRAPE:
        try:
            data = scrape_page(session, path)
            all_data.append(data)
            print(f"   ✓ {data['title']}")
            print(f"     Zoom: {len(data['zoom_links'])} | Deadlines: {len(data['deadlines'])} | Lessons: {len(data['lessons'])}")
        except Exception as e:
            print(f"   ❌ Error on {path}: {e}")

    with open("portal_data.json", "w") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)

    # Summary
    total_zoom = sum(len(p["zoom_links"]) for p in all_data)
    total_deadlines = sum(len(p["deadlines"]) for p in all_data)
    print(f"\n✅ portal_data.json saved")
    print(f"📊 {len(all_data)} pages | {total_zoom} Zoom links | {total_deadlines} deadline refs")

if __name__ == "__main__":
    run()
