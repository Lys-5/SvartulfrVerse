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
    
    sections_dump = page.evaluate("""() => {
        const d = document.querySelector('[role="dialog"]');
        if (!d) return {};
        
        // Let's get the text and input values of:
        // 1. Your Saved World System Prompt
        // 2. Final Instructions
        // 3. Easy Parameters
        // 4. Length Limits
        // 5. Template Override
        // 6. Parameter Preset Override
        
        const textareas = Array.from(d.querySelectorAll('textarea')).map(t => ({
            id: t.id,
            placeholder: t.placeholder,
            value: t.value.slice(0, 300)
        }));
        
        return {
            textareas
        };
    }""")
    print("Textareas:")
    for ta in sections_dump.get('textareas', []):
        print(f"  - id: {ta['id']} | placeholder: '{ta['placeholder']}' | val[:100]: '{ta['value'][:100]}'")
