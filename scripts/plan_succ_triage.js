const fs = require('fs');

const payload = JSON.parse(fs.readFileSync('scratch/succ_payload.json', 'utf8'));
const lexicon = JSON.parse(fs.readFileSync('scratch/world_lexicon.json', 'utf8'));
const characters = JSON.parse(fs.readFileSync('scratch/world_characters.json', 'utf8'));
const locations = JSON.parse(fs.readFileSync('scratch/world_locations.json', 'utf8'));

// Build lookup maps
const charByName = new Map();
characters.forEach(c => {
  charByName.set((c.display_name||'').trim().toLowerCase(), c);
});

const lexByName = new Map();
lexicon.forEach(l => {
  lexByName.set((l.name||'').trim().toLowerCase(), l);
});

const locByName = new Map();
locations.forEach(loc => {
  locByName.set((loc.name||'').trim().toLowerCase(), loc);
});

const triagePlan = payload.map((p, idx) => {
  const rawTitle = (p.comment || p.name || '').trim();
  const cleanTitle = rawTitle.replace(/^[^\w\s]+/, '').trim();
  
  // Decide target category
  // 1. Is it a character profile?
  // Let's check common character names
  let matchedChar = null;
  // Specific character mapping
  const charAliases = {
    'Stanley “Stan” Davies Jr.': 'Stanley Davies Jr.',
    'Jared Thompson': 'Jared Thompson',
    'Casey Williams': 'Casey Williams',
    'Nikolaj Jökull': 'Nikolaj Jökull',
    'Janice Thompson': 'Janice Thompson',
    'Tate': 'Tate',
    'Oskar': 'Oskar',
    'Hank Thompson': 'Hank Thompson',
    'Stanley Davies Sr.': 'Stanley Davies Sr.',
    'Chase Anderson': 'Chase Anderson',
    'Jasmin Thompson': 'Jasmin Thompson',
    'Coach Dullahan': 'Dullahan',
    'Eris Davies': 'Eris Davies',
    'Professor Richard Loewe': 'Professor Loewe',
    'Barkley Rover': 'Barkley Rover',
    'Vincent Campbell': 'Vincent Campbell',
    'Andrew "Andy" Campbell': 'Andrew Campbell',
    'Finnegan "Finn" Novak': 'Finnegan Novak',
    'Roland Vickers': 'Roland Vickers',
    'Fade Greymoor': 'Fade Greymoor',
    'Santiago Herrera': 'Santiago Herrera',
    'Iordan R Vess': 'Iordan R. Vess',
    'Dominic Rogers': 'Dominic Rogers',
    'Bailey Rogers': 'Bailey Rogers',
    'Viola "Via" Carter': 'Viola Carter',
    'Mackenzie "Mac" Sanchez-Rogers': 'Mackenzie Sanchez-Rogers',
    'Tomas Matthews': 'Tomas Matthews'
  };

  const cAlias = charAliases[rawTitle] || charAliases[cleanTitle];
  if (cAlias && charByName.has(cAlias.toLowerCase())) {
    matchedChar = charByName.get(cAlias.toLowerCase());
  }

  // 2. Is it an existing Lexicon entry?
  let matchedLex = null;
  const lexAliases = {
    'Founding of SUCC': 'Founding of SUCC',
    'Supernatural Degrees': 'Supernatural Degrees',
    'Rivalry with CUMS': 'Rivalry with CUMS',
    'Werewolves': 'Species: Werewolf & Lycanthrope',
    'Vampires': 'Species: Vampire',
    'Demihumans': 'Species: Demihuman (Kemonomimi)',
    'Humans': 'Species: Human',
    'Anti-Vampire Legislation': 'Anti-Vampire Legislation',
    '1999 Nocturnal Crisis': '1999 Nocturnal Crisis',
    'Grave Mistake (Band)': 'Grave Mistake',
    'SUCC BULLS': 'SUCC BULLS',
    'SUCC BEARS': 'SUCC BEARS',
    'Student Body Population': 'Student Body Population',
    'Frats & Sororities': 'Frats & Sororities',
    'Sports @ SUCC': 'Sports @ SUCC',
    'Allegra Lumsden': 'Allegra Lumsden'
  };

  const lAlias = lexAliases[rawTitle] || lexAliases[cleanTitle] || cleanTitle;
  if (lexByName.has(lAlias.toLowerCase())) {
    matchedLex = lexByName.get(lAlias.toLowerCase());
  }

  // 3. Is it a Location?
  let matchedLoc = null;
  const locAliases = {
    'Solarton': 'Solarton',
    'Hex Valley': 'Hex Valley',
    'Supernatural University of Central California': 'Supernatural University of Central California',
    'Supernatural & Human Alliance': 'Supernatural & Human Alliance',
    'Anime Club': 'Anime Club',
    'The Pack': 'The Pack',
    'Bigfeet Hiking Club': 'Bigfeet Hiking Club',
    'Vampire & Undead Association': 'Vampire & Undead Association'
  };
  const locAlias = locAliases[rawTitle] || locAliases[cleanTitle] || cleanTitle;
  if (locByName.has(locAlias.toLowerCase())) {
    matchedLoc = locByName.get(locAlias.toLowerCase());
  }

  let action = 'CREATE_LEXICON';
  let targetType = 'lore/concept';

  if (matchedChar) {
    action = 'UPDATE_CHARACTER_OR_ATTACHED_MEMORY';
  } else if (['Luisa Sanchez-Rogers', 'Nurse Ariadne Cirillo'].includes(cleanTitle)) {
    action = 'CREATE_CHARACTER_OR_MEMORY';
  } else if (matchedLex) {
    action = 'UPDATE_LEXICON';
  } else if (matchedLoc) {
    action = 'UPDATE_LOCATION_OR_LEXICON';
  }

  return {
    index: idx,
    uid: p.uid,
    rawTitle,
    cleanTitle,
    action,
    matchedChar: matchedChar ? { id: matchedChar.id, name: matchedChar.display_name } : null,
    matchedLex: matchedLex ? { id: matchedLex.id, name: matchedLex.name, type: matchedLex.type } : null,
    matchedLoc: matchedLoc ? { id: matchedLoc.id, name: matchedLoc.name } : null,
    keys: p.key || [],
    contentLength: (p.content || '').length
  };
});

fs.writeFileSync('scratch/succ_triage_detailed.json', JSON.stringify(triagePlan, null, 2));

console.log('Action breakdown:');
const counts = {};
triagePlan.forEach(p => {
  counts[p.action] = (counts[p.action] || 0) + 1;
});
console.log(counts);
