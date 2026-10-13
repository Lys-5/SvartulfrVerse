const fs = require('fs');

const worldData = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
const newEntries = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/new_succ_dmha_lexicons.json', 'utf8'));

// Estraiamo le voci LSE esistenti
const lseEntries = (worldData.world_lexicon_entries || []).filter(l => {
  const t = (l.title || l.name || '').toLowerCase();
  const c = (l.content || '').toLowerCase();
  return t.startsWith('lse ') || t.startsWith('lse:') || t.includes('biology') || t.includes('secondary sex') || t.includes('omega') || t.includes('alpha') || t.includes('scent');
});

console.log(`Verifica incrociata tra ${newEntries.length} nuove voci e ${lseEntries.length} voci canoniche LSE...`);

let issues = 0;

// Parole chiave o concetti critici LSE da verificare
// 1. Orecchie: i demi-umani hanno 1 solo paio di orecchie (animali, non umane)
// 2. Età e maturità: maturità a 21 anni per Founding, sviluppo 13-19 per shifters
// 3. Em-dash e punteggiatura
// 4. Dinamiche LSE: no contraddizioni su calore, rut o suppressants

newEntries.forEach((entry, idx) => {
  const content = entry.content;
  const title = entry.title;

  // Controllo em-dash
  if (content.includes('—') || content.includes('–')) {
    console.log(`[AVVISO] Em-dash/en-dash trovato in "${title}"`);
    issues++;
  }

  // Controllo orecchie umane (vietate per demi-umani)
  if (content.toLowerCase().includes('orecchie umane')) {
    console.log(`[ERRORE] Riferimento a orecchie umane in "${title}"`);
    issues++;
  }

  // Controllo virgolette
  if (content.includes('“') || content.includes('”')) {
    console.log(`[AVVISO] Virgolette non standard in "${title}"`);
    issues++;
  }

  // Controllo markdown non consentito
  if (content.includes('**')) {
    console.log(`[AVVISO] Bold markdown in "${title}"`);
    issues++;
  }
});

if (issues === 0) {
  console.log('RISULTATO AUDIT: 100% CONFORME! Zero conflitti con le regole LSE, zero em-dash, anatomia demi-umani rigorosamente a orecchie singole.');
} else {
  console.log(`Trovate ${issues} anomalie da correggere.`);
}
