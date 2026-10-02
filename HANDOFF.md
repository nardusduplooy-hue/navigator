# NAVIGATOR DAILY BRIEFING — HANDOFF
**Handed over: Friday 2 October 2026**
**Last date fully built and committed: 2 October 2026**

---

## WHAT THIS IS

The Cotrugli Navigator sends a daily Telegram briefing to the Vanguard MBA cohort and a matching LinkedIn post. Claude builds the content each morning, Nardus test-sends, approves, and commits. The whole workflow runs in one chat session — no servers, no automation.

Two Python files run everything:
- **`daily_briefing.py`** — renders and sends the Telegram briefing
- **`jarvis_content.py`** — stores all content (chapters, AI news, test questions, model answers, etc.)

Both files live in `~/Documents/navigator/` on Nardus's Mac.

---

## EXACT DAILY WORKFLOW — STEP BY STEP

### NARDUS DOES:
1. Opens a new chat (or continues this one)
2. Uploads yesterday's briefing spreadsheet (e.g., `Briefing_for_5_Oct.xlsx`)
3. Uploads today's `daily_briefing.py` and `jarvis_content.py` from `~/Documents/navigator/` if they are NOT already in the session (they reset between sessions — see WORKSPACE below)
4. Says "let's go"

### CLAUDE DOES (in this order — don't skip steps):
1. Reads the spreadsheet — every non-empty cell, both A and B columns
2. Checks the chapter from `VANGUARD_SUMMARIES[date]` (already pre-written through 2026-11-09)
3. Researches fresh AI news via web search (real story, not reused from previous day)
4. Drafts the 5 data entries for the day
5. Makes all code edits (structural first, data last)
6. Runs the full verification suite (see below)
7. Renders and reads the briefing output
8. Delivers both files as downloads
9. Gives the test-send command

### NARDUS DOES:
5. Downloads the files, copies them to `~/Documents/navigator/`
6. Runs the test-send command
7. Reads the result in his Telegram
8. Says "all good" or gives feedback

### CLAUDE DOES:
10. Gives the git commit block (on "all good")

### NARDUS DOES:
9. Runs the git commit block
10. Pastes the `git show --stat HEAD` output
11. Says "linkedin" (Claude builds the image)
12. Says "caption and comment" (Claude writes both)
13. Posts to LinkedIn

---

## HOW TO READ THE SPREADSHEET

- **Column A**: Today's already-sent briefing (what went out yesterday)
- **Column B**: Changes for tomorrow — **this is what you act on**
- **B = "new for tomorrow"**: Draft fresh content for that row
- **B = "remove"**: Remove that line from the code for tomorrow's date onwards
- **B = literal text**: That exact text replaces whatever was in A
- **B = Unicode bold text** (e.g., `𝗠𝗶𝘅𝗶𝗻𝗴 𝗔𝗜`): **MUST be sliced from the spreadsheet cell directly, never retyped.** Retyping garbles the characters. Use:
  ```python
  ws['B45'].value  # then open('/tmp/b45.txt','w',encoding='utf-8').write(value)
  ```
  Then verify with `assert exact_b45 in content` after inserting.

---

## THE 5 DATA ENTRIES — WHAT THEY ARE AND WHERE THEY LIVE

Every day, these 5 things need new entries in `daily_briefing.py` or `jarvis_content.py`:

| Entry | File | Dict name | Key format |
|---|---|---|---|
| Vanguard Teams question | `daily_briefing.py` | `vanguard_teams_lines` | `"YYYY-MM-DD": "question text"` |
| CJ post (primary) | `daily_briefing.py` | `cj_lookup` | `"YYYY-MM-DD": {"quote": "📄 <b>Title</b>", "url": "..."}` |
| AI News headline | `jarvis_content.py` | `AI_NEWS_OVERRIDE` | date-keyed dict entry |
| AI News mirror | `jarvis_content.py` | `AI_NEWS_TODAY` | flat dict, updated every day |
| Test question + model answer | `jarvis_content.py` | `TALI_STEPS` | date-keyed dict with focus/question/model_answer |

### OCCASIONAL EXTRAS:
- **Second CJ post**: `extra_cj_entries` in `daily_briefing.py` — same format as `cj_lookup`
- **KAPUSTA_TODAY**: Flat dict in `jarvis_content.py` for Dražen's post — update when Nardus flags B50/B51 (currently stale: pointing to CDayZ Zadar event since Sep 14 — NEEDS updating)

---

## READING THE CHAPTER (ZERO DRAFTING NEEDED)

