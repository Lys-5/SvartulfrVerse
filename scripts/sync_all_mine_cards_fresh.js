const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();

const worldChars = JSON.parse(fs.readFileSync('scratch/fresh_world_chars.json', 'utf8'));

const mapping = [
  { mineId: '_t4J9aQNJM36cUKAP4wB4U', worldId: '_x3VY2kcbaDbKyCqywGeET', name: 'Jasper Douglas Bloodmoon' },
  { mineId: '_EWqmxx3Q1fdK97AVBRqEW', worldId: '_d44gDc8N18kkbEhAcfUCG', name: 'Erik Douglas' },
  { mineId: '_AjphrWj2BMT9KJTx4KETE', worldId: '_r42cVzMjcGTAx7bR1DQVt', name: 'Noah Douglas Bloodmoon' },
  { mineId: '_yQeae3DnARft2RH4gaFNx', worldId: '_rAcN9GXD1Le4WxY28e49W', name: 'Malachia Douglas Bloodmoon' },
  { mineId: '_BQ4THBW3BKL2RN9Xy4YHb', worldId: '_JL37wK9PQMNDChULCDrWj', name: 'Logan Douglas' },
  { mineId: '_tJ8zaBLAb6n7XAyd8qhHQ', worldId: '_a6KYGdN3BWTgbYEbT4mx8', name: 'Zeera Darkfire' },
  { mineId: '_G4126zBQhWEtFkKCG3Dw3', worldId: '_BzKwAkgpPfbVkBzbDaEth', name: 'Jared Thompson' },
  { mineId: '_HqzMU3zVrgHaHBFKw4nQA', worldId: '_YY8VbpgzYk4dfFAL78rM3', name: 'Mackenzie Sanchez-Rogers' }
];

const attachedLorebooks = [
  '_J8x7fwRrpa9C6Wct6hb7p', // Svartulfr - Lorebook (498 entries)
  '_kPzhnGxaRgCMdmgrwWjbY', // Svartulfr - NPC Primary (101 entries)
  '_V6jT3gPWDCPdxT2bCedeG'  // Svartulfr - Location (190 entries)
];

async function syncAllMineCards() {
  console.log(`Starting synchronization of ${mapping.length} stand-alone cards in /mine...`);

  for (const item of mapping) {
    const wChar = worldChars.find(c => c.id === item.worldId);
    if (!wChar) {
      console.error(`[ERROR] World character not found for ${item.name} (${item.worldId})`);
      continue;
    }

    console.log(`Fetching mine card ${item.name} (${item.mineId})...`);
    const getRes = await fetch(`https://app.wyvern.chat/api/characters/${item.mineId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!getRes.ok) {
      console.error(`[GET ERROR ${getRes.status}] for ${item.name}`);
      continue;
    }
    const mineData = await getRes.json();

    // Prefer richer outfits
    let outfits = mineData.outfits || [];
    if (wChar.outfits && wChar.outfits.length >= outfits.length) {
      outfits = wChar.outfits;
    }

    // Build patch payload
    const patchPayload = {
      name: wChar.name || wChar.display_name,
      display_name: wChar.display_name || wChar.name,
      description: (wChar.long_summary || wChar.description || mineData.description || '').replace(/—/g, ', '),
      personality: (wChar.summary || wChar.personality || mineData.personality || '').replace(/—/g, ', '),
      system_prompt: (wChar.system_prompt || mineData.system_prompt || '').replace(/—/g, ', '),
      first_mes: (wChar.first_mes || mineData.first_mes || '').replace(/—/g, ', '),
      mes_example: (wChar.mes_example || mineData.mes_example || '').replace(/—/g, ', '),
      scenario: (wChar.scenario || mineData.scenario || '').replace(/—/g, ', '),
      tagline: wChar.tagline || mineData.tagline || '',
      tags: wChar.tags || mineData.tags || [],
      outfits: outfits,
      lorebooks: attachedLorebooks,
      story_engine_id: 'engine_HCTPXhL8xr89wUY9r9dYU', // Link Svartulfr OS Engine
      post_history_instructions: (wChar.post_history_instructions || mineData.post_history_instructions || 'Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.').replace(/—/g, ', ')
    };

    console.log(`Updating ${item.name}...`);
    const putRes = await fetch(`https://app.wyvern.chat/api/characters/${item.mineId}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(patchPayload)
    });

    if (!putRes.ok) {
      console.error(`[PUT ERROR ${putRes.status}] for ${item.name}:`, await putRes.text());
    } else {
      console.log(`-> Successfully aligned ${item.name}!`);
    }

    await new Promise(r => setTimeout(r, 100));
  }

  console.log('\nAll 8 stand-alone characters in /mine synchronized successfully!');
}

syncAllMineCards().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
