const fs = require('fs');
const path = require('path');
const activePortFile = path.join(process.env.LOCALAPPDATA, 'Google\\Chrome\\User Data\\DevToolsActivePort');
const [port, browserPath] = fs.readFileSync(activePortFile, 'utf8').trim().split('\n');
const wsUrl = 'ws://127.0.0.1:' + port.trim() + browserPath.trim();
const ws = new WebSocket(wsUrl);

ws.addEventListener('open', () => {
  ws.send(JSON.stringify({
    id: 1,
    method: 'Target.attachToTarget',
    params: { targetId: '59C3AB195CC2269792EE0D228F070693', flatten: true }
  }));
});

ws.addEventListener('message', (e) => {
  const msg = JSON.parse(e.data);
  if (msg.id === 1 && msg.result) {
    const sessionId = msg.result.sessionId;
    const expr = `(() => {
      const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText && b.innerText.includes('Offer a persona to play as'));
      if (btn) {
        btn.click();
        return new Promise(res => {
          setTimeout(() => {
            const panel = document.getElementById(btn.getAttribute('aria-controls'));
            res({
              clicked: true,
              panelHtml: panel ? panel.innerHTML : null,
              panelText: panel ? panel.innerText : null
            });
          }, 500);
        });
      }
      return { clicked: false };
    })()`;
    ws.send(JSON.stringify({
      id: 2,
      sessionId: sessionId,
      method: 'Runtime.evaluate',
      params: { expression: expr, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 2) {
    console.log(JSON.stringify(msg.result.result.value, null, 2));
    ws.close();
    process.exit(0);
  }
});
