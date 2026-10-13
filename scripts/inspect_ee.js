async function inspectEeEarlier() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('er=Math.min');
  console.log('--- Context before er=Math.min (1000 chars) ---');
  console.log(text.slice(Math.max(0, idx - 1000), idx));
}

inspectEeEarlier().catch(console.error);
