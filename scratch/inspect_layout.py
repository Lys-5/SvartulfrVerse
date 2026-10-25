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
    
    # Let's inspect the entire DOM layout of the simulation page
    layout = page.evaluate("""() => {
        // Find all buttons, tabs, panels
        const allButtons = Array.from(document.querySelectorAll('button')).map(b => ({
            text: b.innerText.trim(),
            ariaLabel: b.getAttribute('aria-label'),
            title: b.getAttribute('title'),
            ariaSelected: b.getAttribute('aria-selected'),
            role: b.getAttribute('role'),
            classes: b.className
        })).filter(b => b.text || b.ariaLabel || b.title);
        
        // Find all elements that look like sidebars or panels on the right (bounding rect with x > window.innerWidth / 2)
        const rightElements = Array.from(document.querySelectorAll('div, aside, section')).filter(el => {
            const rect = el.getBoundingClientRect();
            return rect.width > 200 && rect.right > window.innerWidth * 0.7 && rect.height > 300;
        }).map(el => ({
            tag: el.tagName,
            classes: el.className,
            textSnippet: el.innerText.slice(0, 300)
        }));
        
        return {
            windowWidth: window.innerWidth,
            rightElements,
            buttons: allButtons.slice(0, 30)
        };
    }""")
    print("Window width:", layout['windowWidth'])
    print("\nRight Elements count:", len(layout['rightElements']))
    for re in layout['rightElements'][:5]:
        print(f"Tag: {re['tag']} | Classes: {re['classes'][:50]} | Text:\n{re['textSnippet'][:200]}\n" + "-"*40)
        
    print("\nButtons snippet:")
    for b in layout['buttons'][:20]:
        print(f"Button: text='{b['text']}' | label='{b['ariaLabel']}' | title='{b['title']}' | role='{b['role']}'")
