const fs = require('fs');

async function syncLorebookAndEngine() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldData = JSON.parse(fs.readFileSync('exports/Svartulfr_Export.json', 'utf8'));
  const worldLex = worldData.world_lexicon_entries || [];

  console.log('=== 1. AGGIORNAMENTO SVARTÚLFR - LOREBOOK IN /mine ===');
  const lbId = '_J8x7fwRrpa9C6Wct6hb7p';
  const lbRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const lbData = await lbRes.json();
  const currentEntries = lbData.lexicon || [];
  const currentTitles = new Set(currentEntries.map(e => (e.title || e.name || (e.keys && e.keys[0]) || '').toLowerCase().trim()));

  const missingEntries = [];
  worldLex.forEach(w => {
    if (w.type === 'npc') return;
    const title = (w.name || w.title || (w.keys && w.keys[0]) || '').trim();
    if (!title) return;
    if (!currentTitles.has(title.toLowerCase())) {
      missingEntries.push({
        title: title,
        keys: w.keys || [title],
        key_logic: w.key_logic || 'AND_ANY',
        content: (w.content || '').replace(/—/g, ', '),
        enabled: true,
        is_global: w.is_global !== false
      });
      currentTitles.add(title.toLowerCase());
    }
  });

  console.log(`Voci attuali in Lorebook: ${currentEntries.length}`);
  console.log(`Nuove voci da aggiungere dal World: ${missingEntries.length}`);

  const updatedLexicon = [...currentEntries, ...missingEntries];
  const putLbRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lbId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: lbData.name,
      description: lbData.description,
      photoURL: lbData.photoURL,
      lexicon: updatedLexicon
    })
  });
  console.log('Svartúlfr - Lorebook PUT status:', putLbRes.status);
  if (!putLbRes.ok) console.log(await putLbRes.text());
  else console.log(`Lorebook aggiornato con successo a ${updatedLexicon.length} voci!`);

  console.log('\n=== 2. AGGIORNAMENTO STORY ENGINE SVARTULFR OS IN /mine ===');
  const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';
  const getEng = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const engData = await getEng.json();
  const def = engData.definition || {};

  // Collegamento del World e dei Lorebooks
  const updatedWorlds = ['_CgYT8fHXpDC4crjmegQF7'];
  const updatedLorebooks = [
    '_xZkWyqB9z1C3QMQp71kXh', // Core & Setting
    '_kPzhnGxaRgCMdmgrwWjbY', // NPC Primary
    '_J8x7fwRrpa9C6Wct6hb7p', // Svartulfr - Lorebook
    '_V6jT3gPWDCPdxT2bCedeG'  // Svartulfr - Location
  ];

  const updatedPromptTemplate = def.prompt_template + `

=== ESPANSIONI CANONICHE: CLASSI SPECIALI, CYBERSPAZIO & CAMP MYSTIC ===
- Malachia Douglas (Guild Berserker): Dotato della Fornace Interna (metabolismo termico ad accelerazione metabolica e consumo di ferro). In battaglia o in caccia nei Rift, emana calore fumante e ignora il dolore fino all'esaurimento della frenesia.
- Jasper Douglas (Technomancer) & Echo (Digital Familiar): Jasper opera come Tecnomanzonte della Villa, collegando incantesimi runici a fibra ottica e server DCC. Echo e la sua intelligenza artificiale senziente / famiglio digitale, sempre connessa ai display, con tono deadpan e la funzione Music Mood Speaker per le scene di tensione o comiche.
- Angelo Moreno (Puppet Master): Maestro dei fili di mana psichici e simulacri, capace di muovere bambole tattiche e legare la mente degli avversari nel suo labirinto onirico.
- Camp Mystic (Lago Erie): Riserva estiva per studenti e facolta del SUCC con chalet fortificati, barriere antimostro e addestramento sulle acque lacustri per le vacanze universitarie.`;

  const updatedDef = {
    ...def,
    worlds: updatedWorlds,
    lorebooks: updatedLorebooks,
    prompt_template: updatedPromptTemplate
  };

  const putEngRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: engData.name,
      tagline: engData.tagline,
      description: engData.description,
      avatar: engData.avatar,
      tags: engData.tags,
      rating: engData.rating,
      visibility: engData.visibility,
      status: engData.status,
      definition: updatedDef
    })
  });
  console.log('StoryEngine PUT status:', putEngRes.status);
  if (!putEngRes.ok) console.log(await putEngRes.text());
  else console.log('StoryEngine Svartulfr OS aggiornato e collegato al World!');
}

syncLorebookAndEngine();
