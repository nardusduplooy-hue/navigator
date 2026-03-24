import json
import asyncio
import random
import os
from datetime import datetime
import anthropic
from telegram import Bot
from dotenv import load_dotenv
from jarvis_content import (
    MODULE_4_TALI,
    KAPUSTA_ARTICLES,
    KAPUSTA_WFR_ARTICLE,
    MODULE_1_TALI, MODULE_2_TALI, MODULE_1_ASSIGNMENTS, TOOLS_EXPLAINED, SUPPLEMENTARY, LLM_MANUAL_CHAPTERS, NEO_WORLD_ARTICLES
)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

def fetch_rundown_headline():
    """Fetch the latest headline from The Rundown AI RSS feed with retry."""
    import urllib.request
    import xml.etree.ElementTree as ET
    import time as _time
    url = "https://rss.beehiiv.com/feeds/2R3C6Bt5wj.xml"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as response:
                xml_data = response.read()
            root = ET.fromstring(xml_data)
            channel = root.find("channel")
            item = channel.find("item")
            title = item.find("title").text.strip()
            link = item.find("link").text.strip()
            return title, link
        except Exception:
            if attempt < 2:
                _time.sleep(10)
    return None, None

def generate_daily_question_and_answer(assignment_text, why_it_matters):
    """Use Claude to generate a creative question AND model answer based on yesterday's assignment."""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    prompt = f"""You are Navigator, an AI tutor for MBA students in the COTRUGLI Vanguard programme.

Yesterday's assignment was: {assignment_text}
Why it matters: {why_it_matters}

Generate ONE creative, thought-provoking test question and a model answer.

Requirements for the question:
- Tests deep understanding, not just recall
- Uses a real-world analogy or scenario (like comparing AI to something unexpected)
- Is specific enough that a vague answer would not suffice
- Is 1-3 sentences maximum

Requirements for the answer:
- Practical and opinionated, not textbook
- 3-4 sentences maximum
- Written in Navigator's voice — direct, confident, MBA-level

Return ONLY this exact format:
QUESTION: [your question here]
ANSWER: [your answer here]"""

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}]
    )
    text = response.content[0].text.strip()
    lines = text.split("\n")
    question = ""
    answer = ""
    for line in lines:
        if line.startswith("QUESTION:"):
            question = line.replace("QUESTION:", "").strip()
        elif line.startswith("ANSWER:"):
            answer = line.replace("ANSWER:", "").strip()
    return question, answer

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# Chat IDs now loaded from subscribers.json
CHAT_IDS = []

# Noise blocks to filter out from portal scraping
NOISE_BLOCKS = [
    "the moment we've been building toward",
    "officially kicks off",
    "february 20",
    "february 21",
    "february 22",
    "dates:february",
    "mandatory prework to be submitted by",
    "students are required to complete graded prework",
    "students were required to complete graded prework",
    "re: intro to the vanguard",
    "your next zook session is on saturday (january 10",
    "by the end of this course, students will be able to",
    "discussion of individual assignments is encouraged",
]

def get_portal_data():
    """Load and filter portal_data.json if it exists."""
    zoom_link = None
    deadlines = []

    try:
        with open("portal_data.json") as f:
            pages = json.load(f)

        # Get most recent Zoom meeting link (highest session number)
        best_session = 0
        for page in pages:
            for z in page["zoom_links"]:
                if "/zoom/meetings/" in z["url"]:
                    try:
                        num = int(z["url"].rstrip("/").split("/")[-1].split("?")[0])
                        if num > best_session:
                            best_session = num
                            zoom_link = z
                    except:
                        pass

        # Get deadline blocks — filter noise, deduplicate
        seen = set()
        future_keywords = ["march", "april", "may", "june", "2026", "2027"]
        for page in pages:
            for d in page["deadlines"]:
                d_lower = d.lower()
                # Skip noise
                if any(noise in d_lower for noise in NOISE_BLOCKS):
                    continue
                # Prefer blocks with future dates
                if any(kw in d_lower for kw in future_keywords):
                    if d not in seen and len(d) > 30:
                        seen.add(d)
                        deadlines.append(d[:200])

    except FileNotFoundError:
        pass

    return zoom_link, deadlines[:5]

