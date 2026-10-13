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
// 1. THE FAMILIAR SPECIES (OC) - Gestione Animali da Compagnia nel Mondo Magico
// =========================================================================
entries.push({
  title: 'SUCC: Animali da Compagnia & Famigli nel Mondo Magico',
  type: 'creature',
  keys: ['famigli SUCC', 'animali compagni magia', 'familiars magic', 'creature vincolate'],
  content: sanitizeText(`Nel contesto magico e accademico della Solarton University e delle casate sovrannaturali, i Famigli sono creature speciali, spiriti guardiani o costrutti biologici avanzati legati da un patto simbiotico a un custode umano, mutaforma o mago.
A differenza dei normali animali domestici, i famigli possiedono un nucleo di intelligenza arcanica, longevita aumentata dipendente dal mana del padrone e una sensibilita innata nel rilevare anomalie dimensionali, veleni o intenzioni ostili nell'ambiente circostante.`)
});

entries.push({
  title: 'SUCC: Il Rito di Vincolo del Famiglio & Sincronia Animica',
  type: 'lore/concept',
  keys: ['vincolo famiglio', 'patto animico famigli', 'sincronia famiglio'],
  content: sanitizeText(`Il rito di vincolo e una cerimonia formale attraverso cui un individuo e un famiglio consenziente intrecciano le rispettive frequenze auriche.
Il legame stabilisce un canale di comunicazione telepatica ed empatica a corto raggio: il custode puo percepire gli allarmi sensoriali del compagno animale e condividere porzioni minori della propria riserva energetica per accelerarne la guarigione.
Il codice accademico del SUCC vieta l'imposizione di vincoli forzati o l'uso di sostanze coercitive, tutelando i diritti e il benessere psicofisico dei compagni sovrannaturali.`)
});

entries.push({
  title: 'SUCC: Protocolli di Cura, Nutrizione & Clinica Veterinaria dei Famigli',
  type: 'lore/concept',
  keys: ['cura famigli SUCC', 'nutrizione magica animali', 'veterinaria sovrannaturale'],
  content: sanitizeText(`La Facolta di Medicina Veterinaria Arcana del SUCC gestisce un dispensario dedicato alla cura e alla nutrizione specializzata dei famigli del campus.
Le diete variano a seconda della fisiologia della creatura: paste nutrienti arricchite con estratti di erbe lunari per famigli therianthropi, composti mineralizzati per costrutti di pietra e integratori di mana purificato per spiriti eterici.
Sono previste visite periodiche di allineamento aurico per prevenire la saturazione eterica e verificare l'elasticita dei canali di risonanza con il proprietario.`)
});

// =========================================================================
// 2. GRAVITON - Manipolazione Gravitazionale & Vettori Cinetici
// =========================================================================
entries.push({
  title: 'Magia: Disciplina del Gravitone & Controllo dei Vettori di Massa',
  type: 'lore/concept',
  keys: ['Gravitone magia', 'gravitocinesi', 'controllo gravita', 'Graviton magic'],
  content: sanitizeText(`La scuola del Gravitone e una disciplina arcana avanzata fondata sulla manipolazione attiva dei campi di massa e delle linee di gravita locale.
I praticanti possono alterare il peso percepito del proprio corpo o di oggetti bersaglio, rendendosi leggeri come una piuma per compiere balzi titanici o incrementando la densita cinetica di un'arma nel momento esatto dell'impatto per sfondare blindature corazzate.
La canalizzazione consuma elevate riserve di glucosio e richiede un'impeccabile concentrazione geometrica per non creare micro-singolarita instabili nel piano materiale.`)
});

entries.push({
  title: 'Magia: Barriere a Repulsione Gravitazionale & Deflessione Balistica',
  type: 'ability',
  keys: ['barriere gravitazionali', 'deflessione balistica gravita', 'scudo gravitone'],
  content: sanitizeText(`Applicazione difensiva della magia gravitonica. Emettendo una bolla a repulsione cinetica invertita attorno al perimetro dell'operatore, proiettili balistici, schegge metalliche e onde d'urto esplosive perdono istantaneamente momento cinetico, cadendo inerti al suolo prima di toccare il bersaglio.
La barriera puo essere estesa per proteggere alleati adiacenti, fungendo da indispensabile strumento tattico durante gli scontri con tiratori scelti o creature dalle cariche travolgenti.`)
});

