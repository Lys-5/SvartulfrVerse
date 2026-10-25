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
        // Search all strings in webpack chunks for 'connections' and 'providers'
        const results = [];
        if (window.webpackChunk_N_E) {
            window.webpackChunk_N_E.forEach(chunk => {
                const modules = chunk[1];
                for (const k in modules) {
                    const src = modules[k].toString();
                    // look for fetch or axios or api calls
                    const m = src.match(/(?:post|put|patch|delete|get)\s*\(\s*["'`](\/api\/[^"'`]+)["'`]/gi);
                    if (m) results.push(...m);
                }
            });
        }
        return Array.from(new Set(results));
    }"""
    print(json.dumps(page.evaluate(js), indent=2))
