const fs = require('fs');

async function run() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token };

  let r = await fetch('https://app.wyvern.chat/api/worlds/characters/world/_CgYT8fHXpDC4crjmegQF7', { headers });
  let list = await r.json();
  let jasper = list.find(c => c.id === '_x3VY2kcbaDbKyCqywGeET');
  let malachia = list.find(c => c.id === '_rAcN9GXD1Le4WxY28e49W');
  let noah = list.find(c => c.id === '_r42cVzMjcGTAx7bR1DQVt');

  fs.writeFileSync('scratch/jasper.json', JSON.stringify(jasper, null, 2));
  fs.writeFileSync('scratch/malachia.json', JSON.stringify(malachia, null, 2));
  fs.writeFileSync('scratch/noah.json', JSON.stringify(noah, null, 2));

  // Let's check IDs embedded inside jasper and malachia
  function findSuspiciousIds(obj, path = '') {
    if (!obj || typeof obj !== 'object') return;
    for (let k of Object.keys(obj)) {
      let val = obj[k];
      let currentPath = path ? `${path}.${k}` : k;
      if (typeof val === 'string' && val.length > 5) {
        // check if val looks like an id or has weird chars
        if (k.endsWith('_id') || k === 'id' || k === '_id') {
          console.log(`[${currentPath}] = ${val}`);
        }
      } else if (typeof val === 'object') {
        findSuspiciousIds(val, currentPath);
      }
    }
  }

  console.log('--- JASPER IDs ---');
  findSuspiciousIds(jasper);

  console.log('\n--- MALACHIA IDs ---');
  findSuspiciousIds(malachia);

  console.log('\n--- NOAH IDs ---');
  findSuspiciousIds(noah);
}

run().catch(console.error);
