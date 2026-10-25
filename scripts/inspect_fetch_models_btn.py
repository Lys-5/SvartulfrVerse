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
        function getReactFiber(el) {
            const key = Object.keys(el).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
            return key ? el[key] : null;
        }
        
        const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Fetch Models'));
        if (!btn) return { error: 'Fetch Models button not found' };
        
        const fiber = getReactFiber(btn);
        let curr = fiber;
        let onClickCode = null;
        while (curr) {
            if (curr.memoizedProps?.onClick) {
                onClickCode = curr.memoizedProps.onClick.toString();
                break;
            }
            curr = curr.return;
        }
        return {
            buttonFound: true,
            onClick: onClickCode
        };
    }"""
    print(page.evaluate(js))
