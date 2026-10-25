import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # 1. Inspect Simulation > Settings
    btn_settings = page.locator('button:has-text("Settings")').filter(has_not=page.locator('[role="dialog"] button')).first
    print("Simulation Settings button:", btn_settings.count())
    if btn_settings.is_visible():
        btn_settings.click()
        page.wait_for_timeout(500)
        panel_text = page.evaluate("""() => {
            const panel = document.querySelector('div.border-l') || document.querySelector('aside');
            return panel ? panel.innerText : 'Not found';
        }""")
        print("=== SIMULATION > SETTINGS ===")
        print(panel_text[:2000])

    # 2. Inspect Simulation > Party
    btn_party = page.locator('button:has-text("Party")').first
    if btn_party.is_visible():
        btn_party.click()
        page.wait_for_timeout(500)
        panel_text = page.evaluate("""() => {
            const panel = document.querySelector('div.border-l') || document.querySelector('aside');
            return panel ? panel.innerText : 'Not found';
        }""")
        print("\n=== SIMULATION > PARTY ===")
        print(panel_text[:2000])

    # 3. Inspect Simulation > Stats
    btn_stats = page.locator('button:has-text("Stats")').first
    if btn_stats.is_visible():
        btn_stats.click()
        page.wait_for_timeout(500)
        panel_text = page.evaluate("""() => {
            const panel = document.querySelector('div.border-l') || document.querySelector('aside');
            return panel ? panel.innerText : 'Not found';
        }""")
        print("\n=== SIMULATION > STATS ===")
        print(panel_text[:2000])
