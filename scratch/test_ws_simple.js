const fs = require('fs');

const devToolsActivePort = fs.readFileSync('C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort', 'utf8').split('\n');
const port = devToolsActivePort[0].trim();
const browserPath = devToolsActivePort[1].trim();
const url = `ws://127.0.0.1:${port}${browserPath}`;
console.log('Connecting to:', url);

const ws = new WebSocket(url);
const timer = setTimeout(() => {
  console.log('Timeout after 4s!');
  process.exit(1);
}, 4000);

ws.onopen = () => {
  console.log('WS Open!');
  ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
};

ws.onmessage = (e) => {
  console.log('WS Message received:', e.data.slice(0, 200));
  clearTimeout(timer);
  ws.close();
  process.exit(0);
};

ws.onerror = (err) => {
  console.error('WS Error:', err);
  clearTimeout(timer);
  process.exit(1);
};

ws.onclose = (evt) => {
  console.log('WS Closed:', evt.code, evt.reason);
};
