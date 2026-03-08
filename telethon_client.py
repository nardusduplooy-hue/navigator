import os
import base64
from telethon import TelegramClient

API_ID = int(os.getenv("API_ID", "33536648"))
API_HASH = os.getenv("API_HASH", "967150ea324c2059fc79952d46486600")

def get_client():
    session_string = os.getenv("SESSION_STRING")
    if session_string:
        session_data = base64.b64decode(session_string.encode())
        with open("navigator_session.session", "wb") as f:
            f.write(session_data)
    return TelegramClient("navigator_session", API_ID, API_HASH)
