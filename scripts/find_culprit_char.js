const fs = require('fs');

async function run() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };

  const s3 = JSON.parse(fs.readFileSync('scratch/scenario_3_backup.json', 'utf8'));
  const pool = s3.included_character_pool || [];

  for (let item of pool) {
    // Put single char
    await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
      method: 'PUT',
      headers,
      body: JSON.stringify({
        included_character_pool: [item],
        resolved_characters: []
      })
    });

    let res = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
      method: 'POST',
      headers,
      body: JSON.stringify({
        world_id: '_CgYT8fHXpDC4crjmegQF7',
        scenario_id: '_p1Ffq22CTwVywz1CFQBfF'
      })
    });
    console.log(`Char ${item.character_id}: Status ${res.status}`);
  }
}

run().catch(console.error);
