import os
import sys
import time
import json
from playwright.sync_api import sync_playwright

temp_profile = r'C:\Users\mande\.gemini\antigravity\brain\88874201-ff74-4d24-9b6a-25251d18ed6a\scratch\chrome_temp_profile'
chrome_dev_path = r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'

if not os.path.exists(chrome_dev_path):
    # fallback to regular chrome
    chrome_dev_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

print(f"Using Chrome binary: {chrome_dev_path}")
print(f"Using profile: {temp_profile}")

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        executable_path=chrome_dev_path,
        headless=True,
        args=[
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-renderer-backgrounding'
        ]
    )
    
    page = ctx.new_page()
    requests_log = []
    
    def on_req(req):
        if '/api/' in req.url:
            requests_log.append(f"{req.method} {req.url}")
            
    page.on("request", on_req)
    
    print("Navigating to https://app.wyvern.chat/worlds...")
    page.goto("https://app.wyvern.chat/worlds", wait_until="networkidle", timeout=30000)
    time.sleep(3)
    
    print("\n--- Network API requests made ---")
    for r in requests_log:
        print(" ", r)
        
    print("\n--- Page Title & URL ---")
    print("Title:", page.title())
    print("URL:", page.url)
    
    # Extract all links that contain 'world'
    links = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('a')).map(a => ({
            href: a.href,
            text: a.innerText.trim()
        })).filter(a => a.href.includes('/worlds/'));
    }""")
    print("\n--- World Links found on page ---")
    for l in links:
        print(" ", l)
        
    # Extract cards
    cards = page.evaluate("""() => {
        // Look for cards, items, or rows
        let items = Array.from(document.querySelectorAll('div, a, li')).filter(el => {
            return el.innerText && (el.innerText.includes('Svartúlfr') || el.innerText.includes('Blackwood') || el.innerText.includes('World'));
        });
        return items.map(el => el.innerText.slice(0, 150));
    }""")
    print("\n--- Snippets containing world text ---")
    seen = set()
    for c in cards[:25]:
        snippet = " ".join(c.split())
        if snippet not in seen and len(snippet) > 10:
            seen.add(snippet)
            print("  *", snippet[:100])
            
    ctx.close()
