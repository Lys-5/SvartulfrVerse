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
        // Find button 'Playlists'
        const playlistBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Playlists');
        if (playlistBtn) playlistBtn.click();
        
        // Wait a bit and inspect dialog text
        return { clicked: !!playlistBtn };
    }"""
    print(page.evaluate(js))
