# daily_briefing.py
import requests
import json
import sys
from datetime import datetime, timezone, timedelta
from jarvis_content import (
    FUTURE_LAB,
    FUTURE_LAB_FULL,
    TALI_STEPS,
    TOOL_SPOTLIGHT,
    KAPUSTA_TODAY,
    AI_NEWS_TODAY,
    JTBD_STATUS,
)
import urllib.request
import xml.etree.ElementTree as ET


with open(".env") as f:
    env = dict(line.strip().split("=", 1) for line in f if "=" in line and not line.startswith("#"))

BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "")
with open("subscribers.json") as f:
    SUBSCRIBERS = json.load(f)

CAT = timezone(timedelta(hours=2))

def today_str():
    return datetime.now(CAT).strftime("%Y-%m-%d")

def today_label():
    return datetime.now(CAT).strftime("%A, %-d %B %Y")

def wait_for_network(max_attempts=10, delay=15):
    """Wait until the Telegram API is reachable — handles Mac waking before network is ready."""
    import time
    for attempt in range(1, max_attempts + 1):
        try:
            urllib.request.urlopen("https://api.telegram.org", timeout=5)
            print("Network ready.")
            return True
        except Exception:
            print(f"Network not ready (attempt {attempt}/{max_attempts}) — retrying in {delay}s...")
            time.sleep(delay)
    print("Network unavailable after all attempts — aborting.")
    return False

def send_message(chat_id, text):
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    try:
        r = requests.post(url, json=payload, timeout=15)
        if not r.ok:
            data = r.json()
            err = data.get("description", "")
            if "deactivated" in err or "blocked" in err or "not found" in err:
                print(f"Skipping {chat_id}: {err}")
                return True  # Skip silently — don't crash the run
        return r.ok
    except Exception as e:
        print(f"Error sending to {chat_id}: {e}")
        return False


def fetch_ai_news():
    try:
        url = 'https://feeds.feedburner.com/venturebeat/SZYF'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        root = ET.fromstring(res.read())
        item = root.find('./channel/item')
        title = item.find('title').text
        link = item.find('link').text
        return {"headline": title, "url": link, "source": "VentureBeat AI"}
    except Exception:
        return {"headline": AI_NEWS_TODAY["headline"], "url": "", "source": AI_NEWS_TODAY["source"]}

def build_briefing():
    date_key = today_str()
    tool = TOOL_SPOTLIGHT.get(date_key)
    tali = TALI_STEPS.get(date_key)

    lines = []

    # HEADER
    lines.append("🧭 <b>NAVIGATOR DAILY BRIEFING</b>")
    lines.append(today_label())
    lines.append("")

    # DEADLINES
    lines.append("🔴 <b>DEADLINES</b>")
    lines.append("• Prepare for Module 2 before Session 9")
    lines.append("• Vanguard Session 9 — Chasing Jarvis Module 2 — <b>Sat 4 April 2026 at 5:00 PM</b> (Belgrade, Bratislava, Ljubljana)")
    lines.append("")

    # NEXT ZOOM
    lines.append("📅 <b>NEXT ZOOM SESSION</b>")
    lines.append("• Vanguard Session 9 — Chasing Jarvis Module 2 — <b>TODAY at 5:00 PM</b> (Belgrade, Bratislava, Ljubljana)")
    lines.append("  <a href='https://cotrugli.online/groups/vanguard/zoom/meetings/9/?wm=1&mi=84405931387'>Join Zoom</a>")
    lines.append("• <a href='https://cotrugli.online/groups/vanguard/'>Zoom Recordings — all sessions</a>")
    lines.append("")

    # STATUS
    lines.append("✅ <b>STATUS</b>")
    lines.append("• All JTBDs current")
    lines.append("• <a href='https://www.linkedin.com/feed/update/urn:li:activity:7442446986844217344/?originTrackingId=pO%2Fw8vwhIdjLEwbFFiYXBQ%3D%3D'>JTBD: Read the 5 series articles and engage on LinkedIn</a>")
    lines.append("• Awaiting Future of Work multiple choice exam results")
    lines.append("• Future of Work Essay — Submitted, awaiting results and feedback")
    lines.append("")

    # CHASING JARVIS — all 5 steps
    lines.append("🎯 <b>CHASING JARVIS — TODAY'S FOCUS</b>")
    lines.append("")
    lines.append("🔜 <b>Module 2 preview — coming TODAY:</b>")
    lines.append("<b>𝗧𝗵𝗲 𝗡𝗼𝗻-𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿'𝘀 𝗣𝗹𝗮𝘆𝗯𝗼𝗼𝗸 𝗳𝗼𝗿 𝗕𝘂𝗶𝗹𝗱𝗶𝗻𝗴 𝘄𝗶𝘁𝗵 𝗔𝗜 𝗔𝗴𝗲𝗻𝘁𝘀</b>")
    lines.append("<b>Five articles. One complete system. No computer science degree required.</b>")
    lines.append("")

    s1 = TALI_STEPS.get("2026-03-27", {})
    s2 = TALI_STEPS.get("2026-03-28", {})
    s3 = TALI_STEPS.get("2026-03-29", {})
    s4 = TALI_STEPS.get("2026-03-30", {})
    s5 = TALI_STEPS.get("2026-03-31", {})

    if s1:
        lines.append("<a href='" + s1["url"] + "'>→ STEP 1 — " + s1["title"] + "</a>")
    if s2:
        lines.append("<a href='" + s2["url"] + "'>→ STEP 2 — " + s2["title"] + "</a>")
    if s3:
        lines.append("<a href='" + s3["url"] + "'>→ STEP 3 — " + s3["title"] + "</a>")
    if s4:
        lines.append("<a href='" + s4["url"] + "'>→ STEP 4 — " + s4["title"] + "</a>")
    if s5:
        lines.append("<a href='" + s5["url"] + "'>→ STEP 5 — " + s5["title"] + "</a>")

    lines.append("")
    lines.append("Read and work through all five before Module 2 — and comment on Dr. Tali Režun's LinkedIn articles.")
    lines.append("")

    # MODULE 2 TOOLS
    lines.append("📝 <b>Module 2 — Prepare for Session 9 (April 4):</b>")
    lines.append("Create accounts and explore these tools — then decide what goes into YOUR personal AI stack:")
    lines.append("")
    lines.append("<b>𝗧𝗢𝗗𝗔𝗬, 𝘄𝗲 𝗴𝗼 𝘁𝗼𝗼𝗹-𝗱𝗲𝗲𝗽. 🛠️</b>")
    lines.append("<a href='https://www.linkedin.com/feed/update/urn:li:activity:7445030971264917504/?originTrackingId=TstswaWRSLICwAtqpbGEHg%3D%3D'>See the full tool breakdown on LinkedIn</a>")
    lines.append("")
    lines.append("Explore, break things, and decide what goes into YOUR personal AI stack.")
    lines.append("")

    # ROADMAP.SH
    lines.append("🗺️ <b>Turning complexity into a navigable path:</b>")
    lines.append("Visit <a href='https://roadmap.sh/dashboard'>roadmap.sh</a> and create an account.")
    lines.append("")

    # KAPUSTA
    lines.append("🏛️ <b>VANGUARD LEADERSHIP &amp; NEO WORLD — Kapusta reading:</b>")
    lines.append("• <a href='" + KAPUSTA_TODAY["url"] + "'>" + KAPUSTA_TODAY["title"] + "</a>")
    lines.append("  " + KAPUSTA_TODAY["description"])
    lines.append("")

    # FUTURE LAB
    lab_articles = FUTURE_LAB.get(date_key, FUTURE_LAB_FULL)
    lines.append("🔬 <b>FUTURE LAB LEARNING — Kapusta &amp; Cotrugli:</b>")
    for article in lab_articles:
        lines.append("• <a href='" + article["url"] + "'>" + article["title"] + "</a>")
        lines.append("  " + article["author"])
    lines.append("")

    # AI NEWS
    news = fetch_ai_news()
    lines.append("🌐 <b>AI NEWS — VENTUREBEAT:</b>")
    if news["url"]:
        lines.append("<a href='" + news["url"] + "'>" + news["headline"] + "</a>")
    else:
        lines.append(news["headline"])
    lines.append(news["source"])
    lines.append("")

    # KNOWLEDGE QUESTION
    if tali:
        lines.append("🧠 <b>Test your knowledge from today's reading:</b>")
        lines.append(tali["question"])
        lines.append("")

    # ADDME
    lines.append("📲 Vanguard — want this briefing every morning at 05:30 CAT? Message /addme to @CotNavigatorBot on Telegram and you're in.")
    lines.append("")
    lines.append("⚡ Navigator out.")

    return "\n".join(lines)

