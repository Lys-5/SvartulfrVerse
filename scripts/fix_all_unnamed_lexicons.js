const fs = require('fs');

async function fixAllUnnamedLexicons() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  
  // 1. Mappa completa ID -> Title
  const uploadFiles = [
    'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/uploaded_new_lexicons.json',
    'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/uploaded_block1_lexicons.json',
    'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/uploaded_block2_lexicons.json'
  ];
  const idToTitle = {};
  for (const uf of uploadFiles) {
    if (fs.existsSync(uf)) {
      const arr = JSON.parse(fs.readFileSync(uf, 'utf8'));
      arr.forEach(item => {
        if (item.id && item.title) idToTitle[item.id] = item.title;
      });
    }
  }

  // 2. Fetch di tutte le voci live
  console.log('Recupero elenco voci Lexicon live...');
  const res = await fetch('https://app.wyvern.chat/api/worlds/lexicon/world/' + worldId, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const list = await res.json();
  console.log('Voci totali nel World:', list.length);

  const unnamed = list.filter(e => !e.name || e.name.trim() === '' || /^untitled/i.test(e.name.trim()));
  console.log('Voci unnamed da correggere:', unnamed.length);

  let successCount = 0;
  let failCount = 0;

  for (let i = 0; i < unnamed.length; i++) {
    const entry = unnamed[i];
    const correctTitle = idToTitle[entry.id];

    if (!correctTitle) {
      console.error(`[ERRORE] Nessun titolo trovato per ID ${entry.id}!`);
      failCount++;
      continue;
    }

    // Disciplina tipografica: niente em-dash
    const cleanTitle = correctTitle.replace(/—/g, ', ').replace(/–/g, '-').trim();

    try {
      const putRes = await fetch('https://app.wyvern.chat/api/worlds/lexicon/' + entry.id, {
        method: 'PUT',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: cleanTitle })
      });

      if (putRes.ok) {
        successCount++;
        process.stdout.write(`\r[${i + 1}/${unnamed.length}] Aggiornato: "${cleanTitle.slice(0, 45)}" (ID: ${entry.id})`);
      } else {
        failCount++;
        console.error(`\n[ERRORE PUT ${putRes.status}] ${entry.id}: ${await putRes.text()}`);
      }
    } catch (e) {
      failCount++;
      console.error(`\n[ECCEZIONE] ${entry.id}: ${e.message}`);
    }

    // Throttle leggero per rispettare i limiti API
    await new Promise(r => setTimeout(r, 60));
  }

  console.log(`\n\nOperazione completata! Successi: ${successCount}, Errori: ${failCount}`);

  // 3. Verifica finale
  console.log('\nEsecuzione verifica post-aggiornamento su tutte le voci...');
  const verifyRes = await fetch('https://app.wyvern.chat/api/worlds/lexicon/world/' + worldId, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const verifyList = await verifyRes.json();
  const remainingUnnamed = verifyList.filter(e => !e.name || e.name.trim() === '' || /^untitled/i.test(e.name.trim()));
  console.log('Voci unnamed rimanenti nel World:', remainingUnnamed.length);
}

fixAllUnnamedLexicons().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});
