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
        
        // Let's test a few models: glm-5.3-flash, glm-5-venice, glm-4.7-flash-heretic, schizogpt
        const candidates = ['glm-5.3', 'glm-5.3-flash', 'glm-5-venice', 'glm-4.7-flash-heretic', 'schizogpt'];
        const results = {};
        for (const m of candidates) {
            try {
                const chatRes = await fetch('https://api.navy/v1/chat/completions', {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${apiKey}`,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        model: m,
                        messages: [{ role: 'user', content: 'Ping' }],
                        max_tokens: 10
                    })
                });
                results[m] = {
                    status: chatRes.status,
                    body: await chatRes.json()
                };
            } catch (e) {
                results[m] = { error: e.message };
            }
        }
        return results;
    }"""
    res = page.evaluate(js)
    print(json.dumps(res, indent=2))
