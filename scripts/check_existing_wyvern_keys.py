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
        
        const providers = ['gemini', 'openrouter', 'navyai', '_WwxWntJxMzFWfQ4RYghQN'];
        const res = {};
        for (const p of providers) {
            try {
                const r = await fetch(`/api/api-keys/raw/${p}`, {
                    headers: { 'Authorization': `Bearer ${token}` }
                });
                const d = await r.json();
                res[p] = {
                    status: r.status,
                    success: d.success,
                    hasKey: !!d.apiKey,
                    keyPrefix: d.apiKey ? d.apiKey.slice(0, 8) + '...' : null
                };
            } catch (e) {
                res[p] = { error: e.message };
            }
        }
        return res;
    }"""
    print(json.dumps(page.evaluate(js), indent=2))
