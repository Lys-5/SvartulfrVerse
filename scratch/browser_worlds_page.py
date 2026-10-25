import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
TOKEN = open(TOKEN_PATH, 'r', encoding='utf-8').read().strip()

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://app.wyvern.chat", wait_until="domcontentloaded", timeout=30000)
    page.evaluate(f"""(token) => {{
        localStorage.setItem('auth_token', token);
        localStorage.setItem('token', token);
    }}""", TOKEN)

    # Now navigate to https://app.wyvern.chat/worlds
    print("Navigating to https://app.wyvern.chat/worlds...")
    page.goto("https://app.wyvern.chat/worlds", wait_until="domcontentloaded", timeout=30000)
    time.sleep(3)

    print("Current URL:", page.url)
    
    # Grab all text on page
    body_text = page.evaluate("() => document.body.innerText")
    print("\n--- Body text lines (first 50) ---")
    for line in [l for l in body_text.split('\n') if l.strip()][:50]:
        print("  ", line)

    # Grab all links
    links = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('a, button')).map(el => ({
            tag: el.tagName,
            href: el.href || '',
            text: el.innerText.trim()
        })).filter(x => x.text || x.href);
    }""")
    print("\n--- Links and buttons ---")
    for l in links[:40]:
        print("  ", l)

    browser.close()
