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
        function findReactRoot(el) {
            for (const key in el) {
                if (key.startsWith('__reactContainer$') || key.startsWith('__reactFiber$')) {
                    return el[key];
                }
            }
            return null;
        }
        let fiber = findReactRoot(document.getElementById('__next') || document.body);
        let qClient = null;
        function walk(node, depth = 0) {
            if (!node || depth > 200 || qClient) return;
            if (node.memoizedProps?.client?.getQueryCache) {
                qClient = node.memoizedProps.client;
                return;
            }
            if (node.memoizedState?.element?.props?.client?.getQueryCache) {
                qClient = node.memoizedState.element.props.client;
                return;
            }
            let child = node.child;
            while (child) {
                walk(child, depth + 1);
                child = child.sibling;
            }
        }
        walk(fiber);
        
        const cache = qClient.getQueryCache().getAll();
        const customProviders = cache.find(q => JSON.stringify(q.queryKey) === JSON.stringify(["providers", "custom"]))?.state.data;
        const userConnections = cache.find(q => q.queryKey[0] === "connections" && q.queryKey[1] === "user")?.state.data;
        const apiKeys = cache.find(q => q.queryKey[0] === "user-api-keys" || q.queryKey[0] === "api-keys")?.state.data;
        
        return {
            customProviders,
            userConnections,
            apiKeys
        };
    }"""
    data = page.evaluate(js)
    with open("navy_glm_config_dump.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Dump written to navy_glm_config_dump.json")
