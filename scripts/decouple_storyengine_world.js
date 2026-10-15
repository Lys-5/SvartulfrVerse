const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();
const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';

async function decoupleStoryEngine() {
  console.log(`1. Fetching StoryEngine "${engineId}"...`);
  const res = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (!res.ok) throw new Error('Fetch failed: ' + res.status);
  const eng = await res.json();
  console.log(`Found "${eng.name}" (version: v${eng.version})`);
  console.log('Current definition.worlds:', eng.definition?.worlds);
  console.log('Current definition.lorebooks:', eng.definition?.lorebooks);

  // Snapshot before changes
  fs.writeFileSync('scratch/pre_decouple_engine.json', JSON.stringify(eng, null, 2), 'utf8');

  console.log('2. Decoupling worlds and lorebooks from internal engine definition...');
  const updatedDef = {
    ...eng.definition,
    worlds: [],
    lorebooks: []
  };

  const patchPayload = {
    expected_version: eng.version,
    name: eng.name,
    tagline: eng.tagline,
    description: eng.description,
    avatar: eng.avatar,
    tags: eng.tags,
    rating: eng.rating,
    visibility: eng.visibility,
    status: eng.status,
    definition: updatedDef
  };

  console.log('3. Sending PUT to StoryEngine API...');
  const putRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(patchPayload)
  });

  if (!putRes.ok) {
    throw new Error('PUT failed: ' + putRes.status + ' ' + await putRes.text());
  }

  const updatedEng = await putRes.json();
  console.log(`[OK] StoryEngine updated! New version: v${updatedEng.version}`);

  console.log('4. Publishing new StoryEngine revision...');
  const pubRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}/publish`, {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ expected_version: updatedEng.version })
  });

  if (!pubRes.ok) {
    console.warn('Publish warning:', pubRes.status, await pubRes.text());
  } else {
    const pubData = await pubRes.json();
    console.log(`[OK] Published revision: ${pubData.published_revision_id || 'success'}`);
  }

  // Verify fresh state
  console.log('5. Verifying fresh GET state...');
  const vRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const vData = await vRes.json();
  console.log('Verified definition.worlds:', vData.definition?.worlds);
  console.log('Verified definition.lorebooks:', vData.definition?.lorebooks);
}

decoupleStoryEngine().catch(console.error);
