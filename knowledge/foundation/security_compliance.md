# Cotrugli Navigator — Security & Compliance Document
**Version:** 1.0 | **Date:** March 2026 | **Author:** Nardus Du Plooy
**Classification:** CONFIDENTIAL

## ⚠️ CRITICAL LESSON LEARNED (March 2026)
Using a personal Telegram account to automatically read messages from multiple channels violated Telegram's Terms of Service. The account was SUSPENDED. Navigator was redesigned to use only the official Bot API. No personal credentials are used for channel access. **This must never happen again.**

## 1. Credentials

| Credential | Purpose | Storage |
|---|---|---|
| ANTHROPIC_API_KEY | Claude LLM API | .env file only |
| TELEGRAM_BOT_TOKEN | CotNavigatorBot authentication | .env file only |
| GOOGLE_API_KEY | Gemini API (future) | .env file only |
| COTRUGLI_USERNAME | Portal scraper | .env file only |
| COTRUGLI_PASSWORD | Portal scraper | .env file only |

## 2. Credential Security Rules — NON-NEGOTIABLE
- .env file listed in .gitignore — NEVER committed to GitHub
- No credentials in any code file, prompt, or conversation history
- No credentials shared via Telegram, email, or any messaging platform
- All credentials rotated immediately after any suspected exposure
- GitHub push protection enabled

**INCIDENT (March 2026):** .env.save editor backup accidentally committed to GitHub. Anthropic API key exposed. Immediately detected, all credentials revoked and regenerated. .env.save added to .gitignore.

## 3. Platform Compliance

### 3.1 Telegram — CRITICAL
Telegram ToS requirements:
- Bots may only read messages in groups/channels where they are OFFICIAL MEMBERS
- Automated collection using personal account credentials is PROHIBITED
- Bots must not be used for mass messaging or spam

**Navigator compliance status:**
- ✅ COMPLIANT: Bot API only — @CotNavigatorBot
- ✅ COMPLIANT: No personal account credentials used
- ✅ COMPLIANT: Users opt in via /addme — no unsolicited messaging
- 🚫 PERMANENTLY DISABLED: Personal account Telethon library (read_channels.py)
- ⏳ PENDING: Bot must be officially added to channels by administrators

### 3.2 Cotrugli Portal
- Read-only access only — NO write, edit, or delete operations
- Single-student scope — only requesting student's own data
- Formal approval required from COTRUGLI IT before re-enabling
- Portal scraper (portal_scraper.py) currently DISABLED

### 3.3 Anthropic API
- Used for daily knowledge question and answer generation only
- No student personal data sent beyond programme content
- API key rotated after March 2026 security incident

## 4. Compliance Checklist — Before Each New Feature
- [ ] Does this feature access any external platform? → Review their ToS before building
- [ ] Does this feature use personal user credentials? → Ensure explicit user consent
- [ ] Does this feature store personal data? → Document what, why, and how long
- [ ] Does this feature send data to an external API? → Ensure no PII included
- [ ] Has this feature been tested in isolation before connecting to production subscribers?

## 5. Data Privacy

### Data Stored
- subscribers.json: Telegram chat IDs and names only
- deadlines.json: Programme deadline data — not personal
- navigator_data.json: Telegram channel messages — programme content only

### Data NOT Collected
- No location data, device data, browsing history, financial data, biometric data
- No private Telegram messages

### Data Sharing
- No student data shared with any third party
- Claude API receives anonymised programme content only — no PII

## 6. Known Security Gaps (MVP Phase)
- No authentication on local Flask dashboard
- JSON file storage has no encryption
- No rate limiting on bot commands
- Single-device deployment — no redundancy

## 7. Incident Log

| Date | Incident | Impact | Resolution |
|---|---|---|---|
| March 2026 | API key exposed in .env.save commit | Anthropic API key compromised | Key revoked, regenerated, .env.save added to .gitignore |
| March 2026 | Telegram ToS violation — personal account scraping | Account suspended, bot offline ~2 days | Architecture redesigned to Bot API only. New bot @CotNavigatorBot created. |
