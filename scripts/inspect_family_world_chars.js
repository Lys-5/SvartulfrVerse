const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  const res = await fetch(`https://app.wyvern.chat/api/worlds/characters/world/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const chars = await res.json();
  const names = ['jasper', 'malachia', 'noah', 'erik', 'wulfnic', 'edric', 'nixara'];
  const targets = chars.filter(c => names.some(n => (c.display_name || '').toLowerCase().includes(n) || (c.first_name || '').toLowerCase().includes(n)));
  console.log(`Found family members in World: ${targets.length}`);
  targets.forEach(c => {
    console.log(` - ${c.display_name} (${c.id}) | first: ${c.first_name} | middle: ${JSON.stringify(c.middle_names)} | last: ${c.last_name}`);
  });
  fs.writeFileSync('scratch/pre_update_family_world_chars.json', JSON.stringify(targets, null, 2));
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
