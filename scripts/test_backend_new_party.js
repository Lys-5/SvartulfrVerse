const fs = require('fs');

async function testBackend() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
  };

  const payload = {
    world_id: "_CgYT8fHXpDC4crjmegQF7",
    scenario_id: "_p1Ffq22CTwVywz1CFQBfF",
    name: "Test New Party Chat"
  };

  console.log('--- Test A: Minimal without party or persona ---');
  let r = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST', headers, body: JSON.stringify(payload)
  });
  console.log('Status A:', r.status, await r.text());

  console.log('--- Test B: Minimal world_id only ---');
  r = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST', headers, body: JSON.stringify({ world_id: "_CgYT8fHXpDC4crjmegQF7" })
  });
  console.log('Status B:', r.status, await r.text());

  // What about other worlds? Does it happen on other worlds?
  // Let's check public worlds or user worlds
  let worldsRes = await fetch('https://app.wyvern.chat/api/worlds/user', { headers });
  console.log('Worlds res:', worldsRes.status);
  let worlds = await worldsRes.json();
  console.log('User worlds:', worlds.map(w => ({ id: w.id, name: w.name })));
}

testBackend().catch(console.error);