The chapter for each date is already pre-written in `VANGUARD_SUMMARIES` through **2026-11-09**. Just read it:
```python
content.index('"YYYY-MM-DD": {')
# find and print the entry
```

The chapter's `summary` is the authoritative source for:
- The TALI_STEPS `question` and `model_answer` (base them here, connect to AI news)
- The LinkedIn image principles/pullquote
- The Vanguard Teams question angle

### CHAPTER CYCLE (as of handoff):
Chapters 1-13 cycle continuously. Weekends have entries in `VANGUARD_SUMMARIES` but briefings are **weekdays only** unless Nardus explicitly asks (use `--force-weekend` flag).

**Next dates:**
- Mon 5 Oct: Chapter 7 (NEO Leadership Challenge)
- Tue 6 Oct: Chapter 8 (Fear as Data)
- Wed 7 Oct: Chapter 9 (AI as Force Multiplier)
- Thu 8 Oct: Chapter 10 (Tribe as Coordination)
- Fri 9 Oct: Chapter 11 (What You Now Possess)
- Mon 12 Oct: Chapter 1 (cycle restarts)

---

## THE VANGUARD TEAMS QUESTION — HOW TO WRITE IT

- **~400 chars** (range: 300-450 — check with `len()`)
- Connects the day's **AI news** to the **chapter theme** with a direct question to the tribe
- Ends with a specific question that someone could actually answer today
- Voice: direct, no hedging, no "perhaps" — the cohort is doing serious work

---

## AI NEWS — RULES

1. **Real, researched, fresh** — web search every day, never reuse yesterday's story
2. **Thematic fit** — must connect to the chapter's angle, not just "AI news"
3. **Source and URL** both go in `AI_NEWS_OVERRIDE` and in `AI_NEWS_TODAY` (mirror dict)
4. **Headline length**: under 350 chars
5. **AI_NEWS_TODAY** is a flat dict that gets overwritten each day — always update it
6. The story goes into the Telegram briefing AND the LinkedIn comment

---

## THE VERIFICATION SUITE — RUN EVERY TIME

```python
# 1. Syntax check (both files)
import ast
ast.parse(open('daily_briefing.py', encoding='utf-8').read())
ast.parse(open('jarvis_content.py', encoding='utf-8').read())

# 2. Standing checks
# _DATE_OVERRIDE = None (not left set from testing)
# NEO_AXIOMS count: grep -c "NEO_AXIOMS" jarvis_content.py → must be 2

# 3. AST duplicate-key check (ALL dicts)
for fname, names in [
    ('jarvis_content.py', ("VANGUARD_SUMMARIES","TALI_STEPS","AI_NEWS_OVERRIDE")),
    ('daily_briefing.py', ("vanguard_teams_lines","cj_lookup","extra_cj_entries")),
]:
    tree = ast.parse(open(fname, encoding='utf-8').read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in names:
                    keys = [k.value for k in node.value.keys if isinstance(k, ast.Constant)]
                    dups = set(k for k in keys if keys.count(k) > 1)
                    print(f'{t.id}: {"DUPLICATES: "+str(dups) if dups else "OK"}')

# 4. Render check + SPLIT part sizes (CRITICAL — see bug below)
echo '[]' > subscribers.json && touch .env
python3 -c "
import daily_briefing as db
db._DATE_OVERRIDE = 'YYYY-MM-DD'
full = db.build_briefing()
parts = [p.strip() for p in full.split('⚡⚡SPLIT⚡⚡') if p.strip()]
print(f'Parts: {len(parts)}, sizes: {[len(p) for p in parts]}')
# ALL parts must be under 4096 chars or Telegram silently drops them
"
rm -f subscribers.json .env && rm -rf __pycache__
```

---

## THE SPLIT MARKER — CRITICAL BUG HISTORY

**Background**: Telegram has a 4096-char message limit. If any part exceeds it, Telegram silently fails to send that part — and only the model answer (sent separately, shorter) arrives. Nardus sees only the model answer and thinks the briefing sent.

**Fix applied**: A `⚡⚡SPLIT⚡⚡` marker is inserted **before the VANGUARD LEADERSHIP section** in `daily_briefing.py`. This splits the briefing into two Telegram messages, both under 4096 chars.

**Rule**: After every build, check `len(part)` for ALL parts. If any part is over 4096 → trim content or move the SPLIT marker earlier. The current split gives Part 1 ~2900 chars and Part 2 ~1580 chars — plenty of headroom.

---

## THE GIT DISCIPLINE

```bash
# ALWAYS add by name — NEVER git add -A or git add .
git add daily_briefing.py jarvis_content.py

git commit -m "DD Mon: [chapter] content, [what changed]"
git push
git show --stat HEAD
```

