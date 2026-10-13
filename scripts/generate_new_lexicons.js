const fs = require('fs');

// Carichiamo i dump grezzi estratti
const laEntries = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/la_entries.json', 'utf8'));
const aegisEntries = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/aegis_entries.json', 'utf8'));

console.log(`Caricati ${laEntries.length} record da LA e ${aegisEntries.length} record da Aegis.`);

// Funzione di bonifica testo: divieto em-dash, virgolette standard, no asterischi inappropriati
function sanitizeText(str) {
  if (!str) return '';
  return str
    .replace(/—/g, ', ')
    .replace(/–/g, '-')
    .replace(/[“”]/g, '"')
    .replace(/[‘’]/g, "'")
    .replace(/\*\*/g, '') // no markdown bold nei testi world come da Regola 3
    .trim();
}

// -------------------------------------------------------------
// 1. GENERAZIONE DELLE 36 VOCI SUCC (DA LA: NEW MOON COMPENDIUM)
// -------------------------------------------------------------
const succEntries = [];

// A. Biologia & Fisiologia Mutaforma (16 voci)
succEntries.push({
  title: 'SUCC: Tassonomia & Fisiologia Generale dei Mutaforma',
  type: 'lore/concept',
  keys: ['SUCC mutaforma', 'mutaforma fisiologia', 'therianthropes SUCC', 'shapeshifter taxonomy'],
  content: sanitizeText(`La Facolta di Scienze Biologiche e Morfologiche della Solarton University adotta una classificazione sistematica per le specie therianthrope e mutaforma.
I mutaforma registrati al campus si suddividono in due macro-categorie biologiche: licantropi e werebeasts (a base umana con nucleo mutaforma ancestrale) e Beastweres (mutaforma inversi la cui forma originaria primaria e animale).
La trasformazione cellulare e un processo somatico controllato che richiede una riserva metabolica specifica, accelerando la rigenerazione tissutale e la densita muscolare a seconda della forma adottata (Base, Ibrida o Completa).`)
});

succEntries.push({
  title: 'SUCC: Fisiologia Licantropa & Fluttuazioni del Ciclo Lunare',
  type: 'lore/concept',
  keys: ['SUCC ciclo lunare', 'werewolf lunar cycle', 'fasi lunari SUCC', 'lunar rhythm SUCC'],
  content: sanitizeText(`Nel campus di Solarton, le fluttuazioni biologiche dei licantropi seguono una curva di risonanza sincronizzata con le fasi lunari.
Durante il novilunio (Luna Nuova), le capacita di rigenerazione e i sensi acuti operano a livello basale, favorendo la concentrazione accademica e la stabilita bio-chimica.
Con il crescere della luna fino al plenilunio, la soglia di tolleranza ferormonale e l'aggressivita istintiva si innalzano progressivamente, richiedendo l'uso preventivo di integratori calmanti e protocolli di de-escalation approvati dal Dipartimento Medico del SUCC.`)
});

succEntries.push({
  title: 'SUCC: Risonanza di Branco & Coesione Emotiva',
  type: 'lore/concept',
  keys: ['pack resonance SUCC', 'risonanza di branco', 'pack bond SUCC', 'coesione emotiva branco'],
  content: sanitizeText(`La risonanza di branco e il fenomeno empatico e sensoriale attraverso cui individui legati da gerarchia lupina o legame biologico condividono frequenze di reazione e impulsi ormonali.
Presso la SUCC, la concentrazione di branchi studenteschi (inclusi i nuclei legati alla Confraternita Bulls e al Branco Douglas) puo amplificare le risposte emotive collettive.
I corsi universitari di Gestione del Branco insegnano a canalizzare la risonanza per evitare reazioni di panico o rabbia a catena nei dormitori misti.`)
});

succEntries.push({
  title: 'SUCC: Regolamento Dieta & Igiene Olfattiva Predatoria',
  type: 'lore/concept',
  keys: ['SUCC dieta predatori', 'carnivore diet SUCC', 'igiene olfattiva SUCC', 'scent regulation SUCC'],
  content: sanitizeText(`Gli studenti carnivori e therianthropi mantengono un fabbisogno calorico giornaliero compreso tra 3.500 e 6.000 kcal, con una prevalenza di proteine nobili e ferro biodisponibile.
Le strutture ristorative del SUCC forniscono linee separate di macellazione certificata a crudo per preservare il valore nutritivo essenziale agli shifters.
Per garantire la convivenza serena nei corridoi didattici, e imposto l'uso di docce a neutralizzazione enzimatica per prevenire marcature territoriali involontarie tramite le ghiandole sudoripare e sebacee.`)
});

succEntries.push({
  title: 'SUCC: Vulnerabilita Tossicologiche ad Aconito & Metalli Pesanti',
  type: 'lore/concept',
  keys: ['aconito SUCC', 'vulnerabilita argento', 'wolfsbane SUCC', 'silver toxicity SUCC'],
  content: sanitizeText(`Il Dipartimento di Tossicologia del SUCC cataloga con rigore le sostanze capaci di compromettere la rigenerazione cellulare dei mutaforma.
L'argento puro genera un blocco mitocondriale immediato a contatto con i tessuti, inibendo il fattore di guarigione e provocando necrosi da rigetto superficiale.
L'aconito (Wolfsbane) agisce invece sul sistema nervoso autonomo, scatenando aritmie e paralisi morfologica temporanea. Entrambe le sostanze sono severamente vietate nel perimetro del campus universitario, salvo permessi speciali del DMHA per munizioni da contenimento.`)
});

succEntries.push({
  title: 'SUCC: Biologia dei Beastwere & Fisiologia Inversa',
  type: 'lore/concept',
  keys: ['Beastweres SUCC', 'mutaforma inversi', 'reverse shifters SUCC', 'true form biology'],
  content: sanitizeText(`I Beastweres costituiscono una rara categoria biologica in cui il corpo naturale primario e quello di un animale sapiente, capace di proiettare una forma umanoide o demi-umana per periodi limitati.
Il mantenimento della forma umana comporta un consumo continuo della riserva di trasformazione cellulare.
Negli ambienti universitari del SUCC, i Beastweres sono tutelati dal diritto al riposo somatico, con aree studio e stalli di decompressione dove possono risiedere nella propria forma biologica originaria senza penalita o discriminazioni.`)
});

succEntries.push({
  title: 'SUCC: Il Diritto della Vera Forma (Right of True Form)',
  type: 'lore/concept',
  keys: ['Right of True Form SUCC', 'diritto vera forma', 'personhood beastwere', 'normativa forma animale'],
  content: sanitizeText(`Principio giuridico recepito dal Senato Accademico del SUCC in accordo con le direttive federali sul sovrannaturale.
Ogni creatura o mutaforma, inclusi i Beastweres e i demi-umani ad alta percentuale animale, e riconosciuta come soggetto di diritto a pieno titolo indipendentemente dalla forma assunta.
E formalmente vietato imporre l'aspetto umanoide durante esami, riunioni accademiche o lezioni teoriche, purche la comunicazione cognitiva o telepatica sia garantita.`)
});

