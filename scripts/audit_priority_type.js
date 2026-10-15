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
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', data.id_token, 'utf8');
  return data.id_token;
}

async function check() {
  const token = await refreshToken();
  const headers = { 'Authorization': 'Bearer ' + token };
  
  // 1. Check all lorebooks
  console.log('--- Checking Lorebooks ---');
  // First list all user lorebooks if possible or check known IDs
  let lbIds = ['_LBkRWNpPxpdn6dxYaDU2b', '_xJUNQC3BBTAbJfRGfWnF1'];
  try {
    const listRes = await fetch('https://app.wyvern.chat/api/lorebooks', { headers });
    if (listRes.ok) {
      const allLbs = await listRes.json();
      console.log('Found', allLbs.length, 'lorebooks in user account.');
      lbIds = allLbs.map(l => l.id || l._id);
    }
  } catch (err) {
    console.log('Could not list lorebooks:', err.message);
  }

  for (const lbId of lbIds) {
    const res = await fetch('https://app.wyvern.chat/api/lorebooks/' + lbId, { headers });
    if (res.ok) {
      const data = await res.json();
      let badCount = 0;
      (data.lexicon || []).forEach((e, idx) => {
        if (e.priority !== undefined && typeof e.priority !== 'number') {
          console.log(`  Bad priority in LB '${data.name}' [${idx}] '${e.comment || e.keys}': typeof=${typeof e.priority}, val=${JSON.stringify(e.priority)}`);
          badCount++;
        }
      });
      if (badCount > 0) {
        console.log(`--> TOTAL bad priority entries in LB '${data.name}' (${lbId}): ${badCount}`);
      } else {
        console.log(`LB '${data.name}' (${lbId}): OK (${(data.lexicon || []).length} entries)`);
      }
    } else {
      console.log('Failed to fetch LB', lbId, res.status);
    }
  }

  // 2. Check World
  console.log('\n--- Checking World ---');
  const wRes = await fetch('https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7', { headers });
  if (wRes.ok) {
    const wData = await wRes.json();
    console.log('World fetched.');
    let badLex = 0;
    (wData.lexicon || []).forEach((e, idx) => {
      if (e.priority !== undefined && typeof e.priority !== 'number') {
        console.log(`  Bad world lexicon priority [${idx}] '${e.name || e.keys}': typeof=${typeof e.priority}, val=${JSON.stringify(e.priority)}`);
        badLex++;
      }
    });
    console.log(`World Lexicon bad priority: ${badLex} / ${(wData.lexicon || []).length}`);

    let badScen = 0;
    (wData.scenarios || []).forEach((s, idx) => {
      if (s.priority !== undefined && typeof s.priority !== 'number') {
        console.log(`  Bad scenario priority [${idx}] '${s.title}': typeof=${typeof s.priority}, val=${JSON.stringify(s.priority)}`);
        badScen++;
      }
    });
    console.log(`World Scenarios bad priority: ${badScen} / ${(wData.scenarios || []).length}`);

    // Check characters inside world just in case
    let badChar = 0;
    (wData.characters || []).forEach((c, idx) => {
      if (c.priority !== undefined && typeof c.priority !== 'number') {
        console.log(`  Bad character priority [${idx}] '${c.name}': typeof=${typeof c.priority}, val=${JSON.stringify(c.priority)}`);
        badChar++;
      }
    });
    console.log(`World Characters bad priority: ${badChar} / ${(wData.characters || []).length}`);
  }
}

check();
