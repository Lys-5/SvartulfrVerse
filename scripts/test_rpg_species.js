const fs = require('fs');

async function testRpgEndpoints() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token };
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  const res = await fetch(`https://app.wyvern.chat/api/worlds/rpg/species/${worldId}`, { headers });
  console.log('GET species status:', res.status);
  if (res.ok) {
    const list = await res.json();
    console.log(`Found ${list.length} RPG species:`);
    list.forEach((s, i) => {
      console.log(`[${i}] id=${s.id}, name="${s.name}", desc="${s.description?.slice(0, 30)}", mods=${JSON.stringify(s.stat_modifiers)}`);
    });
  }
}

testRpgEndpoints().catch(console.error);
