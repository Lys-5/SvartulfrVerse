const fs = require('fs');

async function listAllLorebooks() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const uid = '2r4fVpvImte5dbljedLkZJxre2d2';

  // 1. Created Lorebooks
  const rCreated = await fetch(`https://app.wyvern.chat/api/lorebooks/user/${uid}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const createdData = await rCreated.json();
  const createdList = createdData.lorebooks || [];

  // 2. Bookmarked Lorebooks (from inventory collection)
  const rBookmarked = await fetch('https://app.wyvern.chat/api/inventory/collection/lorebooks?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const bookmarkedData = await rBookmarked.json();
  const bookmarkedList = bookmarkedData.items || [];

  console.log('=== LOREBOOKS CREATED (' + createdList.length + ') ===');
  createdList.forEach((l, idx) => {
    console.log(`${idx + 1}. [${l.id}] ${l.name} (${l.entries_count || (l.entries ? Object.keys(l.entries).length : '?')} entries)`);
  });

  console.log('\n=== LOREBOOKS BOOKMARKED (' + bookmarkedList.length + ') ===');
  bookmarkedList.forEach((l, idx) => {
    console.log(`${idx + 1}. [${l.id}] ${l.name} (${l.entries_count || (l.entries ? Object.keys(l.entries).length : '?')} entries)`);
  });
}

listAllLorebooks();
