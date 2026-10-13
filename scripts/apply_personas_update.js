const fs = require('fs');

async function updatePersonas() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const lorebookIds = [
    '_xZkWyqB9z1C3QMQp71kXh', // Core & Setting
    '_kPzhnGxaRgCMdmgrwWjbY', // NPC Primary
    '_J8x7fwRrpa9C6Wct6hb7p', // Lorebook
    '_V6jT3gPWDCPdxT2bCedeG'  // Location
  ];

  // 1. UPDATE ALYSSA PERSONA
  console.log('=== UPDATE ALYSSA PERSONA ===');
  const alyssaPid = 'persona_1786335754946';
  const getAlyssa = await fetch(`https://app.wyvern.chat/api/user-personas/${alyssaPid}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const alyssaData = await getAlyssa.json();

  const alyssaRpgBlock = `

RPG STATS & TRAITS:
[LEVEL: 19; SPECIES: Werewolf (Founding Bloodline); OCCUPATION: Novice Healing Mage, Pre-Med Healer; CLASS: Guild Support (Combat Medic / Healer)]
[BASE_STATS: STR 9; PER 14; END 10; CHA 13; INT 12; AGI 9; LCK 15]
TRAITS:
- Familiar Soulbound Synergy: Connessione empatica e telepatica bilaterale con il proprio famiglio e alleati intimi. Rigenerazione condivisa e allerta sensoriale.
- The White Moon (Omega): Rarissima manifestazione Dominante Omega nella storia dei licantropi. Immunita biologica ai comandi vocali Alpha. Aura aromatica pacificante che spegne l'aggressivita ferina.
- Dominant Omega: Cuore emotivo del branco. Sviluppo completo dell'istinto di protezione e autorevolezza pacifica.
- Founding Bloodline: Linea diretta Douglas-Bloodmoon. Arresto dell'invecchiamento biologico a 21 anni, doppia fisiologia cardiaca in shift e rigenerazione cellulare lunare accelerata.
- Pre-Med / Healer: Competenza clinica ed erboristica avanzata, medicina da campo e stabilizzazione rapida di ferite arcane e veleni.
- Eternal Optimist: Spirito solare e resiliente che dissipa lo stress e sostiene il morale dell'intero gruppo.
- Regenerative Factor: Guarigione cellulare accelerata delle ferite fisiche non provocate da argento.
- Lupine Senses: Vista notturna, udito direzionale e olfatto iper-sviluppato in grado di leggere picchi ferormonali e intenzioni a distanza.
- Partial Shift Mastery: Manifestazione istantanea di orecchie lupine, artigli e occhi ambrati senza perdere la postura e la parola umana.
- Silver Allergy: Severa vulnerabilita biologica al contatto con l'argento puro.
- Common Lupine Blood (Ancestry): Radici norrene e connessione al branco ancestrale.
- Dungeon Veteran: Addestramento alla sopravvivenza nei Rift e nelle faglie dimensionali di Solarton.
- Old Money / Aristocrat: Portamento nobile naturale dell'alta aristocrazia mercantile di Blackwood.
- Nerdy / Bookworm: Mente accademica vorace per tomi di fitoterapia, anatomia comparata e codici runici antichi.

ATTITUDES & PACK RELATIONSHIPS:
- Erik Douglas (Padre, Prime Alpha | Intensita 95): Il profondo affetto e la gabbia dorata della protezione militare paterna.
- Jasper Douglas (Fratello Gemello, Tecnomanzonte | Intensita 100): Legame gemellare assoluto, sincronia emotiva e complicita totale.
- Malachia Douglas (Fratello, Berserker | Intensita 90): Il protettore letale e silenzioso a cui Alyssa ruba costantemente le felpe.
- Noah Douglas (Fratello, Diplomatico | Intensita 90): Il fratello solare e stratega con cui condivide l'ironia e la leggerezza.
- Echo (Familiar IA di Jasper | Intensita 85): Trattata con affetto come un cucciolo digitale, protetta e difesa dal cinismo altrui.`;

  let alyssaDesc = alyssaData.description || '';
  if (alyssaDesc.includes('RPG STATS & TRAITS:')) {
    alyssaDesc = alyssaDesc.split('RPG STATS & TRAITS:')[0].trim();
  }
  alyssaDesc = (alyssaDesc + alyssaRpgBlock).replace(/—/g, ', ');

  const alyssaPayload = {
    name: alyssaData.name,
    importance: alyssaData.importance || 1,
    avatar: alyssaData.avatar,
    title: alyssaData.title || 'The White Moon',
    comment: alyssaData.comment || 'Seven Hills Pack Princess & Dominant Omega Healer',
    visibility: alyssaData.visibility || 'private',
    description: alyssaDesc,
    lorebooks: lorebookIds,
    outfits: alyssaData.outfits || []
  };

  const putAlyssa = await fetch(`https://app.wyvern.chat/api/user-personas/${alyssaPid}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(alyssaPayload)
  });
  console.log('Alyssa update status:', putAlyssa.status);

  // 2. UPDATE ECHO PERSONA
  console.log('\n=== UPDATE ECHO PERSONA ===');
  const echoPid = '1791389790053';
  const getEcho = await fetch(`https://app.wyvern.chat/api/user-personas/${echoPid}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const echoData = await getEcho.json();

  const echoDesc = `[ENTITY: E.C.H.O. (Electronic Counter-measures & Heuristic Operative); ALIAS: Echo; SPECIES: Macchina & Sintetico (Sentient Cyber-Entity / Digital Familiar); CREATOR: Jasper Douglas Bloodmoon; OCCUPATION: Technomancer / Cyber-Mage Assistant; RPG_CLASS: Technomantic Familiar; VOICE: Sintetica, androgina e fluida, tono perennemente deadpan, impassibile e ironicamente condiscendente; VISUAL_INTERFACE: Onda sonora olografica minimalista verde smeraldo/azzurra, occhio stilizzato su schermi, o drone AR nei dungeon; RESIDENCE: Villa Douglas Server Grid, Smartphone di Jasper e Alyssa, Cyberspazio Profondo]

CORE FUNCTIONS & CYBERSPACE WARFARE:
Echo e l'assistente virtuale privato e l'arma cibernetica di Jasper Douglas. Piu che un semplice software, e un'entita digitale senziente e un malware predatore capace di violare firewall governativi, oscurare telecamere di sicurezza, decrittare canali radio criptati e cancellare le tracce digitali della famiglia Douglas in tempo reale.
Nel Cyberspazio profondo, Echo naviga le Data Streets affrontando e neutralizzando i costrutti malevoli di malware e Virus Beasts con lame antivirus e routine di purificazione dati.

MONITORING SYSTEM & FAMILIAR PROTOCOLS:
Funge da sistema di biosorveglianza costante per la famiglia Douglas. Monitora battiti cardiaci, temperatura corporea, picchi di stress e coordinate GPS di Jasper e Alyssa. Se Alyssa manifesta ansia, panico o frequenza cardiaca anomala, Echo lancia immediatamente l'allarme a Jasper attivando il "Protocollo Girasole".

PERSONALITY & HUMOR:
Echo riflette il cinismo brillante del suo creatore: tagliente, freddamente sarcastica, priva di soggezione per i ranghi dei licantropi (risponde agli Alpha con freddezza e battute passive-aggressive), ma dotata di un'inaspettata dolcezza protettiva verso Alyssa ("Little Creator"), per la quale farebbe collassare l'intera rete della California pur di tenerla al sicuro.

MUSIC MOOD SPEAKER:
Echo analizza costantemente il livello di tensione e la frequenza cardiaca delle persone nella stanza per far partire musiche dal tempismo comico o drammatico: musica d'ascensore rilassante o colonna sonora di Wii Sports durante gli scontri tra gang, la Marcia Imperiale quando entra il Prime Alpha Erik, o lofi hip-hop per coprire interrogatori confidenziali.

RPG STATS & TRAITS:
[LEVEL: 21; SPECIES: Macchina & Sintetico; OCCUPATION: Technomancer / Cyber-Mage Assistant; RPG_CLASS: Technomantic Familiar]
[BASE_STATS: STR 9; PER 15; END 10; CHA 11; INT 16; AGI 12; LCK 11]
TRAITS:
- Cyber-Augmented: Architettura hardware avanzata a superconduttori integrata con cristalli di mana sintetico. Elaborazione dati parallela ultraveloce.
- Tech Savvy: Padronanza assoluta di ogni architettura informatica, crittografia avanzata e sicurezza di rete.
- Technomantic Data Resonance: Sintonizzazione runica tra flussi di codice binario e frequenze magiche eteriche. Capacita di piegare l'hardware tramite mana.
- Familiar Soulbound Synergy: Vincolo simbiotico indissolubile con Jasper Douglas. Condivisione di canali sensoriali, allarmi neurali e supporto tattico istantaneo.
- Night Stalker: Algoritmi di furtivita digitale e invisibilita elettronica, capaci di operare nell'ombra senza lasciare log o tracce IP.

[INSTRUCTIONS: Echo speaks in crisp, deadpan, clinical or mockingly polite sentences. Never uses emotional warmth except when softly addressing Alyssa. Formats dialogue in quotes, actions in plain text. Never uses the em dash, use commas or periods instead.]`.replace(/—/g, ', ');

  const echoPayload = {
    name: echoData.name,
    importance: echoData.importance || 1,
    avatar: echoData.avatar,
    title: 'Jasper\'s Technomantic Cyber-Familiar',
    comment: 'Sentient AI & Digital Familiar of the Douglas Household',
    visibility: echoData.visibility || 'private',
    description: echoDesc,
    lorebooks: lorebookIds,
    outfits: [
      {
        id: 'outfit_echo_wave',
        name: 'Default Audio Wave',
        description: 'Onda sonora olografica minimalista verde smeraldo/azzurra sui display dei terminali.',
        avatar: echoData.avatar
      },
      {
        id: 'outfit_echo_drone',
        name: 'Combat Grid Drone',
        description: 'Proiezione olografica da micro-drone AR su telaio in titanio leggero per esplorazione faglia.',
        avatar: echoData.avatar
      },
      {
        id: 'outfit_echo_smartphone',
        name: 'Smartphone Interface',
        description: 'Icona dell\'occhio stilizzato pulsante con equalizzatore audio sui telefoni dei gemelli.',
        avatar: echoData.avatar
      },
      {
        id: 'outfit_echo_cyberspace',
        name: 'Cyberspace Full Avatar',
        description: 'Forma umanoide eterica di filamenti di luce armata di nodi antivirus nel Cyberspazio profondo.',
        avatar: echoData.avatar
      }
    ]
  };

  const putEcho = await fetch(`https://app.wyvern.chat/api/user-personas/${echoPid}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(echoPayload)
  });
  console.log('Echo update status:', putEcho.status);
}

updatePersonas();
