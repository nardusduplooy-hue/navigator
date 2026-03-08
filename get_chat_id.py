import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def get_chat_id():
    bot = Bot(token=TOKEN)
    updates = await bot.get_updates()
    if updates:
        chat_id = updates[0].message.chat_id
        print(f"Your Chat ID is: {chat_id}")
        print("Save this number - you will need it!")
    else:
        print("No messages found - send your bot a message on Telegram first then run again")

asyncio.run(get_chat_id())
