const fs = require('fs');

const worldData = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
const lex = worldData.world_lexicon_entries || [];

const traits = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/rpg_traits.json', 'utf8'));
const occs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/rpg_occs.json', 'utf8'));
const speciesList = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/rpg_species.json', 'utf8'));

console.log(`Caricati ${traits.length} tratti, ${occs.length} occupazioni, ${speciesList.length} specie.`);

// Mappe veloci
const traitByName = {};
traits.forEach(t => traitByName[t.name.toLowerCase().trim()] = t.id);

const occByName = {};
occs.forEach(o => occByName[o.name.toLowerCase().trim()] = o.id);

const specByName = {};
speciesList.forEach(s => specByName[s.name.toLowerCase().trim()] = s.id);

function getTraitId(pattern) {
  const p = pattern.toLowerCase().trim();
  for (const [k, id] of Object.entries(traitByName)) {
    if (k === p) return id;
  }
  for (const [k, id] of Object.entries(traitByName)) {
    if (k.startsWith(p) || k.includes(' ' + p) || k.includes('(' + p)) return id;
  }
  for (const [k, id] of Object.entries(traitByName)) {
    if (k.includes(p)) return id;
  }
  return null;
}

function getOccId(pattern) {
  const p = pattern.toLowerCase().trim();
  for (const [k, id] of Object.entries(occByName)) {
    if (k === p) return id;
  }
  for (const [k, id] of Object.entries(occByName)) {
    if (k.startsWith(p) || k.includes(' ' + p) || k.includes('(' + p)) return id;
  }
  for (const [k, id] of Object.entries(occByName)) {
    if (k.includes(p)) return id;
  }
  return null;
}

function getSpecId(pattern) {
  const p = pattern.toLowerCase().trim();
  for (const [k, id] of Object.entries(specByName)) {
    if (k === p) return id;
  }
  for (const [k, id] of Object.entries(specByName)) {
    if (k.startsWith(p) || k.includes(' ' + p) || k.includes('(' + p)) return id;
  }
  for (const [k, id] of Object.entries(specByName)) {
    if (k.includes(p)) return id;
  }
  return null;
}

// -------------------------------------------------------------
// 1. PIANIFICAZIONE DELLE 14 CREATURE / MOSTRI / MOB
// -------------------------------------------------------------
const creatures = lex.filter(e => e.type === 'creature');
console.log(`\nPianificazione di ${creatures.length} creature...`);

