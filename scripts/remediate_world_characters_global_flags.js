const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();
const worldId = '_CgYT8fHXpDC4crjmegQF7';

// The 5 Core Douglas protagonists that remain is_global: true
const coreDouglasIds = new Set([
  '_MXcEC8Y6B3BNm3b1ttHj6', // Alyssa Douglas Bloodmoon
  '_x3VY2kcbaDbKyCqywGeET', // Jasper Douglas Bloodmoon
  '_r42cVzMjcGTAx7bR1DQVt', // Noah Douglas Bloodmoon
  '_rAcN9GXD1Le4WxY28e49W', // Malachia Douglas Bloodmoon
  '_d44gDc8N18kkbEhAcfUCG'  // Erik Douglas
]);

async function remediateCharacters() {
  console.log('Fetching all World Characters...');
  const res = await fetch(`https://app.wyvern.chat/api/worlds/characters/world/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (!res.ok) throw new Error('Failed to fetch characters: ' + res.status);
  const chars = await res.json();
  console.log(`Total World Characters: ${chars.length}`);

  // Save snapshot before changes
  fs.writeFileSync('scratch/pre_remediation_world_characters.json', JSON.stringify(chars, null, 2), 'utf8');

  // Identify targets to set is_global: false
  const targets = chars.filter(c => (c.is_global === true || c.global_character === true) && !coreDouglasIds.has(c.id));
  console.log(`Characters to update (set is_global: false): ${targets.length}`);
  targets.forEach(t => console.log(`- ${t.display_name} (${t.id})`));

  let updatedCount = 0;
  for (const char of targets) {
    const putRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${char.id}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        is_global: false,
        global_character: false
      })
    });
    if (putRes.ok) {
      updatedCount++;
      console.log(`[OK] Updated ${char.display_name} -> is_global: false`);
    } else {
      console.error(`[FAIL] ${char.display_name}: HTTP ${putRes.status}`);
    }
    await new Promise(r => setTimeout(r, 100));
  }

  console.log(`\nCharacter remediation complete! Updated ${updatedCount} characters.`);

  // Verify fresh state
  const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/world/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const freshChars = await verifyRes.json();
  const remainingGlobals = freshChars.filter(c => c.is_global === true || c.global_character === true);
  console.log(`Remaining global characters count: ${remainingGlobals.length}`);
  remainingGlobals.forEach(c => console.log(`- ${c.display_name} (${c.id})`));
}

remediateCharacters().catch(console.error);
