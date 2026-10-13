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

async function updateBarrowAndUnbookmark() {
  let token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const barrowWorldId = '_LEeEzdCCyGjQ8kfVkcra8';
  const barrowBookmarkId = '_nbEC7qk3NgU1LDfpQN9BW';

  console.log('1. Recupero dati live di Barrow nel World...');
  let getRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${barrowWorldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });

  if (getRes.status === 401 || getRes.status === 404) {
    console.log('Token scaduto, refresh in corso...');
    token = await refreshToken();
    getRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${barrowWorldId}`, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
  }

  const barrow = await getRes.json();
  console.log(`Trovato: ${barrow.display_name} (${barrow.id})`);

  // Aggiorna long_summary sostituendo {{age}} con età e data di nascita esplicita
  const updatedLongSummary = barrow.long_summary.replace(
    'AGE: {{age}};',
    'AGE: 42 (Born 9 November 1981);'
  );

  const updatedSummary = '[NAME: Barrow; SPECIES: Minotaur; OCCUPATION: Council Master Builder, Veteran Brawler; TRAITS: Stoic, Honest, Protective, Pragmatic, Heavy Muscle, Controlled Temper, Blue-Collar Wisdom, Deep Voice, Demihuman Council Leader]';

  // Tratti pertinenti di Barrow
  const traits = [
    '_8AYDaJ2xJaP7Vhe26M1jA', // Gentle Giant
    '_VrgTBJR3aEyW3FBD1zLkR', // Dungeon Veteran
    '_AMT6xk8rnrT9E9Vx8mhdq', // The Weight He Carries
    '_ycHNkaW9aEjTxppUe6Wtg'  // Knight in Sour Armor
  ];

  console.log('\n2. Aggiornamento scheda Barrow per piena conformità JED+, RPG e Setting...');
  const patchPayload = {
    long_summary: updatedLongSummary,
    summary: updatedSummary,
    character_traits: traits,
    final_instructions: 'Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.'
  };

  const putRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${barrowWorldId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(patchPayload)
  });

  if (putRes.ok) {
    console.log('   -> Barrow aggiornato con successo nel World!');
  } else {
    console.error('   -> Errore PUT Barrow:', putRes.status, await putRes.text());
    return;
  }

  // 3. Verifica aggiornamento
  const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/characters/${barrowWorldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const verified = await verifyRes.json();
  console.log(`   -> Verifica GET: long_summary include 'Born 9 November 1981': ${verified.long_summary.includes('Born 9 November 1981')}`);
  console.log(`   -> Verifica GET: traits count: ${(verified.character_traits || []).length}`);

  // 4. Rimozione del segnalibro della scheda originale esterna di Barrow
  console.log(`\n4. Rimozione segnalibro originale di Barrow (${barrowBookmarkId})...`);
  const delRes = await fetch(`https://app.wyvern.chat/api/inventory/characters/${barrowBookmarkId}`, {
    method: 'DELETE',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({})
  });

  if (delRes.ok) {
    console.log('   -> Segnalibro di Barrow rimosso con successo!');
  } else {
    console.error('   -> Errore DELETE bookmark:', delRes.status, await delRes.text());
  }

  // 5. Verifica inventario segnalibri caratteri
  console.log('\n5. Verifica segnalibri personaggi rimanenti...');
  const bookmarkedRes = await fetch('https://app.wyvern.chat/api/inventory/collection/characters?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const bookmarkedData = await bookmarkedRes.json();
  const remaining = bookmarkedData.items || [];
  console.log(`Segnalibri personaggi rimanenti: ${remaining.length} (da 43 a 42)`);
  const barrowStillThere = remaining.some(c => (c.id || c._id) === barrowBookmarkId);
  console.log(`Barrow ancora presente nei segnalibri: ${barrowStillThere}`);
}

updateBarrowAndUnbookmark();