succEntries.push({
  title: 'SUCC: Riserva di Trasformazione & Decompressione Morfologica',
  type: 'lore/concept',
  keys: ['transformation reserve SUCC', 'riserva morfologica', 'decompressione somatica SUCC'],
  content: sanitizeText(`La riserva di trasformazione e l'energia bio-eterica accumulata nel fegato e nei tessuti connettivi dai mutaforma non nativi della forma umana.
Quando la riserva scende al di sotto della soglia di sicurezza, il soggetto manifesta tremori, perdita di controllo dei tratti facciali e ritorno involontario alla forma ancestrale.
Le infermerie del campus sono dotate di baccelli rigenerativi con saturazione di ioni negativi per accelerare il ripristino della riserva entro 4 ore.`)
});

succEntries.push({
  title: 'SUCC: Istinto Animale, Stress Accademico & Soppressione',
  type: 'lore/concept',
  keys: ['istinto therianthrope SUCC', 'stress esami mutaforma', 'impulso predatore SUCC'],
  content: sanitizeText(`L'istinto animale nei mutaforma non e un'entita separata, ma uno strato profondo di percezione sensoriale e riflessi primordiali.
I periodi di sessione d'esami e forte privazione di sonno possono abbassare i freni inibitori corticali, favorendo l'emergere di ringhi, dilatazione pupillare e postura di sfida nei corridoi.
Il SUCC incoraggia percorsi di meditazione runica e allenamenti fisici intensi nei sotterranei della palestra per scaricare la pressione istintuale senza incidenti.`)
});

succEntries.push({
  title: 'SUCC: Eredita di Sangue & Sviluppo Biologico nei Giovani Licantropi',
  type: 'lore/concept',
  keys: ['eredita licantropa SUCC', 'sviluppo biologico shifters', 'adolescenza mutaforma SUCC'],
  content: sanitizeText(`Lo sviluppo biologico dei mutaforma ereditari vede una fase critica tra i 13 e i 19 anni, momento in cui il corpo raggiunge la prima maturita fenotipica e si stabilizza la forma ibrida.
Presso la SUCC, gli studenti del primo anno affrontano corsi obbligatori di stabilizzazione del baricentro corporeo e controllo della forza mascellare.
Il supporto medico verifica costantemente la calcificazione ossea durante le trasformazioni rapide per prevenire micro-fratture da torsione articolare.`)
});

succEntries.push({
  title: 'SUCC: Comunicazione Non-Verbale, Orecchie & Coda nei Demi-Umani',
  type: 'lore/concept',
  keys: ['demi-umani anatomia SUCC', 'comunicazione posturale', 'orecchie singole SUCC'],
  content: sanitizeText(`Nel rispetto rigoroso dell'anatomia canonica, i demi-umani del SUCC possiedono un unico paio di orecchie: esclusivamente quelle animali, posizionate sulla sommita del capo.
Il movimento di orecchie e coda funge da canale comunicativo primario, indicando allerta, rispetto gerarchico, fastidio o sottomissione.
Il codice di condotta del campus punisce severamente chi tocca o tira code e padiglioni auricolari senza consenso esplicito, equiparando l'atto a una molestia fisica grave.`)
});

succEntries.push({
  title: 'SUCC: Abbigliamento Elastico & Tessuti a Memoria Morfologica',
  type: 'lore/concept',
  keys: ['abbigliamento mutaforma SUCC', 'tessuti a memoria morfologica', 'divise SUCC shifters'],
  content: sanitizeText(`Per rispondere alle necessita pratiche di studenti e docenti soggetti a cambi di taglia repentini, i laboratori tessili del SUCC e della Douglas Commercial Coalition hanno sviluppato fibre polimeriche a memoria elastica.
Questi tessuti si estendono fino al 400% del volume originario senza lacerarsi durante l'assunzione della forma ibrida, ritraendosi perfettamente al ritorno alla forma base.
Tali uniformi sono obbligatorie durante i tornei sportivi inter-collegiali e le simulazioni di combattimento del DMHA.`)
});

succEntries.push({
  title: 'SUCC: Addestramento al Combattimento Morfologico & Sicurezza',
  type: 'lore/concept',
  keys: ['combattimento morfologico SUCC', 'addestramento shifters SUCC', 'palestra SUCC ring'],
  content: sanitizeText(`L'arena sotterranea della Solarton University ospita corsi avanzati di autodifesa e combattimento ravvicinato per studenti therianthropi e cacciatori.
I ring sono protetti da barriere cinetiche runiche che impediscono la fuoriuscita di schegge ossee o ondate d'urto durante gli scontri tra forme ibride pesanti.
I duelli si svolgono sotto la supervisione di arbitri con licenza di Grado A e medici armati di sedativi a rilascio istantaneo.`)
});

succEntries.push({
  title: 'SUCC: Tradizioni & Cultura dei Lupi Solitari nel Campus',
  type: 'lore/concept',
  keys: ['lupi solitari SUCC', 'lone wolf protocol', 'studenti indipendenti SUCC'],
  content: sanitizeText(`Non tutti gli studenti licantropi appartengono a un branco formale o desiderano affiliarsi alle confraternite della SUCC.
I cosiddetti "lupi solitari" godono di piena tutela da parte della Consulta di Coesistenza, che impedisce ai branchi dominanti di esercitare pressioni territoriali o intimidazioni ferormonali per forzare l'affiliazione.
Gli alloggi della Torre Nord sono riservati specificamente a individui indipendenti desiderosi di neutralita sociale.`)
});

succEntries.push({
  title: 'SUCC: Rituali di Plenilunio nel Parco Naturale del Campus',
  type: 'lore/concept',
  keys: ['rituali plenilunio SUCC', 'parco naturale SUCC', 'full moon campus SUCC'],
  content: sanitizeText(`Nelle tre notti di luna piena di ogni mese, l'estesa area boschiva annessa al campus della Solarton University viene chiusa al traffico civile ed escursionistico.
La riserva e messa a disposizione dei branchi studenteschi per la corsa in forma quadrupede (Full Shift) e per i canti territoriali, permettendo di sfogare l'energia lunare senza infrangere la quiete urbana della citta di Solarton.`)
});

succEntries.push({
  title: 'SUCC: Servizi di Supporto Psicologico & Integrazione Morfologica',
  type: 'lore/concept',
  keys: ['supporto psicologico SUCC', 'consulenza specie SUCC', 'terapia mutaforma'],
  content: sanitizeText(`Il centro di salute mentale del SUCC offre consulenza specialistica per studenti che affrontano la dissonanza tra identita umana e pulsioni animali.
I terapeuti, appartenenti sia alla specie umana che demi-umana, trattano i disordini da dissociazione corporea, il panico da prima trasformazione e l'ansia sociale da marcatura olfattiva, garantendo la riservatezza assoluta delle cartelle cliniche.`)
});

