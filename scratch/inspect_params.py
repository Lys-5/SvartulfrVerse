import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # Click Length Limits
    btn_length = page.locator('button:has-text("Length Limits")')
    if btn_length.is_visible():
        btn_length.click()
        page.wait_for_timeout(300)
        
    btn_easy = page.locator('button:has-text("Easy Parameters")')
    if btn_easy.is_visible():
        btn_easy.click()
        page.wait_for_timeout(300)

    details = page.evaluate("""() => {
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return null;
        return dialog.innerText;
    }""")
    print("=== EXPANDED EASY PARAMS & LENGTH LIMITS ===")
    print(details)
