import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # Let's inspect the content of the right panel currently visible (AI Models)
    right_panel = page.evaluate("""() => {
        // Find the right sidebar container
        const aside = document.querySelector('aside') || document.querySelector('div.w-full.border-l') || document.querySelector('[data-panel-id]');
        
        // Find visible text in the right sidebar
        const sidebar = document.querySelector('div.flex-1.flex.flex-col.overflow-hidden') || document.querySelector('aside');
        
        // Let's get the text of the right side (excluding the chat area)
        const panel = document.querySelector('div.border-l') || document.querySelector('aside');
        return panel ? panel.innerText : document.body.innerText.slice(-2000);
    }""")
    print("=== CURRENT RIGHT SIDEBAR CONTENT (AI Models) ===")
    print(right_panel[:2500])
