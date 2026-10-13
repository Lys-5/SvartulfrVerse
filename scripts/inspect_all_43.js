const fs = require('fs');

async function inspectAll43() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const res = await fetch('https://app.wyvern.chat/api/inventory/collection/characters?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const data = await res.json();
  const items = data.items || [];

  console.log(`Fetched ${items.length} bookmarked characters. Details:\n`);

  for (let i = 0; i < items.length; i++) {
    const c = items[i];
    const cid = c.id || c._id;
    const name = c.name || c.display_name;
    const creator = c.creator?.displayName || c.creator?.uid;
    const tag = (c.tagline || c.short_description || '').slice(0, 100);
    console.log(`[${i + 1}] ID: ${cid} | Name: "${name}" | Creator: ${creator}`);
    if (tag) console.log(`    Tagline: ${tag}`);
  }
}

inspectAll43();
