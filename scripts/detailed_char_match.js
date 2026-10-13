const fs = require('fs');

async function detailedMatch() {
  const worldData = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
  const worldChars = worldData.world_characters || [];
  const worldLexicon = worldData.lexicon || [];

  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const res = await fetch('https://app.wyvern.chat/api/inventory/collection/characters?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const data = await res.json();
  const bookmarked = data.items || [];

  console.log(`Checking ${bookmarked.length} bookmarked characters against World...\n`);

  for (let i = 0; i < bookmarked.length; i++) {
    const b = bookmarked[i];
    const bTitle = b.name || b.display_name || '';
    const bId = b.id || b._id;

    // Search terms from bTitle: split by |, •, -, :, &
    const rawTokens = bTitle.split(/[|•\-:–,]+/).map(s => s.trim()).filter(Boolean);
    const keywords = [];
    rawTokens.forEach(t => {
      // split words like "Radek, Goran & Kian" or "Liam O’Connor"
      const sub = t.split(/&/).map(s => s.trim()).filter(Boolean);
      keywords.push(...sub);
    });

    const matches = [];

    for (const kw of keywords) {
      if (kw.length < 3) continue;
      const kwLower = kw.toLowerCase();
      // exclude generic words
      if (['ukiyo', 'series', 'best friend', 'alpha', 'rpg', 'once upon a prince', 'academy of magic', 'invading prince'].includes(kwLower)) continue;

      worldChars.forEach(wc => {
        const wcName = (wc.display_name || wc.name || '').toLowerCase();
        if (wcName.includes(kwLower) || kwLower.includes(wcName)) {
          if (!matches.some(m => m.id === wc.id)) {
            matches.push({
              type: 'world_character',
              id: wc.id,
              name: wc.display_name || wc.name,
              long_summary: wc.long_summary || '',
              rpg: wc.rpg_stats,
              traits: wc.character_traits || []
            });
          }
        }
      });

      worldLexicon.forEach(lex => {
        const lName = (lex.name || '').toLowerCase();
        if (lName.includes(kwLower)) {
          if (!matches.some(m => m.id === lex.id)) {
            matches.push({
              type: 'lexicon_' + lex.type,
              id: lex.id,
              name: lex.name
            });
          }
        }
      });
    }

    if (matches.length > 0) {
      console.log(`[MATCH FOUND] #${i + 1} "${bTitle}" (${bId})`);
      matches.forEach(m => {
        if (m.type === 'world_character') {
          const isJed = m.long_summary.includes('[NAME:');
          console.log(`   -> World Character: "${m.name}" (${m.id}) | JED+: ${isJed} | Traits: ${m.traits.length}`);
        } else {
          console.log(`   -> World Lexicon: [${m.type}] "${m.name}" (${m.id})`);
        }
      });
      console.log('');
    }
  }
}

detailedMatch();
