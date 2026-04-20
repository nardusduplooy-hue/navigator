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
    MODULE3_ARTICLES,
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
    lines.append("")

    # NEXT ZOOM
    lines.append("📅 <b>NEXT ZOOM SESSION</b>")
    lines.append("• <a href='https://cotrugli.online/groups/vanguard/zoom/meetings/11/?wm=1&mi=87497940375'>Next Zoom session — Saturday 2 May</a>")
    lines.append("• <a href='https://cotrugli.online/groups/vanguard/'>Zoom Recordings — all sessions</a>")
    lines.append("")

    # STATUS
    lines.append("✅ <b>STATUS</b>")
    lines.append("• All JTBDs current")
    lines.append("• Awaiting Future of Work multiple choice exam results")
    lines.append("• Future of Work Essay — Submitted, awaiting results and feedback")
    lines.append("")

    # CHASING JARVIS — Module 3 (weekday) or full recap (weekend)
    lines.append("🎯 <b>CHASING JARVIS — TODAY'S FOCUS</b>")
    lines.append("")

    if date_key in ("2026-04-11", "2026-04-12"):
        # WEEKEND BRIEFING — full programme recap
        lines.append("<b>Your complete Chasing Jarvis reading list</b>")
        lines.append("Use the weekend to catch up, revisit, and go deeper. Everything we've covered so far — in one place.")
        lines.append("")

        lines.append("<b>📗 MODULE 1 — The Non-Developer's Playbook for Building with AI</b>")
        s1 = TALI_STEPS.get("2026-03-27", {})
        s2 = TALI_STEPS.get("2026-03-28", {})
        s3 = TALI_STEPS.get("2026-03-29", {})
        s4 = TALI_STEPS.get("2026-03-30", {})
        s5 = TALI_STEPS.get("2026-03-31", {})
        if s1: lines.append("<a href='" + s1["url"] + "'>→ STEP 1 — " + s1["title"] + "</a>")
        if s2: lines.append("<a href='" + s2["url"] + "'>→ STEP 2 — " + s2["title"] + "</a>")
        if s3: lines.append("<a href='" + s3["url"] + "'>→ STEP 3 — " + s3["title"] + "</a>")
        if s4: lines.append("<a href='" + s4["url"] + "'>→ STEP 4 — " + s4["title"] + "</a>")
        if s5: lines.append("<a href='" + s5["url"] + "'>→ STEP 5 — " + s5["title"] + "</a>")
        lines.append("")

        lines.append("<b>📘 MODULE 2 — Tools & Orchestration</b>")
        lines.append("<a href='https://gemini.google.com'>→ Google Gemini — Login & Explore</a>")
        lines.append("<a href='https://aistudio.google.com'>→ Google AI Studio — Login & Explore</a>")
        lines.append("<a href='https://notebooklm.google.com'>→ Google NotebookLM — Login & Explore</a>")
        lines.append("<a href='https://claude.ai/download'>→ Anthropic Claude Desktop — Create Account & Explore</a>")
        lines.append("<a href='https://github.com'>→ GitHub — Create Account & Explore</a>")
        lines.append("<a href='https://lmstudio.ai'>→ LM Studio — Download & Install (advanced)</a>")
        lines.append("<a href='https://n8n.io'>→ n8n — Login & Explore</a>")
        lines.append("")

        lines.append("<b>📙 MODULE 3 — AI Agents: From Chatbots to Autonomous Workers</b>")
        lines.append("<a href='https://cotrugli.online/courses/chasing-jarvis/lessons/ai-agents/'>→ Module 3 portal</a>")
        lines.append("<a href='https://medium.com/@talirezun/understanding-ai-agents-from-chatbots-to-autonomous-digital-workers-407217d84695'>→ Understanding AI Agents: From Chatbots to Autonomous Digital Workers</a>")
        lines.append("<a href='https://medium.com/@talirezun/the-year-i-started-coding-with-ai-my-coding-agent-journey-431f6f25afe1'>→ The Year I Started Coding with AI: My Coding Agent Journey</a>")
        lines.append("<a href='https://medium.com/@talirezun/from-english-to-code-building-production-saas-with-claude-desktop-3ee9c787f5be'>→ From English to Code: Building Production SaaS with Claude Desktop</a>")
        lines.append("<a href='https://medium.com/@talirezun/exploring-early-indicators-of-agi-in-coding-agents-bc671f98eddc'>→ Exploring Early Indicators of AGI in Coding Agents</a>")
        lines.append("")
        lines.append("<b>📚 Pre-Module 3 Reading — Essential for Track B:</b>")
        lines.append("<a href='https://www.linkedin.com/posts/talirezun_fromlabtolife-ai-codingagents-share-7447218059364159489-zQSL'>→ Augment Code vs Claude Code vs Codex CLI — Dr. Tali Režun</a>")
        lines.append("")
        lines.append("<b>🧠 Second Brain — New from Dr. Tali:</b>")
        lines.append("<a href='https://www.linkedin.com/posts/talirezun_opensource-secondbrain-obsidian-share-7447927944905347072-HyX3'>→ A fully local, open-source AI app that turns your research into an interconnected Obsidian wiki. Try it and drop your thoughts in the comments.</a>")
        lines.append("")
        lines.append("<b>Supplementary resources:</b>")
        lines.append("<a href='https://www.linkedin.com/feed/update/urn:li:activity:7447927947971416064/?commentUrn=urn%3Ali%3Acomment%3A(activity%3A7447927947971416064%2C7448323986196897792)&dashCommentUrn=urn%3Ali%3Afsd_comment%3A(7448323986196897792%2Curn%3Ali%3Aactivity%3A7447927947971416064)'>→ Second Brain — community discussion: share your thoughts and see what others are building</a>")
        lines.append("<a href='https://www.linkedin.com/posts/talirezun_i-recently-wrote-an-article-comparing-augment-activity-7448967589017366528-q3qe/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAJkcvoBxTW_IU_6a4K4AWRwEHahONmqfLg'>→ Dr. Tali's coding frameworks comparison — Augment Code vs Claude Code vs Codex CLI: join the discussion</a>")
        lines.append("")

    else:
        # WEEKDAY BRIEFING
        lines.append("<b>🎯 Chasing Jarvis | Module 3 Homework</b>")
        lines.append("")
        lines.append("Time to build something real, people! 🚀")
        lines.append("")
        lines.append("Your task: use an AI coding tool of your choice — Google AI Studio, Cursor, Claude Code, Windsurf, Copilot — whatever feels right for you — and build a simple app or game.")
        lines.append("")
        lines.append("<b>Two paths:</b>")
        lines.append("")
        lines.append("1. Already have your MVP idea? → Build a first working version and give us a sneak peek 👀")
        lines.append("")
        lines.append("2. No MVP yet? → Build something fun! A game, a tool, anything that works and runs in a browser 🎮 that you can share with us.")
        lines.append("")
        lines.append("<b>Deadline: Wednesday, 29 April</b>")
        lines.append("📎 Share your project link directly in the Chasing Jarvis group")
        lines.append("👤 Tag your team leader and team members in the post")
        lines.append("")
        lines.append("Let's see what you've got! 💪")
        lines.append("")
        lines.append("<b>Chasing Jarvis Module Pre-reading and podcast:</b>")
        lines.append("<a href='https://redcircle.com/shows/ab71928c-8c79-46b9-a324-0d82a84b3254/ep/2f8a063f-121e-4c43-b268-a3c0e42c6701'>→ From Prompts to Precision: AI-Generated Research Podcast Discussion | From Lab to Life</a>")
        lines.append("")
        lines.append("<a href='https://medium.com/@talirezun/from-prompts-to-precision-the-art-science-of-context-engineering-cebd47462b1c'>→ From Prompts to Precision: The Art &amp; Science of Context Engineering — Dr. Tali Režun</a>")
        lines.append("Core reading — read thoroughly before Module 4")
        lines.append("")
        lines.append("<a href='https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents'>→ Effective Context Engineering for AI Agents — Anthropic</a>")
        lines.append("Technical deep dive from Anthropic's engineering team")
        lines.append("")

    # MODULE 3 TOOLS
    lines.append("Explore, break things, and decide what goes into YOUR personal AI stack.")
    lines.append("")

    # ROADMAP.SH
    lines.append("🗺️ <b>Supplementary Resources (Recommended):</b>")
    lines.append("<a href='https://www.markdownguide.org/'>→ Markdown Guide — Complete reference for markdown syntax</a>")
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
    lines.append("📲 Vanguard — want this briefing every morning at 08:00 CAT? Message /addme to @CotNavigatorBot on Telegram and you're in.")
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
    full = build_briefing()
    parts = [p.strip() for p in full.split("⚡⚡SPLIT⚡⚡") if p.strip()]
    answer = build_model_answer()
    for i, part in enumerate(parts):
        r = send_message(MY_CHAT_ID, part)
        print(f"Briefing part {i+1} sent: {'OK' if r else 'FAILED'}")
    if answer:
        r = send_message(MY_CHAT_ID, answer)
        print("Answer sent: OK" if r else "Answer sent: FAILED")

def send_briefing():
    if not wait_for_network():
        return
    full = build_briefing()
    parts = [p.strip() for p in full.split("⚡⚡SPLIT⚡⚡") if p.strip()]
    answer = build_model_answer()
    for sub in SUBSCRIBERS:
        chat_id = sub['chat_id'] if isinstance(sub, dict) else sub
        for i, part in enumerate(parts):
            ok = send_message(chat_id, part)
            print(f"Briefing part {i+1} -> {chat_id}: {'OK' if ok else 'FAILED'}")
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
        full = build_briefing()
        parts = [p.strip() for p in full.split("⚡⚡SPLIT⚡⚡") if p.strip()]
        for sub in SUBSCRIBERS:
            chat_id = sub['chat_id'] if isinstance(sub, dict) else sub
            for i, part in enumerate(parts):
                ok = send_message(chat_id, part)
                print(f"Briefing part {i+1} -> {chat_id}: {'OK' if ok else 'FAILED'}")
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
