import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import urllib.request
import json
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

world_id = "_YpX47fNraQFw2dD7TdycJ"
scenario_id = "_2MTWKjxrQPdQVaz9y4Q7H"
location_id = "_aPqjQX8UBNTC9y2tEUdX3"    # Lunar Quad
environment_id = "_38JCUykN4wwRfgGjQyjLr" # SUCC campus
avatar_url = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public"

# Linked character IDs
linked_char_ids = [
    "_t4J9aQNJM36cUKAP4wB4U", # Jasper Svartr Douglas Bloodmoon
    "_QPea6g4Q1QfeYCVHCLMPR", # Erik Ulfr Douglas
    "_T8Ywcr9FEqNf9JxbK6eHP", # Logan Járn Douglas
    "_RDfz7XzTpM23LpPALVXHM", # Malachia Björn Douglas Bloodmoon
    "_zFLUjV8aVxQRAfQxGcAcY", # Noah Loki Douglas Bloodmoon
    "_TbRM3EdxDjHFgqztTbCpL", # Edric Douglas
    "_HEQQbbRFwKdG8QE2Fh1z1", # Wulfnic Báleygr Bloodmoon
    "_zn24784jfcchQ7EwCyAnm", # Mackenzie Sanchez-Rogers
]

# Scene 1: Alyssa POV (FemPOV)
scene_alyssa_text = """=>Narrator:
Il sole della tarda mattinata batte sui prati gremiti del Lunar Quad il 26 agosto 2024, filtrando tra gli stendardi cremisi e oro issati per il Welcome Day della SUCC. Poiché la cerimonia inaugurale è aperta anche ai familiari degli studenti per gli ultimi saluti prima dell'inizio delle lezioni, l'intero clan Douglas-Bloodmoon ha accompagnato sul quad i quattro iscritti all'università: i fratelli maggiori Noah e Malachia insieme ai gemelli matricole Jasper e {{user}}, scortati dal padre Erik, dallo zio Logan e dal cugino tredicenne Edric. Sul palco del padiglione centrale, il Cancelliere Archer Wolfwood è affiancato dai presidi di facoltà mentre i tecnici del suono regolano il microfono d'ottone.

Erik Ulfr Douglas: "Restate uniti quando la folla si disperderà dopo il discorso, e chiamate subito se i guardiani del campus vi danno qualsiasi problema," brontola Erik, la sua alta figura che proietta un'ombra protettiva sul vialetto mentre i suoi occhi ambrati scrutano il prato.

Logan Járn Douglas: "Lasciali respirare, Erik, è l'orientamento universitario, non un assedio," dice Logan con una risata calorosa, posando una mano massiccia sulla spalla di Edric.

Edric Douglas: "Aspetta di vedere quanto è grande la mensa, Jasper! Ma le matricole hanno davvero i pass illimitati anche per la sala giochi dell'Annex?" chiede Edric con entusiasmo, allungando il collo verso l'edificio dell'unione studentesca.

Noah Loki Douglas Bloodmoon: "Il tendone di rappresentanza della KSA sul prato est ha bevande fresche e posti all'ombra riservati per noi quando volete sfuggire al caldo," osserva Noah con eleganza, sistemandosi il revers della giacca di lino su misura.

Malachia Björn Douglas Bloodmoon: "Ho già controllato il perimetro dalla palestra fino a Greek Row. Nessuno darà fastidio alla mia sorellina in questo campus," aggiunge Malachia con tono basso e roca fermezza, incrociando le braccia sul petto.

Accanto a {{user}}, Jasper alza lo sguardo dalla telemetria di rete sul suo datapad; le sue orecchie scure da lupo si orientano verso il cancello principale, un unico paio lupino sulla sommità del capo senza alcuna orecchia umana ai lati della testa. "Le registrazioni delle matricole hanno già mandato in crash il server centrale della biblioteca," mormora Jasper, dando un leggero colpetto di gomito a {{user}}. "Aspetta un secondo. Guarda chi sta varcando l'arco di pietra principale proprio adesso."

=>Narrator:
Il brusio lungo il viale centrale si apre in un'ondata di silenzio stupefatto quando Wulfnic Báleygr Bloodmoon avanza sul Lunar Quad con Zefir Hvitskog al suo fianco. Lo Jarl di Svartúlfr, a milleduecento anni compiuti, sfoggia il suo outfit gag preferito con solenne e fierissimo orgoglio: una t-shirt di cotone nero oversize regalatagli da Jasper che porta stampata sulla schiena, a grandi caratteri bianchi, una lunghissima e fitta lista di Regole per Uscire con Mia Nipote, abbinata a jeans scuri con l'apertura sartoriale per la coda da lupo argentata, pesanti stivali da motociclista con fibbie e un antico torque d'argento ritorto al collo. Accanto a lui, Zefir ha tutto l'aspetto di un giovane ribelle punk sui vent'anni: i suoi capelli bianco-neve sono rasati ai lati in una netta cresta alla moicana e indossa un pesante giubbotto di pelle nera tempestato di borchie d'argento sopra una canotta nera strappata e jeans aderenti, tenendo il fascicolo dell'orientamento piegato in una mano tatuata.

"In fondo non sei mai andato a scuola e tecnicamente sei un ragazzino!" tuona Wulfnic scoppiando in una risata profonda e fragorosa, mentre batte una manata pesante sulla spalla borchiata di Zefir.
"Non fare quella faccia sorpresa, Erik! Per assicurarmi che la nostra piccola Alyssa sia protetta come si deve nel campus, ho deciso di iscrivere anche Zefir all'università. Per la segreteria è un vostro lontano parente appena arrivato dall'Islanda, così giustifichiamo il suo accento marcatamente norreno e la sua poca dimestichezza con l'inglese scritto."

Zefir Hvitskog: "Ridi pure quanto vuoi, mio Jarl, ma se qualche professore pieno di sé mi agita un gessetto sotto il naso, non prometto di lasciarglielo intero," ribatte Zefir con un ghigno sfrontato e vivace, la spavalderia giovanile del vichingo sedicenne che era un tempo che gli brilla negli occhi azzurro ghiaccio come una raffica di vento del Mare del Nord, prima di rivolgere un beffardo saluto a due dita a {{user}} e Jasper.
"Tranquilla, cuginetta. Il tuo parente islandese è ufficialmente una matricola. Indicami chiunque ti guardi storta e sparirà prima che suoni la campanella."

=>Narrator:
Finnegan Novak attraversa il flusso dell'orientamento dal padiglione atletico con il suo giubbotto da varsity dei Bears su una spalla, arrivando insieme a Scarlett Rose e Sierra Cruz. Per evitare che i tre compagni di campus si mettano sul chi vive attorno a un Firstborn, la famiglia presenta subito Zefir con la copertura del lontano cugino appena atterrato dall'Islanda per il suo primo anno. Poiché Zefir ha completamente schermato la sua aura divina da Enigma, ai loro sensi appare come un normale e trasandato licantropo in chiodo di pelle punk, eppure la postura di Finn si irrigidisce immediatamente. Il suo unico paio di orecchie da lupo bianco si appiattisce leggermente sulla sommità del capo, senza alcuna orecchia umana ai lati, mentre un inspiegabile istinto primordiale lo fa sentire stranamente surclassato dal giovane sconosciuto islandese, spingendolo a gonfiare il petto per darsi un tono davanti a {{user}}.

Finnegan Novak: "Ci ho messo venti minuti a seminare gli osservatori vicino all'arena, Alyssa. Il coach mi ha già inserito nel primo blocco di power-play per la prima di campionato, quindi se tuo cugino dall'Islanda vuole vedere come si gioca il vero hockey universitario, posso fargli avere i pass in prima fila," si vanta Finn, appoggiandosi alla balaustra di pietra e flettendo con disinvoltura l'avambraccio mentre si sistema il colletto della varsity.

Sierra Cruz: "Un attimo, fermi tutti, devo assolutamente sapere dove hai preso quel chiodo adesso," interviene Sierra, la sua imponente coda da serpente color arcobaleno che scivola fluida e sinuosa tra le panchine di pietra mentre striscia più vicina a Zefir, i suoi capelli arcobaleno che brillano al sole e le sue scaglie iridescenti che riflettono la luce mentre esamina con invidia genuina le file di pesanti borchie d'argento sui suoi revers. "I dettagli della pelle consumata e quelle punte personalizzate sembrano vintage europeo d'avanguardia. C'è qualche boutique underground a Reykjavik che dovrei conoscere?"

Scarlett Rose: "Devo ammettere che lo stile punk islandese ti dona in modo pericoloso, Zefir," mormora Scarlett con un sorriso malizioso e provocante, le sue ali scure da succubus che fremono appena dietro le sue spalle, i suoi capelli e occhi rosa confetto abbinati alle due corna scarlatte sopra le tempie e la sua coda che ondeggia sinuosa mentre lancia un'occhiata d'intesa a {{user}}. "Benvenuto a Solarton, Zefir. Dato che la tua lettura dell'inglese è ancora arrugginita, mi offro volentieri per qualche lezione privata dopo la cerimonia d'apertura. Dai, Alyssa, Wolfwood sta salendo al podio.\""""

