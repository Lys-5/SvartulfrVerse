const fs = require('fs');
const path = require('path');

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

async function removeAllImportedBookmarkedLorebooks() {
  let token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  // 1. Fetch current bookmarked lorebooks
  console.log('Recupero elenco attuale dei lorebook bookmarked...');
  let res = await fetch('https://app.wyvern.chat/api/inventory/collection/lorebooks?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });

  if (res.status === 401 || res.status === 404) {
    console.log('Token scaduto, eseguo refresh...');
    token = await refreshToken();
    res = await fetch('https://app.wyvern.chat/api/inventory/collection/lorebooks?limit=100', {
      headers: { 'Authorization': 'Bearer ' + token }
    });
  }

  const data = await res.json();
  const items = data.items || [];
  console.log(`Trovati ${items.length} lorebook bookmarked da rimuovere.\n`);

  let removedCount = 0;
  let failCount = 0;

  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    console.log(`[${i + 1}/${items.length}] Rimozione: ${item.name} (${item.id})...`);

    try {
      const delRes = await fetch(`https://app.wyvern.chat/api/inventory/lorebooks/${item.id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
      });

      if (delRes.ok) {
        console.log(`   -> OK: Rimosso con successo`);
        removedCount++;
      } else {
        console.error(`   -> ERRORE HTTP ${delRes.status}: ${await delRes.text()}`);
        failCount++;
      }
    } catch (err) {
      console.error(`   -> ECCEZIONE: ${err.message}`);
      failCount++;
    }
    // Small delay between calls
    await new Promise(r => setTimeout(r, 200));
  }

  console.log(`\nCompletato! Rimossi: ${removedCount}, Errori: ${failCount}`);

  // 2. Verifica finale
  console.log('\nVerifica finale su /api/inventory/collection/lorebooks...');
  const verifyRes = await fetch('https://app.wyvern.chat/api/inventory/collection/lorebooks?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const verifyData = await verifyRes.json();
  const remaining = verifyData.items || [];
  console.log(`Lorebook bookmarked residui: ${remaining.length}`);
  remaining.forEach(r => console.log(` - ${r.name} (${r.id})`));

  // 3. Aggiornamento dell'export locale
  const uid = '2r4fVpvImte5dbljedLkZJxre2d2';
  const createdRes = await fetch(`https://app.wyvern.chat/api/lorebooks/user/${uid}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const createdData = await createdRes.json();
  const createdList = createdData.lorebooks || [];

  const exportPath = path.join(__dirname, '..', 'exports', 'Mine_Lorebooks_Export.json');
  fs.writeFileSync(exportPath, JSON.stringify({
    created: createdList,
    bookmarked: remaining
  }, null, 2), 'utf8');

  console.log(`\nAggiornato ${exportPath}: ${createdList.length} Created, ${remaining.length} Bookmarked.`);
}

removeAllImportedBookmarkedLorebooks();
