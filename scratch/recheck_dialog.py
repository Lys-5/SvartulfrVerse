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
    
    dialog = page.locator('[role="dialog"]')
    is_open = dialog.count() > 0 and dialog.first.is_visible()
    print('Dialog open:', is_open)
    print('Current Page URL:', page.url)
    
    if is_open:
        tabs = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('[role="dialog"] [role="tab"]')).map(t => ({
                text: t.innerText,
                selected: t.getAttribute('aria-selected')
            }));
        }""")
        print('Tabs:', tabs)
        
        inputs = page.evaluate("""() => {
            const d = document.querySelector('[role="dialog"]');
            const items = Array.from(d.querySelectorAll('input, select, [role="combobox"], [role="switch"]'));
            return items.map(el => {
                const container = el.closest('div.space-y-2') || el.closest('div.flex') || el.parentElement;
                const label = container?.querySelector('label')?.innerText || el.getAttribute('aria-label') || el.innerText || '';
                return {
                    tag: el.tagName,
                    role: el.getAttribute('role'),
                    type: el.type,
                    value: el.value || el.innerText,
                    checked: el.checked,
                    ariaChecked: el.getAttribute('aria-checked'),
                    label: label.trim()
                };
            });
        }""")
        print('Total inputs in dialog:', len(inputs))
        for item in inputs:
            val_display = item.get('value', '').replace('\n', ' ')
            chk = item.get('checked') if item.get('checked') is not None else item.get('ariaChecked')
            print(f"  - [{item.get('role') or item.get('type') or item.get('tag')}] '{item.get('label')}' -> val: '{val_display}' (chk: {chk})")
    else:
        print('Dialog is closed. Main page content preview:')
        print(page.locator('body').inner_text()[:600])
