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

  console.log('Testing message with world_party_id on the new chat log:');
  const msgRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      chat_log_id: 'chat_log_QXMmztcRzwG9mcyGtEfeG',
      content: 'Testing with party attached',
      world_id: '_CgYT8fHXpDC4crjmegQF7',
      world_party_id: '_c8Hpj4Mq2pGYkNHzP3RRX',
      data: { speak_as: true },
      attachments: [],
      idempotency_key: 'diag_party_' + Date.now(),
      object_data: []
    })
  });
  console.log('Message POST status with world_party_id:', msgRes.status);
  console.log('Response:', await msgRes.text());
}
run();
