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

        // Find all accordion triggers
        const triggers = Array.from(dialog.querySelectorAll('[data-radix-collection-item], button[data-state]')).map(b => ({
          text: b.innerText.trim().replace(/\\s+/g, ' '),
          state: b.getAttribute('data-state'),
          ariaControls: b.getAttribute('aria-controls'),
          ariaExpanded: b.getAttribute('aria-expanded')
        }));

        // Let's find all elements with id containing 'narrator' or 'assembly' or 'prompt'
        const specific = Array.from(dialog.querySelectorAll('[id*="narrator"], [id*="prompt"], [id*="assembly"], [id*="advanced"]')).map(el => ({
          tag: el.tagName,
          id: el.id,
          role: el.getAttribute('role'),
          text: el.innerText ? el.innerText.slice(0, 100) : '',
          dataState: el.getAttribute('data-state')
        }));

        return {
          triggers,
          specific
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
    console.log('Accordion Inspection:');
    console.log(JSON.stringify(msg.result.result.value, null, 2));
    ws.close();
    process.exit(0);
  }
});
