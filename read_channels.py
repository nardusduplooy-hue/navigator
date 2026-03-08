from telethon import TelegramClient
from datetime import datetime, timezone
import json
import asyncio

API_ID = 33536648
API_HASH = '967150ea324c2059fc79952d46486600'
SESSION_NAME = 'navigator_session'
VANGUARD_ID = -1002421053554

TOPICS = {
    838: 'Jobs to Be Done',
    1480: 'Chasing Jarvis',
    456: 'General Chat',
    750: 'eX / Vanguard Chiefs',
    542: 'Tenders',
    698: 'Philosophy Lab',
    330: 'Hult Challenge',
    403: 'Portal Support',
    5: 'General Discussion',
    2: 'Announcements',
    10: 'Entrepreneurship',
    11: 'Introduce Yourself',
    1396: 'IT Support',
}

KEYWORDS = [
    'deadline', 'due', 'submit', 'assignment', 'zoom', 'meeting',
    'http', 'jtbd', 'job to be done', 'urgent', 'important',
    'session', 'next week', 'tomorrow', 'by march', 'by april',
    'by may', '2026', 'cet', 'slides', 'homework', 'task'
]

def is_important(text):
    text_lower = text.lower()
    return any(kw in text_lower for kw in KEYWORDS)

async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()
    
    print('🧭 Navigator — Reading Vanguard channels...\n')
    
    all_messages = []
    important_messages = []
    
    for topic_id, topic_name in TOPICS.items():
        try:
            msgs = await client.get_messages(VANGUARD_ID, limit=20, reply_to=topic_id)
            for m in msgs:
                if m.text:
                    msg_data = {
                        'topic_id': topic_id,
                        'topic_name': topic_name,
                        'date': m.date.strftime('%Y-%m-%d %H:%M'),
                        'text': m.text,
                        'important': is_important(m.text)
                    }
                    all_messages.append(msg_data)
                    if msg_data['important']:
                        important_messages.append(msg_data)
        except Exception as e:
            print(f'  ⚠️  Could not read {topic_name}: {e}')
    
    # Save all messages
    with open('navigator_data.json', 'w') as f:
        json.dump(all_messages, f, indent=2)
    
    # Print important messages
    print(f'📊 Scanned {len(all_messages)} messages across {len(TOPICS)} channels')
    print(f'🚨 Found {len(important_messages)} important messages\n')
    print('=== IMPORTANT MESSAGES ===\n')
    
    for msg in important_messages:
        print(f'[{msg["topic_name"]}] {msg["date"]}')
        print(f'{msg["text"][:200]}')
        print()
    
    print(f'\n✅ All data saved to navigator_data.json')
    await client.disconnect()

asyncio.run(main())
