const fs = require('fs');

async function searchAllChunks() {
  const r = await fetch('https://app.wyvern.chat/mine');
  const html = await r.text();
  const scriptMatches = [...html.matchAll(/src="(\/_next\/static\/chunks\/[^"]+\.js)"/g)].map(m => m[1]);
  
  for (const s of scriptMatches) {
    const res = await fetch('https://app.wyvern.chat' + s);
    const txt = await res.text();
    if (txt.includes('collection/lorebooks')) {
      console.log('Match in:', s);
      let idx = 0;
      while ((idx = txt.indexOf('collection/lorebooks', idx)) !== -1) {
        console.log(txt.substring(Math.max(0, idx - 200), Math.min(txt.length, idx + 400)));
        console.log('-------------------------------------------');
        idx += 20;
      }
    }
  }
}

searchAllChunks();
