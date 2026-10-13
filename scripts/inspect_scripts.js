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
      (async () => {
        // Let's search inside all script tags loaded on this page
        const scripts = Array.from(document.querySelectorAll('script[src]')).map(s => s.src);
        const results = [];
        for (const s of scripts) {
          try {
            const res = await fetch(s);
            const text = await res.text();
            if (text.includes('introduction_pages') || text.includes('intro_fields') || text.includes('custom_introduction')) {
              results.push({
                src: s,
                hasPages: text.includes('introduction_pages'),
                hasFields: text.includes('intro_fields'),
                hasCustom: text.includes('custom_introduction')
              });
              // Find matches
              let idx = text.indexOf('introduction_pages');
              if (idx !== -1) {
                results.push({
                  snippetPages: text.slice(Math.max(0, idx - 200), Math.min(text.length, idx + 400))
                });
              }
              let idx2 = text.indexOf('intro_fields');
              if (idx2 !== -1) {
                results.push({
                  snippetFields: text.slice(Math.max(0, idx2 - 200), Math.min(text.length, idx2 + 400))
                });
              }
            }
          } catch(err) {}
        }
        return { totalScripts: scripts.length, results };
      })()
    `;
    ws.send(JSON.stringify({
      id: 3,
      sessionId: msg.result.sessionId,
      method: 'Runtime.evaluate',
      params: { expression: code, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 3) {
    console.log('BROWSER SEARCH RESULT:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
