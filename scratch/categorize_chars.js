const fs = require('fs');
const chars = JSON.parse(fs.readFileSync('scratch/backup_consolidated_snapshot/world_characters.json', 'utf8'));

const groups = {};
chars.forEach(c => {
  let g = 'Other / Civilians';
  const name = c.display_name || '';
  const desc = (c.long_summary || '') + ' ' + (c.description || '');
  if (['Alyssa', 'Jasper', 'Malachia', 'Noah', 'Erik', 'Logan', 'Elizabeth', 'Magnus', 'Cornelius', 'Nixara', 'Wulfnic'].some(n => name.includes(n))) {
    g = 'Douglas Bloodline & Elders';
  } else if (['Zefir', 'Ut Berg'].some(n => name.includes(n))) {
    g = 'Firstborn Primordials';
  } else if (['Kaladin', 'Marcus'].some(n => name.includes(n))) {
    g = 'Project Blackwolf (Military)';
  } else if (['Finnegan', 'Roman'].some(n => name.includes(n))) {
    g = 'Demi-Humans (Kemonomimi)';
  } else if (name.includes('Thompson') || name.includes('Sanchez') || name.includes('Mackenzie') || name.includes('Jared')) {
    g = 'Thompson Family & Pack Allies';
  } else if (desc.includes('SUCC') || desc.includes('Student') || desc.includes('Professor') || desc.includes('Campus')) {
    g = 'SUCC Campus (Faculty & Students)';
  } else if (desc.includes('DMHA') || desc.includes('Hunter') || desc.includes('Guild')) {
    g = 'DMHA Hunters Guild';
  }
  groups[g] = (groups[g] || 0) + 1;
});

console.log('Character Breakdown by Category:');
for (const [k, v] of Object.entries(groups)) {
  console.log(` - ${k}: ${v}`);
}
