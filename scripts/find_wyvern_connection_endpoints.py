import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

# Let's inspect webpack modules for provider creation endpoint
# Or check the forms in the open modal!
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # Check what is currently open on page
    dialog_open = page.locator('[role="dialog"]').is_visible()
    print("Dialog is open:", dialog_open)
    
    # Let's get the token
    js = """async () => {
        const token = await new Promise((resolve) => {
            const req = indexedDB.open('firebaseLocalStorageDb');
            req.onsuccess = () => {
                const db = req.result;
                const tx = db.transaction('firebaseLocalStorage', 'readonly');
                const store = tx.objectStore('firebaseLocalStorage');
                const get = store.getAll();
                get.onsuccess = () => {
                    for (const item of get.result) {
                        if (item.value && item.value.stsTokenManager) {
                            resolve(item.value.stsTokenManager.accessToken);
                            return;
                        }
                    }
                    resolve(null);
                };
            };
            req.onerror = () => resolve(null);
        });

        // Search for endpoints in webpack
        let endpoints = [];
        if (window.webpackChunk_N_E) {
            window.webpackChunk_N_E.forEach(chunk => {
                const modules = chunk[1];
                for (const key in modules) {
                    const str = modules[key].toString();
                    if (str.includes('/providers') || str.includes('/connections')) {
                        const matches = str.match(/["'`](\/api\/[^"'`]+)["'`]/g);
                        if (matches) endpoints.push(...matches);
                    }
                }
            });
        }
        
        return {
            endpoints: Array.from(new Set(endpoints)).slice(0, 30)
        };
    }"""
    print(page.evaluate(js))
