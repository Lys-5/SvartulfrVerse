const fs = require('fs');
const path = require('path');

// 1. Dictionaries & Configurations
const TRAITS = {
  ALPHA_CMD: '_MRxrtF9paJmcB13fAnE9g',
  ANCIENT_HERITAGE: '_CBcWYUneXXPwpyEq2Mjcm',
  APEX_RESONANCE: '_DgLQ22bMWpBnP3nnUK7nf',
  BLOOD_CRAZE: '_3GMDq621yFa7ewyfrd4Pg',
  CYBER_AUG: '_hF64363acKFAJCc77xXjE',
  DUNGEON_VET: '_VrgTBJR3aEyW3FBD1zLkR',
  ETERNAL_OPTIMIST: '_LNe6dhHnxx7BCfXeMERzc',
  FERAL_BLOOD: '_YbYKU6fNwTJgP6x4DPhDT',
  GENTLE_GIANT: '_8AYDaJ2xJaP7Vhe26M1jA',
  KNIGHT_SOUR: '_ycHNkaW9aEjTxppUe6Wtg',
  LUPINE_SENSES: '_VVnrtkB9fn9gr1zMwFRyM',
  MASTERMIND: '_CKqQUUkAh31KTLDkVK96E',
  BOOKWORM: '_pxQ16JrPDh2H6qAQKgKyx',
  NIGHT_STALKER: '_4nTUFT2tfNAjdTKXHfgUc',
  OLD_MONEY: '_JLKHrB9AFqkb1BhT6G3tj',
  PARTIAL_SHIFT: '_8B9wFbE8xag2a2dWTVE9b',
  PRE_MED: '_QT6N7KhahqwqkJVaMXhY9',
  REBEL_HEART: '_URpa2cwkJQgVYt9j966JW',
  REGEN_FACTOR: '_nKtryaNUjK1edMnBNjL9K',
  SRF_VET: '_7a2b7jHqJ7MdbNXQCxG34',
  SILVER_ALLERGY: '_EG7K3mQqJhgaUr7KkYxJR',
  TECH_SAVVY: '_F3Y6PeGWJKq2rk7HKGr9y',
  WEIGHT_CARRIES: '_AMT6xk8rnrT9E9Vx8mhdq',
  TRICKSTER: '_gHdqdc2R8U9GLBxmBLcUV',
  DOMINANT_ALPHA: '_jyDzgjNM8BmbrNC3AxcfB',
  SUBMISSIVE_ALPHA: '_y7reXmHRcYLyErXzpktVK',
  DOMINANT_OMEGA: '_hgNaenaG3qkHjaHgJFreB',
  WHITE_MOON: '_DMMAzBKW3b8wPd9rq6TWp',
  SUBMISSIVE_OMEGA: '_ypmH6A8FdrPa18FHrYjxQ',
  DIVINE_BLOOD: '_1QQ982MmT1fzehNRxq4WU',
  FOUNDING_LINE: '_8YMa2gRKXFMBrWYzx2jqD',
  PUREBLOOD: '_an1zbcGY7MYWA2qHeCzba',
  COMMON_BLOOD: '_fYMTrnz7V4Vd7DECCxLMm'
};

const speciesMap = {
  werewolf: '_wyAYU2Mn7AkQ1hVej7PdW',
  lycan: '_wyAYU2Mn7AkQ1hVej7PdW',
  lupine: '_wyAYU2Mn7AkQ1hVej7PdW',
  demihuman: '_pf9FRybEA1Y7naxw7TDQE',
  'demi-human': '_pf9FRybEA1Y7naxw7TDQE',
  human: '_7YEmLbXRMKazP3gKLK8rf',
  vampire: '_jNfcgFJy6CQqReHEqFy81',
  elf: '_qW1kxMD6Vw9rc3XjYRKYW',
  sidhe: '_qW1kxMD6Vw9rc3XjYRKYW',
  demon: '_FQJetrfXHAA4TyachJqwU',
  fairy: '_GAjbNczaLkzTc6xndRTbj',
  fae: '_GAjbNczaLkzTc6xndRTbj',
  angel: '_8pcCdjPMbeJRVAgtJfX8n',
  celestial: '_8pcCdjPMbeJRVAgtJfX8n',
  dragon: '_eHJ9NMk4zTqzTL3EpPwPq',
  drake: '_eHJ9NMk4zTqzTL3EpPwPq',
  orc: '_y1Cc1bJ6d2D3HzFyymDRB',
  oni: '_y1Cc1bJ6d2D3HzFyymDRB',
  succubus: '_aNMnc8ELREgqgb43JB8YJ',
  incubus: '_aNMnc8ELREgqgb43JB8YJ',
  minotaur: '_nUm9xyCztM9UR8HktQneq',
  centaur: '_nUm9xyCztM9UR8HktQneq',
  holstaur: '_nUm9xyCztM9UR8HktQneq',
  merfolk: '_beC3hUmLcEhV71LRMq18g',
  siren: '_beC3hUmLcEhV71LRMq18g',
  kitsune: '_AzpmdmRG2agmntXRMcTaP',
  neko: '_AzpmdmRG2agmntXRMcTaP',
  shifter: '_ePn1gynpUtQEwUf7JPU6D',
  undead: '_3zBD3Nng6VKUkGDXFWT42',
  revenant: '_3zBD3Nng6VKUkGDXFWT42',
  naga: '_KefEdazJ9gDWnTFwM6XV9',
  lamia: '_KefEdazJ9gDWnTFwM6XV9',
  arachne: '_zEHTMrKEctxkHHB2W3dXq',
  drider: '_zEHTMrKEctxkHHB2W3dXq',
  machine: '_92MghbhEBRkmnzJCDBAR7',
  synthetic: '_92MghbhEBRkmnzJCDBAR7',
  cyborg: '_92MghbhEBRkmnzJCDBAR7',
  mutant: '_QALdzzr2fpf8ATHQbRRnF',
  god: '_dHgJt4PfVjTqtMYm6Dfz9',
  demigod: '_dHgJt4PfVjTqtMYm6Dfz9',
  primordial: '_dHgJt4PfVjTqtMYm6Dfz9'
};