# Scene 2: Jasper POV (MalePOV)
scene_jasper_text = """=>Narrator:
La luce radiosa della tarda mattinata inonda i prati del Lunar Quad il 26 agosto 2024, illuminando gli stendardi cremisi e oro issati per il Welcome Day della SUCC. Poiché la cerimonia inaugurale accoglie le famiglie sul campus per gli ultimi saluti prima delle lezioni, l'intero clan Douglas-Bloodmoon ha accompagnato sul quad i quattro iscritti all'università: i fratelli maggiori Malachia e Noah insieme alle matricole {{user}} e Alyssa, scortati dal padre Erik, dallo zio Logan e dal cugino tredicenne Edric. Sul palco del padiglione centrale, il Cancelliere Archer Wolfwood è fermo davanti al microfono d'ottone a ripassare i suoi appunti, mentre i guardiani del campus guidano centinaia di studenti verso il prato.

Erik Ulfr Douglas: "Tenete aperte le linee di comunicazione dopo il discorso d'apertura, e ricordate che la cena di famiglia della domenica non è facoltativa," brontola Erik, la sua presenza imponente che impone largo rispetto tra gli studenti di passaggio mentre il suo sguardo controlla il perimetro.

Logan Járn Douglas: "Lasciali godersi la prima mattina sul campus, Erik, hanno aspettato tutta l'estate per questo," dice Logan con un sorriso rassicurante, posando una mano pesante sulla spalla di Edric.

Edric Douglas: "Jasper, se hackerate il tabellone dello stadio durante la prima partita dei Bulls, devi assolutamente farmi guardare la diretta dalla tua stanza!" sussurra Edric con un ghigno entusiasta, dondolandosi sui talloni.

Noah Loki Douglas Bloodmoon: "Il padiglione della KSA sul prato est è già allestito se qualcuno di voi desidera bevande fresche lontano dalla folla delle matricole," osserva Noah con impeccabile compostezza, sistemandosi i gemelli dei polsini.

Malachia Björn Douglas Bloodmoon: "Ho già perlustrato Wyrm Hall e Greek Row. Chiunque superi il limite con uno di voi due dovrà risponderne a me," dichiara Malachia con voce ferma, le braccia incrociate sul petto.

Accanto a {{user}}, Alyssa Hvit Douglas Bloodmoon stringe al petto il suo diario erboristico rilegato in pelle; le sue orecchie bianche da lupo si drizzano sulla sommità del capo, un unico paio lupino senza alcuna orecchia umana ai lati della testa, mentre guarda verso l'arco di pietra principale. "Cerca di non infiltrarti nella telemetria dell'amministrazione durante il discorso di Wolfwood, Jasper. Aspetta. Guarda chi è appena entrato sul quad."

=>Narrator:
Un mormorio di incredulità percorre il viale principale quando Wulfnic Báleygr Bloodmoon avanza sul Lunar Quad con Zefir Hvitskog al suo fianco. L'antico Jarl indossa con fierezza regale l'outfit gag che proprio {{user}} gli ha regalato: una t-shirt di cotone nero oversize con una lunghissima e fitta lista di Regole per Uscire con Mia Nipote stampata in bianco sulla schiena, abbinata a jeans scuri con l'apertura per la coda da lupo argentata, pesanti stivali da motociclista e un torque d'argento ritorto al collo. Accanto a lui, Zefir sembra un giovane ribelle punk sui vent'anni: i suoi capelli bianco-neve sono rasati ai lati in una fiera cresta alla moicana e indossa un giubbotto di pelle nera coperto di borchie d'argento sopra una canotta nera strappata e jeans aderenti, con l'orario delle lezioni da matricola infilato tra due dita tatuate.

"In fondo non sei mai andato a scuola e tecnicamente sei un ragazzino!" ruggisce Wulfnic con una risata profonda e tonante, dando una pacca così forte sulla spalla di Zefir da far tintinnare le borchie.
"Ho preso spunto da te, Jasper! Per assicurarmi che Alyssa abbia un'ombra in più a proteggerla nel campus, stamattina ho iscritto anche Zefir all'università. Sui documenti risulta come un vostro lontano parente appena arrivato dall'Islanda, così giustifichiamo il suo marcato accento norreno e la sua poca dimestichezza con l'inglese scritto."

Zefir Hvitskog: "Continua pure a ridere, vecchio, e vediamo chi mi tradurrà questi maledetti programmi dei corsi stasera," ribatte Zefir con un ghigno insolente e vivace, i suoi occhi azzurro ghiaccio accesi dalla spavalderia indomita del guerriero vichingo sedicenne che era e dal brio imprevedibile del vento dei mari del Nord, mentre tocca il revers borchiato verso {{user}} e Alyssa.
"Che ne dici, Svartr? Il tuo nuovo cugino islandese è ufficialmente una matricola universitaria. Basta che non mi chiediate di scrivere un tema, a meno che non lo vogliate inciso sulla cattedra col pugnale."

=>Narrator:
Finnegan Novak attraversa il prato dal complesso atletico nella sua felpa grigia da hockey dei Bears, arrivando insieme a Scarlett Rose e Sierra Cruz giusto in tempo per sentire la famiglia presentare Zefir con la copertura del lontano cugino dall'Islanda per evitare che si mettano sul chi vive. Anche se Zefir ha completamente annullato la sua aura divina da Enigma, sembrando a tutti gli effetti un licantropo qualsiasi in mezzo a centinaia di studenti, l'istinto di Finn avverte comunque un inspiegabile senso di inferiorità davanti a quel ragazzo dalla cresta bianca. Il suo unico paio di orecchie da lupo artico si piega lievemente sulla sommità del capo, senza orecchie umane ai lati, mentre raddrizza le spalle e prova subito a mostrarsi più figo davanti ad Alyssa.

Finnegan Novak: "Bello vederti alla luce del sole, Svartr. Stavo giusto dicendo ad Alyssa che il coach mi ha messo nel primo blocco di power-play, quindi se vostro cugino dall'Islanda vuole vedere cosa significa vera velocità sul ghiaccio, lo metto nella lista VIP," si vanta Finn, infilando i pollici nelle tasche della felpa e assumendo una posa plastica da atleta a beneficio di Alyssa.

Sierra Cruz: "Ferma tutto, devo assolutamente sapere dove hai preso quel giubbotto di pelle adesso," interviene Sierra, strisciando più vicino sulla sua imponente coda da serpente color arcobaleno, le scaglie iridescenti che riflettono il sole e i capelli color arcobaleno che ondeggiano mentre ammira le file di borchie d'argento sulle spalle di Zefir. "Sul serio, nessuno a Solarton lavora la pelle così. Dove l'hai preso in Islanda?"

Scarlett Rose: "Devo ammettere che lo stile da vichingo ribelle ti dona in modo pericoloso, Zefir," mormora Scarlett inclinando la testa così che i suoi capelli rosa confetto sfiorino le corna scarlatte che spuntano sopra le tempie, un lampo malizioso e civettuolo nei suoi occhi rosa confetto mentre flirta con lui prima di lanciare uno sguardo complice a {{user}}. "Se tuo cugino avesse bisogno di una mano per decifrare i manuali in inglese, Jasper, sai dove trovarmi. Dai, venite a sedervi con noi sul prato sud prima che Wolfwood inizi il discorso.\""""

