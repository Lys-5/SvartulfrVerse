const fs = require('fs');

async function inspectUserPersonas() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token };

  const endpoints = [
    'https://app.wyvern.chat/api/users/personas',
    'https://app.wyvern.chat/api/personas',
    'https://app.wyvern.chat/api/users/me',
    'https://app.wyvern.chat/api/users/profile'
  ];

  for (const ep of endpoints) {
    try {
      const res = await fetch(ep, { headers });
      console.log(`${ep} -> Status: ${res.status}`);
      if (res.ok) {
        const data = await res.json();
        console.log('   Data:', JSON.stringify(data).slice(0, 300));
      }
    } catch(e) {
      console.error(ep, e.message);
    }
  }
}

inspectUserPersonas().catch(console.error);
