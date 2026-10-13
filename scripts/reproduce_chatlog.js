const fs = require('fs');

async function reproduceChatLogCreation() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
  };

  // Exact payload extracted from draftState
  const basePayload = {
    world_id: "_CgYT8fHXpDC4crjmegQF7",
    world_party_id: "_c8Hpj4Mq2pGYkNHzP3RRX",
    scenario_id: "_p1Ffq22CTwVywz1CFQBfF",
    greeting_id: "scene-alyssa-story-1-1",
    name: "Svartulfr Chat",
    field_values: {
      "field-secondary-sex": "omega",
      "field-origin": "pack_douglas",
      "field-pack-role": "medical_support"
    },
    persona_id: "persona_1786335754946"
  };

  console.log('--- TEST 1: Full payload as sent by browser ---');
  let res = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify(basePayload)
  });
  console.log('Status 1:', res.status, await res.text());

  // Test 2: Without persona_id
  console.log('\n--- TEST 2: Without persona_id ---');
  const p2 = { ...basePayload };
  delete p2.persona_id;
  res = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify(p2)
  });
  console.log('Status 2:', res.status, await res.text());

  // Test 3: With player_world_character_id instead of persona_id
  console.log('\n--- TEST 3: With player_world_character_id (_MXcEC8Y6B3BNm3b1ttHj6) ---');
  const p3 = { ...basePayload, player_world_character_id: "_MXcEC8Y6B3BNm3b1ttHj6" };
  delete p3.persona_id;
  res = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify(p3)
  });
  console.log('Status 3:', res.status, await res.text());

  // Test 4: Without world_party_id
  console.log('\n--- TEST 4: Without world_party_id ---');
  const p4 = { ...basePayload };
  delete p4.world_party_id;
  res = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify(p4)
  });
  console.log('Status 4:', res.status, await res.text());
}

reproduceChatLogCreation().catch(console.error);
