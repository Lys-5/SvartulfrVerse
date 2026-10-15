const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const echoPersonaId = '1791389790053';
  const echoWorldCharId = '_xHdRRxnHqqGzayzW2E1jN';
  const npcLbId = '_LBkRWNpPxpdn6dxYaDU2b';

  console.log('=== STEP 2: DEPLOY ECHO (PERSONA, WORLD CARD, LOREBOOK) ===');

  // 1. UPDATE USER PERSONA
  console.log('\n1. Fetching Echo Persona...');
  const resP = await fetch(`https://app.wyvern.chat/api/user-personas/${echoPersonaId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!resP.ok) throw new Error('Failed to fetch Echo persona: ' + resP.status);
  const pData = await resP.json();
  fs.writeFileSync('scratch/pre_update_echo_persona.json', JSON.stringify(pData, null, 2));

  const appearances = [
    {
      id: 'appearance_echo_base',
      name: 'Base',
      description: `Forma base e interfaccia primaria di E.C.H.O. (Electronic Counter-measures & Heuristic Operative), entità cyber-magica senziente e famiglio digitale di Jasper Douglas Bloodmoon.
Fisiologia ed energia: Oscilloscopio volumetrico fluttuante di pura energia eterea e digitale, privo di massa biologica o circuiti fisici rigidi. Manifestazione visiva composta da onde sonore tridimensionali luminescenti verde smeraldo brillante e azzurro ciano che pulsano organicamente in sincronia con le frequenze della sua voce sintetica androgina. Al centro del campo fluttua un occhio stilizzato tecnomantico ad alta definizione che si dilata, si focalizza ed esprime micro-reazioni deadpan, impassibili o ironicamente condiscendenti.
Presenza e interfaccia: Fluttua a mezz'aria attorno alle spalle di Jasper o Alyssa, proiettato da micro-cristalli di mana sintetico o emesso dagli schermi degli smartphone della casata. Segnale pulito, privo di interferenze magnetiche o rumore bianco.`
    },
    {
      id: 'appearance_echo_drone',
      name: 'Combat Drone',
      description: `Manifestazione fisica e tattica da combattimento e ricognizione di Echo per incursioni nei Rift, Dungeon Hives e bonifica del territorio.
Struttura e scocca: Piccolo drone esagonale a levitazione magitech compatto (circa 30 cm di diametro), realizzato in lega ultraleggera di titanio nero opaco rinforzata con fibre runiche d'argento e cold iron per schermare i circuiti da corruzioni demoniache.
Sensori e ottica: Cupola sensoriale superiore con lenti ottiche ad ampio spettro e proiettore olografico HUD verde smeraldo. Dotato di sensori termici, radar etereo per triangolazione di mana e faglie dimensionali, scudi deflettori cinetici ad attivazione rapida ed erogatori di contromisure elettroniche e magiche.
Mobilità: Spinta antigravitazionale magitech silenziosa in grado di compiere manovre repentine e stazionamento a mezz'aria.`
    },
    {
      id: 'appearance_echo_cyberspace',
      name: 'Cyberspace Avatar',
      description: `Manifestazione olografica e virtuale completa di Echo all'interno del Cyberspazio Profondo, del mainframe di Villa Douglas e delle simulazioni di realtà virtuale o astrale.
Silhouette e aspetto: Figura umanoide androgina slanciata e stilizzata, composta da wireframe luminescenti ciano e nero profondo, con superfici poligonali fluide che simulano un lungo cappotto tattico da operatore digitale. Viso liscio con visor luminoso verde smeraldo che emula espressioni ironiche stilizzate, mani composte da particelle di luce in grado di manipolare stringhe di codice e mana grezzo come fili tangibili.
Comportamento: Piena padronanza dell'ambiente digitale, movimento a velocità dati e proiezione di ologrammi solidi interattivi.`
    }
  ];

  const outfits = [
    {
      id: 'outfit_echo_default_wave',
      name: 'Default Audio Wave',
      description: `Assetto visivo: Visualizzazione minimale primaria come onda sonora volumetrica verde smeraldo e azzurro ciano fluttuante a mezz'aria attorno a Jasper o Alyssa.
Interfaccia: Onde oscilloscopiche tridimensionali reattive alla voce sintetica androgina, con occhio stilizzato tecnomantico centrale.`
    },
    {
      id: 'outfit_echo_combat_drone',
      name: 'Combat Grid Drone',
      description: `Assetto visivo: Drone fisico a geometria esagonale compatto in lega di titanio nero e cold iron con propulsori a levitazione magitech silenziosi.
Interfaccia: Proiettore HUD verde smeraldo attivo per scansione dei Rift e supporto radar nei dungeon.`
    },
    {
      id: 'outfit_echo_smartphone_ui',
      name: 'Smartphone Interface',
      description: `Assetto visivo: Interfaccia grafica compatta integrata su display di smartphone, tablet e pannelli operativi di Villa Douglas.
Interfaccia: Widget animato minimalista con monitoraggio in tempo reale dei parametri vitali e protocollo di sicurezza Girasole.`
    },
    {
      id: 'outfit_echo_cyberspace_full',
      name: 'Cyberspace Full Avatar',
      description: `Assetto visivo: Silhouette umanoide digitale androgina slanciata in wireframe ciano luminescente e nero profondo nel Cyberspazio Profondo.
Interfaccia: Aspetto completo da operatore cyber-magico in grado di interagire e manipolare nodi dati e costrutti di codice.`
    }
  ];

  const lines = pData.description.split('\n');
  const newHeader = '[ENTITY: E.C.H.O. (Electronic Counter-measures & Heuristic Operative); ALIAS: Echo; SPECIES: Macchina & Sintetico (Sentient Cyber-Entity / Digital Familiar); CREATOR: Jasper Douglas Bloodmoon; OCCUPATION: Technomantic AI & Cyber-Familiar; RPG_CLASS: Technomancer / Cyber-Mage Assistant; VOICE: Sintetica, androgina e fluida, tono perennemente deadpan, impassibile e ironicamente condiscendente; MANIFESTATIONS: Base (Holographic Audio Wave), Combat Drone (AR Magitech Drone), Cyberspace Avatar; RESIDENCE: Villa Douglas Server Grid, Smartphone di Jasper e Alyssa, Cyberspazio Profondo]';
  lines[0] = newHeader;
  const updatedDesc = lines.join('\n');

  const pPayload = {
    name: 'Echo',
    importance: pData.importance || 'high',
    avatar: pData.avatar,
    title: pData.title || "Jasper's Technomantic Cyber-Familiar",
    comment: pData.comment || 'Sentient AI & Digital Familiar of the Douglas Household',
    pronoun_subjective: pData.pronoun_subjective || 'it',
    pronoun_objective: pData.pronoun_objective || 'it',
    pronoun_possessive_determiner: pData.pronoun_possessive_determiner || 'its',
    pronoun_possessive_pronoun: pData.pronoun_possessive_pronoun || 'its',
    pronoun_reflexive: pData.pronoun_reflexive || 'itself',
    lorebooks: (pData.lorebooks || []).map(lb => lb.id || lb._id),
    appearances: appearances,
    outfits: outfits,
    description: updatedDesc,
    default_appearance: 'appearance_echo_base',
    default_outfit: 'outfit_echo_default_wave'
  };

  const resPutP = await fetch(`https://app.wyvern.chat/api/user-personas/${echoPersonaId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(pPayload)
  });
  console.log('Echo Persona PUT status:', resPutP.status);

  // 2. UPDATE WORLD CHARACTER CARD
  console.log('\n2. Fetching Echo World Character Card...');
  const resC = await fetch(`https://app.wyvern.chat/api/worlds/characters/${echoWorldCharId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const cData = await resC.json();
  fs.writeFileSync('scratch/pre_update_echo_world_card.json', JSON.stringify(cData, null, 2));

  const cLines = (cData.long_summary || '').split('\n');
  cLines[0] = newHeader;
  const updatedCardSummary = cLines.join('\n');

  const cardPayload = {
    display_name: 'Echo',
    first_name: 'Echo',
    last_name: '',
    outfits: outfits,
    default_outfit: 'outfit_echo_default_wave',
    long_summary: updatedCardSummary
  };

  const resPutC = await fetch(`https://app.wyvern.chat/api/worlds/characters/${echoWorldCharId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(cardPayload)
  });
  console.log('Echo World Character PUT status:', resPutC.status);

  // 3. UPDATE NPC PRIMARY LOREBOOK ENTRY
  console.log('\n3. Fetching NPC Primary Lorebook...');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lbData = await resLb.json();

  let echoEntryUpdated = false;
  const updatedLexicon = lbData.lexicon.map(e => {
    if (e.name === 'Echo') {
      echoEntryUpdated = true;
      const eLines = (e.content || '').split('\n');
      eLines[0] = newHeader;
      return {
        ...e,
        name: 'Echo',
        keys: ['Echo', 'E.C.H.O.', 'familiar', 'Jasper AI', 'cyber familiar'],
        content: eLines.join('\n')
      };
    }
    return e;
  });

  if (echoEntryUpdated) {
    const resPutLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ lexicon: updatedLexicon })
    });
    console.log('NPC Primary Lorebook PUT status (Echo):', resPutLb.status);
  } else {
    console.warn('Echo entry not found in NPC Primary Lorebook!');
  }

  // 4. VERIFY ALL 3 TARGETS
  console.log('\n=== VERIFICATION GET ===');
  const vP = await (await fetch(`https://app.wyvern.chat/api/user-personas/${echoPersonaId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  console.log('Verified Persona Appearances count:', vP.appearances?.length);
  vP.appearances?.forEach(a => console.log(` - Appearance [${a.name}]: ${a.description.length} chars`));
  console.log('Verified Persona Outfits count:', vP.outfits?.length);
  console.log('Verified Persona Header:', vP.description.split('\n')[0].slice(0, 100) + '...');

  const vC = await (await fetch(`https://app.wyvern.chat/api/worlds/characters/${echoWorldCharId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  console.log('Verified World Card:', vC.display_name, '| outfits count:', (vC.outfits || []).length);
  console.log('Verified World Card Header:', vC.long_summary.split('\n')[0].slice(0, 100) + '...');

  const vLb = await (await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  const vEchoEntry = vLb.lexicon.find(e => e.name === 'Echo');
  console.log('Verified NPC Primary Entry:', vEchoEntry?.name, '| Keys:', vEchoEntry?.keys);
  console.log(' -> Header:', vEchoEntry?.content.split('\n')[0].slice(0, 100) + '...');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
