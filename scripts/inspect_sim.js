async function inspectSimPage() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('/sim');
  while (idx !== -1) {
    console.log('--- /sim ---');
    console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 300)));
    idx = text.indexOf('/sim', idx + 10);
  }
}

inspectSimPage().catch(console.error);
