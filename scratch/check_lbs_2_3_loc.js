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

  const ids = [
    { id: '_xyqrAA3VRAMJFc4FjYwar', name: 'Svartúlfr - Lorebook II' },
    { id: '_EpUytDfYtHyd9AnWg6jDJ', name: 'Svartúlfr - Lorebook III' },
    { id: '_zeMAW9knfrhAGAXC9k4Wk', name: 'Svartúlfr - Location' }
  ];

  for (const item of ids) {
    const res = await fetch(`https://app.wyvern.chat/api/lorebooks/${item.id}`, { headers });
    console.log(`\nLB: ${item.name} (${item.id}) status: ${res.status}`);
    if (res.ok) {
      const data = await res.json();
      console.log(`  Name: "${data.name}"`);
      console.log(`  scan_depth: ${data.scan_depth}, token_budget: ${data.token_budget}`);
      let badCount = 0;
      (data.lexicon || []).forEach((e, idx) => {
        if (e.priority !== undefined && typeof e.priority !== 'number') {
          console.log(`  --> BAD PRIORITY [${idx}] ${e.comment || e.keys}: typeof=${typeof e.priority}, val=${JSON.stringify(e.priority)}`);
          badCount++;
        }
      });
      if (badCount === 0) console.log(`  All ${(data.lexicon || []).length} entries OK!`);
    }
  }
}
run();