const creaturePlans = [
  {
    id: '_C13f22wRTEM3jFe1B9bGz',
    name: 'Virus Beasts',
    species_id: getSpecId('macchina'), // Macchina & Sintetico
    occupation_id: getOccId('technomancer'), // Technomancer / Cyber-Mage
    level: 35,
    traits: [getTraitId('cyber-augmented'), getTraitId('tech savvy')],
    base_stats: { strength: 10, perception: 14, endurance: 11, charisma: 8, intelligence: 15, agility: 12, luck: 10 }
  },
  {
    id: '_r8D1YdXXWczwfb23pzqTY',
    name: 'Boss Dungeon DMHA (Apex Behemoth)',
    species_id: getSpecId('drago'), // Drago & Drake
    occupation_id: getOccId('guild vanguard'), // Guild Vanguard (DPS)
    level: 85,
    traits: [getTraitId('apex core resonance'), getTraitId('blood craze'), getTraitId('dungeon veteran')],
    base_stats: { strength: 18, perception: 13, endurance: 17, charisma: 9, intelligence: 10, agility: 12, luck: 9 }
  },
  {
    id: '_QDNczNxHGjzdTQC8qJFR1',
    name: 'Elementali DMHA',
    species_id: getSpecId('mutante'), // Mutante & Ibrido
    occupation_id: getOccId('defender'), // Defender
    level: 40,
    traits: [getTraitId('apex core resonance'), getTraitId('gentle giant')],
    base_stats: { strength: 14, perception: 11, endurance: 15, charisma: 8, intelligence: 10, agility: 9, luck: 9 }
  },
  {
    id: '_NWwzXdykqgRn7bz9BH3Cm',
    name: 'Drider DMHA',
    species_id: getSpecId('aracnide'), // Aracnide & Drider
    occupation_id: getOccId('hunter'), // Hunter / Provider
    level: 45,
    traits: [getTraitId('night stalker'), getTraitId('feral blood')],
    base_stats: { strength: 13, perception: 13, endurance: 12, charisma: 8, intelligence: 10, agility: 15, luck: 9 }
  },
  {
    id: '_TPjPELkJxeBU3cpftkf6H',
    name: 'Non-Morti DMHA (Ghoul Urbani)',
    species_id: getSpecId('non-morto'), // Non-Morto & Revenant
    occupation_id: getOccId('street scrapper'), // Street Scrapper / Rogue
    level: 28,
    traits: [getTraitId('feral blood'), getTraitId('symbiotic feeder')],
    base_stats: { strength: 12, perception: 10, endurance: 14, charisma: 8, intelligence: 8, agility: 10, luck: 8 }
  },
  {
    id: '_xMLY7zdLqVdNMEnfYymmQ',
    name: 'Yokai DMHA (Spiriti Orientali)',
    species_id: getSpecId('kitsune'), // Kitsune & Neko
    occupation_id: getOccId('scout'), // Scout
    level: 42,
    traits: [getTraitId('lupine senses'), getTraitId('trickster mentor')],
    base_stats: { strength: 9, perception: 14, endurance: 10, charisma: 13, intelligence: 12, agility: 14, luck: 12 }
  },
  {
    id: '_ha21xWTkj7yKRTHJc4zPT',
    name: 'Demoni Minori DMHA (Furie Bassifondi)',
    species_id: getSpecId('demone'), // Demone & Infernale
    occupation_id: getOccId('street scrapper'), // Street Scrapper / Rogue
    level: 35,
    traits: [getTraitId('feral blood'), getTraitId('night stalker')],
    base_stats: { strength: 13, perception: 11, endurance: 12, charisma: 9, intelligence: 9, agility: 13, luck: 9 }
  },
  {
    id: '_xVhVGPEkazJHN9fn97Hhj',
    name: 'Criptidi DMHA (Shadow Entities)',
    species_id: getSpecId('mutante'), // Mutante & Ibrido
    occupation_id: getOccId('scout'), // Scout
    level: 46,
    traits: [getTraitId('night stalker'), getTraitId('apex core resonance')],
    base_stats: { strength: 11, perception: 15, endurance: 11, charisma: 8, intelligence: 10, agility: 15, luck: 10 }
  },
  {
    id: '_81DVqUkcyBbhbM69bb8gn',
    name: 'Chimere DMHA (Bio-Armi Clandestine)',
    species_id: getSpecId('mutante'), // Mutante & Ibrido
    occupation_id: getOccId('guild vanguard'), // Guild Vanguard (DPS)
    level: 58,
    traits: [getTraitId('modified / lab lineage'), getTraitId('feral blood'), getTraitId('blood craze')],
    base_stats: { strength: 16, perception: 12, endurance: 15, charisma: 8, intelligence: 8, agility: 13, luck: 8 }
  },
  {
    id: '_7q84e4Lhtnb83HjTcXt6n',
    name: 'Infezioni Miasma DMHA (Parassiti Eterici)',
    species_id: getSpecId('mutante'), // Mutante & Ibrido
    occupation_id: getOccId('guild support'), // Guild Support (Healer/Mage)
    level: 32,
    traits: [getTraitId('symbiotic feeder'), getTraitId('apex core resonance')],
    base_stats: { strength: 9, perception: 12, endurance: 13, charisma: 8, intelligence: 11, agility: 10, luck: 9 }
  },
  {
    id: '_XPhjYq64NJYCbhMgj4jeL',
    name: 'Vilitanos DMHA (Predatori di Confine)',
    species_id: getSpecId('mutante'), // Mutante & Ibrido
    occupation_id: getOccId('hunter'), // Hunter / Provider
    level: 44,
    traits: [getTraitId('night stalker'), getTraitId('feral blood')],
    base_stats: { strength: 14, perception: 13, endurance: 13, charisma: 8, intelligence: 9, agility: 13, luck: 9 }
  },
  {
    id: '_dcFa7apQDzBF2t9Br28N7',
    name: 'Bestiario DMHA (Registro Scientifico Mostri)',
    species_id: getSpecId('umano'), // Umano
    occupation_id: getOccId('academic'), // Academic / PhD Candidate
    level: 50,
    traits: [getTraitId('nerdy / bookworm'), getTraitId('old money / aristocrat')],
    base_stats: { strength: 8, perception: 14, endurance: 10, charisma: 10, intelligence: 17, agility: 9, luck: 12 }
  },
  {
    id: '_b66ztLLgNRKTyfafhqRg7',
    name: 'Ice Satyrs',
    species_id: getSpecId('minotauro'), // Minotauro & Centauro
    occupation_id: getOccId('defender'), // Defender
    level: 38,
    traits: [getTraitId('gentle giant'), getTraitId('feral blood')],
    base_stats: { strength: 15, perception: 11, endurance: 15, charisma: 8, intelligence: 9, agility: 10, luck: 9 }
  },
  {
    id: '_FkXtyrhQMhCpg7N6gm1Wm',
    name: 'Asag Beast',
    species_id: getSpecId('mutante'), // Mutante & Ibrido
    occupation_id: getOccId('guild vanguard'), // Guild Vanguard (DPS)
    level: 65,
    traits: [getTraitId('apex core resonance'), getTraitId('feral blood'), getTraitId('dungeon veteran')],
    base_stats: { strength: 17, perception: 13, endurance: 16, charisma: 8, intelligence: 9, agility: 12, luck: 9 }
  }
];