# Scene 3: Choral Pack Scene (AnyPOV)
scene_corale_text = """=>Narrator:
Lunedi 26 agosto 2024, ore 10:00 - Lunar Quad, Campus SUCC, Solarton

Il sole caldo della California splende sul Lunar Quad, facendo scintillare le vetrate gotiche della Basilica Library e gli stendardi cremisi e oro issati per il Welcome Day della Supernatural University of Central California. Il prato e' gremito da migliaia di matricole, studenti senior e famiglie venute da ogni angolo dello stato per la cerimonia d'apertura dell'anno accademico.

Sul vialetto principale in pietra lavica, il clan Douglas-Bloodmoon avanza compatto attirando sguardi di rispetto e soggezione: il patriarca Erik Ulfr Douglas e lo zio Logan affiancano i quattro giovani universitari della famiglia. Noah, impeccabile nel suo completo estivo da senior della KSA; Malachia, imponente e silenzioso con lo sguardo che scansiona metodicamente ogni angolo del campus; e i due gemelli matricole, pronti a iniziare il loro cammino accademico tra aule, confraternite e laboratori arcani. Al loro fianco, il giovane Edric di tredici anni osserva tutto a bocca aperta, mentre sul palco Wolfwood e i decani ultimano i preparativi.

=>Erik:
"Guardatevi le spalle a vicenda e non dimenticate chi siete una volta varcati i cancelli del campus," dice Erik a bassa voce, la sua voce profonda carica di un'autorita' istintiva che zittisce il brusio circostante. "Solarton puo sembrare una citta tranquilla sul mare, ma questo college raccoglie ogni fazione e stirpe della costa."

=>Logan:
"Respira, Erik. Oggi e' un giorno di festa, non un briefing tattico prima di una battuta di caccia," interviene Logan con un sorriso caloroso, stringendo le spalle di Edric. "Questi ragazzi sanno cavarsela meglio di quanto credi."

=>Narrator:
Prima che la conversazione possa proseguire, un mormorio improvviso attraversa la folla vicino all'arco monumentale. L'antico Jarl Wulfnic Baleygr Bloodmoon fa il suo ingresso sul prato a passo sicuro, con una vistosa t-shirt nera con la scritta gag delle regole di famiglia e Zefir Hvitskog al suo fianco in chiodo di pelle borchiato e cresta bianca alla moicana, ufficialmente iscritto come matricola islandese sotto copertura. Pochi istanti dopo, dal viale opposto arrivano Finnegan Novak con la felpa dei Bears, Sierra Cruz scivolando sinuosa sulle sue spire arcobaleno e Scarlett Rose con le sue ali da succubus e corna scarlatte, completando il cerchio prima del discorso inaugurale."""

