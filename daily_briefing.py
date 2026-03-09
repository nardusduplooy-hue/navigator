import json
import asyncio
import random
from datetime import datetime
from telegram import Bot
from dotenv import load_dotenv
import os
from jarvis_content import (
    MODULE_1_TALI,
    MODULE_2_TALI,
    MODULE_1_ASSIGNMENTS,
    TOOLS_EXPLAINED,
    SUPPLEMENTARY
)

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_IDS = [1357019604, 285802287]

async def send_daily_briefing():
    bot = Bot(token=BOT_TOKEN)
    today = datetime.now().strftime("%A, %d %B %Y")

    # Always both Module 1 Tali articles + 1 Module 2 preview
    tali_m1 = MODULE_1_TALI  # both, always
    tali_m2_preview = random.choice(MODULE_2_TALI)
    assignment = random.choice(MODULE_1_ASSIGNMENTS)
    tool = random.choice(TOOLS_EXPLAINED)
    supp = random.choice(SUPPLEMENTARY)

    msg = f"🧭 *NAVIGATOR DAILY BRIEFING*\n_{today}_\n\n"

    msg += "🔴 *DEADLINES*\n"
    msg += "• Future of Work essay — March 23, 19:00 CET\n\n"

    msg += "📅 *NEXT SESSION*\n"
    msg += "• Chasing Jarvis Session 2 — Saturday March 21 (estimated)\n\n"

    msg += "✅ *STATUS*\n"
    msg += "• All JTBDs current\n"
    msg += "• Hult — Submitted & Under Review\n\n"

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
    msg += f"Prepare with:\n"
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