creaturePlans.forEach(cp => {
  cp.traits = [...new Set(cp.traits.filter(Boolean))];
});

console.log(`Pianificate ${creaturePlans.length} creature.`);

// -------------------------------------------------------------
// 2. PIANIFICAZIONE DEI 312 NPC TERZIARI
// -------------------------------------------------------------
const npcs = lex.filter(e => e.type === 'npc');
console.log(`\nPianificazione di ${npcs.length} NPC terziari...`);

const speciesRegex = /SPECIES:\s*([^;\]\n]+)/i;
const occRegex = /OCCUPATION:\s*([^;\]\n]+)/i;
const ageRegex = /AGE:\s*([^;\]\n]+)/i;

function matchSpeciesFromText(raw) {
  const s = raw.toLowerCase();
  if (/\b(god|deity|primordial|fenris)\b/.test(s)) return getSpecId('divinita');
  if (/\b(werewolf|licantrop|lupine|wolf|lupo)\b/.test(s)) return getSpecId('licantropo');
  if (/\b(vampire|vampir|nosferatu)\b/.test(s)) return getSpecId('vampiro');
  if (/\b(succub|incub)\b/.test(s)) return getSpecId('succube');
  if (/\b(demon|demone|infernal)\b/.test(s)) return getSpecId('demone');
  if (/\b(elf|elfo|elven|sidhe)\b/.test(s)) return getSpecId('elfo');
  if (/\b(angel|angelo|celestial)\b/.test(s)) return getSpecId('angelo');
  if (/\b(fae|fairy|fata|brownie)\b/.test(s)) return getSpecId('fata');
  if (/\b(dragon|drago|drake)\b/.test(s)) return getSpecId('drago');
  if (/\b(orc|orco|oni|goblin)\b/.test(s)) return getSpecId('orco');
  if (/\b(minotaur|centaur|satyr|satiro)\b/.test(s)) return getSpecId('minotauro');
  if (/\b(merfolk|mermaid|merman|siren|tritone|sirena)\b/.test(s)) return getSpecId('tritone');
  if (/\b(kitsune|yokai|neko)\b/.test(s)) return getSpecId('kitsune');
  if (/\b(drider|arachne)\b/.test(s)) return getSpecId('aracnide');
  if (/\b(shifter|mutaforma|changeling)\b/.test(s)) return getSpecId('mutaforma');
  if (/\b(undead|non-morto|ghoul|revenant|zombie|skeleton)\b/.test(s)) return getSpecId('non-morto');
  if (/\b(lamia|naga|serpent)\b/.test(s)) return getSpecId('lamia');
  if (/\b(machine|robot|android|cyber|synthetic)\b/.test(s)) return getSpecId('macchina');
  if (/\b(mutant|mutante|hybrid|chimera|eldritch|manticore|abomination)\b/.test(s)) return getSpecId('mutante');
  if (/\b(demihuman|demi-human|kemonomimi|bear|fox|rabbit|rat|rodent|alligator|feline|canine)\b/.test(s)) return getSpecId('demi-umano');
  if (/\b(human|umano)\b/.test(s)) return getSpecId('umano');
  return null;
}