// B. Ordinamento Accademico & Vita Campus (12 voci)
succEntries.push({
  title: 'SUCC: Statuto di Santuario Accademico & Immunità Territoriale',
  type: 'lore/concept',
  keys: ['santuario accademico SUCC', 'immunita territoriale SUCC', 'sanctuary ground SUCC'],
  content: sanitizeText(`Fondata sui principi del Trattato di Coesistenza della California Centrale, la Solarton University e riconosciuta legalmente come territorio di santuario neutrale.
All'interno del perimetro universitario sono sospese le faide tra casate pureblood, le rivendicazioni territoriali dei branchi esterni e gli arresti preventivi ordinari delle forze di polizia prive di mandato speciale del DMHA.
La violazione della tregua di santuario comporta l'espulsione immediata e la revoca dello status civile protetto.`)
});

succEntries.push({
  title: 'SUCC: Codice di Condotta per la Convivenza Inter-Specie',
  type: 'lore/concept',
  keys: ['codice condotta SUCC', 'regolamento inter-specie SUCC', 'disciplina studenti SUCC'],
  content: sanitizeText(`Il regolamento disciplinare disciplina i rapporti quotidiani tra umani, demi-umani, vampiri, fae e shifters.
Sono severamente proibiti l'uso offensivo del fascino sovrannaturale (charm/glamour), l'intimidazione tramite il Comando Alpha verbale, il prelievo ematico non autorizzato e la diffusione di odori di minaccia nei luoghi pubblici.
Le sanzioni spaziano dallo svolgimento di ore di servizio sociale per la manutenzione delle barriere runiche fino alla sospensione accademica.`)
});

succEntries.push({
  title: 'SUCC: Rete Digitale Studentesca & Portale SUCCbook',
  type: 'lore/concept',
  keys: ['SUCCbook', 'rete digitale SUCC', 'tecnologia campus SUCC', 'student network SUCC'],
  content: sanitizeText(`L'infrastruttura digitale del campus unisce moderne tecnologie informatiche a crittografia anti-divinazione.
La piattaforma ufficiale SUCCbook permette agli studenti di consultare orari, voti, mercati di scambio di materiali alchemici e forum di discussione tra specie.
I server sono dotati di filtri che bloccano la geolocalizzazione automatica dei membri durante le notti di plenilunio per tutelare la privacy e la sicurezza delle identita sovrannaturali.`)
});

succEntries.push({
  title: 'SUCC: Struttura Didattica & Crediti Formativi Magico-Scientifici',
  type: 'lore/concept',
  keys: ['curriculum SUCC', 'crediti formativi SUCC', 'corsi didattici SUCC'],
  content: sanitizeText(`L'offerta formativa del SUCC combina corsi accademici standard (Giurisprudenza, Economia, Ingegneria, Lettere) con discipline applicate al mondo sovrannaturale (Balistica Runica, Tossicologia Comparata, Teoria delle Barriere, Diritto Inter-Specie).
Il conseguimento della laurea richiede un minimo di 120 CFU complessivi, comprendenti tirocini operativi presso la Douglas Commercial Coalition o la Gilda dei Cacciatori del DMHA.`)
});

succEntries.push({
  title: 'SUCC: Calendario Accademico & Sessioni Straordinarie di Plenilunio',
  type: 'lore/concept',
  keys: ['calendario accademico SUCC', 'sessioni esami plenilunio', 'orari SUCC'],
  content: sanitizeText(`L'anno accademico si articola su due semestri standard, ma integra un calendario flessibile per rispettare i cicli biologici degli iscritti.
Durante la settimana centrale di luna piena e nelle festivita del Solstizio, gli appelli d'esame scritti per studenti licantropi e shifters sono sospesi o posticipati a sessioni di recupero dedicate, evitando sovrapposizioni con l'elevata reattivita ormonale.`)
});

succEntries.push({
  title: 'SUCC: Club Studenteschi, Confraternite & Associazioni di Specie',
  type: 'lore/concept',
  keys: ['club studenteschi SUCC', 'confraternite SUCC', 'frat sorority SUCC', 'Greek life SUCC'],
  content: sanitizeText(`La vita extracurricolare della SUCC e animata da numerose organizzazioni studentesche riconosciute.
Tra queste spiccano le confraternite atletiche tradizionali come i SUCC Bulls (polo licantropo e demi-umano da mischia) e i SUCC Bears, i circoli culturali di botanica arcana, l'Anime Club e la Societa Escursionistica Bigfeet.
Tutti i club devono presentare bilanci trasparenti e rispettare le quote di inclusione inter-specie stabilite dal consiglio studentesco.`)
});

succEntries.push({
  title: 'SUCC: Assistenza Sanitaria & Farmacia d\'Ateneo Multi-Specie',
  type: 'lore/concept',
  keys: ['farmacia SUCC', 'clinica universitaria SUCC', 'medical ward SUCC'],
  content: sanitizeText(`La clinica universitaria di Solarton opera in collaborazione diretta con la divisione farmaceutica della DCC.
Dispone di reparti specializzati per la cura di ferite da morso, traumi muscolari da ipertrofia repentina e intossicazioni da reagenti alchemici.
La farmacia interna distribuisce soppressori ferormonali, sieri nutritivi ad alto contenuto ferrico e unguenti balsamici a base di radice lunare con prescrizione accademica a costo agevolato.`)
});

succEntries.push({
  title: 'SUCC: Sicurezza del Campus & Pattuglie Ausiliarie della Gilda',
  type: 'lore/concept',
  keys: ['sicurezza campus SUCC', 'pattuglie SUCC', 'guardie campus Solarton'],
  content: sanitizeText(`La vigilanza all'interno del perimetro universitario e affidata a un corpo misto formato da guardie giurate accademiche e cacciatori ausiliari autorizzati dal DMHA.
I punti di accesso principali sono dotati di varchi con sensori biometrici e magici in grado di rilevare la presenza di squarci non autorizzati, armi ad argento puro o artefatti maledetti.
In caso di allarme rosso, scattano paratie blindate a tenuta stagna che isolano i singoli blocchi residenziali.`)
});

succEntries.push({
  title: 'SUCC: Alloggi Differenziati & Moduli Residenziali Rinforzati',
  type: 'lore/concept',
  keys: ['alloggi SUCC', 'dormitori campus SUCC', 'moduli residenziali rinforzati'],
  content: sanitizeText(`I dormitori del campus (Apollo, Artemis, Wyrm Dormitories e complessi confraternite) sono progettati tenendo conto delle peculiarita dimensionali e fisiche dei residenti.
Le camere destinate a shifters e minotauri presentano pareti fonoassorbenti ad alta densita, porte rinforzate in lega di titanio e telai letto a portata maggiorata.
I sistemi di aerazione includono filtri al carbone attivo per la dispersione controllata di scie olfattive durante i picchi biologici.`)
});

