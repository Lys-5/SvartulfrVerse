"""
Headless Chrome Playwright verification for Wyvern Scenarios
"""
import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.sync_from_wyvern_web import get_auth_token

def main():
    token = get_auth_token()
    print("Launching Headless Chrome via Playwright...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        
        # Inject auth token into localStorage / cookies if possible
        page = context.new_page()
        
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        
        print("Navigating to https://app.wyvern.chat ...")
        page.goto("https://app.wyvern.chat", wait_until="domcontentloaded", timeout=30000)
        
        # Inject auth token into localStorage
        page.evaluate(f"""
            try {{
                localStorage.setItem('auth_token', '{token}');
                localStorage.setItem('token', '{token}');
            }} catch(e) {{}}
        """)
        
        print("Page Title:", page.title())
        
        # Check world scenarios explore page
        print("Navigating to /worlds/_YpX47fNraQFw2dD7TdycJ ...")
        page.goto("https://app.wyvern.chat/worlds/_YpX47fNraQFw2dD7TdycJ", wait_until="domcontentloaded", timeout=30000)
        time.sleep(3)
        print("World Page Title:", page.title())
        
        # Take a snapshot or check DOM
        content = page.content()
        print("Content length:", len(content))
        has_error_boundary = "Application error: a client-side exception has occurred" in content
        print("Has Client Crash Boundary:", has_error_boundary)
        assert not has_error_boundary, "Client-side exception error boundary detected!"
        
        browser.close()
        print("[SUCCESS] Headless Playwright verification completed cleanly with 0 crashes!")

if __name__ == '__main__':
    main()
