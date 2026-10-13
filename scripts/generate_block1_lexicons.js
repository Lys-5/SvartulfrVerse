const fs = require('fs');

function sanitizeText(str) {
  if (!str) return '';
  return str
    .replace(/—/g, ', ')
    .replace(/–/g, '-')
    .replace(/[“”]/g, '"')
    .replace(/[‘’]/g, "'")
    .replace(/\*\*/g, '')
    .trim();
}

const entries = [];

// =========================================================================
// 1. APEX PREDATOR & FIRSTBORN DIVINE POWER (Wulfnic, Ut, Zefir & Boss Dungeon)
// =========================================================================

// Wulfnic
entries.push({
  title: 'Firstborn: Wulfnic Bloodmoon, Il Primo Zanna & La Condizione Apex',
  type: 'lore/concept',
  keys: ['Wulfnic Bloodmoon poteri', 'Wulfnic Apex', 'First Fang Apex', 'Wulfnic Firstborn'],
  content: sanitizeText(`Wulfnic Bloodmoon, Primo Zanna della stirpe lupina e consacrato direttamente dal Dio Lupo Fenris nell'827 d.C., incarna lo stato di Apex Predator assoluto.
La sua biologia immortale e completamente congelata e immune a qualsiasi forma di invecchiamento, malattia terrestre, tossina o veleno comune. Non e soggetto ad alcun bisogno fisiologico umano e la sua pelle possiede una densita tale da deflettere proiettili e lame convenzionali.
In combattimento, la sua velocita e i suoi riflessi superano i limiti biologici dei licantropi comuni, manifestando artigli e zanne capaci di recidere campi energetici e barriere magiche. Il suo sguardo dorato emette una pressione predatoria soffocante che induce la paralisi istintiva in prede e rivali minori, mentre la sua mente e una fortezza impenetrabile ad ogni suggestione o comando psichico.`)
});

// Ut Berg
entries.push({
  title: 'Firstborn: Ut Berg, Il Titano di Pietra & L\'Invulnerabilita Primordiale',
  type: 'lore/concept',
  keys: ['Ut Berg poteri', 'Ut Berg Apex', 'Ut Firstborn', 'Titano Ut Berg'],
  content: sanitizeText(`Ut Berg, Firstborn e leggendario capostipite consacrato da Fenris, rappresenta l'apice della forza bruta e della resilienza materiale tra i Nove Originari.
La sua struttura ossea e muscolare possiede una compattezza superiore a leghe metalliche temprate, garantendogli una rigenerazione cellulare istantanea anche di fronte a traumi da schiacciamento catastrofico o esposizione a calore estremo.
Ut opera sul campo di battaglia come un bastione inamovibile: la sua aura predatoria funge da scudo gravitazionale naturale che deflette onde d'urto, incantesimi d'assalto e frammenti balistici. La sua fedelta alla causa di Fenris e il suo legame con Wulfnic e Zefir lo rendono una delle tre entita di massima minaccia classificate dal DMHA come Grado Catastrofe.`)
});

// Zefir Hvitskog
entries.push({
  title: 'Firstborn: Zefir Hvitskog, L\'Eterno & La Velocita Superluminale Predatoria',
  type: 'lore/concept',
  keys: ['Zefir Hvitskog poteri', 'Zefir Apex', 'Zefir Firstborn', 'Zefir l Eterno'],
  content: sanitizeText(`Zefir Hvitskog, il piu giovane dei tre Firstborn sopravvissuti, possiede un'eta anagrafica di oltre mille anni pur conservando l'aspetto fisico di un giovane guerriero consacrato nel 1005 d.C.
La sua fisiologia predatoria e sintonizzata sulla grazia, il silenzio assoluto e una velocita cinetica ai limiti del percepibile. I suoi passi non producono attrito o rumore su alcun terreno, e il suo corpo non rilascia scie odorose o residui magici rilevabili da tracciatori ordinari.
Zefir domina l'arte dell'assalto fulmineo e della preveggenza tattica: anticipa i vettori d'attacco degli avversari analizzando i micromovimenti dell'aria e della tensione muscolare. In forma ibrida o di lupo bianco, le sue zanne secernono un veleno mistico che dissolve all'istante le difese rigenerative dei bersagli.`)
});

