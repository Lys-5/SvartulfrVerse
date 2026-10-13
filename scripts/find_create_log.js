async function findCreateWorldChatLogDef() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/88676-11ecc49c3bd7ce22.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('createWorldChatLog');
  while (idx !== -1) {
    console.log('--- 88676 at', idx, '---');
    console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 400)));
    idx = text.indexOf('createWorldChatLog', idx + 10);
  }
}

findCreateWorldChatLogDef().catch(console.error);
