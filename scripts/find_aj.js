async function findAJModule() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('aJ=');
  console.log('--- aJ= ---');
  console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 200)));
}

findAJModule().catch(console.error);
