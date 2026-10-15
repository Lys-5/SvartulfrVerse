const fs = require('fs');

async function updateElders() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const npcLbId = '_LBkRWNpPxpdn6dxYaDU2b';
  const magnusId = '_jeJTbxLcrYWXNWYPDx4ph';
  const corneliusId = '_rJKYcCt61hQa8XRamHEdM';

  console.log('=== FASE 2: FORMALIZZAZIONE BIRTH-RUNES ANZIANI DI CASA DOUGLAS ===\n');

  // 1. UPDATE MAGNUS DOUGLAS III (WORLD)
  console.log('1. Aggiornamento Magnus Douglas III (World)...');
  const resMagW = await fetch(`https://app.wyvern.chat/api/worlds/characters/${magnusId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const magW = await resMagW.json();
  let magLines = (magW.long_summary || '').split('\n');
  magLines[0] = magLines[0].replace(
    '[NAME: Magnus Douglas III;',
    '[NAME: Magnus Douglas III; FIRST_NAME: Magnus; LAST_NAME: Douglas; BIRTH_RUNE: Othala (Ancestral Heritage & Dynastic Sovereignty, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);'
  );
  const putMagW = await fetch(`https://app.wyvern.chat/api/worlds/characters/${magnusId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      display_name: 'Magnus Douglas III',
      first_name: 'Magnus',
      last_name: 'Douglas',
      long_summary: magLines.join('\n')
    })
  });
  console.log(`   Esito World PUT: HTTP ${putMagW.status}`);

  // 2. UPDATE LORD CORNELIUS DOUGLAS (WORLD)
  console.log('2. Aggiornamento Lord Cornelius Douglas (World)...');
  const resCornW = await fetch(`https://app.wyvern.chat/api/worlds/characters/${corneliusId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const cornW = await resCornW.json();
  let cornLines = (cornW.long_summary || '').split('\n');
  cornLines[0] = cornLines[0].replace(
    '[NAME: Lord Cornelius Douglas;',
    '[NAME: Lord Cornelius Douglas; FIRST_NAME: Cornelius; LAST_NAME: Douglas; BIRTH_RUNE: Othala (Dynasty Founding & Ancestral Bloodline, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);'
  );
  const putCornW = await fetch(`https://app.wyvern.chat/api/worlds/characters/${corneliusId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      display_name: 'Lord Cornelius Douglas',
      first_name: 'Cornelius',
      last_name: 'Douglas',
      long_summary: cornLines.join('\n')
    })
  });
  console.log(`   Esito World PUT: HTTP ${putCornW.status}`);

  // 3. UPDATE NPC PRIMARY LOREBOOK
  console.log('3. Aggiornamento Lorebook NPC Primary...');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lbData = await resLb.json();
  const updatedLex = lbData.lexicon.map(e => {
    if (e.name === 'Magnus Douglas III' || (e.name && e.name.includes('Magnus Douglas'))) {
      const lines = (e.content || '').split('\n');
      lines[0] = lines[0].replace(
        '[NAME: Magnus Douglas III;',
        '[NAME: Magnus Douglas III; FIRST_NAME: Magnus; LAST_NAME: Douglas; BIRTH_RUNE: Othala (Ancestral Heritage & Dynastic Sovereignty, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);'
      );
      return {
        ...e,
        name: 'Magnus Douglas III',
        keys: ['Magnus', 'Magnus Douglas', 'Sir Magnus', 'Patriarch Magnus'],
        content: lines.join('\n')
      };
    }
    if (e.name === 'Lord Cornelius Douglas' || (e.name && e.name.includes('Cornelius Douglas'))) {
      const lines = (e.content || '').split('\n');
      lines[0] = lines[0].replace(
        '[NAME: Lord Cornelius Douglas;',
        '[NAME: Lord Cornelius Douglas; FIRST_NAME: Cornelius; LAST_NAME: Douglas; BIRTH_RUNE: Othala (Dynasty Founding & Ancestral Bloodline, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);'
      );
      return {
        ...e,
        name: 'Lord Cornelius Douglas',
        keys: ['Cornelius', 'Lord Cornelius', 'Cornelius Douglas', 'Governor Cornelius'],
        content: lines.join('\n')
      };
    }
    return e;
  });

  const putLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ lexicon: updatedLex })
  });
  console.log(`   Esito Lorebook PUT: HTTP ${putLb.status}`);

  console.log('\n=== FASE 2 COMPLETATA CON SUCCESSO ===');
}

updateElders().catch(err => {
  console.error('Fatal error in updateElders:', err);
  process.exit(1);
});