async def send_daily_briefing(test_mode=False):
    bot = Bot(token=BOT_TOKEN)
    if test_mode:
        global CHAT_IDS
        CHAT_IDS = [8536765390]
    today = datetime.now().strftime("%A, %d %B %Y")

    # Load subscribers dynamically
    if not test_mode:
        try:
            import json as _subjson
            with open("subscribers.json") as _subf:
                _subs = _subjson.load(_subf)
            CHAT_IDS = [s["chat_id"] for s in _subs]
        except:
            CHAT_IDS = [8536765390]

    tali_m1 = MODULE_1_TALI
    tali_m2_preview = random.choice(MODULE_2_TALI)
    assignment = random.choice(MODULE_1_ASSIGNMENTS)
    tool = random.choice(TOOLS_EXPLAINED)
    supp = random.choice(SUPPLEMENTARY)

    zoom_link, portal_deadlines = get_portal_data()

    msg = f"🧭 *NAVIGATOR DAILY BRIEFING*\n_{today}_\n\n"

    # DEADLINES
    import json as _json
    try:
        with open("deadlines.json") as _f:
            _deadlines = _json.load(_f)
    except:
        _deadlines = []
    msg += "🔴 *DEADLINES*\n"
    for _d in _deadlines:
        if _d["status"] in ["active", "upcoming"]:
            from datetime import timezone
            _due_dt = None
            try:
                from datetime import datetime as _dt
                _due_dt = _dt.fromisoformat(_d['due'].replace('Z','+00:00'))
                _diff = _due_dt - _dt.now(timezone.utc)
                _days = _diff.days
                _hours = _diff.seconds // 3600
                _countdown = f" *(T-{_days}d {_hours}h)*" if _diff.total_seconds() > 0 else " *(OVERDUE)*"
            except:
                _countdown = ""
            msg += f"• *{_d['name']}* — {_d['display_due']}{_countdown}\n"
            msg += f"  {_d['details']}\n"
            if _d.get("link"):
                if 'zoom' in _d.get('link', '').lower():
                    msg += f"  [Zoom Link]({_d['link']})\n"
                else:
                    msg += f"  [Submit here]({_d['link']})\n"
    msg += "\n"

    # NEXT SESSION
    msg += "📅 *NEXT ZOOM SESSION*\n"
    msg += "• Vanguard Session 9 — Chasing Jarvis Module 3 — Sat April 4 (estimated)\n"
    msg += "  Zoom link to be confirmed\n"
    msg += "• [Zoom Recordings — all sessions](https://cotrugli.online/groups/vanguard/zoom/meetings/4)\n"
    msg += "\n"

    # STATUS
    msg += "✅ *STATUS*\n"
    msg += "• All JTBDs current\n"
    msg += "• JTBD — [Comment posted on Dr. Tali LinkedIn](https://www.linkedin.com/posts/talirezun_intent-chasingjarvis-chasingjarvis-share-7441742562106966016-nmBH)\n"
    msg += "• Hult — Submitted & Under Review\n"
    msg += "• Awaiting Future of Work multiple choice exam results\n"
    msg += "• Future of Work Essay — Submitted, awaiting results and feedback\n"
    msg += "\n"

    # CHASING JARVIS
    msg += "🎯 *CHASING JARVIS — TODAY'S FOCUS*\n\n"

    msg += "🔜 *Module 2 preview — coming April 4:*\n"
    msg += f"• [{tali_m2_preview['title']}]({tali_m2_preview['url']})\n"
    msg += f"  _{tali_m2_preview['note']}_\n\n"

    msg += "📝 *Module 2 — Prepare for Session 9 (April 4):*\n"
    msg += "_Create accounts and explore these tools — then decide what goes into YOUR personal AI stack:_\n\n"
    msg += "→ [Qwen](https://chat.qwen.ai/) & [LM Studio](https://lmstudio.ai/) — run LLMs locally\n"
    msg += "→ [Hugging Face](https://huggingface.co/) — open-source model hub\n"
    msg += "→ [GitHub](https://github.com/) & [GitBook](https://www.gitbook.com/) — code + docs + AI integrations\n"
    msg += "→ [Cloudflare](https://www.cloudflare.com/) — AI on the edge\n"
    msg += "→ [Nano Banana Pro](https://nanobananago.com/) & [Veo](https://deepmind.google/technologies/veo/) — explore\n"
    msg += "→ [Claude Desktop Agent](https://claude.ai/download) — local agent\n"
    msg += "→ [VS Code](https://code.visualstudio.com/) + [Augment Code](https://www.augmentcode.com/) — your dev environment\n"
    msg += "→ [Google Antigravity](https://sites.research.google/antigravity/) — explore\n"
    msg += "→ [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) — agentic coding\n\n"
    msg += "_Explore, break things, and decide what goes into YOUR personal AI stack._\n\n"
    msg += "\n"

    msg += f"🔧 *Tool to understand today — {tool['module']}:*\n"
    msg += f"*{tool['tool']}*\n"
    msg += f"[Access here]({tool['link']})\n"
    msg += f"_{tool['description']}_\n\n"

    msg += f"📚 *Supplementary resource — {supp['module']}:*\n"
    msg += f"[{supp['title']}]({supp['url']})\n"
    msg += f"_{supp['note']}_\n\n"

    msg += "🏛️ *VANGUARD LEADERSHIP — Kapusta reading:*\n"
    for article in KAPUSTA_ARTICLES:
            msg += f"• [{article['title']}]({article['url']})\n"
            msg += f"  _{article['note']}_\n"
    msg += "\n"
    _neo = NEO_WORLD_ARTICLES[datetime.now().timetuple().tm_yday % len(NEO_WORLD_ARTICLES)]
    msg += "📰 *Must-read — NEO World & AI Commerce:*\n"
    msg += f"[{_neo['title']}]({_neo['url']})\n"
    msg += f"_{_neo['note']}_ — {_neo['authors']}\n\n"
    # Fetch Rundown AI headline
    rundown_title, rundown_link = fetch_rundown_headline()
    if rundown_title and rundown_link:
        msg += "🌐 *AI NEWS — THE RUNDOWN:*\n"
        msg += f"[{rundown_title}]({rundown_link})\n"
        msg += "_therundown.ai — free to read_\n\n"

    # Generate daily knowledge question based on yesterday's assignment
    yesterday_assignment = random.choice([a for a in MODULE_1_ASSIGNMENTS if a != assignment])
    daily_question = ""
    daily_answer = ""
    try:
        daily_question, daily_answer = generate_daily_question_and_answer(
            yesterday_assignment['assignment'],
            yesterday_assignment['why']
        )
        msg += "🧠 *Test your knowledge from yesterday's reading:*\n"
        msg += f"_{daily_question}_\n\n"
    except Exception as e:
        pass

    msg += "⚡ _Navigator out._"

    for chat_id in CHAT_IDS:
        await bot.send_message(
            chat_id=chat_id,
            text=msg,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
        print(f"✅ Briefing sent to {chat_id}")

    # Wait 30 minutes then send the model answer
    if daily_answer:
        await asyncio.sleep(1800)
        answer_msg = f"🧠 *Model answer to this morning's question:*\n\n_{daily_answer}_\n\n⚡ _Navigator out._"
        for chat_id in CHAT_IDS:
            await bot.send_message(
                chat_id=chat_id,
                text=answer_msg,
                parse_mode="Markdown",
                disable_web_page_preview=True
            )
            print(f"✅ Answer sent to {chat_id}")

if __name__ == "__main__":
    import sys
    TEST_MODE = "--test" in sys.argv
    if TEST_MODE:
        CHAT_IDS = [8536765390]  # Only Nardus
        print("🧪 TEST MODE — sending only to Nardus")
    asyncio.run(send_daily_briefing(test_mode=TEST_MODE))
