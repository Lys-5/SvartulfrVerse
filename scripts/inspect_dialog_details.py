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
        const dialogs = document.querySelectorAll('[role="dialog"], [role="alertdialog"], .modal, div[class*="modal"], div[class*="dialog"]');
        const root = dialogs.length ? dialogs[dialogs.length - 1] : document.body;
        
        const inputs = Array.from(root.querySelectorAll('input, select, textarea, [role="combobox"]')).map(el => {
            let label = '';
            if (el.id) {
                const l = document.querySelector(`label[for="${el.id}"]`);
                if (l) label = l.innerText;
            }
            if (!label) {
                const parentLabel = el.closest('label');
                if (parentLabel) label = parentLabel.innerText;
            }
            if (!label) {
                // look at previous sibling or parent header
                const prev = el.previousElementSibling;
                if (prev) label = prev.innerText;
            }
            return {
                id: el.id,
                name: el.name,
                type: el.type || el.tagName,
                value: el.value,
                placeholder: el.placeholder,
                label: label ? label.trim().replace(/\\n+/g, ' ') : '',
                ariaLabel: el.getAttribute('aria-label')
            };
        });
        
        return {
            text: root.innerText,
            inputs: inputs
        };
    }"""
    info = page.evaluate(js)
    print("=== DIALOG TEXT ===")
    print(info['text'])
    print("\n=== INPUTS ===")
    print(json.dumps(info['inputs'], indent=2))
