const fs = require('fs');

async function inspectLorebookCard() {
  const r = await fetch('https://app.wyvern.chat/mine');
  const html = await r.text();
  const scriptMatches = [...html.matchAll(/src="(\/_next\/static\/chunks\/[^"]+\.js)"/g)].map(m => m[1]);
  
  for (const s of scriptMatches) {
    const res = await fetch('https://app.wyvern.chat' + s);
    const txt = await res.text();
    if (txt.includes('LorebookCard') || txt.includes('bookmarked-lorebooks')) {
      console.log('Match LorebookCard in:', s);
      let idx = 0;
      while ((idx = txt.indexOf('bookmark', idx)) !== -1) {
        console.log(txt.substring(Math.max(0, idx - 100), Math.min(txt.length, idx + 200)));
        console.log('---');
        idx += 20;
      }
    }
  }
}

inspectLorebookCard();
