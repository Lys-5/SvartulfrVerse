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
  const res = await fetch('https://app.wyvern.chat/api/new/chat-logs/chat_log_rnHfHQgbBEdXegHGkYn6f', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const log = await res.json();
  fs.writeFileSync('scratch/bad_chat_log.json', JSON.stringify(log, null, 2), 'utf8');
  console.log('Saved scratch/bad_chat_log.json, size:', fs.statSync('scratch/bad_chat_log.json').size);
}
run();
