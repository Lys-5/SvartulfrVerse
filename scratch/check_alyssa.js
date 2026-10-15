const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const charId = '_MXcEC8Y6B3BNm3b1ttHj6';

  const res = await fetch(`https://app.wyvern.chat/api/worlds/characters/${charId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const data = await res.json();
  console.log('--- ALYSSA WORLD CARD DATA ---');
  console.log('id:', data.id);
  console.log('display_name:', data.display_name);
  console.log('first_name:', data.first_name);
  console.log('middle_names:', data.middle_names);
  console.log('last_name:', data.last_name);
  console.log('personality:', data.personality);
  console.log('summary:', data.summary);
  console.log('traits:', data.traits);
  console.log('character_traits:', data.character_traits);
  console.log('rpg_stats:', JSON.stringify(data.rpg_stats, null, 2));
  console.log('long_summary:', data.long_summary ? data.long_summary.slice(0, 300) : 'none');
  console.log('keys in data:', Object.keys(data));
  fs.writeFileSync('scratch/alyssa_world_card_fresh.json', JSON.stringify(data, null, 2));
}

main().catch(console.error);
