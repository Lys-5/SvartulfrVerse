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

  console.log('Fetching Location _RNU9Fx2pLD6PJ8LcKAdg6...');
  const res = await fetch('https://app.wyvern.chat/api/worlds/locations/_RNU9Fx2pLD6PJ8LcKAdg6', { headers });
  console.log('Status:', res.status);
  if (res.ok) {
    const loc = await res.json();
    console.log('Loc Name:', loc.name);
    console.log('Loc Keys:', Object.keys(loc));
    function findPriority(obj, path = '') {
      if (!obj || typeof obj !== 'object') return;
      for (const [k, v] of Object.entries(obj)) {
        const cur = path ? path + '.' + k : k;
        if (k.toLowerCase().includes('priority')) {
          console.log(`MATCH at ${cur}: typeof=${typeof v}, val=${JSON.stringify(v)}`);
        }
        if (typeof v === 'object') {
          findPriority(v, cur);
        }
      }
    }
    findPriority(loc);
    console.log('Included entries:', (loc.included_lexicon_entries || []).length);
    console.log('Characters present:', (loc.characters_present || []).length);
    console.log('Characters:', loc.characters_present);
  }
}
run();
