import os
import time
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws_endpoint = f'ws://127.0.0.1:{port}{ws_path}'
print(f"Connecting to Chrome CDP at {ws_endpoint}...")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    page = context.new_page()

    try:
        url = "https://app.wyvern.chat/mine"
        print(f"Navigating to {url}...")
        page.goto(url, wait_until="domcontentloaded", timeout=20000)
        time.sleep(5)

        title = page.title()
        curr_url = page.url
        print(f"Loaded: title='{title}', url='{curr_url}'")

        # Extract character cards rendered in DOM
        cards_info = page.evaluate("""() => {
            const results = [];
            // Look for character elements / cards
            const imgEls = Array.from(document.querySelectorAll('img'));
            imgEls.forEach(img => {
                const src = img.getAttribute('src') || '';
                const alt = img.getAttribute('alt') || '';
                // find closest card container or text
                const container = img.closest('a') || img.closest('div[role="button"]') || img.parentElement;
                const text = container ? container.innerText : '';
                results.push({ src, alt, text: text ? text.slice(0, 100) : '' });
            });
            return {
                bodyTextSample: document.body.innerText.slice(0, 500),
                images: results
            };
        }""")

        print("\nPage body text sample:")
        print(cards_info.get("bodyTextSample"))

        print("\nRendered Images found:")
        for im in cards_info.get("images", []):
            if "imagedelivery.net" in im["src"]:
                print(f"  Img: src={im['src']} | alt={im['alt']} | text={im['text'][:60].strip()}")

    finally:
        page.close()
        print("\nVerification tab closed cleanly.")
