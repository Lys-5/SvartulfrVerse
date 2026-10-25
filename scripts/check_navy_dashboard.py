import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    context = browser.contexts[0]
    
    # Check if there is an existing tab with api.navy
    navy_page = None
    for pg in context.pages:
        if 'navy' in pg.url:
            navy_page = pg
            break
            
    if not navy_page:
        print("No navy page open in Chrome tabs.")
        # Let's open a background tab to check https://api.navy/dashboard
        temp_page = context.new_page()
        temp_page.goto('https://api.navy/dashboard', wait_until='networkidle', timeout=15000)
        print("Navy Dashboard title:", temp_page.title())
        print("Navy Dashboard URL:", temp_page.url)
        # Search for Free button and click it to see filtered models
        models = temp_page.evaluate('''() => {
            // Find all filter buttons
            const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim());
            
            // Get all model cards or rows
            const rows = Array.from(document.querySelectorAll('[class*="model"], tr, [role="row"]')).map(r => r.innerText.trim());
            return { buttons, rowsCount: rows.length, sampleRows: rows.slice(0, 10) };
        }''')
        print(models)
        temp_page.close()
    else:
        print("Found active navy page:", navy_page.url)
        models = navy_page.evaluate('''() => {
            const cards = Array.from(document.querySelectorAll('div, tr, li')).filter(el => el.innerText.includes('Free') && el.innerText.includes('Chat'));
            return cards.map(c => c.innerText.slice(0, 100));
        }''')
        print(models[:10])
