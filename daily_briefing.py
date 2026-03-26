# daily_briefing.py
import requests
import json
import sys
from datetime import datetime, timezone, timedelta
from jarvis_content import (
    TALI_STEPS,
    TOOL_SPOTLIGHT,
    KAPUSTA_TODAY,
    SUPPLEMENTARY_RESOURCE,
    AI_NEWS_TODAY,
)

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

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    r = requests.post(url, json=payload)
    return r.ok

def build_briefing():
    date_key = today_str()
    tali = TALI_STEPS.get(date_key)
    tool = TOOL_SPOTLIGHT.get(date_key)

    lines = []

    lines.append("🧭 <b>NAVIGATOR DAILY BRIEFING</b>")
    lines.append(today_label())
    lines.append("")

    lines.append("🔴 <b>DEADLINES</b>")
    lines.append("• Prepare for Module 2 before Session 9")
    lines.append("• Session 9 — Chasing Jarvis Module 2 — <b>Sat 4 April</b> (estimated)")
    lines.append("")

    lines.append("📅 <b>NEXT ZOOM SESSION</b>")
    lines.append("• Vanguard Session 9 — Chasing Jarvis Module 2 — Sat 4 April (estimated)")
    lines.append("  Zoom link to be confirmed")
    lines.append("")

    lines.append("✅ <b>STATUS</b>")
    lines.append("• All JTBDs current")
    lines.append("• JTBD — Comment posted on Dr. Tali LinkedIn")
    lines.append("• Awaiting Future of Work multiple choice exam results")
    lines.append("• Future of Work Essay — Submitted, awaiting results and feedback")
    lines.append("")

    lines.append("🎯 <b>CHASING JARVIS — TODAY'S FOCUS</b>")
    lines.append("")
    lines.append("𝗧𝗵𝗲 𝗡𝗼𝗻-𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿'𝘀 𝗣𝗹𝗮𝘆𝗯𝗼𝗼𝗸 𝗳𝗼𝗿 𝗕𝘂𝗶𝗹𝗱𝗶𝗻𝗴 𝘄𝗶𝘁𝗵 𝗔𝗜 𝗔𝗴𝗲𝗻𝘁𝘀")
    lines.append("Five articles. One complete system. No computer science degree required.")
    lines.append("")

    if tali:
        lines.append(f"→ <b>STEP {tali['step']} — {tali['title']}</b>")
        lines.append(f"<a href='{tali['url']}'>Read on Medium</a>")
        lines.append("")
        lines.append(f"<b>Focus:</b> {tali['focus']}")
        lines.append("")
        lines.append("Read and comment on Dr. Tali Režun's LinkedIn articles.")
    else:
        lines.append("→ All 5 steps complete — review your notes before Session 9 on 4 April.")
    lines.append("")

    if tool:
        lines.append(f"📝 <b>Module 2 — Tool spotlight today: {tool['name']}</b>")
        lines.append(f"→ <a href='{tool['url']}'>{tool['name']} — {tool['action']}</a>")
        lines.append("")
        lines.append(tool["what_its_good_for"])
        lines.append("")
        lines.append("Explore, break things, and decide what goes into YOUR personal AI stack.")
        lines.append("")

    lines.append("📚 <b>Supplementary resource — Module 2:</b>")
    lines.append(f"<a href='{SUPPLEMENTARY_RESOURCE['url']}'>{SUPPLEMENTARY_RESOURCE['title']}</a>")
    lines.append(SUPPLEMENTARY_RESOURCE["description"])
    lines.append("")

    lines.append("🏛️ <b>VANGUARD LEADERSHIP &amp; NEO WORLD — Kapusta reading:</b>")
    lines.append(f"• <a href='{KAPUSTA_TODAY['url']}'>{KAPUSTA_TODAY['title']}</a>")
    lines.append(f"  {KAPUSTA_TODAY['description']}")
    lines.append("")

    lines.append("🌐 <b>AI NEWS — THE RUNDOWN:</b>")
    lines.append(AI_NEWS_TODAY["headline"])
    lines.append(AI_NEWS_TODAY["source"])
    lines.append("")

    if tali:
        lines.append("🧠 <b>Test your knowledge from today's reading:</b>")
        lines.append(tali["question"])
        lines.append("")

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

def send_briefing():
    briefing = build_briefing()
    answer = build_model_answer()
    for chat_id in SUBSCRIBERS:
        ok = send_message(chat_id, briefing)
        print(f"Briefing → {chat_id}: {'✅' if ok else '❌'}")
    if answer:
        import time
        time.sleep(1800)
        for chat_id in SUBSCRIBERS:
            ok = send_message(chat_id, answer)
            print(f"Answer → {chat_id}: {'✅' if ok else '❌'}")

if __name__ == "__main__":
    if "--test" in sys.argv:
        print("─── BRIEFING PREVIEW ───")
        print(build_briefing())
        print("")
        print("─── MODEL ANSWER PREVIEW ───")
        answer = build_model_answer()
        print(answer if answer else "(No model answer for today)")
    else:
        send_briefing()
