const fs = require('fs');

function getCdpWs() {
  const devToolsActivePort = fs.readFileSync('C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort', 'utf8').split('\n');
  const port = devToolsActivePort[0].trim();
  const browserPath = devToolsActivePort[1].trim();
  return new WebSocket(`ws://127.0.0.1:${port}${browserPath}`);
}

async function inspectWyvernDom() {
  const ws = getCdpWs();
  let sessionId = null;

  ws.addEventListener('open', () => {
    ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
  });

  ws.addEventListener('message', async (e) => {
    const msg = JSON.parse(e.data);
    if (msg.id === 1) {
      const targets = msg.result.targetInfos.filter(x => x.url && x.url.includes('app.wyvern.chat'));
      console.log('Wyvern targets:', targets.map(t => ({ id: t.targetId, url: t.url, title: t.title })));
      // Find the one that is active or /sim or /world
      const t = targets.find(x => x.url.includes('sim') || x.url.includes('chat') || x.url.includes('world')) || targets[0];
      if (!t) {
        console.error('No Wyvern tab found');
        ws.close();
        return;
      }
      ws.send(JSON.stringify({
        id: 2,
        method: 'Target.attachToTarget',
        params: { targetId: t.targetId, flatten: true }
      }));
    } else if (msg.id === 2) {
      sessionId = msg.result.sessionId;
      const evalExpr = `
        (() => {
          // Check what URL we are on
          const currentUrl = window.location.href;
          // Inspect the DOM for intro wizard
          const bodyText = document.body.innerText;
          const modalOrContainer = document.querySelector('div[class*="Introduction"], div[class*="wizard"], div[class*="intro"], main, #root');
          
          // Let's inspect React fiber or state on the main element
          const allInputs = Array.from(document.querySelectorAll('input, select, button')).map(el => el.outerHTML);
          
          // Let's find any error in console or window.__NEXT_DATA__
          const nextData = window.__NEXT_DATA__ ? Object.keys(window.__NEXT_DATA__) : null;
          
          // Also let's check localStorage for world or draft
          return {
            currentUrl,
            inputs: allInputs,
            bodySnippet: bodyText.slice(0, 500)
          };
        })()
      `;
      ws.send(JSON.stringify({
        id: 3,
        sessionId,
        method: 'Runtime.evaluate',
        params: { expression: evalExpr, awaitPromise: true, returnByValue: true }
      }));
    } else if (msg.id === 3) {
      console.log('DOM INSPECTION RESULT:\n', JSON.stringify(msg.result.result.value, null, 2));
      ws.close();
    }
  });
}

inspectWyvernDom().catch(console.error);
