import json
import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = 1357019604

async def send_briefing():
    bot = Bot(token=BOT_TOKEN)
    
    with open('navigator_data.json', 'r') as f:
        messages = json.load(f)
    
    # Find important messages from last 7 days
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=7)
    
    briefing = "🧭 *NAVIGATOR BRIEFING — March 8, 2026*\n\n"
    briefing += "📡 *LATEST FROM YOUR CHANNELS:*\n\n"
    
    seen = []
    for msg in messages:
        if msg['important'] and msg['text'] not in seen:
            if any(kw in msg['text'].lower() for kw in ['zoom', 'deadline', 'due', 'submit', 'session', 'saturday', 'next']):
                briefing += f"*[{msg['topic_name']}]*\n{msg['text'][:200]}\n\n"
                seen.append(msg['text'])
    
    briefing += "✅ *STATUS:* All JTBDs current\n"
    briefing += "📅 *NEXT SESSION:* Saturday March 21 (estimated)\n"
    briefing += "🎯 *FOCUS:* Chasing Jarvis Module 1 complete"
    
    await bot.send_message(
        chat_id=CHAT_ID,
        text=briefing,
        parse_mode='Markdown'
    )
    print("✅ Briefing sent to Telegram!")

asyncio.run(send_briefing())
