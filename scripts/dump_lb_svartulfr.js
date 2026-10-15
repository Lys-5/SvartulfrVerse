const fs = require('fs');
const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();

async function checkLb348() {
  const res = await fetch('https://app.wyvern.chat/api/lorebooks/_J8x7fwRrpa9C6Wct6hb7p', {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const data = await res.json();
  console.log(`Lorebook _J8x7fwRrpa9C6Wct6hb7p: name="${data.name}", count=${(data.lexicon||[]).length}`);
  fs.writeFileSync('scratch/lb_svartulfr_dump.json', JSON.stringify(data, null, 2));
}
checkLb348().catch(console.error);
