const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
  };
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  console.log('=== STEP 1: CLEANING INTRO PAGES & FIELDS (REMOVING REDUNDANT SPECIES & OCCUPATION QUESTIONS) ===');
  
  // 1. Fetch current world
  const worldRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, { headers });
  const world = await worldRes.json();

  // Filter introduction_pages
  const cleanedPages = (world.introduction_pages || []).filter(p => p.id !== 'p_species_select' && p.id !== 'p_occupation_select');
  
  // Clean intro_fields
  const cleanedFields = { ...world.intro_fields };
  delete cleanedFields['field-species'];
  delete cleanedFields['field-occupation'];

  console.log(`Original pages: ${world.introduction_pages?.length}, Cleaned pages: ${cleanedPages.length}`);
  console.log(`Original fields: ${Object.keys(world.intro_fields || {}).length}, Cleaned fields: ${Object.keys(cleanedFields).length}`);

  // PUT World
  const putWorldRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    method: 'PUT',
    headers,
    body: JSON.stringify({
      introduction_pages: cleanedPages,
      intro_fields: cleanedFields
    })
  });
  console.log('PUT World Status:', putWorldRes.status);

  // Update Scenarios
  const scenariosRes = await fetch(`https://app.wyvern.chat/api/worlds/scenarios/world/${worldId}`, { headers });
  const scenarios = await scenariosRes.json();
  for (const sc of scenarios) {
    console.log(`Updating Scenario [${sc.id}] ${sc.name}...`);
    const putScRes = await fetch(`https://app.wyvern.chat/api/worlds/scenarios/${sc.id}`, {
      method: 'PUT',
      headers,
      body: JSON.stringify({
        fields: cleanedFields
      })
    });
    console.log(`  PUT Scenario status: ${putScRes.status}`);
  }

  console.log('\n=== STEP 2: CONFIGURE THE 21 SVARTULFR RPG SPECIES ===');

  // The 21 canonical species specifications
  const speciesDefs = [
    {
      name: "Licantropo (Werewolf)",
      description: "Predatore lunare del branco Douglas. Dotato di doppio cuore, sensi olfattivi superiori, artigli retrattili e rigenerazione accelerata.",
      stat_modifiers: { strength: 2, endurance: 2, perception: 1, intelligence: -1 }
    },
    {
      name: "Demi-umano (Demihuman)",
      description: "Umanoide con singoli tratti anatomici animali (orecchie e coda singole). Riflessi fulminei, equilibrio perfetto e sensi acuti.",
      stat_modifiers: { agility: 2, perception: 2, charisma: 1, endurance: -1 }
    },
    {
      name: "Umano (Human)",
      description: "Ingegnoso, versatile e tenace. Spina dorsale della societa civile, della ricerca arcana e delle squadre operative DMHA.",
      stat_modifiers: { intelligence: 1, luck: 1, charisma: 1, endurance: 1 }
    },
    {
      name: "Vampiro (Vampire)",
      description: "Predatore notturno immortale sostenuto da sangue sintetico DCC. Carisma aristocratico magnetico, eleganza letale e sensi infallibili.",
      stat_modifiers: { charisma: 2, agility: 1, perception: 1, endurance: -1 }
    },
    {
      name: "Elfo & Sidhe (Elf)",
      description: "Umanoide longevo ed eterico con profonda affinita per le correnti di mana della natura e percezione arcana affinata.",
      stat_modifiers: { intelligence: 2, agility: 1, perception: 1, strength: -1 }
    },
    {
      name: "Demone & Infernale (Demon)",
      description: "Essere legato al fuoco abissale e ai patti vincolanti. Presenza imponente, alta resistenza termica e ferrea volonta.",
      stat_modifiers: { strength: 2, charisma: 1, endurance: 1, luck: -1 }
    },
    {
      name: "Fata & Fae (Fairy)",
      description: "Piccolo Popolo dei boschi e delle corti faeriche. Maestri di inganni, illusioni sensoriali, furtivita e fortuna sfuggente.",
      stat_modifiers: { agility: 2, luck: 2, charisma: 1, strength: -2 }
    },
    {
      name: "Angelo & Celestiale (Angel)",
      description: "Essere di emanazione sacra radiante autorita protettiva, magia di risanamento miracolosa e inflessibile giustizia.",
      stat_modifiers: { charisma: 2, endurance: 1, strength: 1, luck: -1 }
    },
    {
      name: "Drago & Drake (Dragon)",
      description: "Colosso draconico corazzato da scaglie resistenti. Respiro elementale primordiale, fierezza d'animo e potenza d'impatto sovrumana.",
      stat_modifiers: { strength: 2, endurance: 2, charisma: 1, agility: -1 }
    },
    {
      name: "Orco & Oni (Orc)",
      description: "Guerriero titanico dalla possente massa muscolare e corna cerchiate. Travolgente forza d'urto e incrollabile tempra marziale.",
      stat_modifiers: { strength: 3, endurance: 2, intelligence: -1, charisma: -1 }
    },
    {
      name: "Succube & Incubo (Succubus)",
      description: "Maestro empatico dell'attrazione e delle energie sottili. Tesse fili emozionali, dissipa tensioni o soggioga con fascino magnetico.",
      stat_modifiers: { charisma: 3, agility: 1, endurance: -1, strength: -1 }
    },
    {
      name: "Minotauro & Centauro (Minotaur)",
      description: "Pilastro taurino o equino di stazza imponente. Carica cinetica inarrestabile, tenacia da assedio e massiccia stabilita fisica.",
      stat_modifiers: { strength: 2, endurance: 3, agility: -1, intelligence: -1 }
    },
    {
      name: "Tritone & Sirena (Merfolk)",
      description: "Umanoide acquatico dei fondali di Blackwood Bay. Padroneggia l'idromanzia, l'agilita subacquea fluida e il canto delle correnti.",
      stat_modifiers: { agility: 2, endurance: 1, intelligence: 1, perception: -1 }
    },
    {
      name: "Kitsune & Neko (Beast Spirit)",
      description: "Spirito volpe o felino dai riflessi acrobatici e molteplici code. Astuzia vivace, fascino naturale e destrezza urbana eccezionale.",
      stat_modifiers: { agility: 2, charisma: 2, luck: 1, strength: -1 }
    },
    {
      name: "Mutaforma & Antro (Shifter)",
      description: "Essere dai contorni biologici plastici capace di adattare forma, densita e attributi animali al contesto operativo.",
      stat_modifiers: { endurance: 2, agility: 1, perception: 1, charisma: -1 }
    },
    {
      name: "Non-Morto & Revenant (Undead)",
      description: "Corpo rianimato immune alla stanchezza, ai veleni e al dolore fisico. Freddo e calcolatore, animato da pura volonta psichica.",
      stat_modifiers: { endurance: 3, intelligence: 1, charisma: -2, luck: -1 }
    },
    {
      name: "Lamia & Naga (Serpentine)",
      description: "Fisiologia serpentina sinuosa e ipnotica. Presa costrittiva poderosa, percezione termica e tossine paralizzanti.",
      stat_modifiers: { agility: 2, perception: 2, endurance: 1, strength: -1 }
    },
    {
      name: "Aracnide & Drider (Arachne)",
      description: "Tessitore ibrido che domina agguati, filamenti di seta arcanamente rinforzati e letali veleni neurotossici.",
      stat_modifiers: { perception: 2, agility: 1, endurance: 1, charisma: -1 }
    },
    {
      name: "Macchina & Sintetico (Machine)",
      description: "Costrutto cibernetico o androide runico alimentato da micro-core magici. Logica impeccabile, corazza pesante e totale immunita biologica.",
      stat_modifiers: { intelligence: 2, endurance: 2, strength: 1, charisma: -2 }
    },
    {
      name: "Mutante & Ibrido (Mutant)",
      description: "Creatura esposta ai gradienti di mana instabile dei Rift abissali. Fisiologia adattiva imprevedibile e colpi di fortuna anomali.",
      stat_modifiers: { endurance: 2, strength: 1, luck: 2, charisma: -1 }
    },
    {
      name: "Divinita & Primordiale (Demigod)",
      description: "Incarnazione terrena di antiche potenze cosmiche. Presenza maestosa che piega la realta e comanda rispetto assoluto.",
      stat_modifiers: { charisma: 2, strength: 1, intelligence: 1, endurance: 1, luck: -1 }
    }
  ];

  // Fetch current live species
  const curSpeciesRes = await fetch(`https://app.wyvern.chat/api/worlds/rpg/species/${worldId}`, { headers });
  const liveSpecies = await curSpeciesRes.json();
  console.log(`Live RPG species count on server: ${liveSpecies.length}`);

  // 1. Update the existing slots with our 21 definitions
  for (let i = 0; i < speciesDefs.length; i++) {
    const def = speciesDefs[i];
    if (i < liveSpecies.length) {
      const existing = liveSpecies[i];
      console.log(`Updating species [${existing.id}] -> ${def.name}...`);
      const putRes = await fetch(`https://app.wyvern.chat/api/worlds/rpg/species/${existing.id}`, {
        method: 'PUT',
        headers,
        body: JSON.stringify({
          name: def.name,
          description: def.description,
          stat_modifiers: def.stat_modifiers,
          player_selectable: true,
          display_order: i
        })
      });
      console.log(`  PUT status: ${putRes.status}`);
    } else {
      console.log(`Creating new species: ${def.name}...`);
      const postRes = await fetch(`https://app.wyvern.chat/api/worlds/rpg/species`, {
        method: 'POST',
        headers,
        body: JSON.stringify({
          world_id: worldId,
          name: def.name,
          description: def.description,
          stat_modifiers: def.stat_modifiers,
          player_selectable: true,
          display_order: i
        })
      });
      console.log(`  POST status: ${postRes.status}`);
    }
  }

  // 2. Delete any surplus species if liveSpecies.length > speciesDefs.length
  if (liveSpecies.length > speciesDefs.length) {
    for (let i = speciesDefs.length; i < liveSpecies.length; i++) {
      const surplus = liveSpecies[i];
      console.log(`Deleting surplus species [${surplus.id}] ("${surplus.name}")...`);
      const delRes = await fetch(`https://app.wyvern.chat/api/worlds/rpg/species/${surplus.id}`, {
        method: 'DELETE',
        headers
      });
      console.log(`  DELETE status: ${delRes.status}`);
    }
  }

  // 3. Verify final list
  console.log('\n=== FINAL VERIFICATION ===');
  const finalRes = await fetch(`https://app.wyvern.chat/api/worlds/rpg/species/${worldId}`, { headers });
  const finalList = await finalRes.json();
  console.log(`Final species count on server: ${finalList.length}`);
  finalList.forEach((s, idx) => {
    console.log(`[${idx + 1}] ID: ${s.id} | Name: "${s.name}" | Modifiers: ${JSON.stringify(s.stat_modifiers)}`);
  });
}

main().catch(console.error);
