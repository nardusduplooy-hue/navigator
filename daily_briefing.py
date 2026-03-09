import json
import asyncio
import random
from datetime import datetime
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_IDS = [1357019604, 285802287]

PODCASTS = [
    ("Dr. Tali Režun — Understanding LLMs", "https://redcircle.com/shows/from-lab-to-life/ep/8a6a7d09-b3fb-4513-88c6-b2784619a301"),
    ("Dr. Tali Režun — From Prompts to Precision", "https://redcircle.com/shows/ab71928c-8c79-46b9-a324-0d82a84b3254/ep/2f8a063f-121e-4c43-b268-a3c0e42c6701"),
    ("Lex Fridman — Andrej Karpathy: Deep Dive into LLMs", "https://www.youtube.com/watch?v=zjkBMFhNj_g"),
    ("Lex Fridman — Sam Altman on OpenAI & AGI", "https://www.youtube.com/watch?v=jvqFAi7vkBc"),
    ("Lex Fridman — Demis Hassabis: DeepMind & AGI", "https://www.youtube.com/watch?v=Gfr50f6ZBvo"),
    ("Andrej Karpathy — Intro to Large Language Models", "https://www.youtube.com/watch?v=zjkBMFhNj_g"),
    ("Cognitive Revolution — AI in Business", "https://www.youtube.com/@CognitiveRevolutionPodcast"),
    ("Latent Space — AI Engineering Podcast", "https://www.latent.space/podcast"),
    ("Practical AI — Changelog Podcast", "https://changelog.com/practicalai"),
    ("Eye on AI — Weekly Industry News", "https://www.eye-on.ai/podcast-archive"),
    ("TWIML AI Podcast", "https://twimlai.com/podcast/twimlai/"),
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

    today_podcasts = random.sample(PODCASTS, 2)
    today_articles = random.sample(ARTICLES, 3)

    msg = f"🧭 *NAVIGATOR DAILY BRIEFING*\n_{today}_\n\n"
    msg += "🔴 *DEADLINES*\n"
    msg += "• Future of Work essay — March 23, 19:00 CET\n\n"
    msg += "📅 *NEXT SESSION*\n"
    msg += "• Chasing Jarvis Session 2 — Saturday March 21 (estimated)\n\n"
    msg += "✅ *STATUS*\n"
    msg += "• All JTBDs current\n"
    msg += "• Hult — Submitted & Under Review\n\n"
    msg += "🎧 *TODAY'S LISTENING — 2 x 15-30 min*\n"
    for name, url in today_podcasts:
        msg += f"• [{name}]({url})\n"
    msg += "\n"
    msg += "📰 *TODAY'S READING — 3 ARTICLES*\n"
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
