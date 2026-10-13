const fs = require('fs');

async function findMineJs() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const r = await fetch('https://app.wyvern.chat/mine', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const html = await r.text();
  const scriptRegex = /src="([^"]+\.js)"/g;
  let match;
  const scripts = [];
  while ((match = scriptRegex.exec(html)) !== null) {
    scripts.push(match[1]);
  }
  console.log('Scripts found:', scripts.length);
  
  for (const s of scripts) {
    const url = s.startsWith('http') ? s : 'https://app.wyvern.chat' + s;
    const jsRes = await fetch(url);
    if (!jsRes.ok) continue;
    const jsText = await jsRes.text();
    if (jsText.includes('bookmarked') || jsText.includes('bookmark') || jsText.includes('lorebook')) {
      console.log('Match in script:', url);
      // find occurrences of /api/
      const apiMatches = jsText.match(/\/api\/[a-zA-Z0-9_\-\/]+/g) || [];
      const lorebookApis = apiMatches.filter(a => a.toLowerCase().includes('lore') || a.toLowerCase().includes('book'));
      if (lorebookApis.length > 0) {
        console.log('  Endpoints:', [...new Set(lorebookApis)]);
      }
    }
  }
}

findMineJs();
