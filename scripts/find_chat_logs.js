const fs = require('fs');

async function searchAllForChatLogsWorld() {
  const chunks = [
    '52117-2379a41b09e4c3bb.js',
    '88676-11ecc49c3bd7ce22.js',
    '24224-6accf84b4f65cb82.js',
    '35454-a8397a1df44fbba7.js',
    '77818-620a879e0867944c.js'
  ];

  for (const c of chunks) {
    const url = 'https://app.wyvern.chat/_next/static/chunks/' + c;
    const text = await (await fetch(url)).text();
    let idx = text.indexOf('chat-logs/world');
    if (idx !== -1) {
      console.log(`FOUND IN ${c} at ${idx}:`);
      console.log(text.slice(Math.max(0, idx - 200), Math.min(text.length, idx + 400)));
    }
  }
}

searchAllForChatLogsWorld().catch(console.error);
