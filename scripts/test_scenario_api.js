const fs = require('fs');

async function testScenarioGet() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const scenarioId = '_p1Ffq22CTwVywz1CFQBfF';

  // Test endpoints
  const endpoints = [
    `https://app.wyvern.chat/api/worlds/scenarios/${scenarioId}`,
    `https://app.wyvern.chat/api/scenarios/${scenarioId}`,
    `https://app.wyvern.chat/api/worlds/scenarios/world/_CgYT8fHXpDC4crjmegQF7`
  ];

  for (const ep of endpoints) {
    try {
      const res = await fetch(ep, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      console.log(`${ep} -> Status: ${res.status}`);
      if (res.ok) {
        const data = await res.json();
        console.log('   Data keys:', Array.isArray(data) ? `array of ${data.length}` : Object.keys(data));
      }
    } catch(e) {
      console.error(ep, e.message);
    }
  }
}

testScenarioGet().catch(console.error);
