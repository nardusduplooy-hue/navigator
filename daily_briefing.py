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

# Date override — set by --date argument to preview a specific day
_DATE_OVERRIDE = None

def today_str():
    if _DATE_OVERRIDE:
        return _DATE_OVERRIDE
    return datetime.now(CAT).strftime("%Y-%m-%d")

def today_label():
    if _DATE_OVERRIDE:
        d = datetime.strptime(_DATE_OVERRIDE, "%Y-%m-%d")
        return d.strftime("%A, %-d %B %Y")
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
    REQUIRE_KEYWORDS = ["anthropic", "claude"]
    EXCLUDE_KEYWORDS = ["attack", "vulnerability", "exploit", "breach", "hack", "malware", "ransomware", "jailbreak", "turned every engineer into three", "two-thirds had already built their hedge", "internal reasoning is more deceptive", "grok"]
    try:
        url = 'https://feeds.feedburner.com/venturebeat/SZYF'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        root = ET.fromstring(res.read())
        items = root.findall('./channel/item')
        for item in items:
            title = item.find('title').text or ""
            link = item.find('link').text or ""
            title_lower = title.lower()
            has_required = any(kw in title_lower for kw in REQUIRE_KEYWORDS)
            has_excluded = any(kw in title_lower for kw in EXCLUDE_KEYWORDS)
            if has_required and not has_excluded:
                return {"headline": title, "url": link, "source": "VentureBeat AI"}
        # No matching item — use fallback
        return {"headline": AI_NEWS_TODAY["headline"], "url": "", "source": AI_NEWS_TODAY["source"]}
    except Exception:
        return {"headline": AI_NEWS_TODAY["headline"], "url": "", "source": AI_NEWS_TODAY["source"]}

