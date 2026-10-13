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
        // Let's inspect __apiErrors or console errors stored in window
        const apiErrors = window.__apiErrors || [];
        // Let's inspect what createWorldChatLog sent
        return {
          apiErrorsCount: apiErrors.length,
          lastApiErrors: apiErrors.slice(-3),
          currentUrl: window.location.href
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
    console.log('API ERRORS:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
