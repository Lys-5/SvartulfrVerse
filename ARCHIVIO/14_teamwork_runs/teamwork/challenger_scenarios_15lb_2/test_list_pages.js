const { spawn } = require('child_process');

async function testListPages() {
  const proc = spawn('npx', ['chrome-devtools-mcp@latest', '--auto-connect'], {
    shell: true,
    stdio: ['pipe', 'pipe', 'inherit']
  });

  let buffer = '';
  let idCounter = 1;
  const pending = new Map();

  proc.stdout.on('data', (chunk) => {
    buffer += chunk.toString();
    const lines = buffer.split('\n');
    buffer = lines.pop();
    for (const line of lines) {
      if (!line.trim()) continue;
      try {
        const msg = JSON.parse(line);
        if (msg.id && pending.has(msg.id)) {
          const { res, rej } = pending.get(msg.id);
          pending.delete(msg.id);
          if (msg.error) rej(msg.error);
          else res(msg.result);
        }
      } catch (e) {}
    }
  });

  function send(msg) {
    return new Promise((res, rej) => {
      pending.set(msg.id, { res, rej });
      proc.stdin.write(JSON.stringify(msg) + '\n');
    });
  }

  // initialize
  console.log("Initializing MCP...");
  const initRes = await send({
    jsonrpc: '2.0',
    id: idCounter++,
    method: 'initialize',
    params: {
      protocolVersion: '2024-11-05',
      capabilities: {},
      clientInfo: { name: 'challenger-cdp', version: '1.0.0' }
    }
  });
  proc.stdin.write(JSON.stringify({ jsonrpc: '2.0', method: 'notifications/initialized' }) + '\n');
  console.log("MCP Initialized successfully!");

  console.log("Calling list_pages tool...");
  const pages = await send({
    jsonrpc: '2.0',
    id: idCounter++,
    method: 'tools/call',
    params: { name: 'list_pages', arguments: {} }
  });

  console.log("PAGES RESULT:\n", JSON.stringify(pages, null, 2));

  proc.kill();
}

testListPages().catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
