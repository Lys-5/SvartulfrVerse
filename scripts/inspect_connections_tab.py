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
    
    # Let's inspect React state / query client cache!
    # TanStack Query / React Query is commonly used in Next.js/Wyvern!
    js = """() => {
        // Let's look for React Query Cache or SWR or similar
        const queryClient = window.__REACT_QUERY_CACHE__ || 
            (window.queryClient ? window.queryClient.getQueryCache() : null);
            
        // Look for any global stores or search React fiber for connection list
        const results = {};
        
        // Let's find all buttons with text 'Connections'
        const connBtns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === 'Connections');
        results.connButtonsCount = connBtns.length;
        
        // Let's inspect localStorage and IndexedDB once more or window globals
        return results;
    }"""
    print(page.evaluate(js))
