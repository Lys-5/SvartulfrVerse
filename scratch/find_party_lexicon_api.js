const fs = require('fs');

(async () => {
  const html = await (await fetch('https://app.wyvern.chat/')).text();
  const chunks = [...new Set([...html.matchAll(/\/static\/chunks\/([a-zA-Z0-9_\.-]+\.js)/g)].map(m => m[1]))];
  for (const c of chunks) {
    try {
      const res = await fetch('https://app.wyvern.chat/_next/static/chunks/' + c);
      if (res.ok) {
        const text = await res.text();
        if (text.includes('/parties/') && text.includes('lexicon')) {
          console.log(`Chunk ${c} has /parties/ and lexicon!`);
          const matches = [...text.matchAll(/.{0,80}\/parties\/[^"'`\s]+.{0,80}/g)].map(m => m[0]);
          matches.forEach(m => console.log('  ', m));
        }
      }
    } catch(e) {}
  }
})();
