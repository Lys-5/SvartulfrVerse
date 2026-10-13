const fs = require('fs');

const w = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8')).world;
const opts = w.intro_fields['field-species'].options;
console.log(`Total species options: ${opts.length}`);
opts.forEach((o, i) => {
  console.log(`[${i}] value="${o.value}", label="${o.label}"`);
});