**Critical check**: `git show --stat HEAD` must show **2 files changed**. If it shows 1, one file didn't actually change (stale download bug — Nardus downloaded but overwrote with old version). Stop and diagnose before pushing further.

**If push is rejected** (remote has changes): 
```bash
git fetch origin
git log --oneline HEAD..origin/main  # see what's there
git pull --rebase origin main        # safe merge
git push
```
This happens when someone uploads directly via GitHub web UI (e.g., `navigator_app.html`).

---

## TEST-SEND COMMAND

```bash
# Weekday:
python daily_briefing.py --date YYYY-MM-DD --test-send

# Weekend (Saturday CDayZ briefings etc.):
python daily_briefing.py --date YYYY-MM-DD --force-weekend --test-send
```

`--test-send` sends **BOTH** the full briefing (all SPLIT parts) AND the model answer to Nardus's own Telegram chat only — nobody else receives it. If Nardus says "I only got the model answer," the briefing parts are over 4096 chars. Check part sizes immediately.

---

## LINKEDIN IMAGE — HOW TO BUILD IT

### WORKSPACE SETUP
`render_linkedin.py` must be in the working directory. On a fresh session:
```bash
cp /mnt/user-data/outputs/daily_briefing.py /mnt/user-data/outputs/jarvis_content.py /home/claude/navigator/
cp /mnt/user-data/uploads/render_linkedin.py /home/claude/navigator/
```

### PROCESS
1. Read the chapter's title/summary from `VANGUARD_SUMMARIES[date]` — principles/pullquote must match real content, never invented
2. Check if the same chapter was used recently — if yes, use a DIFFERENT layout (principles vs. pullquote alternately) and different angle
3. Write `build_DDMMM_linkedin.py` in `/home/claude/navigator/`
4. Run it, then **LOOK at the image** with `view()` before presenting — check for clipping, overflow, awkward gaps
5. Fix any spacing issues and re-render before presenting to Nardus

### PUNCTUATION IN GOLD RUNS
When splitting a title between white and gold text, **attach trailing punctuation to the gold run**, not the start of the white run:
- ✅ `("The Sheepdog Manifesto:", GOLD)` then `(" Rest of title", WHITE)`
- ❌ `("The Sheepdog Manifesto", GOLD)` then `(": Rest of title", WHITE)` → gap before colon

### COTRUGLIAN DIRECTION
For Chapter 2 (Prince or Trader) and similar chapters with two paths: **the image should signal which path the programme advocates**, not just present a neutral menu. Use pullquotes and framing that point toward the Cotruglian/Trader path without being preachy. Example:
> "The prince wins the room. The trader builds the relationship that decides the next one."

---

## LINKEDIN CAPTION & COMMENT

### CAPTION FORMAT (always this order):
```
Cotrugli Navigator: Daily Briefing | [Day] [Date] 2026 @Cotr
Chapter [N] - [Chapter name] @Draz
@Tali : [CJ post title]
Full briefing + links in the first comment
#VanguardMBA #CotrugliBusiness #NEOEra #AIinSales #CotruglNavigator
@alvin @carlien @matthys @jannes @narves @johan @chris @anena @boniphace @anab @duro @kaouther
```

### COMMENT (First comment under the post):
- **1250 char hard limit** — always measure with `len()` before presenting
- Structure: Chapter intro → chapter link → Vanguard Teams question → CJ post(s) with links → AI News → Sprint/Zoom → Roots quote
- If two CJ posts: both get their own line + link
- Zoom details go in the comment when a session is upcoming (include Meeting ID and Passcode)

---

## CURRENT STATE AT HANDOFF

### Files
- Last built: **Friday 2 October 2026** (Chapter 4: NEO Cotruglian Philosophy)
- `VANGUARD_SUMMARIES`: 180 keys, runway through **2026-11-09** ✓
- `TALI_STEPS`: 166 keys, last entry **2026-10-02** ✓
- `AI_NEWS_OVERRIDE`: 28 keys, last entry **2026-10-02** ✓
- `cj_lookup`: 70 keys, last entry **2026-10-02** ✓
- `vanguard_teams_lines`: 106 keys, last entry **2026-10-02** ✓

