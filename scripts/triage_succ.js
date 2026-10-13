const fs = require('fs');

const payload = JSON.parse(fs.readFileSync('scratch/succ_payload.json', 'utf8'));
const lexicon = JSON.parse(fs.readFileSync('scratch/world_lexicon.json', 'utf8'));
const characters = JSON.parse(fs.readFileSync('scratch/world_characters.json', 'utf8'));
const locations = JSON.parse(fs.readFileSync('scratch/world_locations.json', 'utf8'));

console.log('=== TRIAGE REPORT FOR SUCC PAYLOAD (60 items) ===\n');

const report = payload.map((item, idx) => {
  const rawTitle = (item.comment || item.name || '').trim();
  const cleanTitle = rawTitle.replace(/^[^\w\s]+/, '').trim();
  const keys = item.key || [];
  
  // Matched Lexicon entries
  const matchedLex = lexicon.filter(l => {
    const lName = (l.name || '').trim().toLowerCase();
    const cLow = cleanTitle.toLowerCase();
    const rLow = rawTitle.toLowerCase();
    if (lName === cLow || lName === rLow) return true;
    // Check if any primary key matches
    if (keys.some(k => k.toLowerCase() === lName)) return true;
    return false;
  });

  // Matched Characters
  const matchedChar = characters.filter(c => {
    const cName = (c.display_name || '').trim().toLowerCase();
    const cLow = cleanTitle.toLowerCase();
    const rLow = rawTitle.toLowerCase();
    if (cName === cLow || cName === rLow) return true;
    if (keys.some(k => k.toLowerCase() === cName)) return true;
    return false;
  });

  // Matched Locations
  const matchedLoc = locations.filter(loc => {
    const lName = (loc.name || '').trim().toLowerCase();
    const cLow = cleanTitle.toLowerCase();
    const rLow = rawTitle.toLowerCase();
    if (lName === cLow || lName === rLow) return true;
    return false;
  });

  return {
    index: idx,
    uid: item.uid,
    rawTitle,
    cleanTitle,
    matchedChars: matchedChar.map(c => ({ id: c.id, name: c.display_name })),
    matchedLocs: matchedLoc.map(l => ({ id: l.id, name: l.name })),
    matchedLex: matchedLex.map(l => ({ id: l.id, name: l.name, type: l.type }))
  };
});

fs.writeFileSync('scratch/triage_summary.json', JSON.stringify(report, null, 2));

report.forEach(r => {
  console.log(`[${r.index}] uid ${r.uid} | "${r.rawTitle}" -> Char: ${r.matchedChars.length > 0 ? r.matchedChars.map(c=>c.name).join(', ') : 'none'} | Loc: ${r.matchedLocs.length > 0 ? r.matchedLocs.map(l=>l.name).join(', ') : 'none'} | Lex: ${r.matchedLex.length > 0 ? r.matchedLex.map(l=>l.name).join(', ') : 'none'}`);
});
