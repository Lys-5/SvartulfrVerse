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
    
    # Check if modal is still open, if so click Close
    dialog = page.locator('[role="dialog"]')
    if dialog.count() > 0 and dialog.first.is_visible():
        close_btn = dialog.locator('button:has-text("Close")')
        if close_btn.count() > 0 and close_btn.first.is_visible():
            close_btn.first.click()
            page.wait_for_timeout(500)
    
    # Inspect right sidebar: aside or right-aligned containers / panels
    sidebar_info = page.evaluate("""() => {
        // Look for aside, sidebar, or right-side panels
        const asides = Array.from(document.querySelectorAll('aside, [data-panel-group-id], div[class*="sidebar"], div[class*="drawer"]'));
        
        // Also look for buttons on the right side of the header/navbar that toggle panels
        const rightButtons = Array.from(document.querySelectorAll('header button, div.flex button')).map(b => ({
            text: b.innerText.trim(),
            ariaLabel: b.getAttribute('aria-label'),
            title: b.getAttribute('title')
        })).filter(b => b.text || b.ariaLabel || b.title);
        
        // Find visible right panel text
        const rightPanel = document.querySelector('aside') || document.querySelector('[data-panel-id]') || document.querySelector('div[class*="right"]');
        
        return {
            url: window.location.href,
            rightPanelText: rightPanel ? rightPanel.innerText : null,
            rightButtons
        };
    }""")
    print("Page URL:", sidebar_info.get('url'))
    print("Right Panel Preview:\n", (sidebar_info.get('rightPanelText') or '')[:800])
