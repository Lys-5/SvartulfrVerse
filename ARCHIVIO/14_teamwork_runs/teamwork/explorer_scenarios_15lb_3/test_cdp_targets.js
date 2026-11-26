const fs = require('fs');
const http = require('http');

console.log("=== 1. Testing HTTP endpoints on 9222 ===");
function testHttp(path) {
  return new Promise((resolve) => {
    const req = http.get({
      host: '127.0.0.1',
      port: 9222,
      path: path,
      headers: { 'Host': '127.0.0.1' }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        resolve({ path, status: res.statusCode, body: data.slice(0, 100) });
      });
    });
    req.on('error', (err) => resolve({ path, error: err.message }));
    req.setTimeout(2000, () => {
      req.destroy();
      resolve({ path, error: 'TIMEOUT' });
    });
  });
}

async function run() {
  const paths = ['/json/version', '/json/list', '/json', '/'];
  for (const p of paths) {
    const res = await testHttp(p);
    console.log(`Path: ${p.padEnd(15)} -> Status: ${res.status || res.error}`);
  }

  console.log("\n=== 2. Reading DevToolsActivePort ===");
  const activePortFile = 'C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort';
  if (fs.existsSync(activePortFile)) {
    const lines = fs.readFileSync(activePortFile, 'utf8').trim().split('\n');
    console.log(`DevToolsActivePort Port: ${lines[0].trim()}`);
    console.log(`DevToolsActivePort Browser Target: ${lines[1].trim()}`);
    const wsUrl = `ws://127.0.0.1:${lines[0].trim()}${lines[1].trim()}`;
    console.log(`Full WebSocket URL: ${wsUrl}`);
  } else {
    console.log("DevToolsActivePort file does NOT exist!");
  }
}

run();
