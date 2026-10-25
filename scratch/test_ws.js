const fs = require('fs');

const devToolsActivePort = fs.readFileSync('C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort', 'utf8').split('\n');
const port = devToolsActivePort[0].trim();
const browserPath = devToolsActivePort[1].trim();
const wsUrl = `ws://127.0.0.1:${port}${browserPath}`;
console.log('Connecting to', wsUrl);

const ws = new WebSocket(wsUrl);

ws.onopen = () => {
  console.log('Connected! Sending Target.getTargets');
  ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
};

ws.onerror = (err) => {
  console.error('WS Error:', err);
};

ws.onmessage = (e) => {
  console.log('Received message:');
  const msg = JSON.parse(e.data);
  console.log(JSON.stringify(msg, null, 2));
  ws.close();
  process.exit(0);
};

setTimeout(() => {
  console.log('Timeout reached');
  process.exit(1);
}, 5000);
