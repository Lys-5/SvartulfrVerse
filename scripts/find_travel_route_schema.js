const fs = require('fs');

async function findSchema() {
  const htmlRes = await fetch('https://app.wyvern.chat', {
    headers: { 'User-Agent': 'Mozilla/5.0' }
  });
  const html = await htmlRes.text();
  const scriptRegex = /src="(\/_next\/static\/chunks\/[^"]+\.js)"/g;
  let match;
  const scriptUrls = [];
  while ((match = scriptRegex.exec(html)) !== null) {
    scriptUrls.push('https://app.wyvern.chat' + match[1]);
  }
  console.log('Found chunks in index:', scriptUrls.length);

  for (const url of scriptUrls) {
    const res = await fetch(url);
    const text = await res.text();
    if (text.includes('Distance (flavor)') || text.includes('travel_routes') || text.includes('Required Mediums')) {
      console.log('MATCH IN CHUNK:', url);
      const idx = text.indexOf('Distance (flavor)');
      if (idx !== -1) {
        console.log('Context around Distance (flavor):');
        console.log(text.slice(Math.max(0, idx - 200), idx + 200));
      }
      const idx2 = text.indexOf('travel_routes');
      if (idx2 !== -1) {
        console.log('Context around travel_routes:');
        console.log(text.slice(Math.max(0, idx2 - 150), idx2 + 150));
      }
    }
  }
}

findSchema().catch(console.error);
