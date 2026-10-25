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
        const items = [];
        document.querySelectorAll('button, a, [role="button"], span, div').forEach(el => {
            const text = (el.innerText || el.getAttribute('aria-label') || el.title || '').trim();
            if (text && text.length < 60) {
                const lower = text.toLowerCase();
                if (['ai', 'connect', 'setting', 'model', 'provider', 'navy', 'glm'].some(k => lower.includes(k))) {
                    items.push({ tag: el.tagName, text: text, href: el.getAttribute('href') });
                }
            }
        });
        return items;
    }"""
    elements = page.evaluate(js)
    # Deduplicate by text
    seen = set()
    for el in elements:
        if el['text'] not in seen:
            seen.add(el['text'])
            print(el)
