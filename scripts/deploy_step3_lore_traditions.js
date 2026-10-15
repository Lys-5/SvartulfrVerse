const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const lb1Id = '_xJUNQC3BBTAbJfRGfWnF1'; // Svartulfr - Lorebook I

  console.log('=== STEP 3: DEPLOY LORE TRADITIONS (WORLD LEXICON & LOREBOOK I) ===');

  const tradition1 = {
    title: 'Lycanthrope Naming Tradition',
    name: 'Lycanthrope Naming Tradition',
    type: 'lore/concept',
    keys: ['werewolf naming', 'wolf name', 'middle name', 'presentation ceremony', 'hvit tradition', 'lycanthrope name', 'svartr', 'sol', 'mani', 'skoll', 'hati'],
    key_logic: 'OR',
    is_global: true,
    enabled: true,
    position: 'before_char',
    priority: 0,
    content: `Nella cultura dei licantropi norreni della Founding Bloodline e dell'antico lignaggio Svartulfr, ogni individuo riceve alla nascita un nome civile. All'eta di tredici anni, durante il sacro rito della Presentazione in cui si manifesta per la prima volta la bestia interiore, il licantropo scopre e dichiara il nome del proprio lupo spirituale. Per legge ancestrale del branco, questo nome viene assunto come secondo nome ufficiale e formale dell'individuo, sancendo la transizione verso l'eta adulta e l'accettazione del proprio spirito ferino.

I Pilastri Mitologici e Dinastici della Tradizione:
1. Il Mito Primordiale di Hvit e la Prima Compagna di Wulfnic: La prima Hvit delle origini nacque dall'unione mistica tra Mani (la divinita maschile della Luna) e Hati Hrodvitnisson (che nella cosmologia di Svartulfr e la sacra lupa primordiale). Questa prima lupa bianca divenne la prima compagna eterna di Wulfnic Bloodmoon, il capostipite creato da Fenris. Alla sua morte, la sua essenza lunare e il suo spirito protettivo si legano indissolubilmente al sangue Bloodmoon, reincarnandosi in ogni generazione attraverso le White Moon.
2. Il Vincolo delle White Moon: Tutte le reincarnazioni della lupa primordiale portano immancabilmente per legge sacra il nome del lupo originale: Hvit (la Bianca). Per questo motivo sia Nixara sia sua figlia Alyssa portano Hvit come secondo nome formale (Nixara Hvit Bloodmoon e Alyssa Hvit Douglas Bloodmoon), e per questo l'antico patriarca Wulfnic vede in Alyssa il riflesso vivente e benedetto della sua compagna perduta.
3. La Stirpe Solare di Svartr e Skoll: In simmetria perfetta e opposta ad Hvit, la controparte maschile dell'eclissi solare discende dall'unione tra Sol (la divinita femminile del Sole) e il lupo Skoll. Se Hvit incarna la pura luce lunare (Bianco), la progenie di Skoll assume il nome di Svartr (il Lupo Nero / l'Ombra Solare). Da questo archetipo millenario, Jasper Douglas assume alla sua Presentazione il nome di lupo Svartr (Jasper Svartr Douglas Bloodmoon), creando con la gemella Alyssa Hvit la perfetta polarita cosmica del branco.
4. I Nove Firstblood: I nove guerrieri originali creati direttamente da Fenris (tra cui Wulfnic Bloodmoon) non possiedono un secondo nome separato. Essendo entita ancestrali unificate in cui uomo e lupo non sono mai stati divisi, il loro nome da lupo coincide identicamente con il loro nome vichingo di nascita.
5. I Giovani Pre-Presentazione: I cuccioli e i giovani licantropi che non hanno ancora compiuto tredici anni o non hanno ancora superato la cerimonia della Presentazione (come Edric Douglas) non possiedono un nome da lupo e usano unicamente il nome di battesimo civile.`
  };

  const tradition2 = {
    title: 'Lycanthrope Birth-Rune Ritual',
    name: 'Lycanthrope Birth-Rune Ritual',
    type: 'lore/concept',
    keys: ['birth-rune', 'birth rune', 'runa di nascita', 'fifth day ritual', 'serpent tooth', 'cold iron ink', 'gebo', 'thurisaz', 'kenaz', 'tiwaz', 'othala', 'perthro', 'ingwaz'],
    key_logic: 'OR',
    is_global: true,
    enabled: true,
    position: 'before_char',
    priority: 0,
    content: `Il rito della Runa di Nascita (Birth-Rune) e una delle pratiche cerimoniali piu intoccabili della tradizione licantropica. Esattamente il quinto giorno dopo la nascita del neonato, il patriarca o l'anziano del branco celebra l'incisione della runa dell'antico Futhark che ne dichiara l'essenza spirituale, il temperamento e il vincolo col destino.

Il rituale esige rigorosamente tre elementi arcaici:
- L'Ago Sacro: L'incisione viene effettuata unicamente utilizzando un autentico dente di serpente, simbolo di saggezza velenosa, mutamento e precisione.
- L'Inchiostro del Vincolo: L'inchiostro viene preparato miscelando carbone di legna sacra purificata con polvere finissima di ferro freddo (cold iron). La presenza del cold iron e fondamentale: ancorando l'inchiostro nella carne, sigilla la risonanza magica della runa e funge da barriera indelebile contro interferenze demoniache, corruzioni astrali e incantesimi di possessione mentale.
- La Sede: La runa viene sempre incisa all'interno del polso (tradizionalmente il sinistro, il lato del cuore e della guardia in combattimento), lasciando una caratteristica cicatrice scura cerimoniale.

Le Rune della Casata Douglas e Bloodmoon:
- Gebo (Il Dono e il Legame Sacro): Incisa sui polsi dei gemelli Alyssa e Jasper, a suggello della loro sincronia spirituale ed empatica assoluta.
- Thurisaz (La Spina e la Forza Bruta): Incisa su Malachia, a sigillo della sua potenza da berserker d'assalto e guardiano incrollabile.
- Kenaz (La Torcia e l'Acume): Incisa su Noah, a riflettere la sua visione strategica, l'intelletto brillante e la diplomazia.
- Tiwaz (La Giustizia e il Comando): Incisa su Erik, il Prime Alpha, quale simbolo di onore marziale e autorita legittima di comando.
- Perthro (Il Destino Lunare): Incisa su Nixara Bloodmoon.
- Othala (La Stirpe Ancestrale): Incisa sul patriarca Wulfnic Bloodmoon.
- Ingwaz (Il Potenziale in Germoglio): Incisa sul giovane Edric Douglas in attesa della maturita.`
  };

  // 1. POST TO WORLD LEXICON
  console.log('\n1. Creating entries in World Lexicon...');
  for (const entry of [tradition1, tradition2]) {
    const payload = {
      world_id: worldId,
      title: entry.title,
      type: entry.type,
      keys: entry.keys,
      key_logic: entry.key_logic,
      content: entry.content,
      is_global: true,
      enabled: true,
      position: entry.position,
      priority: entry.priority
    };

    const res = await fetch('https://app.wyvern.chat/api/worlds/lexicon', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    console.log(` -> Created in World Lexicon: "${entry.title}" (Status: ${res.status}, ID: ${data.id})`);
  }

  // 2. APPEND TO LOREBOOK I
  console.log('\n2. Fetching Svartulfr - Lorebook I for targeted append...');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb1Id}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const lbData = await resLb.json();
  fs.writeFileSync('scratch/pre_traditions_lorebook_I.json', JSON.stringify(lbData, null, 2));

  const existingLexicon = lbData.lexicon || [];
  console.log(`Current entries in Lorebook I: ${existingLexicon.length}`);

  // Check if entries already exist
  const hasTrad1 = existingLexicon.some(e => (e.title || e.name) === tradition1.title);
  const hasTrad2 = existingLexicon.some(e => (e.title || e.name) === tradition2.title);

  const updatedLex = [...existingLexicon];
  if (!hasTrad1) {
    updatedLex.push({
      entry_id: `entry_lore_naming_tradition_${Date.now()}`,
      name: tradition1.title,
      title: tradition1.title,
      keys: tradition1.keys,
      key_logic: 'OR',
      type: 'lore/concept',
      content: tradition1.content,
      enabled: true,
      constant: false,
      position: 'before_char',
      priority: 0
    });
    console.log(`Added "${tradition1.title}" to Lorebook I payload.`);
  } else {
    console.log(`"${tradition1.title}" already exists in Lorebook I.`);
  }

  if (!hasTrad2) {
    updatedLex.push({
      entry_id: `entry_lore_birth_rune_${Date.now() + 1}`,
      name: tradition2.title,
      title: tradition2.title,
      keys: tradition2.keys,
      key_logic: 'OR',
      type: 'lore/concept',
      content: tradition2.content,
      enabled: true,
      constant: false,
      position: 'before_char',
      priority: 0
    });
    console.log(`Added "${tradition2.title}" to Lorebook I payload.`);
  } else {
    console.log(`"${tradition2.title}" already exists in Lorebook I.`);
  }

  const resPutLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb1Id}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ lexicon: updatedLex })
  });
  console.log('Lorebook I PUT status:', resPutLb.status);

  // 3. VERIFY
  console.log('\n=== VERIFICATION ===');
  const vLb = await (await fetch(`https://app.wyvern.chat/api/lorebooks/${lb1Id}`, { headers: { 'Authorization': 'Bearer ' + token } })).json();
  console.log(`Verified Lorebook I total entries: ${vLb.lexicon?.length}`);
  const v1 = vLb.lexicon?.find(e => (e.title || e.name) === tradition1.title);
  const v2 = vLb.lexicon?.find(e => (e.title || e.name) === tradition2.title);
  console.log(' - Found Tradition 1 in Lorebook I:', !!v1, '| Keys:', v1?.keys?.length);
  console.log(' - Found Tradition 2 in Lorebook I:', !!v2, '| Keys:', v2?.keys?.length);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