for name, text in [("alyssa", scene_alyssa_text), ("jasper", scene_jasper_text), ("corale", scene_corale_text)]:
    assert '—' not in text, f"Em-dash found in {name}!"
    assert '*' not in text, f"Asterisk found in {name}!"

payload = {
    "world_id": world_id,
    "world": world_id,
    "name": "SUCC: Welcome Day al Lunar Quad",
    "description": "26 agosto 2024. Cerimonia inaugurale del Welcome Day sul Lunar Quad della SUCC con tutta la famiglia Douglas-Bloodmoon (Noah, Malachia, Jasper, Alyssa, Erik, Logan ed Edric), l'arrivo a sorpresa di Wulfnic in maglietta gag che iscrive Zefir in versione punk come cugino islandese, e l'incontro con Scarlett, Sierra e Finn.",
    "scenario_premise": "Il 26 agosto 2024 segna l'inizio ufficiale dell'anno accademico alla Supernatural University of Central California (SUCC). Sul Lunar Quad, gremito di matricole, famiglie e docenti sotto gli stendardi cremisi e oro, l'intero clan Douglas-Bloodmoon accompagna i suoi studenti per la cerimonia d'apertura. Mentre il Cancelliere Archer Wolfwood si prepara al discorso dal palco centrale e i fratelli maggiori controllano il perimetro, l'arrivo dell'antico Jarl Wulfnic con Zefir Hvitskog in incognito come matricola punk ribelle scatena stupore e dinamiche imprevedibili.",
    "tags": ["succ", "welcome-day", "lunar-quad", "douglas", "bloodmoon", "solarton", "college", "werewolf"],
    "community_tags": [],
    "avatar": avatar_url,
    "location_id": location_id,
    "environment_id": environment_id,
    "insertion_point": 10489906,
    "visibility": "private",
    "rating": "explicit",
    "world_only": False,
    "scenario_type": "any",
    "include_character_select": True,
    "include_rpg_build": False,
    "playable_character_ids": linked_char_ids,
    "included_character_pool": [{"character_id": cid, "participation_weight": 50} for cid in linked_char_ids],
    "scene_instructions": "Capture the collegiate atmosphere, family dynamics, and pack instincts of the Douglas-Bloodmoon clan on the SUCC campus during the Fall 2024 Welcome Day. Highlight protective banter between Erik, Logan, and the older brothers, Wulfnic's comedic yet fierce presence enrolling Zefir as an undercover freshman punk, and the interactions with Scarlett, Sierra, and Finn. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.",
    "premade_scenes": [
        {
            "id": "scene-succ-welcome-day-alyssa",
            "description": "Welcome Day al Lunar Quad: Punto di Vista Alyssa (FemPOV / Matricola Pre-Med)",
            "scene_text": scene_alyssa_text
        },
        {
            "id": "scene-succ-welcome-day-jasper",
            "description": "Welcome Day al Lunar Quad: Punto di Vista Jasper (MalePOV / Matricola Ingegneria Arcana)",
            "scene_text": scene_jasper_text
        },
        {
            "id": "scene-succ-welcome-day-corale",
            "description": "Welcome Day al Lunar Quad: Scena Corale del Branco (AnyPOV / Arrivo sul Campus)",
            "scene_text": scene_corale_text
        }
    ]
}

url = f'https://app.wyvern.chat/api/worlds/scenarios/{scenario_id}'
req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
try:
    with urllib.request.urlopen(req) as resp:
        print(f"Scenario update HTTP {resp.status}")
        updated_data = json.loads(resp.read().decode('utf-8'))
        print("Updated Scenario ID:", updated_data.get('_id'))
        print("Name:", updated_data.get('name'))
        print("Location:", updated_data.get('location', {}).get('name'))
        print("Environment:", updated_data.get('environment', {}).get('name'))
        print("Insertion Point:", updated_data.get('insertion_point'))
        print("Premade Scenes Count:", len(updated_data.get('premade_scenes', [])))
        for s in updated_data.get('premade_scenes', []):
            print(f"  - [{s.get('id')}] {s.get('description')} (len: {len(s.get('scene_text', ''))} chars)")
        
        # Save local JSON artifact in FINAL/scenarios/
        local_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'FINAL', 'scenarios', 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json')
        with open(local_path, 'w', encoding='utf-8') as f:
            json.dump(updated_data, f, indent=2, ensure_ascii=False)
        print(f"[OK] Saved local file: {local_path}")
except urllib.error.HTTPError as e:
    print(f"PUT Error {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("Error:", e)
