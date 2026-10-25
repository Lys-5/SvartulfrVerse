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
    
    # 1. Inspect Template Override section
    # Let's click on "Template Override" or check its content
    btn_template = page.locator('button:has-text("Template Override")')
    if btn_template.is_visible():
        btn_template.click()
        page.wait_for_timeout(500)
    
    btn_param = page.locator('button:has-text("Parameter Preset Override")')
    if btn_param.is_visible():
        btn_param.click()
        page.wait_for_timeout(500)

    overrides_text = page.locator('[role="dialog"]').inner_text()
    print("=== Overrides & Extras Expanded Text ===")
    print(overrides_text)
