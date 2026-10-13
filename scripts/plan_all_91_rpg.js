const fs = require('fs');

const worldData = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
const chars = worldData.world_characters || [];
const traits = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/rpg_traits.json', 'utf8'));
const occs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/rpg_occs.json', 'utf8'));
const speciesList = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/rpg_species.json', 'utf8'));

console.log(`Analisi di ${chars.length} personaggi...`);

// Mappe veloci
const traitByName = {};
traits.forEach(t => traitByName[t.name.toLowerCase().trim()] = t.id);

const occByName = {};
occs.forEach(o => occByName[o.name.toLowerCase().trim()] = o.id);

const specByName = {};
speciesList.forEach(s => specByName[s.name.toLowerCase().trim()] = s.id);

function getTraitId(pattern) {
  const p = pattern.toLowerCase();
  for (const [k, id] of Object.entries(traitByName)) {
    if (k.includes(p)) return id;
  }
  return null;
}

function getOccId(pattern) {
  const p = pattern.toLowerCase();
  for (const [k, id] of Object.entries(occByName)) {
    if (k.includes(p)) return id;
  }
  return null;
}

function getSpecId(pattern) {
  const p = pattern.toLowerCase();
  for (const [k, id] of Object.entries(specByName)) {
    if (k.includes(p)) return id;
  }
  return null;
}