def build_briefing():
    date_key = today_str()
    tool = TOOL_SPOTLIGHT.get(date_key)
    tali = TALI_STEPS.get(date_key)

    # Always-available CJ lookup for Running Courses block (from 3 July)
    cj_lookup = {
        "2026-07-03": {"quote": "\u201cData without context is noise. Context without data is intuition. The Vanguard leader needs both \u2014 and the analytics layer is where they meet.\u201d", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477984748645146624/"},
        "2026-07-04": {"quote": "\u201cTwo announcements, 24 hours apart. Sonnet 5 at near-Opus cost, Fable 5 restored globally. When platforms move this fast, the question is not what changed \u2014 it is whether your workflow moved with it.\u201d", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477984748645146624/"},
        "2026-07-05": {"quote": "\u201cTwo small updates from Anthropic this week that most people walked past. That is the adoption gap in real time.\u201d", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7478691596318916608/"},
        "2026-07-06": {"quote": "\u201cIn a world moving this fast, what does the next level of education for leaders actually look like? Not a degree. A practice.\u201d", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477256761729552384/"},
        "2026-07-07": {"quote": "\u201cHere is the full state of The Curator, honestly, not the pitch version. This is what it actually looks like when a tool is in production.\u201d", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7479782406443655169/"},
        "2026-07-08": {"quote": "\u201cSecond Brain has been stable since April.\u201d", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7479782406443655169/"},
        "2026-07-09": {"quote": "\U0001f4c4 <b>The Fight for Intelligence</b>", "url": "https://medium.com/@talirezun/the-fight-for-intelligence-6cd1f0925afc", "source": "Medium"},
        "2026-07-10": {"quote": "\U0001f4c4 <b>The Fight for Intelligence</b>", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7480874290544807936/"},
        "2026-07-11": {"quote": "\U0001f4c4 <b>The Fight for Intelligence</b>", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7480874290544807936/"},
        "2026-07-12": {"quote": "\U0001f4c4 <b>The Fight for Intelligence</b>", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7480874290544807936/"},
        "2026-07-13": {"quote": "\U0001f4c4 <b>If AI writes most of the code, who is left?</b>", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7476206245402689536/"},
    }

    lines = []

    # HEADER
    lines.append("🧭 <b>NAVIGATOR DAILY BRIEFING</b>")
    lines.append(today_label())
    lines.append("")

    # VANGUARD TEAMS
    lines.append("🏆 <b>VANGUARD TEAMS</b>")
    vanguard_teams_lines = {
        "2026-05-28": "The vanguard standard is not set in the big moments. It is set in the small ones — the ones no one is watching. Hold it anyway.",
        "2026-05-29": "You don\u2019t rise to the level of the opportunity. You fall to the level of your preparation. The tribe that prepares together performs together.",
        "2026-05-30": "In a NEO world, your tribe is your network and your network is your moat. Invest in it like it compounds — because it does.",
        "2026-05-31": "The tribes that endure are not built on enthusiasm — they are built on reliability. Show up. Every time. That is the whole strategy.",
        "2026-06-01": "Every great tribe has a moment where the work gets hard and the easy thing is to slow down. The vanguard does not slow down. It locks in.",
        "2026-06-02": "The cohort is not a classroom. It is a coordination network. Every connection you build here is a node in the system you will lead for decades.",
        "2026-06-03": "Exponential returns don\u2019t come from lone stars \u2014 they come from tribes that build together, trust each other, and refuse to stop. Your team is your compounding force.",
        "2026-06-04": "No one wins this alone. The teams that break through are the ones that show up for each other.",
        "2026-06-05": "A tribe without standards is just a group. Hold the standard — even when no one is watching. Especially when no one is watching.",
        "2026-06-06": "The vanguard standard is not set in the big moments. It is set in the small ones — the ones no one is watching. Hold it anyway.",
        "2026-06-07": "You don’t rise to the level of the opportunity. You fall to the level of your preparation. The tribe that prepares together performs together.",
        "2026-06-08": "In a NEO world, your tribe is your network and your network is your moat. Invest in it like it compounds — because it does.",
        "2026-06-09": "The tribes that endure are not built on enthusiasm — they are built on reliability. Show up. Every time. That is the whole strategy.",
        "2026-06-10": "Every great tribe has a moment where the work gets hard and the easy thing is to slow down. The vanguard does not slow down. It locks in.",
        "2026-06-11": "The cohort is not a classroom. It is a coordination network. Every connection you build here is a node in the system you will lead for decades.",
        "2026-06-12": "Exponential returns don’t come from lone stars — they come from tribes that build together, trust each other, and refuse to stop. Your team is your compounding force.",
        "2026-06-13": "The tribes that endure are not built on enthusiasm — they are built on reliability. Show up. Every time. That is the whole strategy.",
        "2026-06-14": "Every great tribe has a moment where the work gets hard and the easy thing is to slow down. The vanguard does not slow down. It locks in.",
        "2026-06-15": "The vanguard standard is not set in the big moments. It is set in the small ones — the ones no one is watching. Hold it anyway.",
        "2026-06-16": "Exponential returns don’t come from lone stars — they come from tribes that build together, trust each other, and refuse to stop. Your team is your compounding force.",
        "2026-06-17": "The vanguard does not wait for permission to lead. It moves first, creates clarity for others, and pulls the group forward.",
        "2026-06-18": "Tribes don’t wait to be built. They are chosen — one decision, one contribution, one standard held at a time.",
        "2026-06-19": "Not in a team yet? Put up your hand — reach out to a Chief and get involved.",
        "2026-06-20": "The standard you hold on Day 2 — when the energy dips and the novelty is gone — is the one that actually defines your tribe.",
        "2026-06-21": "Finish what you started. The final day is not a formality — it is where commitment becomes identity.",
        "2026-06-22": "The cohort that debriefs together after a hard session learns faster than the one that simply moves on. What did you take from the marathon?",
        "2026-06-23": "Trust is not declared. It is demonstrated — one delivered promise at a time. What will you deliver today?",
        "2026-06-24": "Your network is not a list of contacts. It is the accumulated record of every promise kept, every standard held, every person you showed up for.",
        "2026-06-25": "Psychological safety is not about being comfortable. It is about being able to say: I do not know. I was wrong. I disagree. Without it, the tribe cannot hear its own truth.",
        "2026-06-26": "The Vanguard leader does not wait for certainty. They act on the best available information, build in feedback, and correct fast. Speed with sustainability. Movement with purpose.",
        "2026-06-27": "Standards compound. Every time you hold the standard when it is expensive, you invest in your future. Every time you let it slide for convenience, you degrade it. The direction matters more than any single moment.",
        "2026-06-28": "The quarter is always more urgent than the decade. The Vanguard leader's discipline is to ask, before every significant decision: what does this look like in ten years?",
        "2026-06-29": "Benedetto Cotrugli wrote the founding text of modern commerce in 1458. It was not published for 115 years. Some things are built for the long run — yours is one of them.",
        "2026-06-30": "Dubrovnik survived empires. Not through force — through reputation. Every promise you keep is a brick in your own republic.",
        "2026-07-01": "A republic of one is not a republic. Find the people who will hold the standard with you, and the standard becomes unbreakable.",
        "2026-07-02": "Every cohort has people doing the work quietly. Find them. Name what they are building. That is how a tribe becomes visible to itself.",
        "2026-07-03": "The cohort that ships something together remembers it longer than the cohort that only studied together. Find a reason to build.",
        "2026-07-04": "The wolf's Year 1 is always impressive. Hold the standard anyway. The three-year pattern does not lie.",
        "2026-07-05": "Scale without integrity is just a bigger problem. The standard you hold when the tribe is small is the one that determines what it becomes at scale.",
        "2026-07-06": "Don't trust without verification. In the NEO era, the leaders who endure are not the most confident — they are the most rigorous.",
        "2026-07-07": "The reputation you are building today was started by how you showed up last month. What are you adding to the ledger this week?",
        "2026-07-08": "The entries you make on the quiet, unremarkable days are the ones that decide what the ledger says when someone finally reads it.",
        "2026-07-09": "The tribe that stops fighting to stay sharp is not resting — it is losing ground it will have to fight twice as hard to get back.",
        "2026-07-10": "Trust is not the reward for winning the fight for intelligence. It is the only thing that lets the tribe keep fighting it together.",
        "2026-07-11": "The tribe that shows up in the room together is stronger than the tribe that only shows up in the group chat.",
        "2026-07-12": "The room empties, the group chat goes quiet, and what's left is whether you actually changed anything. That's the only scoreboard that counts.",
        "2026-07-13": "A tribe that talks about craft is a book club. A tribe that ships something every sprint is a guild.",
    }
    lines.append(vanguard_teams_lines.get(date_key, "The reputation you are building today was started by how you showed up last month. What are you adding to the ledger this week?"))
    lines.append("")

    # DEADLINES
    # BAW MODULE 2 PRE-DEPLOYMENT TASKS — 7 to 9 July
    if "2026-07-07" <= date_key <= "2026-07-09":
        lines.append("🔴 <b>DEADLINES</b>")
        lines.append("")
        if date_key == "2026-07-09":
            lines.append("⚠️ <b>BAW MODULE 2 PRE-DEPLOYMENT TASKS — DUE TODAY 16:00 CET</b>")
        else:
            lines.append("📋 <b>BAW Module 2 Pre-Deployment Tasks</b> — Due Thursday 9 July, 16:00 CET")
        lines.append("Complete: PayPal Mafia baseline report, SEC EDGAR, Google Patents, and Alerts tasks.")
        lines.append("<a href='https://cotrugli.online/courses/business-as-warfare/lessons/module-1-business-as-warfare/'>→ Submit via Cotrugli course portal</a>")
        lines.append("")

    # NEXT ZOOM / UPCOMING SESSION
    if date_key >= "2026-06-22":
        if date_key <= "2026-06-27":
            if date_key == "2026-06-27":
                lines.append("📅 <b>BUSINESS AS WARFARE — Zoom Session TODAY</b>")
            else:
                lines.append("📅 <b>BUSINESS AS WARFARE — Zoom Session</b>")
            lines.append("<i>Dr. Zrinko Petener</i>")
            lines.append("")
            if date_key == "2026-06-27":
                lines.append("\u2022 \U0001f5d3 Today 27 June @ 17:00 CET")
            else:
                lines.append("\u2022 \U0001f5d3 Saturday 27 June @ 17:00 CET")
            lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/25/?wm=1&mi=89281123748'>\u2192 Join Zoom Meeting</a>")
            lines.append("<b>Meeting ID:</b> 892 8112 3748 | <b>Passcode:</b> BUSasWAR")
            lines.append("")
        else:
            if date_key >= "2026-07-12":
                lines.append("📅 <b>NEXT ZOOM SESSION</b>")
                lines.append("<i>Sessions resume after the summer break — watch this space</i>")
                lines.append("")
            elif date_key == "2026-07-11":
                lines.append("📅 <b>NEXT ZOOM SESSION — TODAY</b>")
                lines.append("<i>Chasing Jarvis 5 — War Room with Dražen Kapusta &amp; Dr. Tali Režun</i>")
                lines.append("\u2022 \U0001f5d3 Today, Saturday 11 July 2026 @ 17:00 CET")
                lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/26/?wm=1&mi=83238383656'>\u2192 Join Zoom Meeting</a>")
                lines.append("<b>Meeting ID:</b> 832 3838 3656 | <b>Passcode:</b> JARVIS5")
                lines.append("")
            else:
                lines.append("📅 <b>NEXT ZOOM SESSION</b>")
                lines.append("<i>War Room with Dražen Kapusta &amp; Dr. Tali Režun</i>")
                lines.append("\u2022 \U0001f5d3 Saturday 11 July 2026")
                lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/25/?wm=1&mi=89281123748'>\u2192 Join Zoom Meeting</a>")
                lines.append("<b>Meeting ID:</b> 892 8112 3748 | <b>Passcode:</b> BUSasWAR2")
                lines.append("")
            if date_key >= "2026-07-03":
                lines.append("\U0001f4da <b>RUNNING COURSES</b>")
                lines.append("")
                lines.append("\U0001f3a7 <b>Business as Warfare — Module 1</b>")
                lines.append("<a href='https://stream.redcircle.com/episodes/80e855e2-4cef-48da-b7fe-e6fd58e69e7e/stream.mp3'>\u2192 PayPal Mafia podcast</a>")
                if date_key >= "2026-07-07":
                    lines.append("Three actions to complete before Module 2 \u2014 full detail at <a href='https://nardusduplooy-hue.github.io/navigator/navigator_app.html'>Business as Warfare \u2014 Module 1</a>.")
                lines.append("")
            elif date_key >= "2026-06-29":
                lines.append("\U0001f3a7 <b>BUSINESS AS WARFARE — MODULE 1</b>")
                lines.append("Listen to the PayPal Mafia podcast while it's fresh:")
                lines.append("<a href='https://stream.redcircle.com/episodes/80e855e2-4cef-48da-b7fe-e6fd58e69e7e/stream.mp3'>\u2192 Listen here</a>")
                lines.append("Also available under the Sessions tab on the <a href='https://nardusduplooy-hue.github.io/navigator/navigator_app.html'>Cotrugli Navigator app</a>.")
                lines.append("")
    elif date_key >= "2026-06-14":
        if date_key == "2026-06-19":
            lines.append("📅 <b>THIS WEEKEND MARATHON STARTING TODAY — Sales Management</b>")
        elif date_key == "2026-06-20":
            lines.append("📅 <b>THIS WEEKEND MARATHON — DAY 2 — Sales Management</b>")
        elif date_key == "2026-06-21":
            lines.append("📅 <b>THIS WEEKEND MARATHON — FINAL DAY — Sales Management</b>")
        elif date_key >= "2026-06-18":
            lines.append("📅 <b>THIS WEEKEND MARATHON — Sales Management</b>")
        else:
            lines.append("📅 <b>NEXT WEEKEND MARATHON — Sales Management</b>")
        lines.append("<i>Prof. Primož Hvala</i>")
        lines.append("")
        lines.append("Three days. Deep dive into sales strategy, key account management, sales force leadership, and AI in sales. Success in sales depends more on managing your sales force than knowing all the tricks — and in the NEO era, AI is changing every layer of it.")
        lines.append("")
        lines.append("\u2022 \U0001f5d3 Friday 19 June @ 09:00 CET — through Sunday 21 June")
        lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/20/?wm=1&amp;mi=89427239190'>\u2192 Join Zoom Meeting</a>")
        lines.append("<b>Meeting ID:</b> 894 2723 9190 | <b>Passcode:</b> saleslive")
        lines.append("")
        if date_key >= "2026-06-18":
            lines.append("📅 <b>BUSINESS AS WARFARE — Zoom Session</b>")
            lines.append("<i>Dr. Zrinko Petener</i>")
            lines.append("")
            lines.append("• 🗓 Saturday 27 June @ 17:00 CET")
            lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/25/?wm=1&mi=89281123748'>\u2192 Join Zoom Meeting</a>")
            lines.append("<b>Meeting ID:</b> 892 8112 3748 | <b>Passcode:</b> BUSasWAR")
            lines.append("")
    else:
        lines.append("📅 <b>NEXT ZOOM SESSION</b>")
        if date_key >= "2026-06-13":
            lines.append("• 🗓 <b>AI in B2B Sales — Module 2</b> | Today 13 June @ 17:00 CET")
            lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/24/?wm=1&amp;mi=84732424623'>\u2192 Join Zoom Meeting</a> | <b>ID:</b> 847 3242 4623 | <b>Passcode:</b> AI_Sales_2")
        elif date_key >= "2026-06-11":
            lines.append("• 🗓 <b>AI in B2B Sales — Module 2</b> | Saturday 13 June @ 17:00 CET")
            lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/24/?wm=1&amp;mi=84732424623'>\u2192 Join Zoom Meeting</a> | <b>ID:</b> 847 3242 4623 | <b>Passcode:</b> AI_Sales_2")
        elif date_key >= "2026-05-31":
            lines.append("• 🗓 Saturday 13 June @ 17:00 Belgrade/Bratislava/Ljubljana — AI in B2B Sales Module 2")
        else:
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
        elif date_key == "2026-05-28":
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
            lines.append("🔖 <b>Six releases in three weeks. Here\u2019s what changed in #TheCurator 3.0.1. Beta 13</b>")
            lines.append("<i>Too much context is chaos</i> — Dr. Tali Re\u017eun")
            lines.append("<a href='https://www.linkedin.com/feed/update/urn:li:activity:7463975452337156096/'>→ Dr. Tali Re\u017eun on LinkedIn</a>")
            lines.append("")
            lines.append("<b>📊 AI IN B2B SALES</b>")
            lines.append("<a href='https://cotrugli.online/wp-content/uploads/2026/04/Module1_AI_Force_Multiplier.pdf'>→ Module 1 — The Thesis &amp; Landscape: AI as Force Multiplier in B2B Sales</a>")
            lines.append("")
        elif date_key < "2026-06-14":
            lines.append("📊 <b>AI IN B2B SALES</b>")
            lines.append("<i>Delivered by Saša Pavlaković</i>")
            lines.append("")
            if date_key >= "2026-06-14":
                pass  # Module 2 complete
            elif date_key >= "2026-06-11":
                lines.append("\U0001f4ca <b>MODULE 2 \u2014 Individual Augmentation: Your Personal AI Sales Stack</b>")
                lines.append("<i>Saša Pavlaković</i>")
                lines.append("")
                lines.append("In our next live session, we\u2019ll build your personal AI sales stack from the ground up \u2014 prospecting with Apollo, meeting prep with Otter, CRM workflows in HubSpot, and strategic thinking with Claude/ChatGPT. Come ready to work \u2014 you\u2019ll leave with a fully designed personal AI workflow.")
                lines.append("")
                lines.append("")
            elif date_key >= "2026-06-02":
                lines.append("\U0001f4cb <b>ASSIGNMENT \u2014 Due before Module 2 (Saturday 13 June)</b>")
                lines.append("<b>Map. Submit. Bring it back.</b> Choose your product, map your B2B funnel, identify 3–5 friction points, and propose one AI lever per point. Deliverable: 1–2 page write-up or 3–5 slides (PDF or Google Slides). Think clearly, not lengthily. 📧 <a href='mailto:sasa.pavlakovic@cotrugli.eu'>sasa.pavlakovic@cotrugli.eu</a>")
                lines.append("")
                lines.append("<a href='https://cotrugli.online/wp-content/uploads/2026/04/Module1_AI_Force_Multiplier.pdf'>\u2192 Module 1 PDF</a> | <a href='https://stream.redcircle.com/episodes/5cbe03c7-4603-479e-bccd-81f231f95f89/stream.mp3'>\u2192 Module 1 Podcast</a>")
                lines.append("\U0001f6e0 HubSpot \u00b7 Apollo.io \u00b7 Otter.ai \u00b7 Claude / ChatGPT")
                lines.append("")
            else:
                lines.append("We are pleased to announce the start of a new module in your Vanguard MBA programme: <b>AI in B2B Sales</b>. This course is about turning AI into your unfair advantage in B2B sales. You\u2019ll get hands-on with tools like HubSpot, Apollo, and ChatGPT to level up your prospecting, prep like a pro for meetings, and walk into negotiations with sharper insights.")
                lines.append("")
                lines.append("By the end, you\u2019ll have a clear 90-day game plan to implement AI in a real business context. If you want to stay ahead of the curve — and not get replaced by it — this is where it starts.")
                lines.append("")
                lines.append("<b>📅 Next Session: Saturday 30 May — 17:00 CET</b>")
                lines.append("<b>Topic:</b> VANGUARD — AI in B2B Sales")
                lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/19/?wm=1&amp;mi=86987581433'>→ Join Zoom Meeting</a>")
                lines.append("<b>Meeting ID:</b> 869 8758 1433 | <b>Passcode:</b> AI_Sales")
                lines.append("")
                lines.append("<b>📊 Module 1 — The Thesis &amp; Landscape: AI as Force Multiplier in B2B Sales</b>")
                lines.append("<a href='https://cotrugli.online/wp-content/uploads/2026/04/Module1_AI_Force_Multiplier.pdf'>→ Module 1 PDF</a>")
                lines.append("")

    # CHASING JARVIS — Dr. Tali block (from 2 June; position moved just before Vanguard Leadership from 18 June)
    if date_key >= "2026-06-02" and date_key < "2026-06-18":
        # Pre-18 June: Chasing Jarvis appears here (original position)
        chasing_jarvis_entries = {
            "2026-06-02": {
                "quote": "\u201cThe machine is ready. The question is \u2014 are you?\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_chasingjarvis-chasingjarvis-aiagents-share-7467106207451897856-xPDj/",
            },
            "2026-06-03": {
                "quote": "\u201c95% of enterprise AI pilots produce no measurable business impact.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7467487084430299137/",
            },
            "2026-06-04": {
                "quote": "\u201cPope Leo XIV published Magnifica Humanitas on 15 May \u2014 a call to ensure AI serves human dignity, not replaces it.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7467875702097481729/",
            },
            "2026-06-05": {
                "quote": "\u201cTOKENS\u2026the new currency of intelligence.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7468211823654096896/",
            },
            "2026-06-06": {
                "quote": "\u201cTOKENS\u2026the new currency of intelligence.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7468353468613791744/",
            },
            "2026-06-07": {
                "quote": "\u201cContext is the Code: The Complete Three-Phase Process for Building with AI Agents.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7468977290987823104/",
            },
            "2026-06-08": {
                "quote": "\u201cContext is the Code: The Complete Three-Phase Process for Building with AI Agents.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7468977290987823104/",
            },
            "2026-06-09": {
                "quote": "\u201cKnowledge compounds. Just like experience.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7469636710654431233/",
            },
            "2026-06-10": {
                "quote": "\u201cTwo years of building with AI coding agents.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7470009990666248193/",
            },
            "2026-06-11": {
                "quote": "\u201cOnce upon a time, there was a model that existed only in whispers.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_fromlabtolife-ai-claudefable5-share-7470394320831832064-YYiE/",
            },
            "2026-06-12": {
                "quote": "\u201cI asked a Fable to audit my second brain.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7470727011125133314/",
            },
            "2026-06-13": {
                "quote": "\u201cI asked a Fable to audit my second brain.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7470727011125133314/",
            },
            "2026-06-14": {
                "quote": "\u201cThe US government just pulled Fable 5 and Mythos 5 from every non-American workflow. Overnight. Without warning.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_the-us-government-just-pulled-fable-5-and-share-7471438584655441920--AWk/",
            },
            "2026-06-15": {
                "quote": "\u201cTwo years of building with AI coding agents.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7470009990666248193/",
            },
            "2026-06-16": {
                "quote": "\u201cOrganisation of Tomorrow (\u00d8\u00d8T).\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7472198719535415296/",
            },
            "2026-06-17": {
                "quote": "\u201cI spent 18 months building something I had no name for.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_i-spent-18-months-building-something-i-had-share-7472570244776157185-Hd-z/",
            },
            "2026-06-18": {
                "quote": "\u201cThe hard limit on my production agentic stack was never the model intelligence.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_the-hard-limit-on-my-production-agentic-stack-share-7472948269506252800-uSKc/",
            },
            "2026-06-19": {
                "quote": "\u201cCan AI finally democratise the law?\u201d",
                "url": "https://talirezun.substack.com/p/law-code-can-ai-finally-democratise",
            },
            "2026-06-20": {
                "quote": "\u201cThe best coding model in the world lasted three days.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7473417268882780164/",
            },
            "2026-06-21": {
                "quote": "\u201cI stopped trying to keep up with support emails. I built an agent to do it for me.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7473784782359990272/",
            },
            "2026-06-22": {
                "quote": "\u201cThe team is not the bottleneck. The trust is.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7474142368551976960/",
            },
            "2026-06-23": {
                "quote": "\u201cEveryone is talking about loop engineering. Most of them are describing something that already existed.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_everyone-is-talking-about-loop-engineering-share-7474794617436098560-druA/",
            },
            "2026-06-24": {
                "quote": "\u201cEveryone is talking about loop engineering. Most of them are describing something that already existed.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_everyone-is-talking-about-loop-engineering-share-7474794617436098560-druA/",
            },
            "2026-06-25": {
                "quote": "\u201cThe models are not the moat. The workflows are not the moat. The people who know how to use them are.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_the-models-are-not-the-moat-share-7475520183344066560-Pq8r/",
            },
            "2026-06-26": {
                "quote": "\u201cThe bottleneck is no longer code. It is context and vision.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_i-almost-didnt-post-this-a-github-graph-share-7475844659043430403-Awgg/",
            },
            "2026-06-27": {
                "quote": "\u201cIf AI writes most of the code, who is left?\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_this-summer-the-same-question-keeps-surfacing-share-7476206242437242880-0Rgc/",
            },
            "2026-06-28": {
                "quote": "\u201cIf AI writes most of the code, who is left?\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_this-summer-the-same-question-keeps-surfacing-share-7476206242437242880-0Rgc/",
            },
            "2026-06-29": {
                "quote": "\u201cEveryone is talking about loop engineering. Most of them are describing something that already existed.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7474794620502323200/",
            },
            "2026-06-30": {
                "quote": "\u201cThe technical barrier is almost always psychological. You are one context package away from shipping.\u201d",
                "url": "https://www.linkedin.com/posts/talirezun_a-while-back-drazen-kapusta-the-principal-share-7477256758432915456-qK9G/",
            },
            "2026-07-01": {
                "quote": "\u201cThree levels of engineering: Prompt at the core, Context in the middle ring, Harness as the outer ring. Understanding the harness means understanding all three.\u201d",
                "url": "https://medium.com/@talirezun/blueprint-of-a-frontier-coding-agent-1059730d802a",
            },
            "2026-07-02": {
                "quote": "\u201cAnthropic sent two announcements 24 hours apart. The model race is no longer about capability \u2014 it is about who controls the infrastructure beneath it.\u201d",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477984748645146624/",
            },
            "2026-07-03": {
                "quote": "“Data without context is noise. Context without data is intuition. The Vanguard leader needs both — and the analytics layer is where they meet.”",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477984748645146624/",
            },
            "2026-07-04": {
                "quote": "“Two announcements, 24 hours apart. Sonnet 5 at near-Opus cost, Fable 5 restored globally. When platforms move this fast, the question is not what changed — it is whether your workflow moved with it.”",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477984748645146624/",
            },
            "2026-07-05": {
                "quote": "“Two small updates from Anthropic this week that most people walked past. That is the adoption gap in real time.”",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7478691596318916608/",
            },
            "2026-07-06": {
                "quote": "“In a world moving this fast, what does the next level of education for leaders actually look like? Not a degree. A practice.”",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477256761729552384/",
            },
            "2026-07-07": {
                "quote": "“Here is the full state of The Curator, honestly, not the pitch version. This is what it actually looks like when a tool is in production.”",
                "url": "https://www.linkedin.com/feed/update/urn:li:activity:7479782406443655169/",
            },
        }
        cj = chasing_jarvis_entries.get(date_key, chasing_jarvis_entries["2026-07-07"])
        lines.append("🎯 <b>CHASING JARVIS</b>")
        lines.append("<i>Dr. Tali Re\u017eun</i>")
        lines.append("")
        lines.append(cj["quote"])
        lines.append("<a href='" + cj["url"] + "'>→ Dr. Tali Re\u017eun on LinkedIn</a>")
        lines.append("")

    # MODULE 2 ASSIGNMENT — from 15 June onwards
    if date_key >= "2026-06-15":
        if date_key >= "2026-07-03":
            lines.append("\U0001f4cb <b>AI in B2B Sales — Module 2</b>")
            lines.append("<i>Saša Pavlaković</i>")
            lines.append("\U0001f4fa <b>Recording:</b> <a href='https://cotrugli.online/courses/ai-sales/lessons/the-thesis-landscape/'>→ Watch here</a>")
            lines.append("")
            lines.append("\U0001f4ca <b>Analytics</b>")
            lines.append("<a href='https://cotrugli.online/courses/vanguard-mba-analytics/lessons/introduction/'>→ Start here</a>")
            lines.append("")
            if date_key <= "2026-07-12":
                if date_key == "2026-07-12":
                    lines.append("\u26a0\ufe0f <b>Sales Management — EXAM DUE TODAY, MIDNIGHT</b>")
                else:
                    lines.append("\U0001f4dd <b>Sales Management — Exam deadline Sunday 12 July, midnight</b>")
                lines.append("<i>Prof. Primž Hvala</i>")
                lines.append("Upload at <a href='https://cotrugli.online/'>Alumni Portal</a> — name at top of document.")
                lines.append("")
            # Chasing Jarvis inside Running Courses from 3 July
            cj_rc = cj_lookup.get(date_key, cj_lookup["2026-07-03"])
            lines.append("\U0001f3af <b>Chasing Jarvis — Dr. Tali Režun</b>")
            lines.append("")
            lines.append(cj_rc["quote"])
            cj_source = cj_rc.get("source", "LinkedIn")
            lines.append("<a href='" + cj_rc["url"] + "'>→ Dr. Tali Režun on " + cj_source + "</a>")
            lines.append("")
            # VANGUARD SPRINT PROGRAMME — from 8 July onwards
            if date_key >= "2026-07-08":
                lines.append("\U0001f680 <b>VANGUARD SPRINT PROGRAMME</b>")
                lines.append(
                    "<blockquote><i>All Chiefs · All Tribes · Sprint 2 in progress</i>\n\n"
                    "The Vanguard Sprint Programme runs across Chasing Jarvis, AI in B2B Sales and Entrepreneurship "
                    "simultaneously. Every two weeks, your tribe advances your Chief's MVP — building a real "
                    "product, for a real market, with real deliverables. More modules will integrate as the "
                    "programme progresses.\n\n"
                    "<i>This week: what did your tribe ship?</i></blockquote>"
                )
                lines.append("")
        elif date_key >= "2026-06-18":
            lines.append("\U0001f4cb <b>AI in B2B Sales: MODULE 2 ASSIGNMENT — AI as Force Multiplier</b>")
            lines.append("<i>Saša Pavlaković</i>")
            if date_key >= "2026-06-27":
                lines.append("\U0001f4fa <b>RECORDING OF SESSION 2</b> <a href='https://cotrugli.online/courses/ai-sales/lessons/the-thesis-landscape/'>→ Watch here</a>")
                lines.append("")
            if date_key >= "2026-06-28":
                lines.append("\U0001f4dd <b>SALES MANAGEMENT — EXAMINATION DEADLINE</b>")
                lines.append("<i>Prof. Prim\u017e Hvala</i>")
                lines.append("")
                lines.append("Upload your final exam at the <a href='https://cotrugli.online/'>Alumni Portal</a> by <b>Sunday 12 July 2026, midnight</b>.")
                if date_key < "2026-07-02":
                    lines.append("\u2022 Put your name at the beginning of the exam")
                    lines.append("\u2022 Sales Management materials available at Alumni Portal")
                    lines.append("\u2022 Please complete the <b>module evaluation</b> at Alumni Portal")
                lines.append("")
            lines.append("")
            if date_key < "2026-06-26":
                lines.append("Document one AI sales workflow you actually tested. Pick any single workflow from the module — prospecting via Apollo, LLM-augmented outreach, the Otter post-meeting flow, or the MEDDICC pipeline audit — and walk through 3–5 steps with screenshots or a short Loom recording.")
                lines.append("")
                lines.append("\u2022 Include the exact prompts you used")
                lines.append("\u2022 Show the real output (anonymised if needed)")
                lines.append("\u2022 One honest paragraph: what worked, what didn\u2019t, what you\u2019d change")
                lines.append("")
                lines.append("<b>Graded on:</b> Workflow specificity (30%) \u00b7 Prompt quality (25%) \u00b7 Honest reflection (25%) \u00b7 Polish (20%)")
                lines.append("<b>Bonus:</b> Connect one tool to Claude and let it make a live CRM write — bring that to Module 3 as a tribal seed.")
            lines.append("")
        else:
            lines.append("\U0001f4cb <b>MODULE 2 ASSIGNMENT — AI as Force Multiplier</b>")
            lines.append("<i>Saša Pavlaković</i>")
            lines.append("")

    # SALES MANAGEMENT WEEKEND MARATHON — shown in zoom slot from 14 June onwards
    if date_key >= "2026-06-14":
        pass  # Already shown in zoom slot above
    elif date_key >= "2026-06-03":
        lines.append("📅 <b>NEXT WEEKEND MARATHON — Sales Management</b>")
        lines.append("<i>Prof. Primo\u017e Hvala</i>")
        lines.append("")
        lines.append("Three days. Deep dive into sales strategy, key account management, sales force leadership, and AI in sales. Success in sales depends more on managing your sales force than knowing all the tricks — and in the NEO era, AI is changing every layer of it.")
        lines.append("")
        lines.append("\u2022 \U0001f5d3 Friday 19 June @ 09:00 CET — through Sunday 21 June")
        lines.append("<a href='https://cotrugli.online/groups/vanguard/zoom/meetings/20/?wm=1&amp;mi=89427239190'>→ Join Zoom Meeting</a>")
        lines.append("<b>Meeting ID:</b> 894 2723 9190 | <b>Passcode:</b> saleslive")
        lines.append("")

    # CHASING JARVIS — new position from 18 June (just before Vanguard Leadership)
    # From 3 July it appears inside RUNNING COURSES block above
    if date_key >= "2026-06-18" and date_key < "2026-07-03":
        cj_entries = {
            "2026-06-02": {"quote": "“The machine is ready. The question is — are you?”", "url": "https://www.linkedin.com/posts/talirezun_chasingjarvis-chasingjarvis-aiagents-share-7467106207451897856-xPDj/"},
            "2026-06-03": {"quote": "“95% of enterprise AI pilots produce no measurable business impact.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7467487084430299137/"},
            "2026-06-14": {"quote": "“The US government just pulled Fable 5 and Mythos 5 from every non-American workflow. Overnight. Without warning.”", "url": "https://www.linkedin.com/posts/talirezun_the-us-government-just-pulled-fable-5-and-share-7471438584655441920--AWk/"},
            "2026-06-16": {"quote": "“Organisation of Tomorrow (ØØT).”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7472198719535415296/"},
            "2026-06-17": {"quote": "“I spent 18 months building something I had no name for.”", "url": "https://www.linkedin.com/posts/talirezun_i-spent-18-months-building-something-i-had-share-7472570244776157185-Hd-z/"},
            "2026-06-18": {"quote": "“The hard limit on my production agentic stack was never the model intelligence.”", "url": "https://www.linkedin.com/posts/talirezun_the-hard-limit-on-my-production-agentic-stack-share-7472948269506252800-uSKc/"},
            "2026-06-19": {"quote": "“Can AI finally democratise the law?”", "url": "https://talirezun.substack.com/p/law-code-can-ai-finally-democratise"},
            "2026-06-20": {"quote": "“The best coding model in the world lasted three days.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7473417268882780164/"},
            "2026-06-21": {"quote": "“I stopped trying to keep up with support emails. I built an agent to do it for me.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7473784782359990272/"},
            "2026-06-22": {"quote": "“The team is not the bottleneck. The trust is.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7474142368551976960/"},
            "2026-06-23": {"quote": "“Everyone is talking about loop engineering. Most of them are describing something that already existed.”", "url": "https://www.linkedin.com/posts/talirezun_everyone-is-talking-about-loop-engineering-share-7474794617436098560-druA/"},
            "2026-06-24": {"quote": "“Everyone is talking about loop engineering. Most of them are describing something that already existed.”", "url": "https://www.linkedin.com/posts/talirezun_everyone-is-talking-about-loop-engineering-share-7474794617436098560-druA/"},
            "2026-06-25": {"quote": "“The models are not the moat. The workflows are not the moat. The people who know how to use them are.”", "url": "https://www.linkedin.com/posts/talirezun_the-models-are-not-the-moat-share-7475520183344066560-Pq8r/"},
            "2026-06-26": {"quote": "“The bottleneck is no longer code. It is context and vision.”", "url": "https://www.linkedin.com/posts/talirezun_i-almost-didnt-post-this-a-github-graph-share-7475844659043430403-Awgg/"},
            "2026-06-27": {"quote": "“If AI writes most of the code, who is left?”", "url": "https://www.linkedin.com/posts/talirezun_this-summer-the-same-question-keeps-surfacing-share-7476206242437242880-0Rgc/"},
            "2026-06-28": {"quote": "“If AI writes most of the code, who is left?”", "url": "https://www.linkedin.com/posts/talirezun_this-summer-the-same-question-keeps-surfacing-share-7476206242437242880-0Rgc/"},
            "2026-06-29": {"quote": "“Everyone is talking about loop engineering. Most of them are describing something that already existed.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7474794620502323200/"},
            "2026-06-30": {"quote": "“The technical barrier is almost always psychological. You are one context package away from shipping.”", "url": "https://www.linkedin.com/posts/talirezun_a-while-back-drazen-kapusta-the-principal-share-7477256758432915456-qK9G/"},
            "2026-07-01": {"quote": "“Three levels of engineering: Prompt at the core, Context in the middle ring, Harness as the outer ring. Understanding the harness means understanding all three.”", "url": "https://medium.com/@talirezun/blueprint-of-a-frontier-coding-agent-1059730d802a"},
            "2026-07-02": {"quote": "“Anthropic sent two announcements 24 hours apart. The model race is no longer about capability — it is about who controls the infrastructure beneath it.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477984748645146624/"},
            "2026-07-03": {"quote": "“Data without context is noise. Context without data is intuition. The Vanguard leader needs both — and the analytics layer is where they meet.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477984748645146624/"},
            "2026-07-04": {"quote": "“Two announcements, 24 hours apart. Sonnet 5 at near-Opus cost, Fable 5 restored globally. When platforms move this fast, the question is not what changed — it is whether your workflow moved with it.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477984748645146624/"},
            "2026-07-05": {"quote": "“Two small updates from Anthropic this week that most people walked past. That is the adoption gap in real time.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7478691596318916608/"},
            "2026-07-06": {"quote": "“In a world moving this fast, what does the next level of education for leaders actually look like? Not a degree. A practice.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7477256761729552384/"},
            "2026-07-07": {"quote": "“Here is the full state of The Curator, honestly, not the pitch version. This is what it actually looks like when a tool is in production.”", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7479782406443655169/"},
        }
        cj = cj_entries.get(date_key, cj_entries["2026-07-07"])
        lines.append("🎯 <b>CHASING JARVIS</b>")
        lines.append("<i>Dr. Tali Režun</i>")
        lines.append("")
        lines.append(cj["quote"])
        lines.append("<a href='" + cj["url"] + "'>→ Dr. Tali Režun on LinkedIn</a>")
        lines.append("")

    # STUDENT LINKEDIN ARTICLES — from 2 July
    if date_key >= "2026-07-02":
        lines.append("\U0001f4f0 <b>STUDENT LINKEDIN ARTICLES</b>")
        lines.append("")
        if date_key < "2026-07-06":
            lines.append("\U0001f4cc <b>Skin in the game</b> — Matthys van Rooyen")
            lines.append("<a href='https://www.linkedin.com/feed/update/urn:li:activity:7471288144236048384/'>→ Read on LinkedIn</a>")
            lines.append("")
        if "2026-07-05" <= date_key < "2026-07-09":
            lines.append("\U0001f4cc <b>SA\u2019s AI Policy: what it means on the ground</b> — Matthys van Rooyen")
            lines.append("<a href='https://www.linkedin.com/feed/update/urn:li:ugcPost:7472553564662562818/'>→ Read on LinkedIn</a>")
            lines.append("")
        if date_key >= "2026-07-09":
            lines.append("\U0001f4cc <b>The Wolf that guards the sheep</b> — Matthys van Rooyen")
            lines.append("<a href='https://www.linkedin.com/feed/update/urn:li:activity:7480168741188747265/'>→ Read on LinkedIn</a>")
            lines.append("")
        if date_key >= "2026-07-13":
            lines.append("\U0001f4cc <b>Raising the Floor: The Role of the Junior Developer in the AI Era</b> — Matthys van Rooyen")
            lines.append("<a href='https://www.linkedin.com/feed/update/urn:li:activity:7475080819590557698/'>→ Read on LinkedIn</a>")
            lines.append("")
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
        if date_key not in ("2026-05-28",):
            if date_key >= "2026-07-06":
                lines.append("<a href='" + KAPUSTA_TODAY["url"] + "'>→ Read more on LinkedIn — Dra\u017een Kapusta</a>")
            elif date_key >= "2026-05-30":
                lines.append("<a href='https://www.linkedin.com/pulse/neo-cotruglian-philosophy-leadership-operating-system-drazen-kapusta-z03of/?trackingId=yjbjhb2qREidGPz36JtTRQ%3D%3D'>→ Read more on LinkedIn — Dra\u017een Kapusta</a>")
            else:
                lines.append("<a href='https://www.linkedin.com/posts/cotrugli_thucydidestrap-leadership-geopolitics-share-7462394444852379648-OMgP?utm_source=share&utm_medium=member_android&rcm=ACoAAABVXjQBjD1rAkelAiZQjLIpnQRQFS6tooE'>→ Read more on LinkedIn — Dra\u017een Kapusta</a>")
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
    # --date YYYY-MM-DD overrides today's date for previewing future briefings
    if "--date" in sys.argv:
        idx = sys.argv.index("--date")
        if idx + 1 < len(sys.argv):
            import daily_briefing as _self
            _self._DATE_OVERRIDE = sys.argv[idx + 1]
            _DATE_OVERRIDE = sys.argv[idx + 1]

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
