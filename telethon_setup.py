from telethon import TelegramClient
import asyncio

API_ID = 33536648
API_HASH = '967150ea324c2059fc79952d46486600'
SESSION_NAME = 'navigator_session'

async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()
    
    print("✅ Connected successfully!")
    me = await client.get_me()
    print(f"Logged in as: {me.first_name} {me.last_name} (@{me.username})")
    
    print("\nFetching your Telegram channels and groups...")
    async for dialog in client.iter_dialogs():
        if dialog.is_channel or dialog.is_group:
            print(f"  📢 {dialog.name} | ID: {dialog.id}")
    
    await client.disconnect()

asyncio.run(main())
