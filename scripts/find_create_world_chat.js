async function findCreateWorldChat() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('createWorldChat:');
  if (idx === -1) idx = text.indexOf('createWorldChat');
  console.log('--- Context of createWorldChat ---');
  console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 400)));
}

findCreateWorldChat().catch(console.error);
