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
    
    details = page.evaluate("""() => {
        const d = document.querySelector('[role="dialog"]');
        if (!d) return [];
        
        const switches = Array.from(d.querySelectorAll('[role="switch"]'));
        return switches.map(s => {
            // Find preceding heading or closest container text
            let p = s.parentElement;
            let context = '';
            for (let i = 0; i < 4; i++) {
                if (!p) break;
                if (p.innerText.length > 5 && p.innerText.length < 200) {
                    context = p.innerText;
                    break;
                }
                p = p.parentElement;
            }
            return {
                id: s.id,
                ariaChecked: s.getAttribute('aria-checked'),
                context: context.replace(/\\n+/g, ' -- ')
            };
        });
    }""")
    for d in details:
        print(f"Switch [{d['ariaChecked']}]: {d['context']}")
