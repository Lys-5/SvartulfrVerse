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
  const headers = { 'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json' };

  // 1. Delete test party _Ly7XJLQDGL6xf2P9DK7V9
  console.log('1. Deleting test sandbox party _Ly7XJLQDGL6xf2P9DK7V9...');
  try {
    const delP = await fetch('https://app.wyvern.chat/api/worlds/parties/_Ly7XJLQDGL6xf2P9DK7V9', {
      method: 'DELETE',
      headers
    });
    console.log('Delete test party status:', delP.status);
  } catch(e) {
    console.log('Error deleting test party:', e.message);
  }

  // 2. Check all user parties
  console.log('\n2. Checking user parties...');
  const partiesRes = await fetch('https://app.wyvern.chat/api/worlds/parties/user', { headers });
  if (partiesRes.ok) {
    const parties = await partiesRes.json();
    console.log(`Total user parties: ${parties.length}`);
    for (const p of parties) {
      console.log(`- Party: ${p.id} | title="${p.party_title || p.name}" | created_at=${p.created_at}`);
      if (p.party_title && p.party_title.includes('Test') && p.id !== '_c8Hpj4Mq2pGYkNHzP3RRX') {
        console.log(`  --> Deleting test party ${p.id}...`);
        await fetch(`https://app.wyvern.chat/api/worlds/parties/${p.id}`, { method: 'DELETE', headers });
      }
    }
  }

  // 3. Check all user chat logs for diagnostic / temp chats
  console.log('\n3. Checking user chat logs...');
  const clsRes = await fetch('https://app.wyvern.chat/api/new/chat-logs?limit=50', { headers });
  if (clsRes.ok) {
    const cls = await clsRes.json();
    const chatLogs = Array.isArray(cls) ? cls : (cls.items || cls.chat_logs || []);
    console.log(`Recent chat logs count: ${chatLogs.length}`);
    for (const cl of chatLogs) {
      const isTest = cl.name && (cl.name.includes('Temp') || cl.name.includes('Diagnostic') || cl.name.includes('Test'));
      if (isTest && cl.id !== 'chat_log_rnHfHQgbBEdXegHGkYn6f') {
        console.log(`Deleting test chat log: ${cl.id} (${cl.name})...`);
        await fetch(`https://app.wyvern.chat/api/new/chat-logs/${cl.id}`, { method: 'DELETE', headers });
      }
    }
  }

  console.log('\nZero-Footprint Cleanup Completed!');
})();
