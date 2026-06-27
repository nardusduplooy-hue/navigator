# Cotrugli Navigator — Security & Compliance Document
**Version:** 2.0 | **Updated:** June 2026 | **Author:** Nardus Du Plooy
**Classification:** CONFIDENTIAL

## ⚠️ CRITICAL LESSON LEARNED (March 2026)
Using a personal Telegram account to automatically read messages from multiple channels violated Telegram's Terms of Service. The account was SUSPENDED. Navigator was redesigned to use only the official Bot API for all Telegram interactions. **Personal account credentials are permanently banned from this project.**

## ⚠️ SECOND LESSON (March 2026)
An `.env.save` editor backup file was accidentally committed to GitHub, exposing the Anthropic API key. Key was immediately revoked and regenerated. `.env.save` added to `.gitignore`.

**Rule: treat any file that might contain credentials as a credential. Add it to .gitignore before it touches the repo.**

## 1. Credentials

| Credential | Purpose | Storage |
|---|---|---|
| ANTHROPIC_API_KEY | Claude LLM API | .env file only |
| TELEGRAM_BOT_TOKEN | CotNavigatorBot authentication | .env file only |
| GOOGLE_API_KEY | Gemini API (future) | .env file only |
| COTRUGLI_USERNAME | Portal scraper (disabled) | .env file only |
| COTRUGLI_PASSWORD | Portal scraper (disabled) | .env file only |

## 2. Credential Security Rules — NON-NEGOTIABLE
- .env listed in .gitignore — NEVER committed to GitHub
- .env.save listed in .gitignore — editor backup files are equally dangerous
- No credentials in any code file, prompt, chat, or conversation history
- No credentials shared via Telegram, email, or any messaging platform
- All credentials rotated immediately after any suspected exposure
- GitHub push protection enabled

## 3. Platform Compliance

### 3.1 Telegram — COMPLIANT ✅
- ✅ Bot API only — @CotNavigatorBot — no personal account credentials used
- ✅ Sends to subscribers who opted in via /addme — no unsolicited messaging
- ✅ Posts to Navigator channel where bot is an official member
- ✅ No channel reading, scraping, or automated data collection from any Telegram channel
- 🚫 PERMANENTLY DISABLED: Personal account Telethon library
- ⏳ PENDING: Bot to be added to Vanguard programme channels by admins (Drazen Kapusta)

**On channel_listener.py:** This file exists but is not used in production. No Telegram channel reading of any kind is permitted or active. The account suspension in March 2026 was a direct result of automated channel reading — this will never be reintroduced in any form.

### 3.2 Cotrugli Portal
- Read-only access only — NO write, edit, or delete operations
- Single-student scope — only Nardus Du Plooy's own data
- Formal written approval required from COTRUGLI IT before re-enabling
- portal_scraper.py currently DISABLED

### 3.3 Anthropic API
- Used for daily knowledge question generation only
- No student personal data sent — programme content only
- API key rotated after March 2026 security incident

## 4. Compliance Checklist — Before Each New Feature
- [ ] Does this feature access any external platform? → Review their ToS before building
- [ ] Does this feature use personal user credentials? → Ensure explicit user consent
- [ ] Does this feature store personal data? → Document what, why, and how long
- [ ] Does this feature send data to an external API? → Ensure no PII included
- [ ] Has this feature been tested in isolation before connecting to production subscribers?
- [ ] Does this feature create any new files that could contain credentials? → Add to .gitignore first

## 5. Data Privacy

### Data Stored
- subscribers.json: Telegram chat IDs and display names only — no emails, no phone numbers
- deadlines.json: Programme deadline data — not personal
- logs/scheduler.log: Delivery confirmations with chat IDs — not personal content

### Data NOT Collected
- No location data, device data, browsing history, financial data, biometric data
- No private Telegram messages
- No content from Telegram channels

### Data Sharing
- No student data shared with any third party
- Claude API receives anonymised programme content only — no PII

## 6. Known Security Gaps (MVP Phase)
- No authentication on local Flask dashboard (localhost only — acceptable for now)
- JSON file storage has no encryption
- No rate limiting on bot commands
- Single-device deployment — no redundancy or failover

## 7. Incident Log

| Date | Incident | Impact | Resolution |
|---|---|---|---|
| March 2026 | API key exposed in .env.save commit | Anthropic API key compromised | Key revoked, regenerated. .env.save added to .gitignore |
| March 2026 | Telegram ToS violation — personal account scraping via Telethon | Account suspended, bot offline ~2 days | Architecture redesigned to Bot API only. New bot @CotNavigatorBot created. Personal credentials permanently removed. |
