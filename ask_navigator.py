import json
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

with open('navigator_data.json', 'r') as f:
    messages = json.load(f)

context = ""
for msg in messages:
    context += f"[{msg['topic_name']}] {msg['date']}: {msg['text'][:300]}\n\n"

def ask(question):
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1000,
        system="""You are Navigator, an AI assistant for Nardus Du Plooy who is a student in the COTRUGLI Vanguard MBA programme. 
You have access to recent messages from all Vanguard Telegram channels.
Be concise, direct, and military-precise. Flag deadlines and urgent items first.
Today is March 10, 2026.""",
        messages=[{
            "role": "user",
            "content": f"Here are the recent Telegram messages from all Vanguard channels:\n\n{context}\n\nQuestion: {question}"
        }]
    )
    return response.content[0].text

print("🧭 Navigator is ready. Ask me anything about your MBA.\n")
print("Type 'quit' to exit\n")

while True:
    question = input("You: ").strip()
    if question.lower() == 'quit':
        break
    if question:
        print(f"\nNavigator: {ask(question)}\n")
