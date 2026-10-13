const fs = require('fs');
const d = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
const lexicon = d.lexicon || [];

const searchNames = [
  'Barrow', 'Marek', 'Radek', 'Goran', 'Kian', 'Neve', 'Jaelyn',
  'Bessie May', 'Liam', 'Hugh', 'Amerian', 'Ashton', 'Caien',
  'Lestat', 'Xaiden', 'Aeril', 'Zaire', 'Dorian', 'Yuzuha', 'Mizuki', 'Lucan'
];

console.log('Searching Lexicon entries:');
searchNames.forEach(name => {
  const matches = lexicon.filter(l => l.name.toLowerCase().includes(name.toLowerCase()));
  if (matches.length > 0) {
    console.log(`\nMatch for "${name}":`);
    matches.forEach(m => console.log(`  - [${m.type}] "${m.name}" (${m.id})`));
  } else {
    console.log(`No match for "${name}" in Lexicon`);
  }
});
