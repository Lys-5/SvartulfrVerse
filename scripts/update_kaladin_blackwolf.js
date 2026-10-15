const fs = require('fs');

async function updateKaladinBlackwolf() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const npcLbId = '_LBkRWNpPxpdn6dxYaDU2b';
  const lb1Id = '_xJUNQC3BBTAbJfRGfWnF1';
  const kalId = '_b7QqV43D8pU1tewx4qenY';

  console.log('=== UPDATING KALADIN CALL-SIGN TO BLACKWOLF ===');

  // 1. UPDATE KALADIN WORLD CHARACTER
  console.log('1. Fetching Kaladin World Character...');
  const resKalW = await fetch(`https://app.wyvern.chat/api/worlds/characters/${kalId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const kalW = await resKalW.json();
  let kalWLines = (kalW.long_summary || '').split('\n');

  kalWLines[0] = kalWLines[0]
    .replace('[NAME: Kaladin Nargathon;', '[NAME: Kaladin Blackwolf Nargathon; FIRST_NAME: Kaladin; MIDDLE_NAME: Blackwolf (Military Call-Sign & Project Prototype Designation); LAST_NAME: Nargathon;')
    .replace('FIRST_NAME: Kaladin; LAST_NAME: Nargathon; ', '')
    .replace(/WOLF_CODENAME:\s*Six[^;]+;/i, 'WOLF_CODENAME: Blackwolf (Military Call-Sign / Subject Zero - First subject to undergo genetic experimentation, whose call-sign designated Project Blackwolf, Vanguard-Actual);')
    .replace(/MILITARY_BACKGROUND:\s*Raised by the Armed Forces[^;]+;/i, 'MILITARY_BACKGROUND: Raised by the Armed Forces, first experimental subject whose call-sign designated Project Blackwolf;')
    .replace(/ALIASES:\s*Commander,\s*Kal,\s*Six,\s*Lycan;/i, 'ALIASES: Commander, Kal, Blackwolf, Lycan, Subject Zero;');

  let kalSummary = kalWLines.join('\n');
  kalSummary = kalSummary.replace(
    'PROJECT BLACKWOLF: classified genetic-enhancement program run on Gamma-7',
    'PROJECT BLACKWOLF: classified genetic-enhancement program named after Kaladin\'s call-sign ("Blackwolf"), as he was the very first subject to undergo the experimental procedures, run on Gamma-7'
  );

  const putKalW = await fetch(`https://app.wyvern.chat/api/worlds/characters/${kalId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      display_name: 'Kaladin Nargathon',
      first_name: 'Kaladin',
      middle_names: ['Blackwolf'],
      last_name: 'Nargathon',
      long_summary: kalSummary
    })
  });
  console.log(' -> Kaladin World PUT status:', putKalW.status);

  // 2. UPDATE KALADIN IN NPC PRIMARY LOREBOOK
  console.log('2. Fetching NPC Primary Lorebook...');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lbData = await resLb.json();
  const updatedLex = lbData.lexicon.map(e => {
    if (e.name === 'Kaladin Nargathon' || (e.name && e.name.includes('Kaladin'))) {
      return {
        ...e,
        name: 'Kaladin Nargathon',
        keys: ['Kaladin', 'Blackwolf', 'BlackWolf', 'Kaladin Nargathon', 'Commander Kaladin', 'DCC Security', 'Subject Zero'],
        content: kalSummary
      };
    }
    return e;
  });

  const putLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ lexicon: updatedLex })
  });
  console.log(' -> NPC Primary Lorebook PUT status:', putLb.status);

  // 3. UPDATE WORLD LEXICON (Lycanthrope Naming Tradition)
  console.log('3. Updating World Lexicon Lycanthrope Naming Tradition...');
  const resLex = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/_q136ajAq8qR3EkNeYhR2C`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lexData = await resLex.json();
  let updatedLexContent = lexData.content.replace(
    /5\. I Licantropi Militari[^\n]+/g,
    '5. I Licantropi Militari (Nargathon e Project Blackwolf): I lupi cresciuti ed addestrati all\'interno delle gerarchie militari e dei battaglioni d\'assalto (come Kaladin Nargathon e Marcus Thornfield) sostituiscono il nome lupino tradizionale con codici tattici e call-sign operativi. Kaladin fu il primo soggetto in assoluto a venire sottoposto alle sperimentazioni genetiche dell\'esercito, assumendo il call-sign "Blackwolf" che diede il nome all\'intero programma segreto Project Blackwolf (mentre Marcus porta il call-sign operativo "Iron").'
  );

  const putLex = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/_q136ajAq8qR3EkNeYhR2C`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ content: updatedLexContent })
  });
  console.log(' -> World Lexicon PUT status:', putLex.status);

  // 4. UPDATE LOREBOOK I (Lycanthrope Naming Tradition)
  console.log('4. Updating Lorebook I Lycanthrope Naming Tradition...');
  const resLb1 = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb1Id}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lb1Data = await resLb1.json();
  const updatedLb1Lex = lb1Data.lexicon.map(e => {
    if (e.name === 'Lycanthrope Naming Tradition' || e.title === 'Lycanthrope Naming Tradition') {
      return { ...e, content: updatedLexContent };
    }
    return e;
  });

  const putLb1 = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb1Id}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ lexicon: updatedLb1Lex })
  });
  console.log(' -> Lorebook I PUT status:', putLb1.status);

  console.log('=== ALL KALADIN UPDATES COMPLETED SUCCESSFULLY ===');
}

updateKaladinBlackwolf().catch(err => {
  console.error('Error during update:', err);
  process.exit(1);
});
