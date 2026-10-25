import os
import sys
import json
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
TOKEN = open(TOKEN_PATH, 'r', encoding='utf-8').read().strip()

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Log in by setting token in localStorage
    page.goto("https://app.wyvern.chat", wait_until="domcontentloaded", timeout=30000)
    page.evaluate(f"""(token) => {{
        localStorage.setItem('auth_token', token);
        localStorage.setItem('token', token);
    }}""", TOKEN)

    # Now inspect sidebar links
    sidebar_links = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('a')).map(a => ({
            href: a.href,
            text: a.innerText.trim()
        }));
    }""")
    print("Sidebar / Page Links:")
    for l in sidebar_links:
        if any(w in l['href'].lower() or w in l['text'].lower() for w in ['world', 'mine', 'scenario', 'lorebook', 'explore']):
            print("  ", l)

    browser.close()