succEntries.push({
  title: 'SUCC: Tirocini Curricolari & Relazioni con la Citta di Solarton',
  type: 'lore/concept',
  keys: ['tirocini SUCC', 'stage aziendali Solarton', 'career center SUCC'],
  content: sanitizeText(`L'ufficio stage del SUCC coordina tirocini professionalizzanti con le realta industriali, sanitarie e investigative dell'area metropolitana.
Gli studenti piu meritevoli possono accedere a percorsi sul campo presso gli stabilimenti della Douglas Commercial Coalition, i laboratori biotecnologici della Verve o i reparti di ricognizione urbana del DMHA, maturando crediti validi per l'abilitazione alle carriere sovrannaturali ufficiali.`)
});

succEntries.push({
  title: 'SUCC: Protocolli per Visitatori & Delegazioni Esterne',
  type: 'lore/concept',
  keys: ['visitatori SUCC', 'delegazioni campus', 'protocolli accesso SUCC'],
  content: sanitizeText(`L'ingresso di ospiti civili, diplomatici di casata o inviati delle comunita sovrannaturali esterne richiede la registrazione preventiva presso la Portineria Centrale.
Ai visitatori viene rilasciato un pass temporaneo dotato di circuito di tracciamento passivo, attivo unicamente perimetralmente per garantire che non accedano accidentalmente a laboratori di bio-contenimento o stadi di combattimento non vigilati.`)
});

succEntries.push({
  title: 'SUCC: Biblioteca Centrale & Sezione Testi Proibiti',
  type: 'lore/concept',
  keys: ['biblioteca SUCC', 'testi proibiti SUCC', 'grimoires SUCC archive'],
  content: sanitizeText(`La Biblioteca della Solarton University custodisce oltre centomila volumi di letteratura ordinaria e arcanistica.
L'accesso alla Sezione Riservata (Grangia Runica Sotterranea) e limitato a docenti e studenti laureandi muniti di autorizzazione congiunta del Decano e del delegato del DMHA.
I testi conservati in quest'area includono trattati su squarci dimensionali, grimori vincolati da sigilli di sangue e registri storici di epoche precedenti al Trattato di Coesistenza.`)
});

// C. Umani Dotati & Scienze Arcane (8 voci)
succEntries.push({
  title: 'SUCC: Fenomenologia del Risveglio nei Giovani Umani',
  type: 'lore/concept',
  keys: ['risveglio poteri SUCC', 'powered humans SUCC', 'awakening human magic'],
  content: sanitizeText(`Gli studenti umani che manifestano doti magiche o extrasensoriali rientrano nella categoria degli Umani Risvegliati.
Il risveglio avviene tipicamente durante la puberta o in risposta a traumi emotivi e contatti prolungati con anomalie energetiche.
La SUCC fornisce percorsi di accoglienza e monitoraggio per evitare che un risveglio incontrollato causi incendi spontanei, campi cinetici instabili o incidenti telecinetici nelle aule comuni.`)
});

succEntries.push({
  title: 'SUCC: Tassonomia delle Abilita Psichiche ed Elementali',
  type: 'lore/concept',
  keys: ['abilita psichiche SUCC', 'elemental powers SUCC', 'classificazione magia SUCC'],
  content: sanitizeText(`Il Dipartimento di Parapsicologia classifica i poteri umani in quattro branche operative principali:
Manipolazione Cinetico-Elementale (fuoco, gelo, elettricita, vettori fisici), Percezione Extrasensoriale e Telepatia (lettura emotiva, chiaroveggenza locale), Trasmutazione Materica (alterazione delle proprieta degli oggetti) e Portali Spazio-Temporali a corto raggio.
Ogni studente impara a riconoscere il raggio d'azione efficace e le condizioni di sicurezza per l'utilizzo delle proprie capacita.`)
});

succEntries.push({
  title: 'SUCC: Costi Metabolici, Termoregolazione & Sforzo Arcano',
  type: 'lore/concept',
  keys: ['costi metabolici magia', 'burnout magico SUCC', 'sforzo arcano umani'],
  content: sanitizeText(`L'uso prolungato di capacita arcane negli esseri umani non e privo di conseguenze organiche, poiche il corpo funge da conduttore eterico.
Un pirocineta sperimenta un rapido calo della temperatura corporea e disidratazione massiccia, un criocinetico rischia ipotermia periferica, mentre i telecineti subiscono forti emicranie da sovraccarico della corteccia prefrontale.
Le linee guida del SUCC impongono pause obbligatorie e assunzione di integratori di elettroliti arricchiti dopo ogni sessione di canalizzazione.`)
});

succEntries.push({
  title: 'SUCC: Integrazione Sociale tra Umani Dotati e Non Dotati',
  type: 'lore/concept',
  keys: ['integrazione umani SUCC', 'uguaglianza studenti SUCC', 'social dynamics powers'],
  content: sanitizeText(`A differenza delle societa segregate, la Solarton University promuove l'interazione paritaria tra studenti umani privi di poteri e individui dotati di abilita straordinarie.
I corsi di sociologia applicata studiano le dinamiche di potere per evitare complessi di superiorita o ghettizzazioni.
La politica di ateneo premia la cooperazione interdisciplinare, incoraggiando team misti composti da ingegneri ordinari, maghi e atleti mutaforma per la risoluzione di progetti complessi.`)
});

succEntries.push({
  title: 'SUCC: Discipline di Schermatura Psichica & Difesa Personale',
  type: 'lore/concept',
  keys: ['schermatura psichica SUCC', 'mental warding SUCC', 'difesa mentale studenti'],
  content: sanitizeText(`Laboratorio propedeutico obbligatorio per tutti gli studenti umani iscritti al campus.
Insegna tecniche di concentrazione mentale e chiusura della barriera aurica per proteggersi da intrusioni empatiche, suggestioni di sirene, manipolazioni da incubi e incanti illusori minori.
Gli studenti imparano a creare un punto focale interiore in grado di resistere a pressioni esterne senza l'ausilio di talismani protettivi.`)
});

succEntries.push({
  title: 'SUCC: Gestione delle Anomalie & Risvegli Traumatici',
  type: 'lore/concept',
  keys: ['anomalie magiche SUCC', 'risvegli traumatici campus', 'reparto emergenza arcana'],
  content: sanitizeText(`Unita d'intervento rapido formata da docenti di arcanistica e psicologi clinici, attiva 24 ore su 24 per gestire emergenze in cui uno studente perde il controllo delle proprie emissioni magiche.
La procedura prevede il confinamento della zona mediante sigilli runici temporanei, la sedazione dolce del soggetto e il successivo inserimento in percorsi di rieducazione neuromuscolare prima del reintegro nei corsi accademici.`)
});

succEntries.push({
  title: 'SUCC: Laboratori di Teoria Runica & Incantamento Applicato',
  type: 'lore/concept',
  keys: ['teoria runica SUCC', 'laboratori incantamento SUCC', 'runic lab Solarton'],
  content: sanitizeText(`Struttura ad alta sicurezza situata nel polo scientifico ovest del campus.
Gli studenti sperimentano l'incisione di matrici runiche nordiche e simboli geometrici protettivi su materiali metallici e compositi.
Tutti i banchi di lavoro sono collegati a terra tramite cavi d'argento e quarzo per scaricare in sicurezza eventuali picchi di mana instabile generati da errori di tracciamento.`)
});

