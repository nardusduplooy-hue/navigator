import schedule
import time
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone, timedelta

CAT = timezone(timedelta(hours=2))

def wait_for_network(max_attempts=20, delay=15):
    """Wait until network is ready before starting the scheduler loop."""
    for attempt in range(1, max_attempts + 1):
        try:
            urllib.request.urlopen("https://api.telegram.org", timeout=5)
            print("✅ Network ready — starting scheduler.")
            return True
        except Exception:
            print(f"⏳ Network not ready (attempt {attempt}/{max_attempts}) — retrying in {delay}s...")
            time.sleep(delay)
    print("❌ Network unavailable after all attempts — scheduler starting anyway.")
    return False

def send_briefing():
    cat_time = datetime.now(CAT)
    print(f"⏰ Sending briefing at {cat_time.strftime('%H:%M')} CAT")
    subprocess.run([sys.executable, "daily_briefing.py", "--briefing-only"])

def send_answer():
    cat_time = datetime.now(CAT)
    print(f"⏰ Sending model answer at {cat_time.strftime('%H:%M')} CAT")
    subprocess.run([sys.executable, "daily_briefing.py", "--answer-only"])

# Wait for network before registering schedules
wait_for_network()

schedule.every().day.at("05:30").do(send_briefing)
schedule.every().day.at("06:00").do(send_answer)

print("🧭 Navigator scheduler running...")
print("📅 Briefing: 05:30 CAT | Model answer: 06:00 CAT")

while True:
    schedule.run_pending()
    time.sleep(30)
