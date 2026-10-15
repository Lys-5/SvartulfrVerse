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
  
  const body = {
    chat_log_id: 'chat_log_rnHfHQgbBEdXegHGkYn6f',
    content: '--- Test ping ---',
    world_id: '_CgYT8fHXpDC4crjmegQF7',
    world_party_id: '_c8Hpj4Mq2pGYkNHzP3RRX',
    data: { speak_as: true },
    attachments: [],
    user_id: '2r4fVpvImte5dbljedLkZJxre2d2',
    idempotency_key: 'test_key_' + Date.now(),
    object_data: []
  };

  console.log('--- Test 2: WITHOUT header priority ---');
  const res2 = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  });
  console.log('Status 2:', res2.status);
  console.log('Response 2:', await res2.text());
}
run();
