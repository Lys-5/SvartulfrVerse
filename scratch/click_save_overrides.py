import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    save_btn = page.locator('button:has-text("Save chat overrides")')
    print("Save chat overrides count:", save_btn.count())
    if save_btn.count() > 0:
        print("Visible:", save_btn.first.is_visible())
        print("Enabled:", save_btn.first.is_enabled())
        # Let's click it to persist!
        if save_btn.first.is_visible() and save_btn.first.is_enabled():
            save_btn.first.click()
            print("Clicked 'Save chat overrides'!")
            page.wait_for_timeout(500)
