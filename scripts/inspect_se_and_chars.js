const fs = require('fs');

async function inspectStoryEnginesAndMineChars() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  // 1. Story Engines in /mine
  console.log('--- STORY ENGINES /mine ---');
  const seMineRes = await fetch('https://app.wyvern.chat/api/story-engines/mine', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const seMine = await seMineRes.json();
  console.log(JSON.stringify(seMine, null, 2));

  // 2. Sample stand-alone character from /mine (Jasper)
  console.log('\n--- SAMPLE MINE CHARACTER (Jasper) ---');
  const jasperRes = await fetch('https://app.wyvern.chat/api/characters/_t4J9aQNJM36cUKAP4wB4U', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  console.log('Jasper fetch status:', jasperRes.status);
  if (jasperRes.ok) {
    const jData = await jasperRes.json();
    console.log('Keys:', Object.keys(jData));
    console.log('Name:', jData.name || jData.display_name);
    console.log('Description length:', (jData.description || '').length);
    console.log('Personality length:', (jData.personality || '').length);
    console.log('rpg_stats:', jData.rpg_stats);
    console.log('character_traits:', jData.character_traits);
  }
}

inspectStoryEnginesAndMineChars();
