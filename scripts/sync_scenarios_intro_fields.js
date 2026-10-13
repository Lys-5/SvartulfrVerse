const fs = require('fs');

async function syncScenariosIntroFields() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
  };

  // 1. Fetch current world
  console.log('Fetching World _CgYT8fHXpDC4crjmegQF7...');
  const worldRes = await fetch('https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7', { headers });
  if (!worldRes.ok) {
    throw new Error('Failed to fetch world: ' + worldRes.status);
  }
  const world = await worldRes.json();
  const introFields = world.intro_fields;
  console.log('World intro_fields count:', Object.keys(introFields).length);
  console.log('Keys:', Object.keys(introFields));

  // 2. Fetch all scenarios
  const scenariosRes = await fetch('https://app.wyvern.chat/api/worlds/scenarios/world/_CgYT8fHXpDC4crjmegQF7', { headers });
  const scenarios = await scenariosRes.json();
  console.log(`Found ${scenarios.length} scenarios.`);

  const snapshot = {};

  for (const sc of scenarios) {
    console.log(`\nProcessing Scenario: [${sc.id}] ${sc.name}`);
    snapshot[sc.id] = sc;

    // Partial PUT
    const putRes = await fetch(`https://app.wyvern.chat/api/worlds/scenarios/${sc.id}`, {
      method: 'PUT',
      headers,
      body: JSON.stringify({
        fields: introFields
      })
    });

    console.log(`PUT Status: ${putRes.status}`);
    if (!putRes.ok) {
      const errText = await putRes.text();
      console.error(`PUT Error: ${errText}`);
      continue;
    }

    // Verify GET
    const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/scenarios/${sc.id}`, { headers });
    const verifyData = await verifyRes.json();
    console.log(`Verified fields count: ${Object.keys(verifyData.fields || {}).length}`);
    if (verifyData.fields && verifyData.fields['field-species']) {
      console.log(`SUCCESS: Scenario ${sc.id} has field-species with ${verifyData.fields['field-species'].options?.length} options.`);
    } else {
      console.error(`FAILURE: Scenario ${sc.id} missing field-species!`);
    }
  }

  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/scenarios_fields_snapshot.json', JSON.stringify(snapshot, null, 2), 'utf8');
  console.log('\nSnapshot saved to scratch/scenarios_fields_snapshot.json');
}

syncScenariosIntroFields().catch(console.error);
