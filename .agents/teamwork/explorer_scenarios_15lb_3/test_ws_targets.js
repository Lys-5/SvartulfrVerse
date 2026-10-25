const fs = require('fs');

const activePortFile = 'C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort';
const lines = fs.readFileSync(activePortFile, 'utf8').trim().split('\n');
const wsUrl = `ws://127.0.0.1:${lines[0].trim()}${lines[1].trim()}`;

console.log("Connecting to WebSocket:", wsUrl);

const ws = new WebSocket(wsUrl);

const timer = setTimeout(() => {
  console.log("WebSocket connection timed out (Chrome security dialog or restricted WebSocket)");
  ws.close();
  process.exit(0);
}, 4000);

ws.onopen = () => {
  console.log("Connected to browser WebSocket!");
  ws.send(JSON.stringify({
    id: 1,
    method: "Target.getTargets"
  }));
};

ws.onmessage = (event) => {
  clearTimeout(timer);
  const data = JSON.parse(event.data);
  console.log("Received response for id:", data.id);
  if (data.id === 1 && data.result) {
    console.log("Target count:", data.result.targetInfos.length);
    for (const t of data.result.targetInfos) {
      console.log(`- [${t.type}] ${t.title} (${t.url})`);
    }
  }
  ws.close();
  process.exit(0);
};

ws.onerror = (err) => {
  console.log("WebSocket error:", err.message);
};
