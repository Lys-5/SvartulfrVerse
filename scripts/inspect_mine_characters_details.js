const fs = require('fs');

async function inspectMineCharactersDetails() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const raw = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/chars_mine_raw.json', 'utf8'));

  for (const c of raw.characters) {
    const res = await fetch(`https://app.wyvern.chat/api/characters/${c.id || c._id}`, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
    if (!res.ok) {
      console.log('Error fetching', c.name, res.status);
      continue;
    }
    const d = await res.json();
    console.log('=== ' + (d.name || d.display_name) + ' (' + d.id + ') ===');
    console.log('  linked_world:', d.linked_world);
    console.log('  lorebooks count:', (d.lorebooks || []).length);
    console.log('  outfits count:', (d.outfits || []).length);
    console.log('  desc length:', (d.description || '').length);
    console.log('  personality length:', (d.personality || '').length);
    console.log('  post_history_instructions:\n   ', (d.post_history_instructions || '').slice(0, 150));
  }
}

inspectMineCharactersDetails();
