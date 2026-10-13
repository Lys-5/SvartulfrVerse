const fs = require('fs');

const devToolsActivePort = fs.readFileSync('C:\\Users\\mande\\AppData\\Local\\Google\\Chrome\\User Data\\DevToolsActivePort', 'utf8').split('\n');
const browserPath = devToolsActivePort[1].trim();

const ws = new WebSocket('ws://127.0.0.1:9222' + browserPath);
ws.onopen = () => ws.send(JSON.stringify({ id: 1, method: 'Target.getTargets' }));

ws.onmessage = async (e) => {
  const msg = JSON.parse(e.data);
  if (msg.id === 1) {
    const t = msg.result.targetInfos.find(x => x.url && x.url.includes('app.wyvern.chat'));
    ws.send(JSON.stringify({
      id: 2,
      method: 'Target.attachToTarget',
      params: { targetId: t.targetId, flatten: true }
    }));
  } else if (msg.id === 2) {
    const code = `
      (() => {
        try {
          const h2 = document.querySelector('h2');
          if (!h2) return { error: 'h2 not found' };
          
          let cur = h2;
          let foundProps = null;
          let depth = 0;
          
          const key = Object.keys(h2).find(k => k.startsWith('__reactFiber$'));
          let fiber = h2[key];
          
          const components = [];
          while (fiber && depth < 40) {
            depth++;
            const compName = fiber.type ? (fiber.type.displayName || fiber.type.name || (typeof fiber.type === 'string' ? fiber.type : 'Anonymous')) : 'Unknown';
            const props = fiber.memoizedProps;
            if (props) {
              const pKeys = Object.keys(props);
              components.push({
                compName,
                keys: pKeys.filter(k => k !== 'children'),
                page: props.page ? { id: props.page.id, type: props.page.type, title: props.page.title } : undefined,
                pagesCount: Array.isArray(props.pages) ? props.pages.length : undefined,
                currentPage: typeof props.currentPage === 'number' ? props.currentPage : undefined,
                fieldsKeys: props.fields ? Object.keys(props.fields) : undefined,
                introFieldsKeys: props.intro_fields ? Object.keys(props.intro_fields) : undefined
              });
            }
            fiber = fiber.return;
          }
          
          return {
            h2Text: h2.innerText,
            components
          };
        } catch(err) {
          return { error: err.message, stack: err.stack };
        }
      })()
    `;
    ws.send(JSON.stringify({
      id: 3,
      sessionId: msg.result.sessionId,
      method: 'Runtime.evaluate',
      params: { expression: code, returnByValue: true, awaitPromise: true }
    }));
  } else if (msg.id === 3) {
    console.log('RESULT:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
