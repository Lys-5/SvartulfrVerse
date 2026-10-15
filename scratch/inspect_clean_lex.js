const fs = require('fs');
async function getJwt() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rt = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt', 'utf8').trim();
  const res = await fetch('https://securetoken.googleapis.com/v1/token?key=' + ak, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grant_type: 'refresh_token', refresh_token: rt })
  });
  const data = await res.json();
  return data.id_token;
}

(async () => {
  const jwt = await getJwt();
  const headers = { 'Authorization': 'Bearer ' + jwt };

  const rClean = await fetch('https://app.wyvern.chat/api/worlds/parties/_Ly7XJLQDGL6xf2P9DK7V9/lexicon', { headers });
  const cleanData = await rClean.json();
  console.log('Clean entries count:', cleanData.length);
  for (const e of cleanData.slice(0, 10)) {
    console.log(`- ${e.name} | type=${e.type} | is_global=${e.is_global}`);
  }
})();
