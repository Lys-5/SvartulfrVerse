import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    dialog = page.locator('[role="dialog"]')
    buttons = dialog.locator('button')
    print("Buttons count in dialog:", buttons.count())
    for i in range(buttons.count()):
        b = buttons.nth(i)
        t = b.inner_text().strip()
        if t in ['Save', 'Cancel', 'Close', 'Apply', 'OK']:
            print(f"Button '{t}': visible={b.is_visible()}, enabled={b.is_enabled()}")
