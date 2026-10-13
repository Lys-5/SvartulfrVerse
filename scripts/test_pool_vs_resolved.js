const fs = require('fs');

async function run() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };

  async function tryCreateChat(label) {
    let r = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
      method: 'POST',
      headers,
      body: JSON.stringify({
        world_id: '_CgYT8fHXpDC4crjmegQF7',
        scenario_id: '_p1Ffq22CTwVywz1CFQBfF'
      })
    });
    console.log(label, 'Status:', r.status);
    return r.status;
  }

  // Test A: pool: [], resolved: []
  await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
    method: 'PUT', headers, body: JSON.stringify({ included_character_pool: [], resolved_characters: [] })
  });
  await tryCreateChat('A (empty pool, empty resolved)');

  // Test B: pool: [1 valid item], resolved: []
  await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
    method: 'PUT', headers, body: JSON.stringify({
      included_character_pool: [{ character_id: '_MXcEC8Y6B3BNm3b1ttHj6', participation_weight: 50 }],
      resolved_characters: []
    })
  });
  await tryCreateChat('B (1 char in pool, empty resolved)');

  // Test C: pool: [], resolved: [1 item]
  await fetch('https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF', {
    method: 'PUT', headers, body: JSON.stringify({
      included_character_pool: [],
      resolved_characters: [{ id: '_MXcEC8Y6B3BNm3b1ttHj6', display_name: 'Alyssa' }]
    })
  });
  await tryCreateChat('C (empty pool, 1 resolved)');
}

run().catch(console.error);
