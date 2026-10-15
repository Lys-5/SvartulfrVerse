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
  const headers = { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' };

  // 1. Create CL from bad party
  const clBad = await (await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify({ world_id: '_CgYT8fHXpDC4crjmegQF7', world_party_id: '_c8Hpj4Mq2pGYkNHzP3RRX' })
  })).json();

  // 2. Create CL from clean party
  const clClean = await (await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify({ world_id: '_CgYT8fHXpDC4crjmegQF7', world_party_id: '_Ly7XJLQDGL6xf2P9DK7V9' })
  })).json();

  console.log('clBad:', clBad.id, 'clClean:', clClean.id);

  // Fetch full details of both
  const badDoc = await (await fetch('https://app.wyvern.chat/api/new/chat-logs/' + clBad.id, { headers: { 'Authorization': 'Bearer ' + jwt } })).json();
  const cleanDoc = await (await fetch('https://app.wyvern.chat/api/new/chat-logs/' + clClean.id, { headers: { 'Authorization': 'Bearer ' + jwt } })).json();

  fs.writeFileSync('scratch/cl_bad_fresh.json', JSON.stringify(badDoc, null, 2));
  fs.writeFileSync('scratch/cl_clean_fresh.json', JSON.stringify(cleanDoc, null, 2));
  console.log('Saved cl_bad_fresh.json and cl_clean_fresh.json');

  // Clean up both immediately
  await fetch('https://app.wyvern.chat/api/new/chat-logs/' + clBad.id, { method: 'DELETE', headers });
  await fetch('https://app.wyvern.chat/api/new/chat-logs/' + clClean.id, { method: 'DELETE', headers });
  console.log('Cleaned up both diagnostic chat logs.');
})();
