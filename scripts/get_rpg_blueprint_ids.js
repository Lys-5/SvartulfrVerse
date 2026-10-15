const fs = require('fs');

async function getRpgBlueprints() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  const res = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const data = await res.json();
  const statConfig = data.stat_config || {};

  console.log('=== RPG SPECIES ===');
  (statConfig.species || []).forEach(s => console.log(`${s.id} -> "${s.name}"`));

  console.log('\n=== RPG OCCUPATIONS ===');
  (statConfig.occupations || []).forEach(o => console.log(`${o.id} -> "${o.name}"`));

  console.log('\n=== RPG TRAITS ===');
  (statConfig.character_traits || []).forEach(t => console.log(`${t.id} -> "${t.name}"`));
}

getRpgBlueprints();
