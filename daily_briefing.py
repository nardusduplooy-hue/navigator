import json
import asyncio
import random
from datetime import datetime
from telegram import Bot
from dotenv import load_dotenv
import os
from jarvis_content import (
    MODULE_1_PREREADING, MODULE_2_PREREADING,
    MODULE_1_ASSIGNMENTS, MODULE_2_ASSIGNMENTS,
    TOOLS_EXPLAINED
)

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_IDS = [1357019604, 285802287]

ARTICLES = [
    ("Anthropic Research Blog", "https://www.anthropic.com/research"),
    ("Philipp Schmid — Context Engineering", "https://www.philschmid.de/context-engineering"),
    ("Simon Willison's AI Blog", "https://simonwillison.net"),
    ("Andrej Karpathy Blog", "https://karpathy.ai"),
    ("VentureBeat AI", "https://venturebeat.com/ai/"),
    ("TechCrunch AI", "https://techcrunch.com/category/artificial-intelligence/"),
    ("DeepMind Blog", "https://www.deepmind.com/blog"),
    ("OpenAI Blog", "https://openai.com/blog"),
    ("AI Snake Oil — Critical AI Thinking", "https://www.aisnakeoil.com"),
    ("Benedict Evans — Tech & Business", "https://www.ben-evans.com"),
    ("HuggingFace Blog", "https://huggingface.co/blog"),
    ("Manus.im — Context Engineering Lessons", "https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus"),
]

async def send_daily_briefing():
    bot = Bot(token=BOT_TOKEN)
    today = datetime.now().strftime("%A, %d %B %Y")

    # Pick content
    prereading = random.choice(MODULE_1_PREREADING + MODULE_2_PREREADING)
    m1_assignment = random.choice(MODULE_1_ASSIGNMENTS)
    m2_assignment = random.choice(MODULE_2_ASSIGNMENTS)
    tool = random.choice(TOOLS_EXPLAINED)
    today_articles = random.sample(ARTICLES, 3)

    msg = f"🧭 *NAVIGATOR DAILY BRIEFING*\n_{today}_\n\n"

    # Deadlines
    msg += "🔴 *DEADLINES*\n"
    msg += "• Future of Work essay — March 23, 19:00 CET\n\n"

    # Next session
    msg += "📅 *NEXT SESSION*\n"
    msg += "• Chasing Jarvis Session 2 — Saturday March 21 (estimated)\n\n"

    # Status
    msg += "✅ *STATUS*\n"
    msg += "• All JTBDs current\n"
    msg += "• Hult — Submitted & Under Review\n\n"

    # Chasing Jarvis section
    msg += "🎯 *CHASING JARVIS — TODAY'S FOCUS*\n\n"

    msg += f"📖 *Pre-reading (Module {prereading['module']}):*\n"
    msg += f"[{prereading['title']}]({prereading['url']})\n"
    msg += f"_{prereading['focus']}_\n\n"

    msg += f"🔧 *Tool to understand today:*\n"
    msg += f"*{tool['tool']}* — {tool['why']}\n"
    msg += f"[Watch/Read explanation]({tool['link']})\n"
    msg += f"_{tool['description']}_\n\n"

    msg += f"📝 *Module 1 Assignment to prepare:*\n"
    msg += f"_{m1_assignment['assignment']}_\n"
    msg += f"Why it matters: {m1_assignment['why']}\n"
    for name, url in m1_assignment['prep_links']:
        msg += f"• [{name}]({url})\n"
    msg += "\n"

    msg += f"📝 *Module 2 Assignment to prepare:*\n"
    msg += f"_{m2_assignment['assignment']}_\n"
    msg += f"Why it matters: {m2_assignment['why']}\n"
    for name, url in m2_assignment['prep_links']:
        msg += f"• [{name}]({url})\n"
    msg += "\n"

    # Articles
    msg += "📰 *TODAY'S AI READING — 3 ARTICLES*\n"
    for name, url in today_articles:
        msg += f"• [{name}]({url})\n"
    msg += "\n"

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
