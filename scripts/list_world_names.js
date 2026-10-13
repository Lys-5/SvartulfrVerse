const fs = require('fs');
const d = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
console.log('Total world characters:', d.world_characters.length);
d.world_characters.forEach((c, i) => {
  console.log(`${i+1}. [${c.id}] "${c.display_name || c.name}"`);
});
