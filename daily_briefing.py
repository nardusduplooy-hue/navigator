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
    lines.append("🤝 <b>Stronger Together</b>")
    lines.append("<i>Vanguard is a team sport. The cohort is forming active groups right now — find your people, find your Chief, and get to work. That is what this programme is built for.</i>")
    lines.append("")

    # DEADLINES
    lines.append("🔴 <b>DEADLINES</b>")
    lines.append("")

    # NEXT ZOOM
    lines.append("📅 <b>NEXT ZOOM SESSION</b>")
    lines.append("• Next Zoom session — Saturday 16 May (approximate)")
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
        lines.append("📚 <b>REQUIRED READING — New from Dr. Tali Režun</b>")
        lines.append("")
        lines.append("<b>The Brain is Ready. The Body is the Problem.</b>")
        lines.append(
            "We've been learning how to build software with coding agents. "
            "But there's a wall you're going to hit the moment you try to connect your agent to the real world. "
            "APIs are locked. Data is siloed. Social platforms block agent access. "
            "And the moment you give an agent access to sensitive data, privacy becomes a serious design decision — not an afterthought. "
            "This article maps exactly that wall. Where it is, why it exists, and what the frontier labs are doing about it right now. "
            "If you want to build useful agents — not just impressive demos — this is the context you need."
        )
        lines.append("")
        lines.append("<a href='https://medium.com/@talirezun/the-brain-is-ready-the-body-is-the-problem-f32f08e42b0d'>→ Read on Medium</a>")
        lines.append("<a href='https://open.substack.com/pub/talirezun/p/the-brain-is-ready-the-body-is-the?r=68m2cw&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true'>→ Read on Substack</a>")
        lines.append("")
        lines.append("💬 After you read it — <a href='https://www.linkedin.com/posts/talirezun_fromlabtolife-ai-aiagents-activity-7456956758431875073-rRpZ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAJkcvoBxTW_IU_6a4K4AWRwEHahONmqfLg'>drop your thoughts on LinkedIn</a>. What's the biggest obstacle you would face trying to build around these constraints? Have you already hit any of these walls? Let's spin a real debate — not polite reactions.")
        lines.append("")
        lines.append("Reflect on what you have been building.")
        lines.append("Gather your team, refine and iterate — and use your new B2B Sales module to start thinking about how you will ship your product.")
        lines.append("")
        lines.append("<a href='https://anthropic.skilljar.com/introduction-to-claude'>→ Free Claude training — Anthropic's official Introduction to Claude</a>")
        lines.append("")
        lines.append("<b>📊 AI IN B2B SALES</b>")
        lines.append("<a href='https://cotrugli.online/wp-content/uploads/2026/04/Module1_AI_Force_Multiplier.pdf'>→ Module 1 — The Thesis &amp; Landscape: AI as Force Multiplier in B2B Sales</a>")
        lines.append("")
        lines.append("🏆 <b>VANGUARD TEAMS</b>")
        lines.append("<i>No one wins this alone. The teams that break through are the ones that show up for each other. If you are still on the outside — get in. Message someone today.</i>")
        lines.append("")

    # KAPUSTA
    lines.append("🏛️ <b>VANGUARD LEADERSHIP &amp; NEO WORLD — Kapusta just posted this:</b>")
    lines.append("")
    lines.append("<b>Trust as a Protocol — The Cotrugli Ledger</b>")
    lines.append(
        "Kapusta argues that trust will be one of the most important virtues in the NEO era — "
        "not blind trust, not trust as a feeling, but engineered trust. A protocol. "
        "He and his team at COlab have spent years developing this: the Cotrugli Ledger. "
        "Not just a decentralised accounting and governance system — but the minimal trust layer "
        "that AI needs right now. This is the first post in a series. Read it, and watch for what follows."
    )
    lines.append("")
    lines.append("<a href='https://www.linkedin.com/posts/cotrugli_it-is-hard-to-explain-why-i-believe-trust-ugcPost-7457021692511424512-g8gj/'>→ Read Kapusta's post on LinkedIn</a>")
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


def send_channel():
    """Manually post today's briefing + model answer to the COTRUGLI Navigator channel topic.
    Only run this after --test-send has been approved. Never called by cron."""
    CHANNEL_CHAT_ID = -1002421053554
    CHANNEL_THREAD_ID = 2201

    def send_to_channel(text):
        url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
        payload = {
            "chat_id": CHANNEL_CHAT_ID,
            "message_thread_id": CHANNEL_THREAD_ID,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        }
        try:
            r = requests.post(url, json=payload, timeout=15)
            return r.ok
        except Exception as e:
            print(f"Error sending to channel: {e}")
            return False

    full = build_briefing()
    parts = [p.strip() for p in full.split("⚡⚡SPLIT⚡⚡") if p.strip()]
    answer = build_model_answer()

    for i, part in enumerate(parts):
        ok = send_to_channel(part)
        print(f"Channel briefing part {i+1}: {'OK' if ok else 'FAILED'}")
    if answer:
        ok = send_to_channel(answer)
        print(f"Channel answer: {'OK' if ok else 'FAILED'}")


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
    elif "--send-channel" in sys.argv:
        send_channel()
    else:
        send_briefing()
