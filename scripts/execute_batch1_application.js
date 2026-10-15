const fs = require('fs');

async function executeBatch1() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const lbId = '_LBkRWNpPxpdn6dxYaDU2b'; // Svartúlfr - NPC Primary
  const echoPersonaId = '1791389790053';

  const traitsCatalog = JSON.parse(fs.readFileSync('scratch/rpg_traits_catalog.json', 'utf8'));
  const traitMapById = {};
  traitsCatalog.forEach(t => { traitMapById[t.id] = t; });

  const batch1Definitions = [
    {
      id: '_x3VY2kcbaDbKyCqywGeET',
      name: 'Jasper Svartr Douglas Bloodmoon',
      mineId: '_t4J9aQNJM36cUKAP4wB4U',
      lbSearch: 'Jasper',
      level: 3,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_3mrK4LGktdtUHGbf6CWNp',
      speciesName: 'Werewolf (Founding Bloodline & Pureblood)',
      occupationName: 'Technomancer / Cyber-Mage',
      className: 'Guild Infiltrator & Black-Market Info-Broker',
      stats: { strength: 8, perception: 14, endurance: 10, charisma: 8, intelligence: 18, agility: 13, luck: 10 },
      traitIds: [
        '_aReYAkFDzYfFHwBWqQbyU', // LSE Beta Biology
        '_8YMa2gRKXFMBrWYzx2jqD', // Founding Bloodline
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage
        '_AQ6Qy4KHMDgFWKPHDJeqb', // Technomantic Data Resonance
        '_F3Y6PeGWJKq2rk7HKGr9y', // Tech Savvy
        '_CKqQUUkAh31KTLDkVK96E', // Mastermind
        '_kUV13hFp2R2a4aYEXq3c4', // Familiar Soulbound Synergy
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR', // Silver Allergy
        '_VrgTBJR3aEyW3FBD1zLkR', // Dungeon Veteran
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_JLKHrB9AFqkb1BhT6G3tj'  // Old Money / Aristocrat
      ]
    },
    {
      id: '_rAcN9GXD1Le4WxY28e49W',
      name: 'Malachia Björn Douglas Bloodmoon',
      mineId: '_yQeae3DnARft2RH4gaFNx',
      lbSearch: 'Malachia',
      level: 4,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_d7mHQJKnQqQNzwdwnqMdM',
      speciesName: 'Werewolf (Founding Bloodline & Pureblood Alpha)',
      occupationName: 'Guild Berserker (Vanguard)',
      className: 'Guild Frontline TANK / Vanguard',
      stats: { strength: 18, perception: 10, endurance: 17, charisma: 8, intelligence: 8, agility: 12, luck: 8 },
      traitIds: [
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_yQj1axBPPjLBp79cCD3JG', // Ascended Enigma
        '_DgLQ22bMWpBnP3nnUK7nf', // Apex Core Resonance
        '_mJezfhzrdYDq8k7GWaGzm', // Pack Leader (Designato Futuro Leader)
        '_8YMa2gRKXFMBrWYzx2jqD', // Founding Bloodline
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage
        '_L2xQk9j8RnMKUgGnCVWRR', // Berserker Internal Furnace
        '_YbYKU6fNwTJgP6x4DPhDT', // Feral Blood
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_ycHNkaW9aEjTxppUe6Wtg', // Knight in Sour Armor
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR', // Silver Allergy
        '_VrgTBJR3aEyW3FBD1zLkR', // Dungeon Veteran
        '_JLKHrB9AFqkb1BhT6G3tj'  // Old Money / Aristocrat
      ]
    },
    {
      id: '_r42cVzMjcGTAx7bR1DQVt',
      name: 'Noah Loki Douglas Bloodmoon',
      mineId: '_AjphrWj2BMT9KJTx4KETE',
      lbSearch: 'Noah',
      level: 4,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_mG8DVrPTq8JdL8B2meJRY',
      speciesName: 'Werewolf (Founding Bloodline & Pureblood Delta)',
      occupationName: 'Right Hand (Advisor/Peacekeeper)',
      className: 'Pack PR Shield & Strategic Grey Eminence',
      stats: { strength: 9, perception: 12, endurance: 10, charisma: 18, intelligence: 14, agility: 10, luck: 8 },
      traitIds: [
        '_f8kfz4eJLh6br4fgGXyc6', // LSE Delta Biology
        '_8YMa2gRKXFMBrWYzx2jqD', // Founding Bloodline
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage
        '_CKqQUUkAh31KTLDkVK96E', // Mastermind
        '_gHdqdc2R8U9GLBxmBLcUV', // Trickster Mentor
        '_LNe6dhHnxx7BCfXeMERzc', // Eternal Optimist
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR', // Silver Allergy
        '_JLKHrB9AFqkb1BhT6G3tj', // Old Money / Aristocrat
        '_VrgTBJR3aEyW3FBD1zLkR'  // Dungeon Veteran
      ]
    },
    {
      id: '_d44gDc8N18kkbEhAcfUCG',
      name: 'Erik Ulfr Douglas',
      mineId: '_EWqmxx3Q1fdK97AVBRqEW',
      lbSearch: 'Erik',
      level: 9,
      birthdate: 10035648, // 1972-10-31
      start_timeline_position: 10035648,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_AAc7xBcAEttBdFmWTjBTg',
      speciesName: 'Werewolf (Pureblood Prime Alpha)',
      occupationName: 'Pack Leader',
      className: 'Prime Alpha & CEO of DCC',
      stats: { strength: 15, perception: 12, endurance: 15, charisma: 15, intelligence: 8, agility: 8, luck: 8 },
      traitIds: [
        '_mJezfhzrdYDq8k7GWaGzm', // Pack Leader
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_DgLQ22bMWpBnP3nnUK7nf', // Apex Core Resonance
        '_CKqQUUkAh31KTLDkVK96E', // Mastermind
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_ycHNkaW9aEjTxppUe6Wtg', // Knight in Sour Armor
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR', // Silver Allergy
        '_JLKHrB9AFqkb1BhT6G3tj', // Old Money / Aristocrat
        '_VrgTBJR3aEyW3FBD1zLkR'  // Dungeon Veteran
      ]
    },
    {
      id: '_JL37wK9PQMNDChULCDrWj',
      name: 'Logan Dominic Járn Douglas',
      mineId: '_BQ4THBW3BKL2RN9Xy4YHb',
      lbSearch: 'Logan',
      level: 9,
      birthdate: 10054920, // 1975-01-12
      start_timeline_position: 10054920,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_mG8DVrPTq8JdL8B2meJRY',
      speciesName: 'Werewolf (Pureblood Beta)',
      occupationName: 'Right Hand (Advisor/Peacekeeper)',
      className: "Erik's Right Hand & DCC Black Market Commander",
      stats: { strength: 16, perception: 13, endurance: 16, charisma: 8, intelligence: 9, agility: 11, luck: 8 },
      traitIds: [
        '_aReYAkFDzYfFHwBWqQbyU', // LSE Beta Biology
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_YbYKU6fNwTJgP6x4DPhDT', // Feral Blood
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_ycHNkaW9aEjTxppUe6Wtg', // Knight in Sour Armor
        '_URpa2cwkJQgVYt9j966JW', // Rebel Heart / Underground
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR', // Silver Allergy
        '_JLKHrB9AFqkb1BhT6G3tj', // Old Money / Aristocrat
        '_VrgTBJR3aEyW3FBD1zLkR'  // Dungeon Veteran
      ]
    },
    {
      id: '_EwPN1te7qtUKYEx4NLgag',
      name: 'Elizabeth Duskwood',
      lbSearch: 'Elizabeth',
      level: 14,
      birthdate: 9822648,
      start_timeline_position: 9822648,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_UqPTxeWDKkGT9R8bpM9U2',
      speciesName: 'Werewolf (Pureblood Dominant Omega)',
      occupationName: "Leader's Mate / Pack Mom",
      className: 'Pack Mom Reggente & DCC Medical Director',
      stats: { strength: 8, perception: 12, endurance: 12, charisma: 17, intelligence: 16, agility: 8, luck: 8 },
      traitIds: [
        '_hgNaenaG3qkHjaHgJFreB', // Dominant Omega
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage
        '_QT6N7KhahqwqkJVaMXhY9', // Pre-Med / Healer
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_JLKHrB9AFqkb1BhT6G3tj', // Old Money / Aristocrat
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_pxQ16JrPDh2H6qAQKgKyx', // Nerdy / Bookworm
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR'  // Silver Allergy
      ]
    },
    {
      id: '_jeJTbxLcrYWXNWYPDx4ph',
      name: 'Magnus Douglas III',
      lbSearch: 'Magnus',
      level: 99,
      birthdate: 7372272,
      start_timeline_position: 7372272,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_e8MAN4PAq111hqe91UhCY',
      speciesName: 'Werewolf (Pureblood Alpha Patriarch)',
      occupationName: 'Patriarch / Coven Leader',
      className: 'Ancestral Pack Elder & Dynastic Sovereign',
      stats: { strength: 11, perception: 12, endurance: 12, charisma: 16, intelligence: 14, agility: 8, luck: 8 },
      traitIds: [
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_JLKHrB9AFqkb1BhT6G3tj', // Old Money / Aristocrat
        '_CKqQUUkAh31KTLDkVK96E', // Mastermind
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR'  // Silver Allergy
      ]
    },
    {
      id: '_rJKYcCt61hQa8XRamHEdM',
      name: 'Lord Cornelius Douglas',
      lbSearch: 'Cornelius',
      level: 99,
      birthdate: 7044624,
      start_timeline_position: 7044624,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_YngWPBkwzfxfd6MbjhQAj',
      speciesName: 'Werewolf (Pureblood Alpha Founder)',
      occupationName: 'House Head (Lord/Patriarch)',
      className: 'Blackwood Colony Governor & House Founder',
      stats: { strength: 13, perception: 12, endurance: 13, charisma: 16, intelligence: 11, agility: 8, luck: 8 },
      traitIds: [
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_JLKHrB9AFqkb1BhT6G3tj', // Old Money / Aristocrat
        '_DgLQ22bMWpBnP3nnUK7nf', // Apex Core Resonance
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR'  // Silver Allergy
      ]
    },
    {
      id: '_fmzBDjDn3Gnq2hXKy7tY6',
      name: 'Nixara Hvit Bloodmoon',
      lbSearch: 'Nixara',
      level: 99,
      birthdate: 10058472, // 1975-06-09
      start_timeline_position: 10058472,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_UqPTxeWDKkGT9R8bpM9U2',
      speciesName: 'Werewolf (Founding Bloodline White Moon Omega)',
      occupationName: "Leader's Mate / Pack Mom",
      className: 'Ancestral Pack Mom & The White Moon of Seven Hills',
      stats: { strength: 8, perception: 14, endurance: 12, charisma: 18, intelligence: 13, agility: 8, luck: 8 },
      traitIds: [
        '_DMMAzBKW3b8wPd9rq6TWp', // The White Moon (Omega)
        '_hgNaenaG3qkHjaHgJFreB', // Dominant Omega
        '_8YMa2gRKXFMBrWYzx2jqD', // Founding Bloodline (ONLY)
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_LNe6dhHnxx7BCfXeMERzc', // Eternal Optimist
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR', // Silver Allergy
        '_JLKHrB9AFqkb1BhT6G3tj'  // Old Money / Aristocrat
      ]
    },
    {
      id: '_W9PLYt9ERTBJBXqKQL2en',
      name: 'Wulfnic Báleygr Bloodmoon',
      lbSearch: 'Wulfnic',
      level: 99,
      birthdate: 0,
      start_timeline_position: 0,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_b8KfUNHq4z3bFw6jKkmzf',
      speciesName: 'Werewolf (Divine Blood Firstborn Primordial)',
      occupationName: 'Firstborn Apex Sovereign',
      className: 'Alpha of Alphas & Omniscient Jarl of California',
      stats: { strength: 16, perception: 12, endurance: 16, charisma: 13, intelligence: 8, agility: 8, luck: 8 },
      traitIds: [
        '_HwqVPTYtptM1Cwz1aCaaJ', // Primordial Enigma
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_1QQ982MmT1fzehNRxq4WU', // Divine Blood (Firstborn)
        '_NL4ANGp2gjKtbAgRTFxbD', // Apex Predator Divine Core
        '_8YMa2gRKXFMBrWYzx2jqD', // Founding Bloodline
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_L2xQk9j8RnMKUgGnCVWRR', // Berserker Internal Furnace
        '_YbYKU6fNwTJgP6x4DPhDT', // Feral Blood
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR'  // Silver Allergy
      ]
    },
    {
      id: '_xHdRRxnHqqGzayzW2E1jN',
      name: 'Echo',
      lbSearch: 'Echo',
      level: 3,
      birthdate: 10486470,
      start_timeline_position: 10486470,
      speciesId: '_92MghbhEBRkmnzJCDBAR7',
      occupationId: '_3mrK4LGktdtUHGbf6CWNp',
      speciesName: 'Macchina & Sintetico (Cyber-Entity Familiar)',
      occupationName: 'Technomancer / Cyber-Mage',
      className: "Jasper's Technomantic Cyber-Familiar",
      stats: { strength: 8, perception: 16, endurance: 8, charisma: 8, intelligence: 20, agility: 13, luck: 8 },
      traitIds: [
        '_hF64363acKFAJCc77xXjE', // Cyber-Augmented
        '_F3Y6PeGWJKq2rk7HKGr9y', // Tech Savvy
        '_AQ6Qy4KHMDgFWKPHDJeqb', // Technomantic Data Resonance
        '_kUV13hFp2R2a4aYEXq3c4', // Familiar Soulbound Synergy
        '_CKqQUUkAh31KTLDkVK96E', // Mastermind
        '_4nTUFT2tfNAjdTKXHfgUc', // Night Stalker
        '_pxQ16JrPDh2H6qAQKgKyx'  // Nerdy / Bookworm
      ]
    }
  ];

  function formatRpgBlock(char) {
    const s = char.stats;
    const traitsList = char.traitIds.map(tid => {
      const tr = traitMapById[tid];
      return `- ${tr ? tr.name : tid}: ${tr ? tr.description : ''}`;
    }).join('\n');

    return `RPG STATS & TRAITS:
[LEVEL: ${char.level}; SPECIES: ${char.speciesName}; OCCUPATION: ${char.occupationName}; CLASS: ${char.className}]
[BASE_STATS: STR ${s.strength}; PER ${s.perception}; END ${s.endurance}; CHA ${s.charisma}; INT ${s.intelligence}; AGI ${s.agility}; LCK ${s.luck}]
TRAITS:
${traitsList}`;
  }

  console.log('================================================================');
  console.log('   ESECUZIONE BATCH 1: WORLD, /mine, LOREBOOK E PERSONA ECHO    ');
  console.log('================================================================\n');

  // 1. WORLD CHARACTERS (10 schede, escluso Alyssa già allineata a mano dall\'utente)
  console.log('--- FASE 1: AGGIORNAMENTO WORLD CHARACTERS (10 SCHEDE) ---');
  for (const c of batch1Definitions) {
    const sum = Object.values(c.stats).reduce((a, b) => a + b, 0);
    if (sum !== 81) throw new Error(`Somma statistiche errata per ${c.name}: ${sum}`);

    const payload = {
      species_id: c.speciesId,
      occupation_id: c.occupationId,
      rpg_stats: {
        species_id: c.speciesId,
        occupation_id: c.occupationId,
        level: c.level,
        base_stats: c.stats
      },
      character_traits: c.traitIds
    };

    if (c.birthdate !== undefined) {
      payload.birthdate = c.birthdate;
      payload.start_timeline_position = c.start_timeline_position;
    }

    const res = await fetch(`https://app.wyvern.chat/api/worlds/characters/${c.id}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      console.log(`[OK] World Char: ${c.name.padEnd(32)} | Lv ${String(c.level).padStart(2)} | Tratti: ${c.traitIds.length}`);
    } else {
      console.error(`[FAIL] World Char: ${c.name} (${res.status})`);
      const err = await res.text();
      console.error(err);
    }
    await new Promise(r => setTimeout(r, 400));
  }

  // 2. SCHEDE STAND-ALONE IN /mine (5 fratelli e zii)
  console.log('\n--- FASE 2: CASCATA SCHEDE STAND-ALONE IN /mine (5 FRATELLI & ZII) ---');
  for (const c of batch1Definitions) {
    if (!c.mineId) continue;
    const resMine = await fetch(`https://app.wyvern.chat/api/characters/${c.mineId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!resMine.ok) {
      console.error(`[FAIL GET] Stand-alone ${c.name} (${c.mineId})`);
      continue;
    }
    const mineChar = await resMine.json();
    let desc = mineChar.description || '';
    const rpgText = formatRpgBlock(c);

    if (desc.includes('RPG STATS & TRAITS:')) {
      desc = desc.split('RPG STATS & TRAITS:')[0].trimEnd() + '\n\n' + rpgText;
    } else {
      desc = desc.trimEnd() + '\n\n' + rpgText;
    }
    desc = desc.replace(/—/g, ', ');

    const putMine = await fetch(`https://app.wyvern.chat/api/characters/${c.mineId}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        description: desc
      })
    });

    if (putMine.ok) {
      console.log(`[OK] Stand-Alone /mine: ${c.name.padEnd(32)} (${c.mineId}) aggiornato con successo!`);
    } else {
      console.error(`[FAIL PUT] Stand-Alone /mine: ${c.name} (${putMine.status})`);
      console.error(await putMine.text());
    }
    await new Promise(r => setTimeout(r, 400));
  }

  // 3. LOREBOOK NPC PRIMARY
  console.log('\n--- FASE 3: CASCATA LOREBOOK NPC PRIMARY (11 VOCI) ---');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lb = await resLb.json();

  let lbUpdatedCount = 0;
  for (const c of batch1Definitions) {
    const entry = lb.lexicon.find(e => (e.name || '').includes(c.lbSearch));
    if (!entry) {
      console.warn(`[WARN] Voce Lorebook non trovata per: ${c.name} (cerca: "${c.lbSearch}")`);
      continue;
    }
    const rpgText = formatRpgBlock(c);
    let content = entry.content;

    if (content.includes('RPG STATS & TRAITS:')) {
      const parts = content.split('RPG STATS & TRAITS:');
      const after = parts[1].indexOf('SYSTEM & ENGINE KEYS:') !== -1 ? '\n\nSYSTEM & ENGINE KEYS:' + parts[1].split('SYSTEM & ENGINE KEYS:')[1] : '';
      content = parts[0].trimEnd() + '\n\n' + rpgText + after;
    } else if (content.includes('SYSTEM & ENGINE KEYS:')) {
      const parts = content.split('SYSTEM & ENGINE KEYS:');
      content = parts[0].trimEnd() + '\n\n' + rpgText + '\n\nSYSTEM & ENGINE KEYS:' + parts[1];
    } else if (content.includes('[INSTRUCTIONS:')) {
      const parts = content.split('[INSTRUCTIONS:');
      content = parts[0].trimEnd() + '\n\n' + rpgText + '\n\n[INSTRUCTIONS:' + parts[1];
    } else {
      content = content.trimEnd() + '\n\n' + rpgText;
    }

    content = content.replace(/—/g, ', ');
    entry.content = content;
    lbUpdatedCount++;
    console.log(`[OK] Preparata voce Lorebook per: ${c.name.padEnd(32)}`);
  }

  const putLbPayload = {
    name: lb.name || "Svartúlfr - NPC Primary",
    description: lb.description || "",
    scan_depth: lb.scan_depth || 5,
    token_budget: lb.token_budget || 5000,
    recursive_scanning: lb.recursive_scanning !== undefined ? lb.recursive_scanning : true,
    visibility: lb.visibility || "private",
    rating: lb.rating || "explicit",
    is_private: lb.is_private || false,
    lexicon: lb.lexicon
  };

  const putLbRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(putLbPayload)
  });

  if (putLbRes.ok) {
    console.log(`[OK] Lorebook NPC Primary salvato con successo! (${lbUpdatedCount} voci aggiornate, metadati preservati)`);
  } else {
    console.error(`[FAIL PUT] Lorebook NPC Primary (${putLbRes.status})`);
    console.error(await putLbRes.text());
  }

  // 4. USER PERSONA ECHO
  console.log('\n--- FASE 4: AGGIORNAMENTO USER PERSONA ECHO ---');
  const resEcho = await fetch(`https://app.wyvern.chat/api/user-personas/${echoPersonaId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const echoDef = batch1Definitions.find(d => d.name === 'Echo');
  if (resEcho.ok && echoDef) {
    const echoPersona = await resEcho.json();
    let desc = echoPersona.description || '';
    const rpgText = formatRpgBlock(echoDef);

    if (desc.includes('RPG STATS & TRAITS:')) {
      desc = desc.split('RPG STATS & TRAITS:')[0].trimEnd() + '\n\n' + rpgText;
    } else {
      desc = desc.trimEnd() + '\n\n' + rpgText;
    }
    desc = desc.replace(/—/g, ', ');

    const putEchoRes = await fetch(`https://app.wyvern.chat/api/user-personas/${echoPersonaId}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        ...echoPersona,
        lorebooks: (echoPersona.lorebooks || []).map(l => l.id || l._id),
        description: desc
      })
    });

    if (putEchoRes.ok) {
      console.log(`[OK] User Persona Echo (${echoPersonaId}) aggiornata con successo!`);
    } else {
      console.error(`[FAIL PUT] User Persona Echo (${putEchoRes.status})`);
      console.error(await putEchoRes.text());
    }
  }

  console.log('\n================================================================');
  console.log('   ESECUZIONE BATCH 1 COMPLETATA CON SUCCESSO!                  ');
  console.log('================================================================\n');
}

executeBatch1().catch(console.error);