def build_model_answer():
    date_key = today_str()
    tali = TALI_STEPS.get(date_key)
    if not tali:
        return None
    lines = []
    lines.append("🧠 <b>Model answer to this morning's question:</b>")
    lines.append("")
    lines.append(tali["model_answer"])
    lines.append("")
    lines.append("⚡ Navigator out.")
    return "\n".join(lines)

def send_test():
    MY_CHAT_ID = 8536765390
    briefing = build_briefing()
    answer = build_model_answer()
    r = send_message(MY_CHAT_ID, briefing)
    print("Briefing sent: OK" if r else "Briefing sent: FAILED")
    if answer:
        r = send_message(MY_CHAT_ID, answer)
        print("Answer sent: OK" if r else "Answer sent: FAILED")

def send_briefing():
    if not wait_for_network():
        return
    briefing = build_briefing()
    answer = build_model_answer()
    for sub in SUBSCRIBERS:
        chat_id = sub['chat_id'] if isinstance(sub, dict) else sub
        ok = send_message(chat_id, briefing)
        print("Briefing -> " + str(chat_id) + ": " + ("OK" if ok else "FAILED"))
    if answer:
        import time
        time.sleep(1800)
        for sub in SUBSCRIBERS:
            chat_id = sub['chat_id'] if isinstance(sub, dict) else sub
            ok = send_message(chat_id, answer)
            print("Answer -> " + str(chat_id) + ": " + ("OK" if ok else "FAILED"))


if __name__ == "__main__":
    if "--test-send" in sys.argv:
        send_test()
    elif "--test" in sys.argv:
        print("--- BRIEFING PREVIEW ---")
        print(build_briefing())
        print("")
        print("--- MODEL ANSWER PREVIEW ---")
        answer = build_model_answer()
        print(answer if answer else "(No model answer for today)")
    elif "--briefing-only" in sys.argv:
        briefing = build_briefing()
        for sub in SUBSCRIBERS:
            chat_id = sub['chat_id'] if isinstance(sub, dict) else sub
            ok = send_message(chat_id, briefing)
            print("Briefing -> " + str(chat_id) + ": " + ("OK" if ok else "FAILED"))
    elif "--answer-only" in sys.argv:
        answer = build_model_answer()
        if answer:
            for sub in SUBSCRIBERS:
                chat_id = sub['chat_id'] if isinstance(sub, dict) else sub
                ok = send_message(chat_id, answer)
                print("Answer -> " + str(chat_id) + ": " + ("OK" if ok else "FAILED"))
        else:
            print("No model answer for today")
    else:
        send_briefing()
