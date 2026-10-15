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

  console.log('Test A: Omit world_party_id and world_id');
  const resA = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      chat_log_id: 'chat_log_rnHfHQgbBEdXegHGkYn6f',
      content: '--- Test ping without party id ---',
      data: { speak_as: true },
      attachments: [],
      user_id: '2r4fVpvImte5dbljedLkZJxre2d2',
      idempotency_key: 'test_a_' + Date.now(),
      object_data: []
    })
  });
  console.log('Status A:', resA.status);
  console.log('Response A:', await resA.text());
}
run();
