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
  const partyId = '_c8Hpj4Mq2pGYkNHzP3RRX';
  
  // 1. Snapshot live party
  const partyRes = await fetch('https://app.wyvern.chat/api/worlds/parties/' + partyId, {
    headers: { 'Authorization': 'Bearer ' + jwt }
  });
  const liveParty = await partyRes.json();
  fs.writeFileSync('scratch/live_party_c8_backup.json', JSON.stringify(liveParty, null, 2));
  console.log('Backed up live party. world_lexicon_entries count:', liveParty.world_lexicon_entries?.length);

  try {
    // 2. Clear world_lexicon_entries
    console.log('Clearing world_lexicon_entries on _c8Hpj4Mq2pGYkNHzP3RRX...');
    const putRes = await fetch('https://app.wyvern.chat/api/worlds/parties/' + partyId, {
      method: 'PUT',
      headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
      body: JSON.stringify({ world_lexicon_entries: [] })
    });
    console.log('PUT status:', putRes.status);
    const updated = await putRes.json();
    console.log('Party world_lexicon_entries now:', updated.world_lexicon_entries?.length);

    // 3. Create test chat log
    const clRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        world_id: '_CgYT8fHXpDC4crjmegQF7',
        world_party_id: partyId
      })
    });
    const cl = await clRes.json();
    console.log('Chat log ID:', cl.id);

    // 4. Send message
    const msgRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_log_id: cl.id,
        content: 'ping after clearing world_lexicon_entries',
        role: 'user'
      })
    });
    console.log('Msg status without world_lexicon_entries:', msgRes.status);
    if (!msgRes.ok) {
      console.log('Error:', await msgRes.text());
    }

    // 5. Delete test chat log
    await fetch('https://app.wyvern.chat/api/new/chat-logs/' + cl.id, {
      method: 'DELETE',
      headers: { 'Authorization': 'Bearer ' + jwt }
    });
    console.log('Deleted test chat log');
  } finally {
    // 6. Restore world_lexicon_entries
    console.log('Restoring world_lexicon_entries on live party...');
    await fetch('https://app.wyvern.chat/api/worlds/parties/' + partyId, {
      method: 'PUT',
      headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
      body: JSON.stringify({ world_lexicon_entries: liveParty.world_lexicon_entries })
    });
    console.log('Restored.');
  }
})();