// =========================================================================
// 3. SHAPESHIFTER ESTESO - Mutaforma Non-Canini & Trasmutazione Fluida
// =========================================================================
entries.push({
  title: 'SUCC: Mutaforma a Morfologia Fluida & Specie Non-Canine',
  type: 'lore/concept',
  keys: ['mutaforma fluidi', 'trasmutazione non-canina', 'shapeshifting avanzato', 'Shapeshifter magic'],
  content: sanitizeText(`Oltre ai rami tradizionali dei lupi e dei therianthropi predatori, il SUCC riconosce e ospita studenti dotati di mutaforma fluida, capaci di alterare la propria struttura cellulare per assumere tratti di rettili, uccelli da preda, anfibi o sagome umanoidi mimetiche.
Questi individui non dipendono dal ciclo lunare, ma regolano la propria biochimica mediante respirazione ritmica e focalizzazione emotiva.
I corsi universitari di Morfogenesi Applicata insegnano a stabilizzare la densita degli organi interni durante i cambi rapidi di fisionomia per prevenire nausee da riallineamento viscerale.`)
});

// =========================================================================
// 4. DREAMWALKER - Viaggio Onirico & Combattimento nel Piano Astrale
// =========================================================================
entries.push({
  title: 'Magia: L\'Arte del Dreamwalker & Navigazione del Piano Onirico',
  type: 'lore/concept',
  keys: ['Dreamwalker magia', 'viaggio onirico SUCC', 'piano astrale sogni', 'combattimento onirico'],
  content: sanitizeText(`I Dreamwalker sono maghi e sensitivi capaci di distaccare la propria coscienza dal corpo fisico durante la fase REM per accedere al Piano Astrale Onirico.
In questa dimensione liminale, il pensiero modella istantaneamente la realta circostante: i Dreamwalker possono visitare i sogni di alleati per trasmettere messaggi criptati, estrarre traumi da possessione o combattere entita parassitarie notturne che tentano di prosciugare la mente di studenti e cittadini addormentati.
Il ritorno al corpo materiale richiede un'ancora sensoriale precisa, come un tocco familiare o una sveglia a frequenza runica controllata.`)
});

// =========================================================================
// 5. THE WARPER - Piegamento Spaziale, Teletrasporto & Micro-Squarci
// =========================================================================
entries.push({
  title: 'Magia: L\'Arte del Warper & Piegamento dello Spazio-Tempo Locale',
  type: 'lore/concept',
  keys: ['The Warper magia', 'piegamento spaziale', 'teletrasporto breve raggio', 'micro-squarci'],
  content: sanitizeText(`La disciplina del Warper permette di comprimere la distanza lineare tra due punti dello spazio mediante la creazione di micro-fratture controllate nel continuum dimensionale.
Un Warper addestrato puo teletrasportarsi istantaneamente per brevi distanze (Blink tattico), scambiare la propria posizione con quella di un oggetto o deviare traiettorie di attacchi aprendo fessure di deviazione eterica.
La pratica e strettamente regolamentata dal DMHA per evitare la formazione accidentale di squarci stabili di Classe 1 all'interno di edifici civili.`)
});

// =========================================================================
// 6. SHADOW LORD - Umbracinesi & Lame d'Ombra Condensata
// =========================================================================
entries.push({
  title: 'Magia: Disciplina dello Shadow Lord & Manipolazione dell\'Oscurità',
  type: 'lore/concept',
  keys: ['Shadow Lord magia', 'umbracinesi SUCC', 'lame ombra condensata', 'fusione con l ombra'],
  content: sanitizeText(`La scuola dello Shadow Lord canalizza l'energia fredda delle ombre e dei recessi dimensionali non illuminati.
I praticanti sono in grado di fondersi con le superfici buie per muoversi in totale invisibilita sensoriale, emergendo alle spalle del nemico con armi forgiate in ombra solida capaci di congelare i tessuti organici e intorpidire le risposte neuromuscolari della vittima.
La luce intensa e le rune solari consacrate costituiscono l'antidoto naturale a questa magia, che predilige missioni notturne di infiltrazione e ricognizione furtiva.`)
});

