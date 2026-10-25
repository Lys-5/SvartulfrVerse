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
    
    # 1. Inspect Linked Connections
    tab_conn = page.locator('button[role="tab"]:has-text("Linked Connections")')
    tab_conn.click()
    page.wait_for_timeout(500)
    conn_text = page.locator('[role="dialog"]').inner_text()
    print("=== LINKED CONNECTIONS TAB ===")
    print(conn_text)
    
    # 2. Inspect Output Settings
    tab_out = page.locator('button[role="tab"]:has-text("Output Settings")')
    tab_out.click()
    page.wait_for_timeout(500)
    out_text = page.locator('[role="dialog"]').inner_text()
    print("\n=== OUTPUT SETTINGS TAB ===")
    print(out_text)

    # Return to Overrides & Extras
    tab_over = page.locator('button[role="tab"]:has-text("Overrides & Extras")')
    tab_over.click()
