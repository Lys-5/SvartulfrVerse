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
    
    # 1. Click Simulation tab on the right sidebar
    sim_tab = page.locator('button[title="Simulation"], button[aria-label="Simulation"]').first
    sim_tab.click()
    page.wait_for_timeout(500)
    
    # 2. Inspect tabs inside the simulation panel
    sim_tabs = page.evaluate("""() => {
        const panel = document.querySelector('div.border-l') || document.querySelector('aside');
        if (!panel) return [];
        const tabs = Array.from(panel.querySelectorAll('[role="tab"], button')).map(b => ({
            text: b.innerText.trim(),
            role: b.getAttribute('role'),
            selected: b.getAttribute('aria-selected')
        })).filter(b => b.text.length > 0 && b.text.length < 30);
        return tabs;
    }""")
    print("Simulation Panel Internal Tabs:")
    for t in sim_tabs:
        print(f"  [{t['role']}] '{t['text']}' (selected: {t['selected']})")