succEntries.push({
  title: 'SUCC: Dipartimento di De-escalation Magica & Mediazione di Crisi',
  type: 'lore/concept',
  keys: ['de-escalation magica SUCC', 'mediazione crisi SUCC', 'arbitrato accademico'],
  content: sanitizeText(`Organo di mediazione e risoluzione pacifica dei conflitti all'interno del corpo studentesco.
Interviene in caso di dispute territoriali tra branchi, liti tra studenti umani e demi-umani o incidenti derivanti da malintesi culturali o olfattivi.
I mediatori utilizzano tecniche di colloquio neutro e, in rari casi, sigilli di mutismo temporaneo per ristabilire la calma prima di deferire i soggetti alla Commissione Disciplinare.`)
});

// -------------------------------------------------------------
// 2. GENERAZIONE DELLE 38 VOCI DMHA (DA AEGIS CITY HUNTERS)
// -------------------------------------------------------------
const dmhaEntries = [];

// A. Dotazione, Armamenti & Sistemi di Caccia (10 voci)
dmhaEntries.push({
  title: 'DMHA: Sistemi d\'Armamento Reliquia (Armi Vincolate / Messors)',
  type: 'item',
  keys: ['Messors DMHA', 'armi vincolate DMHA', 'reliquie animiche', 'soul-bound weapons'],
  content: sanitizeText(`I Messors sono antichi artefatti bellici o armi ad alta tecnologia runica capaci di legarsi direttamente all'impronta animica e metabolica dell'operatore.
Una volta completato il rito di sintonia, l'arma risponde unicamente al tocco del proprio custode, amplificandone la velocita di reazione e infondendo i colpi con frequenze letali per minacce biologiche ad alta rigenerazione.
La DMHA censisce rigorosamente ogni arma di classe Messor in circolazione, assegnandone la custodia solo a cacciatori veterani di Grado A o superiore.`)
});

dmhaEntries.push({
  title: 'DMHA: Generatori Portatili di Barriera & Dissuasione Mana (Mana Fields)',
  type: 'item',
  keys: ['Mana Field DMHA', 'generatori barriera DMHA', 'repulsion field DMHA', 'barriere cinetiche'],
  content: sanitizeText(`Dispositivi tattici di contenimento utilizzati dalle squadre di caccia per isolare le zone d'ingaggio in ambito urbano.
Attivando il generatore, si crea un campo repulsivo sferico che impedisce alle entita sovrannaturali di fuggire tra i civili e schermando l'area visiva e sonora dall'esterno.
Il campo consuma cartucce di etere compresso e puo resistere a impatti cinetici di Classe 3 per un massimo di quarantacinque minuti continui.`)
});

dmhaEntries.push({
  title: 'DMHA: Dottrina del Velo & Protocolli di Occultamento Sovrannaturale',
  type: 'lore/concept',
  keys: ['Il Velo DMHA', 'dottrina occultamento', 'The Veil protocol', 'censura sovrannaturale'],
  content: sanitizeText(`Principio cardine che regola l'operato del Department of Monster and Human Affairs e delle forze dell'ordine consociate.
Il Velo rappresenta l'insieme di procedure operative, depistaggi mediatici e barriere magiche mirate a mantenere la maggioranza della popolazione ignara della reale scala delle minacce sovrannaturali.
Eventi di breccia pubblica comportano l'intervento immediato di specialisti della memoria e squadre di bonifica per prevenire panico di massa e reazioni isteriche civili.`)
});

dmhaEntries.push({
  title: 'DMHA: Equipaggiamento d\'Assalto per Operativi di Grado S & A',
  type: 'item',
  keys: ['equipaggiamento cacciatori DMHA', 'assalto grado S DMHA', 'tuta tattica caccia'],
  content: sanitizeText(`Dotazione standard fornita ai cacciatori autorizzati per missioni di Classe Catastrofe.
Comprende armature composite rinforzate con trame di seta di drider e polimeri balistici anti-morso, visori con spettrometro per la rilevazione di tracce eteriche e firme termiche di creature invisibili, granate a dispersione di aconito purificato e dosatori automatici di stimolanti metabolici per resistere all'affaticamento prolungato.`)
});

dmhaEntries.push({
  title: 'DMHA: Munizionamento Argentato Silver-Hollowpoint',
  type: 'item',
  keys: ['Silver-Hollowpoint DMHA', 'proiettili argento caccia', 'munizioni argentate DMHA'],
  content: sanitizeText(`Munizioni balistiche calibro regolamentare prodotte sotto licenza congiunta DCC e DMHA.
Il nucleo in piombo e placcato con uno strato elettrochimico di argento puro al 99%, intagliato con canaline a espansione controllata.
All'impatto con tessuti rigeneranti di lupi feroci o mostri infetti, la camiciatura si frammenta rilasciando particelle d'argento micronizzate che causano shock cellulare istantaneo, bloccando la rigenerazione biologica.`)
});

dmhaEntries.push({
  title: 'DMHA: Lame Mana-Conductive & Sigilli Runici da Trincea',
  type: 'item',
  keys: ['lame mana-conductive DMHA', 'armi bianche caccia', 'spade runiche cacciatori'],
  content: sanitizeText(`Armi bianche da combattimento ravvicinato realizzate in acciaio forgiato e vanadio, arricchite con filamenti di rame arcanico lungo la spina della lama.
Consentono al cacciatore di scaricare la propria energia vitale o impulsi di mana durante l'affondo, recidendo carapaci chitinosi, membrane eteriche e barriere spettrali altrimenti immuni alle ordinarie armi da fuoco.`)
});

dmhaEntries.push({
  title: 'DMHA: Visori Spettrali & Tracciatori di Squarcio Classe 1 e 2',
  type: 'item',
  keys: ['visori spettrali DMHA', 'tracciatori squarcio', 'spectral goggles DMHA'],
  content: sanitizeText(`Dispositivi optoelettronici montati su elmetto o a maschera facciale.
Sfruttano cristalli piezo-eterici per convertire le micro-oscillazioni dimensionali in immagini termografiche a colori falsi, permettendo al personale operativo di individuare micro-fratture nel tessuto dello spazio, fumo di spettri incorporei e residui di sangue demoniaco non visibili all'occhio umano.`)
});

dmhaEntries.push({
  title: 'DMHA: Manette a Densita Variabile & Collari di Blocco Morfologico',
  type: 'item',
  keys: ['manette densita variabile DMHA', 'collari blocco morfologico', 'contenimento shifters'],
  content: sanitizeText(`Sistemi di ritenzione ad alta tecnologia utilizzati per l'arresto e il trasporto di mutaforma e criminali therianthropi.
Le manette regolano automaticamente la propria circonferenza e pressione mediante micro-attuatori pneumatici quando rilevano l'espansione muscolare del prigioniero.
Il collare emette impulsi a frequenza costante che disturbano la corteccia cerebrale, inibendo l'avvio della sequenza di trasformazione biologica.`)
});

