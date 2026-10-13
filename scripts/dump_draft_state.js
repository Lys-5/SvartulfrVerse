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
        try {
          // Find l4 component fiber
          const allEl = Array.from(document.querySelectorAll('*'));
          let l4Fiber = null;
          for (const el of allEl) {
            const k = Object.keys(el).find(k => k.startsWith('__reactFiber$'));
            if (!k) continue;
            let f = el[k];
            while (f) {
              if (f.memoizedProps && f.memoizedProps.worldId && f.memoizedProps.mode) {
                l4Fiber = f;
                break;
              }
              f = f.return;
            }
            if (l4Fiber) break;
          }
          
          if (!l4Fiber) return { error: 'l4 not found' };
          
          let hook = l4Fiber.memoizedState;
          let draftState = null;
          while (hook) {
            if (hook.memoizedState && typeof hook.memoizedState === 'object' && 'worldIntro' in hook.memoizedState) {
              draftState = hook.memoizedState;
              break;
            }
            hook = hook.next;
          }
          
          return {
            l4Props: {
              worldId: l4Fiber.memoizedProps.worldId,
              mode: l4Fiber.memoizedProps.mode,
              initialScenarioId: l4Fiber.memoizedProps.initialScenarioId
            },
            draftState
          };
        } catch(err) {
          return { error: err.message, stack: err.stack };
        }
      })()
    `;
    ws.send(JSON.stringify({
      id: 3,
      sessionId: msg.result.sessionId,
      method: 'Runtime.evaluate',
      params: { expression: code, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 3) {
    console.log('DRAFT STATE DUMP:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
