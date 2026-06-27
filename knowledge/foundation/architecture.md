# Cotrugli Navigator — Technical Architecture Document
**Version:** 2.0 | **Updated:** June 2026 | **Author:** Nardus Du Plooy
**Classification:** CONFIDENTIAL

## 1. Overview
Cotrugli Navigator is an AI orchestration agent that consolidates all Vanguard MBA programme information into a single daily intelligence briefing — delivered automatically every morning at 06:00 CAT.

## 2. System Architecture — Four Layers

1. **Content Layer** — manually curated programme content, stored in Python and JSON files
2. **AI Brain Layer** — LLM-powered knowledge question and model answer generation
3. **Delivery Layer** — cron-triggered briefing assembly and Telegram dispatch
4. **Interface Layer** — Telegram bot for subscriber management, Flask dashboard for local use

| CONTENT | AI BRAIN | DELIVERY | INTERFACE |
|---|---|---|---|
| jarvis_content.py, deadlines.json, daily_briefing.py | Claude API (knowledge Q&A) | macOS cron → daily_briefing.py | Telegram bot, Flask dashboard |

## 3. Data Sources

### 3.1 Telegram — Send Only
- **Protocol:** Bot API only — @CotNavigatorBot
- **Usage:** Outbound delivery to subscribers and the Navigator channel topic
- **NO channel reading or scraping of any kind** — not permitted under Telegram ToS
- Bot is a member of the COTRUGLI Navigator channel for posting briefings

### 3.2 Programme Content (Static)
All programme content is manually curated and embedded in `daily_briefing.py` and `jarvis_content.py`:
- Zoom session details (links, dates, passcodes)
- Module assignments and deadlines
- Vanguard Teams daily messages
- Chasing Jarvis daily entries (Dr. Tali Režun LinkedIn posts)
- Vanguard Leadership summaries (Dražen Kapusta book)
- AI news fallback content

### 3.3 Live AI News Feed
- VentureBeat RSS feed fetched live at briefing time
- Filtered for Anthropic/Claude content, security content excluded
- Falls back to manually curated content if feed unavailable

### 3.4 Cotrugli Portal
- Portal scraper built (`portal_scraper.py`) — **DISABLED**
- Pending formal approval from COTRUGLI IT
- Read-only, single-student scope when re-enabled

## 4. Current Stack (Live)

| Component | Detail |
|---|---|
| Runtime | Python 3.14 on MacBook Pro (local) |
| LLM | claude-sonnet-4-6 (Anthropic API) |
| Bot Framework | python-telegram-bot v22+ |
| Scheduling | macOS cron (runs at 06:00 SAST daily) |
| Web Server | Flask (local dashboard at localhost:5000) |
| Data Storage | Local JSON files (deadlines.json, subscribers.json) |
| Version Control | GitHub (github.com/nardusduplooy-hue/navigator) |

## 5. Target Stack (Scale — Phase 3+)

| Component | Detail |
|---|---|
| Hosting | Hetzner VPS or DigitalOcean Droplet |
| LLM | Google Gemini 2.0 Flash (recommended by Dr. Tali Režun) |
| Database | PostgreSQL or Supabase |
| Web Interface | React frontend + Python/Node backend |
| Mobile | React Native or Progressive Web App |

## 6. Key Files

| File | Purpose |
|---|---|
| daily_briefing.py | Assembles and sends the 06:00 CAT briefing — 682 lines, heart of the system |
| jarvis_content.py | All curated content: book summaries, articles, assignments, tools — 3,441 lines |
| bot_listener.py | Handles /addme, /removeme, /status, /subscribers commands |
| scheduler.py | Legacy file — no longer used. Cron replaced it |
| server.py | Flask web server for local North Star dashboard |
| deadlines.json | Structured deadline data |
| subscribers.json | Dynamic subscriber list (Telegram chat IDs + names) |
| navigator_app.html | Mobile web app |
| portal_scraper.py | Portal scraper — DISABLED pending compliance approval |
| channel_listener.py | Bot API update listener — reads messages posted to bot, not channel scraping |
| .env | API keys — NEVER committed to GitHub |

## 7. Daily Briefing Flow (06:00 SAST / CAT)

macOS cron fires three commands in sequence at 06:00:

1. `daily_briefing.py --briefing-only` → builds full briefing, sends to all subscribers via Telegram DM
2. `daily_briefing.py --answer-only` → sends model answer to all subscribers via Telegram DM
3. `daily_briefing.py --send-channel` → posts briefing + answer to the COTRUGLI Navigator Telegram channel topic

All three run within seconds of each other. Briefing and answer are delivered simultaneously (not 30 minutes apart).

Logs written to `logs/scheduler.log`.

## 8. Briefing Structure (as of June 2026)

Each briefing contains, in order:
- Header: date and title
- 🏆 Vanguard Teams: daily motivational message
- 🔴 Deadlines: active deadlines with countdown
- 📅 Next Zoom Session: upcoming session with link, ID, passcode
- Module-specific content (current active module)
- 🎯 Chasing Jarvis: Dr. Tali Režun daily LinkedIn post
- 📋 Assignment reminders
- 🏛️ Vanguard Leadership: Dražen Kapusta book summary
- 🌐 AI News: live VentureBeat feed or fallback
- 🧠 Knowledge Question (from TALI_STEPS in jarvis_content.py)
- 📲 /addme prompt for new subscribers
- ⚡ Navigator out.

Model answer sent as a separate message immediately after.

## 9. Delivery Targets (as of June 2026)
- 8 active subscribers receiving daily DMs
- 1 subscriber has blocked the bot (skipped silently)
- COTRUGLI Navigator Telegram channel (topic thread ID 2201)

## 10. Infrastructure Decisions

### Why Local First
Zero infrastructure cost, fast iteration, immediate deployment. Limitation: requires MacBook to be on and connected at 06:00 SAST.

### Migration Path to Cloud
All code is environment-agnostic Python. GitHub is source of truth. Estimated migration time: 2–4 hours once a VPS is provisioned.

### Why scheduler.py Is No Longer Used
macOS cron replaced scheduler.py. Cron is more reliable on Mac (survives crashes, doesn't need a Python process running 24/7), and allows precise control over each command in the sequence.
