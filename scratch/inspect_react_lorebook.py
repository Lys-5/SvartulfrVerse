import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws_endpoint = f'ws://127.0.0.1:{port}{ws_path}'

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    tab = [pg for pg in browser.contexts[0].pages if 'lorebooks/edit' in pg.url][0]
    
    # Inspect React Fiber
    script = """() => {
        function findReactFiber(el) {
            for (const key in el) {
                if (key.startsWith('__reactFiber$') || key.startsWith('__reactInternalInstance$')) {
                    return el[key];
                }
            }
            return null;
        }
        
        let root = document.querySelector('#__next') || document.body;
        let fiber = findReactFiber(root);
        
        // Traverse to find component state holding lorebook data
        let curr = fiber;
        let foundData = null;
        while (curr) {
            if (curr.memoizedState || curr.memoizedProps) {
                const props = curr.memoizedProps;
                if (props && (props.lorebook || props.initialLorebook || props.entries)) {
                    foundData = {
                        lorebookKeys: Object.keys(props.lorebook || props.initialLorebook || {}),
                        gallery: (props.lorebook || props.initialLorebook || {}).gallery,
                        gallery_count: (props.lorebook || props.initialLorebook || {}).gallery_count
                    };
                    break;
                }
            }
            curr = curr.child;
        }
        return foundData;
    }"""
    res = tab.evaluate(script)
    print('React Lorebook state:', json.dumps(res, indent=2))
