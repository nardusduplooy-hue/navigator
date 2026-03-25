# Cotrugli Navigator — Technical Architecture Document
**Version:** 1.0 | **Date:** March 2026 | **Author:** Nardus Du Plooy
**Classification:** CONFIDENTIAL

## 1. Overview
Cotrugli Navigator is an AI orchestration agent that consolidates all Vanguard MBA programme information into a single calm, always-current planning interface.

## 2. System Architecture — Four Layers
1. **Data Sources Layer** — external platforms where programme information lives
2. **Knowledge Base Layer** — structured local store of consolidated programme data
3. **AI Brain Layer** — LLM-powered query, synthesis, and planning engine
4. **Output Layer** — Telegram bot, web dashboard, and daily briefings

| DATA SOURCES | KNOWLEDGE BASE | AI BRAIN | OUTPUT |
|---|---|---|---|
| Telegram Bot API, Cotrugli Portal, Programme Documents, Deadlines (JSON) | Unified Timeline, Assignment Index, Module Summaries, Progress Store | Claude API, Query Engine, Context Window, Natural Language | Telegram Briefings, Web Dashboard, Mobile App (future), Q&A Interface |

## 3. Data Sources

### 3.1 Telegram (Bot API)
- **Protocol:** Bot API only — @CotNavigatorBot — NO personal account credentials
- **Status:** Bot created, services running, no channel scraping active
- **PERMANENTLY DISABLED:** Personal account Telethon library
- **Required:** Bot added to Vanguard channels by channel administrators
- **Channels:** 9 Vanguard programme channels identified

### 3.2 Cotrugli Portal (cotrugli.online)
- **Platform:** BuddyBoss (social) + LearnDash LMS (course layer)
- **Status:** Portal scraper built and tested (portal_scraper.py) — DISABLED pending compliance review
- **Required:** Formal approval from COTRUGLI IT before re-enabling
- **Target data:** Course deadlines, assignment details, Zoom links, module progress

### 3.3 Programme Documents
Static documents parsed once and stored in jarvis_content.py:
- Vanguard MBA Programme Design
- Vanguard MBA Field Manual
- Learning Schedule and Assessment Weights
- Module-specific reading lists

### 3.4 Manual Content Feed
Curated by Nardus Du Plooy:
- Daily reading articles from Dr. Tali Režun (Medium)
- Dražen Kapusta LinkedIn articles
- NEO World articles (World Financial Review)
- Module assignment details and preparation links

## 4. Current Stack (MVP)

| Component | Detail |
|---|---|
| Runtime | Python 3.14 on MacBook Pro (local) |
| LLM | claude-sonnet-4-6 (Anthropic API) |
| Bot Framework | python-telegram-bot v22+ |
| Web Server | Flask (local dashboard at localhost:5000) |
| Scheduling | macOS wake schedule + scheduler.py |
| Data Storage | Local JSON files (deadlines.json, subscribers.json) |
| Version Control | GitHub (github.com/nardusduplooy-hue/navigator) |

## 5. Target Stack (Scale)

| Component | Detail |
|---|---|
| Hosting | Hetzner VPS or DigitalOcean Droplet (R150-300/month) |
| LLM | Google Gemini 2.0 Flash (recommended by Dr. Tali Režun) |
| Database | PostgreSQL or Supabase |
| Web Interface | React frontend + Python/Node backend |
| Mobile | React Native or Progressive Web App |

## 6. Key Files

| File | Purpose |
|---|---|
| daily_briefing.py | Generates and sends 05:30 CAT briefing to all subscribers |
| bot_listener.py | Handles /addme, /removeme, /status commands |
| scheduler.py | Fires daily_briefing.py at 05:30 CAT |
| server.py | Flask web server at localhost:5000 |
| jarvis_content.py | All static content: articles, assignments, tools |
| deadlines.json | Structured deadline data |
| subscribers.json | Dynamic subscriber list |
| navigator_app.html | Mobile web app |
| portal_scraper.py | Portal scraper — DISABLED pending approval |
| .env | API keys — NEVER committed to GitHub |

## 7. Daily Briefing Flow (05:30 CAT)
1. scheduler.py fires at 05:30 CAT, waits 30 seconds for network
2. daily_briefing.py loads subscribers.json, deadlines.json, jarvis_content.py
3. Claude API generates daily knowledge question and model answer
4. Briefing assembled and sent to all subscribers via Telegram Bot API
5. 30-minute delay — model answer sent at 06:00 CAT

## 8. Infrastructure Decisions

### Why Local First
Zero infrastructure cost, fast iteration, immediate deployment. Limitation: requires MacBook to be on and connected.

### Migration Path to Cloud
All code is environment-agnostic Python. GitHub is source of truth. Estimated migration time: 2-4 hours.
