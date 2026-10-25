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
    
    inputs_data = page.evaluate("""() => {
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return null;
        
        const inputs = Array.from(dialog.querySelectorAll('input, select, [role="switch"]'));
        return inputs.map(el => {
            const container = el.closest('div.space-y-2') || el.closest('div.flex') || el.parentElement;
            const label = container?.querySelector('label')?.innerText || el.getAttribute('aria-label') || '';
            return {
                tagName: el.tagName,
                type: el.type,
                value: el.value,
                placeholder: el.placeholder,
                checked: el.checked,
                ariaChecked: el.getAttribute('aria-checked'),
                label: label.trim()
            };
        });
    }""")
    print("Inputs Data in Modal:")
    for inp in inputs_data:
        if inp.get('label') or inp.get('placeholder') or inp.get('value'):
            print(f"- Label: '{inp.get('label')}' | Val: '{inp.get('value')}' | Placeholder: '{inp.get('placeholder')}' | Checked: {inp.get('checked')} / {inp.get('ariaChecked')}")
