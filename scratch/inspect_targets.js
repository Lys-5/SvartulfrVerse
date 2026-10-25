const fs = require('fs');
const path = require('path');

const activePortFile = path.join(
  process.env.LOCALAPPDATA || 'C:\\Users\\mande\\AppData\\Local',
  'Google\\Chrome\\User Data\\DevToolsActivePort'
);

const [port, browserPath] = fs.readFileSync(activePortFile, 'utf8').trim().split('\n');
const wsUrl = `ws://127.0.0.1:${port.trim()}${browserPath.trim()}`;

console.log('Connecting to:', wsUrl);
const ws = new WebSocket(wsUrl);

ws.addEventListener('open', () => {
  ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
});

ws.addEventListener('message', (e) => {
  const msg = JSON.parse(e.data);
  if (msg.id === 1) {
    const targets = (msg.result && msg.result.targetInfos) || [];
    console.log(`Found ${targets.length} targets:`);
    targets.forEach(t => {
      if (t.type === 'page') {
        console.log(`- [${t.type}] "${t.title}" -> ${t.url} (id: ${t.targetId})`);
      }
    });
    ws.close();
    process.exit(0);
  }
});

ws.addEventListener('error', (err) => {
  console.error('WS Error:', err);
  process.exit(1);
});
