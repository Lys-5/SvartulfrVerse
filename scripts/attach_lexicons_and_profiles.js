const fs = require('fs');

async function attachLexiconsAndProfiles() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  // 1. Associazione delle voci di Lexicon tramite attached_world_character_id
  const lexiconBindings = [
    // Wulfnic Bloodmoon (_W9PLYt9ERTBJBXqKQL2en)
    { lexiconId: '_WJWnx4N194daLFkqGxp8R', charId: '_W9PLYt9ERTBJBXqKQL2en', name: 'Wulfnic Apex' },
    // Ut Berg (_NYtBzeKNkm3pedHMnYaka)
    { lexiconId: '_zD4Mma4YDmLUxNhAKcwPq', charId: '_NYtBzeKNkm3pedHMnYaka', name: 'Ut Berg Apex' },
    // Zefir Hvitskog (_FJhtBq4xUM4aUWpaJAPYF)
    { lexiconId: '_7gNVDmqBx7RXN7emQ64LG', charId: '_FJhtBq4xUM4aUWpaJAPYF', name: 'Zefir Apex' },
    // Malachia Douglas (_rAcN9GXD1Le4WxY28e49W)
    { lexiconId: '_J883n9w7LPFnATmkH18PQ', charId: '_rAcN9GXD1Le4WxY28e49W', name: 'Malachia Fornace Interna' },
    { lexiconId: '_B6DUUmVbfq3prV3NF3xGU', charId: '_rAcN9GXD1Le4WxY28e49W', name: 'Malachia Furia Berserker' },
    // Angelo Moreno (_mwqYFKwWfHDMctDJQMR6w)
    { lexiconId: '_EXT2mccBLN9wJ1Pt69qzx', charId: '_mwqYFKwWfHDMctDJQMR6w', name: 'Angelo Puppet Master' },
    { lexiconId: '_kCkV96ehYJnQDy8x6NyY7', charId: '_mwqYFKwWfHDMctDJQMR6w', name: 'Angelo Fili di Mana' },
    { lexiconId: '_jKn9BHQXztHqjegeAY2fd', charId: '_mwqYFKwWfHDMctDJQMR6w', name: 'Angelo Palazzo Mentale' },
    // Jasper Douglas (_x3VY2kcbaDbKyCqywGeET)
    { lexiconId: '_UYe9MV2eEEVYjMKw27HVU', charId: '_x3VY2kcbaDbKyCqywGeET', name: 'Jasper Technomancer' },
    { lexiconId: '_q1CyTUwGeULUdYU7NW3xq', charId: '_x3VY2kcbaDbKyCqywGeET', name: 'Jasper Proiezione Eterica' },
    // Alyssa Douglas (_MXcEC8Y6B3BNm3b1ttHj6)
    { lexiconId: '_XYk23YkzMhqwzxpVwbH2t', charId: '_MXcEC8Y6B3BNm3b1ttHj6', name: 'Alyssa Famigli' },
    { lexiconId: '_rtaqBgdMtgQe7arh9qAaT', charId: '_MXcEC8Y6B3BNm3b1ttHj6', name: 'Alyssa Rito Vincolo Famiglio' }
  ];

  console.log('--- FASE 1: Aggiornamento attached_world_character_id nei Lexicon ---');
  for (const b of lexiconBindings) {
    const res = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${b.lexiconId}`, {
      method: 'PUT',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        attached_world_character_id: b.charId
      })
    });
    console.log(`Lexicon ${b.name} (${b.lexiconId}) -> Char ${b.charId} [Status: ${res.status}]`);
    await new Promise(r => setTimeout(r, 100));
  }

  // 2. Aggiornamento Occupazioni e Tratti RPG sui Personaggi
  console.log('\n--- FASE 2: Aggiornamento Occupazioni e Tratti RPG sui Personaggi ---');

  const charUpdates = [
    {
      cid: '_rAcN9GXD1Le4WxY28e49W', // Malachia
      name: 'Malachia Douglas Bloodmoon',
      occupationId: '_d7mHQJKnQqQNzwdwnqMdM', // Guild Berserker (Vanguard)
      newTraits: ['_L2xQk9j8RnMKUgGnCVWRR']   // Berserker Internal Furnace
    },
    {
      cid: '_mwqYFKwWfHDMctDJQMR6w', // Angelo Moreno
      name: 'Angelo Moreno',
      occupationId: '_4mxkMwTthmXt9AqXXdxfE', // Puppet Master (Mind Weaver)
      newTraits: ['_C8XXTwLd1mmF33EkQMUyD']   // Puppeteer Mana Strings
    },
    {
      cid: '_x3VY2kcbaDbKyCqywGeET', // Jasper Douglas
      name: 'Jasper Douglas Bloodmoon',
      occupationId: '_3mrK4LGktdtUHGbf6CWNp', // Technomancer / Cyber-Mage
      newTraits: ['_AQ6Qy4KHMDgFWKPHDJeqb']   // Technomantic Data Resonance
    },
    {
      cid: '_W9PLYt9ERTBJBXqKQL2en', // Wulfnic Bloodmoon
      name: 'Wulfnic Bloodmoon',
      occupationId: '_b8KfUNHq4z3bFw6jKkmzf', // Firstborn Apex Sovereign
      newTraits: ['_NL4ANGp2gjKtbAgRTFxbD']   // Apex Predator Divine Core
    },
    {
      cid: '_NYtBzeKNkm3pedHMnYaka', // Ut Berg
      name: 'Ut Berg',
      occupationId: '_b8KfUNHq4z3bFw6jKkmzf', // Firstborn Apex Sovereign
      newTraits: ['_NL4ANGp2gjKtbAgRTFxbD']   // Apex Predator Divine Core
    },
    {
      cid: '_FJhtBq4xUM4aUWpaJAPYF', // Zefir Hvitskog
      name: 'Zefir Hvitskog',
      occupationId: '_b8KfUNHq4z3bFw6jKkmzf', // Firstborn Apex Sovereign
      newTraits: ['_NL4ANGp2gjKtbAgRTFxbD']   // Apex Predator Divine Core
    },
    {
      cid: '_MXcEC8Y6B3BNm3b1ttHj6', // Alyssa Douglas
      name: 'Alyssa Douglas Bloodmoon',
      occupationId: null, // Mantiene Guild Support / Pre-Med
      newTraits: ['_kUV13hFp2R2a4aYEXq3c4'] // Familiar Soulbound Synergy
    }
  ];

  for (const cu of charUpdates) {
    // 1. Leggiamo lo stato attuale del personaggio per preservare tratti esistenti
    const getRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${cu.cid}`, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
    if (!getRes.ok) {
      console.error(`Errore lettura ${cu.name}: ${getRes.status}`);
      continue;
    }
    const cData = await getRes.json();
    const existingTraits = cData.character_traits || [];
    
    // Unione tratti esistenti con i nuovi
    const existingIds = existingTraits.map(t => (typeof t === 'string' ? t : (t.id || t._id)));
    const mergedIds = [...new Set([...existingIds, ...cu.newTraits])];

    const patchPayload = {
      character_traits: mergedIds
    };

    if (cu.occupationId) {
      patchPayload.rpg_stats = {
        ...(cData.rpg_stats || {}),
        occupation_id: cu.occupationId
      };
    }

    const putRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${cu.cid}`, {
      method: 'PUT',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(patchPayload)
    });

    console.log(`Character ${cu.name} aggiornato [Status: ${putRes.status}]`);
    await new Promise(r => setTimeout(r, 120));
  }

  console.log('\nTutte le associazioni incrociate sono state completate!');
}

attachLexiconsAndProfiles();
