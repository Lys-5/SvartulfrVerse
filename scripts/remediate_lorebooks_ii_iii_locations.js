const fs = require('fs');

async function remediateLorebooks() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  
  const targetLorebooks = [
    { id: '_xyqrAA3VRAMJFc4FjYwar', name: 'Svartúlfr - Lorebook II', backupFile: 'scratch/backup_pre_remediation_lb2.json' },
    { id: '_EpUytDfYtHyd9AnWg6jDJ', name: 'Svartúlfr - Lorebook III', backupFile: 'scratch/backup_pre_remediation_lb3.json' },
    { id: '_zeMAW9knfrhAGAXC9k4Wk', name: 'Svartúlfr - Location', backupFile: 'scratch/backup_pre_remediation_lb_loc.json' }
  ];

  console.log('=== FASE 1: AUDIT & BONIFICA LOREBOOKS II, III E LOCATION ===\n');

  for (const lb of targetLorebooks) {
    console.log(`>>> Elaborazione ${lb.name} (${lb.id})...`);
    
    // 1. Fetch
    const res = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!res.ok) {
      console.error(`Errore fetch ${lb.id}: HTTP ${res.status}`);
      continue;
    }
    const data = await res.json();
    const lexicon = data.lexicon || [];
    console.log(`    Totale voci caricate: ${lexicon.length}`);

    // 2. Backup preventivo obbligatorio (Regola 11)
    fs.writeFileSync(lb.backupFile, JSON.stringify(data, null, 2), 'utf8');
    console.log(`    Backup preventivo salvato in ${lb.backupFile}`);

    // 3. Scan & Sanitize
    let emDashCount = 0;
    let boldMarkdownCount = 0;
    let modifiedEntries = 0;

    const sanitizedLexicon = lexicon.map(entry => {
      let content = entry.content || '';
      let changed = false;

      // Sostituzione em-dash (—) con virgola o punto secondo contesto
      if (content.includes('—')) {
        const matches = (content.match(/—/g) || []).length;
        emDashCount += matches;
        content = content.replace(/—\s*/g, ', ');
        changed = true;
      }

      // Rimozione grassetti markdown (**) vietati nei testi di world/lexicon
      if (content.includes('**')) {
        const matches = (content.match(/\*\*/g) || []).length;
        boldMarkdownCount += Math.floor(matches / 2);
        content = content.replace(/\*\*([^*]+)\*\*/g, '$1');
        changed = true;
      }

      if (changed) {
        modifiedEntries++;
        return {
          ...entry,
          content: content
        };
      }
      return entry;
    });

    console.log(`    Rilevati: ${emDashCount} em-dash, ${boldMarkdownCount} grassetti markdown in ${modifiedEntries} voci.`);

    if (modifiedEntries > 0) {
      console.log(`    Salvataggio modifiche via PUT su /api/lorebooks/${lb.id}...`);
      const putRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
        method: 'PUT',
        headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({ lexicon: sanitizedLexicon })
      });
      console.log(`    Esito PUT: HTTP ${putRes.status}`);

      // 4. Verifica GET post-scrittura
      const verifyRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const verifyData = await verifyRes.json();
      const stillHasEmDash = (verifyData.lexicon || []).some(e => (e.content || '').includes('—'));
      console.log(`    Verifica post-scrittura: ${verifyData.lexicon.length} voci salvate. Residui em-dash: ${stillHasEmDash ? 'PRESISTENTI (ERRORE)' : 'ZERO (CONFERMATO PULITO)'}\n`);
    } else {
      console.log(`    Nessuna modifica necessaria, archivio già conforme al 100%.\n`);
    }
  }

  console.log('=== FASE 1 COMPLETATA CON SUCCESSO ===');
}

remediateLorebooks().catch(err => {
  console.error('Fatal error in remediateLorebooks:', err);
  process.exit(1);
});
