const fs = require('fs');

async function run() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };

  // Fetch world characters
  let r = await fetch('https://app.wyvern.chat/api/worlds/characters/world/_CgYT8fHXpDC4crjmegQF7', { headers });
  let worldChars = await r.json();
  const validCharMap = new Map();
  for (let c of worldChars) {
    validCharMap.set(c.id, c.display_name || c.name);
  }
  console.log('Total world characters:', validCharMap.size);

  const s3 = JSON.parse(fs.readFileSync('scratch/scenario_3_backup.json', 'utf8'));
  const pool = s3.included_character_pool || [];
  console.log('Scenario pool has:', pool.length, 'entries');

  for (let item of pool) {
    const id = item.character_id;
    const exists = validCharMap.has(id);
    console.log(`Pool char ${id}: ${exists ? 'EXISTS (' + validCharMap.get(id) + ')' : 'MISSING / INVALID!'}`);
  }
}

run().catch(console.error);
