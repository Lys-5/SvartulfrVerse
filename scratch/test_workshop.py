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

    # Log in
    page.goto("https://app.wyvern.chat", wait_until="domcontentloaded", timeout=30000)
    page.evaluate(f"""(token) => {{
        localStorage.setItem('auth_token', token);
        localStorage.setItem('token', token);
    }}""", TOKEN)

    # Click or navigate to Workshop
    # Let's inspect where "Workshop" button/link goes
    page.goto("https://app.wyvern.chat/explore?tab=worlds", wait_until="networkidle", timeout=30000)
    time.sleep(2)

    buttons = page.evaluate("""() => {
        let b = Array.from(document.querySelectorAll('button, a')).filter(x => x.innerText.includes('Workshop'));
        return b.map(x => ({ text: x.innerText, href: x.href, tag: x.tagName }));
    }""")
    print("Workshop elements:", buttons)

    # Click on Workshop button
    page.locator("button:has-text('Workshop')").first.click()
    time.sleep(3)
    print("After clicking Workshop, URL:", page.url)

    # Get body text or cards
    body_text = page.evaluate("() => document.body.innerText")
    lines = [l.strip() for l in body_text.split('\n') if l.strip()]
    print("\nPage lines after Workshop click:")
    for l in lines[30:80]:
        print("  ", l)

    browser.close()
