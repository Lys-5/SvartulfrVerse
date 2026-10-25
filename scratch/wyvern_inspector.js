const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

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
          } catch (e) {
            // Not JSON or partial log
          }
        }
      });

      this.send({
        jsonrpc: '2.0',
        id: this.idCounter++,
        method: 'initialize',
        params: {
          protocolVersion: '2024-11-05',
          capabilities: {},
          clientInfo: { name: 'wyvern-session-inspector', version: '1.0.0' }
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
    if (this.proc) {
      this.proc.kill();
    }
  }
}

async function main() {
  const client = new DevToolsClient();
  console.log('Connecting to Chrome DevTools MCP...');
  await client.start();
  console.log('Connected!');

  const pagesRes = await client.callTool('list_pages', {});
  console.log('Pages result:', JSON.stringify(pagesRes, null, 2));

  // Write pages list to scratch/pages.json
  fs.writeFileSync('scratch/pages.json', JSON.stringify(pagesRes, null, 2));

  // Let's inspect Page 4 (Assistant)
  console.log('--- Inspecting Page 4 (Assistant) ---');
  try {
    const snapshotPage4 = await client.callTool('take_snapshot', { pageId: 4, verbose: false });
    fs.writeFileSync('scratch/snapshot_page4.txt', typeof snapshotPage4.content[0].text === 'string' ? snapshotPage4.content[0].text : JSON.stringify(snapshotPage4));
    console.log('Snapshot Page 4 saved. Size:', snapshotPage4.content[0].text ? snapshotPage4.content[0].text.length : 0);
  } catch (err) {
    console.error('Error snapshot Page 4:', err);
  }

  // Let's evaluate script on Page 4 to get DOM details
  try {
    const page4Details = await client.callTool('evaluate_script', {
      pageId: 4,
      waitForStableDom: false,
      function: `() => {
        return {
          title: document.title,
          url: window.location.href,
          hasLocalStorageToken: !!localStorage.getItem('token') || !!localStorage.getItem('supabase.auth.token') || !!localStorage.getItem('sb-yqewlyrchsqdhyvswwvi-auth-token'),
          localStorageKeys: Object.keys(localStorage),
          headings: Array.from(document.querySelectorAll('h1, h2, h3, h4')).map(h => h.innerText),
          buttons: Array.from(document.querySelectorAll('button')).map(b => ({
            text: b.innerText.trim(),
            ariaLabel: b.getAttribute('aria-label'),
            className: b.className
          })).slice(0, 30),
          inputs: Array.from(document.querySelectorAll('input, textarea, select')).map(el => ({
            tagName: el.tagName,
            name: el.name,
            id: el.id,
            placeholder: el.placeholder,
            type: el.type,
            value: el.value ? el.value.slice(0, 50) : ''
          }))
        };
      }`
    });
    fs.writeFileSync('scratch/page4_dom_eval.json', JSON.stringify(page4Details, null, 2));
    console.log('Page 4 DOM eval saved!');
  } catch (err) {
    console.error('Error eval Page 4:', err);
  }

  // Let's inspect Page 2 (Main WyvernChat app)
  console.log('--- Inspecting Page 2 (WyvernChat App) ---');
  try {
    const page2Details = await client.callTool('evaluate_script', {
      pageId: 2,
      waitForStableDom: false,
      function: `() => {
        return {
          title: document.title,
          url: window.location.href,
          localStorageKeys: Object.keys(localStorage),
          userProfile: (() => {
            const userKey = Object.keys(localStorage).find(k => k.includes('auth-token') || k.includes('user'));
            if (userKey) {
              try {
                const parsed = JSON.parse(localStorage.getItem(userKey));
                return { key: userKey, user: parsed?.user?.email || parsed?.email || parsed?.user?.id || 'Found JSON' };
              } catch(e) {
                return { key: userKey, val: 'Not JSON' };
              }
            }
            return 'No auth token found';
          })(),
          navLinks: Array.from(document.querySelectorAll('a, button')).map(el => ({
            tag: el.tagName,
            text: el.innerText.trim().slice(0, 40),
            href: el.getAttribute('href') || '',
            ariaLabel: el.getAttribute('aria-label') || ''
          })).filter(x => x.text || x.href || x.ariaLabel).slice(0, 40)
        };
      }`
    });
    fs.writeFileSync('scratch/page2_dom_eval.json', JSON.stringify(page2Details, null, 2));
    console.log('Page 2 DOM eval saved!');
  } catch (err) {
    console.error('Error eval Page 2:', err);
  }

  // Let's inspect Console Messages for Page 4 & Page 2
  console.log('--- Inspecting Console Messages ---');
  try {
    const consolePage4 = await client.callTool('list_console_messages', { pageId: 4, pageSize: 20 });
    fs.writeFileSync('scratch/console_page4.json', JSON.stringify(consolePage4, null, 2));
  } catch (err) {
    console.error('Error console Page 4:', err);
  }

  try {
    const consolePage2 = await client.callTool('list_console_messages', { pageId: 2, pageSize: 20 });
    fs.writeFileSync('scratch/console_page2.json', JSON.stringify(consolePage2, null, 2));
  } catch (err) {
    console.error('Error console Page 2:', err);
  }

  // Let's inspect Network Requests for Page 4 & Page 2
  console.log('--- Inspecting Network Requests ---');
  try {
    const netPage4 = await client.callTool('list_network_requests', { pageId: 4, pageSize: 25 });
    fs.writeFileSync('scratch/network_page4.json', JSON.stringify(netPage4, null, 2));
  } catch (err) {
    console.error('Error network Page 4:', err);
  }

  await client.stop();
  console.log('Inspection completed successfully!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