function matchOccupationFromText(raw) {
  const o = raw.toLowerCase();
  if (/\b(firstborn|fenris|father of the species)\b/.test(o)) return getOccId('firstborn apex');
  if (/\b(berserker)\b/.test(o)) return getOccId('berserker');
  if (/\b(puppet master|puppeteer|marionette)\b/.test(o)) return getOccId('puppet master');
  if (/\b(technomancer|cyber-mage|hacker)\b/.test(o)) return getOccId('technomancer');
  if (/\b(pmc|security|bodyguard|bouncer|guard)\b/.test(o)) return getOccId('dcc security');
  if (/\b(hunter|cacciatore|trapper|dmha|specimen broker)\b/.test(o)) return getOccId('hunter');
  if (/\b(defender|guardian|shield)\b/.test(o)) return getOccId('defender');
  if (/\b(vanguard|tactician|assault|shock troop|fighter|warrior)\b/.test(o)) return getOccId('guild vanguard');
  if (/\b(support|healer|medic|nurse|doctor|cleric|mage|wizard|sorcerer)\b/.test(o)) return getOccId('guild support');
  if (/\b(scout|recon|spy|infiltrator|assassin)\b/.test(o)) return getOccId('scout');
  if (/\b(rogue|thief|scrapper|underworld|smuggler|delinquent)\b/.test(o)) return getOccId('street scrapper');
  if (/\b(professor|coach|teacher|docente|instructor)\b/.test(o)) return getOccId('teacher');
  if (/\b(phd|academic|researcher|scientist|chemist|botanist)\b/.test(o)) return getOccId('academic');
  if (/\b(student|sophomore|freshman|junior|senior|cheerleader|undergrad|college|succ)\b/.test(o)) return getOccId('succ student');
  if (/\b(builder|carpenter|artisan|baker|blacksmith|construction)\b/.test(o)) return getOccId('builder');
  if (/\b(diplomat|hostess|model|runway|public image|ambassador|pr)\b/.test(o)) return getOccId('diplomat');
  if (/\b(fixer|mortician|broker|event organizer|relic broker)\b/.test(o)) return getOccId('event organizer');
  if (/\b(knight|paladin|sworn)\b/.test(o)) return getOccId('knight');
  if (/\b(pack leader|clan head|syndicate head|gang leader|president|coven leader|underboss|patriarch|lord)\b/.test(o)) return getOccId('pack leader') || getOccId('house head');
  if (/\b(pack mom|leader's mate)\b/.test(o)) return getOccId('leader\'s mate');
  if (/\b(right hand|advisor|peacekeeper|consigliere)\b/.test(o)) return getOccId('right hand');
  if (/\b(caretaker|breeder|handler)\b/.test(o)) return getOccId('caretaker');
  return null;
}

const npcPlans = npcs.map((n, idx) => {
  const name = n.name || (n.keys && n.keys[0]) || `NPC_${idx}`;
  const content = n.content || '';
  const text = (name + ' ' + (n.keys || []).join(' ') + ' ' + (n.labels || []).join(' ') + ' ' + content).toLowerCase();

  // 1. Specie
  let specId = null;
  const sm = content.match(speciesRegex);
  if (sm) {
    specId = matchSpeciesFromText(sm[1]);
  }
  if (!specId) {
    specId = matchSpeciesFromText(text);
  }
  if (!specId) {
    specId = getSpecId('umano');
  }

  // 2. Occupazione
  let occId = null;
  const om = content.match(occRegex);
  if (om) {
    occId = matchOccupationFromText(om[1]);
  }
  if (!occId) {
    occId = matchOccupationFromText(text);
  }
  if (!occId) {
    occId = getOccId('citizen');
  }

  // 3. Livello (da AGE o ruolo, max 99)
  let level = 20;
  const am = content.match(ageRegex);
  if (am) {
    const rawAge = am[1];
    const num = parseInt(rawAge.replace(/\D+/g, ''), 10);
    if (!isNaN(num) && num > 0) {
      level = Math.min(num, 99);
    }
  } else {
    if (name.toLowerCase().includes('fenris') || text.includes('ancient') || text.includes('primordial')) {
      level = 99;
    } else if (text.includes('professor') || text.includes('teacher') || text.includes('coach') || text.includes('elder') || text.includes('head')) {
      level = 45;
    } else if (text.includes('hunter') || text.includes('security') || text.includes('underworld') || text.includes('fixer')) {
      level = 32;
    } else if (text.includes('student') || text.includes('sophomore') || text.includes('freshman')) {
      level = 20;
    } else {
      level = 25;
    }
  }

  // 4. Tratti
  const assignedTraits = [];

  // Tratti biologici
  if (specId === getSpecId('licantropo')) {
    assignedTraits.push(getTraitId('lupine senses'));
    assignedTraits.push(getTraitId('partial shift mastery'));
    assignedTraits.push(getTraitId('silver allergy'));
    assignedTraits.push(getTraitId('common lupine blood'));
  }
  if (text.includes('alpha')) {
    assignedTraits.push(getTraitId('alpha command'));
  }
  if (text.includes('beta')) {
    assignedTraits.push(getTraitId('lse beta biology'));
  }
  if (text.includes('delta')) {
    assignedTraits.push(getTraitId('lse delta biology'));
  }

  // Tratti ruolo e background
  if (text.includes('dungeon') || text.includes('dmha') || text.includes('hunter') || text.includes('combat')) {
    assignedTraits.push(getTraitId('dungeon veteran'));
  }
  if (text.includes('ancient') || text.includes('heritage') || text.includes('primordial') || name.toLowerCase().includes('fenris')) {
    assignedTraits.push(getTraitId('ancient heritage'));
  }
  if (text.includes('hacker') || text.includes('tech') || text.includes('cyber') || text.includes('computer')) {
    assignedTraits.push(getTraitId('tech savvy'));
  }
  if (text.includes('book') || text.includes('phd') || text.includes('study') || text.includes('academic') || text.includes('professor') || text.includes('student')) {
    assignedTraits.push(getTraitId('nerdy / bookworm'));
  }
  if (text.includes('noble') || text.includes('estate') || text.includes('rich') || text.includes('mansion') || text.includes('virtuoso') || text.includes('deville')) {
    assignedTraits.push(getTraitId('old money / aristocrat'));
  }
  if (text.includes('night') || text.includes('shadow') || text.includes('stealth') || text.includes('stalker') || text.includes('underworld')) {
    assignedTraits.push(getTraitId('night stalker'));
  }
  if (text.includes('gentle') || text.includes('bear') || text.includes('huge') || text.includes('massive') || text.includes('giant')) {
    assignedTraits.push(getTraitId('gentle giant'));
  }
  if (text.includes('medic') || text.includes('nurse') || text.includes('healer') || text.includes('doctor') || text.includes('botanist')) {
    assignedTraits.push(getTraitId('pre-med / healer'));
  }
  if (text.includes('optimist') || text.includes('cheerful') || text.includes('bubbly') || text.includes('friendly') || text.includes('cheerleader')) {
    assignedTraits.push(getTraitId('eternal optimist'));
  }
  if (text.includes('rebel') || text.includes('underground') || text.includes('punk') || text.includes('scrapper')) {
    assignedTraits.push(getTraitId('rebel heart / underground'));
  }

  if (assignedTraits.length === 0) {
    if (specId === getSpecId('umano')) {
      assignedTraits.push(getTraitId('eternal optimist') || getTraitId('nerdy / bookworm'));
    } else {
      assignedTraits.push(getTraitId('feral blood') || getTraitId('regenerative factor'));
    }
  }

  const cleanTraits = [...new Set(assignedTraits.filter(Boolean))];

  // 5. Statistiche Base (Base 8 + 25 punti)
  let s_str = 3, s_per = 3, s_end = 3, s_cha = 3, s_int = 3, s_agi = 3, s_lck = 4;
  if (text.includes('fighter') || text.includes('brawler') || text.includes('warrior') || text.includes('vanguard') || text.includes('berserker')) {
    s_str = 7; s_end = 6; s_agi = 5; s_per = 3; s_int = 1; s_cha = 1; s_lck = 2;
  } else if (text.includes('tank') || text.includes('defender') || text.includes('guardian') || text.includes('bear')) {
    s_end = 7; s_str = 6; s_per = 4; s_agi = 2; s_int = 2; s_cha = 2; s_lck = 2;
  } else if (text.includes('academic') || text.includes('professor') || text.includes('researcher') || text.includes('phd') || text.includes('chemist') || text.includes('tech')) {
    s_int = 7; s_per = 6; s_agi = 3; s_cha = 3; s_end = 2; s_str = 1; s_lck = 3;
  } else if (text.includes('diplomat') || text.includes('hostess') || text.includes('model') || text.includes('runway') || text.includes('pr') || text.includes('cheerleader')) {
    s_cha = 7; s_per = 5; s_int = 4; s_lck = 4; s_end = 2; s_agi = 2; s_str = 1;
  } else if (text.includes('healer') || text.includes('medic') || text.includes('support') || text.includes('nurse')) {
    s_lck = 7; s_cha = 5; s_per = 5; s_int = 4; s_end = 2; s_agi = 1; s_str = 1;
  } else if (text.includes('scout') || text.includes('hunter') || text.includes('rogue') || text.includes('speed') || text.includes('stalker')) {
    s_agi = 7; s_per = 6; s_str = 4; s_end = 3; s_lck = 3; s_int = 1; s_cha = 1;
  }

  const base_stats = {
    strength: 8 + s_str,
    perception: 8 + s_per,
    endurance: 8 + s_end,
    charisma: 8 + s_cha,
    intelligence: 8 + s_int,
    agility: 8 + s_agi,
    luck: 8 + s_lck
  };

  return {
    id: n.id,
    name: name,
    species_id: specId,
    occupation_id: occId,
    level: level,
    traits: cleanTraits,
    base_stats: base_stats
  };
});

console.log(`Pianificazione completata per tutti i ${npcPlans.length} NPC!`);

// Salvataggio piani in scratch
fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_creatures_rpg_plan.json', JSON.stringify(creaturePlans, null, 2), 'utf8');
fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_npcs_rpg_plan.json', JSON.stringify(npcPlans, null, 2), 'utf8');

console.log('\n--- CAMPIONE CREATURE (Top 3) ---');
console.log(creaturePlans.slice(0, 3));

console.log('\n--- CAMPIONE NPC (Alicia Virtuoso) ---');
console.log(npcPlans.find(n => n.name.includes('Alicia Virtuoso')));

console.log('\n--- CAMPIONE NPC (Fenris) ---');
console.log(npcPlans.find(n => n.name.includes('Fenris')));

console.log('\n--- CAMPIONE NPC (Adrian Werewolf) ---');
console.log(npcPlans.find(n => n.name.includes('Adrian')));

console.log('\n--- CAMPIONE NPC (Bruce Bear) ---');
console.log(npcPlans.find(n => n.name.includes('Bruce')));
