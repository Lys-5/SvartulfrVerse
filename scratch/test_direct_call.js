const { spawn } = require('child_process');
const fs = require('fs');

const MCP_BIN = 'C:\\Users\\mande\\AppData\\Local\\npm-cache\\_npx\\15c61037b1978c83\\node_modules\\chrome-devtools-mcp\\build\\src\\bin\\chrome-devtools-mcp.js';

const devToolsPort = fs.readFileSync('C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort', 'utf8').trim().split('\n');
const wsEndpoint = `ws://127.0.0.1:${devToolsPort[0].trim()}${devToolsPort[1].trim()}`;
console.log('Connecting via wsEndpoint:', wsEndpoint);

const proc = spawn('node', [MCP_BIN, `--wsEndpoint=${wsEndpoint}`, '--logFile=scratch/cdm_direct.log'], {
  stdio: ['pipe', 'pipe', 'inherit']
});

let buffer = '';

function send(obj) {
  console.log('>>> SENDING:', JSON.stringify(obj));
  proc.stdin.write(JSON.stringify(obj) + '\n');
}

proc.stdout.on('data', (chunk) => {
  buffer += chunk.toString();
  const lines = buffer.split('\n');
  buffer = lines.pop();
  for (const line of lines) {
    if (!line.trim()) continue;
    try {
      const msg = JSON.parse(line);
      console.log('<<< RECV:', JSON.stringify(msg, null, 2));
      if (msg.id === 1) {
        send({ jsonrpc: '2.0', method: 'notifications/initialized' });
        send({ jsonrpc: '2.0', id: 2, method: 'tools/call', params: { name: 'list_pages', arguments: {} } });
      } else if (msg.id === 2) {
        console.log('SUCCESS! list_pages:', msg.result.content[0].text);
        proc.kill();
        process.exit(0);
      }
    } catch (e) {
      console.log('<<< RAW:', line);
    }
  }
});

send({
  jsonrpc: '2.0',
  id: 1,
  method: 'initialize',
  params: {
    protocolVersion: '2024-11-05',
    capabilities: {},
    clientInfo: { name: 'test-direct', version: '1.0.0' }
  }
});

setTimeout(() => {
  console.log('Timeout after 12s!');
  if (fs.existsSync('scratch/cdm_direct.log')) {
    console.log('LOG CONTENT:\n', fs.readFileSync('scratch/cdm_direct.log', 'utf8'));
  }
  proc.kill();
  process.exit(1);
}, 12000);
