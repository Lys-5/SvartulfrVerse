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

    # Let's check multiple URLs:
    test_urls = [
        "https://app.wyvern.chat/explore?tab=worlds",
        "https://app.wyvern.chat/explore?tab=worlds&sort=recent",
        "https://app.wyvern.chat/worlds",
    ]

    for u in test_urls:
        print(f"\nNavigating to {u}...")
        page.goto(u, wait_until="networkidle", timeout=30000)
        time.sleep(3)

        cards_data = page.evaluate("""() => {
            let cards = Array.from(document.querySelectorAll('div, a')).filter(el => {
                return el.innerText && el.innerText.includes('Svartúlfr — Blackwood & Solarton');
            });
            
            // Find all anchor links inside or near these cards
            let found = [];
            for (let c of cards) {
                let links = Array.from(c.querySelectorAll('a')).map(a => a.href);
                let text = c.innerText.slice(0, 100);
                found.push({ text, links });
            }
            
            // Also find all links on entire page that have /worlds/
            let allWorldLinks = Array.from(document.querySelectorAll('a[href*=\"/worlds/\"]')).map(a => ({
                href: a.href,
                text: a.innerText.slice(0, 50)
            }));
            
            return { found: found.slice(0, 5), allWorldLinks };
        }""")
        
        print("World links on page:")
        for wl in cards_data.get('allWorldLinks', []):
            print("  ", wl)

    browser.close()
