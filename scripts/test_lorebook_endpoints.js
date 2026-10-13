const fs = require('fs');

async function testLorebookEndpoints() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const eps = [
    '/api/lorebook',
    '/api/lorebook/mine',
    '/api/lorebooks/mine',
    '/api/user/lorebooks',
    '/api/worlds/lorebooks',
    '/api/library/lorebooks',
    '/api/bookmarked',
    '/api/bookmarks'
  ];

  for (const ep of eps) {
    const res = await fetch('https://app.wyvern.chat' + ep, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
    console.log(ep.padEnd(30), 'Status:', res.status);
    if (res.ok) {
      const data = await res.json();
      console.log('   Keys/Type:', typeof data, Object.keys(data));
      fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/lorebooks_endpoint_found.json', JSON.stringify(data, null, 2), 'utf8');
    }
  }
}

testLorebookEndpoints();
