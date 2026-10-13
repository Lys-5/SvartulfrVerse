const fs = require('fs');

async function fixAndTest() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };

  // 1. Clear phantom default_inventory on Malachia, Zefir, Ut (and ensure Jasper is clear)
  const fixChars = [
    { id: '_rAcN9GXD1Le4WxY28e49W', name: 'Malachia' },
    { id: '_FJhtBq4xUM4aUWpaJAPYF', name: 'Zefir' },
    { id: '_NYtBzeKNkm3pedHMnYaka', name: 'Ut' },
    { id: '_x3VY2kcbaDbKyCqywGeET', name: 'Jasper' }
  ];

  for (let c of fixChars) {
    let r = await fetch(`https://app.wyvern.chat/api/worlds/characters/${c.id}`, {
      method: 'PUT',
      headers,
      body: JSON.stringify({ default_inventory: [] })
    });
    console.log(`Cleared default_inventory on ${c.name} (${c.id}): status ${r.status}`);
  }

  // 2. Fetch all current world character IDs
  let rWorldChars = await fetch('https://app.wyvern.chat/api/worlds/characters/world/_CgYT8fHXpDC4crjmegQF7', { headers });
  let worldChars = await rWorldChars.json();
  const validIds = new Set(worldChars.map(c => c.id));

  // 3. Read original s3 scenario backup
  const s3 = JSON.parse(fs.readFileSync('scratch/scenario_3_backup.json', 'utf8'));

  // Filter pool to valid characters
  const cleanPool = (s3.included_character_pool || []).filter(item => validIds.has(item.character_id));
  const cleanResolved = (s3.resolved_characters || []).filter(item => validIds.has(item.id));

  console.log(`Setting Scenario 3 pool to ${cleanPool.length} characters (all valid and cleaned)...`);
  let putScRes = await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
    method: 'PUT',
    headers,
    body: JSON.stringify({
      included_character_pool: cleanPool,
      resolved_characters: cleanResolved
    })
  });
  console.log('PUT Scenario 3 status:', putScRes.status);

  // 4. Test creating world chat log for Scenario 3 (both with and without party!)
  console.log('\n--- Test 1: Scenario 3 WITHOUT world_party_id ---');
  let test1 = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      world_id: '_CgYT8fHXpDC4crjmegQF7',
      scenario_id: '_p1Ffq22CTwVywz1CFQBfF'
    })
  });
  console.log('Status Test 1:', test1.status);
  let txt1 = await test1.text();
  console.log('Response Test 1:', txt1.slice(0, 150));

  console.log('\n--- Test 2: Full wizard payload (as sent from browser wizard) ---');
  const fullPayload = {
    world_id: '_CgYT8fHXpDC4crjmegQF7',
    scenario_id: '_p1Ffq22CTwVywz1CFQBfF',
    greeting_id: 'scene-alyssa-story-1-1',
    name: 'Svartulfr Chat',
    field_values: {
      'field-secondary-sex': 'omega',
      'field-origin': 'pack_douglas',
      'field-pack-role': 'medical_support'
    },
    persona_id: 'persona_1786335754946'
  };
  let test2 = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify(fullPayload)
  });
  console.log('Status Test 2:', test2.status);
  let txt2 = await test2.text();
  console.log('Response Test 2:', txt2.slice(0, 150));
}

fixAndTest().catch(console.error);
