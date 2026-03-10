from flask import Flask, jsonify, send_from_directory
import json, os
from datetime import datetime

SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SERVER_DIR)

STATIC_DIR = os.path.join(SERVER_DIR, 'static')

app = Flask(__name__)

DEADLINE_KEYWORDS = ['deadline', 'due', 'submit', 'submission', 'essay', 'assignment', 'march', 'april', 'cet', 'by ', 'before ']
SESSION_KEYWORDS  = ['zoom', 'session', 'saturday', 'meeting', 'link', 'cotrugli.zoom', 'cotrugli.online/groups']

def load_data():
    with open(os.path.join(ROOT_DIR, 'navigator_data.json'), 'r') as f:
        return json.load(f)

def classify_message(msg):
    text_lower = msg['text'].lower()
    tags = []
    if any(k in text_lower for k in DEADLINE_KEYWORDS):
        tags.append('deadline')
    if any(k in text_lower for k in SESSION_KEYWORDS):
        tags.append('session')
    return tags

@app.route('/api/data')
def api_data():
    messages = load_data()
    channels = {}
    for msg in messages:
        name = msg['topic_name']
        if name not in channels:
            channels[name] = {'name': name, 'total': 0, 'important': 0, 'latest': None, 'latest_date': None}
        channels[name]['total'] += 1
        if msg['important']:
            channels[name]['important'] += 1
        if channels[name]['latest_date'] is None or msg['date'] > channels[name]['latest_date']:
            channels[name]['latest'] = msg['text'][:120]
            channels[name]['latest_date'] = msg['date']
    important = []
    for msg in messages:
        tags = classify_message(msg)
        if msg['important'] or tags:
            important.append({'topic': msg['topic_name'], 'date': msg['date'], 'text': msg['text'][:300], 'tags': tags, 'flagged': msg['important']})
    important.sort(key=lambda x: x['date'], reverse=True)
    deadlines = [m for m in important if 'deadline' in m['tags']]
    sessions  = [m for m in important if 'session' in m['tags']]
    stats = {'total_messages': len(messages), 'total_channels': len(channels), 'total_important': sum(1 for m in messages if m['important']), 'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M')}
    return jsonify({'stats': stats, 'channels': list(channels.values()), 'important': important[:30], 'deadlines': deadlines[:10], 'sessions': sessions[:10]})

@app.route('/')
def index():
    return send_from_directory(SERVER_DIR, 'navigator_dashboard.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    print("Navigator server starting...")
    print("Dashboard: http://localhost:5000")
    app.run(debug=False, port=5000, host="127.0.0.1")
