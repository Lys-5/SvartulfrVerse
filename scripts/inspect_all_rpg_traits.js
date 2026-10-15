const fs = require('fs');

async function inspectAllTraits() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const res = await fetch('https://app.wyvern.chat/api/worlds/rpg/traits/' + worldId, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const traits = await res.json();
  console.log('Total traits:', traits.length);
  
  const withoutModifiers = traits.filter(t => !t.stat_modifiers || Object.keys(t.stat_modifiers).length === 0);
  console.log('Traits WITHOUT modifiers (No modifiers):', withoutModifiers.length);
  
  console.log('\n--- LISTA COMPLETA TRATTI SENZA MODIFICATORI ---');
  withoutModifiers.forEach((t, i) => {
    console.log(`${i + 1}. [${t.id}] "${t.name}" | Desc: ${(t.description || '').slice(0, 90)}`);
  });

  console.log('\n--- TUTTI I TRATTI CON MODIFICATORI ESISTENTI ---');
  traits.filter(t => t.stat_modifiers && Object.keys(t.stat_modifiers).length > 0).forEach(t => {
    console.log(`"${t.name}":`, JSON.stringify(t.stat_modifiers));
  });

  // Salva dump in scratch
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_rpg_traits_dump.json', JSON.stringify(traits, null, 2), 'utf8');
}

inspectAllTraits().catch(err => {
  console.error(err);
  process.exit(1);
});
