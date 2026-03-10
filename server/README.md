# Navigator Server

Flask server that serves the dashboard and exposes the `/api/data` endpoint.

## Structure

```
server/
  server.py       - Flask app
  static/
    dashboard.css - Dashboard styles
    dashboard.js  - Dashboard logic
    logo.png      - Navigator logo
```

## Setup

Install dependencies into the virtual environment from the project root:

```bash
# Windows
.venv\Scripts\pip install -r requirements.txt

# macOS / Linux
.venv/bin/pip install -r requirements.txt
```

## Run

```bash
# Windows
.venv\Scripts\python server/server.py

# macOS / Linux
.venv/bin/python server/server.py
```

Dashboard will be available at: http://localhost:5000

## API

`GET /api/data` - Returns stats, channels, important messages, deadlines, and sessions derived from `navigator_data.json`.
