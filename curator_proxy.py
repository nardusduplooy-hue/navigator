#!/usr/bin/env python3
"""
curator_proxy.py
----------------
Local HTTP proxy that connects the Cotrugli Navigator app to the
navigator-2nd-brain Curator domain.

How it works:
  1. Receives a question from the Navigator app via HTTP POST
  2. Searches the navigator-2nd-brain wiki for relevant markdown files
  3. Sends the question + wiki context to Claude API
  4. Returns the answer as JSON

Run:
  cd ~/Documents/navigator && source venv/bin/activate
  python3 curator_proxy.py

Runs on port 5001 by default.
Keep running alongside daily_briefing.py via launchd (see instructions below).
"""

import os
import re
import json
import glob
import anthropic
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
PORT = 5001
DOMAIN = "navigator-2nd-brain"
CURATOR_BASE = Path.home() / "the-curator" / "domains" / DOMAIN / "wiki"
MAX_FILES = 8       # max wiki files to include as context per query
MAX_CHARS  = 12000  # max total chars of wiki content per query
MODEL      = "claude-sonnet-4-20250514"

# ── Load credentials ──────────────────────────────────────────────────────────
with open(Path.home() / "Documents" / "navigator" / ".env") as f:
    env = dict(
        line.strip().split("=", 1)
        for line in f
        if "=" in line and not line.startswith("#")
    )

ANTHROPIC_API_KEY = env.get("ANTHROPIC_API_KEY", "")
if not ANTHROPIC_API_KEY:
    print("ERROR: ANTHROPIC_API_KEY not found in .env")
    print("Add ANTHROPIC_API_KEY=sk-ant-... to ~/Documents/navigator/.env")
    exit(1)

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# ── Wiki search ───────────────────────────────────────────────────────────────

def get_all_wiki_files():
    """Return all markdown files in the wiki."""
    patterns = [
        str(CURATOR_BASE / "concepts" / "*.md"),
        str(CURATOR_BASE / "entities" / "*.md"),
        str(CURATOR_BASE / "summaries" / "*.md"),
    ]
    files = []
    for p in patterns:
        files.extend(glob.glob(p))
    return files


def score_file(filepath: str, query_terms: list[str]) -> int:
    """Score a file by how many query terms appear in its name or content."""
    name = Path(filepath).stem.lower().replace("-", " ").replace("_", " ")
    try:
        content = open(filepath, encoding="utf-8").read(3000).lower()
    except Exception:
        content = ""

    score = 0
    for term in query_terms:
        t = term.lower()
        if t in name:
            score += 3
        if t in content:
            score += 1
    return score


def search_wiki(query: str, max_files: int = MAX_FILES) -> str:
    """Search the wiki for relevant files and return combined content."""
    # Tokenise query — strip common words
    stopwords = {"what", "is", "the", "a", "an", "in", "of", "and", "or",
                 "how", "why", "who", "does", "do", "explain", "tell", "me",
                 "about", "can", "you", "please", "describe", "define"}
    terms = [w for w in re.findall(r'\w+', query.lower()) if w not in stopwords and len(w) > 2]

    if not terms:
        terms = re.findall(r'\w+', query.lower())

    all_files = get_all_wiki_files()

    # Score and sort
    scored = [(f, score_file(f, terms)) for f in all_files]
    scored.sort(key=lambda x: x[1], reverse=True)

    # Take top scoring files with content
    selected = []
    total_chars = 0
    for filepath, score in scored:
        if score == 0:
            break
        if total_chars >= MAX_CHARS:
            break
        try:
            content = open(filepath, encoding="utf-8").read()
            # Strip frontmatter
            content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
            snippet = content[:2000]
            selected.append({
                "file": Path(filepath).stem,
                "content": snippet
            })
            total_chars += len(snippet)
            if len(selected) >= max_files:
                break
        except Exception:
            continue

    if not selected:
        return ""

    parts = []
    for item in selected:
        parts.append(f"### {item['file']}\n{item['content']}")
    return "\n\n---\n\n".join(parts)


# ── Claude API call ───────────────────────────────────────────────────────────

def ask_claude(question: str, wiki_context: str) -> str:
    """Send question + wiki context to Claude and return the answer."""
    if wiki_context:
        system = f"""You are the Cotrugli Navigator Second Brain — a knowledge assistant for Vanguard MBA students at Cotrugli Business School.

You answer questions using the knowledge from the Navigator's second brain wiki below. Be concise, direct, and practical. Use the wiki content as your primary source. If the wiki doesn't contain enough to answer fully, say so briefly and answer from general knowledge.

Always write in the tone of the Navigator: confident, no fluff, actionable.

WIKI CONTEXT:
{wiki_context}"""
    else:
        system = """You are the Cotrugli Navigator Second Brain — a knowledge assistant for Vanguard MBA students at Cotrugli Business School.

Answer questions about the programme, frameworks (NEO Era, Centaur Doctrine, NCTE, Cotruglian Philosophy), faculty (Kapusta, Dr. Tali Režun), and AI in business. Be concise, direct, and practical. Write in the tone of the Navigator: confident, no fluff, actionable."""

    message = client.messages.create(
        model=MODEL,
        max_tokens=600,
        system=system,
        messages=[{"role": "user", "content": question}]
    )
    return message.content[0].text


# ── HTTP handler ──────────────────────────────────────────────────────────────

class ProxyHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        print(f"[curator_proxy] {format % args}")

    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self._cors_headers()
        self.end_headers()

    def do_POST(self):
        if self.path != "/ask":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body)
            question = data.get("question", "").strip()
            if not question:
                raise ValueError("Empty question")
        except Exception as e:
            self.send_response(400)
            self._cors_headers()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
            return

        print(f"[curator_proxy] Question: {question[:80]}")

        try:
            wiki_context = search_wiki(question)
            files_used = len(re.findall(r'^### ', wiki_context, re.MULTILINE)) if wiki_context else 0
            print(f"[curator_proxy] Wiki files matched: {files_used}")

            answer = ask_claude(question, wiki_context)

            response = {
                "answer": answer,
                "sources": files_used,
                "domain": DOMAIN
            }

            self.send_response(200)
            self._cors_headers()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode())

        except Exception as e:
            print(f"[curator_proxy] ERROR: {e}")
            self.send_response(500)
            self._cors_headers()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Quick sanity check
    wiki_files = get_all_wiki_files()
    print(f"[curator_proxy] Navigator Second Brain: {len(wiki_files)} wiki files found")
    print(f"[curator_proxy] Curator path: {CURATOR_BASE}")

    if len(wiki_files) == 0:
        print(f"ERROR: No wiki files found at {CURATOR_BASE}")
        print("Check that the navigator-2nd-brain domain exists and has been ingested.")
        exit(1)

    print(f"[curator_proxy] Starting proxy on http://localhost:{PORT}")
    print(f"[curator_proxy] POST http://localhost:{PORT}/ask  {{\"question\": \"...\"}}")
    print(f"[curator_proxy] Press Ctrl+C to stop")

    server = HTTPServer(("localhost", PORT), ProxyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[curator_proxy] Stopped.")
