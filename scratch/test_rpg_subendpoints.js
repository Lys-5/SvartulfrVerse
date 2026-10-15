const fs = require('fs');

async function checkRpgEndpoints() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  const eps = [
    `https://app.wyvern.chat/api/worlds/rpg/traits/${worldId}`,
    `https://app.wyvern.chat/api/worlds/rpg/species/${worldId}`,
    `https://app.wyvern.chat/api/worlds/rpg/occupations/${worldId}`,
    `https://app.wyvern.chat/api/worlds/rpg/stats/${worldId}`
  ];

  for (const ep of eps) {
    const res = await fetch(ep, { headers: { 'Authorization': `Bearer ${token}` } });
    console.log(res.status, ep);
    if (res.ok) {
      const data = await res.json();
      console.log(' -> count:', data.length);
      if (data.length > 0) {
        console.log(' -> sample:', data[0].name, data[0].id);
      }
    }
  }
}

checkRpgEndpoints().catch(console.error);
