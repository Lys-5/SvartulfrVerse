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

async function testParty(jwt, partyId, label) {
  const clRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      world_id: '_CgYT8fHXpDC4crjmegQF7',
      world_party_id: partyId
    })
  });
  const cl = await clRes.json();
  const clId = cl.id;
  
  const msgRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_log_id: clId,
      content: 'test ping ' + label,
      role: 'user'
    })
  });
  
  console.log(`[TEST: ${label}] Msg status: ${msgRes.status}`);
  let errText = '';
  if (!msgRes.ok) {
    errText = await msgRes.text();
    console.log(`  -> Error: ${errText.slice(0, 300)}`);
  }
  
  // Teardown
  await fetch(`https://app.wyvern.chat/api/new/chat-logs/${clId}`, {
    method: 'DELETE',
    headers: { 'Authorization': 'Bearer ' + jwt }
  });
  console.log(`  -> Deleted test chat log ${clId}`);
  
  return msgRes.status === 200;
}

(async () => {
  const jwt = await getJwt();
  const bad = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/a1805fc9-c19e-4378-ac46-f9c73c1e3f96/scratch/bad_party.json', 'utf8'));
  const cleanId = '_Ly7XJLQDGL6xf2P9DK7V9';

  console.log('--- 10. Testing current_environment_id: _gNmX2qncQ6m9E4fG223ge ---');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ current_environment_id: '_gNmX2qncQ6m9E4fG223ge' })
  });
  await testParty(jwt, cleanId, 'current_environment_id');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ current_environment_id: null })
  });

  console.log('\n--- 11. Testing party_avatar ---');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ party_avatar: bad.party_avatar })
  });
  await testParty(jwt, cleanId, 'party_avatar');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ party_avatar: null })
  });

  console.log('\n--- 12. Testing current_world ---');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ current_world: bad.current_world })
  });
  await testParty(jwt, cleanId, 'current_world');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ current_world: null })
  });
})();
