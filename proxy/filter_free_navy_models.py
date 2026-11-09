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
        
        const modelsRes = await fetch('https://api.navy/v1/models', {
            headers: { 'Authorization': `Bearer ${apiKey}` }
        });
        const json = await modelsRes.json();
        
        // Find all models where is_free or pricing is 0 or metadata says free
        const freeModels = json.data.filter(m => {
            const isZeroPrompt = m.pricing?.prompt === '0' || m.pricing?.prompt === 0;
            const isZeroComp = m.pricing?.completion === '0' || m.pricing?.completion === 0;
            return m.is_free || m.free || m.premium === false && (isZeroPrompt && isZeroComp) || m.id.includes('free');
        });
        
        return {
            total: json.data.length,
            freeCount: freeModels.length,
            freeModels: freeModels.map(m => ({
                id: m.id,
                owned_by: m.owned_by,
                endpoint: m.endpoint,
                pricing: m.pricing,
                context_window: m.context_window,
                max_output_tokens: m.max_output_tokens
            })),
            sampleModelsWithPricing: json.data.slice(0, 10).map(m => ({ id: m.id, pricing: m.pricing, premium: m.premium, free: m.is_free }))
        };
    }"""
    res = page.evaluate(js)
    print(json.dumps(res, indent=2))
