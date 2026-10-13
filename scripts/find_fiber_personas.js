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
        // Let's find where personas list is in the React tree of the wizard
        const allButtons = Array.from(document.querySelectorAll('button'));
        // Find persona selector or character selector fiber
        let foundPersonas = [];
        for (const b of allButtons) {
          const k = Object.keys(b).find(k => k.startsWith('__reactFiber$'));
          if (!k) continue;
          let fib = b[k];
          while (fib) {
            if (fib.memoizedProps) {
              const p = fib.memoizedProps;
              if (p.personas) foundPersonas = p.personas;
              if (p.personaList) foundPersonas = p.personaList;
              if (p.currentPersonas) foundPersonas = p.currentPersonas;
            }
            if (foundPersonas.length > 0) break;
            fib = fib.return;
          }
          if (foundPersonas.length > 0) break;
        }

        return {
          foundPersonas: foundPersonas.map(p => ({
            id: p.id,
            _id: p._id,
            name: p.name || p.displayName,
            keys: Object.keys(p)
          }))
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
    console.log('PERSONAS RESULT:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
