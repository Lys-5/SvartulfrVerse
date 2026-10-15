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
  return data.id_token;
}

async function run() {
  const token = await refreshToken();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };
  const goodId = 'chat_log_QXMmztcRzwG9mcyGtEfeG';
  const bad = JSON.parse(fs.readFileSync('scratch/bad_chat_log.json', 'utf8'));

  console.log('Testing setting world_party on good chat...');
  const putRes = await fetch(`https://app.wyvern.chat/api/new/chat-logs/${goodId}`, {
    method: 'PUT',
    headers,
    body: JSON.stringify({
      world_party: bad.world_party
    })
  });
  console.log('PUT world_party status:', putRes.status);

  const resParty = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      chat_log_id: goodId,
      content: 'Testing embedded world_party effect',
      data: { speak_as: true },
      attachments: [],
      user_id: '2r4fVpvImte5dbljedLkZJxre2d2',
      idempotency_key: 'test_wp_' + Date.now(),
      object_data: []
    })
  });
  console.log('Status with embedded world_party:', resParty.status);
  if (!resParty.ok) console.log('Error:', await resParty.text());
}
run();
