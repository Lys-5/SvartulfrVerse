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
    
    subtabs = ['Party', 'Stats', 'Inventory', 'Settings']
    
    for st in subtabs:
        print(f"\n{'='*50}\n=== SIMULATION SUBTAB: {st} ===\n{'='*50}")
        # Click button with exact text
        res = page.evaluate(f"""(tabName) => {{
            const panel = document.querySelector('div.border-l') || document.querySelector('aside');
            if (!panel) return 'No panel';
            const btn = Array.from(panel.querySelectorAll('button, [role="tab"]')).find(b => b.innerText.trim() === tabName);
            if (btn) {{
                btn.click();
                return 'Clicked ' + tabName;
            }}
            return 'Button ' + tabName + ' not found';
        }}""", st)
        print(res)
        page.wait_for_timeout(600)
        
        panel_text = page.evaluate("""() => {
            const panel = document.querySelector('div.border-l') || document.querySelector('aside');
            return panel ? panel.innerText : 'None';
        }""")
        print(panel_text[:1500])
