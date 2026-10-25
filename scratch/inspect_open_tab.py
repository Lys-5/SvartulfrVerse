import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws_endpoint = f'ws://127.0.0.1:{port}{ws_path}'

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    tab = None
    for pg in context.pages:
        if 'lorebooks/edit' in pg.url:
            tab = pg
            break
    if tab:
        print('Found lorebook edit tab:', tab.url)
        eval_script = """() => {
            const text = document.body.innerText;
            const hasUnknownSource = text.includes('Unknown source');
            const hasCustomImage = text.includes('Custom Image');
            
            // Find gallery elements or buttons
            const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim()).filter(Boolean);
            
            // Look for any input or select
            const selects = Array.from(document.querySelectorAll('[role="dialog"] button, [role="tab"]')).map(el => el.innerText.trim());
            
            return {
                hasUnknownSource,
                hasCustomImage,
                buttons: buttons.slice(0, 30),
                dialogOrTabs: selects
            };
        }"""
        info = tab.evaluate(eval_script)
        print('Tab info:', json.dumps(info, indent=2))
    else:
        print('Tab not found')
