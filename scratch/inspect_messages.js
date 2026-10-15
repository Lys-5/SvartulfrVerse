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
  const headers = { 'Authorization': 'Bearer ' + token };
  const chatId = 'chat_log_rnHfHQgbBEdXegHGkYn6f';

  const res = await fetch(`https://app.wyvern.chat/api/new/chat-logs/${chatId}/messages?page=1&limit=20`, { headers });
  console.log('Messages status:', res.status);
  const data = await res.json();
  const messages = data.messages || [];
  console.log('Fetched messages count:', messages.length);

  function findPriority(obj, path = '') {
    if (!obj || typeof obj !== 'object') return;
    for (const [k, v] of Object.entries(obj)) {
      const cur = path ? path + '.' + k : k;
      if (k.toLowerCase().includes('priority')) {
        console.log(`FOUND PRIORITY in message at ${cur}: typeof=${typeof v}, val=${JSON.stringify(v)}`);
      }
      if (typeof v === 'object') {
        findPriority(v, cur);
      }
    }
  }

  findPriority(messages, 'messages');
  console.log('Scan of last 20 messages complete.');

  // Print last 2 messages
  if (messages.length > 0) {
    console.log('\nLast message:', JSON.stringify(messages[0], null, 2));
  }
}
run();
