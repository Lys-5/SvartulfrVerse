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
    
    sections = page.evaluate("""() => {
        const d = document.querySelector('[role="dialog"]');
        if (!d) return [];
        
        // Find all accordion buttons or section headings
        const buttons = Array.from(d.querySelectorAll('button'));
        return buttons.map(b => {
            const text = b.innerText.trim();
            const ariaExpanded = b.getAttribute('aria-expanded');
            return { text, ariaExpanded };
        }).filter(b => b.text.length > 0 && b.text.length < 50);
    }""")
    print("Section Accordions:")
    for s in sections:
        print(f"  - '{s['text']}' (expanded: {s['ariaExpanded']})")
