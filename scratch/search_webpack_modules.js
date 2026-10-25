const { spawn } = require('child_process');
const fs = require('fs');

class DevToolsClient {
  constructor() {
    this.proc = null;
    this.buffer = '';
    this.idCounter = 1;
    this.pending = new Map();
  }

  async start() {
    return new Promise((resolve, reject) => {
      this.proc = spawn('npx', ['chrome-devtools-mcp@latest', '--auto-connect'], {
        shell: true,
        stdio: ['pipe', 'pipe', 'inherit']
      });

      this.proc.stdout.on('data', (chunk) => {
        this.buffer += chunk.toString();
        const lines = this.buffer.split('\n');
        this.buffer = lines.pop();
        for (const line of lines) {
          if (!line.trim()) continue;
          try {
            const msg = JSON.parse(line);
            if (msg.id && this.pending.has(msg.id)) {
              const { res, rej } = this.pending.get(msg.id);
              this.pending.delete(msg.id);
              if (msg.error) rej(msg.error);
              else res(msg.result);
            }
          } catch (e) {}
        }
      });

      this.send({
        jsonrpc: '2.0',
        id: this.idCounter++,
        method: 'initialize',
        params: {
          protocolVersion: '2024-11-05',
          capabilities: {},
          clientInfo: { name: 'wyvern-webpack-explorer', version: '1.0.0' }
        }
      }).then((res) => {
        this.proc.stdin.write(JSON.stringify({ jsonrpc: '2.0', method: 'notifications/initialized' }) + '\n');
        resolve(res);
      }).catch(reject);
    });
  }

  async send(msg) {
    return new Promise((res, rej) => {
      this.pending.set(msg.id, { res, rej });
      this.proc.stdin.write(JSON.stringify(msg) + '\n');
    });
  }

  async callTool(name, args = {}) {
    const id = this.idCounter++;
    return this.send({
      jsonrpc: '2.0',
      id,
      method: 'tools/call',
      params: { name, arguments: args }
    });
  }

  async stop() {
    if (this.proc) this.proc.kill();
  }
}

async function main() {
  const client = new DevToolsClient();
  await client.start();

  const pagesRes = await client.callTool('list_pages', {});
  console.log('Pages:', JSON.stringify(pagesRes));

  // Evaluate search across webpack modules and global scripts on Page 1
  const searchEval = await client.callTool('evaluate_script', {
    pageId: 1,
    waitForStableDom: false,
    function: `() => {
      const results = {};
      
      // Look for webpack modules
      let webpackModules = [];
      if (typeof window.__webpack_require__ !== 'undefined' && window.__webpack_require__.m) {
        webpackModules = Object.entries(window.__webpack_require__.m);
      } else if (typeof window.webpackChunk_N_E !== 'undefined') {
        // try to find webpack modules from push
        for (const chunk of window.webpackChunk_N_E) {
          if (chunk && chunk[1]) {
            for (const [modId, fn] of Object.entries(chunk[1])) {
              webpackModules.push([modId, fn]);
            }
          }
        }
      }

      results.moduleCount = webpackModules.length;

      const keywords = ['avatar_activation_regex', 'npc_info', 'custom_avatar_regex', 'lines_parsed', 'npc_prefix'];
      results.matches = {};

      for (const [modId, fn] of webpackModules) {
        const fnStr = fn.toString();
        for (const kw of keywords) {
          if (fnStr.includes(kw)) {
            if (!results.matches[kw]) results.matches[kw] = [];
            results.matches[kw].push({
              modId,
              snippet: fnStr.slice(Math.max(0, fnStr.indexOf(kw) - 150), Math.min(fnStr.length, fnStr.indexOf(kw) + 300))
            });
          }
        }
      }

      return results;
    }`
  });

  fs.writeFileSync('scratch/webpack_search_results.json', JSON.stringify(searchEval, null, 2));
  console.log('Search Eval Result written to scratch/webpack_search_results.json');
  console.log('Summary:', JSON.stringify(searchEval, null, 2).slice(0, 1000));

  await client.stop();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
