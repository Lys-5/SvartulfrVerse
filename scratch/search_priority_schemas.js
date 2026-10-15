const fs = require('fs');

async function run() {
  const r = await fetch('https://app.wyvern.chat/mine');
  const html = await r.text();
  const scriptRegex = /src="([^"]+\.js)"/g;
  let match;
  const scripts = [];
  while ((match = scriptRegex.exec(html)) !== null) {
    scripts.push(match[1]);
  }
  console.log('Total scripts to search:', scripts.length);

  for (const s of scripts) {
    const url = s.startsWith('http') ? s : 'https://app.wyvern.chat' + s;
    try {
      const res = await fetch(url);
      if (!res.ok) continue;
      const txt = await res.text();
      const matches = txt.match(/priority\s*:\s*[a-zA-Z0-9_\.\(\)]+/g);
      if (matches) {
        const filtered = matches.filter(m => !m.includes('!0') && !m.includes('!1') && !m.includes('true') && !m.includes('false'));
        if (filtered.length > 0) {
          console.log('\n================================');
          console.log('Script:', url);
          console.log('Matches:', filtered);
          for (const m of filtered) {
            const idx = txt.indexOf(m);
            console.log('Snippet for ' + m + ':\n', txt.slice(Math.max(0, idx - 80), Math.min(txt.length, idx + 120)));
          }
        }
      }
    } catch (e) {}
  }
}
run();
