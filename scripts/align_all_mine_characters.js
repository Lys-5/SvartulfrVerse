const fs = require('fs');

async function alignAllMineCharacters() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldData = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
  const worldChars = worldData.world_characters || [];

  const mapping = [
    { mineId: '_t4J9aQNJM36cUKAP4wB4U', worldId: '_x3VY2kcbaDbKyCqywGeET', name: 'Jasper Douglas Bloodmoon' },
    { mineId: '_EWqmxx3Q1fdK97AVBRqEW', worldId: '_d44gDc8N18kkbEhAcfUCG', name: 'Erik Douglas' },
    { mineId: '_AjphrWj2BMT9KJTx4KETE', worldId: '_r42cVzMjcGTAx7bR1DQVt', name: 'Noah Douglas Bloodmoon' },
    { mineId: '_yQeae3DnARft2RH4gaFNx', worldId: '_rAcN9GXD1Le4WxY28e49W', name: 'Malachia Douglas Bloodmoon' },
    { mineId: '_BQ4THBW3BKL2RN9Xy4YHb', worldId: '_JL37wK9PQMNDChULCDrWj', name: 'Logan Douglas' },
    { mineId: '_tJ8zaBLAb6n7XAyd8qhHQ', worldId: '_a6KYGdN3BWTgbYEbT4mx8', name: 'Zeera Darkfire' },
    { mineId: '_G4126zBQhWEtFkKCG3Dw3', worldId: '_BzKwAkgpPfbVkBzbDaEth', name: 'Jared Thompson' },
    { mineId: '_HqzMU3zVrgHaHBFKw4nQA', worldId: '_YY8VbpgzYk4dfFAL78rM3', name: 'Mackenzie "Mac" Sanchez-Rogers' }
  ];

  const lorebookIds = [
    '_xZkWyqB9z1C3QMQp71kXh',
    '_kPzhnGxaRgCMdmgrwWjbY',
    '_J8x7fwRrpa9C6Wct6hb7p',
    '_V6jT3gPWDCPdxT2bCedeG'
  ];

  console.log(`Avvio allineamento di ${mapping.length} personaggi stand-alone in /mine al World...`);

  let success = 0;
  let errors = 0;

  for (let i = 0; i < mapping.length; i++) {
    const item = mapping[i];
    const wChar = worldChars.find(c => c.id === item.worldId);
    if (!wChar) {
      console.error(`[ERRORE] World character non trovato per ${item.name} (${item.worldId})`);
      errors++;
      continue;
    }

    try {
      // 1. GET scheda attuale in /mine
      const getRes = await fetch(`https://app.wyvern.chat/api/characters/${item.mineId}`, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (!getRes.ok) {
        console.error(`[ERRORE GET ${getRes.status}] ${item.name} (${item.mineId})`);
        errors++;
        continue;
      }
      const mineData = await getRes.json();

      // Mantenimento outfits esistenti o sincronizzazione con World
      let outfits = mineData.outfits || [];
      if (wChar.outfits && wChar.outfits.length > outfits.length) {
        outfits = wChar.outfits;
      }

      // Preparazione payload aggiornato conforme alle regole di GEMINI.md
      const patchPayload = {
        name: wChar.name || wChar.display_name,
        display_name: wChar.display_name,
        avatar: wChar.avatar || mineData.avatar,
        description: (wChar.long_summary || '').replace(/—/g, ', '),
        personality: (wChar.summary || '').replace(/—/g, ', '),
        post_history_instructions: (wChar.final_instructions || mineData.post_history_instructions || '').replace(/—/g, ', '),
        linked_world: '_CgYT8fHXpDC4crjmegQF7',
        lorebooks: lorebookIds,
        outfits: outfits
      };

      const putRes = await fetch(`https://app.wyvern.chat/api/characters/${item.mineId}`, {
        method: 'PUT',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(patchPayload)
      });

      if (putRes.ok) {
        success++;
        console.log(`[${i + 1}/${mapping.length}] Sincronizzato con successo: ${item.name}`);
      } else {
        const errText = await putRes.text();
        console.error(`[ERRORE PUT ${putRes.status}] ${item.name}: ${errText.slice(0, 100)}`);
        errors++;
      }
    } catch (e) {
      console.error(`[ECCEZIONE] ${item.name}: ${e.message}`);
      errors++;
    }

    await new Promise(r => setTimeout(r, 200));
  }

  console.log(`\nAllineamento Characters /mine completato! Successi: ${success}, Errori: ${errors}`);
}

alignAllMineCharacters();
