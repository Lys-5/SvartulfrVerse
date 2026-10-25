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
        
        const keyRes = await fetch('/api/api-keys/raw/_WwxWntJxMzFWfQ4RYghQN', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const keyData = await keyRes.json();
        const apiKey = keyData.apiKey;
        
        try {
            const modelsRes = await fetch('https://api.navy/v1/models', {
                headers: {
                    'Authorization': `Bearer ${apiKey}`
                }
            });
            const text = await modelsRes.text();
            let json = null;
            try { json = JSON.parse(text); } catch {}
            return {
                status: modelsRes.status,
                isJson: !!json,
                data: json || text.slice(0, 500)
            };
        } catch (err) {
            return { error: err.message };
        }
    }"""
    res = page.evaluate(js)
    if 'data' in res and isinstance(res['data'], dict) and 'data' in res['data']:
        models = [m.get('id') for m in res['data']['data']]
        print(f"Total models returned from https://api.navy/v1/models: {len(models)}")
        glm_models = [m for m in models if 'glm' in m.lower()]
        print("GLM models:", glm_models)
        print("First 20 models:", models[:20])
    else:
        print("Response:", res)
