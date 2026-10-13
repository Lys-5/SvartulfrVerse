async function inspectBuildHook() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('function l$');
  console.log('--- Context before function l$ ---');
  console.log(text.slice(Math.max(0, idx - 1500), idx));
}

inspectBuildHook().catch(console.error);
