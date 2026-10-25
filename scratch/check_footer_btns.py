import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    footer_buttons = page.evaluate("""() => {
        const d = document.querySelector('[role="dialog"]');
        if (!d) return [];
        // Look at the last elements / footer
        const btns = Array.from(d.querySelectorAll('button'));
        return btns.slice(-10).map(b => ({
            text: b.innerText,
            disabled: b.disabled,
            visible: b.offsetParent !== null
        }));
    }""")
    print("Footer buttons:")
    for b in footer_buttons:
        print(f"  '{b['text']}': disabled={b['disabled']}, visible={b['visible']}")
