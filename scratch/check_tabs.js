const fs = require('fs');
const path = require('path');

const devtoolsPath = path.join(process.env.LOCALAPPDATA, 'Google', 'Chrome', 'User Data', 'DevToolsActivePort');
const devtools = fs.readFileSync(devtoolsPath, 'utf8').trim().split(/\r?\n/);
const port = devtools[0];
const wsPath = devtools[1];

const ws = new WebSocket(`ws://127.0.0.1:${port}${wsPath}`);

ws.onopen = () => {
  ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.id === 1) {
    const pages = data.result.targetInfos.filter(t => t.type === 'page');
    console.log(JSON.stringify(pages, null, 2));
    ws.close();
  }
};

ws.onerror = (e) => {
  console.error('WS Error:', e);
  process.exit(1);
};
