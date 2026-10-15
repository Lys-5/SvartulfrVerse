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
  
  const lbIds = [
    '_kPzhnGxaRgCMdmgrwWjbY',
    '_b6ezzLBynKkdLCKqN8M1U',
    '_J8x7fwRrpa9C6Wct6hb7p',
    '_V6jT3gPWDCPdxT2bCedeG',
    '_xZkWyqB9z1C3QMQp71kXh',
    '_xJUNQC3BBTAbJfRGfWnF1',
    '_LBkRWNpPxpdn6dxYaDU2b'
  ];

  for (const id of lbIds) {
    try {
      const res = await fetch('https://app.wyvern.chat/api/lorebooks/' + id, { headers });
      if (!res.ok) {
        console.log('LB', id, 'status:', res.status);
        continue;
      }
      const data = await res.json();
      console.log(`LB: "${data.name}" (${id}) entries count: ${(data.lexicon || []).length}`);
      let badCount = 0;
      (data.lexicon || []).forEach((e, idx) => {
        if (e.priority !== undefined && typeof e.priority !== 'number') {
          console.log(`  --> BAD PRIORITY in "${data.name}" [${idx}] ${e.comment || e.keys}: typeof=${typeof e.priority}, val=${JSON.stringify(e.priority)}`);
          badCount++;
        }
      });
      if (badCount === 0) {
        console.log(`  [OK] No bad priorities in "${data.name}"`);
      }
    } catch (err) {
      console.log('Error fetching', id, err.message);
    }
  }
}
run();
