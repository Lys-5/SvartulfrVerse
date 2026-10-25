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
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return { error: "No dialog" };

        const forms = Array.from(dialog.querySelectorAll('form'));
        const buttons = Array.from(dialog.querySelectorAll('button')).filter(b => b.innerText && (b.innerText.includes('Save') || b.innerText.includes('Close') || b.innerText.includes('Cancel')));

        return {
          formCount: forms.length,
          buttons: buttons.map(b => ({
            text: b.innerText.trim(),
            type: b.type,
            className: b.className,
            disabled: b.disabled
          }))
        };
      })()
    `;

    ws.send(JSON.stringify({
      id: 3,
      sessionId,
      method: 'Runtime.evaluate',
      params: { expression: expr, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 3) {
    console.log('Save buttons detail:');
    console.log(JSON.stringify(msg.result.result.value, null, 2));
    ws.close();
    process.exit(0);
  }
});
