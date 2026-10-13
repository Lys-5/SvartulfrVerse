const fs = require('fs');

async function testPutSpecies() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
  };

  const testId = '_QALdzzr2fpf8ATHQbRRnF'; // The first blank species
  const payload = {
    name: "Licantropo (Werewolf)",
    description: "Predatore lunare del branco Douglas, dotato di doppio cuore, sensi affilati e fiero legame istintivo.",
    stat_modifiers: {
      strength: 2,
      endurance: 2,
      perception: 1,
      intelligence: -1
    }
  };

  const res = await fetch(`https://app.wyvern.chat/api/worlds/rpg/species/${testId}`, {
    method: 'PUT',
    headers,
    body: JSON.stringify(payload)
  });

  console.log('PUT Status:', res.status);
  const text = await res.text();
  console.log('PUT Response:', text);

  // Check GET
  const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/rpg/species/_CgYT8fHXpDC4crjmegQF7`, { headers });
  const list = await verifyRes.json();
  const updated = list.find(s => s.id === testId);
  console.log('Updated item:', JSON.stringify(updated, null, 2));
}

testPutSpecies().catch(console.error);
