async function findWorldApiDef() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('getSpecies(');
  while (idx !== -1) {
    console.log('--- getSpecies( ---');
    console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 200)));
    idx = text.indexOf('getSpecies(', idx + 10);
  }
}

findWorldApiDef().catch(console.error);
