const fs = require('fs');

async function run() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' };
  
  let eps = [
    ['PUT', 'https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF'],
    ['PATCH', 'https://app.wyvern.chat/api/worlds/scenarios/_p1Ffq22CTwVywz1CFQBfF'],
    ['PUT', 'https://app.wyvern.chat/api/scenarios/_p1Ffq22CTwVywz1CFQBfF'],
    ['PATCH', 'https://app.wyvern.chat/api/scenarios/_p1Ffq22CTwVywz1CFQBfF']
  ];
  for (let [method, url] of eps) {
    let r = await fetch(url, { method, headers, body: JSON.stringify({ name: "Alyssa's Story: Cronache del Primo Anno (SUCC & Blackwood)" }) });
    console.log(method, url, r.status, (await r.text()).slice(0, 100));
  }
}

run().catch(console.error);
