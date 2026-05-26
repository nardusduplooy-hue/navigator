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
    VANGUARD_SUMMARIES,
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

    # VANGUARD TEAMS
    lines.append("🏆 <b>VANGUARD TEAMS</b>")
    lines.append("Tribes don\u2019t wait to be built. They are chosen — one decision, one contribution, one standard held at a time.")
    lines.append("")

    # DEADLINES
    lines.append("🔴 <b>DEADLINES</b>")
    lines.append("")

    # NEXT ZOOM
    lines.append("📅 <b>NEXT ZOOM SESSION</b>")
    lines.append("• 🗓 Saturday 30 May")
    lines.append("")

    # CHASING JARVIS — Module 3 (weekday) or full recap (weekend)
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
        step = TALI_STEPS.get(date_key, {})
        if date_key == "2026-05-16":
            # SESSION DAY — Module 4 Context Engineering
            lines.append("🎯 <b>CHASING JARVIS — MODULE 4: CONTEXT ENGINEERING</b>")
            lines.append("")
            lines.append("🚀 <b>Message from Dr. Tali — today is the day</b>")
            lines.append("")
            lines.append("We are back <b>today at 17:00 Belgrade / Ljubljana time</b> for Module 4: Context Engineering. Here is what you need to know:")
            lines.append("")
            lines.append("<b>🛠️ App Showcases — Module 3 Homework</b>")
            lines.append("We have dedicated slots for 5 or 6 presentations. This is your time to show us the brains of what you have built.")
            lines.append("• <b>The Focus:</b> Mechanics &amp; Functionalities. Skip the landing pages — show us the backend-to-frontend logic, the features, and the smart elements.")
            lines.append("• <b>The Format:</b> 5 minutes each. No slides needed — just a live demo of the app in action.")
            lines.append("• <b>Action:</b> If you want to present, have your environment ready to share today.")
            lines.append("")
            lines.append("🎯 <b>Chasing Jarvis: Five Modules. One Mission. Build the Future.</b>")
            lines.append("<a href='https://www.linkedin.com/posts/talirezun_chasingjarvis-chasingjarvis-aiagents-share-7460995022214270976-GoJa?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAJkcvoBxTW_IU_6a4K4AWRwEHahONmqfLg'>→ Links in the comments of Dr. Tali's LinkedIn post</a>")
            lines.append("")
            lines.append("See you later today. Let's get to work. 🦾")
            lines.append("")
            lines.append("<b>📊 AI IN B2B SALES</b>")
            lines.append("<a href='https://cotrugli.online/wp-content/uploads/2026/04/Module1_AI_Force_Multiplier.pdf'>→ Module 1 — The Thesis &amp; Landscape: AI as Force Multiplier in B2B Sales</a>")
            lines.append("")
        else:
            lines.append("🎯 <b>CHASING JARVIS — MODULE 5: BUILDING AN MVP — FROM CONCEPT TO DEPLOYMENT</b>")
            lines.append("")
            lines.append("Module 5 is the capstone. Everything you have learned converges into one tangible output: a functioning MVP you build, test, and deploy using AI tools and agents — guided by the context packages you built in Module 4.")
            lines.append("")
            lines.append("📋 <b>STUDENT WORK: MVP DOCUMENTATION — BUILD YOUR CONTEXT PACKAGE</b>")
            lines.append("")
            lines.append("<b>Your Task:</b> Research your app idea → Validate market fit → Generate 4 Markdown docs → Feed to Coding Agent in Module 5")
            lines.append("<b>Tool:</b> Claude Desktop + Sonnet 4.5 or GPT-5.2")
            lines.append("")
            lines.append("This is where Chasing Jarvis becomes real. 🦾")
            lines.append("")
            lines.append("🔖 <b>Six releases in three weeks. Here's what changed in #TheCurator 3.0.1. Beta 13</b>")
            lines.append("<a href='https://www.linkedin.com/feed/update/urn:li:activity:7464590551913324544/'>→ Dr. Tali Režun on LinkedIn</a>")
            lines.append("")
            lines.append("<b>📊 AI IN B2B SALES</b>")
            lines.append("<a href='https://cotrugli.online/wp-content/uploads/2026/04/Module1_AI_Force_Multiplier.pdf'>→ Module 1 — The Thesis &amp; Landscape: AI as Force Multiplier in B2B Sales</a>")
            lines.append("")

    # VANGUARD LEADERSHIP — daily book summary
    vanguard = VANGUARD_SUMMARIES.get(date_key)
    if vanguard:
        lines.append("🏛️ <b>VANGUARD LEADERSHIP — Dražen Kapusta</b>")
        lines.append("")
        lines.append("<b>" + vanguard["title"] + "</b>")
        lines.append("<i>" + vanguard["chapter"] + "</i>")
        lines.append("")
        lines.append(vanguard["summary"])
        lines.append("")
        lines.append("<a href='https://www.linkedin.com/posts/cotrugli_thucydidestrap-leadership-geopolitics-share-7462394444852379648-OMgP?utm_source=share&utm_medium=member_android&rcm=ACoAAABVXjQBjD1rAkelAiZQjLIpnQRQFS6tooE'>→ Read more on LinkedIn — Dražen Kapusta</a>")
        lines.append("")
    else:
        lines.append("🏛️ <b>VANGUARD ROOTS — Who was Benedetto Cotrugli?</b>")
        lines.append("")
        lines.append("Considered one of the most important figures in the history of Dubrovnik, Benedetto Cotrugli was a 15th-century merchant, diplomat, and humanist — known as the author of one of the earliest publications on entrepreneurship and double-entry bookkeeping. His book, <i>The Art of Trade</i> (<i>Il libro del arte del mercatura</i>), is one of the most significant writings of all time on the philosophy and art of business.")
        lines.append("")
        lines.append("<a href='https://www.linkedin.com/pulse/benedetto-cotrugli-cotrugli-business-school-8pd7f/?trackingId=qt1hfzDgJGatWWtZFvj6iA%3D%3D'>→ Read more on LinkedIn</a>")
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
    if tali and date_key != "2026-05-17":
        lines.append("🧠 <b>Test your knowledge:</b>")
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
    if not tali or date_key == "2026-05-17":
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


def test_channel():
    """Preview the channel post — sends to Nardus DM only. Never touches the channel."""
    MY_CHAT_ID = 8536765390
    full = build_briefing()
    parts = [p.strip() for p in full.split("⚡⚡SPLIT⚡⚡") if p.strip()]
    answer = build_model_answer()
    print("--- CHANNEL TEST (to your DM only) ---")
    for i, part in enumerate(parts):
        ok = send_message(MY_CHAT_ID, part)
        print(f"Channel test part {i+1}: {'OK' if ok else 'FAILED'}")
    if answer:
        ok = send_message(MY_CHAT_ID, answer)
        print(f"Channel test answer: {'OK' if ok else 'FAILED'}")


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
    elif "--test-channel" in sys.argv:
        test_channel()
    elif "--send-channel" in sys.argv:
        send_channel()
    else:
        send_briefing()
