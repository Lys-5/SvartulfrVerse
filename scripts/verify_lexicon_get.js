const fs = require('fs');
const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();

const ids = [
  '_Py1N2Lh64D4c8gkkMatpA', // Calendar
  '_CFTFWPR8UJDAkc9fA6Q2Q', // Luisa
  '_gwCGDnDYbf9Wgak1BDrax', // Ariadne
  '_NXA2RPpp6RHTVtxRa9pD7', // Dorms
  '_cHWapLYF6kyLTaaw8a4pF', // Nutrition
  '_DG4frH4W3yqNMzJXYVVPU'  // DMHA
];

async function verify() {
  for (const id of ids) {
    const res = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const d = await res.json();
    console.log(`ID ${id}: name="${d.name}", type="${d.type}", content_len=${(d.content||'').length}`);
  }
}

verify().catch(console.error);
