const fs = require('fs');

async function inspectCreatedLorebooks() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const lbs = [
    { id: '_V6jT3gPWDCPdxT2bCedeG', name: 'Svartúlfr - Location' },
    { id: '_J8x7fwRrpa9C6Wct6hb7p', name: 'Svartúlfr - Lorebook' },
    { id: '_kPzhnGxaRgCMdmgrwWjbY', name: 'Svartúlfr - NPC Primary' },
    { id: '_b6ezzLBynKkdLCKqN8M1U', name: 'Svartúlfr - NPC Secondary' }
  ];

  for (const lb of lbs) {
    const res = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
    console.log('=== LOREBOOK:', lb.name, '(', lb.id, ') Status:', res.status, '===');
    if (res.ok) {
      const d = await res.json();
      console.log('  Keys:', Object.keys(d));
      const entries = Array.isArray(d.entries) ? d.entries : (d.entries ? Object.keys(d.entries).length : (d.lexicon && d.lexicon.entries ? d.lexicon.entries.length : 0));
      console.log('  Entries count:', entries);
      console.log('  Description snippet:\n  ', (d.description || '').slice(0, 150));
    }
  }
}

inspectCreatedLorebooks();
