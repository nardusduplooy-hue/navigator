# Cotrugli Navigator — Project Blueprint
**Version:** 2.0 | **Updated:** June 2026 | **Author:** Nardus Du Plooy
**Classification:** CONFIDENTIAL

## 1. Product Vision
Cotrugli Navigator is an AI orchestration agent that consolidates all Vanguard MBA programme information into one calm, always-current daily briefing.

**Navigator answers one question for every student, every morning:**
> "What do I need to do today, and am I on track?"

## 2. Target Users

| Phase | Users | Scale |
|---|---|---|
| Phase 1 (Now) | Nardus Du Plooy + Vanguard cohort early adopters | 8 subscribers |
| Phase 2 (Soon) | Full Vanguard MBA cohort | ~100 users |
| Phase 3 | Future COTRUGLI cohorts | Ongoing |
| Phase 4 (Chiron) | Any educational programme | Unlimited |

## 3. Feature Specification

### 3.1 Daily Briefing — LIVE ✅
- 06:00 SAST delivery via Telegram bot (@CotNavigatorBot)
- Delivered to individual subscribers (DM) and the Navigator Telegram channel simultaneously
- Vanguard Teams daily message
- Active deadlines with context
- Next Zoom session with link, ID, passcode
- Module-specific content (current module rotates as programme progresses)
- Chasing Jarvis: Dr. Tali Režun daily LinkedIn post
- Vanguard Leadership: Dražen Kapusta book summary
- Live AI news from VentureBeat (filtered for Anthropic/Claude content)
- AI-generated knowledge question (claude-sonnet-4-6)
- Model answer sent immediately after briefing (same cron run)

### 3.2 Bot Interface — LIVE ✅
- /start — welcome message
- /addme — subscribe to daily briefings
- /removeme — unsubscribe
- /status — check subscription status
- /subscribers — admin only (Nardus)

### 3.3 North Star Dashboard — LIVE (local) ✅
- Dark tactical command center aesthetic
- Flask server at localhost:5000
- Reads navigator_data.json for channel message data
- Auto-refresh every 5 minutes

### 3.4 Portal Intelligence — BUILT, DISABLED ⚠️
- Authenticated login to cotrugli.online
- Course progress scraping (LearnDash)
- Zoom link extraction
- DISABLED pending COTRUGLI IT formal approval

### 3.5 Channel Listener — BUILT, NOT YET USEFUL
- channel_listener.py reads bot API updates (getUpdates)
- Can only see messages from chats where the bot is a member
- Not channel scraping — fully compliant with Telegram ToS
- Limited utility until bot is added to more programme channels by admins
- No channel reading of any kind without bot being official member

### 3.6 Natural Language Q&A — BUILT ✅
- ask_navigator.py powers CLI Q&A
- claude-sonnet-4-6 with full programme context in system prompt
- Not yet integrated into web app

## 4. Sprint Status (June 2026)

| Sprint | What | Status |
|---|---|---|
| Sprint 1 | Daily Briefing + Bot | ✅ LIVE |
| Sprint 2 | North Star Web Dashboard | ✅ LIVE (local) |
| Sprint 3 | Portal Scraper | ✅ BUILT — disabled pending approval |
| Sprint 3.5 | Cron automation + Channel delivery | ✅ LIVE |
| Sprint 4 | Content management — spreadsheet to code pipeline | 🔄 IN PROGRESS |
| Sprint 5 | Foundation doc update + Claude Code workflow | 🔄 IN PROGRESS |
| Sprint 6 | CPN Foundation (Character formation layer) | 📋 PLANNED |
| Sprint 7 | Public Web Interface | 📋 PLANNED |
| Sprint 8 | Mobile App | 🔮 FUTURE |
| Sprint 9 | Chiron Integration (multi-school) | 🔮 FUTURE |

## 5. MVP Definition
A single daily message delivered at 06:00 SAST containing: deadlines, next Zoom session, module content, leadership reading, AI news, and a knowledge question with model answer.

**MVP is live and operational. Delivering daily to 8 subscribers.**

## 6. Open Dependencies
- Telegram channel access: @CotNavigatorBot must be added to Vanguard programme channels by admins
- Portal scraper approval: COTRUGLI IT must formally approve
- Gemini migration: Google Cloud billing setup required for Phase 3
- Cloud hosting: Required before Phase 2 (full cohort scale)
- Content pipeline: Daily briefing content currently hardcoded — needs a structured input system (spreadsheet → code)

## 7. eX Venture Context
Navigator is Nardus Du Plooy's eX Venture project, developed through the Chasing Jarvis course as part of the COTRUGLI Vanguard MBA programme. It is a live, production system — not a prototype or academic exercise.
