async function inspectWorldApi() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('getSpecies:');
  if (idx === -1) idx = text.indexOf('getSpecies');
  console.log('--- Context of getSpecies ---');
  console.log(text.slice(Math.max(0, idx - 200), Math.min(text.length, idx + 400)));

  let idx2 = text.indexOf('/species');
  while (idx2 !== -1) {
    console.log('--- /species ---');
    console.log(text.slice(Math.max(0, idx2 - 100), Math.min(text.length, idx2 + 200)));
    idx2 = text.indexOf('/species', idx2 + 10);
  }
}

inspectWorldApi().catch(console.error);
