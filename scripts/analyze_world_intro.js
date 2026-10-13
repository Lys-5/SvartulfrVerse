async function analyzeWorldIntro() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const res = await fetch(url);
  const text = await res.text();
  
  let idx = text.indexOf('worldIntro:');
  while (idx !== -1) {
    console.log('--- worldIntro: ---');
    console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 300)));
    idx = text.indexOf('worldIntro:', idx + 10);
  }

  let idx2 = text.indexOf('.worldIntro');
  while (idx2 !== -1) {
    console.log('--- .worldIntro ---');
    console.log(text.slice(Math.max(0, idx2 - 100), Math.min(text.length, idx2 + 300)));
    idx2 = text.indexOf('.worldIntro', idx2 + 10);
  }
}

analyzeWorldIntro().catch(console.error);
