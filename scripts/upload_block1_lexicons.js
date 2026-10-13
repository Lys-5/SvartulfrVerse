const fs = require('fs');

async function uploadBlock1() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const url = 'https://app.wyvern.chat/api/worlds/lexicon';

  const entries = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/block1_new_lexicons.json', 'utf8'));

  console.log(`Caricamento di ${entries.length} voci di Lexicon per il Blocco 1...`);

  const created = [];
  for (let i = 0; i < entries.length; i++) {
    const e = entries[i];
    const payload = {
      world_id: worldId,
      title: e.title,
      type: e.type || 'lore/concept',
      keys: e.keys || [],
      key_logic: 'AND_ANY',
      content: e.content || '',
      is_global: true,
      enabled: true,
      position: 'before_char',
      priority: 0
    };

    const res = await fetch(url, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      const d = await res.json();
      created.push({ id: d.id, title: e.title });
      console.log(`[${i + 1}/${entries.length}] OK: ${e.title} -> ${d.id}`);
    } else {
      const err = await res.text();
      console.error(`[${i + 1}/${entries.length}] ERRORE ${res.status}: ${e.title} -> ${err}`);
    }
    await new Promise(r => setTimeout(r, 120));
  }

  console.log(`\nCompletato! ${created.length} voci create con successo.`);
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/uploaded_block1_lexicons.json', JSON.stringify(created, null, 2), 'utf8');
}

uploadBlock1();
