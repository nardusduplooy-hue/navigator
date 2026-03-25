# Cotrugli Navigator — UI/UX Document
**Version:** 1.0 | **Date:** March 2026 | **Author:** Nardus Du Plooy
**Classification:** CONFIDENTIAL

## 1. Design Philosophy
> "Calm clarity in the face of programme complexity. The student is the captain. Navigator is the compass."

- **Calm over busy** — information hierarchy, not information overload
- **Countdown over calendar** — urgency is felt, not calculated
- **One screen, one truth** — North Star as single source of orientation
- **Dark and tactical** — serious tool aesthetic, not academic pastels

## 2. Current Interfaces

### 2.1 Telegram Daily Briefing
Primary interface. Delivered at 05:30 CAT. Structured sections with emoji anchors for rapid scanning.

**Briefing structure:**
- Header: Date and briefing title
- 🔴 DEADLINES: Active deadlines with countdown timers
- 📅 NEXT ZOOM SESSION: Upcoming session and recordings link
- ✅ STATUS: JTBD and submission status
- 🎯 CHASING JARVIS FOCUS: Module readings
- 🔜 MODULE PREVIEW: Upcoming module preparation
- 📝 ASSIGNMENT: Today's assignment with preparation links
- 🔧 TOOL: Tool of the day with access link
- 📚 SUPPLEMENTARY: Additional resource
- 🏛️ KAPUSTA READING: Leadership article
- 📰 NEO WORLD: Featured article
- 🧠 KNOWLEDGE QUESTION: AI-generated daily test question
- *(30 min later)* 🧠 MODEL ANSWER

### 2.2 North Star Web Dashboard
Local web dashboard at localhost:5000. Dark tactical command center. Auto-refreshes every 5 minutes.

**Components:**
- Navigation header with NAVIGATOR logo and live CAT clock
- Hero section: Day/date display and programme name
- Stats bar: Message count, channel count, flagged items
- Left panel: Deadlines feed with countdown badges (RED/GREEN/SESSION)
- Centre panel: Interactive monthly calendar with event markers
- Right panel: JTBD tracker, Sprint status, Module progress bars

### 2.3 Bot Command Interface

| Command | Response |
|---|---|
| /start | Welcome message |
| /addme | Subscribe to daily briefings |
| /removeme | Unsubscribe |
| /status | Check subscription status |
| /subscribers | Admin only: list all subscribers |

## 3. Planned Interfaces

### 3.1 Public Web Interface (Phase 3)
- Login page (COTRUGLI credentials or Google Auth)
- Personal North Star dashboard
- Daily briefing archive (searchable)
- Q&A interface powered by Claude/Gemini
- Progress tracking: module completion, JTBD status
- Settings: notification preferences, timezone, briefing time

### 3.2 Mobile App (Phase 4)
- Push notifications for deadline alerts (48hr and 24hr warnings)
- Offline access to briefing archive
- Quick JTBD status update
- One-tap Zoom join from next session card

## 4. User Journeys

### New Student Onboarding
1. Find @CotNavigatorBot on Telegram
2. Send /start — receive welcome message
3. Send /addme — subscribed
4. Next morning at 05:30 — first briefing arrives
5. At 06:00 — model answer arrives

### Daily Student Interaction
1. 05:30 — Briefing arrives
2. Scan: deadlines, zoom, today's focus
3. Read knowledge question over breakfast
4. 06:00 — Model answer arrives, check understanding
5. During day — access dashboard for calendar view

## 5. Design Specifications

### Colour Palette (North Star Dashboard)
- Background: #0a0f1e (deep navy)
- Surface panels: #111827
- Primary accent: #00d4ff (electric blue)
- Warning: #ff6b35 (orange)
- Success: #00ff88 (green)
- Text primary: #e2e8f0
- Text secondary: #94a3b8

### Typography
- Dashboard headings: Orbitron (Google Font) — tactical, technical
- Dashboard body: Space Grotesk — modern, readable
- Telegram messages: System default — clean, fast-loading