dmhaEntries.push({
  title: 'DMHA: Spray Neutralizzante ad Aconito & Solventi Antimagici',
  type: 'item',
  keys: ['spray neutralizzante DMHA', 'solvente antimagico', 'aconito spray DMHA'],
  content: sanitizeText(`Nebulizzatori portatili ad alta pressione destinati alle pattuglie di primo intervento.
Emettono una nube a saturazione immediata contenente alcaloidi estratti da aconito e sali disperdenti di berillio.
Lo spray provoca irritazione acuta delle vie respiratorie nei mutaforma e dissipa all'istante formazioni di mana gassoso o barriere elementali di basso livello, offrendo tempo vitale per la messa in sicurezza dei civili.`)
});

dmhaEntries.push({
  title: 'DMHA: Manuale Tascabile dei Protocolli di De-escalation Urbana',
  type: 'item',
  keys: ['manuale DMHA', 'protocolli de-escalation DMHA', 'codice ingaggio caccia'],
  content: sanitizeText(`Documento operativo distribuito a ogni matricola della Gilda dei Cacciatori e agli agenti di polizia distrettuale.
Elenca i codici di ingaggio a sette livelli, i protocolli di comunicazione verbale con capibranco territoriali, le cautele olfattive per non scatenare aggressioni preventive e le tabelle di responsabilita civile per danni collaterali durante gli scontri urbani.`)
});

// B. Bestiario, Anomalie & Minacce di Caccia (12 voci)
dmhaEntries.push({
  title: 'DMHA: Bestiario Classificato & Tracciamento Entita Ostili',
  type: 'creature',
  keys: ['Bestiario DMHA', 'Book of Monsters DMHA', 'classificazione mostri', 'monster registry'],
  content: sanitizeText(`Archivio centrale costantemente aggiornato dalla Commissione Scientifica del DMHA.
Registra ogni specie, aberrazione genetica, parassita dimensionale e creatura folkloristica che manifesti ostilita attiva verso la popolazione civile.
Ogni scheda include dettagli su habitat prevalente, raggio sensoriale, punti deboli fisiologici, grado di letalita stimato (da Minaccia Verde a Catastrofe Nera) e valore delle taglie ufficiali corrisposte ai cacciatori.`)
});

dmhaEntries.push({
  title: 'DMHA: Classificazione Vilitanos & Predatori di Confine',
  type: 'creature',
  keys: ['Vilitanos DMHA', 'predatori di confine', 'mostri folklore DMHA'],
  content: sanitizeText(`Creature mostruose originate da leggende e folklore rurale, dotate di rapida capacita mimetica e spiccata predilezione per la caccia notturna ai margini dei centri urbani.
I Vilitanos possiedono un'epidermide cheratinizzata resistente ai piccoli calibri e tendono a cacciare in coppie coordinate.
La dottrina DMHA prescrive l'uso di munizioni ad alto impatto cinetico o frecce incendiarie runiche per impedirne il rintanamento nel sottosuolo.`)
});

dmhaEntries.push({
  title: 'DMHA: Fenomenologia delle Possessioni & Infestazioni Spettrali',
  type: 'lore/concept',
  keys: ['possessioni DMHA', 'infestazioni spettrali', 'poltergeist DMHA', 'spettri contenimento'],
  content: sanitizeText(`Le entita incorporee, inclusi poltergeist furiosi e spiriti legati a traumi mortali irrisolti, non possono essere eliminate con proiettili tradizionali.
Il protocollo della Gilda prevede l'uso di barriere al sale consacrato per confinare l'area e la successiva applicazione di lame mana-conductive per disperdere il nucleo eterico dello spirito.
Nei casi di possessione di oggetti inanimati o manichini, l'obiettivo prioritario e la distruzione del recipiente focale.`)
});

dmhaEntries.push({
  title: 'DMHA: Protocollo di Contenimento per Culti Fanatici Sovrannaturali',
  type: 'lore/concept',
  keys: ['culti fanatici DMHA', 'sette sovrannaturali', 'contenimento culti DMHA'],
  content: sanitizeText(`Linee guida d'intervento per neutralizzare congreghe e organizzazioni esoteriche clandestine che praticano sacrifici o tentano l'apertura forzata di varchi verso altre dimensioni.
Le operazioni contro i culti prevedono l'infiltrazione preliminare, l'accerchiamento con campi di repulsione mana e l'arresto immediato dei cerimonieri prima del completamento dell'invocazione.`)
});

dmhaEntries.push({
  title: 'DMHA: Aberrazioni Parassitarie & Infezioni da Miasma Eterico',
  type: 'creature',
  keys: ['infezioni miasma DMHA', 'parassiti eterici', 'aberrazioni squarcio'],
  content: sanitizeText(`Organismi microscopici o larvali che si sviluppano in prossimita di squarci dimensionali aperti per oltre 72 ore.
I parassiti penetrano attraverso il flusso sanguigno o l'inalazione di vapori eterici, causando mutazioni somatiche dolorose, perdita del controllo cognitivo e aggressivita incontrollabile.
Il personale della Gilda contaminato viene posto in quarantena ermetica presso il reparto isolamento della DCC.`)
});

dmhaEntries.push({
  title: 'DMHA: Entita Chimere & Ibridi da Laboratorio Clandestino',
  type: 'creature',
  keys: ['chimere DMHA', 'ibridi clandestini', 'bio-armi sovrannaturali'],
  content: sanitizeText(`Risultato di esperimenti genetici illegali condotti da corporazioni corrotte o cabale di maghi rinnegati che innestano tratti di piu specie mostruose su un unico ospite.
Le chimere mostrano spesso organi vitali duplicati e imprevedibili resistenze elementali.
Il loro abbattimento richiede l'impiego congiunto di cacciatori ad armamento pesante e specialisti dell'incantamento.`)
});

dmhaEntries.push({
  title: 'DMHA: Entita Criptidi & Creature dell\'Ombra',
  type: 'creature',
  keys: ['criptidi DMHA', 'creature ombra', 'shadow entities DMHA'],
  content: sanitizeText(`Manifestazioni viventi composte interamente da materia d'ombra condensata, capaci di fondersi con gli angoli bui degli edifici e ignorare le superfici solide.
L'unico fattore letale costante e costituito da proiezioni di luce polarizzata ad alta intensita e rune consacrate al fuoco solare.
Le pattuglie notturne portano sempre torce tattiche al fosforo per contrastarne l'avvicinamento furtivo.`)
});

dmhaEntries.push({
  title: 'DMHA: Demoni Minori & Furie dei Bassifondi',
  type: 'creature',
  keys: ['demoni minori DMHA', 'furie bassifondi', 'demoni urbani DMHA'],
  content: sanitizeText(`Creature eteriche originate dai piani inferiori che si insediano nelle fognature, nei tunnel abbandonati e nelle zone industriali degradate di Solarton.
Nutrendosi delle vibrazioni di disperazione e violenza, manifestano artigli capaci di fondere il metallo e pelle ricoperta di zolfo.
La loro neutralizzazione richiede un fuoco incrociato continuo per impedirne la combustione spontanea di rappresaglia.`)
});

