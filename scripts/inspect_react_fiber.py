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
    
    js = """async () => {
        // Let's inspect React Fiber on the modal or provider element
        function getReactFiber(el) {
            const key = Object.keys(el).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
            return key ? el[key] : null;
        }
        
        // Find all buttons or inputs in the dialog
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return { error: 'No dialog found' };
        
        // Let's traverse fiber up to find state or hooks
        let fiber = getReactFiber(dialog);
        const states = [];
        let curr = fiber;
        while (curr) {
            if (curr.memoizedState) {
                // inspect memoizedState chain
                let s = curr.memoizedState;
                while (s) {
                    if (s.memoizedState && typeof s.memoizedState === 'object') {
                        const str = JSON.stringify(s.memoizedState);
                        if (str && (str.includes('Navy') || str.includes('glm') || str.includes('provider') || str.includes('connection'))) {
                            states.push({
                                comp: curr.type?.name || curr.type?.displayName || 'Unknown',
                                state: s.memoizedState
                            });
                        }
                    }
                    s = s.next;
                }
            }
            if (curr.memoizedProps) {
                const str = JSON.stringify(curr.memoizedProps);
                if (str && (str.includes('Navy') || str.includes('glm'))) {
                    states.push({
                        comp: curr.type?.name || curr.type?.displayName || 'UnknownProps',
                        props: curr.memoizedProps
                    });
                }
            }
            curr = curr.return;
        }
        
        return states;
    }"""
    res = page.evaluate(js)
    print(json.dumps(res, indent=2)[:3000])