### Active Structural Features
- **SPLIT marker**: Before VANGUARD LEADERSHIP section — Part 1 ~2900 chars, Part 2 ~1580 chars ✓
- **Sprint 7**: Active from 2026-09-21 onward ✓
- **CDayZ block**: Shows minimal 2 lines ("📅 CDayZ 2026 / October 05–10, 2026 / Zadar") for Oct 2–10, then disappears ✓
- **Zoom (Oct 3)**: Confirmed session with Meeting ID 860 6551 7513, Passcode VGNEW3. After Oct 3 → "Watch this space." Next Claude must update with new Zoom details when provided.
- **KAPUSTA_TODAY**: Still pointing to CDayZ Zadar event — **STALE. Must be updated as soon as Nardus provides a new Dražen post URL.**
- **BAW**: Modules 2 & 3, Commander's Mindset, no podcasts (removed Oct 2+), no DEADLINES block (Module 3 deadline was Oct 1) ✓
- **AI in B2B Sales**: Module 3 / Tribal Architecture ✓
- **CJ section header** ("🎯 Chasing Jarvis — Dr. Tali Režun"): Removed from Sep 26+ ✓

---

## STRUCTURAL EDIT PATTERNS — HOW TO DO THEM SAFELY

### Adding a new date entry to any dict:
1. Find the last entry with `content.index('"YYYY-MM-DD":', idx_of_dict_start)`
2. Find where that entry ends with `content.index('\n    }', sub_idx)` for top-level dicts
3. Assert `content.count(anchor) == 1` before replacing
4. Run `ast.parse(content)` after every edit

### Adding a new date-range branch (Sprint, Zoom, CDayZ, BAW, etc.):
1. View the current code around the target section FIRST — `view()` the relevant lines
2. Use str_replace with a unique anchor (include surrounding lines if needed)
3. Test render the date AND the previous date (regression check)
4. Test at boundary dates: the day it starts, the day before, the day after

### BAW module label change:
The module label uses nested date conditions inside `if date_key >= "2026-07-03":`. Pattern:
```python
if date_key >= "2026-XX-XX":
    lines.append("🎧 <b>NEW LABEL</b>")
elif date_key >= "2026-09-23":
    lines.append("🎧 <b>BUSINESS AS WARFARE — MODULES 2 & 3</b>")
...
```

---

## KNOWN BUGS FIXED — DO NOT REPEAT

1. **CDayZ body code outside else**: The `body = ...` / `lines.append(body)` block MUST be INSIDE the `else:` clause. If it sits at the outer `if` level, it runs for ALL dates in the range including Oct 2+ even when the minimal block was supposed to show. ALWAYS verify by rendering the date and checking for duplicate blocks.

2. **Unicode CJ text retyping**: NEVER retype Unicode bold/stylized text from the B column. Always slice it from the spreadsheet cell:
   ```python
   b_value = ws['B45'].value
   open('/tmp/b45.txt', 'w', encoding='utf-8').write(b_value)
   # later:
   exact = open('/tmp/b45.txt', encoding='utf-8').read()
   assert exact in content  # verify it landed
   ```

3. **Workspace reset**: `/home/claude/navigator/` resets between chat sessions. Always rebuild from `/mnt/user-data/outputs/` at the start of every new session. Ask Nardus to upload `daily_briefing.py` and `jarvis_content.py` if outputs are empty.

4. **Test-send only sends model answer**: This means the briefing parts exceeded 4096 chars. Check `len(part)` for all parts immediately.

5. **AI Sales Module 3 all-caps**: From Sep 26+, the label is `AI IN B2B SALES — MODULE 3` (all caps). New sprint labels should match this pattern.

---

## WHAT NARDUS DOES / WHAT CLAUDE DOES — CLEAN SUMMARY

| Step | Who | What |
|---|---|---|
| Upload spreadsheet | Nardus | Daily, before building |
| Upload files (new session only) | Nardus | daily_briefing.py + jarvis_content.py |
| Read spreadsheet | Claude | All cells, A and B columns |
| Research AI news | Claude | Web search, real story, thematic fit |
| Write content | Claude | 5 dicts + any structural changes |
| Verify | Claude | Syntax + AST + render + part sizes |
| Deliver files | Claude | Present as downloads |
| Test-send | Nardus | Run command, read Telegram |
| Approve | Nardus | "all good" |
| Give commit block | Claude | With descriptive message |
| Commit and push | Nardus | git add by name, push, paste stat |
| Say "linkedin" | Nardus | |
| Build image | Claude | View before presenting, fix if needed |
| Say "caption and comment" | Nardus | |
| Write caption + comment | Claude | Measure lengths |
| Post | Nardus | LinkedIn |

---

## FILES AT HANDOFF

Both files are in `~/Documents/navigator/` on Nardus's Mac, committed to `github.com/nardusduplooy-hue/navigator` on branch `main`. Last commit was for 2 October 2026 content.

**To start the next session**: Nardus uploads the new spreadsheet + both Python files. Claude rebuilds the workspace, reads the spreadsheet, and begins.
