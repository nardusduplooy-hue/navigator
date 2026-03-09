# 🧭 Cotrugli Navigator + North Star

> *"We don't build in secret. We build together."* — Dr. Tali Režun, Vice Dean, COTRUGLI Business School

## What is this?

**Navigator** is an AI orchestration agent built for the COTRUGLI Vanguard MBA programme. It consolidates Telegram channels, programme documents, and deadlines into one always-current intelligence feed — delivered to your phone every morning.

**North Star** is the planning layer on top. Countdowns on every deadline. No more hunting across 13 channels for a Zoom link posted three days ago.

This is a live build project, developed through the **Chasing Jarvis** course as the eX Venture project.

---

## The Problem It Solves

The Vanguard MBA has 14 Telegram channels, a portal that changes without notice, and a programme schedule that evolves in real time. For the African and Asian online cohort — the first time COTRUGLI has run this format — there is no physical classroom, no corridor announcements, no informal information flow.

Navigator is survival infrastructure for students who can't afford to miss a deadline buried in channel 9 of 14.

---

## What It Does Right Now

- **Reads all 13 Vanguard Telegram channels** automatically
- **Filters for deadlines, Zoom links, JTBDs, and announcements**
- **Sends a daily briefing to your phone** via Telegram bot with:
  - Active deadlines with dates and times
  - Next session information
  - JTBD status
  - 2 curated podcast episodes on AI and context engineering
  - 3 curated articles on AI development and safety
- **Answers questions in plain English** using Claude AI connected to live channel data

---

## Coming Next

- Web dashboard — calendar view, JTBD tracker, countdown timers
- Portal scraper — reads cotrugli.online course materials
- CPN — Cotrugli Personal Navigator — character formation layer

---

## Tech Stack

| Component | Tool |
|---|---|
| Telegram reading | Telethon 1.42 |
| Telegram bot | python-telegram-bot 22.6 |
| AI intelligence | Claude API (Anthropic) |
| Language | Python 3.14 |

---

## Built By

**Nardus Du Plooy** — Vanguard Chief, Team Chiron
COTRUGLI Vanguard MBA 2025–2027 | Cape Town, South Africa

Built with institutional support from COTRUGLI Business School.

---

## Status

🟢 Sprint 1 Complete — Channel reader + daily briefing operational
🔵 Sprint 2 Next — Web dashboard
⚪ Sprint 3 — Portal scraper
⚪ Sprint 4 — CPN character layer

*Navigator is the compass. North Star is the destination. CPN is who you become on the way.*
