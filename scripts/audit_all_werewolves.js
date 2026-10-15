const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const npcLbId = '_LBkRWNpPxpdn6dxYaDU2b';

  console.log('Fetching all World Characters...');
  const resW = await fetch(`https://app.wyvern.chat/api/worlds/characters/world/${worldId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const worldChars = await resW.json();

  console.log('Fetching NPC Primary Lorebook...');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lbData = await resLb.json();
  const lbEntries = lbData.lexicon || [];

  const werewolfMap = new Map();

  function isWerewolf(text, species) {
    const combined = `${text || ''} ${species || ''}`.toLowerCase();
    return combined.includes('werewolf') ||
           combined.includes('licantrop') ||
           combined.includes('lupine') ||
           combined.includes('bloodmoon') ||
           combined.includes('lupo');
  }

  // 1. Process World Characters
  for (const c of worldChars) {
    const text = `${c.display_name} ${c.first_name} ${c.long_summary || ''}`;
    const sp = c.species?.name || '';
    if (isWerewolf(text, sp)) {
      const line0 = (c.long_summary || '').split('\n')[0];
      const hasRune = /birth[ _-]?rune/i.test(c.long_summary || '');
      const runeMatch = (c.long_summary || '').match(/birth[ _-]?rune[:\s]+([a-zA-Z\(\)\s&]+?)(?:;|\n|\])/i);
      const rune = runeMatch ? runeMatch[1].trim() : 'NONE';

      werewolfMap.set(c.id, {
        id: c.id,
        name: c.display_name,
        first_name: c.first_name,
        middle_names: c.middle_names || [],
        last_name: c.last_name,
        source: 'World Character',
        line0: line0.slice(0, 120),
        hasBirthRune: hasRune,
        birthRune: rune,
        summaryLen: (c.long_summary || '').length
      });
    }
  }

  // 2. Process NPC Primary Lorebook
  for (const e of lbEntries) {
    const text = `${e.name || e.title} ${e.content || ''}`;
    if (isWerewolf(text, '')) {
      const line0 = (e.content || '').split('\n')[0];
      const hasRune = /birth[ _-]?rune/i.test(e.content || '');
      const runeMatch = (e.content || '').match(/birth[ _-]?rune[:\s]+([a-zA-Z\(\)\s&]+?)(?:;|\n|\])/i);
      const rune = runeMatch ? runeMatch[1].trim() : 'NONE';

      const existing = [...werewolfMap.values()].find(w => w.name === e.name || (w.first_name && e.name && e.name.includes(w.first_name)));
      if (existing) {
        existing.source = 'Both (World + Lorebook)';
        existing.lbName = e.name;
        existing.lbHasRune = hasRune;
        existing.lbRune = rune;
      } else {
        werewolfMap.set(e.name, {
          id: e.entry_id || 'lb_entry',
          name: e.name,
          source: 'Lorebook NPC Primary',
          line0: line0.slice(0, 120),
          hasBirthRune: hasRune,
          birthRune: rune,
          summaryLen: (e.content || '').length
        });
      }
    }
  }

  const results = [...werewolfMap.values()];
  console.log(`\n=== TOTALE WEREWOLF INDIVIDUATI: ${results.length} ===`);
  results.forEach((w, idx) => {
    console.log(`${idx + 1}. [${w.source}] ${w.name}`);
    console.log(`   Middle: ${JSON.stringify(w.middle_names || [])} | Birth-Rune: ${w.birthRune}`);
    console.log(`   Line 0: ${w.line0}...`);
  });

  fs.writeFileSync('scratch/all_werewolves_audit.json', JSON.stringify(results, null, 2), 'utf8');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