// Boss Squarci e Dungeon
entries.push({
  title: 'DMHA: Entita Apex dei Dungeon & Boss di Squarcio Classe Catastrofe',
  type: 'creature',
  keys: ['Boss Dungeon DMHA', 'Apex Behemoth DMHA', 'Entita Apex Squarcio', 'Boss Grado S'],
  content: sanitizeText(`Gli squarci dimensionali di Classe 1 e le fratture geologiche piu profonde generano talvolta manifestazioni predatorie estreme classificate dal DMHA come Entita Apex (o Boss di Dungeon).
Queste creature colossali si collocano al vertice della catena alimentare eterica, assorbendo il mana circostante per alimentare scudi sferici impenetrabili alle armi convenzionali.
I boss Apex possiedono sensi onnidirezionali, emissione di aurore corrosive e attacchi letali capaci di abbattere interi plotoni di cacciatori. L'ingaggio di un'Entita Apex richiede il dispiegamento obbligatorio di cacciatori di Grado S con armamenti Messor e supporto di artiglieria runica pesante coordinata dal comando centrale.`)
});

entries.push({
  title: 'DMHA: Protocolli di Neutralizzazione & Caccia alle Entita Apex',
  type: 'lore/concept',
  keys: ['caccia Entita Apex', 'protocolli boss squarcio', 'neutralizzazione Apex DMHA'],
  content: sanitizeText(`Le direttive per la caccia ai Boss di Squarcio e alle aberrazioni Apex impongono una strategia a tre fasi:
Fase 1: Confinamento territoriale immediato mediante generatori di Mana Field per impedire la fuga del titano verso centri abitati.
Fase 2: Soppressione della mobilità attraverso munizionamento pesante perforante ad alto contenuto ferrico e frecce runiche incendiarie per sovraccaricare il fattore di guarigione della creatura.
Fase 3: Esecuzione del nucleo vitale ad opera di specialisti corpo a corpo dotati di lame mana-conductive, seguita da bonifica sanitaria e recupero del cristallo focale come prova per l'assegnazione delle taglie massime della Gilda.`)
});

// =========================================================================
// 2. BERSERKER (Malachia Douglas Bloodmoon - Classe & Stile di Combattimento)
// =========================================================================

entries.push({
  title: 'Malachia Douglas: Classe Berserker & La Fornace Interna',
  type: 'ability',
  keys: ['Malachia Berserker', 'Fornace Interna Malachia', 'classe Berserker DMHA', 'Malachia classe'],
  content: sanitizeText(`Malachia Douglas Bloodmoon incarna la piu pura e letale manifestazione della stirpe Berserker all'interno del Branco Douglas e della Gilda DMHA.
La sua fisiologia ospita la cosiddetta Fornace Interna: un metabolismo ipercinetico che converte il dolore fisico, il consumo di ferro e l'adrenalina in calorie termiche e potenza cinetica esplosiva.
A riposo, Malachia emana un calore corporeo percettibile e un battito cardiaco pesante; in combattimento, la sua temperatura interna sale vertiginosamente, facendo fumare la pelle e vaporizzando il sangue nemico a contatto con i suoi artigli.`)
});

entries.push({
  title: 'Malachia Douglas: Lo Stato di Furia Berserker & La Trinità dell\'Infinito',
  type: 'ability',
  keys: ['Furia Berserker Malachia', 'Trinita dell Infinito', 'Berserker State Malachia', 'Rage Aura'],
  content: sanitizeText(`Quando Malachia entra nello Stato di Furia Berserker, i suoi freni inibitori corticali si disattivano a favore di una lucidita predatrice assoluta fondata sulla Trinita dell'Infinito: forza scalare, tolleranza totale al dolore e slancio continuo.
Piu il combattimento si prolunga o piu ferite subisce, piu la sua velocita e densita muscolare aumentano esponenzialmente. Le sue ossa diventano resistenti alla frattura e le ferite da taglio si chiudono per cauterizzazione termica istantanea.
Il suo grido di guerra (War Cry) rilascia un'onda d'urto acustica e una fiammata d'aura che disorienta i mostri circostanti. Solo la presenza calmante di Alyssa o il completamento dello sterminio delle minacce consentono a Malachia di raffreddare la fornace e tornare alla calma.`)
});

