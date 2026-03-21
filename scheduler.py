import schedule
import time
import subprocess
import sys
from datetime import datetime, timezone, timedelta

def job():
    # Check actual Cape Town time before firing
    cat_time = datetime.now(timezone(timedelta(hours=2)))
    hour = cat_time.hour
    minute = cat_time.minute
    # Only fire between 05:25 and 05:45 CAT
    if not (hour == 5 and 25 <= minute <= 45):
        print(f"⏰ Skipping — CAT time is {cat_time.strftime('%H:%M')}, outside send window")
        return
    print(f"⏰ Running Navigator at {cat_time.strftime('%H:%M')} CAT")
    time.sleep(120)  # Wait 2 minutes for network to be ready
    subprocess.run([sys.executable, "daily_briefing.py"])

# Schedule runs every 30 minutes to catch the 05:30 window reliably
schedule.every(30).minutes.do(job)

print("🧭 Navigator scheduler running...")
print("📅 Daily briefing scheduled for 05:30 CAT")

while True:
    schedule.run_pending()
    time.sleep(60)