dmhaEntries.push({
  title: 'DMHA: Yokai & Spiriti Predatori della Tradizione Orientale',
  type: 'creature',
  keys: ['Yokai DMHA', 'spiriti orientali DMHA', 'kitsune corrotte'],
  content: sanitizeText(`Entita spiritiche legate a santuari dimenticati o tradizioni folkloristiche d'oltremare.
Se pacifici, sono protetti dal trattato di residenza civile, ma quando vengono corrotti da miasmi urbani manifestano illusioni ipnotiche complesse e attacchi psionici.
L'ingaggio richiede l'uso di specchi di bronzo arcanico per disperdere le immagini illusorie prima del colpo decisivo.`)
});

dmhaEntries.push({
  title: 'DMHA: Non-Morti Autonomi & Risvegli Cimiteriali',
  type: 'creature',
  keys: ['non-morti DMHA', 'risvegli cimiteriali', 'ghoul urbani DMHA'],
  content: sanitizeText(`Cadaveri rianimati da correnti di necromanzia residua o da contaminazioni chimiche clandestine.
A differenza dei vampiri intelligenti, questi costrutti agiscono unicamente guidati da una fame cieca per tessuti organici freschi.
La procedura operativa prescrive la decapitazione e l'incenerimento totale delle spoglie tramite cariche termiche per prevenire la diffusione di batteri necrotizzanti.`)
});

dmhaEntries.push({
  title: 'DMHA: Drider & Aracnidi di Faglia',
  type: 'creature',
  keys: ['drider DMHA', 'aracnidi faglia', 'ragni giganti caccia'],
  content: sanitizeText(`Creature orripilanti con busto umanoide e addome a otto zampe da ragno colossale, originarie delle cavita geologiche profonde della costa californiana.
Tessono ragnatele con resistenza alla trazione superiore a cavi d'acciaio, cosparse di neurotossine paralizzanti.
Le squadre di sterminio del DMHA utilizzano lanciafiamme tattici a miscela arricchita per bonificare i nidi sotterranei.`)
});

dmhaEntries.push({
  title: 'DMHA: Elementali Fuori Controllo & Fratture di Mana',
  type: 'creature',
  keys: ['elementali DMHA', 'fratture di mana', 'anomalie elementali'],
  content: sanitizeText(`Masse instabili di fuoco, fango, tempesta o magma che prendono forma in corrispondenza di guasti alle centrali a convertitore eterico o incidenti nei laboratori accademici.
Non possiedono cervello o organi bersaglio, ma un nucleo cristallino centrale che deve essere frantumato per interrompere il flusso di materia elementale coesa.`)
});

// C. Divisioni Governative, Fazioni Ombra & Squadre (10 voci)
dmhaEntries.push({
  title: 'DMHA: Crimson Crimes Division (CCD - Sezione Crimini Straordinari)',
  type: 'faction',
  keys: ['CCD DMHA', 'Crimson Crimes Division', 'sezione crimini straordinari'],
  content: sanitizeText(`Divisione d'elite governativa integrata tra la Polizia di Solarton e il Dipartimento DMHA.
La CCD indaga su omicidi rituali, traffico illegale di parti anatomiche sovrannaturali, cospirazioni di sangue tra casate pureblood e incidenti di grave violazione del Velo.
Gli ispettori della CCD hanno facolta di scavalcare le giurisdizioni ordinarie e richiedere il supporto immediato dei cacciatori di Grado S.`)
});

dmhaEntries.push({
  title: 'DMHA: La Societa Balor & Criminalita Organizzata Sovrannaturale',
  type: 'faction',
  keys: ['Societa Balor', 'Balor Society DMHA', 'sindacato Balor'],
  content: sanitizeText(`Vasto cartello clandestino composto da creature sovrannaturali rinnegate, contrabbandieri di aconito e maghi radiati dall'albo.
La Societa Balor gestisce bische clandestine, arene clandestine di combattimento per shifters e traffico di artefatti maledetti nei bassifondi dell'area costiera.
Costituisce uno dei principali bersagli prioritari per le taglie a ricompensa elevata della Gilda.`)
});

dmhaEntries.push({
  title: 'DMHA: Il Culto del Prime Order & Minacce Apocalittiche',
  type: 'faction',
  keys: ['Prime Order DMHA', 'culto Prime Order', 'fanatici apocalittici'],
  content: sanitizeText(`Organizzazione fanatica clandestina devota all'accelerazione del collasso dimensionale e al ritorno delle potenze primordiali pre-umane.
I suoi membri, spesso umani fanatici e ibridi disillusi, operano tramite cellule compartimentate dedite all'acquisto illegale di esplosivi e matrici runiche instabili.
La DMHA considera ogni affiliato al Prime Order come un bersaglio a neutralizzazione autorizzata a vista.`)
});

dmhaEntries.push({
  title: 'DMHA: Compagnia Mercenaria Scarlet Fog',
  type: 'faction',
  keys: ['Scarlet Fog DMHA', 'compagnia Scarlet Fog', 'mercenari caccia'],
  content: sanitizeText(`Compagnia di cacciatori privati e contractors a contratto che opera ai margini della legalita ufficiale.
Rifiutano molti dei vincoli burocratici del DMHA, offrendo i propri servizi a corporazioni minerarie e magnati privati per l'eliminazione sommaria di nidi di mostri o il recupero di reliquie in aree contaminate.
I rapporti tra la Gilda ufficiale e la Scarlet Fog sono tesi, caratterizzati da una tregua armata fondata sulla necessita.`)
});

dmhaEntries.push({
  title: 'DMHA: Agenzia Investigativa Serenson & Rete Ausiliaria Privata',
  type: 'faction',
  keys: ['Agenzia Serenson DMHA', 'SDA detective', 'investigatori privati caccia'],
  content: sanitizeText(`Una delle principali agenzie investigative private con licenza speciale per casi a sfondo sovrannaturale operante tra Solarton e le colline adiacenti.
Fondata da veterani della caccia, collabora come consulente esterno per il DMHA e la Famiglia Douglas, raccogliendo prove su sparizioni misteriose e rintracciando fuggitivi ricercati prima che la situazione degeneri in scontro aperto.`)
});

dmhaEntries.push({
  title: 'DMHA: Confraternita dei Tessitori Ermetici (Hermetic Weavers)',
  type: 'faction',
  keys: ['Hermetic Weavers DMHA', 'tessitori ermetici', 'societa maghi ritualisti'],
  content: sanitizeText(`Confraternita segreta di maghi ritualisti e studiosi di geometria sacra.
Specializzati nella riparazione di barriere dimensionali logorate e nell'ancoraggio di sigilli millenari, operano come consulenti tecnici del DMHA durante le crisi da squarcio su larga scala, fornendo perizie archeologiche e incantesimi di stabilizzazione.`)
});

