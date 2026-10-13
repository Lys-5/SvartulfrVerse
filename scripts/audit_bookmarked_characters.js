const fs = require('fs');

async function listBookmarkedCharacters() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const res = await fetch('https://app.wyvern.chat/api/inventory/collection/characters?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const data = await res.json();
  const items = data.items || [];
  console.log('Total bookmarked characters:', items.length);
  items.forEach((c, idx) => {
    const name = c.name || c.display_name || 'Unnamed';
    const creator = c.creator?.displayName || c.creator?.uid || 'Unknown';
    console.log(`${idx + 1}. [${c.id || c._id}] "${name}" (creator: ${creator})`);
  });
}

listBookmarkedCharacters();
