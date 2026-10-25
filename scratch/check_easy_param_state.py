import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    easy_param_state = page.evaluate("""() => {
        const d = document.querySelector('[role="dialog"]');
        if (!d) return null;
        
        const allInputs = Array.from(d.querySelectorAll('input')).map(i => {
            const lbl = i.closest('div.space-y-2')?.querySelector('label')?.innerText || i.parentElement?.innerText || '';
            return {
                label: lbl.replace(/\\n+/g, ' '),
                val: i.value,
                type: i.type,
                checked: i.checked
            };
        });
        
        return {
            allInputs
        };
    }""")
    print("Easy Heading:", easy_param_state.get('easyHeadingText'))
    print("All Inputs:")
    for inp in easy_param_state.get('allInputs', []):
        if any(k in inp['label'] for k in ['Temperature', 'Top P', 'Top K', 'Min P', 'Repetition', 'Presence', 'Frequency', 'Min Tokens', 'Max Tokens', 'Max Messages']):
            print(f"  {inp['label']} -> '{inp['val']}' (checked: {inp['checked']})")
