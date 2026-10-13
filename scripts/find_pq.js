async function findPersonasHook() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('.pQ)(');
  console.log('--- Context of .pQ)( ---');
  console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 200)));
}

findPersonasHook().catch(console.error);
