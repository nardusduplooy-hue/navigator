import json
import asyncio
import random
from datetime import datetime
from telegram import Bot
from dotenv import load_dotenv
import os
from jarvis_content import (
    DR_TALI_ARTICLES,
    MODULE_1_PREREADING,
    MODULE_1_ASSIGNMENTS,
    TOOLS_EXPLAINED
)

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_IDS = [1357019604, 285802287]

ARTICLES = [
    ("MIT Sloan — Open vs Closed AI Models: performance and cost data", "https://mitsloan.mit.edu/ideas-made-to-matter/ai-open-models-have-benefits-so-why-arent-they-more-widely-used"),
    ("McKinsey — What is a Context Window", "https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-a-context-window"),
    ("IBM Think — Context Windows explained", "https://www.ibm.com/think/topics/context-window"),
    ("Red Hat — LLM vs SLM key differences", "https://www.redhat.com/en/topics/ai/llm-vs-slm"),
    ("Euronews — Open vs Closed Source AI explained", "https://www.euronews.com/next/2024/02/20/open-source-vs-closed-source-ai-whats-the-difference-and-why-does-it-matter"),
    ("AI Snake Oil — what AI cannot do (Princeton researchers)", "https://www.aisnakeoil.com"),
    ("Anthropic — Prompt Engineering overview", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"),
    ("DataCamp — Tokens and context windows explained", "https://www.datacamp.com/blog/context-window"),
    ("GeeksforGeeks — LLM vs SLM architecture comparison", "https://www.geeksforgeeks.org/artificial-intelligence/llms-vs-slms-comparative-analysis-of-language-model-architectures/"),
]

async def send_daily_briefing():
    bot = Bot(token=BOT_TOKEN)
    today = datetime.now().strftime("%A, %d %B %Y")

    tali_picks = random.sample(DR_TALI_ARTICLES, 2)
    prereading = random.choice(MODULE_1_PREREADING)
    assignment = random.choice(MODULE_1_ASSIGNMENTS)
    tool = random.choice(TOOLS_EXPLAINED)
    today_articles = random.sample(ARTICLES, 3)

    msg = f"🧭 *NAVIGATOR DAILY BRIEFING*\n_{today}_\n\n"

    msg += "🔴 *DEADLINES*\n"
    msg += "• Future of Work essay — March 23, 19:00 CET\n\n"

    msg += "📅 *NEXT SESSION*\n"
    msg += "• Chasing Jarvis Session 2 — Saturday March 21 (estimated)\n\n"

    msg += "✅ *STATUS*\n"
    msg += "• All JTBDs current\n"
    msg += "• Hult — Submitted & Under Review\n\n"

    msg += "🎯 *CHASING JARVIS — TODAY'S FOCUS*\n\n"

    msg += f"📖 *Pre-reading:*\n"
    msg += f"[{prereading['title']}]({prereading['url']})\n"
    msg += f"_{prereading['focus']}_\n\n"

    msg += f"✍️ *Dr. Tali's Reading — 2 articles today:*\n"
    for article in tali_picks:
        msg += f"• [{article['title']}]({article['url']})\n"
        msg += f"  _{article['focus']}_\n"
    msg += "\n"

    msg += f"🔧 *Tool to understand today:*\n"
    msg += f"*{tool['tool']}*\n"
    msg += f"[Read or watch here]({tool['link']})\n"
    msg += f"_{tool['description']}_\n\n"

    msg += f"📝 *Assignment to prepare:*\n"
    msg += f"_{assignment['assignment']}_\n\n"
    msg += f"Why it matters: {assignment['why']}\n\n"
    msg += f"Prepare with:\n"
    for name, url in assignment['prep_links']:
        msg += f"• [{name}]({url})\n"
    msg += "\n"

    msg += "📰 *TODAY'S AI READING*\n"
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
