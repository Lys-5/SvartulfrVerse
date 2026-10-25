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
        // Let's check window or React root
        const token = await (async () => {
            return new Promise((resolve) => {
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
        })();

        // Let's test endpoints
        const endpoints = [
            '/api/users/me',
            '/api/user-connections',
            '/api/user/connections',
            '/api/connections',
            '/api/custom-providers',
            '/api/user/providers',
            '/api/providers'
        ];
        
        const results = {};
        for (const ep of endpoints) {
            try {
                const res = await fetch(ep, {
                    headers: token ? { 'Authorization': `Bearer ${token}` } : {}
                });
                results[ep] = {
                    status: res.status,
                    body: res.status === 200 ? await res.json() : await res.text()
                };
            } catch (e) {
                results[ep] = { error: e.message };
            }
        }
        return results;
    }"""
    print(json.dumps(page.evaluate(js), indent=2))
