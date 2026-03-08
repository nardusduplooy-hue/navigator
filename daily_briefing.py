import json
import asyncio
import random
from datetime import datetime
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = 1357019604

PODCASTS = [
    ("Dr. Tali Režun — Understanding LLMs", "https://redcircle.com/shows/from-lab-to-life/ep/8a6a7d09-b3fb-4513-88c6-b2784619a301"),
    ("Dr. Tali Režun — From Prompts to Precision", "https://redcircle.com/shows/ab71928c-8c79-46b9-a324-0d82a84b3254/ep/2f8a063f-121e-4c43-b268-a3c0e42c6701"),
    ("Lex Fridman — Andrej Karpathy on LLMs", "https://open.spotify.com/episode/4LgBEBRSgaGN4VqYGKGiNH"),
    ("Lex Fridman — Sam Altman: OpenAI & AGI", "https://open.spotify.com/episode/6PxpRmEEQhiJSE0pQSiFjE"),
    ("Practical AI — AI Agents in Production", "https://open.spotify.com/show/1LaCr5TFAgYPK5qHjP3XDp"),
    ("Cognitive Revolution — AI in Business", "https://open.spotify.com/show/6yHyok3M3BmIHDtBZyNBpF"),
    ("No Priors — AI Founders & Builders", "https://open.spotify.com/show/0bZNDmcaUSjFCaVdmDTJeP"),
    ("Latent Space — AI Engineering", "https://open.spotify.com/show/2p22p2Z3tLRgHtEJFmECQc"),
    ("The AI Breakdown — Daily AI News", "https://open.spotify.com/show/6LbQ4bRQESmrRSFkFHwKNG"),
    ("Eye on AI — Weekly Industry News", "https://open.spotify.com/show/7fl4AnOhBqKCfRfHJnrUQg"),
]

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
    
    # Load channel data
    try:
        with open('navigator_data.json', 'r') as f:
            messages = json.load(f)
        deadlines = [m for m in messages if any(kw in m['text'].lower() 
                    for kw in ['due', 'deadline', 'submit', 'by march', 'by april', '19:00', 'cet'])]
        zoom_msgs = [m for m in messages if 'zoom' in m['text'].lower() and 'http' in m['text'].lower()]
    except:
        deadlines = []
        zoom_msgs = []

    # Pick random podcasts and articles
    today_podcasts = random.sample(PODCASTS, 2)
    today_articles = random.sample(ARTICLES, 3)

    # Build briefing
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

    # Podcasts
    msg += "🎧 *TODAY'S LISTENING — 2 x 15-30 min*\n"
    for name, url in today_podcasts:
        msg += f"• [{name}]({url})\n"
    msg += "\n"

    # Articles
    msg += "📰 *TODAY'S READING — 3 ARTICLES*\n"
    for name, url in today_articles:
        msg += f"• [{name}]({url})\n"
    msg += "\n"

    msg += "⚡ _Navigator out._"

    await bot.send_message(
        chat_id=CHAT_ID,
        text=msg,
        parse_mode='Markdown',
        disable_web_page_preview=True
    )
    print(f"✅ Daily briefing sent at {datetime.now().strftime('%H:%M')}")

asyncio.run(send_daily_briefing())
