const fs = require('fs');

async function testInventory() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  
  const urls = [
    'https://api.wyvern.chat/api/inventory',
    'https://api.wyvern.chat/api/inventory/ids',
    'https://api.wyvern.chat/api/inventory/collection/lorebooks',
    'https://app.wyvern.chat/api/inventory',
    'https://app.wyvern.chat/api/inventory/ids',
    'https://app.wyvern.chat/api/inventory/collection/lorebooks'
  ];

  for (const u of urls) {
    const res = await fetch(u, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
    console.log(u, res.status);
    if (res.ok) {
      const data = await res.json();
      console.log('  -> Success!', Object.keys(data).slice(0, 5));
      if (data.items) {
        console.log('     Items count:', data.items.length);
        data.items.slice(0, 10).forEach(i => console.log('       *', i.id, '|', i.name || i.title));
      } else if (Array.isArray(data)) {
        console.log('     Array length:', data.length);
      }
    }
  }
}

testInventory();
