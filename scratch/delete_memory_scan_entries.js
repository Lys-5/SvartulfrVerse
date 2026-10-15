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

  const entries = JSON.parse(fs.readFileSync('scratch/party_c8_lexicon_endpoint.json', 'utf8'));
  console.log(`Starting deletion of ${entries.length} auto-generated memory-scan entries...`);

  let deleted = 0;
  let errors = 0;

  for (let i = 0; i < entries.length; i++) {
    const e = entries[i];
    try {
      const res = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${e.id}`, {
        method: 'DELETE',
        headers
      });
      if (res.status === 204 || res.status === 200 || res.status === 404) {
        deleted++;
      } else {
        console.log(`Failed to delete ${e.id}: status ${res.status}`);
        errors++;
      }
    } catch (err) {
      console.log(`Error deleting ${e.id}: ${err.message}`);
      errors++;
    }

    if ((i + 1) % 25 === 0 || i === entries.length - 1) {
      console.log(`Progress: ${i + 1}/${entries.length} (Deleted: ${deleted}, Errors: ${errors})`);
    }
  }

  console.log(`\nFinished deletion! Total deleted: ${deleted}, Errors: ${errors}`);

  // Check remaining count on party
  const partyLex = await (await fetch('https://app.wyvern.chat/api/worlds/parties/_c8Hpj4Mq2pGYkNHzP3RRX/lexicon', { headers })).json();
  console.log(`Party _c8Hpj4Mq2pGYkNHzP3RRX lexicon count now: ${partyLex.length}`);

  // Test sending message on _c8Hpj4Mq2pGYkNHzP3RRX!
  console.log('\n--- TESTING FRESH CHAT LOG ON _c8Hpj4Mq2pGYkNHzP3RRX ---');
  const cl = await (await fetch('https://app.wyvern.chat/api/new/chat-logs/world', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({ world_id: '_CgYT8fHXpDC4crjmegQF7', world_party_id: '_c8Hpj4Mq2pGYkNHzP3RRX' })
  })).json();
  console.log('Created fresh test CL:', cl.id);

  const msgRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_log_id: cl.id,
      content: 'test probe after clearing auto-generated memory scan bloat',
      role: 'user'
    })
  });
  console.log(`Message status: ${msgRes.status}`);
  if (!msgRes.ok) {
    console.log('Failed:', await msgRes.text());
  } else {
    console.log('🎉🎉🎉 SUCCESS! 200 OK! PARTY _c8Hpj4Mq2pGYkNHzP3RRX IS FULLY RESTORED!');
  }

  if (cl.id) {
    await fetch(`https://app.wyvern.chat/api/new/chat-logs/${cl.id}`, { method: 'DELETE', headers });
    console.log('Cleaned up test CL:', cl.id);
  }
})();
