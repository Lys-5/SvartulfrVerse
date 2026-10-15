const fs = require('fs');

async function executeBatch2() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const lbId = '_LBkRWNpPxpdn6dxYaDU2b'; // Svartúlfr - NPC Primary

  const traitsCatalog = JSON.parse(fs.readFileSync('scratch/rpg_traits_catalog.json', 'utf8'));
  const traitMapById = {};
  traitsCatalog.forEach(t => { traitMapById[t.id] = t; });

  const batch2Definitions = [
    {
      id: '_FJhtBq4xUM4aUWpaJAPYF',
      name: 'Zefir Hvitskog',
      lbSearch: 'Zefir',
      level: 99,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_yCNjpDEBrLGbMK73CrBzR',
      speciesName: 'Werewolf (Divine Blood Firstborn Primordial)',
      occupationName: 'Scout',
      className: 'Primordial Shadow Scout & Snow-Wolf Sovereign',
      stats: { strength: 12, perception: 18, endurance: 14, charisma: 8, intelligence: 11, agility: 10, luck: 8 },
      traitIds: [
        '_HwqVPTYtptM1Cwz1aCaaJ', // Primordial Enigma
        '_1QQ982MmT1fzehNRxq4WU', // Divine Blood (Firstborn)
        '_8YMa2gRKXFMBrWYzx2jqD', // Founding Bloodline
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_NL4ANGp2gjKtbAgRTFxbD', // Apex Predator Divine Core
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_4nTUFT2tfNAjdTKXHfgUc', // Night Stalker
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR'  // Silver Allergy
      ]
    },
    {
      id: '_NYtBzeKNkm3pedHMnYaka',
      name: 'Ut Berg',
      lbSearch: 'Ut',
      level: 99,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_fgTDn33yV6eE9HEmm3qec',
      speciesName: 'Werewolf (Divine Blood Firstborn Primordial)',
      occupationName: 'Guild Tank',
      className: 'Primordial Mountain Titan & Vanguard Breaker',
      stats: { strength: 18, perception: 10, endurance: 18, charisma: 11, intelligence: 8, agility: 8, luck: 8 },
      traitIds: [
        '_HwqVPTYtptM1Cwz1aCaaJ', // Primordial Enigma
        '_1QQ982MmT1fzehNRxq4WU', // Divine Blood (Firstborn)
        '_8YMa2gRKXFMBrWYzx2jqD', // Founding Bloodline
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_NL4ANGp2gjKtbAgRTFxbD', // Apex Predator Divine Core
        '_L2xQk9j8RnMKUgGnCVWRR', // Berserker Internal Furnace
        '_YbYKU6fNwTJgP6x4DPhDT', // Feral Blood
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K'  // Regenerative Factor
      ]
    },
    {
      id: '_b7QqV43D8pU1tewx4qenY',
      name: 'Major Kaladin Blackwolf Nargathon',
      lbSearch: 'Kaladin',
      level: 6,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_12YM878yc9tkLC32Lfdhx',
      speciesName: 'Werewolf (Modified / Lab Lineage)',
      occupationName: 'DCC Security / PMC',
      className: 'DCC Security Division Commander & Subject Zero',
      stats: { strength: 15, perception: 14, endurance: 15, charisma: 11, intelligence: 10, agility: 8, luck: 8 },
      traitIds: [
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_YT36NBpQWKPTwqwRNeGzp', // Modified / Lab Lineage
        '_7a2b7jHqJ7MdbNXQCxG34', // S.R.F. Veteran
        '_VrgTBJR3aEyW3FBD1zLkR', // Dungeon Veteran
        '_ycHNkaW9aEjTxppUe6Wtg', // Knight in Sour Armor
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR', // Silver Allergy
        '_F3Y6PeGWJKq2rk7HKGr9y'  // Tech Savvy
      ]
    },
    {
      id: '_6hc62Ay9tVBXecnAfmqdU',
      name: 'Archer Wolfwood',
      lbSearch: 'Archer',
      level: 34,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_12YM878yc9tkLC32Lfdhx',
      speciesName: 'Werewolf (Pureblood Lineage)',
      occupationName: 'DCC Security / PMC',
      className: 'Wolfwood House Head & Senior DCC Security Liaison',
      stats: { strength: 12, perception: 14, endurance: 12, charisma: 15, intelligence: 12, agility: 8, luck: 8 },
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
      id: '_YY8VbpgzYk4dfFAL78rM3',
      name: 'Mackenzie Sanchez-Rogers',
      mineId: '_HqzMU3zVrgHaHBFKw4nQA',
      lbSearch: 'Mackenzie',
      level: 4,
      speciesId: '_wyAYU2Mn7AkQ1hVej7PdW',
      occupationId: '_R3MA2NAW1yXtXDT4KkqqN',
      speciesName: 'Werewolf (Pureblood Rogers & Common Sanchez)',
      occupationName: 'Street Scrapper / Rogue',
      className: 'Underground Street Fighter & Protective Brawler',
      stats: { strength: 14, perception: 12, endurance: 14, charisma: 11, intelligence: 8, agility: 14, luck: 8 },
      traitIds: [
        '_jyDzgjNM8BmbrNC3AxcfB', // Dominant Alpha
        '_MRxrtF9paJmcB13fAnE9g', // Alpha Command
        '_an1zbcGY7MYWA2qHeCzba', // Pureblood Lineage (Rogers)
        '_fYMTrnz7V4Vd7DECCxLMm', // Common Lupine Blood (Sanchez)
        '_URpa2cwkJQgVYt9j966JW', // Rebel Heart / Underground
        '_YbYKU6fNwTJgP6x4DPhDT', // Feral Blood
        '_VrgTBJR3aEyW3FBD1zLkR', // Dungeon Veteran
        '_VVnrtkB9fn9gr1zMwFRyM', // Lupine Senses
        '_8B9wFbE8xag2a2dWTVE9b', // Partial Shift Mastery
        '_nKtryaNUjK1edMnBNjL9K', // Regenerative Factor
        '_EG7K3mQqJhgaUr7KkYxJR', // Silver Allergy
        '_AMT6xk8rnrT9E9Vx8mhdq'  // The Weight He Carries
      ]
    },
    {
      id: '_PQHGb4gL2LwDhNDrLFa3A',
      name: 'Finnegan Novak',
      lbSearch: 'Finn',
      level: 3,
      speciesId: '_pf9FRybEA1Y7naxw7TDQE',
      occupationId: '_GwQBtq3JX8MGjF6QYpVkg',
      speciesName: 'Demi-umano (Arctic Wolf Kemonomimi)',
      occupationName: 'Pro Athlete / Fighter',
      className: 'SUCC Bears Left Wing (Varsity Hockey Athlete)',
      stats: { strength: 12, perception: 12, endurance: 14, charisma: 11, intelligence: 9, agility: 15, luck: 8 },
      traitIds: [
        '_8AYDaJ2xJaP7Vhe26M1jA', // Gentle Giant
        '_URpa2cwkJQgVYt9j966JW', // Rebel Heart / Underground
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_ycHNkaW9aEjTxppUe6Wtg', // Knight in Sour Armor
        '_LNe6dhHnxx7BCfXeMERzc', // Eternal Optimist
        '_F3Y6PeGWJKq2rk7HKGr9y'  // Tech Savvy
      ]
    },
    {
      id: '_a6KYGdN3BWTgbYEbT4mx8',
      name: 'Zeera Darkfire',
      mineId: '_tJ8zaBLAb6n7XAyd8qhHQ',
      lbSearch: 'Zeera',
      level: 6,
      speciesId: '_FQJetrfXHAA4TyachJqwU',
      occupationId: '_eFTUaaMbVTByeDbbM9cLP',
      speciesName: 'Demone & Infernale (High Infernal Bloodline)',
      occupationName: 'Diplomat',
      className: 'Horned Skull Clan Leader & CEO of HSK Consulting',
      stats: { strength: 10, perception: 12, endurance: 12, charisma: 17, intelligence: 14, agility: 8, luck: 8 },
      traitIds: [
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_JLKHrB9AFqkb1BhT6G3tj', // Old Money / Aristocrat
        '_CKqQUUkAh31KTLDkVK96E', // Mastermind
        '_4nTUFT2tfNAjdTKXHfgUc', // Night Stalker
        '_VrgTBJR3aEyW3FBD1zLkR', // Dungeon Veteran
        '_C8XXTwLd1mmF33EkQMUyD', // Puppeteer Mana Strings
        '_AMT6xk8rnrT9E9Vx8mhdq'  // The Weight He Carries
      ]
    },
    {
      id: '_BzKwAkgpPfbVkBzbDaEth',
      name: 'Jared Thompson',
      mineId: '_G4126zBQhWEtFkKCG3Dw3',
      lbSearch: 'Jared',
      level: 3,
      speciesId: '_nUm9xyCztM9UR8HktQneq',
      occupationId: '_GwQBtq3JX8MGjF6QYpVkg',
      speciesName: 'Minotauro & Centauro (Half-Minotaur Hybrid)',
      occupationName: 'Pro Athlete / Fighter',
      className: 'SUCC Bulls Starting Quarterback & Beta Rho Omega Frat',
      stats: { strength: 16, perception: 10, endurance: 16, charisma: 14, intelligence: 8, agility: 9, luck: 8 },
      traitIds: [
        '_8AYDaJ2xJaP7Vhe26M1jA', // Gentle Giant
        '_URpa2cwkJQgVYt9j966JW', // Rebel Heart / Underground
        '_LNe6dhHnxx7BCfXeMERzc', // Eternal Optimist
        '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
        '_CBcWYUneXXPwpyEq2Mjcm', // Ancient Heritage
        '_YbYKU6fNwTJgP6x4DPhDT'  // Feral Blood
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
  console.log('   ESECUZIONE BATCH 2: FIRSTBORNS, PMC, ALLIES, /mine & LOREBOOK ');
  console.log('================================================================\n');

  // 1. WORLD CHARACTERS (8 schede)
  console.log('--- FASE 1: AGGIORNAMENTO WORLD CHARACTERS (8 SCHEDE) ---');
  for (const c of batch2Definitions) {
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

  // 2. SCHEDE STAND-ALONE IN /mine (Mackenzie, Zeera, Jared)
  console.log('\n--- FASE 2: CASCATA SCHEDE STAND-ALONE IN /mine (MACKENZIE, ZEERA, JARED) ---');
  for (const c of batch2Definitions) {
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

  // 3. LOREBOOK NPC PRIMARY (8 VOCI)
  console.log('\n--- FASE 3: CASCATA LOREBOOK NPC PRIMARY (8 VOCI) ---');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lb = await resLb.json();

  let lbUpdatedCount = 0;
  for (const c of batch2Definitions) {
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

  console.log('\n================================================================');
  console.log('   ESECUZIONE BATCH 2 COMPLETATA CON SUCCESSO!                  ');
  console.log('================================================================\n');
}

executeBatch2().catch(console.error);
