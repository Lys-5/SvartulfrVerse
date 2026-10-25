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
    
    # Check current tab: Overrides & Extras
    # Let's see all accordions / collapsible sections in Overrides & Extras
    overrides_details = page.evaluate("""() => {
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return null;
        
        // Find all switches, checkboxes, buttons, accordions
        const items = Array.from(dialog.querySelectorAll('button, input, select, [role="switch"]')).map(el => {
            const label = el.closest('div')?.innerText?.split('\\n')[0] || el.getAttribute('aria-label') || el.innerText || '';
            return {
                text: el.innerText,
                tag: el.tagName,
                role: el.getAttribute('role'),
                type: el.type,
                ariaChecked: el.getAttribute('aria-checked'),
                checked: el.checked,
                value: el.value,
                id: el.id,
                label: label.slice(0, 100)
            };
        });
        return items;
    }""")
    print("Overrides & Extras items count:", len(overrides_details))
    for item in overrides_details:
        if item.get('role') in ['switch', 'combobox', 'tab'] or item.get('type') in ['checkbox']:
            print(f"[{item.get('role') or item.get('type')}] text: {item.get('text')} | checked: {item.get('ariaChecked') or item.get('checked')} | label: {item.get('label')}")
        elif item.get('tag') == 'BUTTON' and ('Override' in item.get('text') or 'Template' in item.get('text') or 'World' in item.get('text') or 'Parameter' in item.get('text')):
            print(f"[BUTTON] text: {item.get('text')} | value: {item.get('value')}")
