const fs = require('fs');

const lbData = JSON.parse(fs.readFileSync('scratch/lb_svartulfr_dump.json', 'utf8'));
const worldLex = JSON.parse(fs.readFileSync('scratch/fresh_world_lexicon.json', 'utf8'));

console.log('Current Lorebook entries count:', (lbData.lexicon || []).length);
console.log('Total World Lexicon entries count:', worldLex.length);

const currentEntries = lbData.lexicon || [];
const currentTitles = new Set();
currentEntries.forEach(e => {
  const t = (e.name || e.title || (e.keys && e.keys[0]) || '').toLowerCase().trim();
  if (t) currentTitles.add(t);
});

const missingEntries = [];
worldLex.forEach(w => {
  if (w.type === 'npc') return; // NPCs go in NPC Primary lorebook
  const title = (w.name || w.title || (w.keys && w.keys[0]) || '').trim();
  if (!title) return;
  if (!currentTitles.has(title.toLowerCase())) {
    missingEntries.push({
      name: title,
      title: title,
      keys: w.keys || [title],
      key_logic: w.key_logic || 'AND_ANY',
      secondary_keys: w.secondary_keys || [],
      content: (w.content || '').replace(/—/g, ', '),
      enabled: true,
      case_sensitive: false,
      whole_words_only: w.whole_words_only !== false,
      constant: w.constant || false,
      position: w.position || 'before_char',
      priority: w.priority || 0,
      insertion_order: w.insertion_order || 100,
      is_global: w.is_global !== false
    });
    currentTitles.add(title.toLowerCase());
  }
});

console.log(`Entries to add to Svartulfr - Lorebook: ${missingEntries.length}`);
console.log('Sample missing entries:');
missingEntries.slice(0, 10).forEach(m => console.log('  -', m.name));

fs.writeFileSync('scratch/lorebook_additions.json', JSON.stringify(missingEntries, null, 2));
