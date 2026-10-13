async function inspectAfterK() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('if(c&&!ee&&I.rpg){');
  console.log('--- Context of if(c&&!ee&&I.rpg) ---');
  console.log(text.slice(idx, idx + 800));
}

inspectAfterK().catch(console.error);
