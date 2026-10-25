const { spawn } = require('child_process');
const fs = require('fs');

async function run() {
  const proc = spawn('npx', ['chrome-devtools-mcp@latest', '--auto-connect'], {
    shell: true,
    stdio: ['pipe', 'pipe', 'inherit']
  });

  let buffer = '';
  let currentReqId = 1;
  const pendingRequests = new Map();

  function sendRequest(method, params) {
    const id = currentReqId++;
    const msg = { jsonrpc: '2.0', id, method, params };
    console.log(`[REQ ${id}] -> ${method}`, params?.name || '');
    proc.stdin.write(JSON.stringify(msg) + '\n');
    return new Promise((resolve, reject) => {
      pendingRequests.set(id, { resolve, reject, method, params });
    });
  }

  function sendNotification(method, params) {
    const msg = { jsonrpc: '2.0', method, params };
    console.log(`[NOTIFY] -> ${method}`);
    proc.stdin.write(JSON.stringify(msg) + '\n');
  }

  proc.stdout.on('data', (chunk) => {
    buffer += chunk.toString();
    const lines = buffer.split('\n');
    buffer = lines.pop();
    for (const line of lines) {
      if (!line.trim()) continue;
      try {
        const msg = JSON.parse(line);
        if (msg.id && pendingRequests.has(msg.id)) {
          const { resolve, reject } = pendingRequests.get(msg.id);
          pendingRequests.delete(msg.id);
          if (msg.error) {
            console.error(`[ERR ${msg.id}]`, JSON.stringify(msg.error));
            reject(msg.error);
          } else {
            console.log(`[RESP ${msg.id}] received`);
            resolve(msg.result);
          }
        }
      } catch (e) {
        // console.log('NON-JSON:', line);
      }
    }
  });

  // Step 1: Initialize
  console.log('Step 1: Initializing...');
  const initRes = await sendRequest('initialize', {
    protocolVersion: '2024-11-05',
    capabilities: {},
    clientInfo: { name: 'wyvern-explorer', version: '1.0.0' }
  });
  console.log('Initialized server:', initRes.serverInfo.name);

  sendNotification('notifications/initialized');

  // Step 2: List Pages
  console.log('\nStep 2: Listing pages...');
  const pagesRes = await sendRequest('tools/call', {
    name: 'list_pages',
    arguments: {}
  });
  const pagesText = pagesRes.content[0].text;
  console.log('Pages:\n' + pagesText);
  fs.writeFileSync('scratch/pages_list.txt', pagesText);

  // Parse page numbers:
  // e.g. 1: ..., 2: ..., 4: ...
  const lines = pagesText.split('\n');
  let assistantPageId = 4;
  let wyvernAppPageId = 2;

  for (const l of lines) {
    if (l.includes('https://app.wyvern.chat/assistants')) {
      const match = l.match(/^(\d+):/);
      if (match) assistantPageId = parseInt(match[1]);
    } else if (l.includes('https://app.wyvern.chat/')) {
      const match = l.match(/^(\d+):/);
      if (match) wyvernAppPageId = parseInt(match[1]);
    }
  }

  console.log(`Targeting Assistant Page: ${assistantPageId}, App Page: ${wyvernAppPageId}`);

  // Step 3: Evaluate Login Status on Wyvern App Page
  console.log('\nStep 3: Evaluating Login Status and LocalStorage on App Page...');
  try {
    const authEval = await sendRequest('tools/call', {
      name: 'evaluate_script',
      arguments: {
        pageId: wyvernAppPageId,
        waitForStableDom: false,
        function: `() => {
          const authKey = Object.keys(localStorage).find(k => k.toLowerCase().includes('auth') || k.toLowerCase().includes('user') || k.toLowerCase().includes('token'));
          let authData = null;
          if (authKey) {
            try { authData = JSON.parse(localStorage.getItem(authKey)); } catch(e) { authData = localStorage.getItem(authKey); }
          }
          return {
            title: document.title,
            url: window.location.href,
            localStorageKeys: Object.keys(localStorage),
            authKey: authKey,
            userEmail: authData?.user?.email || authData?.email || 'N/A',
            userId: authData?.user?.id || authData?.id || 'N/A',
            isLoggedIn: !!authKey
          };
        }`
      }
    });
    console.log('Auth eval result:', JSON.stringify(authEval, null, 2));
    fs.writeFileSync('scratch/auth_status.json', JSON.stringify(authEval, null, 2));
  } catch (err) {
    console.error('Auth eval failed:', err);
  }

  // Step 4: Snapshot of Assistant Page (pageId: assistantPageId)
  console.log('\nStep 4: Snapshot of Assistant Page...');
  try {
    const snapRes = await sendRequest('tools/call', {
      name: 'take_snapshot',
      arguments: {
        pageId: assistantPageId,
        filePath: 'scratch/snapshot_assistant_page.txt'
      }
    });
    console.log('Snapshot result:', JSON.stringify(snapRes, null, 2));
  } catch (err) {
    console.error('Snapshot failed:', err);
  }

  // Step 5: DOM deep inspection of Assistant Page
  console.log('\nStep 5: DOM deep inspection of Assistant Page...');
  try {
    const domEval = await sendRequest('tools/call', {
      name: 'evaluate_script',
      arguments: {
        pageId: assistantPageId,
        waitForStableDom: false,
        function: `() => {
          return {
            title: document.title,
            url: window.location.href,
            inputs: Array.from(document.querySelectorAll('input')).map(el => ({
              type: el.type,
              name: el.name,
              id: el.id,
              placeholder: el.placeholder,
              value: el.value,
              ariaLabel: el.getAttribute('aria-label'),
              className: el.className
            })),
            textareas: Array.from(document.querySelectorAll('textarea')).map(el => ({
              name: el.name,
              id: el.id,
              placeholder: el.placeholder,
              valueSnippet: el.value ? el.value.slice(0, 100) : '',
              ariaLabel: el.getAttribute('aria-label'),
              className: el.className
            })),
            buttons: Array.from(document.querySelectorAll('button')).map(el => ({
              text: el.innerText.trim(),
              ariaLabel: el.getAttribute('aria-label'),
              className: el.className
            })),
            tabs: Array.from(document.querySelectorAll('[role="tab"], nav a, nav button')).map(el => ({
              text: el.innerText.trim(),
              role: el.getAttribute('role'),
              href: el.getAttribute('href')
            })),
            headings: Array.from(document.querySelectorAll('h1, h2, h3, h4, h5')).map(el => el.innerText.trim())
          };
        }`
      }
    });
    console.log('Assistant DOM details extracted!');
    fs.writeFileSync('scratch/assistant_dom_details.json', JSON.stringify(domEval, null, 2));
  } catch (err) {
    console.error('Assistant DOM eval failed:', err);
  }

  // Step 6: Console status
  console.log('\nStep 6: Inspecting console messages on Assistant Page...');
  try {
    const consoleRes = await sendRequest('tools/call', {
      name: 'list_console_messages',
      arguments: {
        pageId: assistantPageId,
        pageSize: 30
      }
    });
    console.log('Console messages retrieved!');
    fs.writeFileSync('scratch/console_assistant_page.json', JSON.stringify(consoleRes, null, 2));
  } catch (err) {
    console.error('Console retrieval failed:', err);
  }

  // Step 7: Network requests on Assistant Page
  console.log('\nStep 7: Inspecting network requests on Assistant Page...');
  try {
    const netRes = await sendRequest('tools/call', {
      name: 'list_network_requests',
      arguments: {
        pageId: assistantPageId,
        pageSize: 30
      }
    });
    console.log('Network requests retrieved!');
    fs.writeFileSync('scratch/network_assistant_page.json', JSON.stringify(netRes, null, 2));
  } catch (err) {
    console.error('Network retrieval failed:', err);
  }

  console.log('\nAll steps completed! Closing server.');
  proc.kill();
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal error in run():', err);
  process.exit(1);
});
