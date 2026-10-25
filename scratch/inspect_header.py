import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # Inspect header / connection badges outside the modal
    header_info = page.evaluate("""() => {
        // Look for connection indicator, model badge, or buttons in the top navbar / chat header
        const badges = Array.from(document.querySelectorAll('header button, header [role="button"], div.sticky button, [data-testid="connection-selector"]')).map(el => ({
            text: el.innerText.trim(),
            title: el.getAttribute('title') || '',
            ariaLabel: el.getAttribute('aria-label') || ''
        }));
        
        const chatTitle = document.querySelector('header h1, header h2, .chat-title')?.innerText || '';
        return {
            chatTitle,
            badges
        };
    }""")
    print("Chat Header & Badges:")
    print(header_info)
