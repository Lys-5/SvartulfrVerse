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
  // Create chat log
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
  
  // Send message
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
    console.log(`  -> Error: ${errText.slice(0, 200)}`);
  }
  
  // Teardown: delete the test chat log immediately
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

  console.log('--- 1. Baseline test on clean party ---');
  await testParty(jwt, cleanId, 'baseline clean');

  console.log('\n--- 2. Testing attached_lorebook_ids ---');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ attached_lorebook_ids: bad.attached_lorebook_ids })
  });
  await testParty(jwt, cleanId, 'attached_lorebook_ids');
  // reset
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ attached_lorebook_ids: [] })
  });

  console.log('\n--- 3. Testing current_location_id (_RNU9Fx2pLD6PJ8LcKAdg6) ---');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ current_location_id: '_RNU9Fx2pLD6PJ8LcKAdg6' })
  });
  await testParty(jwt, cleanId, 'current_location_id');
  // reset
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ current_location_id: null })
  });

  console.log('\n--- 4. Testing linked_characters ---');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ linked_characters: bad.linked_characters })
  });
  await testParty(jwt, cleanId, 'linked_characters');
  // reset
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ linked_characters: [] })
  });

  console.log('\n--- 5. Testing companion_supply_character_ids ---');
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ companion_supply_character_ids: bad.companion_supply_character_ids })
  });
  await testParty(jwt, cleanId, 'companion_supply_character_ids');
  // reset
  await fetch(`https://app.wyvern.chat/api/worlds/parties/${cleanId}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ companion_supply_character_ids: [] })
  });
})();
