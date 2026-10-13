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
      (() => {
        // Let's inspect React Query cache for personas
        // In React Query, queryCache has all cached queries
        const root = document.querySelector('#__next') || document.body;
        const key = Object.keys(root).find(k => k.startsWith('__reactFiber$'));
        let f = root[key];
        let qc = null;
        while (f) {
          if (f.memoizedProps && f.memoizedProps.client && f.memoizedProps.client.getQueryCache) {
            qc = f.memoizedProps.client.getQueryCache();
            break;
          }
          f = f.return;
        }
        
        let queries = [];
        if (qc) {
          queries = qc.getAll().map(q => ({
            queryKey: q.queryKey,
            dataSummary: Array.isArray(q.state.data) ? ('array of ' + q.state.data.length) : typeof q.state.data,
            data: q.queryKey.some(k => String(k).includes('persona')) ? q.state.data : undefined
          }));
        }

        return {
          queries
        };
      })()
    `;
    ws.send(JSON.stringify({
      id: 3,
      sessionId: msg.result.sessionId,
      method: 'Runtime.evaluate',
      params: { expression: code, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 3) {
    console.log('QUERY CACHE RESULT:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
