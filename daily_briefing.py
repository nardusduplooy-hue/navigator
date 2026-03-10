import json
import asyncio
import random
import os
from datetime import datetime
from telegram import Bot
from dotenv import load_dotenv
from jarvis_content import (
    MODULE_4_TALI,
    KAPUSTA_ARTICLES,
    KAPUSTA_WFR_ARTICLE,
    MODULE_1_TALI, MODULE_2_TALI, MODULE_1_ASSIGNMENTS, TOOLS_EXPLAINED, SUPPLEMENTARY
)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

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

async def send_daily_briefing():
    bot = Bot(token=BOT_TOKEN)
    today = datetime.now().strftime("%A, %d %B %Y")

    # Load subscribers dynamically
    try:
        import json as _subjson
        with open("subscribers.json") as _subf:
            _subs = _subjson.load(_subf)
        CHAT_IDS = [s["chat_id"] for s in _subs]
    except:
        CHAT_IDS = [1357019604]

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
            msg += f"• *{_d['name']}* — {_d['display_due']}\n"
            msg += f"  {_d['details']}\n"
            if _d.get("link"):
                msg += f"  [Submit here]({_d['link']})\n"
    msg += "\n"

    # NEXT SESSION
    msg += "📅 *NEXT ZOOM SESSION*\n"
    msg += "• Chasing Jarvis Session 2 — Saturday March 21 (estimated)\n"
    if zoom_link:
        msg += f"• [Last Zoom Session — Vanguard Session 7 · Chasing Jarvis Module 1 · Sat March 7]({zoom_link['url']})\n"
    msg += "\n"

    # STATUS
    msg += "✅ *STATUS*\n"
    msg += "• All JTBDs current\n"
    msg += "• Hult — Submitted & Under Review\n\n"

    # CHASING JARVIS
    msg += "🎯 *CHASING JARVIS — TODAY'S FOCUS*\n\n"

    msg += "📖 *Module 1 — Dr. Tali's required reading:*\n"
    for article in tali_m1:
        msg += f"• [{article['title']}]({article['url']})\n"
        msg += f"  _{article['note']}_\n"
    msg += "\n"

    msg += "🔜 *Module 2 preview — coming March 21:*\n"
    msg += f"• [{tali_m2_preview['title']}]({tali_m2_preview['url']})\n"
    msg += f"  _{tali_m2_preview['note']}_\n\n"

    msg += f"📝 *Module 1 assignment to prepare:*\n"
    msg += f"_{assignment['assignment']}_\n\n"
    msg += f"Why it matters: {assignment['why']}\n\n"
    msg += "Prepare with:\n"
    for name, url in assignment['prep_links']:
        msg += f"• [{name}]({url})\n"
    msg += "\n"

    msg += f"🔧 *Tool to understand today — {tool['module']}:*\n"
    msg += f"*{tool['tool']}*\n"
    msg += f"[Access here]({tool['link']})\n"
    msg += f"_{tool['description']}_\n\n"

    msg += f"📚 *Supplementary resource — {supp['module']}:*\n"
    msg += f"[{supp['title']}]({supp['url']})\n"
    msg += f"_{supp['note']}_\n\n"

    msg += "🏛️ *Vanguard Leadership — Kapusta reading:*\n"
    for article in KAPUSTA_ARTICLES:
        msg += f"• [{article['title']}]({article['url']})\n"
        msg += f"  _{article['note']}_\n"
    msg += "\n"
    msg += "📰 *Must-read — NEO World & AI Commerce:*\n"
    msg += f"[{KAPUSTA_WFR_ARTICLE['title']}]({KAPUSTA_WFR_ARTICLE['url']})\n"
    msg += f"_{KAPUSTA_WFR_ARTICLE['note']}_ — {KAPUSTA_WFR_ARTICLE['authors']}\n\n"
    msg += "⚡ _Navigator out._"

    for chat_id in CHAT_IDS:
        await bot.send_message(
            chat_id=chat_id,
            text=msg,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
        print(f"✅ Briefing sent to {chat_id}")

asyncio.run(send_daily_briefing())