// =========================================================================
// 7. DRUID & SCULPTER - Geomanzia, Botanica da Guerra & Costrutti
// =========================================================================
entries.push({
  title: 'Magia: Druidismo Accademico & Botanica Bellica del SUCC',
  type: 'lore/concept',
  keys: ['Druidismo SUCC', 'botanica bellica', 'Druid magic', 'fitochimica arcana'],
  content: sanitizeText(`Il dipartimento di Botanica e Druidismo della Solarton University insegna la cooperazione diretta con la biosfera vegetale californiana.
I druidi del campus non praticano culti eremitici, ma applicano la fitochimica arcana per accelerare la crescita di radici stritolatrici, sintetizzare spore soporifere e purificare terreni contaminati da scorie di mostri o sostanze chimiche industriali.
La sinergia tra magia botanica e medicina rende i druidi tra i piu apprezzati guaritori e specialisti sul campo del DMHA.`)
});

entries.push({
  title: 'Magia: L\'Arte dello Sculpter & Modellazione dei Materiali Inorganici',
  type: 'lore/concept',
  keys: ['Sculpter magia', 'geomanzia SUCC', 'modellazione pietra metallo', 'costrutti inorganici'],
  content: sanitizeText(`Gli Sculpter sono specialisti nella trasmutazione e nel controllo plastico della materia solida inorganica: pietra, cemento armato, asfalto e leghe metalliche.
In pochi istanti, uno Sculpter puo innalzare barricate difensive dal suolo stradale, rimodellare varchi in pareti crollate o animare armature vuote e statue per creare sentinelle ausiliarie di supporto alle squadre di caccia urbane.`)
});

// =========================================================================
// 8. MYSTICS & SPELL COMPENDIUM - Tassonomia degli Incantesimi Accademici
// =========================================================================
entries.push({
  title: 'SUCC: Tassonomia Generale degli Incantesimi (Spell Compendium)',
  type: 'lore/concept',
  keys: ['Spell Compendium SUCC', 'incantesimi SUCC', 'Mystics magic system', 'circoli magia'],
  content: sanitizeText(`Il Compendio Ufficiale degli Incantesimi adottato dalla Facolta di Scienze Arcane del SUCC classifica le formule e i pattern magici in base a circoli di complessita e consumo di riserva metabolica:
Dal Primo Circolo (trucchetti di luce, accensione focale, stabilizzazione della pressione, telecinesi da laboratorio) fino ai Circoli Superiori (barriere di contenimento a cupola, trasmutazioni alchemiche di massa, fulmini a catena runica).
Ogni incantesimo e corredato da specifiche sui requisiti di focalizzazione (gestuale, verbale o tramite catalizzatore) e sulle precauzioni termiche per non incorrere nel burnout eterico.`)
});

entries.push({
  title: 'SUCC: Catalizzatori, Focus Runici & Sigilli d\'Incanalamento',
  type: 'item',
  keys: ['catalizzatori magici SUCC', 'focus runici', 'bacchette bastoni magia', 'sigilli incanalamento'],
  content: sanitizeText(`Strumenti di precisione utilizzati da studenti e incantatori per disciplinare il flusso di mana durante il lancio di formule complesse.
Realizzati in legni arcanici con anima di filo d'argento, cristalli di quarzo sintonizzato o anelli d'acciaio runico, i catalizzatori riducono del quaranta percento lo sforzo termico a carico del sistema nervoso dell'operatore, prevenendo contraccolpi magici in caso di formule interrotte bruscamente.`)
});

console.log(`Generate ${entries.length} voci canoniche per il Blocco 2.`);
fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/block2_new_lexicons.json', JSON.stringify(entries, null, 2), 'utf8');
console.log('File salvato con successo!');
