import schedule
import time
import subprocess
import sys
from datetime import datetime, timezone, timedelta

CAT = timezone(timedelta(hours=2))

def send_briefing():
    cat_time = datetime.now(CAT)
    print(f"⏰ Sending briefing at {cat_time.strftime('%H:%M')} CAT")
    subprocess.run([sys.executable, "daily_briefing.py", "--briefing-only"])

def send_answer():
    cat_time = datetime.now(CAT)
    print(f"⏰ Sending model answer at {cat_time.strftime('%H:%M')} CAT")
    subprocess.run([sys.executable, "daily_briefing.py", "--answer-only"])

schedule.every().day.at("05:30").do(send_briefing)
schedule.every().day.at("06:00").do(send_answer)

print("🧭 Navigator scheduler running...")
print("📅 Briefing: 05:30 CAT | Model answer: 06:00 CAT")

while True:
    schedule.run_pending()
    time.sleep(30)
