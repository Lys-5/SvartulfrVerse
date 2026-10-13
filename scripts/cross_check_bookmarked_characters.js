const fs = require('fs');

async function crossCheckBookmarkedCharacters() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldData = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
  const worldChars = worldData.world_characters || [];
  const worldLexicon = worldData.lexicon || [];

  const res = await fetch('https://app.wyvern.chat/api/inventory/collection/characters?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const data = await res.json();
  const bookmarked = data.items || [];

  console.log(`=== AUDIT BOOKMARKED CHARACTERS (${bookmarked.length} totali) ===\n`);

  const results = [];

  for (let i = 0; i < bookmarked.length; i++) {
    const b = bookmarked[i];
    const bName = (b.name || b.display_name || '').trim();
    const bId = b.id || b._id;
    const bCreator = b.creator?.displayName || b.creator?.uid || 'Unknown';

    // Check matches in world characters
    // Normalized name matching (e.g. Barrow, Marek, Radek, Goran, Kian, Neve, Jaelyn, Liam, Hugh, Bessie May, etc.)
    const matchesInWorld = [];
    for (const wc of worldChars) {
      const wcName = (wc.display_name || wc.name || '').trim();
      // Match exact or substring or specific aliases
      const bLower = bName.toLowerCase();
      const wcLower = wcName.toLowerCase();

      // Check if wcName is in bName or bName is in wcName or first names match
      const bFirstName = bLower.split(/[\s,•|]+/)[0];
      const wcFirstName = wcLower.split(/[\s,•|]+/)[0];

      if (bLower.includes(wcLower) || wcLower.includes(bLower)) {
        matchesInWorld.push(wc);
      } else if (bFirstName.length >= 4 && bFirstName === wcFirstName) {
        matchesInWorld.push(wc);
      }
    }

    // Check matches in world lexicon
    const matchesInLexicon = [];
    for (const lex of worldLexicon) {
      const lName = (lex.name || '').toLowerCase();
      const bLower = bName.toLowerCase();
      const bFirstName = bLower.split(/[\s,•|]+/)[0];
      if (bFirstName.length >= 4 && lName.includes(bFirstName)) {
        matchesInLexicon.push(lex);
      }
    }

    results.push({
      index: i + 1,
      id: bId,
      name: bName,
      creator: bCreator,
      matchesInWorld,
      matchesInLexicon
    });
  }

  console.log('--- PERSONAGGI CON RISCONTRO NEL WORLD ---');
  const matched = results.filter(r => r.matchesInWorld.length > 0 || r.matchesInLexicon.length > 0);
  matched.forEach(r => {
    console.log(`\n#${r.index} [${r.id}] "${r.name}" (Creator: ${r.creator})`);
    if (r.matchesInWorld.length > 0) {
      r.matchesInWorld.forEach(wc => {
        const isJed = (wc.long_summary || '').includes('[NAME:');
        const hasRpg = !!(wc.rpg_stats && wc.character_traits && wc.character_traits.length > 0);
        console.log(`   -> WORLD CHARACTER: "${wc.display_name}" (${wc.id}) | JED+: ${isJed} | RPG: ${hasRpg} (Traits: ${(wc.character_traits || []).length})`);
      });
    }
    if (r.matchesInLexicon.length > 0) {
      r.matchesInLexicon.slice(0, 3).forEach(lex => {
        console.log(`   -> WORLD LEXICON (${lex.type}): "${lex.name}" (${lex.id})`);
      });
    }
  });

  console.log('\n--- PERSONAGGI SENZA RISCONTRO NEL WORLD (ESTERNI / NON IMPORTATI) ---');
  const unmatched = results.filter(r => r.matchesInWorld.length === 0 && r.matchesInLexicon.length === 0);
  unmatched.forEach(r => {
    console.log(`#${r.index} [${r.id}] "${r.name}" (Creator: ${r.creator})`);
  });
}

crossCheckBookmarkedCharacters();
