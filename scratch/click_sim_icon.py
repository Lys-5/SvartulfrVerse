import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # Click on Simulation icon button at (1341, 131)
    page.mouse.click(1341, 131)
    page.wait_for_timeout(600)
    
    sim_content = page.evaluate("""() => {
        const aside = document.querySelector('div.border-l') || document.querySelector('aside');
        if (!aside) return 'None';
        
        // Find all buttons inside aside
        const btns = Array.from(aside.querySelectorAll('button')).map(b => b.innerText.trim());
        return {
            btns,
            text: aside.innerText
        };
    }""")
    print("Simulation Buttons:", sim_content.get('btns'))
    print("=== SIMULATION TEXT ===")
    print(sim_content.get('text')[:2500])
