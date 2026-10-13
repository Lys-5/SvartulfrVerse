const fs = require('fs');

const devToolsActivePort = fs.readFileSync('C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort', 'utf8').split('\n');
const browserPath = devToolsActivePort[1].trim();

const ws = new WebSocket('ws://127.0.0.1:9222' + browserPath);
ws.onopen = () => ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));

ws.onmessage = async (e) => {
  const msg = JSON.parse(e.data);
  if (msg.id === 1) {
    const t = msg.result.targetInfos.find(x => x.url && x.url.includes('app.wyvern.chat'));
    ws.send(JSON.stringify({
      id: 2,
      method: 'Target.attachToTarget',
      params: { targetId: t.targetId, flatten: true }
    }));
  } else if (msg.id === 2) {
    const code = `
      (async () => {
        const dbs = await indexedDB.databases();
        const results = [];
        for (const dbInfo of dbs) {
          try {
            const db = await new Promise((res, rej) => {
              const req = indexedDB.open(dbInfo.name, dbInfo.version);
              req.onsuccess = () => res(req.result);
              req.onerror = rej;
            });
            for (const storeName of Array.from(db.objectStoreNames)) {
              const items = await new Promise((res) => {
                const tx = db.transaction(storeName, 'readonly');
                const store = tx.objectStore(storeName);
                const r = store.getAll();
                r.onsuccess = () => res(r.result);
                r.onerror = () => res([]);
              });
              for (const it of items) {
                const str = JSON.stringify(it);
                if (str.includes('persona_1786335754946') || str.includes('Alyssa')) {
                  results.push({
                    db: dbInfo.name,
                    store: storeName,
                    itemSnippet: str.slice(0, 300)
                  });
                }
              }
            }
          } catch(e) {}
        }
        return { dbs: dbs.map(d => d.name), results };
      })()
    `;
    ws.send(JSON.stringify({
      id: 3,
      sessionId: msg.result.sessionId,
      method: 'Runtime.evaluate',
      params: { expression: code, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 3) {
    console.log('INDEXEDDB SEARCH:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
