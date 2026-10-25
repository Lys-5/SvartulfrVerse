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
    const targets = msg.result.targetInfos.filter(x => x.type === 'page' && x.url && x.url.includes('chat_log_qUdWrgx232YGtwDE2318a'));
    if (targets.length === 0) {
      console.error('Target not found among:', msg.result.targetInfos.map(x => ({ type: x.type, url: x.url })));
      process.exit(1);
    }
    const target = targets[0];
    console.log('Found target:', target.targetId, target.url);
    ws.send(JSON.stringify({
      id: 2,
      method: 'Target.attachToTarget',
      params: { targetId: target.targetId, flatten: true }
    }));
  } else if (msg.id === 2) {
    const sessionId = msg.result.sessionId;
    console.log('Attached with sessionId:', sessionId);

    // Let's inspect the page
    const expr = `
      (() => {
        try {
          return {
            title: document.title,
            url: window.location.href,
            buttons: Array.from(document.querySelectorAll('button')).map(b => ({
              text: b.innerText.trim(),
              ariaLabel: b.getAttribute('aria-label'),
              title: b.getAttribute('title'),
              className: b.className
            })).filter(b => b.text || b.ariaLabel || b.title).slice(0, 50),
            // Check local state or open dialogs
            modals: Array.from(document.querySelectorAll('[role="dialog"], [role="menu"], div[class*="modal"], div[class*="drawer"]')).map(m => m.innerText.slice(0, 200))
          };
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
    console.log('Result:');
    console.log(JSON.stringify(msg.result.result.value, null, 2));
    ws.close();
    process.exit(0);
  }
});
