const fs = require('fs');

const devToolsActivePort = fs.readFileSync('C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort', 'utf8').split('\n');
const port = devToolsActivePort[0].trim();
const browserPath = devToolsActivePort[1].trim();
const wsUrl = `ws://127.0.0.1:${port}${browserPath}`;

const ws = new WebSocket(wsUrl);

ws.addEventListener('open', () => {
  ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
});

ws.addEventListener('message', async (e) => {
  const msg = JSON.parse(e.data);
  if (msg.id === 1) {
    const target = msg.result.targetInfos.find(x => x.type === 'page' && x.url && x.url.includes('chat_log_qUdWrgx232YGtwDE2318a'));
    ws.send(JSON.stringify({
      id: 2,
      method: 'Target.attachToTarget',
      params: { targetId: target.targetId, flatten: true }
    }));
  } else if (msg.id === 2) {
    const sessionId = msg.result.sessionId;

    const expr = `
      (() => {
        try {
          const dialog = document.querySelector('[role="dialog"]');
          if (!dialog) return { error: "No dialog" };

          // Look for react form or state on form element
          const form = dialog.querySelector('form');
          const el = form || dialog;
          const key = Object.keys(el).find(k => k.startsWith('__reactFiber$'));
          let fiber = el[key];

          const propsList = [];
          while (fiber && propsList.length < 20) {
            if (fiber.memoizedProps) {
              const p = fiber.memoizedProps;
              const keys = Object.keys(p).filter(k => k !== 'children');
              if (keys.length > 0) {
                propsList.push({
                  name: fiber.type ? (typeof fiber.type === 'string' ? fiber.type : (fiber.type.displayName || fiber.type.name || 'Component')) : 'Unknown',
                  keys: keys.slice(0, 20)
                });
              }
            }
            fiber = fiber.return;
          }

          return { propsList };
        } catch (err) {
          return { error: err.message, stack: err.stack };
        }
      })()
    `;

    ws.send(JSON.stringify({
      id: 3,
      sessionId,
      method: 'Runtime.evaluate',
      params: { expression: expr, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 3) {
    if (msg.error) {
      console.error('CDP Error:', msg.error);
    } else {
      console.log('Result:', JSON.stringify(msg.result?.result?.value, null, 2));
    }
    ws.close();
    process.exit(0);
  }
});
