# Cotrugli Navigator — Project Blueprint
**Version:** 1.0 | **Date:** March 2026 | **Author:** Nardus Du Plooy
**Classification:** CONFIDENTIAL

## 1. Product Vision
Cotrugli Navigator is an AI orchestration agent that consolidates all Vanguard MBA programme information into one calm, always-current planning interface.

**Navigator answers one question for every student, every morning:**
> "What do I need to do today, and am I on track?"

## 2. Target Users

| Phase | Users | Scale |
|---|---|---|
| Phase 1 (Now) | Nardus Du Plooy only | 1 user |
| Phase 2 (Soon) | Drazen's test group | 10-20 users |
| Phase 3 | Full Vanguard MBA cohort | ~100 users |
| Phase 4 | Future COTRUGLI cohorts | Ongoing |
| Phase 5 (Chiron) | Any educational programme | Unlimited |

## 3. Feature Specification

### 3.1 Daily Briefing — LIVE ✅
- 05:30 CAT delivery via Telegram bot (@CotNavigatorBot)
- Deadline countdown timers (T-Xd Xh format)
- Module reading list with rotation
- Daily assignment and tool of the day
- Supplementary resource
- Kapusta leadership reading
- NEO World article (rotating)
- AI-generated knowledge question (claude-sonnet-4-6)
- Model answer at 06:00 CAT (30-minute delay)

### 3.2 Bot Interface — LIVE ✅
- /start — welcome message
- /addme — subscribe to daily briefings
- /removeme — unsubscribe
- /status — check subscription status
- /subscribers — admin only (Nardus)

### 3.3 North Star Dashboard — LIVE (local) ✅
- Dark tactical command center aesthetic
- Live CAT clock, countdown timers, interactive calendar
- JTBD tracker, Sprint status, Module progress bars
- Auto-refresh every 5 minutes

### 3.4 Portal Intelligence — BUILT, DISABLED ⚠️
- Authenticated login to cotrugli.online
- Course progress scraping (LearnDash)
- Zoom link extraction
- DISABLED pending COTRUGLI compliance approval

### 3.5 Channel Intelligence — REDESIGN REQUIRED ⚠️
- Original implementation SUSPENDED (Telethon personal account — ToS violation)
- Required: Bot API only, bot must be official channel member
- Dependency: @CotNavigatorBot must be added by admins

### 3.6 Natural Language Q&A — BUILT ✅
- claude-sonnet-4-6 powers Q&A engine
- Full programme context injected into system prompt
- Target: Integrate into web app Ask tab

## 4. Sprint Status

| Sprint | What | Status |
|---|---|---|
| Sprint 1 | Channel Reader + Daily Briefing | ✅ DONE |
| Sprint 2 | Web App | ✅ DONE |
| Sprint 3 | Portal Scraper | ✅ BUILT (disabled) |
| Sprint 3.5 | Bot Onboarding + Auto-start | ✅ DONE |
| Sprint 4 | Channel Redesign (Bot API) | 🔄 IN PROGRESS |
| Sprint 5 | CPN Foundation | 📋 PLANNED |
| Sprint 6 | Web Interface | 📋 PLANNED |
| Sprint 7 | Mobile App | 🔮 FUTURE |
| Sprint 8 | Chiron Integration | 🔮 FUTURE |

## 5. MVP Definition
A single daily message delivered at 05:30 CAT containing: deadlines with countdown timers, next Zoom session, one reading for today, one assignment to prepare, and a knowledge question with model answer 30 minutes later.

**MVP is live and operational as of March 2026.**

## 6. Open Dependencies
- Telegram channel access: @CotNavigatorBot must be added by Drazen Kapusta
- Portal scraper approval: COTRUGLI IT must formally approve
- Gemini migration: Google Cloud billing setup required
- Cloud hosting: Required before Phase 3
- Technical partner: Backend developer needed for Sprint 5+
