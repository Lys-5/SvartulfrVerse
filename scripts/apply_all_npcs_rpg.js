const fs = require('fs');

async function refreshToken() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rt = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt', 'utf8').trim();
  const res = await fetch(`https://securetoken.googleapis.com/v1/token?key=${ak}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grant_type: 'refresh_token', refresh_token: rt })
  });
  const data = await res.json();
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', data.id_token, 'utf8');
  return data.id_token;
}

async function applyAllNpcsRpg() {
  let token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const npcsPlan = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_npcs_rpg_plan.json', 'utf8'));

  console.log(`Avvio applicazione RPG per ${npcsPlan.length} NPC terziari nel Lexicon su Wyvern (con auto-refresh token)...`);

  let success = 0;
  let errors = 0;

  for (let i = 0; i < npcsPlan.length; i++) {
    const item = npcsPlan[i];

    let attempts = 0;
    let updated = false;

    while (attempts < 2 && !updated) {
      attempts++;
      try {
        // 1. GET stato attuale
        let getRes = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${item.id}`, {
          headers: { 'Authorization': 'Bearer ' + token }
        });

        if (getRes.status === 401 || getRes.status === 404) {
          // Token scaduto: rinfresca e riprova
          token = await refreshToken();
          getRes = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${item.id}`, {
            headers: { 'Authorization': 'Bearer ' + token }
          });
        }

        if (!getRes.ok) {
          console.error(`\n[ERRORE GET ${getRes.status}] ${item.name} (${item.id})`);
          break;
        }

        const currentData = await getRes.json();
        const existingExtensions = currentData.extensions || {};

        const patchPayload = {
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

        let putRes = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${item.id}`, {
          method: 'PUT',
          headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(patchPayload)
        });

        if (putRes.status === 401) {
          token = await refreshToken();
          putRes = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${item.id}`, {
            method: 'PUT',
            headers: {
              'Authorization': 'Bearer ' + token,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(patchPayload)
          });
        }

        if (putRes.ok) {
          success++;
          updated = true;
          process.stdout.write(`\r[${i + 1}/${npcsPlan.length}] Aggiornato NPC: ${item.name.slice(0, 30).padEnd(30)} (Lv ${item.level}, ${item.traits.length} tratti)`);
        } else {
          const errText = await putRes.text();
          console.error(`\n[ERRORE PUT ${putRes.status}] ${item.name}: ${errText.slice(0, 100)}`);
        }
      } catch (e) {
        console.error(`\n[ECCEZIONE] ${item.name}: ${e.message}`);
      }
    }

    if (!updated) {
      errors++;
    }

    // Pausa di 120ms per non saturare i rate limits
    await new Promise(r => setTimeout(r, 120));
  }

  console.log(`\n\nApplicazione NPC terziari completata! Successi: ${success}, Errori: ${errors}`);
}

applyAllNpcsRpg();
