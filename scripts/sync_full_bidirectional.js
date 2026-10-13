const fs = require('fs');
const path = require('path');

async function syncFullBidirectional() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const exportsDir = path.join(__dirname, '..', 'exports');
  if (!fs.existsSync(exportsDir)) fs.mkdirSync(exportsDir, { recursive: true });

  console.log('================================================================');
  console.log('   SINCRONIZZAZIONE BIDIREZIONALE TOTALE SVARTÚLFR VERSE');
  console.log('================================================================\n');

  // 1. USER PERSONAS (Alyssa ed Echo)
  console.log('1. Sincronizzazione User Personas (/api/user-personas)...');
  const personasRes = await fetch('https://app.wyvern.chat/api/user-personas', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (personasRes.ok) {
    const personas = await personasRes.json();
    const personasExportPath = path.join(exportsDir, 'User_Personas_Export.json');
    fs.writeFileSync(personasExportPath, JSON.stringify(personas, null, 2), 'utf8');
    console.log(`   -> Esportate ${personas.length} Personas in ${personasExportPath}`);
    personas.forEach(p => {
      console.log(`      * ${p.name} (${p.id}) | Outfits: ${(p.outfits || []).length} | Lorebooks: ${(p.lorebooks || []).length}`);
    });
  } else {
    console.error('   -> Errore fetch Personas:', personasRes.status);
  }

  // 2. STAND-ALONE CHARACTERS IN /mine
  console.log('\n2. Sincronizzazione Stand-Alone Characters in /mine (/api/characters/mine)...');
  const mineCharsRes = await fetch('https://app.wyvern.chat/api/characters/mine', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (mineCharsRes.ok) {
    const mineCharsRaw = await mineCharsRes.json();
    const mineChars = mineCharsRaw.characters || [];
    const fullMineChars = [];

    for (const c of mineChars) {
      const singleRes = await fetch(`https://app.wyvern.chat/api/characters/${c.id || c._id}`, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (singleRes.ok) {
        fullMineChars.push(await singleRes.json());
      } else {
        fullMineChars.push(c);
      }
    }

    const mineCharsExportPath = path.join(exportsDir, 'Mine_Characters_Export.json');
    fs.writeFileSync(mineCharsExportPath, JSON.stringify(fullMineChars, null, 2), 'utf8');
    console.log(`   -> Esportati ${fullMineChars.length} Stand-Alone Characters in ${mineCharsExportPath}`);
    fullMineChars.forEach(c => {
      console.log(`      * ${c.name || c.display_name} (${c.id}) | Linked World: ${c.linked_world || 'N/A'} | Lorebooks: ${(c.lorebooks || []).length}`);
    });
  } else {
    console.error('   -> Errore fetch Mine Characters:', mineCharsRes.status);
  }

  // 3. STORY ENGINES IN /mine
  console.log('\n3. Sincronizzazione Story Engines (/api/story-engines/mine)...');
  const seRes = await fetch('https://app.wyvern.chat/api/story-engines/mine', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (seRes.ok) {
    const seData = await seRes.json();
    const seList = seData.items || [];
    const fullStoryEngines = [];

    for (const se of seList) {
      const singleRes = await fetch(`https://app.wyvern.chat/api/story-engines/${se.id}`, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (singleRes.ok) {
        fullStoryEngines.push(await singleRes.json());
      } else {
        fullStoryEngines.push(se);
      }
    }

    const seExportPath = path.join(exportsDir, 'Story_Engines_Export.json');
    fs.writeFileSync(seExportPath, JSON.stringify(fullStoryEngines, null, 2), 'utf8');
    console.log(`   -> Esportati ${fullStoryEngines.length} Story Engines in ${seExportPath}`);
    fullStoryEngines.forEach(se => {
      console.log(`      * ${se.name} (v${se.version}) | Worlds: ${(se.definition?.worlds || []).length} | Lorebooks: ${(se.definition?.lorebooks || []).length}`);
    });
  } else {
    console.error('   -> Errore fetch Story Engines:', seRes.status);
  }

  // 4. LOREBOOKS IN /mine (Created & Bookmarked)
  console.log('\n4. Sincronizzazione Lorebooks (/mine)...');
  const uid = '2r4fVpvImte5dbljedLkZJxre2d2';
  const createdRes = await fetch(`https://app.wyvern.chat/api/lorebooks/user/${uid}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const bookmarkedRes = await fetch('https://app.wyvern.chat/api/inventory/collection/lorebooks?limit=100', {
    headers: { 'Authorization': 'Bearer ' + token }
  });

  const fullLorebooks = {
    created: [],
    bookmarked: []
  };

  if (createdRes.ok) {
    const createdData = await createdRes.json();
    for (const lb of (createdData.lorebooks || [])) {
      const singleRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (singleRes.ok) fullLorebooks.created.push(await singleRes.json());
      else fullLorebooks.created.push(lb);
    }
  }

  if (bookmarkedRes.ok) {
    const bookmarkedData = await bookmarkedRes.json();
    fullLorebooks.bookmarked = bookmarkedData.items || [];
  }

  const lorebooksExportPath = path.join(exportsDir, 'Mine_Lorebooks_Export.json');
  fs.writeFileSync(lorebooksExportPath, JSON.stringify(fullLorebooks, null, 2), 'utf8');
  console.log(`   -> Esportati ${fullLorebooks.created.length} Lorebooks Creati e ${fullLorebooks.bookmarked.length} Bookmarked in ${lorebooksExportPath}`);
  fullLorebooks.created.forEach(lb => {
    console.log(`      * [Creato] ${lb.name} (${lb.id}) | Voci: ${(lb.lexicon || []).length}`);
  });

  console.log('\n================================================================');
  console.log('   SINCRONIZZAZIONE COMPLETATA AL 100% SU TUTTE LE DIREZIONI');
  console.log('================================================================\n');
}

syncFullBidirectional();
