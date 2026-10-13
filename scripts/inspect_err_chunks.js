async function inspectErrorStack() {
  const url1 = 'https://app.wyvern.chat/_next/static/chunks/88676-11ecc49c3bd7ce22.js';
  const text1 = await (await fetch(url1)).text();
  console.log('--- 88676 chunk (around 3532 and 1333) ---');
  console.log('Around 3532:', text1.slice(Math.max(0, 3532 - 150), Math.min(text1.length, 3532 + 250)));
  console.log('Around 1333:', text1.slice(Math.max(0, 1333 - 150), Math.min(text1.length, 1333 + 250)));

  const url2 = 'https://app.wyvern.chat/_next/static/chunks/24224-6accf84b4f65cb82.js';
  const text2 = await (await fetch(url2)).text();
  console.log('\n--- 24224 chunk (around 144297) ---');
  console.log(text2.slice(Math.max(0, 144297 - 200), Math.min(text2.length, 144297 + 300)));
}

inspectErrorStack().catch(console.error);
