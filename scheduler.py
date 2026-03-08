import asyncio
import schedule
import time
from datetime import datetime
import subprocess
import sys

def job():
    print(f"⏰ Running Navigator at {datetime.now().strftime('%H:%M')}")
    subprocess.run([sys.executable, "read_channels.py"])
    asyncio.run(__import__('daily_briefing').send_daily_briefing())

# 05:30 Cape Town (UTC+2) = 03:30 UTC
schedule.every().day.at("03:30").do(job)

print("🧭 Navigator scheduler running...")
print("📅 Daily briefing scheduled for 05:30 CAT")

while True:
    schedule.run_pending()
    time.sleep(60)
