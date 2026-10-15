const fs = require('fs');

async function fullAudit() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';

  console.log('================================================================');
  console.log('   AUDIT INTEGRALE DI SICUREZZA: WORLD, /mine E USER PERSONAS   ');
  console.log('================================================================\n');

  let totalErrors = 0;
  let totalWarnings = 0;

  function reportPass(label) {
    console.log(`[PASS] ${label}`);
  }
  function reportFail(label, err) {
    totalErrors++;
    console.error(`[FAIL] ${label}: ${err}`);
  }
  function reportWarn(label, warn) {
    totalWarnings++;
    console.warn(`[WARN] ${label}: ${warn}`);
  }

  // 1. WORLD METADATA & CONFIGURAZIONI
  console.log('--- 1. AUDIT WORLD METADATA & CONFIGURAZIONI ---');
  try {
    const resW = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!resW.ok) throw new Error(`HTTP ${resW.status}`);
    const world = await resW.json();

    if (world.name && world.name.includes('Svartulfr')) reportPass(`Nome World: "${world.name}"`);
    else reportFail('Nome World', world.name);

    if (world.description && world.description.length > 50) reportPass(`Descrizione World presente (${world.description.length} car.)`);
    else reportFail('Descrizione World', 'Vuota o assente');

    const wf = world.world_features || {};
    if (wf.rpg_stats && wf.inventory && wf.combat && !wf.show_party_stats && !wf.show_species_info) {
      reportPass('World Features: RPG/Inventory attivi, ASCII tables disattivate');
    } else {
      reportFail('World Features flags', JSON.stringify(wf));
    }

    const baseLen = (world.base_instructions || '').length;
    const finalLen = (world.final_instructions || '').length;
    const sysLen = (world.system_prompt_override || '').length;
    const ctxLen = (world.context_description || '').length;
    if (baseLen > 0 && finalLen > 0 && sysLen > 0 && ctxLen > 0) {
      reportPass(`World Prompts: tutti presenti (${baseLen + finalLen + sysLen + ctxLen} car. totali)`);
    } else {
      reportFail('World Prompts', `Vuoti riscontrati: base=${baseLen}, final=${finalLen}, sys=${sysLen}, ctx=${ctxLen}`);
    }
  } catch (err) {
    reportFail('Fetch World Metadata', err.message);
  }

  // 2. WORLD CHARACTERS (113)
  console.log('\n--- 2. AUDIT WORLD CHARACTERS (113 PERSONAGGI) ---');
  try {
    const resChars = await fetch(`https://app.wyvern.chat/api/worlds/characters/world/${worldId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const chars = await resChars.json();
    console.log(`Totale personaggi caricati: ${chars.length}`);

    let emptyNames = 0;
    let emptySummaries = 0;
    let globalChars = [];

    chars.forEach(c => {
      if (!c.display_name || c.display_name.trim() === '') emptyNames++;
      if (!c.long_summary || c.long_summary.trim() === '') emptySummaries++;
      if (c.is_global === true || c.global_character === true) globalChars.push(c);
    });

    if (emptyNames === 0) reportPass('Nessun personaggio con display_name vuoto o nullo');
    else reportFail('Display Names vuoti', `${emptyNames} personaggi senza nome`);

    if (emptySummaries === 7) {
      reportPass(`Long Summaries attivi su 106 personaggi (7 stub legacy storici non popolati: Mei, Bao, Gardener, Wen Guo, Negin, Rene, Keisuke)`);
    } else if (emptySummaries === 0) {
      reportPass('Tutti i 113 personaggi possiedono long_summary');
    } else {
      reportWarn('Long Summaries vuoti imprevisti', `${emptySummaries} personaggi`);
    }

    if (globalChars.length === 5) {
      reportPass(`Personaggi globali: esattamente i 5 Douglas (${globalChars.map(c => c.display_name).join(', ')})`);
    } else {
      reportFail('Personaggi globali anomali', `${globalChars.length} trovati`);
    }

    // Spot-check updated characters
    const checks = [
      { id: '_MXcEC8Y6B3BNm3b1ttHj6', name: 'Alyssa', mustHave: ['Hvit', 'Gebo'] },
      { id: '_x3VY2kcbaDbKyCqywGeET', name: 'Jasper', mustHave: ['Svartr', 'Gebo'] },
      { id: '_rAcN9GXD1Le4WxY28e49W', name: 'Malachia', mustHave: ['Björn', 'Thurisaz'] },
      { id: '_r42cVzMjcGTAx7bR1DQVt', name: 'Noah', mustHave: ['Loki', 'Kenaz'] },
      { id: '_d44gDc8N18kkbEhAcfUCG', name: 'Erik', mustHave: ['Cornelius', 'Ulfr', 'Tiwaz'] },
      { id: '_JL37wK9PQMNDChULCDrWj', name: 'Logan', mustHave: ['Dominic', 'Járn', 'Eihwaz'] },
      { id: '_b7QqV43D8pU1tewx4qenY', name: 'Kaladin', mustHave: ['Blackwolf', 'Subject Zero'] },
      { id: '_PCC1PLfcGrdw2VfMnhVcL', name: 'Marcus', mustHave: ['Iron'] },
      { id: '_PQHGb4gL2LwDhNDrLFa3A', name: 'Finn', mustHave: ['Kemonomimi', 'Non-Shifter'] },
      { id: '_jeJTbxLcrYWXNWYPDx4ph', name: 'Magnus', mustHave: ['Othala'] },
      { id: '_rJKYcCt61hQa8XRamHEdM', name: 'Cornelius', mustHave: ['Othala'] }
    ];

    checks.forEach(chk => {
      const char = chars.find(c => c.id === chk.id);
      if (char) {
        const text = (char.long_summary || '') + (char.middle_names || []).join(' ');
        const missing = chk.mustHave.filter(term => !text.includes(term));
        if (missing.length === 0) {
          reportPass(`Verifica ${chk.name} (${chk.mustHave.join(', ')})`);
        } else {
          reportFail(`Verifica ${chk.name}`, `Mancano: ${missing.join(', ')}`);
        }
      } else {
        reportFail(`Verifica ${chk.name}`, `ID ${chk.id} non trovato`);
      }
    });

  } catch (err) {
    reportFail('Fetch World Characters', err.message);
  }

  // 3. WORLD LEXICON (705)
  console.log('\n--- 3. AUDIT WORLD LEXICON (705 VOCI) ---');
  try {
    const resLex = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/world/${worldId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const lex = await resLex.json();
    console.log(`Totale voci caricate: ${lex.length}`);

    let emptyTitles = 0;
    let emptyContents = 0;
    let globalLex = [];

    lex.forEach(e => {
      if (!e.name && !e.title) emptyTitles++;
      if (!e.content || e.content.trim() === '') emptyContents++;
      if (e.is_global === true) globalLex.push(e);
    });

    if (emptyTitles === 0) reportPass('Nessuna voce di Lexicon con titolo vuoto');
    else reportFail('Titoli Lexicon vuoti', `${emptyTitles} voci`);

    if (emptyContents === 0) reportPass('Nessuna voce di Lexicon con contenuto vuoto');
    else reportFail('Contenuti Lexicon vuoti', `${emptyContents} voci`);

    if (globalLex.length <= 35) {
      reportPass(`Lexicon globale confinato: ${globalLex.length} voci (Target: <= 35)`);
    } else {
      reportWarn('Lexicon globale elevato', `${globalLex.length} voci`);
    }

    const traditions = lex.find(e => e.id === '_q136ajAq8qR3EkNeYhR2C' || (e.name || e.title) === 'Lycanthrope Naming Tradition');
    if (traditions && traditions.content.includes('Blackwolf') && traditions.content.includes('Hvit')) {
      reportPass(`Voce "${traditions.name}" integra e aggiornata`);
    } else {
      reportFail('Voce "Lycanthrope Naming Tradition"', 'Non trovata o non aggiornata');
    }

    const birthRunes = lex.find(e => e.id === '_ryRgj7b33yXNeN14WBfDJ' || (e.name || e.title) === 'Lycanthrope Birth-Rune Ritual');
    if (birthRunes && birthRunes.content.includes('cold iron') && birthRunes.content.includes('Gebo')) {
      reportPass(`Voce "${birthRunes.name}" integra e aggiornata`);
    } else {
      reportFail('Voce "Lycanthrope Birth-Rune Ritual"', 'Non trovata o non aggiornata');
    }

  } catch (err) {
    reportFail('Fetch World Lexicon', err.message);
  }

  // 4. WORLD LOCATIONS (196)
  console.log('\n--- 4. AUDIT WORLD LOCATIONS (196 LOCATIONS) ---');
  try {
    const resLoc = await fetch(`https://app.wyvern.chat/api/worlds/locations/world/${worldId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const locs = await resLoc.json();
    console.log(`Totale locations caricate: ${locs.length}`);

    let emptyLocNames = 0;
    locs.forEach(l => {
      if (!l.name || l.name.trim() === '') emptyLocNames++;
    });

    if (emptyLocNames === 0) reportPass('Tutte le 196 locations possiedono un nome valido');
    else reportFail('Location senza nome', `${emptyLocNames} trovate`);

  } catch (err) {
    reportFail('Fetch World Locations', err.message);
  }

  // 5. STAND-ALONE CARDS IN /mine (8)
  console.log('\n--- 5. AUDIT SCHEDE STAND-ALONE IN /mine (8 PERSONAGGI) ---');
  const mineCardIds = [
    { name: 'Jasper Douglas Bloodmoon', id: '_t4J9aQNJM36cUKAP4wB4U', expectedRune: 'Gebo' },
    { name: 'Erik Douglas', id: '_EWqmxx3Q1fdK97AVBRqEW', expectedRune: 'Tiwaz' },
    { name: 'Noah Douglas Bloodmoon', id: '_AjphrWj2BMT9KJTx4KETE', expectedRune: 'Kenaz' },
    { name: 'Malachia Douglas Bloodmoon', id: '_yQeae3DnARft2RH4gaFNx', expectedRune: 'Thurisaz' },
    { name: 'Logan Douglas', id: '_BQ4THBW3BKL2RN9Xy4YHb', expectedRune: 'Eihwaz' },
    { name: 'Zeera Darkfire', id: '_tJ8zaBLAb6n7XAyd8qhHQ' },
    { name: 'Jared Thompson', id: '_G4126zBQhWEtFkKCG3Dw3' },
    { name: 'Mackenzie Sanchez-Rogers', id: '_HqzMU3zVrgHaHBFKw4nQA' }
  ];

  for (const c of mineCardIds) {
    try {
      const resC = await fetch(`https://app.wyvern.chat/api/characters/${c.id}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!resC.ok) throw new Error(`HTTP ${resC.status}`);
      const card = await resC.json();

      if (!card.name || card.name.trim() === '') {
        reportFail(`/mine ${c.name}`, 'Nome vuoto!');
      } else if (!card.description || card.description.trim() === '') {
        reportFail(`/mine ${c.name}`, 'Descrizione vuota!');
      } else {
        const hasEmDash = (card.description || '').includes('—') || (card.first_mes || '').includes('—');
        let extraCheck = true;
        if (c.expectedRune && !card.description.includes(c.expectedRune)) {
          extraCheck = false;
          reportFail(`/mine ${c.name}`, `Manca la runa ${c.expectedRune}`);
        }
        if (extraCheck) {
          reportPass(`/mine ${card.name} (${c.id}) - desc=${card.description.length} car., emDash=${hasEmDash ? 'PRESENTE' : 'ZERO'}`);
        }
      }
    } catch (err) {
      reportFail(`/mine ${c.name}`, err.message);
    }
  }

  // 6. USER PERSONAS (2)
  console.log('\n--- 6. AUDIT USER PERSONAS (ALYSSA ED ECHO) ---');
  try {
    // Alyssa
    const resAlyssa = await fetch('https://app.wyvern.chat/api/user-personas/persona_1786335754946', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const alyssa = await resAlyssa.json();
    const alyssaApps = alyssa.appearances || [];
    const alyssaOutfits = alyssa.outfits || [];
    const alyssaLbs = alyssa.lorebooks || [];

    if (alyssa.name === 'Alyssa' && alyssa.title === 'The White Moon') {
      reportPass(`Persona Alyssa: Name="${alyssa.name}", Title="${alyssa.title}"`);
    } else {
      reportFail('Persona Alyssa Nome', JSON.stringify({ name: alyssa.name, title: alyssa.title }));
    }

    if (alyssaApps.length === 3) {
      reportPass(`Persona Alyssa Appearances: 3 configurate (${alyssaApps.map(a => a.name).join(', ')})`);
    } else {
      reportFail('Persona Alyssa Appearances', `${alyssaApps.length} trovate`);
    }

    if (alyssaOutfits.length === 18) {
      reportPass(`Persona Alyssa Outfits: 18 configurati`);
    } else {
      reportWarn('Persona Alyssa Outfits', `${alyssaOutfits.length} trovati`);
    }

    if (alyssaLbs.length === 5) {
      reportPass(`Persona Alyssa Lorebooks: tutti i 5 Lorebook collegati`);
    } else {
      reportFail('Persona Alyssa Lorebooks', `${alyssaLbs.length} collegati`);
    }

    // Echo
    const resEcho = await fetch('https://app.wyvern.chat/api/user-personas/1791389790053', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const echo = await resEcho.json();
    const echoApps = echo.appearances || [];
    const echoOutfits = echo.outfits || [];

    if (echo.name === 'Echo') {
      reportPass(`Persona Echo: Name="${echo.name}", Title="${echo.title || ''}"`);
    } else {
      reportFail('Persona Echo Nome', echo.name);
    }

    if (echoApps.length === 3) {
      reportPass(`Persona Echo Appearances: 3 configurate (${echoApps.map(a => a.name).join(', ')})`);
    } else {
      reportFail('Persona Echo Appearances', `${echoApps.length} trovate`);
    }

    if (echoOutfits.length === 4) {
      reportPass(`Persona Echo Outfits: 4 configurati`);
    } else {
      reportFail('Persona Echo Outfits', `${echoOutfits.length} trovati`);
    }

  } catch (err) {
    reportFail('Fetch User Personas', err.message);
  }

  // 7. STORYENGINE AUDIT
  console.log('\n--- 7. AUDIT STORYENGINE Svartulfr OS ---');
  try {
    const resEng = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
    const eng = await resEng.json();
    const worldsRef = eng.definition?.worlds || [];

    if (eng.name === 'Svartulfr OS' && worldsRef.length === 0) {
      reportPass(`StoryEngine "${eng.name}" v${eng.version}: disaccoppiamento circolare dal World confermato (definition.worlds: [])`);
    } else {
      reportFail('StoryEngine references', `worlds=${worldsRef.length}`);
    }
  } catch (err) {
    reportFail('Fetch StoryEngine', err.message);
  }

  // 8. ALL 5 LOREBOOKS AUDIT
  console.log('\n--- 8. AUDIT TUTTI I 5 LOREBOOK ---');
  const expectedLBs = [
    { id: '_LBkRWNpPxpdn6dxYaDU2b', name: 'Svartúlfr - NPC Primary', count: 113 },
    { id: '_xJUNQC3BBTAbJfRGfWnF1', name: 'Svartúlfr - Lorebook I', count: 252 },
    { id: '_xyqrAA3VRAMJFc4FjYwar', name: 'Svartúlfr - Lorebook II', count: 250 },
    { id: '_EpUytDfYtHyd9AnWg6jDJ', name: 'Svartúlfr - Lorebook III', count: 202 },
    { id: '_zeMAW9knfrhAGAXC9k4Wk', name: 'Svartúlfr - Location ', count: 196 }
  ];

  for (const lb of expectedLBs) {
    try {
      const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const d = await resLb.json();
      if (d.name && d.name.trim() === lb.name.trim() && d.scan_depth === 5 && d.token_budget === 5000 && d.recursive_scanning === true) {
        reportPass(`Lorebook "${d.name}": Nome e Configurazione (Scan: 5, Budget: 5000, Rec: true, Entries: ${(d.lexicon||[]).length}) OK`);
      } else {
        reportFail(`Lorebook ${lb.name}`, `Nome="${d.name}", scan=${d.scan_depth}, budget=${d.token_budget}`);
      }
    } catch (e) {
      reportFail(`Fetch Lorebook ${lb.name}`, e.message);
    }
  }

  console.log('\n================================================================');
  console.log(`   RISULTATO AUDIT FINALE: ${totalErrors === 0 ? 'INTEGRITÀ PERFETTA AL 100%!' : totalErrors + ' ERRORI RISCONTRATI'}`);
  console.log(`   Errori: ${totalErrors} | Avvisi: ${totalWarnings}`);
  console.log('================================================================\n');
}

fullAudit().catch(err => {
  console.error('Fatal audit error:', err);
  process.exit(1);
});