const audit = chars.map((c, idx) => {
  const name = c.name || c.display_name;
  const longSummary = c.long_summary || '';
  const summary = c.summary || '';
  const text = (name + ' ' + longSummary + ' ' + summary).toLowerCase();

  // 1. Specie
  let specId = c.rpg_stats && c.rpg_stats.species_id;
  if (text.includes('werewolf') || text.includes('licantropo') || text.includes('lupine')) {
    specId = getSpecId('licantropo');
  } else if (text.includes('demihuman') || text.includes('demi-umano') || text.includes('kemonomimi') || text.includes('fox') || text.includes('cat') || text.includes('rabbit')) {
    specId = getSpecId('demi-umano');
  } else if (text.includes('vampir')) {
    specId = getSpecId('vampiro');
  } else if (text.includes('succub') || text.includes('incub')) {
    specId = getSpecId('succube');
  } else if (text.includes('dragon') || text.includes('drago') || text.includes('drake')) {
    specId = getSpecId('drago');
  } else if (text.includes('shifter') || text.includes('mutaforma')) {
    specId = getSpecId('mutaforma');
  } else if (text.includes('demon') || text.includes('demone')) {
    specId = getSpecId('demone');
  } else if (text.includes('elf') || text.includes('elfo')) {
    specId = getSpecId('elfo');
  } else if (text.includes('human') || text.includes('umano')) {
    specId = getSpecId('umano');
  }
  if (!specId) specId = getSpecId('umano');

  // 2. Occupazione
  let occId = c.rpg_stats && c.rpg_stats.occupation_id;
  if (name.includes('Wulfnic') || name.includes('Ut Berg') || name.includes('Zefir')) {
    occId = getOccId('firstborn apex');
  } else if (name.includes('Malachia')) {
    occId = getOccId('berserker');
  } else if (name.includes('Angelo Moreno')) {
    occId = getOccId('puppet master');
  } else if (name.includes('Jasper')) {
    occId = getOccId('technomancer');
  } else if (name.includes('Erik Douglas')) {
    occId = getOccId('pack leader');
  } else if (name.includes('Noah')) {
    occId = getOccId('diplomat') || getOccId('right hand');
  } else if (name.includes('Alyssa')) {
    occId = getOccId('guild support');
  } else if (name.includes('Kaladin') || text.includes('pmc') || text.includes('dcc security')) {
    occId = getOccId('dcc security');
  } else if (text.includes('vanguard') || text.includes('assault') || text.includes('fighter')) {
    occId = getOccId('vanguard') || getOccId('fighter');
  } else if (text.includes('healer') || text.includes('medic') || text.includes('support')) {
    occId = getOccId('guild support');
  } else if (text.includes('tank') || text.includes('defender') || text.includes('guardian')) {
    occId = getOccId('guild tank') || getOccId('defender');
  } else if (text.includes('student') || text.includes('matricola') || text.includes('undergrad') || text.includes('succ')) {
    occId = getOccId('succ student');
  } else if (text.includes('professor') || text.includes('teacher') || text.includes('insegnante') || text.includes('coach')) {
    occId = getOccId('teacher') || getOccId('academic');
  } else if (text.includes('hunter') || text.includes('cacciatore')) {
    occId = getOccId('hunter');
  } else if (text.includes('scout') || text.includes('rogue') || text.includes('thief')) {
    occId = getOccId('scout') || getOccId('street scrapper');
  }
  if (!occId) occId = getOccId('citizen');

  // 3. Tratti Multipli
  const assignedTraits = [];
  
  // Tratti biologici / LSE
  if (text.includes('dominant alpha') || text.includes('prime alpha')) assignedTraits.push(getTraitId('dominant alpha'));
  else if (text.includes('alpha')) assignedTraits.push(getTraitId('alpha command'));
  if (text.includes('beta')) assignedTraits.push(getTraitId('beta biology'));
  if (text.includes('delta')) assignedTraits.push(getTraitId('delta biology'));
  if (text.includes('gamma')) assignedTraits.push(getTraitId('pre-first shift'));
  
  // Tratti speciali canonici
  if (name.includes('Wulfnic') || name.includes('Ut Berg') || name.includes('Zefir')) {
    assignedTraits.push(getTraitId('apex predator divine core'));
    assignedTraits.push(getTraitId('ancient heritage'));
    assignedTraits.push(getTraitId('regenerative factor'));
  }
  if (name.includes('Malachia')) {
    assignedTraits.push(getTraitId('berserker internal furnace'));
    assignedTraits.push(getTraitId('feral blood'));
    assignedTraits.push(getTraitId('dungeon veteran'));
    assignedTraits.push(getTraitId('the weight he carries'));
  }
  if (name.includes('Jasper')) {
    assignedTraits.push(getTraitId('technomantic data resonance'));
    assignedTraits.push(getTraitId('tech savvy'));
    assignedTraits.push(getTraitId('mastermind'));
    assignedTraits.push(getTraitId('the weight he carries'));
  }
  if (name.includes('Angelo Moreno')) {
    assignedTraits.push(getTraitId('puppeteer mana strings'));
    assignedTraits.push(getTraitId('mastermind'));
    assignedTraits.push(getTraitId('night stalker'));
  }
  if (name.includes('Alyssa')) {
    assignedTraits.push(getTraitId('familiar soulbound synergy'));
    assignedTraits.push(getTraitId('pre-med / healer'));
    assignedTraits.push(getTraitId('eternal optimist'));
    assignedTraits.push(getTraitId('regenerative factor'));
  }
  if (name.includes('Noah')) {
    assignedTraits.push(getTraitId('trickster mentor'));
    assignedTraits.push(getTraitId('eternal optimist'));
    assignedTraits.push(getTraitId('old money / aristocrat'));
  }
  if (name.includes('Erik')) {
    assignedTraits.push(getTraitId('dominant alpha'));
    assignedTraits.push(getTraitId('alpha command'));
    assignedTraits.push(getTraitId('the weight he carries'));
    assignedTraits.push(getTraitId('old money / aristocrat'));
  }

  // Tratti generali di background
  if (text.includes('lupine') || text.includes('werewolf') || text.includes('licantropo')) {
    assignedTraits.push(getTraitId('lupine senses'));
    assignedTraits.push(getTraitId('partial shift mastery'));
    assignedTraits.push(getTraitId('silver allergy'));
    assignedTraits.push(getTraitId('regenerative factor'));
  }
  if (text.includes('dungeon') || text.includes('guild') || text.includes('dmha') || text.includes('cacciatore')) {
    assignedTraits.push(getTraitId('dungeon veteran'));
  }
  if (text.includes('hacker') || text.includes('tech') || text.includes('cyber') || text.includes('computer')) {
    assignedTraits.push(getTraitId('tech savvy'));
  }
  if (text.includes('pre-med') || text.includes('medic') || text.includes('nurse') || text.includes('healer') || text.includes('botanist')) {
    assignedTraits.push(getTraitId('pre-med / healer'));
  }
  if (text.includes('book') || text.includes('nerd') || text.includes('study') || text.includes('academic') || text.includes('phd')) {
    assignedTraits.push(getTraitId('nerdy / bookworm'));
  }
  if (text.includes('noble') || text.includes('lord') || text.includes('douglas') || text.includes('rich') || text.includes('aristocrat')) {
    assignedTraits.push(getTraitId('old money / aristocrat'));
  }

  // Pulizia e rimozione null/duplicati
  const cleanTraits = [...new Set(assignedTraits.filter(Boolean))];

  // 4. Calcolo Bilanciato delle Statistiche Base (Budget 25 punti distribuiti su base 8)
  // [strength, perception, endurance, charisma, intelligence, agility, luck]
  let s_str = 3, s_per = 3, s_end = 3, s_cha = 3, s_int = 3, s_agi = 3, s_lck = 4; // somma 22 + 3 = 25 punti
  // Calibrazione in base al profilo
  if (text.includes('berserker') || text.includes('vanguard') || text.includes('brawler') || text.includes('fighter')) {
    s_str = 7; s_end = 6; s_agi = 5; s_per = 3; s_int = 1; s_cha = 1; s_lck = 2;
  } else if (text.includes('tank') || text.includes('defender') || text.includes('guardian') || text.includes('giant')) {
    s_end = 7; s_str = 6; s_per = 4; s_agi = 2; s_int = 2; s_cha = 2; s_lck = 2;
  } else if (text.includes('technomancer') || text.includes('hacker') || text.includes('intel') || text.includes('puppet master')) {
    s_int = 7; s_per = 6; s_agi = 4; s_cha = 3; s_end = 2; s_str = 1; s_lck = 2;
  } else if (text.includes('diplomat') || text.includes('charisma') || text.includes('leader') || text.includes('pack mom')) {
    s_cha = 7; s_per = 5; s_int = 4; s_lck = 4; s_end = 2; s_agi = 2; s_str = 1;
  } else if (text.includes('healer') || text.includes('pre-med') || text.includes('medic') || text.includes('alyssa')) {
    s_lck = 7; s_cha = 5; s_per = 5; s_int = 4; s_end = 2; s_agi = 1; s_str = 1;
  } else if (text.includes('scout') || text.includes('speed') || text.includes('rogue') || text.includes('zefir')) {
    s_agi = 7; s_per = 6; s_str = 4; s_end = 3; s_lck = 3; s_int = 1; s_cha = 1;
  }
  // Base stats (base_value = 8)
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
    cid: c.id,
    name: name,
    species_id: specId,
    occupation_id: occId,
    character_traits: cleanTraits,
    base_stats: base_stats
  };
});

console.log(`Pianificazione completata per tutti i ${audit.length} personaggi!`);
fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_91_characters_rpg_plan.json', JSON.stringify(audit, null, 2), 'utf8');

// Mostriamo qualche campione
console.log('\nCampione Malachia:', audit.find(a => a.name.includes('Malachia')));
console.log('\nCampione Alyssa:', audit.find(a => a.name.includes('Alyssa')));
console.log('\nCampione Jasper:', audit.find(a => a.name.includes('Jasper')));
console.log('\nCampione Angelo:', audit.find(a => a.name.includes('Angelo')));
console.log('\nCampione Wulfnic:', audit.find(a => a.name.includes('Wulfnic')));
