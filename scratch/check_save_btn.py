import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    save_btn = page.locator('button:has-text("Save")')
    for i in range(save_btn.count()):
        b = save_btn.nth(i)
        print(f"Save button {i}: visible={b.is_visible()}, enabled={b.is_enabled()}, text='{b.inner_text()}'")
