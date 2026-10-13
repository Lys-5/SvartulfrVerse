async function inspectEi() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('ei=async');
  if (idx === -1) idx = text.indexOf('ei = async');
  console.log('--- Context of ei=async ---');
  console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 1500)));
}

inspectEi().catch(console.error);
