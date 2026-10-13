async function findModeDeterminer() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('("intro"===a||"scenario"===a)&&t');
  console.log('--- Context of mode a ---');
  console.log(text.slice(Math.max(0, idx - 600), Math.min(text.length, idx + 400)));
}

findModeDeterminer().catch(console.error);
