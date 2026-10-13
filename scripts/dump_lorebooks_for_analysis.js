const fs = require('fs');

async function dumpEntryTitles() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const resL = await fetch('https://app.wyvern.chat/api/lorebooks/_U9TVTNMFk3R1VdAUV9yhP', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const dL = await resL.json();
  const entriesL = Array.isArray(dL.entries) ? dL.entries : Object.values(dL.entries || {});
  
  const resA = await fetch('https://app.wyvern.chat/api/lorebooks/_1fPzRX9nz4LgtkcQWVha8', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const dA = await resA.json();
  const entriesA = Array.isArray(dA.entries) ? dA.entries : Object.values(dA.entries || {});

  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/la_entries.json', JSON.stringify(entriesL, null, 2), 'utf8');
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/aegis_entries.json', JSON.stringify(entriesA, null, 2), 'utf8');

  console.log('Saved la_entries.json (' + entriesL.length + ') and aegis_entries.json (' + entriesA.length + ')');
}

dumpEntryTitles();
