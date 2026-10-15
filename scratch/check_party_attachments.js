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

  console.log('1. Checking Lorebook _NEFGEwddwPqzP4HaNwEUm...');
  const lbRes = await fetch('https://app.wyvern.chat/api/lorebooks/_NEFGEwddwPqzP4HaNwEUm', { headers });
  console.log('LB status:', lbRes.status);
  if (lbRes.ok) {
    const lb = await lbRes.json();
    console.log(`LB Name: "${lb.name}", entries count: ${(lb.lexicon || []).length}`);
    (lb.lexicon || []).forEach((e, idx) => {
      if (e.priority !== undefined && typeof e.priority !== 'number') {
        console.log(`  --> BAD PRIORITY in LB "${lb.name}" [${idx}] "${e.comment || e.keys}": typeof=${typeof e.priority}, val=${JSON.stringify(e.priority)}`);
      }
    });
  }

  console.log('2. Checking Linked Character _LLjHwF37Pkb6WbWty6Nkk...');
  const charRes = await fetch('https://app.wyvern.chat/api/characters/_LLjHwF37Pkb6WbWty6Nkk', { headers });
  console.log('Char status:', charRes.status);
  if (charRes.ok) {
    const c = await charRes.json();
    console.log(`Char Name: "${c.name}"`);
    if (c.priority !== undefined && typeof c.priority !== 'number') {
      console.log(`  --> BAD PRIORITY in character: typeof=${typeof c.priority}, val=${JSON.stringify(c.priority)}`);
    }
    (c.character_book?.entries || []).forEach((e, idx) => {
      if (e.priority !== undefined && typeof e.priority !== 'number') {
        console.log(`  --> BAD PRIORITY in char book [${idx}]: typeof=${typeof e.priority}, val=${JSON.stringify(e.priority)}`);
      }
    });
  }
}
run();
