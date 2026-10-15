const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const npcLbId = '_LBkRWNpPxpdn6dxYaDU2b';
  const lb1Id = '_xJUNQC3BBTAbJfRGfWnF1';

  console.log('=== STEP 5: DEPLOY ALLIED, CLAN & MILITARY LORE REFINEMENTS ===');

  // 1. UPDATE LOGAN DOUGLAS (WORLD, /mine, LOREBOOK)
  console.log('\n1. Updating Logan Douglas...');
  // World
  const resLoganW = await fetch(`https://app.wyvern.chat/api/worlds/characters/_JL37wK9PQMNDChULCDrWj`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const loganW = await resLoganW.json();
  const loganWLines = (loganW.long_summary || '').split('\n');
  loganWLines[0] = loganWLines[0].replace('[NAME: Logan Dominic Douglas;', '[NAME: Logan Járn Douglas; FIRST_NAME: Logan; MIDDLE_NAME: Dominic (Civil Nobility), Járn (Wolf Name, Presentation at 13); LAST_NAME: Douglas; BIRTH_RUNE: Eihwaz (Resilience & The World Tree, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
  await fetch(`https://app.wyvern.chat/api/worlds/characters/_JL37wK9PQMNDChULCDrWj`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      display_name: 'Logan Járn Douglas',
      first_name: 'Logan',
      middle_names: ['Dominic', 'Járn'],
      last_name: 'Douglas',
      long_summary: loganWLines.join('\n')
    })
  });
  console.log(' -> Logan World Character updated.');

  // /mine standalone
  const resLoganMine = await fetch(`https://app.wyvern.chat/api/characters/_BQ4THBW3BKL2RN9Xy4YHb`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (resLoganMine.ok) {
    const loganMine = await resLoganMine.json();
    const lmLines = (loganMine.description || '').split('\n');
    lmLines[0] = lmLines[0].replace('[NAME: Logan Dominic Douglas;', '[NAME: Logan Járn Douglas; FIRST_NAME: Logan; MIDDLE_NAME: Dominic (Civil Nobility), Járn (Wolf Name, Presentation at 13); LAST_NAME: Douglas; BIRTH_RUNE: Eihwaz (Resilience & The World Tree, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
    await fetch(`https://app.wyvern.chat/api/characters/_BQ4THBW3BKL2RN9Xy4YHb`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: 'Logan Járn Douglas',
        description: lmLines.join('\n')
      })
    });
    console.log(' -> Logan /mine Standalone Card updated.');
  }

  // 2. UPDATE ELIZABETH DUSKWOOD (WORLD)
  console.log('\n2. Updating Elizabeth Duskwood in World...');
  const resEliz = await fetch(`https://app.wyvern.chat/api/worlds/characters/_EwPN1te7qtUKYEx4NLgag`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const eliz = await resEliz.json();
  const elizLines = (eliz.long_summary || '').split('\n');
  if (!elizLines[0].includes('BIRTH_RUNE')) {
    elizLines[0] = elizLines[0].replace('[NAME: Elizabeth Duskwood;', '[NAME: Elizabeth Duskwood; FIRST_NAME: Elizabeth; LAST_NAME: Duskwood; BIRTH_RUNE: Berkano (The Great Mother & Sanctuary Guardian, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
    await fetch(`https://app.wyvern.chat/api/worlds/characters/_EwPN1te7qtUKYEx4NLgag`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ long_summary: elizLines.join('\n') })
    });
    console.log(' -> Elizabeth Duskwood World Character updated.');
  }

  // 3. UPDATE KALADIN NARGATHON (WORLD)
  console.log('\n3. Updating Kaladin Nargathon in World...');
  const resKal = await fetch(`https://app.wyvern.chat/api/worlds/characters/_b7QqV43D8pU1tewx4qenY`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const kal = await resKal.json();
  const kalLines = (kal.long_summary || '').split('\n');
  if (!kalLines[0].includes('WOLF_CODENAME')) {
    kalLines[0] = kalLines[0].replace('[NAME: Kaladin Nargathon;', '[NAME: Kaladin Nargathon; FIRST_NAME: Kaladin; LAST_NAME: Nargathon; WOLF_CODENAME: Six (Military Call-Sign / Vanguard-Actual); MILITARY_BACKGROUND: Raised by the Armed Forces, wolf identity forged under tactical military codename nomenclature;');
    await fetch(`https://app.wyvern.chat/api/worlds/characters/_b7QqV43D8pU1tewx4qenY`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ long_summary: kalLines.join('\n') })
    });
    console.log(' -> Kaladin Nargathon World Character updated.');
  }

  // 4. UPDATE FINNEGAN NOVAK (WORLD)
  console.log('\n4. Updating Finnegan Novak in World...');
  const resFinn = await fetch(`https://app.wyvern.chat/api/worlds/characters/_PQHGb4gL2LwDhNDrLFa3A`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const finn = await resFinn.json();
  const finnLines = (finn.long_summary || '').split('\n');
  finnLines[0] = finnLines[0].replace('SPECIES: Arctic wolf demihuman;', 'SPECIES: Demi-Human Arctic Wolf (Kemonomimi, Non-Shifter, Bullied in childhood as "mezzo-lupo" due to inability to shift, zero werewolf birth-rune or wolf name);');
  await fetch(`https://app.wyvern.chat/api/worlds/characters/_PQHGb4gL2LwDhNDrLFa3A`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ long_summary: finnLines.join('\n') })
  });
  console.log(' -> Finnegan Novak World Character updated.');

  // 5. UPDATE NPC PRIMARY LOREBOOK ENTRIES
  console.log('\n5. Updating NPC Primary Lorebook for Logan, Elizabeth, Kaladin, Finn...');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lbData = await resLb.json();
  const updatedLex = lbData.lexicon.map(e => {
    if (e.name === 'Logan Douglas') {
      const lines = (e.content || '').split('\n');
      lines[0] = lines[0].replace('[NAME: Logan Dominic Douglas;', '[NAME: Logan Járn Douglas; FIRST_NAME: Logan; MIDDLE_NAME: Dominic (Civil Nobility), Járn (Wolf Name, Presentation at 13); LAST_NAME: Douglas; BIRTH_RUNE: Eihwaz (Resilience & The World Tree, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      return {
        ...e,
        name: 'Logan Járn Douglas',
        keys: ['Logan', 'Járn', 'Logan Járn', 'Logan Douglas', 'Uncle Logan'],
        content: lines.join('\n')
      };
    }
    if (e.name === 'Elizabeth Duskwood') {
      const lines = (e.content || '').split('\n');
      if (!lines[0].includes('BIRTH_RUNE')) {
        lines[0] = lines[0].replace('[NAME: Elizabeth Duskwood;', '[NAME: Elizabeth Duskwood; FIRST_NAME: Elizabeth; LAST_NAME: Duskwood; BIRTH_RUNE: Berkano (The Great Mother & Sanctuary Guardian, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
      return { ...e, content: lines.join('\n') };
    }
    if (e.name === 'Kaladin Nargathon') {
      const lines = (e.content || '').split('\n');
      if (!lines[0].includes('WOLF_CODENAME')) {
        lines[0] = lines[0].replace('[NAME: Kaladin Nargathon;', '[NAME: Kaladin Nargathon; FIRST_NAME: Kaladin; LAST_NAME: Nargathon; WOLF_CODENAME: Six (Military Call-Sign / Vanguard-Actual); MILITARY_BACKGROUND: Raised by the Armed Forces, wolf identity forged under tactical military codename nomenclature;');
      }
      return { ...e, content: lines.join('\n') };
    }
    if (e.name === 'Finnegan Novak') {
      const lines = (e.content || '').split('\n');
      lines[0] = lines[0].replace('SPECIES: Arctic wolf demihuman;', 'SPECIES: Demi-Human Arctic Wolf (Kemonomimi, Non-Shifter, Bullied in childhood as "mezzo-lupo" due to inability to shift, zero werewolf birth-rune or wolf name);');
      return { ...e, content: lines.join('\n') };
    }
    return e;
  });

  await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ lexicon: updatedLex })
  });
  console.log(' -> NPC Primary Lorebook updated successfully.');

  // 6. ENRICH LORE ENTRY IN WORLD LEXICON & LOREBOOK I
  console.log('\n6. Enriching Lore Entry "Lycanthrope Naming Tradition"...');
  const enrichedLoreContent = `Nella cultura dei licantropi norreni della Founding Bloodline e dell'antico lignaggio Svartulfr, ogni individuo riceve alla nascita un nome civile. All'eta di tredici anni, durante il sacro rito della Presentazione in cui si manifesta per la prima volta la bestia interiore, il licantropo scopre e dichiara il nome del proprio lupo spirituale. Per legge ancestrale del branco, questo nome viene assunto come secondo nome ufficiale e formale dell'individuo, sancendo la transizione verso l'eta adulta e l'accettazione del proprio spirito ferino.

I Pilastri Mitologici e Dinastici della Tradizione:
1. Il Mito Primordiale di Hvit e la Prima Compagna di Wulfnic: La prima Hvit delle origini nacque dall'unione mistica tra Mani (la divinita maschile della Luna) e Hati Hrodvitnisson (che nella cosmologia di Svartulfr e la sacra lupa primordiale). Questa prima lupa bianca divenne la prima compagna eterna di Wulfnic Bloodmoon, il capostipite creato da Fenris. Alla sua morte, la sua essenza lunare e il suo spirito protettivo si legano indissolubilmente al sangue Bloodmoon, reincarnandosi in ogni generazione attraverso le White Moon.
2. Il Vincolo delle White Moon: Tutte le reincarnazioni della lupa primordiale portano immancabilmente per legge sacra il nome del lupo originale: Hvit (la Bianca). Per questo motivo sia Nixara sia sua figlia Alyssa portano Hvit come secondo nome formale (Nixara Hvit Bloodmoon e Alyssa Hvit Douglas Bloodmoon), e per questo l'antico patriarca Wulfnic vede in Alyssa il riflesso vivente e benedetto della sua compagna perduta.
3. La Stirpe Solare di Svartr e Skoll: In simmetria perfetta e opposta ad Hvit, la controparte maschile dell'eclissi solare discende dall'unione tra Sol (la divinita femminile del Sole) e il lupo Skoll. Se Hvit incarna la pura luce lunare (Bianco), la progenie di Skoll assume il nome di Svartr (il Lupo Nero / l'Ombra Solare). Da questo archetipo millenario, Jasper Douglas assume alla sua Presentazione il nome di lupo Svartr (Jasper Svartr Douglas Bloodmoon), creando con la gemella Alyssa Hvit la perfetta polarita cosmica del branco.
4. I Secondi Nomi Nobiliari Inglesi vs Wolf Names Norreni: Nella Casa Douglas, a causa della tradizione nobiliare mercantile britannica stabilita dal patriarca Magnus dopo il 1666, ai primogeniti vengono spesso assegnati secondi nomi civili dell'aristocrazia inglese (come Cornelius per Erik e Dominic per Logan). Questi coesistono con i loro veri Wolf Names assunti alla Presentazione (Erik Ulfr e Logan Jarn).
5. I Licantropi Militari (Nargathon e Project Blackfang): I lupi cresciuti ed addestrati all'interno delle gerarchie militari e dei battaglioni d'assalto (come Kaladin Nargathon e Marcus Thornfield) sostituiscono il nome lupino tradizionale con codici tattici e call-sign operativi (es. Six / BlackWolf-Actual per Kaladin).
6. Distinzione Sacra tra Licantropi e Demi-Umani (Kemonomimi): La Presentazione, i Wolf Names e le Birth-Runes appartengono esclusivamente ai veri Licantropi dotati di facolta mutaforma (Shift). I Demi-Umani Lupo (come Finnegan Novak) sono Kemonomimi privi della capacita biologica di mutare in forma ibrida o quadrupede; nella societa conservatrice dei branchi antichi, questa differenza biologica li rendeva storicamente oggetto di disprezzo ed esclusione, etichettati brutalmente come "mezzi-lupi".
7. I Nove Firstblood: I nove guerrieri originali creati direttamente da Fenris (tra cui Wulfnic Bloodmoon) non possiedono un secondo nome separato. Essendo entita ancestrali unificate in cui uomo e lupo non sono mai stati divisi, il loro nome da lupo coincide identicamente con il loro nome vichingo di nascita.
8. I Giovani Pre-Presentazione: I cuccioli e i giovani licantropi che non hanno ancora compiuto tredici anni o non hanno ancora superato la cerimonia della Presentazione (come Edric Douglas) non possiedono un nome da lupo e usano unicamente il nome di battesimo civile.`;

  // Update in World Lexicon (_q136ajAq8qR3EkNeYhR2C)
  await fetch(`https://app.wyvern.chat/api/worlds/lexicon/_q136ajAq8qR3EkNeYhR2C`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ content: enrichedLoreContent })
  });
  console.log(' -> World Lexicon entry updated with full military, nobility & demi-human distinctions.');

  // Update in Lorebook I (_xJUNQC3BBTAbJfRGfWnF1)
  const resLb1 = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb1Id}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lb1Data = await resLb1.json();
  const updatedLb1Lex = lb1Data.lexicon.map(e => {
    if (e.name === 'Lycanthrope Naming Tradition' || e.title === 'Lycanthrope Naming Tradition') {
      return { ...e, content: enrichedLoreContent };
    }
    return e;
  });
  await fetch(`https://app.wyvern.chat/api/lorebooks/${lb1Id}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ lexicon: updatedLb1Lex })
  });
  console.log(' -> Lorebook I entry updated with full military, nobility & demi-human distinctions.');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
