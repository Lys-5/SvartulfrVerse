const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();
const lbId = '_J8x7fwRrpa9C6Wct6hb7p'; // Svartulfr - Lorebook

const lbData = JSON.parse(fs.readFileSync('scratch/lb_svartulfr_dump.json', 'utf8'));
const worldLex = JSON.parse(fs.readFileSync('scratch/fresh_world_lexicon.json', 'utf8'));

// Build lookup map of fresh world entries by normalized title
const worldByTitle = new Map();
worldLex.forEach(w => {
  const t = (w.name || w.title || (w.keys && w.keys[0]) || '').toLowerCase().trim();
  if (t) worldByTitle.set(t, w);
});

// Update existing entries in lbData.lexicon
const updatedExisting = (lbData.lexicon || []).map(entry => {
  const t = (entry.name || entry.title || (entry.keys && entry.keys[0]) || '').toLowerCase().trim();
  if (worldByTitle.has(t)) {
    const w = worldByTitle.get(t);
    return {
      ...entry,
      name: w.name || entry.name,
      title: w.name || entry.title,
      keys: w.keys || entry.keys,
      key_logic: w.key_logic || entry.key_logic || 'AND_ANY',
      secondary_keys: w.secondary_keys || entry.secondary_keys || [],
      content: (w.content || '').replace(/—/g, ', '),
      enabled: true,
      case_sensitive: false,
      whole_words_only: w.whole_words_only !== false,
      is_global: w.is_global !== false
    };
  }
  return entry;
});

// Add new missing entries
const existingTitles = new Set(updatedExisting.map(e => (e.name || e.title || (e.keys && e.keys[0]) || '').toLowerCase().trim()));
const newAdditions = [];

worldLex.forEach(w => {
  if (w.type === 'npc') return;
  const t = (w.name || w.title || (w.keys && w.keys[0]) || '').toLowerCase().trim();
  if (!t) return;
  if (!existingTitles.has(t)) {
    newAdditions.push({
      name: w.name,
      title: w.name,
      keys: w.keys || [w.name],
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
    existingTitles.add(t);
  }
});

const fullLexicon = [...updatedExisting, ...newAdditions];
console.log(`Original Lorebook entries: ${(lbData.lexicon || []).length}`);
console.log(`Updated existing entries: ${updatedExisting.length}`);
console.log(`New entries added: ${newAdditions.length}`);
console.log(`Total final Lorebook entries: ${fullLexicon.length}`);

// Clean all em-dashes and markdown violations
fullLexicon.forEach(e => {
  if (e.content) {
    e.content = e.content.replace(/—/g, ', ');
  }
});

async function updateLorebook() {
  console.log(`Uploading synchronized Svartulfr - Lorebook (${fullLexicon.length} entries)...`);
  const putRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: lbData.name,
      description: lbData.description,
      photoURL: lbData.photoURL,
      lexicon: fullLexicon
    })
  });

  if (!putRes.ok) {
    throw new Error(`PUT lorebook failed (${putRes.status}): ${await putRes.text()}`);
  }

  const result = await putRes.json();
  console.log(`Svartulfr - Lorebook updated successfully! Saved entries count: ${(result.lexicon||[]).length}`);
}

updateLorebook().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
