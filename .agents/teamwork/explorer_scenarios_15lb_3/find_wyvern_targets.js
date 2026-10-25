const fs = require('fs');

const activePortFile = 'C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort';
const lines = fs.readFileSync(activePortFile, 'utf8').trim().split('\n');
const wsUrl = `ws://127.0.0.1:${lines[0].trim()}${lines[1].trim()}`;

const ws = new WebSocket(wsUrl);

const timer = setTimeout(() => {
  console.log("Timed out after 5s");
  ws.close();
  process.exit(0);
}, 5000);

ws.onopen = () => {
  ws.send(JSON.stringify({ id: 1, method: "Target.getTargets" }));
};

ws.onmessage = (event) => {
  clearTimeout(timer);
  const data = JSON.parse(event.data);
  if (data.id === 1 && data.result) {
    const wyvernTargets = data.result.targetInfos.filter(t => t.url.includes('wyvern.chat'));
    console.log(`Found ${wyvernTargets.length} Wyvern targets:`);
    for (const t of wyvernTargets) {
      console.log(`Target ID: ${t.targetId} | Type: ${t.type} | Title: ${t.title} | URL: ${t.url}`);
    }
    fs.writeFileSync('e:\\repository\\SvartulfrVerse\\.agents\\teamwork\\explorer_scenarios_15lb_3\\open_wyvern_tabs.json', JSON.stringify(wyvernTargets, null, 2));
  }
  ws.close();
  process.exit(0);
};

ws.onerror = (err) => {
  console.log("WS error:", err.message);
  process.exit(1);
};
