import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def list_updates():
    bot = Bot(token=TOKEN)
    updates = await bot.get_updates()
    if not updates:
        print("No pending messages found.")
        return
    print(f"Found {len(updates)} pending update(s):\n")
    for u in updates:
        if u.message:
            user = u.message.from_user
            print(f"Name: {user.first_name} {user.last_name or ''}".strip())
            print(f"Username: @{user.username or 'none'}")
            print(f"Chat ID: {u.message.chat_id}")
            print(f"Text: {u.message.text}")
            print("---")

asyncio.run(list_updates())
