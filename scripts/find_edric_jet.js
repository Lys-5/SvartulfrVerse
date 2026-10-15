const fs = require('fs');

const chars = JSON.parse(fs.readFileSync('scratch/fresh_world_chars.json', 'utf8'));
const edric = chars.find(c => (c.display_name||'').toLowerCase().includes('edric'));
const jet = chars.find(c => (c.display_name||'').toLowerCase().includes('jet'));

console.log('Edric in World:', edric ? `${edric.display_name} (ID: ${edric.id})` : 'NOT FOUND');
console.log('Jet in World:', jet ? `${jet.display_name} (ID: ${jet.id})` : 'NOT FOUND');

if (edric) fs.writeFileSync('scratch/edric_char.json', JSON.stringify(edric, null, 2));
if (jet) fs.writeFileSync('scratch/jet_char.json', JSON.stringify(jet, null, 2));