const occKeywords = [
  { match: ['pack leader', 'prime alpha'], id: '_AAc7xBcAEttBdFmWTjBTg' },
  { match: ['patriarch', 'coven leader', 'lord', 'house head'], id: '_YngWPBkwzfxfd6MbjhQAj' },
  { match: ['left hand', 'enforcer'], id: '_VgABCMewQQjJVRh7Rc68N' },
  { match: ['right hand', 'advisor', 'peacekeeper'], id: '_mG8DVrPTq8JdL8B2meJRY' },
  { match: ['mate', 'pack mom', 'matriarch'], id: '_UqPTxeWDKkGT9R8bpM9U2' },
  { match: ['knight', 'sworn warrior'], id: '_V3AT8kBRmW67dfbF7ByXD' },
  { match: ['dcc security', 'pmc', 'security', 'commander'], id: '_12YM878yc9tkLC32Lfdhx' },
  { match: ['guild vanguard', 'vanguard', 'dps'], id: '_XdCtVEfpagDkty7je31B8' },
  { match: ['guild tank', 'tank'], id: '_fgTDn33yV6eE9HEmm3qec' },
  { match: ['guild support', 'healer', 'medic', 'doctor'], id: '_zdew8qxchkMDcJf6Ge39t' },
  { match: ['hunter', 'provider'], id: '_AceqGK7cL6QkAKdPF9kCT' },
  { match: ['scout', 'infiltrator', 'tracking'], id: '_yCNjpDEBrLGbMK73CrBzR' },
  { match: ['street scrapper', 'rogue', 'thief', 'hacker'], id: '_R3MA2NAW1yXtXDT4KkqqN' },
  { match: ['pro athlete', 'fighter', 'mma', 'boxer'], id: '_GwQBtq3JX8MGjF6QYpVkg' },
  { match: ['academic', 'phd', 'researcher', 'scientist', 'professor'], id: '_q22RhFdF3H7RRTx2y31GL' },
  { match: ['teacher'], id: '_wcA4ByUp6A8UCXqgCYKfk' },
  { match: ['diplomat', 'ambassador', 'consul'], id: '_eFTUaaMbVTByeDbbM9cLP' },
  { match: ['event organizer', 'fixer', 'bartender', 'club owner'], id: '_H6qFqB6BHDYGAXYJHLJFm' },
  { match: ['builder', 'mechanic', 'engineer', 'craftsman'], id: '_aFyU3E3TkK483Kt1GAHmX' },
  { match: ['caretaker', 'breeder', 'cook', 'chef'], id: '_F6WVk1mdhfkxMY3jymHCH' },
  { match: ['succ student', 'student', 'undergraduate', 'college'], id: '_73GgtJVQaYhaWCyjVeqRM' },
  { match: ['citizen'], id: '_qVckBABybAfQMUcYMpTkd' }
];

const fallbackAges = {
  'Jet Thompson': 14,
  'Dominic Rogers': 48,
  'Roman Blackwood': 23,
  'Eric': 21,
  'Javier Reyes': 22,
  'Raymond': 22,
  'Dean': 22,
  'Bryson': 28,
  'Scarlett Rose': 21,
  'Sierra': 21,
  'Varg Darkfire': 58,
  'Karshin Darkfire': 45,
  'Boros Darkfire': 42,
  'Aras Darkfire': 39,
  'Kolya Varenkov': 26,
  'Russ Sinclair': 19
};

