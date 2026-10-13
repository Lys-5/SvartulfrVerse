const fs = require('fs');

async function inspectLorebooks() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  // Aegis City Hunters
  const resA = await fetch('https://app.wyvern.chat/api/lorebooks/_1fPzRX9nz4LgtkcQWVha8', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const dA = await resA.json();
  const entriesA = Array.isArray(dA.entries) ? dA.entries : Object.values(dA.entries || {});
  console.log('=== Aegis City Hunters (' + entriesA.length + ' entries) ===');
  entriesA.forEach((e, idx) => {
    const keys = Array.isArray(e.keys) ? e.keys.join(', ') : '';
    const firstLine = (e.content || '').split('\n')[0].slice(0, 70);
    console.log(`${idx + 1}. [Keys: ${keys.slice(0, 35)}] ${firstLine}`);
  });

  // LA: New Moon Compendium
  const resL = await fetch('https://app.wyvern.chat/api/lorebooks/_U9TVTNMFk3R1VdAUV9yhP', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const dL = await resL.json();
  const entriesL = Array.isArray(dL.entries) ? dL.entries : Object.values(dL.entries || {});
  console.log('\n=== LA: New Moon Compendiu (' + entriesL.length + ' entries) ===');
  entriesL.slice(0, 50).forEach((e, idx) => {
    const keys = Array.isArray(e.keys) ? e.keys.join(', ') : '';
    const firstLine = (e.content || '').split('\n')[0].slice(0, 70);
    console.log(`${idx + 1}. [Keys: ${keys.slice(0, 35)}] ${firstLine}`);
  });
}

inspectLorebooks();
