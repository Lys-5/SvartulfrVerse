const fs = require('fs');
const lex = JSON.parse(fs.readFileSync('scratch/world_lexicon.json', 'utf8'));

const names = [
  'Jeremy Thompson', 'Jason Thompson', 'Jaiden Thompson',
  'Stan Davies', 'Chase Anderson', 'Roland Vickers', 'Fade Greymoor',
  'Santiago Herrera', 'Bailey Rogers', 'Viola Carter', 'Tomas Matthews',
  'Jared Thompson', 'Janice Thompson', 'Hank Thompson', 'Jasmin Thompson'
];

names.forEach(n => {
  const found = lex.filter(l => (l.name||'').toLowerCase().includes(n.toLowerCase()));
  const desc = found.map(l => `${l.name} (${l.id}, type: ${l.type})`).join(' | ');
  console.log(`Query "${n}": ${desc || 'none'}`);
});
