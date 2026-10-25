import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
TOKEN = open(TOKEN_PATH, 'r', encoding='utf-8').read().strip()

urls = [
    'https://app.wyvern.chat/u/lys',
    'https://app.wyvern.chat/user/lys',
    'https://app.wyvern.chat/profile',
    'https://app.wyvern.chat/user/2r4fVpvImte5dbljedLkZJxre2d2'
]

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://app.wyvern.chat", wait_until="domcontentloaded", timeout=30000)
    page.evaluate(f"""(token) => {{
        localStorage.setItem('auth_token', token);
        localStorage.setItem('token', token);
    }}""", TOKEN)

    for u in urls:
        resp = page.goto(u, wait_until="networkidle", timeout=30000)
        time.sleep(2)
        print(f"URL: {u} -> Status: {resp.status}, final URL: {page.url}")
        
        # Check tabs on the profile page
        tabs = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('button, a, [role=\"tab\"]')).map(el => el.innerText.trim()).filter(t => t.length > 0 && t.length < 30);
        }""")
        print("  Tabs/Buttons:", [t for t in tabs if any(w in t.lower() for w in ['world', 'character', 'lorebook', 'scenario', 'created', 'public', 'private'])])

    browser.close()
