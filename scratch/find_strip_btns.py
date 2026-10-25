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
    
    vertical_strip_btns = page.evaluate("""() => {
        // Find buttons in the vertical sidebar nav strip
        const buttons = Array.from(document.querySelectorAll('button')).map((b, i) => {
            const rect = b.getBoundingClientRect();
            return {
                index: i,
                text: b.innerText.trim(),
                title: b.title || b.getAttribute('aria-label') || '',
                x: rect.x,
                y: rect.y,
                w: rect.width,
                h: rect.height
            };
        }).filter(b => b.x > 1300 && b.x < 1400);
        return buttons;
    }""")
    print("Vertical Strip Buttons:")
    for b in vertical_strip_btns:
        print(f"  [{b['index']}] Pos ({b['x']}, {b['y']}): text='{b['text']}' | title='{b['title']}'")
