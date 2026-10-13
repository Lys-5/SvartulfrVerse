const fs = require('fs');

async function testCleanPool() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };

  // Fetch world characters to have accurate set
  let r = await fetch('https://app.wyvern.chat/api/worlds/characters/world/_CgYT8fHXpDC4crjmegQF7', { headers });
  let worldChars = await r.json();
  const validIds = new Set(worldChars.map(c => c.id));

  const s3 = JSON.parse(fs.readFileSync('scratch/scenario_3_backup.json', 'utf8'));
  const cleanPool = (s3.included_character_pool || []).filter(item => validIds.has(item.character_id));
  console.log(`Original pool: ${s3.included_character_pool.length}, Clean pool: ${cleanPool.length}`);

  // Also clean resolved_characters if present!
  const cleanResolved = (s3.resolved_characters || []).filter(item => validIds.has(item.id));
  console.log(`Original resolved: ${s3.resolved_characters?.length}, Clean resolved: ${cleanResolved.length}`);

  // Update scenario with cleaned pool
  let putRes = await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
    method: 'PUT',
    headers,
    body: JSON.stringify({
      included_character_pool: cleanPool,
      resolved_characters: cleanResolved
    })
  });
  console.log('PUT clean scenario status:', putRes.status);

  // Now try to create chat log with scenario 3!
  let chatRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      world_id: '_CgYT8fHXpDC4crjmegQF7',
      scenario_id: '_p1Ffq22CTwVywz1CFQBfF'
    })
  });
  console.log('CREATE CHAT STATUS:', chatRes.status);
  let txt = await chatRes.text();
  console.log('Result:', txt.slice(0, 300));
}

testCleanPool().catch(console.error);
