const fs = require('fs');

async function findBookmarkLogic() {
  const r = await fetch('https://app.wyvern.chat/mine');
  const html = await r.text();
  const scriptMatches = [...html.matchAll(/src="(\/_next\/static\/chunks\/[^"]+\.js)"/g)].map(m => m[1]);
  
  for (const s of scriptMatches) {
    const res = await fetch('https://app.wyvern.chat' + s);
    const txt = await res.text();
    if (txt.includes('bookmarked-lorebooks')) {
      console.log('Match bookmarked-lorebooks in:', s);
      let idx = 0;
      while ((idx = txt.indexOf('bookmarked-lorebooks', idx)) !== -1) {
        console.log(txt.substring(Math.max(0, idx - 150), Math.min(txt.length, idx + 350)));
        console.log('-------------------------------------------');
        idx += 20;
      }
    }
  }
}

findBookmarkLogic();
