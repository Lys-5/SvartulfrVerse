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
  const chatId = 'chat_log_rnHfHQgbBEdXegHGkYn6f';

  const res = await fetch('https://app.wyvern.chat/api/new/chat-logs/' + chatId, { headers });
  const chatLog = await res.json();
  const msgs = chatLog.messages || [];
  console.log('Total messages in log:', msgs.length);
  const lastMsg = msgs[msgs.length - 1];
  console.log('Last message:', lastMsg?.id, lastMsg?.content);

  if (lastMsg && lastMsg.content === 'test ping after party cleanup') {
    console.log('Deleting test probe message:', lastMsg.id);
    const delRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/' + chatId + '/messages/' + lastMsg.id, {
      method: 'DELETE',
      headers
    });
    console.log('DELETE message status:', delRes.status);
  }
})();
