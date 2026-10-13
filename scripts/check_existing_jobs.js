const fs = require('fs');
const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

async function run() {
  const res = await fetch('https://app.wyvern.chat/api/worlds/lexicon/world/_CgYT8fHXpDC4crjmegQF7', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const data = await res.json();
  const jobs = data.filter(e => e.type === 'job' || e.job_config != null || (e.keys && e.keys.some(k => k.toLowerCase().includes('job'))));
  console.log('Total jobs found:', jobs.length);
  jobs.forEach(j => {
    console.log(`[${j.id}] ${j.name} | type: ${j.type}`);
  });
}

run().catch(console.error);
