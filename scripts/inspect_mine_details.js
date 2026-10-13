const fs = require('fs');

async function inspectMineDetails() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  // 1. Characters mine
  const charRes = await fetch('https://app.wyvern.chat/api/characters/mine', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const chars = await charRes.json();
  console.log('=== /api/characters/mine (count:', chars.length, ') ===');
  chars.forEach(c => {
    console.log('ID:', c.id, '| Name:', c.name || c.display_name, '| title:', c.title);
  });
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/mine_characters.json', JSON.stringify(chars, null, 2), 'utf8');

  // 2. Story Engines mine
  const seMineRes = await fetch('https://app.wyvern.chat/api/story-engines/mine', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const seMine = await seMineRes.json();
  console.log('\n=== /api/story-engines/mine (count:', Array.isArray(seMine) ? seMine.length : 1, ') ===');
  console.log(JSON.stringify(seMine, null, 2));

  // 3. Story Engines all
  const seRes = await fetch('https://app.wyvern.chat/api/story-engines', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const se = await seRes.json();
  console.log('\n=== /api/story-engines (count:', se.length, ') ===');
  se.forEach(s => console.log('ID:', s.id, '| Name:', s.name, '| is_mine:', s.is_mine));
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_story_engines.json', JSON.stringify(se, null, 2), 'utf8');
}

inspectMineDetails();
