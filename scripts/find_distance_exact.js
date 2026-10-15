const fs = require('fs');

async function searchExact() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const pageRes = await fetch('https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7', {
    headers: { 'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0' }
  });
  const html = await pageRes.text();
  const chunkUrls = [...html.matchAll(/"(\/_next\/static\/chunks\/[^"]+\.js)"/g)].map(m => m[1]);
  console.log('Total page chunks:', chunkUrls.length);

  for (const u of chunkUrls) {
    const res = await fetch('https://app.wyvern.chat' + u);
    const text = await res.text();
    if (text.includes('Distance (flavor)')) {
      console.log('FOUND in:', u);
      const p = text.indexOf('Distance (flavor)');
      console.log(text.slice(Math.max(0, p - 200), p + 400));
      return;
    }
  }
  console.log('Not found in initial page chunks, checking dynamic chunks...');
}

searchExact().catch(console.error);
