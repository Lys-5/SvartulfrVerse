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
        
        // Test chat completion on https://api.navy/v1/chat/completions
        const t0 = performance.now();
        const chatRes = await fetch('https://api.navy/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'glm-5.3',
                messages: [
                    { role: 'user', content: 'Rispondi con una sola parola di test: OK' }
                ],
                max_tokens: 20,
                temperature: 0.7
            })
        });
        const t1 = performance.now();
        const text = await chatRes.text();
        return {
            status: chatRes.status,
            latencyMs: Math.round(t1 - t0),
            response: text.slice(0, 1000)
        };
    }"""
    res = page.evaluate(js)
    print(json.dumps(res, indent=2))
