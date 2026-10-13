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
          const emptyDiv = document.querySelector('.flex-1.min-h-0.overflow-y-auto.p-5');
          const key = Object.keys(emptyDiv).find(k => k.startsWith('__reactFiber$'));
          const fiber = emptyDiv[key];
          
          const ch = fiber.memoizedProps.children;
          
          // Let's inspect ch
          let chInfo = null;
          if (ch) {
            chInfo = {
              type: typeof ch,
              isReactElement: Boolean(ch.$$typeof),
              elementType: typeof ch.type === 'string' ? ch.type : (ch.type?.displayName || ch.type?.name || 'function/class'),
              propsKeys: ch.props ? Object.keys(ch.props) : null,
              props: ch.props ? {
                page: ch.props.page ? { id: ch.props.page.id, type: ch.props.page.type } : null,
                field: ch.props.field ? { id: ch.props.field.id, type: ch.props.field.type, optionsCount: ch.props.field.options?.length } : null,
                fields: ch.props.fields ? Object.keys(ch.props.fields) : null,
                options: ch.props.options ? ch.props.options.length : null
              } : null
            };
          }
          
          // Also let's inspect fiber.child
          let childFiber = fiber.child;
          let childFiberInfo = null;
          if (childFiber) {
            childFiberInfo = {
              type: typeof childFiber.type === 'string' ? childFiber.type : (childFiber.type?.displayName || childFiber.type?.name || 'function'),
              memoizedPropsKeys: childFiber.memoizedProps ? Object.keys(childFiber.memoizedProps) : null
            };
          }

          return {
            chInfo,
            childFiberInfo
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
    console.log('CHILDREN INFO:\n', JSON.stringify(msg.result.result.value, null, 2));
    process.exit(0);
  }
};
