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
  const chatId = 'chat_log_rnHfHQgbBEdXegHGkYn6f';

  console.log('1. Disabling use_chat_summary and memory_scan on chat log...');
  const putRes = await fetch(`https://app.wyvern.chat/api/new/chat-logs/${chatId}`, {
    method: 'PUT',
    headers,
    body: JSON.stringify({
      use_chat_summary: false,
      memory: {
        memory_scan: {
          auto_enabled: false
        }
      }
    })
  });
  console.log('PUT status:', putRes.status);
  const updatedLog = await putRes.json();
  console.log('Updated log use_chat_summary:', updatedLog.use_chat_summary);

  console.log('\n2. Testing POST message again...');
  const msgRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
    method: 'POST',
    headers,
    body: JSON.stringify({
      chat_log_id: chatId,
      content: '--- Test ping with memory scan disabled ---',
      data: { speak_as: true },
      attachments: [],
      user_id: '2r4fVpvImte5dbljedLkZJxre2d2',
      idempotency_key: 'test_toggle_' + Date.now(),
      object_data: []
    })
  });
  console.log('Message POST status:', msgRes.status);
  console.log('Response:', await msgRes.text());
}
run();
