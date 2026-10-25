import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # Find all buttons in the top header or right side of the chat interface
    buttons_info = page.evaluate("""() => {
        const buttons = Array.from(document.querySelectorAll('button')).map(b => {
            const rect = b.getBoundingClientRect();
            return {
                text: b.innerText.trim(),
                ariaLabel: b.getAttribute('aria-label'),
                title: b.getAttribute('title'),
                x: rect.x,
                y: rect.y,
                width: rect.width,
                height: rect.height,
                classes: b.className
            };
        });
        
        // Filter buttons on the top header or right side (x > 800)
        return buttons.filter(b => b.x > 800 && b.y < 300);
    }""")
    print("Header / Right-side Buttons:")
    for b in buttons_info:
        print(f"  Pos ({int(b['x'])}, {int(b['y'])}): text='{b['text']}', label='{b['ariaLabel']}', title='{b['title']}'")