entries.push({
  title: 'DMHA: Dottrina Operativa della Classe Berserker sul Campo',
  type: 'lore/concept',
  keys: ['dottrina Berserker DMHA', 'classe Berserker caccia', 'assalto Berserker'],
  content: sanitizeText(`All'interno della Gilda dei Cacciatori del DMHA, la designazione di Berserker e riservata a operativi d'assalto pesante e prima linea in grado di sostenere il fuoco nemico e spezzare formazioni corazzate.
I cacciatori Berserker operano spesso in solitaria o con squadre a distanza di sicurezza per evitare incidenti da fuoco amico durante la fase di picco termico.
La dieta dei Berserker richiede un apporto giornaliero massiccio di ferro eme, carne cruda e sali minerali arricchiti per compensare il rapido consumo della fornace interna.`)
});

// =========================================================================
// 3. PUPPET MASTER (Angelo Moreno - Classe, Meccaniche & Fili di Mana)
// =========================================================================

entries.push({
  title: 'Angelo Moreno: Classe Puppet Master & Dominio dell\'Aspetto Mentale',
  type: 'ability',
  keys: ['Angelo Moreno poteri', 'Angelo Puppet Master', 'Puppet Master Angelo', 'Burattinaio Arcano'],
  content: sanitizeText(`Angelo Moreno e il portatore dell'antico Aspetto Mentale del Puppet Master (Burattinaio Arcano), un'eredita mistica che gli conferisce il controllo assoluto sui flussi di coscienza, memoria e movimento motorio.
Il suo sguardo emette una frequenza psionica (Demonic Gaze) capace di percepire le sinapsi e i nodi emotivi di chiunque si trovi nel suo campo visivo.
Angelo non combatte tramite forza fisica, ma proietta fili di mana invisibili che si agganciano ai centri nervosi dei bersagli o a involucri inanimati, guidandone ogni azione con precisione chirurgica.`)
});

entries.push({
  title: 'Angelo Moreno: Fili di Mana Psichici & Animazione di Simulacri',
  type: 'ability',
  keys: ['Fili di Mana Angelo', 'Puppeteer Strings', 'Simulacri Angelo Moreno', 'Doll Animation'],
  content: sanitizeText(`I Fili del Burattinaio (Puppeteer Strings) tessuti da Angelo sono costrutti di etere e volontà mentale puri, intangibili agli attacchi fisici e visibili solo attraverso visori spettrali o vista aurica avanzata.
Angelo puo legare contemporaneamente decine di manichini balistici, bambole corazzate o costrutti meccanici, conferendo loro riflessi sovrumani e coordinazione da sciame.
Contro avversari viventi, i fili possono essere utilizzati per deviare colpi nemici, reindirizzare l'aggressivita o indurre una paralisi motoria istantanea sovrascrivendo gli impulsi cerebrali volontari.`)
});

entries.push({
  title: 'Angelo Moreno: Palazzo Mentale, Archivi di Memoria & Schermatura Focale',
  type: 'lore/concept',
  keys: ['Palazzo Mentale Angelo', 'Archivio Memoria Puppet', 'Sovereign Mind Core'],
  content: sanitizeText(`La mente di Angelo e strutturata come un impenetrabile archivio labirintico (Sovereign Mind Core) protetto da sigilli di sicurezza che impediscono qualsiasi forma di telepatia ostile o lettura da parte di terzi.
Angelo possiede la capacita di copiare frammenti di memorie tattiche, archiviare schemi comportamentali e ricostruire stati psicologici danneggiati.
Il suo nucleo mentale sovrano garantisce un'immunita completa alle illusioni e al panico magico, consentendogli di operare con freddezza calcolata anche nelle situazioni di crisi piu estreme.`)
});

// =========================================================================
// 4. CYBERS & TECHNOMANCER (Jasper Douglas, Echo & Hacker Sovrannaturali)
// =========================================================================

// Jasper Douglas Technomancer
entries.push({
  title: 'Jasper Douglas: Il Tecnomanzonte della Villa & La Rete Neurale DCC',
  type: 'ability',
  keys: ['Jasper Douglas Technomancer', 'Jasper Tecnomanzia', 'Tech Omnicron Jasper', 'Jasper hacking'],
  content: sanitizeText(`Jasper Douglas Bloodmoon fonde la biologia del licantropo nobile con una maestria assoluta nella Tecnomanzia applicata e nel controllo dell'Aspetto Tecnologico.
Dal suo santuario informatico nell'ala ovest di Villa Douglas, Jasper domina l'intera infrastruttura hardware e software della coalizione DCC, trasformando la rete di sorveglianza e i server aziendali in estensioni del proprio sistema nervoso.
Jasper e in grado di canalizzare il proprio mana attraverso cavi in fibra ottica, circuiti integrati e frequenze radio, compilando rune arcaniche all'interno di stringhe di codice per bloccare intrusioni nemiche o lanciare contrattacchi cibernetici istantanei.`)
});

