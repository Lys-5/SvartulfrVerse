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
    
    dialog_info = page.evaluate("""() => {
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return { error: 'No dialog' };
        
        const title = dialog.querySelector('h1, h2, h3, [role="heading"]')?.innerText || '';
        const tabs = Array.from(dialog.querySelectorAll('[role="tab"]')).map(b => ({
            text: b.innerText,
            selected: b.getAttribute('aria-selected')
        }));
        
        return {
            title,
            dialogText: dialog.innerText,
            tabs
        };
    }""")
    print('Dialog Title:', dialog_info.get('title'))
    print('Tabs:', dialog_info.get('tabs'))
    print('='*50)
    print('Full Dialog Text:\n', dialog_info.get('dialogText'))