dmhaEntries.push({
  title: 'DMHA: Divisione di Bonifica Sanitaria & Smaltimento Carcasse',
  type: 'lore/concept',
  keys: ['bonifica sanitaria DMHA', 'smaltimento mostri DMHA', 'pulizia zone scontro'],
  content: sanitizeText(`Reparto operativo logistico che interviene immediatamente al termine di ogni operazione di caccia.
Dotato di tute ermetiche, forni crematori mobili e solventi enzimatrici biologici, il reparto sanifica le strade, incenerisce i resti dei mostri abbattuti e raccoglie campioni per i laboratori tossicologici della DCC, eliminando ogni prova visibile agli occhi civili.`)
});

dmhaEntries.push({
  title: 'DMHA: Sezione Investigativa Crimini di Sangue & Antivampirismo',
  type: 'lore/concept',
  keys: ['crimini di sangue DMHA', 'antivampirismo DMHA', 'sezione sangue'],
  content: sanitizeText(`Unita specializzata nella vigilanza sulla comunita vampirica e sul mercato delle sacche ematiche sintetizzate.
Verifica che i dispensari autorizzati non vengano sabotati e persegue con durezza i vampiri non registrati che praticano il dissanguamento illegale di civili o la creazione clandestina di infetti privi di senno.`)
});

dmhaEntries.push({
  title: 'DMHA: Ufficio Taglie, Finanza & Riscossione Crediti di Caccia',
  type: 'lore/concept',
  keys: ['ufficio taglie DMHA', 'crediti caccia DMHA', 'bounty board DMHA'],
  content: sanitizeText(`Il centro nevralgico amministrativo dove i cacciatori presentano le prove di eliminazione (nuclei energetici, corni, sacche di veleno) per la convalida delle kill.
L'ufficio accredita i compensi in crediti ufficiali della Gilda sul terminale dello smartphone dell'operatore, trattenendo le quote previdenziali e aggiornando il tasso di successo per l'avanzamento di rango.`)
});

dmhaEntries.push({
  title: 'DMHA: Servizio Relazioni con la Consulta delle Casate Sovrannaturali',
  type: 'lore/concept',
  keys: ['relazioni casate DMHA', 'diplomazia caccia DMHA', 'trattati specie DMHA'],
  content: sanitizeText(`Ufficio diplomatico permanente che mantiene il dialogo quotidiano tra il comando della Gilda e le autorita delle casate tradizionali, tra cui la Douglas Commercial Coalition e il Concilio della Notte.
Evita che operazioni di caccia in periferia sconfinino nei territori ancestrali protetti senza preventivo avviso ai capibranco.`)
});

// D. Operativi Notabili & Registri d'Onore (6 voci)
dmhaEntries.push({
  title: 'DMHA: Registro d\'Onore dei Cacciatori d\'Elite & Maestri di Gilda',
  type: 'lore/concept',
  keys: ['Registro d Onore DMHA', 'maestri di gilda caccia', 'cacciatori elite DMHA'],
  content: sanitizeText(`Albo storico conservato nel quartier generale della Gilda di Solarton, recante i nomi e le imprese dei cacciatori che hanno conseguito oltre cento abbattimenti confermati di Classe Catastrofe.
I veterani registrati godono di immunita civile speciale, accesso ai caveau di armamenti Messor e diritto di voto nelle deliberazioni sulla proclamazione dello stato d'emergenza cittadino.`)
});

dmhaEntries.push({
  title: 'DMHA: Contratti Speciali di Classe Catastrofe (Grado S)',
  type: 'lore/concept',
  keys: ['Contratti Grado S DMHA', 'contratti catastrofe DMHA', 'missioni rango S'],
  content: sanitizeText(`Incarichi di caccia ad altissimo rischio emessi unicamente dal Direttore Generale del DMHA previa autorizzazione prefettizia.
Riguardano la caccia a titani dimensionali, comandanti di squarcio o culti armati con armi di distruzione magica di massa.
I contratti prevedono ricompense a partire da 50.000 crediti e richiedono il dispiegamento di fireteam congiunti composti da almeno tre cacciatori di Grado A o superiore.`)
});

dmhaEntries.push({
  title: 'DMHA: Registro Operativi e Cacciatori Notabili: Squadre d\'Assalto',
  type: 'lore/concept',
  keys: ['operativi notabili DMHA', 'squadre assalto DMHA', 'cacciatori veterani registro'],
  content: sanitizeText(`Scheda informativa generale che compendia i profili e le specializzazioni delle squadre operative storiche della regione.
Censite unita di prima linea specializzate in sfondamento con armi bianche pesanti, tiratori scelti con caricatori antimana e cacciatori ibridi capaci di fondere la fisiologia therianthrope con tattiche paramilitari moderne.`)
});

dmhaEntries.push({
  title: 'DMHA: Registro Operativi e Cacciatori Notabili: Incursori Furtivi',
  type: 'lore/concept',
  keys: ['incursori furtivi DMHA', 'cecchini caccia DMHA', 'ricognitori gilda'],
  content: sanitizeText(`Dossier riservato dedicato ai nuclei di intelligence e ricognizione avanzata della Gilda.
Questi agenti operano in solitaria o a coppie, precedendo le squadre d'assalto per mappare la densita dei nidi di mostri, sabotare i cerchi rituali dei culti ed eliminare sentinelle eteriche mediante fucili di precisione a silenziatore runico.`)
});

dmhaEntries.push({
  title: 'DMHA: Protocolli di Mutuo Soccorso con la Sicurezza Douglas (DCC)',
  type: 'lore/concept',
  keys: ['mutuo soccorso DCC DMHA', 'accordo Douglas caccia', 'collaborazione sicurezza'],
  content: sanitizeText(`Patto di cooperazione strategica tra la divisione di sicurezza privata della DCC e il comando DMHA di Solarton.
In caso di violazione territoriale o minaccia diretta a Blackwood City o alla Villa Douglas, le unita della DCC assumono il coordinamento tattico della difesa, con l'immediata autorizzazione al dispiegamento dei cacciatori affiliati alla famiglia (Alyssa, Noah, Malachia, Jared, Mac).`)
});

dmhaEntries.push({
  title: 'DMHA: Codice d\'Onore & Diritti dei Caduti della Gilda',
  type: 'lore/concept',
  keys: ['codice onore DMHA', 'caduti della gilda', 'pensioni cacciatori DMHA'],
  content: sanitizeText(`Statuto etico che tutela i cacciatori feriti o caduti in servizio durante la protezione della societa civile.
Garantisce indennizzi completi e pensioni privilegiate per i familiari a carico, la sepoltura con onori solenni nel Cimitero Memoriale dei Guardiani del Velo e la custodia perpetua delle armi e reliquie del defunto nel Sancta Sanctorum della Gilda.`)
});

const allNew = [...succEntries, ...dmhaEntries];
console.log(`Totale nuove voci generate: ${allNew.length} (${succEntries.length} SUCC + ${dmhaEntries.length} DMHA).`);

fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/new_succ_dmha_lexicons.json', JSON.stringify(allNew, null, 2), 'utf8');
console.log('File salvato con successo!');
