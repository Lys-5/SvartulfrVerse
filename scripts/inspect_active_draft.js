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
          const h2 = document.querySelector('h2');
          let fiber = h2[Object.keys(h2).find(k => k.startsWith('__reactFiber$'))];
          while (fiber && !(fiber.memoizedProps && fiber.memoizedProps.worldId)) {
            fiber = fiber.return;
          }
          
          let stateHook = fiber.memoizedState;
          let draftState = null;
          while (stateHook) {
            if (stateHook.memoizedState && typeof stateHook.memoizedState === 'object' && 'worldIntro' in stateHook.memoizedState) {
              draftState = stateHook.memoizedState;
              break;
            }
            stateHook = stateHook.next;
          }
          
          return {
            mode: fiber.memoizedProps.mode,
            initialScenarioId: fiber.memoizedProps.initialScenarioId,
            draftState: draftState ? {
              worldIntro: draftState.worldIntro,
              selectedScenarioId: draftState.selectedScenarioId,
              characterMode: draftState.characterMode,
              fieldValues: draftState.fieldValues
            } : null
          };
        } catch(err) {
          return { error: err.message };
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
    console.log('ACTIVE TAB DRAFT STATE:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
