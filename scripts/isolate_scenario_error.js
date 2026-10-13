const fs = require('fs');

async function run() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };

  // Read backup
  const s3 = JSON.parse(fs.readFileSync('scratch/scenario_3_backup.json', 'utf8'));

  async function tryCreateChat() {
    let r = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
      method: 'POST',
      headers,
      body: JSON.stringify({
        world_id: '_CgYT8fHXpDC4crjmegQF7',
        scenario_id: '_p1Ffq22CTwVywz1CFQBfF'
      })
    });
    let txt = await r.text();
    return { status: r.status, txt };
  }

  // Test 1: included_character_pool: []
  console.log('Testing with included_character_pool: []...');
  let putRes = await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
    method: 'PUT',
    headers,
    body: JSON.stringify({ included_character_pool: [] })
  });
  console.log('PUT pool:[] status:', putRes.status);
  
  let chatRes = await tryCreateChat();
  console.log('Chat status with empty pool:', chatRes.status, chatRes.txt.slice(0, 100));

  // If that fixed it, we know it's in included_character_pool!
  // If not, test next: insertion_point: 0
  if (chatRes.status !== 200) {
    console.log('\nTesting with insertion_point: 0...');
    await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
      method: 'PUT',
      headers,
      body: JSON.stringify({ insertion_point: 0 })
    });
    chatRes = await tryCreateChat();
    console.log('Chat status with insertion_point 0:', chatRes.status, chatRes.txt.slice(0, 100));
  }

  // If still not, test max_number_of_characters: 6
  if (chatRes.status !== 200) {
    console.log('\nTesting with max_number_of_characters: 6...');
    await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
      method: 'PUT',
      headers,
      body: JSON.stringify({ max_number_of_characters: 6 })
    });
    chatRes = await tryCreateChat();
    console.log('Chat status with max_chars 6:', chatRes.status, chatRes.txt.slice(0, 100));
  }

  // Restore s3 original fields
  console.log('\nRestoring original fields...');
  await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
    method: 'PUT',
    headers,
    body: JSON.stringify({
      included_character_pool: s3.included_character_pool,
      insertion_point: s3.insertion_point,
      max_number_of_characters: s3.max_number_of_characters
    })
  });
  console.log('Restored!');
}

run().catch(console.error);