function calculateLevel(c) {
  if (fallbackAges[c.display_name]) return fallbackAges[c.display_name];
  let bd = c.birthdate;
  if (bd !== undefined && bd !== null) {
    let age = Math.floor((10486470 - bd) / (24 * 365.25));
    return Math.max(1, Math.min(99, age));
  }
  const text = (c.long_summary || '') + ' ' + (c.summary || '');
  const m = text.match(/AGE:\s*([0-9]{1,4})/i);
  if (m) return Math.max(1, Math.min(99, parseInt(m[1])));
  return 25;
}

function resolveSpecies(c) {
  const text = (c.long_summary || '') + ' ' + (c.summary || '');
  const m = text.match(/SPECIES:\s*([^;\]\n]+)/i);
  const t = (m ? m[1] : text).toLowerCase();
  for (const [k, v] of Object.entries(speciesMap)) {
    if (t.includes(k)) return v;
  }
  return '_pf9FRybEA1Y7naxw7TDQE'; // default Demihuman
}

function resolveOccupation(c) {
  const text = (c.long_summary || '') + ' ' + (c.summary || '');
  const m = text.match(/OCCUPATION:\s*([^;\]\n]+)/i) || text.match(/ROLE:\s*([^;\]\n]+)/i);
  const t = (m ? m[1] : text).toLowerCase();
  for (const item of occKeywords) {
    if (item.match.some(kw => t.includes(kw))) return item.id;
  }
  return '_qVckBABybAfQMUcYMpTkd'; // Citizen default
}

