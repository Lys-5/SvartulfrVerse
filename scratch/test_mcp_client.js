const { spawn } = require('child_process');

async function run() {
  const proc = spawn('npx', ['chrome-devtools-mcp@latest', '--auto-connect'], {
    shell: true,
    stdio: ['pipe', 'pipe', 'inherit']
  });

  let buffer = '';
  
  function send(obj) {
    const str = JSON.stringify(obj) + '\n';
    console.log('SENDING:', JSON.stringify(obj));
    proc.stdin.write(str);
  }

  proc.stdout.on('data', (chunk) => {
    buffer += chunk.toString();
    const lines = buffer.split('\n');
    buffer = lines.pop(); // keep partial line
    for (const line of lines) {
      if (!line.trim()) continue;
      try {
        const msg = JSON.parse(line);
        console.log('RECEIVED:', JSON.stringify(msg, null, 2));
        if (msg.id === 1) {
          send({ jsonrpc: '2.0', method: 'notifications/initialized' });
          send({ jsonrpc: '2.0', id: 2, method: 'tools/call', params: { name: 'list_pages', arguments: {} } });
        } else if (msg.id === 2) {
          console.log('TOOL RESULT:', JSON.stringify(msg.result, null, 2));
          proc.kill();
          process.exit(0);
        }
      } catch (e) {
        console.log('RAW STDOUT:', line);
      }
    }
  });

  proc.on('close', (code) => {
    console.log('Exited with code', code);
  });

  send({
    jsonrpc: '2.0',
    id: 1,
    method: 'initialize',
    params: {
      protocolVersion: '2024-11-05',
      capabilities: {},
      clientInfo: { name: 'test-inspector', version: '1.0.0' }
    }
  });

  setTimeout(() => {
    console.log('Timeout reached. Killing process.');
    proc.kill();
    process.exit(1);
  }, 15000);
}

run().catch(console.error);
