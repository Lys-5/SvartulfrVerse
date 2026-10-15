const fs = require('fs');

async function refreshToken() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rt = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt', 'utf8').trim();
  const res = await fetch(`https://securetoken.googleapis.com/v1/token?key=${ak}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grant_type: 'refresh_token', refresh_token: rt })
  });
  const data = await res.json();
  return data.id_token;
}

async function run() {
  const token = await refreshToken();
  const headers = { 'Authorization': 'Bearer ' + token };

  for (const id of ['_A9AdcMYm6WRckp9XnqT3Y', '_baf4QmNYp3DXb6wDkG7Wb']) {
    const res = await fetch(`https://app.wyvern.chat/api/worlds/characters/${id}`, { headers });
    console.log('Fetch', id, 'status:', res.status);
    if (res.ok) {
      const char = await res.json();
      console.log('Character:', char.display_name || char.name, '(' + id + ')');
      console.log('Keys:', Object.keys(char));
      function findPriority(obj, path = '') {
        if (!obj || typeof obj !== 'object') return;
        for (const [k, v] of Object.entries(obj)) {
          const cur = path ? path + '.' + k : k;
          if (k.toLowerCase().includes('priority')) {
            console.log(`  MATCH at ${cur}: typeof=${typeof v}, val=${JSON.stringify(v)}`);
          }
          if (typeof v === 'object') {
            findPriority(v, cur);
          }
        }
      }
      findPriority(char);
      if (char.character_traits) {
        console.log('  Traits:', char.character_traits);
      }
      if (char.rpg_stats) {
        console.log('  RPG Stats:', char.rpg_stats);
      }
    }
  }
}
run();
