import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = 1357019604

async def send_first_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="""🧭 Navigator is online.

Good evening, Nardus.

This is your first message from Cotrugli Navigator.

Sprint 1 is live. The North Star is being built.

— Navigator"""
    )
    print("Message sent! Check your Telegram.")

asyncio.run(send_first_message())
