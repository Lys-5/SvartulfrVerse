const fs = require('fs');

process.on('uncaughtException', (err) => console.error('Uncaught:', err));
process.on('unhandledRejection', (err) => console.error('Unhandled:', err));

const devToolsActivePort = fs.readFileSync('C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort', 'utf8').split('\n');
const port = devToolsActivePort[0].trim();
const browserPath = devToolsActivePort[1].trim();
const wsUrl = `ws://127.0.0.1:${port}${browserPath}`;

console.log('Connecting...');
const ws = new WebSocket(wsUrl);

ws.addEventListener('open', () => {
  console.log('Connected, getting targets...');
  ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
});

ws.addEventListener('error', (err) => {
  console.error('WS Error:', err);
});

ws.addEventListener('message', async (e) => {
  try {
    const msg = JSON.parse(e.data);
    if (msg.id === 1) {
      const target = msg.result.targetInfos.find(x => x.type === 'page' && x.url && x.url.includes('chat_log_qUdWrgx232YGtwDE2318a'));
      if (!target) {
        console.error('Target not found!');
        process.exit(1);
      }
      console.log('Target found:', target.targetId);
      ws.send(JSON.stringify({
        id: 2,
        method: 'Target.attachToTarget',
        params: { targetId: target.targetId, flatten: true }
      }));
    } else if (msg.id === 2) {
      const sessionId = msg.result.sessionId;
      console.log('Attached, sessionId:', sessionId);

      const expr = `
        (() => {
          const dialog = document.querySelector('[role="dialog"]');
          if (!dialog) return { error: "No dialog found" };

          return {
            dialogText: dialog.innerText,
            tabs: Array.from(dialog.querySelectorAll('button[role="tab"], [data-state]')).map(b => ({
              text: b.innerText.trim(),
              role: b.getAttribute('role'),
              dataState: b.getAttribute('data-state')
            })),
            activeTab: document.querySelector('[role="tab"][data-state="active"]')?.innerText
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
      console.log('DIALOG RESULT:');
      console.log(JSON.stringify(msg.result.result.value, null, 2));
      ws.close();
      process.exit(0);
    }
  } catch (err) {
    console.error('Handler error:', err);
    process.exit(1);
  }
});
