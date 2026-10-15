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

  console.log('1. Creating a new chat log...');
  const createRes = await fetch('https://app.wyvern.chat/api/new/chat-logs', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      world_id: '_CgYT8fHXpDC4crjmegQF7',
      name: 'Temp Diagnostic Chat'
    })
  });
  console.log('Create chat log status:', createRes.status);
  const newLog = await createRes.json();
  console.log('New chat log:', newLog.id || newLog);

  if (newLog.id) {
    console.log('2. Testing POST message to the NEW chat log...');
    const msgRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
      method: 'POST',
      headers,
      body: JSON.stringify({
        chat_log_id: newLog.id,
        content: 'Hello test world',
        world_id: '_CgYT8fHXpDC4crjmegQF7',
        data: { speak_as: true },
        attachments: [],
        idempotency_key: 'diag_' + Date.now(),
        object_data: []
      })
    });
    console.log('Message POST status on NEW chat log:', msgRes.status);
    console.log('Response:', await msgRes.text());
  }
}
run();
