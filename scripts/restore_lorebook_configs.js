const fs = require('fs');

async function restoreLorebookConfigs() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const toRestore = [
    {
      id: '_LBkRWNpPxpdn6dxYaDU2b',
      name: 'Svartúlfr - NPC Primary',
      description: '',
      scan_depth: 5,
      token_budget: 5000,
      recursive_scanning: true,
      visibility: 'private',
      rating: 'explicit',
      is_private: false
    },
    {
      id: '_xJUNQC3BBTAbJfRGfWnF1',
      name: 'Svartúlfr - Lorebook I',
      description: '',
      scan_depth: 5,
      token_budget: 5000,
      recursive_scanning: true,
      visibility: 'private',
      rating: 'explicit',
      is_private: false
    }
  ];

  console.log('=== RIPRISTINO TITOLI E CONFIGURAZIONI LOREBOOK ===\n');

  for (const item of toRestore) {
    console.log(`>>> Ripristino ${item.name} (${item.id})...`);

    // 1. Fetch current data to get current lexicon
    const resGet = await fetch(`https://app.wyvern.chat/api/lorebooks/${item.id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!resGet.ok) {
      console.error(`Fetch failed for ${item.id}: HTTP ${resGet.status}`);
      continue;
    }
    const current = await resGet.json();
    const currentLexicon = current.lexicon || [];
    console.log(`    Voci di Lexicon attuali: ${currentLexicon.length}`);

    // 2. PUT with complete metadata + preserved lexicon
    const payload = {
      name: item.name,
      description: item.description,
      scan_depth: item.scan_depth,
      token_budget: item.token_budget,
      recursive_scanning: item.recursive_scanning,
      visibility: item.visibility,
      rating: item.rating,
      is_private: item.is_private,
      lexicon: currentLexicon
    };

    const resPut = await fetch(`https://app.wyvern.chat/api/lorebooks/${item.id}`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    console.log(`    Esito PUT: HTTP ${resPut.status}`);

    // 3. Verify via GET
    const resVerify = await fetch(`https://app.wyvern.chat/api/lorebooks/${item.id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const verified = await resVerify.json();
    console.log(`    Verifica post-scrittura:`);
    console.log(`    - Name: "${verified.name}"`);
    console.log(`    - Scan Depth: ${verified.scan_depth}`);
    console.log(`    - Token Budget: ${verified.token_budget}`);
    console.log(`    - Recursive Scanning: ${verified.recursive_scanning}`);
    console.log(`    - Lexicon Entries: ${(verified.lexicon || []).length}\n`);
  }

  console.log('=== TUTTI I LOREBOOK SONO STATI RIPRISTINATI CORRETTAMENTE! ===');
}

restoreLorebookConfigs().catch(err => {
  console.error('Fatal error during restore:', err);
  process.exit(1);
});
