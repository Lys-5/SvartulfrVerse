async function findL4Call() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  // Find where l4 is referenced
  let idx = text.indexOf('initialScenarioId:');
  while (idx !== -1) {
    console.log('--- initialScenarioId: ---');
    console.log(text.slice(Math.max(0, idx - 150), Math.min(text.length, idx + 350)));
    idx = text.indexOf('initialScenarioId:', idx + 10);
  }
}

findL4Call().catch(console.error);
