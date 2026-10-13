async function inspectOAndE() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('q=E.filter');
  console.log('--- Context before q=E.filter ---');
  console.log(text.slice(Math.max(0, idx - 1200), idx));
}

inspectOAndE().catch(console.error);
