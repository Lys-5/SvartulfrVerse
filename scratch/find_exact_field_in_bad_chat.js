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
  const backup = JSON.parse(fs.readFileSync('scratch/bad_chat_log.json', 'utf8'));

  async function testMsg(label) {
    const res = await fetch('https://app.wyvern.chat/api/new/chat-logs/message', {
      method: 'POST',
      headers,
      body: JSON.stringify({
        chat_log_id: chatId,
        content: 'ping ' + label,
        data: { speak_as: true },
        attachments: [],
        user_id: '2r4fVpvImte5dbljedLkZJxre2d2',
        idempotency_key: 'test_' + Date.now(),
        object_data: []
      })
    });
    console.log(`[${label}] status: ${res.status}`);
    return res.ok;
  }

  // Candidates to test resetting on chat log
  const candidates = [
    { field: 'scenario_override', val: null },
    { field: 'info_board_override', val: null },
    { field: 'current_location_id', val: null },
    { field: 'world_data', val: null },
    { field: 'object_data', val: [] },
    { field: 'world_party', val: null },
    { field: 'current_summary', val: null }
  ];

  for (const c of candidates) {
    console.log(`Testing clearing ${c.field}...`);
    await fetch(`https://app.wyvern.chat/api/new/chat-logs/${chatId}`, {
      method: 'PUT',
      headers,
      body: JSON.stringify({ [c.field]: c.val })
    });
    const ok = await testMsg('after_clearing_' + c.field);
    if (ok) {
      console.log(`\n🎉 BINGO! The culprit was field: "${c.field}"!`);
      return;
    }
  }

  console.log('None of the top-level chat log fields resolved it.');
}
run();
