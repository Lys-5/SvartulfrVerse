const fs = require('fs');

async function scan() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0' };
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  
  const res = await fetch('https://app.wyvern.chat/api/worlds/characters/world/' + worldId, { headers });
  const chars = await res.json();
  console.log('Total characters to audit:', chars.length);

  const report = [];

  for (let i = 0; i < chars.length; i++) {
    const c = chars[i];
    try {
      const detailRes = await fetch('https://app.wyvern.chat/api/worlds/characters/' + c.id, { headers });
      const d = await detailRes.json();
      const outfits = d.outfits || [];
      
      const emptyOutfits = outfits.filter(o => !o.description || !o.description.trim());
      const validOutfits = outfits.filter(o => o.description && o.description.trim());

      if (emptyOutfits.length > 0 || outfits.length === 0) {
        report.push({
          id: c.id,
          name: c.display_name,
          totalOutfits: outfits.length,
          validCount: validOutfits.length,
          emptyCount: emptyOutfits.length,
          emptyNames: emptyOutfits.map(o => o.name)
        });
      }
    } catch (e) {
      console.error('Error on ' + c.display_name + ': ' + e.message);
    }
  }

  console.log('\n=== AUDIT REPORT: CHARACTERS WITH EMPTY OUTFIT DESCRIPTIONS ===');
  console.log('Total characters with empty/missing outfits: ' + report.length + ' / ' + chars.length);
  report.forEach(r => {
    console.log(`[${r.id}] ${r.name.padEnd(28)} | Total: ${r.totalOutfits} | Empty: ${r.emptyCount} [${r.emptyNames.join(', ')}]`);
  });

  fs.writeFileSync('scratch/outfits_audit_report.json', JSON.stringify(report, null, 2), 'utf8');
}

scan().catch(console.error);
