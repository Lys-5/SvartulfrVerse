const fs = require('fs');

async function uploadNewLexicons() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const url = 'https://app.wyvern.chat/api/worlds/lexicon';

  const newEntries = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/new_succ_dmha_lexicons.json', 'utf8'));

  console.log(`Avvio upload batch di ${newEntries.length} voci di Lexicon nel World ${worldId}...`);

  const createdIds = [];
  const errors = [];

  for (let i = 0; i < newEntries.length; i++) {
    const entry = newEntries[i];
    const payload = {
      world_id: worldId,
      title: entry.title,
      type: entry.type || 'lore/concept',
      keys: entry.keys || [],
      key_logic: 'AND_ANY',
      content: entry.content || '',
      is_global: true,
      enabled: true,
      position: 'before_char',
      priority: 0
    };

    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        const data = await res.json();
        createdIds.push({ id: data.id, title: entry.title, type: entry.type });
        process.stdout.write(`\r[${i + 1}/${newEntries.length}] Creato: ${entry.title.slice(0, 45)} (ID: ${data.id})`);
      } else {
        const errText = await res.text();
        console.error(`\n[ERRORE ${res.status}] ${entry.title}: ${errText.slice(0, 100)}`);
        errors.push({ title: entry.title, status: res.status, error: errText });
      }
    } catch (e) {
      console.error(`\n[ECCEZIONE] ${entry.title}: ${e.message}`);
      errors.push({ title: entry.title, error: e.message });
    }

    // Piccolo throttle di 100ms per rispettare rate limits
    await new Promise(r => setTimeout(r, 100));
  }

  console.log(`\n\nUpload completato! Successi: ${createdIds.length}, Errori: ${errors.length}`);
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/uploaded_new_lexicons.json', JSON.stringify(createdIds, null, 2), 'utf8');
}

uploadNewLexicons();
