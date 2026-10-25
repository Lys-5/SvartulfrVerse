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
        const dbs = await window.indexedDB.databases();
        const allData = {};
        for (const dbInfo of dbs) {
            allData[dbInfo.name] = await new Promise((resolve) => {
                const req = indexedDB.open(dbInfo.name);
                req.onerror = () => resolve({ error: req.error?.message });
                req.onsuccess = () => {
                    const db = req.result;
                    const storeNames = Array.from(db.objectStoreNames);
                    const tx = db.transaction(storeNames, 'readonly');
                    const dbRes = {};
                    let pending = storeNames.length;
                    if (pending === 0) resolve(dbRes);
                    for (const s of storeNames) {
                        const store = tx.objectStore(s);
                        const getAll = store.getAll();
                        const getKeys = store.getAllKeys();
                        getAll.onsuccess = () => {
                            getKeys.onsuccess = () => {
                                dbRes[s] = getKeys.result.map((k, i) => ({ key: k, value: getAll.result[i] }));
                                pending--;
                                if (pending === 0) resolve(dbRes);
                            };
                        };
                        getAll.onerror = () => {
                            pending--;
                            if (pending === 0) resolve(dbRes);
                        };
                    }
                };
            });
        }
        return allData;
    }"""
    data = page.evaluate(js)
    # Print summary without huge values
    for db_name, stores in data.items():
        print(f"DB: {db_name}")
        for s_name, records in stores.items():
            print(f"  Store: {s_name} ({len(records)} items)")
            for r in records:
                k = r['key']
                val_str = str(r['value'])
                if 'navy' in val_str.lower() or 'glm' in val_str.lower() or 'provider' in val_str.lower():
                    print(f"    MATCH key={k}: {val_str[:300]}")
                else:
                    print(f"    key={k}: {val_str[:100]}")
