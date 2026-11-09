import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    context = browser.contexts[0]
    navy_page = [pg for pg in context.pages if 'navy' in pg.url][0]
    
    js = """() => {
        // Find all cards or elements in model directory
        const cards = [];
        // Look for model cards
        document.querySelectorAll('div, a').forEach(el => {
            const text = el.innerText || '';
            const lines = text.split('\\n').map(l => l.trim()).filter(Boolean);
            if (lines.includes('Free') && lines.includes('Chat') && lines.length <= 8 && lines.length >= 3) {
                cards.push({
                    modelId: lines[0],
                    provider: lines[1],
                    multiplier: lines[2],
                    fullText: lines.join(' | ')
                });
            }
        });
        
        // Deduplicate by modelId
        const unique = [];
        const seen = new Set();
        for (const c of cards) {
            if (!seen.has(c.modelId)) {
                seen.add(c.modelId);
                unique.push(c);
            }
        }
        return unique;
    }"""
    models = navy_page.evaluate(js)
    print(f"Total Chat+Free models found: {len(models)}")
    for m in models:
        print(m['fullText'])
