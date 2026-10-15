const fs = require('fs');

async function dumpAllRpgBlueprints() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  const [traitsRes, speciesRes, occsRes] = await Promise.all([
    fetch(`https://app.wyvern.chat/api/worlds/rpg/traits/${worldId}`, { headers: { 'Authorization': `Bearer ${token}` } }),
    fetch(`https://app.wyvern.chat/api/worlds/rpg/species/${worldId}`, { headers: { 'Authorization': `Bearer ${token}` } }),
    fetch(`https://app.wyvern.chat/api/worlds/rpg/occupations/${worldId}`, { headers: { 'Authorization': `Bearer ${token}` } })
  ]);

  const traits = await traitsRes.json();
  const species = await speciesRes.json();
  const occupations = await occsRes.json();

  fs.writeFileSync('scratch/rpg_traits_catalog.json', JSON.stringify(traits, null, 2));
  fs.writeFileSync('scratch/rpg_species_catalog.json', JSON.stringify(species, null, 2));
  fs.writeFileSync('scratch/rpg_occupations_catalog.json', JSON.stringify(occupations, null, 2));

  console.log(`Dumped: ${traits.length} traits, ${species.length} species, ${occupations.length} occupations.`);
}

dumpAllRpgBlueprints().catch(console.error);
