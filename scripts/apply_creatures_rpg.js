const fs = require('fs');

async function applyCreaturesRpg() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const creaturesPlan = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_creatures_rpg_plan.json', 'utf8'));

  console.log(`Avvio applicazione RPG per ${creaturesPlan.length} creature / mostri / mob su Wyvern...`);

  let success = 0;
  let errors = 0;

  for (let i = 0; i < creaturesPlan.length; i++) {
    const item = creaturesPlan[i];

    try {
      // 1. GET stato attuale
      const getRes = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${item.id}`, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (!getRes.ok) {
        console.error(`\n[ERRORE GET ${getRes.status}] ${item.name} (${item.id})`);
        errors++;
        continue;
      }
      const currentData = await getRes.json();
      const existingExtensions = currentData.extensions || {};

      const patchPayload = {
        name: item.name,
        lexicon_species_id: item.species_id,
        lexicon_occupation_id: item.occupation_id,
        extensions: {
          ...existingExtensions,
          rpg: {
            level: item.level,
            base_stats: item.base_stats,
            traits: item.traits
          }
        }
      };

      const putRes = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${item.id}`, {
        method: 'PUT',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(patchPayload)
      });

      if (putRes.ok) {
        success++;
        console.log(`[${i + 1}/${creaturesPlan.length}] Aggiornata Creatura: ${item.name} (Lv ${item.level}, ${item.traits.length} tratti)`);
      } else {
        const errText = await putRes.text();
        console.error(`\n[ERRORE PUT ${putRes.status}] ${item.name}: ${errText.slice(0, 100)}`);
        errors++;
      }
    } catch (e) {
      console.error(`\n[ECCEZIONE] ${item.name}: ${e.message}`);
      errors++;
    }

    await new Promise(r => setTimeout(r, 150));
  }

  console.log(`\nApplicazione Creature completata! Successi: ${success}, Errori: ${errors}`);
}

applyCreaturesRpg();
