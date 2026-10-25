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
    
    # Let's inspect the entire text and form fields of the currently visible dialog
    dialog = page.locator('[role="dialog"]').first
    print("Dialog visible:", dialog.is_visible())
    
    # Get all form fields in dialog
    fields = page.evaluate("""() => {
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return null;
        
        const inputs = Array.from(dialog.querySelectorAll('input, select, textarea, button[role="combobox"]'));
        return inputs.map(el => {
            let label = el.closest('.form-item')?.querySelector('label')?.innerText ||
                        el.closest('div')?.querySelector('label')?.innerText ||
                        el.getAttribute('aria-label') ||
                        el.name || el.id || '';
            return {
                tagName: el.tagName,
                type: el.type,
                name: el.name,
                id: el.id,
                value: el.value || el.innerText,
                checked: el.checked,
                placeholder: el.placeholder,
                label: label.trim()
            };
        });
    }""")
    print("Form fields in open modal:")
    print(json.dumps(fields, indent=2))
