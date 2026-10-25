#!/usr/bin/env node
/**
 * Chrome CDP Safe Inspector for Wyvern Chat
 * Connects directly via WebSocket discovered in DevToolsActivePort,
 * evaluates DOM state in the target chat page, writes JSON output,
 * and immediately closes the WebSocket to respect Chrome's single-client rule.
 */

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function getArg(flag, defaultValue = null) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : defaultValue;
}

const chatFilter = getArg('--chat-id', 'chat_log_qUdWrgx232YGtwDE2318a');
const outputPath = getArg('--output', path.join(__dirname, '..', '..', '..', 'scratch', 'cdp_inspection_result.json'));

const activePortFile = path.join(
  process.env.LOCALAPPDATA || 'C:\\Users\\mande\\AppData\\Local',
  'Google\\Chrome\\User Data\\DevToolsActivePort'
);

if (!fs.existsSync(activePortFile)) {
  console.error(`Error: DevToolsActivePort not found at ${activePortFile}`);
  process.exit(1);
}

const [port, browserPath] = fs.readFileSync(activePortFile, 'utf8').trim().split('\n');
const wsUrl = `ws://127.0.0.1:${port.trim()}${browserPath.trim()}`;

const ws = new WebSocket(wsUrl);

ws.addEventListener('open', () => {
  ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));
});

ws.addEventListener('message', (e) => {
  const msg = JSON.parse(e.data);

  if (msg.id === 1) {
    const targets = (msg.result && msg.result.targetInfos) || [];
    const target = targets.find((t) => t.type === 'page' && t.url && t.url.includes(chatFilter));
    if (!target) {
      console.error(`Target matching "${chatFilter}" not found.`);
      ws.close();
      process.exit(1);
    }

    ws.send(JSON.stringify({
      id: 2,
      method: 'Target.attachToTarget',
      params: { targetId: target.targetId, flatten: true }
    }));
  } else if (msg.id === 2) {
    const sessionId = msg.result.sessionId;

    const evalExpression = `
      (() => {
        const dialog = document.querySelector('[role="dialog"]');
        const toggles = Array.from(document.querySelectorAll('button[role="switch"], [data-state]')).map(el => ({
          id: el.id,
          name: el.getAttribute('name'),
          state: el.getAttribute('data-state'),
          checked: el.getAttribute('data-state') === 'checked',
          ariaChecked: el.getAttribute('aria-checked')
        }));

        const badges = Array.from(document.querySelectorAll('span, div')).filter(el => {
          const t = el.innerText ? el.innerText.trim() : '';
          return t === 'On' || t === 'Off';
        }).map(el => ({ text: el.innerText.trim(), className: el.className }));

        const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText ? b.innerText.trim() : '').filter(t => t.length > 0 && t.length < 80);

        return {
          title: document.title,
          url: window.location.href,
          dialogOpen: !!dialog,
          dialogTextSnippet: dialog ? dialog.innerText.slice(0, 300) : null,
          toggles,
          badges: badges.slice(0, 10),
          notableButtons: buttons.filter(b => b.includes('Linked:') || b.includes('Overrides') || b.includes('Narrator') || b.includes('Storyteller') || b.includes('Balanced'))
        };
      })()
    `;

    ws.send(JSON.stringify({
      id: 3,
      sessionId,
      method: 'Runtime.evaluate',
      params: { expression: evalExpression, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 3) {
    const evalResult = (msg.result && msg.result.result && msg.result.result.value) || {};
    const resolvedOut = path.resolve(outputPath);
    fs.mkdirSync(path.dirname(resolvedOut), { recursive: true });
    fs.writeFileSync(resolvedOut, JSON.stringify(evalResult, null, 2), 'utf8');
    console.log(`Success! CDP evaluation written to: ${resolvedOut}`);

    ws.close();
    process.exit(0);
  }
});

ws.addEventListener('error', (err) => {
  console.error('WebSocket Error:', err);
  process.exit(1);
});
