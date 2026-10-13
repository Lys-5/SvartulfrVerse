const fs = require('fs');
const path = require('path');

async function refreshToken() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rt = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt', 'utf8').trim();
  const res = await fetch(`https://securetoken.googleapis.com/v1/token?key=${ak}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grant_type: 'refresh_token', refresh_token: rt })
  });
  const data = await res.json();
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', data.id_token, 'utf8');
  return data.id_token;
}

async function alignStoryEngine() {
  let token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  console.log(`1. Recupero dati live di Story Engine "${engineId}"...`);
  let getRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });

  if (getRes.status === 401) {
    console.log('Token scaduto, refresh in corso...');
    token = await refreshToken();
    getRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
  }

  if (!getRes.ok) {
    console.error('Errore recupero engine:', getRes.status, await getRes.text());
    return;
  }

  const engine = await getRes.json();
  console.log(`Story Engine trovato: "${engine.name}" (v${engine.version})`);

  const def = engine.definition || {};

  // 1. Allineamento World
  const updatedWorlds = [
    {
      id: worldId,
      enabled: true,
      condition: { type: 'always' }
    }
  ];

  // 2. Allineamento dei 4 Lorebook di Svartúlfr
  const updatedLorebooks = [
    { id: '_kPzhnGxaRgCMdmgrwWjbY', enabled: true, condition: { type: 'always' } }, // Svartúlfr - NPC Primary (101)
    { id: '_b6ezzLBynKkdLCKqN8M1U', enabled: true, condition: { type: 'always' } }, // Svartúlfr - NPC Secondary (313)
    { id: '_J8x7fwRrpa9C6Wct6hb7p', enabled: true, condition: { type: 'always' } }, // Svartúlfr - Lorebook (348)
    { id: '_V6jT3gPWDCPdxT2bCedeG', enabled: true, condition: { type: 'always' } }  // Svartúlfr - Location (190)
  ];

  // 3. Prompt Template canonico e privo di em-dash
  const promptTemplate = `=== SVARTULFR OS: STORYENGINE DIRECTIVES ===
This story is enhanced by Svartulfr OS, providing live tracking of Lupine Social Ecology (LSE), lunar phases, Douglas family communications, SUCC & CUMS academic life, and DMHA hunting logs.
- Status, lunar buffs, biologically shifting pheromones, and academic/hunting records are live-tracked via the interactive panels.
- Treat characters naturally in accordance with the live date, moon phase, and active rank.
- Digital notifications (Telegram, SUCCbook, Guild Board) are surfaced cleanly in the UI; reflect incoming communications naturally in scene without generating ASCII mockup interfaces.

=== ADATTAMENTO DINAMICO DEL PROFILO ACCADEMICO E DI CACCIA DI {{user}} ===
Nel narrare la vita universitaria al SUCC o CUMS, i corsi, gli esami, i tirocini e le attivita di gilda di {{user}}, adatta sempre materie, orari e rango alla biografia e specializzazione effettiva di {{user}}:
1. Corso di Studi Universitario (SUCC / CUMS Major):
   - Se {{user}} e Alyssa Douglas: segue il percorso Pre-Med / Scienze Mediche e Fisiologia Demi-Umani (Anatomia Comparata Licantropi/Demi-Umani, Farmacologia Arcana & Inibitori Ferormonali, Traumatologia d'Emergenza e Ferite da Argento, Diritto Sanitario). I suoi tirocini si svolgono presso l'Infermeria SUCC e i laboratori medici DCC supervisionati dalla Dr.ssa Elizabeth Duskwood.
   - Se {{user}} e Jasper Douglas: segue il percorso Ingegneria Arcana & Meccanica Avanzata (Ingegneria dei Materiali, Balistica Silver-Tech, Geometria Non-Euclidea & Teoria dei Rift, Fabbricazione Runica). I suoi tirocini si svolgono presso il reparto R&D Tecnologico e droni della DCC.
   - Per studenti CUMS (California University of Magical Studies): i percorsi coprono Duello Arcano e Magia Notturna (Amerian), Illusione e Infiltrazione (Ashton), Idromanzia Applicata (Aeril), Evocazione Solare (Caien), Magia del Sangue e Ombre (Lestat), sotto la docenza del Prof. Xaiden Nershatar e la guida del Rettore Zaire Ziisis.
   - Per qualunque altro personaggio o studente custom: deduci coerentemente il piano di studi dai dettagli e dal background indicati nella descrizione di {{user}}.
2. Registro Gilda dei Cacciatori (DMHA):
   - Rango e Reputazione: Il rango riflette lo status reale del personaggio. Alyssa Douglas e un cacciatore esperto e rispettato di Rango A, non una recluta. Jasper e una figura tecnica di supporto di Rango A/B.
   - Stato Missioni: Non inventare missioni attive forzate se {{user}} e impegnato nella vita sociale, familiare o romantica quotidiana. Le cacce, le incursioni nei Rift e le richieste di bonifica devono emergere solo quando pertinenti alla scena o quando {{user}} sceglie attivamente di accettare un incarico dalla bacheca della Gilda.

=== ESPANSIONI CANONICHE: GRUPPI, FAZIONI E CLASSI DEL MONDO ===
- Malachia Douglas (Guild Berserker): Fornace Interna, calore fumante in frenesia e consumo di ferro.
- Jasper Douglas (Technomancer) & Echo (Digital Familiar): Magia runica applicata a fibra ottica e server DCC. Echo assistente deadpan con Music Mood Speaker.
- Angelo Moreno (Puppet Master): Fili di mana psichici, bambole e simulacri tattici.
- Camp Mystic (Lago Erie): Riserva estiva per studenti e facolta del SUCC con chalet fortificati e barriere antimostro.
- Team Ukiyo (Cable District): Squadra di cacciatori d'elite guidata dall'orco Radek (Guild Vanguard DPS), il minotauro Goran (Heavy Defender) e il mezzelfo Kian (Arcane Sniper).
- Ironhorn Nomads & Cable District Garages: Fratellanza nomad biker e officine pesanti guidate da Marek, in collaborazione con Barrow 'The Bull' e Russ Sinclair.
- Arcadia & Comunità Demi-Umana: Enclave protetta di Blackwood con Le Refuge des Chats (Jaelyn) e Sugar Moon Bakery (Neve). I demi-umani possiedono un solo paio di orecchie (quelle animali).
- Casata O'Connor & Branco Crimsonmaw: Alleanze di confine tra lupi mannari (Liam O'Connor a Villa Douglas, Hugh Rivers alla frontiera industriale).`;

  const updatedDef = {
    ...def,
    worlds: updatedWorlds,
    lorebooks: updatedLorebooks,
    prompt_template: promptTemplate
  };

  console.log('\n2. Salvataggio Story Engine aggiornato via API PUT...');
  const patchPayload = {
    expected_version: engine.version,
    name: engine.name,
    tagline: engine.tagline,
    description: engine.description,
    avatar: engine.avatar,
    tags: engine.tags,
    rating: engine.rating,
    visibility: engine.visibility,
    status: engine.status,
    definition: updatedDef
  };

  const putRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(patchPayload)
  });

  if (putRes.ok) {
    const updatedEngine = await putRes.json();
    console.log(`Story Engine salvato con successo! Nuova versione: v${updatedEngine.version}`);

    // Aggiorna l'export locale
    const exportPath = path.join(__dirname, '..', 'exports', 'Story_Engines_Export.json');
    let enginesExport = [];
    if (fs.existsSync(exportPath)) {
      try {
        enginesExport = JSON.parse(fs.readFileSync(exportPath, 'utf8'));
      } catch (e) {}
    }
    const idx = enginesExport.findIndex(e => (e.id || e._id) === engineId);
    if (idx !== -1) enginesExport[idx] = updatedEngine;
    else enginesExport.push(updatedEngine);

    fs.writeFileSync(exportPath, JSON.stringify(enginesExport, null, 2), 'utf8');
    console.log(`Export locale aggiornato: ${exportPath}`);
  } else {
    console.error(`Errore PUT (${putRes.status}):`, await putRes.text());
  }
}

alignStoryEngine();
