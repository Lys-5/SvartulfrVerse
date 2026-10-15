const fs = require('fs');

async function search() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const buildManifestRes = await fetch('https://app.wyvern.chat/_next/static/development/_buildManifest.js').catch(() => null);
  // Get main page HTML for world edit
  const pageRes = await fetch('https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7', {
    headers: {
      'Authorization': 'Bearer ' + token,
      'User-Agent': 'Mozilla/5.0'
    }
  });
  const html = await pageRes.text();
  const matches = [...html.matchAll(/\/([a-zA-Z0-9_\-\.\/]+\.js)/g)].map(m => m[0]);
  const uniqueUrls = [...new Set(matches)].filter(u => u.includes('/_next/static/chunks/'));
  console.log('Found chunks in world edit page:', uniqueUrls.length);

  for (const u of uniqueUrls) {
    const fullUrl = 'https://app.wyvern.chat' + u;
    const res = await fetch(fullUrl);
    const text = await res.text();
    if (text.includes('Distance') || text.includes('flavor') || text.includes('travel_time') || text.includes('Free Travel')) {
      console.log('MATCH IN:', u);
      const idxs = ['Distance (flavor)', 'Free Travel', 'Required Mediums', 'travel_time'];
      for (const k of idxs) {
        const p = text.indexOf(k);
        if (p !== -1) {
          console.log(`--- [${k}] in ${u} ---`);
          console.log(text.slice(Math.max(0, p - 150), p + 250));
        }
      }
    }
  }
}

search().catch(console.error);
