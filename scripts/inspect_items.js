const fs = require('fs');

async function checkItemEntries() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const res = await fetch('https://app.wyvern.chat/api/worlds/lexicon/world/' + worldId, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const list = await res.json();
  const items = list.filter(e => e.type === 'item');
  console.log('Total items in World Lexicon:', items.length);
  items.forEach((it, i) => {
    console.log(`${i + 1}. [${it.id}] name: "${it.name}" | keys: ${JSON.stringify(it.keys)}`);
  });

  // Verifichiamo anche se ci sono endpoint dedicati agli items in rpg
  const rpgRes = await fetch('https://app.wyvern.chat/api/worlds/rpg/items/' + worldId, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  console.log('/api/worlds/rpg/items status:', rpgRes.status);
  if (rpgRes.ok) {
    const rpgItems = await rpgRes.json();
    console.log('rpgItems count:', rpgItems.length);
    console.log('Sample rpgItem:', rpgItems[0]);
  }
}

checkItemEntries().catch(err => {
  console.error(err);
  process.exit(1);
});
