async function inspect77818() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/77818-620a879e0867944c.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('getSpecies');
  console.log('--- getSpecies in 77818 ---');
  console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 400)));

  let idx2 = text.indexOf('getOccupations');
  console.log('\n--- getOccupations in 77818 ---');
  console.log(text.slice(Math.max(0, idx2 - 100), Math.min(text.length, idx2 + 400)));

  let idx3 = text.indexOf('getTraits');
  console.log('\n--- getTraits in 77818 ---');
  console.log(text.slice(Math.max(0, idx3 - 100), Math.min(text.length, idx3 + 400)));
}

inspect77818().catch(console.error);
