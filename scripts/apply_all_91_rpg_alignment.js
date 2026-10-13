const fs = require('fs');

async function applyAllRpgAlignment() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const plan = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_91_characters_rpg_plan.json', 'utf8'));

  console.log(`Avvio applicazione RPG per tutti i ${plan.length} personaggi su Wyvern...`);

  let success = 0;
  let errors = 0;

  for (let i = 0; i < plan.length; i++) {
    const item = plan[i];

    // 1. Lettura dello stato attuale del personaggio per conservare level, birthdate, ecc.
    try {
      const getRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${item.cid}`, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (!getRes.ok) {
        console.error(`\n[ERRORE GET ${getRes.status}] ${item.name}`);
        errors++;
        continue;
      }
      const cData = await getRes.json();
      const currentRpg = cData.rpg_stats || {};

      const patchPayload = {
        character_traits: item.character_traits,
        rpg_stats: {
          ...currentRpg,
          species_id: item.species_id,
          occupation_id: item.occupation_id,
          base_stats: item.base_stats
        }
      };

      const putRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${item.cid}`, {
        method: 'PUT',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(patchPayload)
      });

      if (putRes.ok) {
        success++;
        process.stdout.write(`\r[${i + 1}/${plan.length}] Aggiornato: ${item.name.slice(0, 35)} (${item.character_traits.length} tratti)`);
      } else {
        const errText = await putRes.text();
        console.error(`\n[ERRORE PUT ${putRes.status}] ${item.name}: ${errText.slice(0, 100)}`);
        errors++;
      }
    } catch (e) {
      console.error(`\n[ECCEZIONE] ${item.name}: ${e.message}`);
      errors++;
    }

    await new Promise(r => setTimeout(r, 120));
  }

  console.log(`\n\nOperazione completata! Successi: ${success}, Errori: ${errors}`);
}

applyAllRpgAlignment();
