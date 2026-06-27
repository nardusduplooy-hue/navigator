# Cotrugli Navigator — UI/UX Document
**Version:** 2.0 | **Updated:** June 2026 | **Author:** Nardus Du Plooy
**Classification:** CONFIDENTIAL

## 1. Design Philosophy
> "Calm clarity in the face of programme complexity. The student is the captain. Navigator is the compass."

- **Calm over busy** — information hierarchy, not information overload
- **Countdown over calendar** — urgency is felt, not calculated
- **One screen, one truth** — North Star as single source of orientation
- **Dark and tactical** — serious tool aesthetic, not academic pastels

## 2. Current Interfaces

### 2.1 Telegram Daily Briefing — PRIMARY INTERFACE
Delivered at 06:00 SAST daily. Sent simultaneously to individual subscribers (DM) and the COTRUGLI Navigator Telegram channel topic.

**Briefing structure (as of June 2026):**
- Header: Date and briefing title
- 🏆 VANGUARD TEAMS: Daily motivational message (rotates daily)
- 🔴 DEADLINES: Active deadlines with context
- 📅 NEXT ZOOM SESSION: Upcoming session with link, Meeting ID, Passcode
- Module content block (current active module — rotates as programme progresses)
- 🎯 CHASING JARVIS: Dr. Tali Režun daily LinkedIn post with quote
- 📋 ASSIGNMENT: Current module assignment reminder
- 🏛️ VANGUARD LEADERSHIP: Dražen Kapusta book summary (daily chapter)
- 🌐 AI NEWS: Live VentureBeat feed (Anthropic/Claude filtered)
- 🧠 KNOWLEDGE QUESTION: Daily test question
- 📲 /addme prompt for new subscribers
- ⚡ Navigator out.

Model answer sent as a second message immediately after.

**Format notes:**
- HTML parse mode (Telegram)
- Clickable links using `<a href>` tags
- Bold headers using `<b>` tags
- Web page preview disabled to keep messages compact
- Long briefings split on `⚡⚡SPLIT⚡⚡` marker and sent as multiple messages

### 2.2 North Star Web Dashboard — LOCAL
Local web dashboard at localhost:5000. Dark tactical command center. Auto-refreshes every 5 minutes.

**Components:**
- Navigation header with NAVIGATOR logo and live CAT clock
- Hero section: Day/date display and programme name
- Stats bar: Message count, channel count, flagged items
- Left panel: Deadlines feed with countdown badges (RED/GREEN/SESSION)
- Centre panel: Interactive monthly calendar with event markers
- Right panel: JTBD tracker, Sprint status, Module progress bars

### 2.3 Bot Command Interface

| Command | Response | Access |
|---|---|---|
| /start | Welcome message | All users |
| /addme | Subscribe to daily briefings | All users |
| /removeme | Unsubscribe | Subscribers |
| /status | Check subscription status | All users |
| /subscribers | List all subscribers | Admin only (Nardus) |

New subscriber triggers a DM notification to Nardus with name, username, chat ID, and total subscriber count.

## 3. Planned Interfaces

### 3.1 Public Web Interface (Phase 2–3)
- Login page (COTRUGLI credentials or Google Auth)
- Personal North Star dashboard
- Daily briefing archive (searchable)
- Q&A interface powered by Claude/Gemini
- Progress tracking: module completion, assignment status
- Settings: notification preferences, timezone, briefing time

### 3.2 Mobile App (Phase 4)
- Push notifications for deadline alerts (48hr and 24hr warnings)
- Offline access to briefing archive
- Quick status update
- One-tap Zoom join from next session card

## 4. User Journeys

### New Student Onboarding
1. Find @CotNavigatorBot on Telegram
2. Send /start — receive welcome message
3. Send /addme — subscribed, Nardus notified
4. Next morning at 06:00 SAST — first briefing arrives
5. Model answer arrives immediately after

### Daily Student Interaction
1. 06:00 SAST — briefing arrives in DM and Navigator channel
2. Scan: deadlines, zoom, today's module focus
3. Read knowledge question
4. Model answer arrives — check understanding
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
