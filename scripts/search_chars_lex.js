const fs = require('fs');
const chars = JSON.parse(fs.readFileSync('scratch/world_characters.json', 'utf8'));
const lexicon = JSON.parse(fs.readFileSync('scratch/world_lexicon.json', 'utf8'));

const names = [
  'Stanley', 'Davies', 'Andy', 'Campbell', 'Finn', 'Novak', 
  'Iordan', 'Vess', 'Via', 'Carter', 'Luisa', 'Sanchez', 
  'Mac', 'Mackenzie', 'Ariadne', 'Cirillo', 'Dullahan'
];

console.log('=== SEARCHING CHARACTERS ===');
names.forEach(n => {
  const found = chars.filter(c => (c.display_name||'').toLowerCase().includes(n.toLowerCase()));
  const desc = found.map(c => `${c.display_name} (id: ${c.id})`).join(' | ');
  console.log(`Query: "${n}" -> ${desc || 'none'}`);
});

console.log('\n=== SEARCHING RELEVANT LEXICON ENTRIES ===');
const lexTopics = ['cums', 'succ', 'vampire', 'werewolf', 'demihuman', 'human', 'solarton', 'hex valley', 'bulls', 'bears', 'grave mistake', 'dorms', 'schedule'];
lexTopics.forEach(t => {
  const found = lexicon.filter(l => (l.name||'').toLowerCase().includes(t.toLowerCase()));
  const desc = found.map(l => `${l.name} (${l.id}, type: ${l.type})`).join(' | ');
  console.log(`Lex Topic "${t}" -> ${desc || 'none'}`);
});
