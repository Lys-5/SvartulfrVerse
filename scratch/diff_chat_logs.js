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

  const goodRes = await fetch('https://app.wyvern.chat/api/new/chat-logs/chat_log_QXMmztcRzwG9mcyGtEfeG', { headers });
  const good = await goodRes.json();
  fs.writeFileSync('scratch/good_chat_log.json', JSON.stringify(good, null, 2), 'utf8');

  const bad = JSON.parse(fs.readFileSync('scratch/bad_chat_log.json', 'utf8'));

  console.log('Comparing fields between Bad and Good:');
  const allKeys = [...new Set([...Object.keys(bad), ...Object.keys(good)])];
  for (const k of allKeys) {
    const bVal = bad[k];
    const gVal = good[k];
    const bType = Array.isArray(bVal) ? `Array(${bVal.length})` : typeof bVal;
    const gType = Array.isArray(gVal) ? `Array(${gVal.length})` : typeof gVal;
    if (JSON.stringify(bVal) !== JSON.stringify(gVal)) {
      console.log(`\nField "${k}":`);
      console.log(`  BAD : ${bType} -> ${bVal !== undefined ? JSON.stringify(bVal).slice(0, 120) : 'undefined'}`);
      console.log(`  GOOD: ${gType} -> ${gVal !== undefined ? JSON.stringify(gVal).slice(0, 120) : 'undefined'}`);
    }
  }
}
run();
