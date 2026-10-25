import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    close_btn = page.locator('[role="dialog"] button:has-text("Close")')
    if close_btn.count() > 0 and close_btn.first.is_visible():
        close_btn.first.click()
        print("Clicked Close on dialog!")
        page.wait_for_timeout(500)
    
    # Check if dialog closed
    dialog = page.locator('[role="dialog"]')
    print("Dialog is still open:", dialog.count() > 0 and dialog.first.is_visible())
