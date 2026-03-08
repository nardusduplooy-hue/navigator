import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

# Load your keys from .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def test():
    bot = Bot(token=TOKEN)
    # Get your chat ID first
    print("Getting bot info...")
    info = await bot.get_me()
    print(f"Bot name: {info.first_name}")
    print(f"Bot username: @{info.username}")
    print("✅ Bot is alive! Now send any message to your bot on Telegram, then run step 2.")

asyncio.run(test())
```

Paste it in and press **⌘ + S** to save.

Then go to Terminal and run:
```
cd ~/Documents/navigator && source venv/bin/activate && python3 test_bot.py
import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

# Load your keys from .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def test():
    bot = Bot(token=TOKEN)
    # Get your chat ID first
    print("Getting bot info...")
    info = await bot.get_me()
    print(f"Bot name: {info.first_name}")
    print(f"Bot username: @{info.username}")
    print("✅ Bot is alive! Now send any message to your bot on Telegram, then run step 2.")

asyncio.run(test())
```

Paste it in and press **⌘ + S** to save.

Then go to Terminal and run:
```
cd ~/Documents/navigator && source venv/bin/activate && python3 test_bot.py
