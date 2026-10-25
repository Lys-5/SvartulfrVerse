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
    
    settings_full = page.evaluate("""() => {
        const panel = document.querySelector('div.border-l') || document.querySelector('aside');
        if (!panel) return {};
        
        const switches = Array.from(panel.querySelectorAll('[role="switch"]')).map(s => {
            const container = s.closest('div.flex') || s.parentElement;
            const label = container?.innerText?.replace(/\\n+/g, ' ') || '';
            return {
                label,
                checked: s.getAttribute('aria-checked')
            };
        });
        
        return {
            text: panel.innerText,
            switches
        };
    }""")
    print("=== SIMULATION SETTINGS SWITCHES ===")
    for s in settings_full.get('switches', []):
        print(f"  - '{s['label']}' -> {s['checked']}")
    print("\n=== FULL SETTINGS TEXT ===")
    print(settings_full.get('text'))
