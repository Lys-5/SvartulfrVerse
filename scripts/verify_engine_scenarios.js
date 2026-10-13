const fs = require('fs');
const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();

async function verify() {
  const [engineRes, scensRes] = await Promise.all([
    fetch('https://app.wyvern.chat/api/story-engines/engine_HCTPXhL8xr89wUY9r9dYU', { headers: { 'Authorization': `Bearer ${token}` } }),
    fetch('https://app.wyvern.chat/api/worlds/scenarios/world/_CgYT8fHXpDC4crjmegQF7', { headers: { 'Authorization': `Bearer ${token}` } })
  ]);
  
  const engine = await engineRes.json();
  const scens = await scensRes.json();
  
  console.log(`StoryEngine v${engine.version} Rules count: ${(engine.definition.rules||[]).length}`);
  console.log('StoryEngine Rules:', (engine.definition.rules||[]).map(r => r.label));
  console.log(`World Scenarios count: ${scens.length}`);
  scens.forEach(s => console.log(`  Scenario: "${s.name}" (ID: ${s.id})`));
}
verify().catch(console.error);
