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

async function testField(jwt, fieldName, value) {
  const headers = { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' };
  console.log(`\n========================================`);
  console.log(`Applying field: ${fieldName}`);

  // 1. PUT on clean party
  const putRes = await fetch('https://app.wyvern.chat/api/worlds/parties/_Ly7XJLQDGL6xf2P9DK7V9', {
    method: 'PUT',
    headers,
    body: JSON.stringify({ [fieldName]: value })
  });
  console.log(`PUT ${fieldName} status: ${putRes.status}`);
  if (!putRes.ok) {
    console.log(`PUT error:`, (await putRes.text()).slice(0, 150));
    return false;
  }

  // 2. Create fresh chat log
  const clRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      world_id: '_CgYT8fHXpDC4crjmegQF7',
      world_party_id: '_Ly7XJLQDGL6xf2P9DK7V9'
    })
  });
  const cl = await clRes.json();
  console.log(`Created CL: ${cl.id}`);

  // 3. Send message
  const msgRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      chat_log_id: cl.id,
      content: 'probe ' + fieldName,
      role: 'user'
    })
  });
  console.log(`Msg status: ${msgRes.status}`);
  const ok = msgRes.ok;
  if (!ok) {
    console.log(`FAILED with 500! FIELD ${fieldName} IS THE CAUSE!`);
    console.log(`Error:`, await msgRes.text());
  } else {
    console.log(`Msg succeeded (200 OK) with ${fieldName}`);
  }

  // 4. Cleanup chat log
  if (cl.id) {
    await fetch('https://app.wyvern.chat/api/new/chat-logs/' + cl.id, { method: 'DELETE', headers });
  }

  return !ok; // return true if it caused the failure!
}

(async () => {
  const jwt = await getJwt();
  const bad = JSON.parse(fs.readFileSync('scratch/live_bad_party.json', 'utf8'));

  const candidateFields = [
    ['player_character_importance', bad.player_character_importance],
    ['continuity_mode', bad.continuity_mode],
    ['party_note', bad.party_note],
    ['party_title', bad.party_title],
    ['party_avatar', bad.party_avatar],
    ['party_instructions', bad.party_instructions],
    ['inventory', bad.inventory],
    ['current_environment_id', bad.current_environment?.id],
    ['current_location_id', bad.current_location?.id],
    ['companion_supply_character_ids', bad.companion_supply_character_ids],
    ['memory_states', bad.memory_states],
    ['world_lexicon_entries', bad.world_lexicon_entries]
  ];

  for (const [name, val] of candidateFields) {
    const isCulprit = await testField(jwt, name, val);
    if (isCulprit) {
      console.log(`\n🎯🎯🎯 FOUND THE EXACT CAUSE: ${name}!`);
      break;
    }
  }
})();
