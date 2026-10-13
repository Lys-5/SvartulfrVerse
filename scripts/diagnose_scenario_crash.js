const fs = require('fs');

async function run() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };

  // Fetch full scenarios list
  let r = await fetch('https://app.wyvern.chat/api/worlds/scenarios/world/_CgYT8fHXpDC4crjmegQF7', { headers });
  let list = await r.json();
  let s3 = list.find(s => s.id === '_p1Ffq22CTwVywz1CFQBfF');
  
  // Save full snapshot of s3 before doing any test!
  fs.writeFileSync('scratch/scenario_3_backup.json', JSON.stringify(s3, null, 2));
  console.log('Backed up s3 to scratch/scenario_3_backup.json');

  // Let's inspect fields that might have bad IDs:
  console.log('location_id:', s3.location_id || s3.location?.id);
  console.log('environment_id:', s3.environment_id || s3.environment?.id);
  console.log('playable_character_ids:', s3.playable_character_ids);
  console.log('included_character_pool:', s3.included_character_pool?.length);
  if (s3.included_character_pool) {
    console.log('pool IDs:', s3.included_character_pool.map(x => x.character_id));
  }
  console.log('startup_script_id:', s3.startup_script_id);
  console.log('premade_scenes:', s3.premade_scenes?.length);
  if (s3.premade_scenes) {
    console.log('scenes:', s3.premade_scenes.map(x => ({ id: x.id, len: x.description?.length })));
  }
}

run().catch(console.error);
