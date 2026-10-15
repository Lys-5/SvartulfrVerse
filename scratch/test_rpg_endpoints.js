const fs = require('fs');

async function testEndpoints() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  const eps = [
    `https://app.wyvern.chat/api/worlds/${worldId}/species`,
    `https://app.wyvern.chat/api/worlds/species/world/${worldId}`,
    `https://app.wyvern.chat/api/species`,
    `https://app.wyvern.chat/api/worlds/${worldId}/occupations`,
    `https://app.wyvern.chat/api/worlds/occupations/world/${worldId}`,
    `https://app.wyvern.chat/api/occupations`,
    `https://app.wyvern.chat/api/worlds/${worldId}/traits`,
    `https://app.wyvern.chat/api/worlds/traits/world/${worldId}`,
    `https://app.wyvern.chat/api/traits`,
    `https://app.wyvern.chat/api/character-traits`,
    `https://app.wyvern.chat/api/character-traits/world/${worldId}`,
    `https://app.wyvern.chat/api/worlds/${worldId}/character-traits`
  ];

  for (const ep of eps) {
    try {
      const res = await fetch(ep, { headers: { 'Authorization': `Bearer ${token}` } });
      console.log(res.status, ep);
      if (res.ok) {
        const d = await res.json();
        console.log(' -> length/keys:', Array.isArray(d) ? `Array length ${d.length}` : Object.keys(d));
        if (Array.isArray(d) && d.length > 0) {
          console.log(' -> sample item:', d[0].name || d[0].title || d[0].display_name, d[0].id);
        }
      }
    } catch (e) {
      console.log('ERR', ep, e.message);
    }
  }
}

testEndpoints().catch(console.error);
