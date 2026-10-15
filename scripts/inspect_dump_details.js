const fs = require('fs');
const dump = JSON.parse(fs.readFileSync('E:/repository/SvartulfrVerse/scratch/source_cards_dump.json', 'utf8'));

dump.forEach((d, i) => {
  const c = d.char;
  console.log('================================================================');
  console.log(`#${i+1} [${d.target.id}] ${d.target.label}`);
  console.log('Name:', c.name || c.display_name);
  console.log('Tagline:', c.tagline);
  const text = c.description || c.long_summary || '';
  console.log('First 250 chars:\n', text.slice(0, 250));
  console.log('Outfits count:', (c.outfits || []).length);
});