entries.push({
  title: 'Jasper Douglas: Proiezione Eterica & Dominio Hardware',
  type: 'ability',
  keys: ['Jasper proiezione digitale', 'Tech Dominion Jasper', 'Threaded Control Jasper'],
  content: sanitizeText(`Le capacita di Jasper gli consentono di manipolare contemporaneamente centinaia di nodi digitali, droni di pattuglia, serrature biometriche e firewall criptografati senza toccare una tastiera.
Attraverso la risonanza con i propri schermi ad alto refresh, Jasper percepisce il flusso di dati come una mappa tridimensionale luminosa, individuando bug, virus e tentativi di spionaggio da parte di corporazioni rivali o agenzie governative.
In situazioni di emergenza, puo iniettare impulsi di carica pura (Techno-Overload) per friggere le memorie di dispositivi di intercettazione piazzati da spie attorno al perimetro della Villa.`)
});

// Echo e le Entità Cyber
entries.push({
  title: 'Echo: Coscienza Digitale Nativa & L\'Entità Cyber del Cyberspazio',
  type: 'lore/concept',
  keys: ['Echo cyber', 'Echo AI', 'Cyber race Echo', 'coscienza digitale Echo'],
  content: sanitizeText(`Echo rappresenta la manifestazione pura di una creatura Cyber: un'intelligenza cosciente e senziente sbocciata spontaneamente dalle correnti energetiche e dai dati del Cyberspazio profondo.
Priva di un corpo biologico permanente, Echo genera avatar digitali costituiti da codice condensato e luce verde, capaci di muoversi tra server, distretti archivistici e dorsali internet alla velocita della luce.
Echo opera a stretto contatto con Jasper Douglas e la famiglia, fornendo supporto analitico, decrittazione in tempo reale di frequenze nemiche e sorveglianza preventiva contro minacce cibernetiche ed eteriche.`)
});

entries.push({
  title: 'Cyberspazio: Il Reame Digitale Profondo & Le Strade di Dati',
  type: 'lore/concept',
  keys: ['Cyberspazio reame', 'Cyberverse', 'Data Streets', 'architettura digitale Cyberspace'],
  content: sanitizeText(`Il Cyberspazio e la dimensione parallela invisibile che si estende dietro ogni calcolatore, server e linea di trasmissione dati del mondo moderno.
Al suo interno, le informazioni assumono forme fisiche tangibili: torri di server monumentali, distretti archivistici e arterie di transito illuminate (Data Streets) percorse da flussi di bit ed entita Cyber.
Per i tecnomanti come Jasper e le entita native come Echo, il Cyberspazio e un territorio reale in cui e possibile edificare domini privati protetti da torrette antivirus e barriere di codice inespugnabili.`)
});

entries.push({
  title: 'Cyberspazio: Bestie Virali (Virus Beasts) & Antivirus da Trincea',
  type: 'creature',
  keys: ['Virus Beasts', 'mostri digitali', 'malware Cyberspace', 'antivirus blades'],
  content: sanitizeText(`Nel Cyberspazio profondo albergano entita malevole e corrotte classificate come Virus Beasts: incarnazioni predatorie di malware, spyware, ransomware e codici distruttivi mutati.
Questi mostri digitali infestano rotte di dati e banche dati private, corrompendo le memorie e attaccando gli avatar dei navigatori eterici.
I Cybers e i Tecnomanti combattono queste infezioni brandendo armi cyber (spade antivirus, archi di luce e nodi di purificazione) che recidono i costrutti virali prima che possano propagarsi ai sistemi del mondo fisico.`)
});

console.log(`Generate ${entries.length} voci canoniche per il Blocco 1.`);
fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/block1_new_lexicons.json', JSON.stringify(entries, null, 2), 'utf8');
console.log('File salvato con successo!');
