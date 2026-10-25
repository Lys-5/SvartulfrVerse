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
    
    js = """() => {
        // Let's check checkboxes status
        const checkboxes = Array.from(document.querySelectorAll('input[type="checkbox"]')).map(cb => ({
            label: cb.closest('label')?.innerText || cb.parentElement?.innerText,
            checked: cb.checked
        }));
        
        // Let's search all IndexedDB databases more thoroughly
        return { checkboxes };
    }"""
    print(page.evaluate(js))
