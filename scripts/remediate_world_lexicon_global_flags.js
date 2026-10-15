const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();
const worldId = '_CgYT8fHXpDC4crjmegQF7';

// Whitelist of Universal Core Concept IDs that MUST stay is_global: true
const universalGlobalIds = new Set([
  '_LCywywQ1hAGNd3XHpgPF3', // LSE Core Principles & Canon Policy
  '_6DabnWdFrqGt4TPcPtV3Y', // LSE Terminology & Glossary
  '_AhRPDRjVcRQ1BWnJ8J3z7', // LSE Social Hierarchy (Bloodline, House, Pack, Family)
  '_zqFVpbAtpeBjVkA4KpxkR', // LSE Six-Axis Identity System
  '_V83DmAJaMP2Y3hXwrt7dy', // LSE Shift Classes (Partial, Hybrid, Full)
  '_r4A9HbcfqE7EhGct8cPQU', // LSE Secondary Sex Physiology
  '_EEPyKdqgCNVwVAaaA96hp', // LSE Scent Glands
  '_nWfTYmUmjCEReR1cTtmkf', // LSE Neurobiology (Pheromones, The Command, Bonding)
  '_HGbtNkakRdDQ7YxqQBwNJ', // LSE Medicine (Treatments, Suppressants, Omega Pain Scale)
  '_WwMyPe7zpVnU2FbmqzBqP', // LSE Blood Classification
  '_KefEdazJ9gDWnTFwM6XV9', // Species: Vampire
  '_kjYznc1nkwYbKbP2QfjHb', // Supernatural Civil Status in the United States
  '_Py1N2Lh64D4c8gkkMatpA', // SUCC Master Calendar & Diurnal Cycle
  '_dBJXFfzdbjXFRUnLLQKf2', // SUCC: Protocollo di Sicurezza Luna Piena
  '_h4mzJh4DBQ9pngaa4DPq7', // Anti-Vampire Legislation
  '_LyHK91bhWrej3K4XyWW6h', // Supernatural Underworld
  '_4bg7BKpHbBwkW6nLArqB9', // LSE Pantheon & the Nine Precepts of Fenris
  '_ALr42Gp4YJGrBdEebpJ83', // LSE Sacred Calendar of Fenris (Monthly Lunar Observances)
  '_3hWVPHUeH4YqyxWacMr4K', // LSE Culture & Traditions (incl. Eíða-Siðr Svartúlfr Pack Oath)
  '_QmPpW9aJTa2WPrMfEQjaY', // The Douglas Face
  '_c8jYQCtx6dg22eVMNED97', // LSE Types of Packs (Traditional, Contemporary, Modern)
  '_2wFBBdnwNFc8dgP1FWYt8', // LSE Social Status & House Government
  '_JpWNXRxdtYBygpzfBJBeV', // LSE Psychology Profiles (Alpha, Delta, Beta, Omega, Enigma)
  '_7UMVk4jm2HWhH3YF7Pxp4', // LSE Nesting & Den Behavior, Scent Reference Lists
  '_8ppCdat3KN9KqArERKkE3', // LSE Naming Conventions & Titles
  '_w6c66b2pc6yyzdfGNV9V6', // LSE Moon Theology & Cult of the Living Sagas
  '_3Rhf8x6wF78V7AGY1gTXa', // LSE Pack Authority Structure
  '_QXrGtPTEYVCqEj6endaBg', // LSE Life Cycle, Genetics & Demographics
  '_yPz7Ha7GB6d9Kpp7CYn4T', // LSE Laws, Crimes & Exile
  '_8wBmMFwkHLENMpPwKExyt'  // LSE Communication (Non-Verbal & Vocalizations)
]);

async function remediateLexicon() {
  console.log('Fetching all World Lexicon entries...');
  const res = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/world/${worldId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!res.ok) throw new Error('Failed to fetch lexicon: ' + res.status);
  const entries = await res.json();
  console.log(`Total World Lexicon entries: ${entries.length}`);

  // Save snapshot before changes
  fs.writeFileSync('scratch/pre_remediation_world_lexicon.json', JSON.stringify(entries, null, 2), 'utf8');

  // Identify targets to set is_global: false
  const targets = entries.filter(e => e.is_global === true && !universalGlobalIds.has(e.id));
  console.log(`Entries to update (set is_global: false): ${targets.length}`);
  console.log(`Entries to keep is_global: true: ${universalGlobalIds.size}`);

  const batchSize = 25;
  let updatedCount = 0;

  for (let i = 0; i < targets.length; i += batchSize) {
    const batch = targets.slice(i, i + batchSize);
    console.log(`Processing batch ${Math.floor(i / batchSize) + 1} (${batch.length} entries, progress ${i}/${targets.length})...`);

    await Promise.all(batch.map(async (entry) => {
      const putRes = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/${entry.id}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ is_global: false })
      });
      if (putRes.ok) {
        updatedCount++;
      } else {
        console.error(`Error updating entry ${entry.id} (${entry.name}): HTTP ${putRes.status}`);
      }
    }));

    // Gentle pause between batches
    await new Promise(r => setTimeout(r, 200));
  }

  console.log(`\nRemediation complete! Successfully updated ${updatedCount} entries to is_global: false.`);

  // Verify fresh state
  console.log('\nVerifying updated state via fresh GET...');
  const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/world/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const freshEntries = await verifyRes.json();
  const remainingGlobals = freshEntries.filter(e => e.is_global === true);
  console.log(`Remaining global entries count: ${remainingGlobals.length}`);
  remainingGlobals.forEach(g => console.log(`- [${g.type||'none'}] ${g.name} (${g.id})`));
}

remediateLexicon().catch(console.error);