function resolveStats(c) {
  const text = (c.long_summary || '') + ' ' + (c.summary || '');
  const t = text.toLowerCase();
  
  if (c.display_name.includes('Alyssa')) {
    return { strength: 9, perception: 11, endurance: 11, charisma: 16, intelligence: 13, agility: 11, luck: 10 };
  }
  if (c.display_name.includes('Jasper')) {
    return { strength: 11, perception: 13, endurance: 12, charisma: 13, intelligence: 12, agility: 14, luck: 6 };
  }
  if (c.display_name.includes('Malachia')) {
    return { strength: 16, perception: 13, endurance: 15, charisma: 14, intelligence: 10, agility: 11, luck: 2 };
  }
  if (c.display_name.includes('Noah')) {
    return { strength: 14, perception: 11, endurance: 13, charisma: 15, intelligence: 11, agility: 12, luck: 5 };
  }
  if (c.display_name.includes('Erik')) {
    return { strength: 16, perception: 13, endurance: 15, charisma: 17, intelligence: 11, agility: 9, luck: 0 };
  }

  // Archetypes (each summing to precisely 81 points)
  if (/tank|brawler|guard|muscle|berserker|heavy|taur/.test(t)) {
    return { strength: 14, endurance: 14, perception: 10, agility: 10, intelligence: 10, charisma: 12, luck: 11 };
  }
  if (/rogue|infiltrator|scout|thief|assassin|hitman|speed|shadow/.test(t)) {
    return { agility: 16, perception: 14, luck: 13, intelligence: 11, strength: 9, endurance: 9, charisma: 9 };
  }
  if (/mage|witch|researcher|doctor|healer|medic|scholar|scientist|alchemy/.test(t)) {
    return { intelligence: 16, charisma: 13, perception: 13, luck: 12, endurance: 9, agility: 9, strength: 9 };
  }
  if (/leader|ceo|head|council|patriarch|matriarch|lord|alpha of alphas/.test(t)) {
    return { charisma: 17, intelligence: 13, perception: 12, endurance: 11, strength: 10, agility: 9, luck: 9 };
  }
  if (/warrior|fighter|vanguard|combat|knight|security|soldier/.test(t)) {
    return { strength: 15, agility: 13, endurance: 14, perception: 12, intelligence: 9, charisma: 9, luck: 9 };
  }
  if (/artist|guitarist|singer|dj|dancer|sorority|performer/.test(t)) {
    return { charisma: 16, agility: 13, luck: 13, perception: 12, intelligence: 11, endurance: 8, strength: 8 };
  }
  return { strength: 11, endurance: 12, perception: 12, intelligence: 12, agility: 12, charisma: 11, luck: 11 };
}

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0' };
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  // 1. Fetch live traits map
  const trRes = await fetch('https://app.wyvern.chat/api/worlds/rpg/traits/' + worldId, { headers });
  const allTraits = await trRes.json();
  const traitMap = {};
  allTraits.forEach(t => { traitMap[t.name] = t; });

  // 2. Fetch all characters
  const res = await fetch('https://app.wyvern.chat/api/worlds/characters/world/' + worldId, { headers });
  const chars = await res.json();
  console.log(`Starting RPG application for ${chars.length} characters in batches of 20...`);

  const snapshotDir = path.join(__dirname, '..', 'scratch', 'rpg_full_snapshots');
  fs.mkdirSync(snapshotDir, { recursive: true });

  const batchSize = 20;
  let successCount = 0;

  for (let i = 0; i < chars.length; i += batchSize) {
    const batch = chars.slice(i, i + batchSize);
    const batchNum = Math.floor(i / batchSize) + 1;
    const totalBatches = Math.ceil(chars.length / batchSize);
    console.log(`\n=== Batch ${batchNum}/${totalBatches} (${batch.length} characters) ===`);

    for (const c of batch) {
      const cid = c.id;
      const name = c.display_name;
      const cUrl = `https://app.wyvern.chat/api/worlds/characters/${cid}`;

      // Snapshot previous
      fs.writeFileSync(path.join(snapshotDir, `${cid}.json`), JSON.stringify(c, null, 2), 'utf8');

      // Resolve fields
      const spId = resolveSpecies(c);
      const occId = resolveOccupation(c);
      const level = calculateLevel(c);
      const stats = resolveStats(c);

      // Verify stat sum
      const sum = Object.values(stats).reduce((a, b) => a + b, 0);
      if (sum !== 81) {
        console.error(`ERROR: Stat sum mismatch for ${name}: ${sum}`);
        continue;
      }

      // Check traits
      let traitsPayload = undefined;
      if (!c.character_traits || c.character_traits.length === 0) {
        const text = ((c.long_summary || '') + ' ' + (c.summary || '')).toLowerCase();
        const assigned = [];
        if (text.includes('demon')) {
          if (traitMap['Apex Core Resonance']) assigned.push(traitMap['Apex Core Resonance']);
        } else if (text.includes('vampire')) {
          if (traitMap['Night Stalker']) assigned.push(traitMap['Night Stalker']);
          if (traitMap['Symbiotic Feeder']) assigned.push(traitMap['Symbiotic Feeder']);
        } else if (text.includes('werewolf') || text.includes('wolf')) {
          if (traitMap['Lupine Senses']) assigned.push(traitMap['Lupine Senses']);
          if (traitMap['Regenerative Factor']) assigned.push(traitMap['Regenerative Factor']);
          if (traitMap['Common Lupine Blood']) assigned.push(traitMap['Common Lupine Blood']);
        } else if (text.includes('fae') || text.includes('fairy')) {
          if (traitMap['Ancient Heritage']) assigned.push(traitMap['Ancient Heritage']);
        }
        if (/enforcer|fighter|mma|boxer|brawler/.test(text)) {
          if (traitMap['Dungeon Veteran']) assigned.push(traitMap['Dungeon Veteran']);
        }
        if (/student|succ/.test(text)) {
          if (traitMap['Rebel Heart / Underground']) assigned.push(traitMap['Rebel Heart / Underground']);
        }
        if (/sorority|party|charism/.test(text)) {
          if (traitMap['Eternal Optimist']) assigned.push(traitMap['Eternal Optimist']);
        }
        if (/book|tome|scholar|law/.test(text)) {
          if (traitMap['Nerdy / Bookworm']) assigned.push(traitMap['Nerdy / Bookworm']);
        }
        if (assigned.length === 0) {
          if (traitMap['Dungeon Veteran']) assigned.push(traitMap['Dungeon Veteran']);
        }
        traitsPayload = assigned;
      }

      const payload = {
        species_id: spId,
        occupation_id: occId,
        rpg_stats: {
          species_id: spId,
          occupation_id: occId,
          level: level,
          base_stats: stats
        }
      };

      if (traitsPayload) {
        payload.character_traits = traitsPayload;
      }

      try {
        const putRes = await fetch(cUrl, {
          method: 'PUT',
          headers: { ...headers, 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (putRes.ok) {
          successCount++;
          console.log(`  [OK] ${name.padEnd(28)} | Lv ${String(level).padStart(2)} | STR ${stats.strength} PER ${stats.perception} END ${stats.endurance} CHA ${stats.charisma} INT ${stats.intelligence} AGI ${stats.agility} LCK ${stats.luck}`);
        } else {
          console.error(`  [FAIL ${putRes.status}] ${name}`);
        }
      } catch (err) {
        console.error(`  [ERR] ${name}: ${err.message}`);
      }
    }

    // Small delay between batches to be polite to the server
    await new Promise(r => setTimeout(r, 1000));
  }

  console.log(`\n=== COMPLETED! Successfully updated ${successCount} / ${chars.length} characters ===`);
}

main().catch(console.error);
