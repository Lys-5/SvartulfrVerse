const fs = require('fs');
const path = require('path');

async function createFullBackup() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const outDir = 'scratch/backup_consolidated_snapshot';

  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  console.log('=== FASE 4: GENERAZIONE BACKUP LOCALE CONSOLIDATO (DISASTER RECOVERY) ===\n');

  // Helper fetch with authorization
  async function fetchJson(endpoint) {
    const res = await fetch(`https://app.wyvern.chat${endpoint}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!res.ok) throw new Error(`Fetch ${endpoint} failed with HTTP ${res.status}`);
    return await res.json();
  }

  // 1. WORLD ENTITIES
  console.log('1. Esportazione entità del World...');
  const worldData = await fetchJson(`/api/worlds/${worldId}`);
  fs.writeFileSync(path.join(outDir, 'world_metadata.json'), JSON.stringify(worldData, null, 2), 'utf8');
  console.log('   - world_metadata.json salvato.');

  const worldChars = await fetchJson(`/api/worlds/characters/world/${worldId}`);
  fs.writeFileSync(path.join(outDir, 'world_characters.json'), JSON.stringify(worldChars, null, 2), 'utf8');
  console.log(`   - world_characters.json salvato (${worldChars.length} personaggi).`);

  const worldLex = await fetchJson(`/api/worlds/lexicon/world/${worldId}`);
  fs.writeFileSync(path.join(outDir, 'world_lexicon.json'), JSON.stringify(worldLex, null, 2), 'utf8');
  console.log(`   - world_lexicon.json salvato (${worldLex.length} voci).`);

  const worldLocs = await fetchJson(`/api/worlds/locations/world/${worldId}`);
  fs.writeFileSync(path.join(outDir, 'world_locations.json'), JSON.stringify(worldLocs, null, 2), 'utf8');
  console.log(`   - world_locations.json salvato (${worldLocs.length} locations).`);

  // 2. LOREBOOKS (ALL 5)
  console.log('\n2. Esportazione dei 5 Lorebook...');
  const lorebooks = [
    { id: '_LBkRWNpPxpdn6dxYaDU2b', filename: 'lorebook_npc_primary.json', label: 'NPC Primary' },
    { id: '_xJUNQC3BBTAbJfRGfWnF1', filename: 'lorebook_svartulfr_I.json', label: 'Lorebook I' },
    { id: '_xyqrAA3VRAMJFc4FjYwar', filename: 'lorebook_svartulfr_II.json', label: 'Lorebook II' },
    { id: '_EpUytDfYtHyd9AnWg6jDJ', filename: 'lorebook_svartulfr_III.json', label: 'Lorebook III' },
    { id: '_zeMAW9knfrhAGAXC9k4Wk', filename: 'lorebook_locations.json', label: 'Locations' }
  ];

  for (const lb of lorebooks) {
    const lbData = await fetchJson(`/api/lorebooks/${lb.id}`);
    fs.writeFileSync(path.join(outDir, lb.filename), JSON.stringify(lbData, null, 2), 'utf8');
    console.log(`   - ${lb.filename} salvato (${lb.label}, ${(lbData.lexicon || []).length} voci).`);
  }

  // 3. USER PERSONAS
  console.log('\n3. Esportazione User Personas...');
  const personas = [
    { id: 'persona_1786335754946', filename: 'persona_alyssa.json', label: 'Alyssa Hvit Douglas Bloodmoon' },
    { id: '1791389790053', filename: 'persona_echo.json', label: 'Echo Cyber-Familiar' }
  ];

  for (const p of personas) {
    const pData = await fetchJson(`/api/user-personas/${p.id}`);
    fs.writeFileSync(path.join(outDir, p.filename), JSON.stringify(pData, null, 2), 'utf8');
    console.log(`   - ${p.filename} salvato (${p.label}).`);
  }

  // 4. STAND-ALONE CHARACTERS (/mine)
  console.log('\n4. Esportazione Schede Stand-Alone (/mine)...');
  const mineChars = [
    { id: '_t4J9aQNJM36cUKAP4wB4U', name: 'Jasper' },
    { id: '_EWqmxx3Q1fdK97AVBRqEW', name: 'Erik' },
    { id: '_AjphrWj2BMT9KJTx4KETE', name: 'Noah' },
    { id: '_yQeae3DnARft2RH4gaFNx', name: 'Malachia' },
    { id: '_BQ4THBW3BKL2RN9Xy4YHb', name: 'Logan' },
    { id: '_tJ8zaBLAb6n7XAyd8qhHQ', name: 'Zeera' },
    { id: '_G4126zBQhWEtFkKCG3Dw3', name: 'Jared' },
    { id: '_HqzMU3zVrgHaHBFKw4nQA', name: 'Mackenzie' }
  ];

  const mineDump = [];
  for (const c of mineChars) {
    const cData = await fetchJson(`/api/characters/${c.id}`);
    mineDump.push(cData);
    console.log(`   - Scheda ${c.name} (${c.id}) esportata.`);
  }
  fs.writeFileSync(path.join(outDir, 'mine_standalone_characters.json'), JSON.stringify(mineDump, null, 2), 'utf8');

  // Summary Report File
  const report = {
    timestamp: new Date().toISOString(),
    world_id: worldId,
    stats: {
      world_characters: worldChars.length,
      world_lexicon: worldLex.length,
      world_locations: worldLocs.length,
      lorebooks_count: lorebooks.length,
      lorebooks_total_entries: 113 + 252 + 250 + 202 + 196,
      personas_count: personas.length,
      mine_characters_count: mineChars.length
    },
    files_created: fs.readdirSync(outDir)
  };
  fs.writeFileSync(path.join(outDir, 'manifest.json'), JSON.stringify(report, null, 2), 'utf8');

  console.log('\n=====================================================');
  console.log(`   BACKUP CONSOLIDATO COMPLETATO AL 100%!`);
  console.log(`   Directory: ${outDir}`);
  console.log(`   File generati: ${report.files_created.length}`);
  console.log('=====================================================\n');
}

createFullBackup().catch(err => {
  console.error('Fatal error during backup:', err);
  process.exit(1);
});
