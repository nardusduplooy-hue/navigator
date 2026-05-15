#!/usr/bin/env python3
"""
add_posts.py
------------
Reads new_posts.txt and adds faculty posts to the Navigator app.

Format of new_posts.txt (one post per line):
    kapusta | Post Title Here | https://linkedin.com/...
    tali | Post Title Here | https://linkedin.com/...

Usage:
    cd ~/Documents/navigator && source venv/bin/activate
    python3 add_posts.py
"""

import re
import subprocess
from pathlib import Path

BASE      = Path(__file__).parent
APP_FILE  = BASE / "navigator_app.html"
POSTS_FILE = BASE / "new_posts.txt"

EMPTY_FILE = "# Add posts here, one per line:\n# kapusta | Post Title | https://...\n# tali | Post Title | https://...\n"


def read_new_posts():
    if not POSTS_FILE.exists():
        POSTS_FILE.write_text(EMPTY_FILE)
        return []
    posts = []
    for line in POSTS_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 3:
            print(f"  Skipping malformed line: {line}")
            continue
        author, title, url = parts
        author = author.lower()
        if author not in ("kapusta", "tali"):
            print(f"  Skipping unknown author '{author}'")
            continue
        posts.append({"author": author, "title": title, "url": url})
    return posts


def already_exists(content, url):
    return url in content


def add_post(content, author, title, url):
    """Insert new post into the correct posts array."""
    # Find the array: kapusta: { ... posts: [ ... ] }
    # Anchor on the author key then find the posts array closing ]
    anchor = f"    {author}:" if author == "kapusta" else f"    {author}:"
    
    # Find posts: [ array for this author
    # Strategy: find "kapusta:" or "tali:" block, then find its posts array
    author_block_start = content.find(f'\n    {author}:')
    if author_block_start == -1:
        print(f"  Could not find {author} block.")
        return content

    # Find the posts array within this block
    posts_start = content.find("posts: [", author_block_start)
    if posts_start == -1:
        print(f"  Could not find posts array for {author}.")
        return content

    # Find the closing ] of the posts array
    # Walk forward counting brackets
    depth = 0
    i = content.find("[", posts_start)
    while i < len(content):
        if content[i] == "[":
            depth += 1
        elif content[i] == "]":
            depth -= 1
            if depth == 0:
                # Insert before this closing bracket
                new_entry = f'\n        {{ title: "{title}", url: "{url}" }},'
                content = content[:i] + new_entry + "\n      " + content[i:]
                print(f"  Added [{author.upper()}]: {title}")
                return content
        i += 1

    print(f"  Could not find closing bracket for {author} posts array.")
    return content


def git_push(titles):
    try:
        subprocess.run(["git", "add", "navigator_app.html"], cwd=BASE, check=True)
        msg = "Faculty posts: " + ", ".join(t[:40] for t in titles[:2])
        if len(titles) > 2:
            msg += f" +{len(titles)-2} more"
        subprocess.run(["git", "commit", "-m", msg], cwd=BASE, check=True)
        subprocess.run(["git", "pull", "--rebase"], cwd=BASE, check=True)
        subprocess.run(["git", "push"], cwd=BASE, check=True)
        print(f"\n✅ Pushed: {msg}")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Git error: {e}")
        print("   Run manually: git add -A && git commit -m 'posts' && git pull --rebase && git push")


def main():
    print("=" * 50)
    print("Navigator — Faculty Post Library Updater")
    print("=" * 50)

    posts = read_new_posts()
    if not posts:
        print("\nNo new posts in new_posts.txt.")
        print("Format: kapusta | Title | https://...")
        return

    print(f"\nAdding {len(posts)} post(s):\n")
    content = APP_FILE.read_text(encoding="utf-8")
    original = content
    added = []

    for p in posts:
        if already_exists(content, p["url"]):
            print(f"  Already exists, skipping: {p['title']}")
            continue
        content = add_post(content, p["author"], p["title"], p["url"])
        added.append(p["title"])

    if not added:
        print("\nNo new posts added.")
        return

    APP_FILE.write_text(content, encoding="utf-8")
    print(f"\n✅ {len(added)} post(s) added to navigator_app.html")

    POSTS_FILE.write_text(EMPTY_FILE)
    print("✅ new_posts.txt cleared")

    print("\nPushing to GitHub...")
    git_push(added)
    print("\n🎉 Done.")


if __name__ == "__main__":
    main()
