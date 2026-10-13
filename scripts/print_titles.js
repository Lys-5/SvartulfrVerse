const fs = require('fs');
const la = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/la_entries.json', 'utf8'));
const aegis = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/aegis_entries.json', 'utf8'));

console.log('=== LA: PRIMI 45 ELEMENTI (SISTEMA, BIOLOGIA, REGOLE) ===');
la.slice(0, 43).forEach((e, i) => {
  const line = (e.content || '').split('\n')[0].replace(/^#+\s*/, '');
  console.log((i+1) + '. ' + line);
});

console.log('\n=== LA: RESTANTI ELEMENTI (STUDENTI / PERSONAGGI / FACOLTA) ===');
console.log('Numero studenti/personaggi in LA:', la.length - 43);

console.log('\n=== AEGIS CITY HUNTERS ELEMENTI SISTEMICI ===');
aegis.forEach((e, i) => {
  const keys = Array.isArray(e.keys) ? e.keys.join(', ') : '';
  const line = (e.content || '').split('\n')[0].replace(/^#+\s*/, '').slice(0, 60);
  console.log((i+1) + '. [' + keys.slice(0, 30) + '] ' + line);
});
