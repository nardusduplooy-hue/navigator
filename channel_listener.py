import requests
import json
from datetime import datetime, timezone, timedelta

with open(".env") as f:
    env = dict(
        line.strip().split("=", 1)
        for line in f
        if "=" in line and not line.startswith("#")
    )

BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "")
if not BOT_TOKEN:
    print("ERROR: TELEGRAM_BOT_TOKEN not found in .env")
    exit(1)

BASE = f"https://api.telegram.org/bot{BOT_TOKEN}"
CAT  = timezone(timedelta(hours=2))
HOURS_BACK = 24

def get_updates():
    try:
        r = requests.get(f"{BASE}/getUpdates", params={"limit": 100, "timeout": 0}, timeout=15)
        r.raise_for_status()
        return r.json().get("result", [])
    except Exception as e:
        print(f"ERROR: {e}")
        return []

def sender_name(msg):
    frm = msg.get("from") or {}
    parts = [frm.get("first_name", ""), frm.get("last_name", "")]
    return " ".join(p for p in parts if p).strip() or frm.get("username") or "Unknown"

cutoff_ts = int((datetime.now(timezone.utc) - timedelta(hours=HOURS_BACK)).timestamp())
updates = get_updates()

if not updates:
    print("No updates found — bot queue is empty.")
    print("Either no new messages since bot joined, or daily_briefing.py already consumed them.")
    exit(0)

chats = {}
for upd in updates:
    msg = upd.get("message") or upd.get("channel_post")
    if not msg or msg.get("date", 0) < cutoff_ts:
        continue
    cid = msg["chat"]["id"]
    if cid not in chats:
        chats[cid] = {"name": msg["chat"].get("title") or msg["chat"].get("username") or str(cid), "messages": []}
    text = msg.get("text") or msg.get("caption") or "[no text]"
    when = datetime.fromtimestamp(msg["date"], tz=CAT).strftime("%H:%M CAT")
    chats[cid]["messages"].append({"when": when, "from": sender_name(msg), "text": text[:200]})

if not chats:
    print(f"No messages in last {HOURS_BACK}h.")
    exit(0)

for cid, chat in chats.items():
    print(f"\n{'='*50}")
    print(f"CHAT: {chat['name']} (id: {cid})")
    for m in chat["messages"]:
        print(f"  [{m['when']}] {m['from']}: {m['text'][:120]}")

with open("channel_dump.json", "w") as f:
    json.dump({str(k): v for k, v in chats.items()}, f, indent=2, ensure_ascii=False)
print("\nDump saved to channel_dump.json")
