import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # Locate inputs inside Easy Parameters
    inputs_info = page.evaluate("""() => {
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return null;
        
        // Find Easy Parameters container
        const labels = Array.from(dialog.querySelectorAll('label')).filter(l => 
            ['Temperature', 'Min P', 'Repetition Penalty', 'Presence Penalty', 'Min Tokens', 'Top P', 'Top K'].some(k => l.innerText.includes(k))
        );
        
        return labels.map(l => {
            const input = l.parentElement.querySelector('input') || l.closest('div').querySelector('input');
            return {
                label: l.innerText,
                inputId: input?.id,
                inputVal: input?.value,
                placeholder: input?.placeholder
            };
        });
    }""")
    print("Easy Parameters Inputs:")
    print(json.dumps(inputs_info, indent=2))
