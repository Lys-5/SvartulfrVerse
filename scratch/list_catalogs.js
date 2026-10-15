const fs = require('fs');
const traits = JSON.parse(fs.readFileSync('scratch/rpg_traits_catalog.json', 'utf8'));
const species = JSON.parse(fs.readFileSync('scratch/rpg_species_catalog.json', 'utf8'));
const occs = JSON.parse(fs.readFileSync('scratch/rpg_occupations_catalog.json', 'utf8'));

console.log('--- 24 SPECIES ---');
species.forEach(s => console.log(`${s.id} | ${s.name} | mod: ${JSON.stringify(s.stat_modifiers)}`));

console.log('\n--- 28 OCCUPATIONS ---');
occs.forEach(o => console.log(`${o.id} | ${o.name} | mod: ${JSON.stringify(o.stat_modifiers)}`));

console.log('\n--- 45 TRAITS ---');
traits.forEach(t => console.log(`${t.id} | ${t.name} | mod: ${JSON.stringify(t.stat_modifiers)}`));
