const fs = require('fs');

async function getJwt() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rt = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt', 'utf8').trim();
  const res = await fetch('https://securetoken.googleapis.com/v1/token?key=' + ak, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grant_type: 'refresh_token', refresh_token: rt })
  });
  const data = await res.json();
  return data.id_token;
}

(async () => {
  const jwt = await getJwt();
  const headers = { 'Authorization': 'Bearer ' + jwt };

  const party = JSON.parse(fs.readFileSync('scratch/live_bad_party.json', 'utf8'));

  console.log('--- 1. Checking Party itself ---');
  for (const [k, v] of Object.entries(party)) {
    if (k.toLowerCase().includes('priority')) {
      console.log(`Party property ${k}: type=${typeof v}, val=${JSON.stringify(v)}`);
    }
  }

  console.log('--- 2. Checking current_characters ---');
  for (const c of party.current_characters || []) {
    const fullChar = await (await fetch(`https://app.wyvern.chat/api/worlds/characters/${c.id}`, { headers })).json();
    for (const [k, v] of Object.entries(fullChar)) {
      if (k.toLowerCase().includes('priority')) {
        console.log(`Character ${fullChar.name || fullChar.id} property ${k}: type=${typeof v}, val=${JSON.stringify(v)}`);
      }
    }
  }

  console.log('--- 3. Checking linked_characters ---');
  for (const lc of party.linked_characters || []) {
    for (const [k, v] of Object.entries(lc)) {
      if (k.toLowerCase().includes('priority')) {
        console.log(`LinkedChar ${lc.name || lc.id} property ${k}: type=${typeof v}, val=${JSON.stringify(v)}`);
      }
    }
  }

  console.log('--- 4. Checking companion_supply_characters ---');
  for (const id of party.companion_supply_character_ids || []) {
    const fullChar = await (await fetch(`https://app.wyvern.chat/api/worlds/characters/${id}`, { headers })).json();
    for (const [k, v] of Object.entries(fullChar)) {
      if (k.toLowerCase().includes('priority')) {
        console.log(`SupplyChar ${fullChar.name || fullChar.id} property ${k}: type=${typeof v}, val=${JSON.stringify(v)}`);
      }
    }
  }

  console.log('--- 5. Checking current_location ---');
  if (party.current_location?.id) {
    const loc = await (await fetch(`https://app.wyvern.chat/api/worlds/locations/${party.current_location.id}`, { headers })).json();
    for (const [k, v] of Object.entries(loc)) {
      if (k.toLowerCase().includes('priority')) {
        console.log(`Location ${loc.name} property ${k}: type=${typeof v}, val=${JSON.stringify(v)}`);
      }
    }
  }

  console.log('--- 6. Checking current_environment ---');
  if (party.current_environment?.id) {
    const env = await (await fetch(`https://app.wyvern.chat/api/worlds/environments/${party.current_environment.id}`, { headers })).json();
    for (const [k, v] of Object.entries(env)) {
      if (k.toLowerCase().includes('priority')) {
        console.log(`Environment ${env.name} property ${k}: type=${typeof v}, val=${JSON.stringify(v)}`);
      }
    }
  }

  console.log('--- 7. Checking current_persona ---');
  if (party.current_persona?.id) {
    const persona = await (await fetch(`https://app.wyvern.chat/api/personas/${party.current_persona.id}`, { headers })).json();
    for (const [k, v] of Object.entries(persona)) {
      if (k.toLowerCase().includes('priority')) {
        console.log(`Persona property ${k}: type=${typeof v}, val=${JSON.stringify(v)}`);
      }
    }
  }

  console.log('--- 8. Checking 167 world_lexicon_entries ---');
  for (let i = 0; i < (party.world_lexicon_entries || []).length; i++) {
    const e = party.world_lexicon_entries[i];
    if (e.priority !== undefined && typeof e.priority !== 'number') {
      console.log(`Lexicon entry ${i} ${e.name} property priority: type=${typeof e.priority}, val=${JSON.stringify(e.priority)}`);
    }
  }

  console.log('All checks completed.');
})();
