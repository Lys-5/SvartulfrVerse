const fs = require('fs');

async function findBookmarkAPI() {
  const r = await fetch('https://app.wyvern.chat/mine');
  const html = await r.text();
  const scriptMatches = [...html.matchAll(/src="(\/_next\/static\/chunks\/[^"]+\.js)"/g)].map(m => m[1]);
  console.log('Found scripts:', scriptMatches.length);
  for (const s of scriptMatches) {
    const sr = await fetch('https://app.wyvern.chat' + s);
    const txt = await sr.text();
    if (txt.includes('collection/lorebooks') || txt.includes('/api/inventory/') || txt.includes('bookmarked')) {
      console.log('\n--- Script matches:', s, '---');
      let idx = 0;
      while ((idx = txt.indexOf('collection/lorebooks', idx)) !== -1) {
        console.log('Snippet near collection/lorebooks:');
        console.log(txt.substring(Math.max(0, idx - 150), Math.min(txt.length, idx + 250)));
        idx += 20;
      }
      let idx2 = 0;
      while ((idx2 = txt.indexOf('/api/inventory', idx2)) !== -1) {
        console.log('Snippet near /api/inventory:');
        console.log(txt.substring(Math.max(0, idx2 - 150), Math.min(txt.length, idx2 + 250)));
        idx2 += 20;
      }
    }
  }
}

findBookmarkAPI();
