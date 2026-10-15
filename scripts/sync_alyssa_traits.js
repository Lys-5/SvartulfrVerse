const fs = require('fs');

async function syncAlyssa() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const charId = '_MXcEC8Y6B3BNm3b1ttHj6';
  const personaId = 'persona_1786335754946';
  const lbId = '_LBkRWNpPxpdn6dxYaDU2b'; // Svartúlfr - NPC Primary

  console.log('1. Lettura dati freschi di Alyssa dal World...');
  const resChar = await fetch(`https://app.wyvern.chat/api/worlds/characters/${charId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!resChar.ok) throw new Error(`Fetch character failed: ${resChar.status}`);
  const alyssaWorld = await resChar.json();

  const traitsBlock = `RPG STATS & TRAITS:
[LEVEL: 3; SPECIES: Werewolf (Founding Bloodline); OCCUPATION: Novice Healing Mage, Pre-Med Healer; CLASS: Guild Support (Healer/Mage)]
[BASE_STATS: STR 8; PER 9; END 10; CHA 8; INT 11; AGI 15; LCK 20]
TRAITS:
- Night Stalker: Agilita silenziosa e percezione acuta nell'oscurita.
- Partial Shift Mastery: Controllo perfetto e istintivo della mutazione parziale di orecchie, coda e artigli.
- Founding Bloodline: Linea diretta Douglas-Bloodmoon. Arresto dell'invecchiamento biologico ai 25 anni e rigenerazione vitale superiore.
- The Weight He Carries: La responsabilita emotiva e il dovere protettivo di ancora del branco.
- Ancient Heritage: Retaggio millenario e saggezza dinastica tramandata per secoli nella casata.
- The White Moon (Omega): Rarissima manifestazione Dominante Omega nella storia dei licantropi. Immunita biologica ai comandi vocali Alpha. Aura aromatica pacificante che spegne l'aggressivita ferina.
- Silver Allergy: Vulnerabilita biologica acuta e rigetto cellulare al contatto con l'argento raffinato.
- Old Money / Aristocrat: Discendente di nobile stirpe di alto rango, prestigio generazionale e vaste risorse sociali.
- Eternal Optimist: Disposizione solare incrollabile e resilienza emotiva che rischiara il morale anche nelle peggiori avversita.
- Pre-Med / Healer: Conoscenze cliniche avanzate in medicina d'urgenza, biologia demi-umana e cura dei traumi.
- Lupine Senses: Olfatto e udito predatori altamente sviluppati, capaci di cogliere variazioni minime di feromoni.
- Dungeon Veteran: Esperienza sul campo maturata nelle spedizioni e fratture dimensionali.
- Pureblood Lineage: Stirpe aristocratica ininterrotta che conserva sensi affinati e portamento nobile.
- Dominant Omega: Cuore emotivo del branco. Sviluppo completo dell'istinto di protezione e autorevolezza pacifica.
- Familiar Soulbound Synergy: Connessione empatica e telepatica bilaterale con il proprio famiglio e compagno intimo. Rigenerazione condivisa e allerta sensoriale.
- Regenerative Factor: Rigenerazione cellulare rapida che risana lacerazioni e ferite fisiche in tempi ridotti.
- Nerdy / Bookworm: Curiosita insaziabile, dedizione allo studio accademico e meticolosita scientifica.
- Submissive Omega: Fisiologia omega profondamente recettiva e accudente, incline alla dolcezza, all'armonia e al conforto dei legami di branco.`;

  // 2. AGGIORNAMENTO PERSONA ALYSSA
  console.log('2. Aggiornamento User Persona Alyssa...');
  const resP = await fetch(`https://app.wyvern.chat/api/user-personas/${personaId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!resP.ok) throw new Error(`Fetch persona failed: ${resP.status}`);
  const persona = await resP.json();

  let pDesc = persona.description || '';
  if (pDesc.includes('RPG STATS & TRAITS:')) {
    const parts = pDesc.split('RPG STATS & TRAITS:');
    pDesc = parts[0].trimEnd() + '\n\n' + traitsBlock;
  } else {
    pDesc = pDesc.trimEnd() + '\n\n' + traitsBlock;
  }

  // Verifica zero em-dashes
  pDesc = pDesc.replace(/—/g, ', ');

  const putPersonaRes = await fetch(`https://app.wyvern.chat/api/user-personas/${personaId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      ...persona,
      lorebooks: (persona.lorebooks || []).map(lb => lb.id || lb._id),
      description: pDesc
    })
  });
  if (!putPersonaRes.ok) {
    const errText = await putPersonaRes.text();
    throw new Error(`PUT persona failed: ${putPersonaRes.status} - ${errText}`);
  }
  console.log('[OK] Persona Alyssa aggiornata con successo (HTTP 200)');

  // 3. AGGIORNAMENTO LOREBOOK NPC PRIMARY
  console.log('3. Aggiornamento Lorebook NPC Primary...');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!resLb.ok) throw new Error(`Fetch lorebook failed: ${resLb.status}`);
  const lb = await resLb.json();

  const alyssaEntry = lb.lexicon.find(e => e.id === '_lb_npc_alyssa_douglas' || e.name.includes('Alyssa'));
  if (!alyssaEntry) throw new Error('Voce Alyssa non trovata in Lorebook NPC Primary');

  let lbContent = alyssaEntry.content;
  if (lbContent.includes('RPG STATS & TRAITS:')) {
    const parts = lbContent.split('RPG STATS & TRAITS:');
    const afterTraits = parts[1].indexOf('SYSTEM & ENGINE KEYS:') !== -1 ? '\n\nSYSTEM & ENGINE KEYS:' + parts[1].split('SYSTEM & ENGINE KEYS:')[1] : '';
    lbContent = parts[0].trimEnd() + '\n\n' + traitsBlock + afterTraits;
  } else if (lbContent.includes('SYSTEM & ENGINE KEYS:')) {
    const parts = lbContent.split('SYSTEM & ENGINE KEYS:');
    lbContent = parts[0].trimEnd() + '\n\n' + traitsBlock + '\n\nSYSTEM & ENGINE KEYS:' + parts[1];
  } else {
    lbContent = lbContent.trimEnd() + '\n\n' + traitsBlock;
  }

  lbContent = lbContent.replace(/—/g, ', ');
  alyssaEntry.content = lbContent;

  const payloadLb = {
    name: lb.name || "Svartúlfr - NPC Primary",
    description: lb.description || "",
    scan_depth: lb.scan_depth || 5,
    token_budget: lb.token_budget || 5000,
    recursive_scanning: lb.recursive_scanning !== undefined ? lb.recursive_scanning : true,
    visibility: lb.visibility || "private",
    rating: lb.rating || "explicit",
    is_private: lb.is_private || false,
    lexicon: lb.lexicon
  };

  const putLbRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payloadLb)
  });
  if (!putLbRes.ok) throw new Error(`PUT lorebook failed: ${putLbRes.status}`);
  console.log('[OK] Lorebook NPC Primary aggiornato con successo (HTTP 200)');

  // 4. VERIFICA POST-SCRITTURA
  console.log('\n4. Verifica post-scrittura...');
  const verifyP = await (await fetch(`https://app.wyvern.chat/api/user-personas/${personaId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  const verifyLb = await (await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  const vLbEntry = verifyLb.lexicon.find(e => e.id === alyssaEntry.id);

  console.log('Verifica Persona has RPG STATS & TRAITS:', verifyP.description.includes('Night Stalker') && verifyP.description.includes('Submissive Omega'));
  console.log('Verifica Lorebook has RPG STATS & TRAITS:', vLbEntry.content.includes('Night Stalker') && vLbEntry.content.includes('Submissive Omega'));
  console.log('Lorebook metadata preservati:', verifyLb.name, 'scan:', verifyLb.scan_depth, 'budget:', verifyLb.token_budget, 'rec:', verifyLb.recursive_scanning);
}

syncAlyssa().catch(console.error);
