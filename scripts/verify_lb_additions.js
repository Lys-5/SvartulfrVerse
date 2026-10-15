const fs = require('fs');

const additions = JSON.parse(fs.readFileSync('scratch/lorebook_additions.json', 'utf8'));
const succCalendar = additions.find(a => a.name.includes('Calendar'));
const luisa = additions.find(a => a.name.includes('Luisa'));
const ariadne = additions.find(a => a.name.includes('Ariadne'));
const dorms = additions.find(a => a.name.includes('Residenziale') || a.name.includes('Dormitori'));

console.log('Includes SUCC Calendar:', !!succCalendar);
console.log('Includes Luisa:', !!luisa);
console.log('Includes Ariadne:', !!ariadne);
console.log('Includes Dorms:', !!dorms);
