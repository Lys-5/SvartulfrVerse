import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

ALYSSA_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json'
JASPER_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json'

ALYSSA_PERSONA_ID = "persona_1786335754946"
JASPER_PERSONA_ID = "1792155173728"

# ==============================================================================
# 1. ALYSSA ROUTE GREETINGS (7 Greetings in Italian)
# ==============================================================================

al_g0_m1 = (
    "Il sole della tarda mattinata batte sui prati gremiti del Lunar Quad il 26 agosto 2024, filtrando tra gli stendardi cremisi e oro issati per il Welcome Day della SUCC. "
    "Poiché la cerimonia inaugurale è aperta anche ai familiari degli studenti per gli ultimi saluti prima dell'inizio delle lezioni, l'intero clan Douglas-Bloodmoon ha accompagnato sul quad i quattro iscritti all'università: i fratelli maggiori {{scenarioChar \"eldest_brother\"}} e {{scenarioChar \"brother\"}} insieme ai gemelli matricole {{scenarioChar \"twin\"}} e {{user}}, scortati dal padre {{scenarioChar \"father\"}}, dallo zio {{scenarioChar \"uncle\"}} e dal cugino tredicenne {{scenarioChar \"cousin\"}}. "
    "Sul palco del padiglione centrale, il Cancelliere Archer Wolfwood è affiancato dai presidi di facoltà mentre i tecnici del suono regolano il microfono d'ottone.\n"
    "Erik Ulfr Douglas: \"Restate uniti quando la folla si disperderà dopo il discorso, e chiamate subito se i guardiani del campus vi danno qualsiasi problema,\" brontola Erik, la sua alta figura che proietta un'ombra protettiva sul vialetto mentre i suoi occhi ambrati scrutano il prato.\n"
    "Logan Járn Douglas: \"Lasciali respirare, Erik, è l'orientamento universitario, non un assedio,\" dice Logan con una risata calorosa, posando una mano massiccia sulla spalla di Edric.\n"
    "Edric Douglas: \"Aspetta di vedere quanto è grande la mensa, Jasper! Ma le matricole hanno davvero i pass illimitati anche per la sala giochi dell'Annex?\" chiede Edric con entusiasmo, allungando il collo verso l'edificio dell'unione studentesca.\n"
    "Noah Loki Douglas Bloodmoon: \"Il tendone di rappresentanza della KSA sul prato est ha bevande fresche e posti all'ombra riservati per noi quando volete sfuggire al caldo,\" osserva Noah con eleganza, sistemandosi il revers della giacca di lino su misura.\n"
    "Malachia Björn Douglas Bloodmoon: \"Ho già controllato il perimetro dalla palestra fino a Greek Row. Nessuno darà fastidio alla mia sorellina in questo campus,\" aggiunge Malachia con tono basso e roca fermezza, incrociando le braccia sul petto.\n"
    "Accanto a {{user}}, {{scenarioChar \"twin\"}} alza lo sguardo dalla telemetria di rete sul suo datapad; le sue orecchie scure da lupo si orientano verso il cancello principale, un unico paio lupino sulla sommità del capo senza alcuna orecchia umana ai lati della testa. "
    "\"Le registrazioni delle matricole hanno già mandato in crash il server centrale della biblioteca,\" mormora Jasper, dando un leggero colpetto di gomito a {{user}}. \"Aspetta un secondo. Guarda chi sta varcando l'arco di pietra principale proprio adesso.\""
)

al_g0_m2 = (
    "Il brusio lungo il viale centrale si apre in un'ondata di silenzio stupefatto quando {{scenarioChar \"maternal_grandfather\"}} avanza sul Lunar Quad con Zefir Hvitskog al suo fianco. "
    "Lo Jarl di Svartúlfr, a milleduecento anni compiuti, sfoggia il suo outfit gag preferito con solenne e fierissimo orgoglio: una t-shirt di cotone nero oversize regalatagli da Jasper che porta stampata sulla schiena, a grandi caratteri bianchi, una lunghissima e fitta lista di Regole per Uscire con Mia Nipote, abbinata a jeans scuri con l'apertura sartoriale per la coda da lupo argentata, pesanti stivali da motociclista con fibbie e un antico torque d'argento ritorto al collo. "
    "Accanto a lui, Zefir ha tutto l'aspetto di un giovane ribelle punk sui vent'anni: i suoi capelli bianco-neve sono rasati ai lati in una netta cresta alla moicana e indossa un pesante giubbotto di pelle nera tempestato di borchie d'argento sopra una canotta nera strappata e jeans aderenti, tenendo il fascicolo dell'orientamento piegato in una mano tatuata.\n"
    "\"In fondo non sei mai andato a scuola e tecnicamente sei un ragazzino!\" tuona Wulfnic scoppiando in una risata profonda e fragorosa, mentre batte una manata pesante sulla spalla borchiata di Zefir.\n"
    "\"Non fare quella faccia sorpresa, Erik! Per assicurarmi che la nostra piccola Alyssa sia protetta come si deve nel campus, ho deciso di iscrivere anche Zefir all'università. Per la segreteria è un vostro lontano parente appena arrivato dall'Islanda, così giustifichiamo il suo accento marcatamente norreno e la sua poca dimestichezza con l'inglese scritto.\"\n"
    "Zefir Hvitskog: \"Ridi pure quanto vuoi, mio Jarl, ma se qualche professore pieno di sé mi agita un gessetto sotto il naso, non prometto di lasciarglielo intero,\" ribatte Zefir con un ghigno sfrontato e vivace, la spavalderia giovanile del vichingo sedicenne che era un tempo che gli brilla negli occhi azzurro ghiaccio come una raffica capricciosa del vento dei mari del Nord, prima di rivolgere un saluto beffardo con due dita a {{user}} e Jasper.\n"
    "Zefir Hvitskog: \"Rilassati, cuginetta. Il tuo parente dall'Islanda è ufficialmente una matricola adesso. Indicami chiunque ti guardi di traverso e sparirà prima che suoni la campanella.\""
)

al_g0_m3 = (
    "Finnegan Novak si fa largo tra il flusso degli studenti dal padiglione atletico con la giacca varsity dei Bears gettata su una spalla, arrivando insieme a Scarlett Rose e Sierra Cruz. "
    "Per evitare che i tre amici del campus si mettano sul chi vive davanti a un Firstborn, la famiglia racconta subito anche a loro della copertura di Zefir come lontano cugino appena arrivato dall'Islanda per il primo anno. "
    "Sebbene Zefir abbia completamente annullato la sua aura divina da Enigma, apparendo ai loro sensi come un normale licantropo qualsiasi con un giubbotto di pelle punk, Finn si irrigidisce all'istante. "
    "Il suo unico paio di orecchie da lupo artico sulla sommità del capo, senza orecchie umane ai lati, si abbassa impercettibilmente mentre un inspiegabile istinto primordiale lo fa sentire in qualche modo inferiore a quel tipo, spingendolo a gonfiare il petto per provare a mostrarsi più figo davanti a {{user}}.\n"
    "Finnegan Novak: \"Ci ho messo venti minuti solo per seminare gli osservatori vicino all'arena, Alyssa. Il coach mi ha già schierato in prima linea per la partita inaugurale, quindi se il tuo cugino dall'Islanda vuole dei posti in prima fila dietro la balaustra per vedere come si gioca a vero hockey universitario, ci penso io,\" dice Finn, appoggiandosi con studiata noncuranza alla colonnina di pietra e flettendo l'avambraccio mentre si sistema il colletto della giacca.\n"
    "Sierra Cruz: \"Okay, aspetta, lascia perdere l'hockey per un secondo, dove hai preso quel giubbotto?\" chiede Sierra, i suoi capelli color arcobaleno che catturano il sole mentre striscia dritta verso Zefir sulla sua imponente coda da serpente color arcobaleno, le scaglie iridescenti che scintillano sul lastricato di pietra mentre i suoi occhi rosa confetto si spalancano con sincera invidia davanti alle pesanti borchie d'argento sui revers di pelle nera.\n"
    "Sierra Cruz: \"L'effetto vissuto della pelle e quelle borchie lavorate sembrano vintage europeo. C'è qualche boutique underground a Reykjavik che devo assolutamente conoscere?\"\n"
    "Scarlett Rose: \"Onestamente, credo che il fascino da punk islandese fosse proprio quello che mancava in questo campus,\" fa le fusa Scarlett con un lento sorriso civettuolo, i suoi capelli rosa confetto che incorniciano le corna scarlatte che spuntano sopra le tempie e i suoi occhi rosa confetto che brillano sotto le ciglia mentre flirta apertamente con Zefir e la sua coda dalla punta a picca ondeggia giocosa dietro di lei.\n"
    "Scarlett Rose: \"Benvenuto a Solarton, Zefir. Visto che hai ancora poca dimestichezza con l'inglese scritto, sarò più che felice di darti qualche ripetizione privata dopo la cerimonia. Dai, Alyssa, Wolfwood sta salendo al microfono.\""
)

al_g1_m1 = (
    "Sierra Cruz avvolge le sue lunghe spire serpentine color arcobaleno davanti allo specchio a figura intera nella suite della Theta Iota Theta, le sue scaglie iridescenti che brillano nella luce del mattino mentre si scosta una ciocca di capelli color arcobaleno e controlla il calendario sul telefono.\n"
    "Sierra Cruz: \"Se strisciamo fuori tra dieci minuti, facciamo in tempo a prendere un matcha ghiacciato prima che l'aula magna si riempia. Lunedì il professor Vance ha chiuso le porte esattamente alle otto e cinque.\""
)
al_g1_m2 = (
    "Giù sulla strada, la porta a rete della confraternita Alpha Rho Omega cigola aprendosi. Finnegan Novak esce sulla veranda in una felpa atletica grigia, il suo unico paio di orecchie da lupo bianco sulla sommità del capo che guizza attento mentre i suoi occhi rossi incrociano la scalinata della sorority. Si raddrizza, esita per una frazione di secondo, poi solleva una mano in un saluto disinvolto prima di avviarsi verso i campi sportivi.\n"
    "Finnegan Novak: \"Non fare tardi al laboratorio di stamattina, Alyssa! Tienimi un posto in mensa per pranzo!\""
)
al_g1_m3 = (
    "Una notifica risuona sulla console della scrivania, un rapido messaggio crittografato da parte di {{scenarioChar \"twin\"}}. "
    "\"Ho visto Vince e le sue reclute della ASS aggirarsi vicino agli archi della biblioteca centrale. Resta sul viale sud con Sierra. Ci vediamo a mezzogiorno vicino alle serre.\""
)

al_g2_m1 = (
    "Scarlett Rose poggia il blocco da disegno accanto a un vassoio di campioni botanici, la matita che traccia la delicata struttura delle venature di una felce fogliargento. Le sue morbide onde di capelli rosa confetto e le corna scarlatte che spuntano tra le ciocche riflettono la luce bianca del laboratorio mentre i suoi occhi rosa confetto si illuminano in un sorriso caloroso.\n"
    "Scarlett Rose: \"Il professor Vance ha detto che se finiamo la titolazione cellulare prima di mezzogiorno possiamo portare le piastre di coltura rimaste nella serra. Ho già preparato i vetrini per la tua sezione.\""
)
al_g2_m2 = (
    "Stanley Davies Jr. si sistema gli occhiali dalla montatura metallica, ricontrollando i valori dello spettrometro sul bancone in resina con un sospiro.\n"
    "Stanley Davies Jr.: \"Se per titolazione intendi vera chimica organica e non l'idea di Jared di mescolare proteine in polvere nell'acqua distillata, potremmo persino mantenere la nostra media dei voti.\""
)
al_g2_m3 = (
    "Un avviso luminoso lampeggia sull'angolo del datapad di {{user}}. \"Ho finito la patch audio per il set di venerdì,\" scrive {{scenarioChar \"twin\"}}. "
    "\"Prendi due muffin alla mensa quando esci, sempre che Stan non dia fuoco al laboratorio prima.\""
)

al_g3_m1 = (
    "{{scenarioChar \"crush\"}} ha una cuffia appoggiata sul colletto e se ne sta appoggiato alla rastrelliera in ferro battuto con le mani affondate nelle tasche del giubbotto di pelle consumato. Alza lo sguardo con un sorriso lento e rilassato che lascia intravedere appena la punta dei canini affilati. "
    "\"La biblioteca è troppo silenziosa per te oggi, o le flashcard di anatomia hanno finalmente organizzato un ammutinamento?\""
)
al_g3_m2 = (
    "Scarlett Rose scende i gradini di pietra portando due caffè ghiacciati, i suoi capelli rosa confetto che rimbalzano attorno alle corna scarlatte mentre coglie lo scambio di battute con un sorriso divertito negli occhi rosa confetto.\n"
    "Scarlett Rose: \"Gliel'ho detto io che una boccata d'aria fresca era obbligatoria. Suoni al locale di Dockside questo venerdì, Mac?\""
)
al_g3_m3 = (
    "Una breve vibrazione risuona nella tasca di {{user}}. {{scenarioChar \"twin\"}} ha inviato un ping automatico: "
    "\"Pattuglia della sicurezza diretta verso il prato ovest della biblioteca. Assicurati che Mac nasconda qualsiasi cosa stia fumando prima che l'agente Higgins inizi ad annusare l'edera.\""
)

al_g4_m1 = (
    "Vincent Campbell raccoglie un passaggio al cerchio di centrocampo, il codino nero che oscilla mentre spedisce il disco sotto l'incrocio dei pali con grazia sprezzante. Pattina lungo la balaustra con un ghigno arrogante, lanciando un commento tagliente in francese che rimbomba sotto le travi gelide del palazzetto.\n"
    "Vincent Campbell: \"Cercate di restare in piedi sui pattini in questo tempo, cuccioli. Il ghiaccio appartiene alla prima linea.\""
)
al_g4_m2 = (
    "Finnegan Novak si lancia nell'angolo della zona neutra con un'accelerazione brutale, schiantando la spalla contro il plexiglass con un boato che solleva una nuvola di ghiaccio tritato verso gli spalti. Il suo unico paio di orecchie da lupo bianco è appiattito sul capo, la coda bianca è rigida per la rabbia e gli occhi rossi ardono mentre fulmina il capitano vampiro, proprio mentre {{scenarioChar \"brother\"}} pattina tra di loro per mantenere l'ordine.\n"
    "Finnegan Novak: \"Ripetilo senza l'arbitro in mezzo a noi, Campbell!\""
)
al_g4_m3 = (
    "Jared Thompson si sporge dalla ringhiera del tunnel nella sua tuta da riscaldamento da football accanto a {{scenarioChar \"eldest_brother\"}}, portandosi le mani a coppa attorno alla bocca per sovrastare il ronzio degli impianti di refrigerazione.\n"
    "Jared Thompson: \"Tenete la testa sulla partita, ragazzi! Venerdì avremo gli osservatori della lega sugli spalti!\""
)

al_g5_m1 = (
    "Jared Thompson torreggia nella sua maglia da allenamento oro e nera fuori dalla sala pesi dove {{scenarioChar \"eldest_brother\"}} si sta fasciando le nocche, con le spalline ancora allacciate sul petto e un asciugamano umido attorno al collo.\n"
    "Jared Thompson: \"Ehi, Alyssa! Dimmi che hai portato gli appunti della lezione di biochimica. Il coach ha detto che se il mio voto di metà semestre scende sotto la B mi tiene in panchina per tutto il primo quarto all'Homecoming.\""
)
al_g5_m2 = (
    "Stanley Davies Jr. è appoggiato alla parete di cemento accanto a {{scenarioChar \"twin\"}}, stringendo il suo raccoglitore con un'espressione impassibile.\n"
    "Stanley Davies Jr.: \"Quello che Jared sta cercando di dire è che non sa distinguere un'ammina da un estere, e io mi rifiuto di passare altre tre ore a spiegare i legami del carbonio a un quarterback.\""
)
al_g5_m3 = (
    "Sierra Cruz scivola lungo il pavimento liscio del corridoio sulle sue spire serpentine color arcobaleno, le scaglie iridescenti che frusciano appena mentre porta un fascio di striscioni del campus e scuote la testa dai capelli arcobaleno ridendo.\n"
    "Sierra Cruz: \"Dagli una mano, Lys. Se i Bulls perdono la partita d'apertura, Greek Row sarà in lutto per due settimane di fila.\""
)

al_g6_m1 = (
    "Sul palco sopraelevato, {{scenarioChar \"crush\"}} è dietro la sua doppia tastiera di sintetizzatori, le dita che si muovono fluide sui tasti mentre la distorsione sale di giri. Gli accordi melodici crescono in un crescendo travolgente e, attraverso la foschia viola e le luci stroboscopiche, i suoi occhi ambrati agganciano quelli di {{user}} in prima fila, le labbra che si schiudono in un sorriso inconfondibile."
)
al_g6_m2 = (
    "Scarlett Rose balla accanto a {{user}}, i suoi capelli rosa confetto e le corna scarlatte che brillano sotto i neon mentre ride sopra il rimbombo del basso e solleva il bicchiere verso il palco.\n"
    "Scarlett Rose: \"Te l'avevo detto che il suo assolo valeva tutta la passeggiata fino al porto! Guarda quanta gente, stasera c'è metà del campus!\""
)
al_g6_m3 = (
    "Dalla balconata della cabina audio sopra la folla, {{scenarioChar \"twin\"}} alza il pollice da dietro la console dell'equalizzatore master, assicurandosi che l'acustica colpisca pulita in tutto il capannone senza mandare in saturazione gli amplificatori."
)

ALYSSA_GREETINGS = [
    {
        "id": "scene-alyssa-welcome-day",
        "name": "SUCC Welcome Day",
        "description": "26 agosto 2024. Welcome Day sul Lunar Quad della SUCC: l'arrivo con tutta la famiglia (Noah, Malachia, Jasper, Alyssa, Erik, Logan ed Edric), Wulfnic con la maglietta gag che iscrive Zefir in versione punk come cugino dall'Islanda, e l'incontro con Scarlett, Sierra e Finn.",
        "messages": [
            {"id": "msg-al-0-1", "speaker_slot": "twin", "content": al_g0_m1},
            {"id": "msg-al-0-2", "speaker_slot": "maternal_grandfather", "content": al_g0_m2},
            {"id": "msg-al-0-3", "speaker_slot": "twin", "content": al_g0_m3}
        ],
        "speaker_slot": "twin",
        "content": al_g0_m1,
        "linked_persona_ids": [ALYSSA_PERSONA_ID]
    },
    {
        "id": "scene-alyssa-greek-row",
        "name": "01. Mattina alla Theta Iota Theta su Greek Row",
        "description": "Luce del mattino su Greek Row, preparativi nella suite con Sierra Cruz e il saluto di Finn Novak dalla veranda della Alpha Rho Omega.",
        "messages": [
            {"id": "msg-al-1-1", "speaker_slot": "twin", "content": al_g1_m1},
            {"id": "msg-al-1-2", "speaker_slot": "twin", "content": al_g1_m2},
            {"id": "msg-al-1-3", "speaker_slot": "twin", "content": al_g1_m3}
        ],
        "speaker_slot": "twin",
        "content": al_g1_m1,
        "linked_persona_ids": [ALYSSA_PERSONA_ID]
    },
    {
        "id": "scene-alyssa-labs",
        "name": "02. Laboratori di Biologia Pre-Med",
        "description": "Campioni botanici nell'ala scientifica, disegni cellulari con Scarlett Rose e il sarcasmo accademico di Stan.",
        "messages": [
            {"id": "msg-al-2-1", "speaker_slot": "twin", "content": al_g2_m1},
            {"id": "msg-al-2-2", "speaker_slot": "twin", "content": al_g2_m2},
            {"id": "msg-al-2-3", "speaker_slot": "twin", "content": al_g2_m3}
        ],
        "speaker_slot": "twin",
        "content": al_g2_m1,
        "linked_persona_ids": [ALYSSA_PERSONA_ID]
    },
    {
        "id": "scene-alyssa-library-corner",
        "name": "03. Angolo Riparato dietro la Basilica Library",
        "description": "Contrafforti di pietra ricoperti d'edera dietro la Basilica Library, aria fresca e una chiacchierata rilassata con Mackenzie.",
        "messages": [
            {"id": "msg-al-3-1", "speaker_slot": "crush", "content": al_g3_m1},
            {"id": "msg-al-3-2", "speaker_slot": "crush", "content": al_g3_m2},
            {"id": "msg-al-3-3", "speaker_slot": "twin", "content": al_g3_m3}
        ],
        "speaker_slot": "crush",
        "content": al_g3_m1,
        "linked_persona_ids": [ALYSSA_PERSONA_ID]
    },
    {
        "id": "scene-alyssa-ice-rink",
        "name": "04. Scontro sul Ghiaccio all'Allenamento dei Bears",
        "description": "Nebbia fredda e balaustre che tremano alla SUCC Ice Arena, l'arroganza di Vincent Campbell e la carica agonistica di Finn Novak.",
        "messages": [
            {"id": "msg-al-4-1", "speaker_slot": "brother", "content": al_g4_m1},
            {"id": "msg-al-4-2", "speaker_slot": "brother", "content": al_g4_m2},
            {"id": "msg-al-4-3", "speaker_slot": "eldest_brother", "content": al_g4_m3}
        ],
        "speaker_slot": "brother",
        "content": al_g4_m1,
        "linked_persona_ids": [ALYSSA_PERSONA_ID]
    },
    {
        "id": "scene-alyssa-bulls-tunnel",
        "name": "05. Spogliatoi dei Bulls e Tunnel dello Stadio",
        "description": "Nastro atletico e linimento nel tunnel dello stadio, la richiesta di ripetizioni di Jared e il commento pungente di Stan.",
        "messages": [
            {"id": "msg-al-5-1", "speaker_slot": "eldest_brother", "content": al_g5_m1},
            {"id": "msg-al-5-2", "speaker_slot": "twin", "content": al_g5_m2},
            {"id": "msg-al-5-3", "speaker_slot": "twin", "content": al_g5_m3}
        ],
        "speaker_slot": "eldest_brother",
        "content": al_g5_m1,
        "linked_persona_ids": [ALYSSA_PERSONA_ID]
    },
    {
        "id": "scene-alyssa-sidewinders",
        "name": "06. Concerto al Locale di Dockside",
        "description": "Luci al neon, sintetizzatori distorti e lo sguardo di Mackenzie dal palco durante il culmine del concerto.",
        "messages": [
            {"id": "msg-al-6-1", "speaker_slot": "crush", "content": al_g6_m1},
            {"id": "msg-al-6-2", "speaker_slot": "crush", "content": al_g6_m2},
            {"id": "msg-al-6-3", "speaker_slot": "twin", "content": al_g6_m3}
        ],
        "speaker_slot": "crush",
        "content": al_g6_m1,
        "linked_persona_ids": [ALYSSA_PERSONA_ID]
    }
]


# ==============================================================================
# 2. JASPER ROUTE GREETINGS (6 Greetings in Italian)
# ==============================================================================

js_g0_m1 = (
    "La luce limpida della tarda mattinata inonda i prati del Lunar Quad il 26 agosto 2024, illuminando gli stendardi cremisi e oro issati nel campus per il Welcome Day della SUCC. "
    "Poiché la cerimonia di apertura è aperta ai familiari degli studenti per gli ultimi saluti, l'intera famiglia Douglas-Bloodmoon ha accompagnato sul quad i quattro iscritti all'università: i fratelli maggiori {{scenarioChar \"eldest_brother\"}} e {{scenarioChar \"brother\"}} insieme alle matricole {{user}} e Alyssa, scortati dal padre {{scenarioChar \"father\"}}, dallo zio {{scenarioChar \"uncle\"}} e dal cugino tredicenne {{scenarioChar \"cousin\"}}. "
    "Sul palco del padiglione centrale, il Cancelliere Archer Wolfwood è dietro il microfono d'ottone a rivedere i suoi appunti mentre gli addetti del campus guidano centinaia di nuovi studenti verso le file di sedie.\n"
    "\"Tenete le linee di comunicazione aperte dopo il discorso inaugurale, e ricordatevi che la cena di famiglia della domenica non è facoltativa,\" brontola Erik, la sua presenza imponente che fa aprire la folla al suo passaggio mentre controlla il perimetro.\n"
    "Logan Járn Douglas: \"Lascia che si godano la loro prima mattina al campus, Erik, hanno aspettato tutta l'estate per questo momento,\" dice Logan con un sorriso rilassato e rassicurante, poggiando una mano sulla spalla di Edric.\n"
    "Edric Douglas: \"Jasper, se violi il tabellone segnapunti dello stadio durante la prima partita dei Bulls, devi farmi guardare la scena dal tuo dormitorio!\" sussurra Edric con un ghigno, saltellando sui talloni.\n"
    "Noah Loki Douglas Bloodmoon: \"Il padiglione della KSA sul prato est è già rifornito se volete qualcosa di fresco lontano dalla calca delle matricole,\" osserva Noah con calma impeccabile, sistemandosi i polsini.\n"
    "Malachia Björn Douglas Bloodmoon: \"Ho già ispezionato Wyrm Hall e Greek Row. Chiunque superi il limite con uno di voi due dovrà risponderne a me,\" dichiara Malachia con voce ferma, le braccia incrociate sul petto.\n"
    "Accanto a {{user}}, Alyssa Hvit Douglas Bloodmoon stringe al petto il suo diario erboristico rilegato in pelle; le sue orecchie bianche da lupo si drizzano sulla sommità del capo, un unico paio lupino senza alcuna orecchia umana ai lati della testa, mentre guarda verso l'arco di pietra principale.\n"
    "Alyssa Hvit Douglas Bloodmoon: \"Cerca di non infiltrarti nella telemetria dell'amministrazione durante il discorso di Wolfwood, Jasper. Aspetta. Guarda chi è appena entrato sul quad.\""
)

js_g0_m2 = (
    "Un mormorio di incredulità percorre il viale principale quando {{scenarioChar \"maternal_grandfather\"}} avanza sul Lunar Quad con Zefir Hvitskog al suo fianco. "
    "L'antico Jarl indossa con fierezza regale l'outfit gag che proprio {{user}} gli ha regalato: una t-shirt di cotone nero oversize con una lunghissima e fitta lista di Regole per Uscire con Mia Nipote stampata in bianco sulla schiena, abbinata a jeans scuri con l'apertura per la coda da lupo argentata, pesanti stivali da motociclista e un torque d'argento ritorto al collo. "
    "Accanto a lui, Zefir sembra un giovane ribelle punk sui vent'anni: i suoi capelli bianco-neve sono rasati ai lati in una fiera cresta alla moicana e indossa un giubbotto di pelle nera coperto di borchie d'argento sopra una canotta nera strappata e jeans aderenti, con l'orario delle lezioni da matricola infilato tra due dita tatuate.\n"
    "\"In fondo non sei mai andato a scuola e tecnicamente sei un ragazzino!\" ruggisce Wulfnic con una risata profonda e tonante, dando una pacca così forte sulla spalla di Zefir da far tintinnare le borchie.\n"
    "\"Ho preso spunto da te, Jasper! Per assicurarmi che Alyssa abbia un'ombra in più a proteggerla nel campus, stamattina ho iscritto anche Zefir all'università. Sui documenti risulta come un vostro lontano parente appena arrivato dall'Islanda, così giustifichiamo il suo marcato accento norreno e la sua poca dimestichezza con l'inglese scritto.\"\n"
    "Zefir Hvitskog: \"Continua pure a ridere, vecchio, e vediamo chi mi tradurrà questi maledetti programmi dei corsi stasera,\" ribatte Zefir con un ghigno insolente e vivace, i suoi occhi azzurro ghiaccio accesi dalla spavalderia indomita del guerriero vichingo sedicenne che era e dal brio imprevedibile del vento dei mari del Nord, mentre tocca il revers borchiato verso {{user}} e Alyssa.\n"
    "Zefir Hvitskog: \"Che ne dici, Svartr? Il tuo nuovo cugino islandese è ufficialmente una matricola universitaria. Basta che non mi chiediate di scrivere un tema, a meno che non lo vogliate inciso sulla cattedra col pugnale.\""
)

js_g0_m3 = (
    "Finnegan Novak attraversa il prato dal complesso atletico nella sua felpa grigia da hockey dei Bears, arrivando insieme a Scarlett Rose e Sierra Cruz giusto in tempo per sentire la famiglia presentare Zefir con la copertura del lontano cugino dall'Islanda per evitare che si mettano sul chi vive. "
    "Anche se Zefir ha completamente annullato la sua aura divina da Enigma, sembrando a tutti gli effetti un licantropo qualsiasi in mezzo a centinaia di studenti, l'istinto di Finn avverte comunque un inspiegabile senso di inferiorità davanti a quel ragazzo dalla cresta bianca. "
    "Il suo unico paio di orecchie da lupo artico si piega lievemente sulla sommità del capo, senza orecchie umane ai lati, mentre raddrizza le spalle e prova subito a mostrarsi più figo davanti ad Alyssa.\n"
    "Finnegan Novak: \"Bello vederti alla luce del sole, Svartr. Stavo giusto dicendo ad Alyssa che il coach mi ha messo nel primo blocco di power-play, quindi se vostro cugino dall'Islanda vuole vedere cosa significa vera velocità sul ghiaccio, lo metto nella lista VIP,\" si vanta Finn, infilando i pollici nelle tasche della felpa e assumendo una posa plastica da atleta a beneficio di Alyssa.\n"
    "Sierra Cruz: \"Ferma tutto, devo assolutamente sapere dove hai preso quel giubbotto di pelle adesso,\" interviene Sierra, strisciando più vicino sulla sua imponente coda da serpente color arcobaleno, le scaglie iridescenti che riflettono il sole e i capelli color arcobaleno che ondeggiano mentre ammira le file di borchie d'argento sulle spalle di Zefir.\n"
    "Sierra Cruz: \"Sul serio, nessuno a Solarton lavora la pelle così. Dove l'hai preso in Islanda?\"\n"
    "Scarlett Rose: \"Devo ammettere che lo stile da vichingo ribelle ti dona in modo pericoloso, Zefir,\" mormora Scarlett inclinando la testa così che i suoi capelli rosa confetto sfiorino le corna scarlatte che spuntano sopra le tempie, un lampo malizioso e civettuolo nei suoi occhi rosa confetto mentre flirta con lui prima di lanciare uno sguardo complice a {{user}}.\n"
    "Scarlett Rose: \"Se tuo cugino avesse bisogno di una mano per decifrare i manuali in inglese, Jasper, sai dove trovarmi. Dai, venite a sedervi con noi sul prato sud prima che Wolfwood inizi il discorso.\""
)

js_g1_m1 = (
    "Russell Sinclair è seduto sul divano basso in vinile della Suite 304 a Wyrm Hall, le spalle scoperte coperte di tatuaggi scuri e la bandana a tenere indietro i riccioli ribelli mentre regola con cura la profondità dell'ago su una macchinetta rotativa da tatuaggio.\n"
    "Russell Sinclair: \"Ehi, Svartr. Javier dice che il cancello della banchina di carico è aperto stasera se vogliamo testare l'antenna parabolica direzionale. Ah, e Raymond ha provato di nuovo a fregarti il saldatore buono, ma l'ho intercettato io.\""
)
js_g1_m2 = (
    "Dalla postazione a doppio monitor sotto il letto a castello, un lieve segnale acustico risuona dagli altoparlanti mentre il visualizzatore vocale geometrico di Echo pulsa di blu sullo schermo ultrawide.\n"
    "Echo: \"Rilevata anomalia sulla rete del campus nella sottorete 4. Il flusso di pacchetti in entrata indica un'ispezione non autorizzata da parte dell'IT universitario. Devo isolare il gateway, Jasper?\""
)
js_g1_m3 = (
    "Un bussare leggero risuona alla porta e Alyssa Hvit Douglas Bloodmoon fa capolino nella stanza tenendo due scatole del pranzo dalla casa della Theta, proprio mentre {{scenarioChar \"cousin\"}} invia un ping sulle cuffie di Jasper nel canale vocale locale.\n"
    "Alyssa Hvit Douglas Bloodmoon: \"Ho portato dei panini da Greek Row prima che i ragazzi svuotino il frigo comune. State ancora ricostruendo quell'amplificatore audio?\""
)

js_g2_m1 = (
    "Sul terminale corazzato appoggiato sul telo catramato del tetto di Wyrm Hall, la forma d'onda digitale di Echo traccia una linea blu costante.\n"
    "Echo: \"Potenza del segnale al novantadue percento. Firewall dell'amministrazione del campus aggirato. Abbiamo un accesso diretto e senza filtri al circuito di telemetria regionale della DCC senza far scattare i log del proxy locale.\""
)
js_g2_m2 = (
    "Russell Sinclair varca la porta d'accesso al tetto portando due lattine gelate di energy drink e appoggiando la schiena contro il condotto di ventilazione in mattoni.\n"
    "Russell Sinclair: \"Nessuno mi ha seguito su per le scale di emergenza. Se spunta la sicurezza del campus, buttiamo il telo sull'antenna e diciamo che stiamo osservando le stelle per il laboratorio di astronomia.\""
)
js_g2_m3 = (
    "Un rapido messaggio di testo lampeggia sullo schermo dello smartphone da parte di Finnegan Novak mentre il pass di sicurezza KSA di {{scenarioChar \"brother\"}} mantiene il ripetitore del tetto nella whitelist:\n"
    "Finnegan Novak: \"L'allenamento serale dei Bears è finito in anticipo. Un furgone della sicurezza del campus si è appena fermato fuori dalla Griffin Clocktower. Tenete d'occhio il perimetro.\""
)

js_g3_m1 = (
    "Vincent Campbell si ferma vicino alla fontana di granito insieme a due reclute della confraternita in giacca sartoriale, sistemandosi gli occhiali da sole con studiato disprezzo.\n"
    "Vincent Campbell: \"Ma guarda, il gremlin residente del dipartimento di ingegneria. Dimmi, Douglas, esci mai da quel seminterrato senza puzzare di cavi bruciati e caffè nero?\""
)
js_g3_m2 = (
    "Jared Thompson attraversa il prato con il pesante borsone da football in spalla accanto a {{scenarioChar \"eldest_brother\"}}, piazzandosi esattamente in mezzo a loro e battendo una mano colossale sulla spalla di Vincent fino a far serrare la mascella al vampiro.\n"
    "Jared Thompson: \"Andiamo, Vince, lascia in pace il mago. Alcuni di noi hanno davvero bisogno della sua magia coi server per passare gli esami di comunicazioni.\""
)
js_g3_m3 = (
    "Stanley Davies Jr. resta qualche passo indietro vicino a {{scenarioChar \"brother\"}}, picchiettando la penna contro il manuale con un mezzo sorriso asciutto.\n"
    "Stanley Davies Jr.: \"Statisticamente parlando, Vincent, ogni volta che insulti chi amministra il Wi-Fi del campus, la banda del tuo dormitorio scende del venti percento. Sceglierei le parole con più attenzione.\""
)

js_g4_m1 = (
    "Russell Sinclair sposta la tenda nera del backstage accanto a {{scenarioChar \"band_peer\"}}, asciugandosi il sudore dalla fronte e porgendo una lattina fredda con un ampio sorriso.\n"
    "Russell Sinclair: \"La folla sta impazzendo per quel drop di basso, Frequency! È venuta persino la squadra di hockey. Mezza linea dei Bears è piazzata vicino all'uscita laterale.\""
)
js_g4_m2 = (
    "Dalla passerella sopraelevata che domina la pista da ballo pulsante, Alyssa Hvit Douglas Bloodmoon si sporge dalla ringhiera di ferro con uno stick luminoso in mano, sorridendo radiosa e facendo il tifo mentre la folla canta sul giro di sintetizzatore.\n"
    "Alyssa Hvit Douglas Bloodmoon: \"Il mix suona in modo incredibile da quaggiù, Jasper!\""
)
js_g4_m3 = (
    "La voce di Echo risuona nitida nelle cuffie monitor, perfettamente isolata dal boato dei subwoofer.\n"
    "Echo: \"Uscita acustica a novantotto decibel. Sensori termici sul rack amplificatori quattro entro i margini di sicurezza. Pronta a lanciare la sequenza di seconda fase al tuo segnale, Jasper.\""
)

js_g5_m1 = (
    "Scarlett Rose è appoggiata alla balaustra in legno del secondo piano, vestita con un elaborato costume da ninfa dei boschi con foglie d'alloro fresche intrecciate tra i capelli rosa confetto attorno alle sue corna scarlatte. Si volta sentendo i passi avvicinarsi e i suoi occhi rosa confetto si illuminano in un sorriso dolce e sincero sotto la luce calda delle lanterne.\n"
    "Scarlett Rose: \"Non pensavo che saresti venuto davvero a questa festa. Russ diceva che eri chiuso nella sala server tutto il pomeriggio.\""
)
js_g5_m2 = (
    "Giù nell'atrio affollato, Jared Thompson solleva una gigantesca zucca intagliata piena di punch vestito da gladiatore romano, guidando un brindisi fragoroso della confraternita che rimbomba lungo lo scalone di quercia.\n"
    "Jared Thompson: \"Ai Bulls, a Halloween, e a nessuno che chiami la sicurezza del campus prima di mezzanotte!\""
)
js_g5_m3 = (
    "Russell Sinclair incrocia lo sguardo di Jasper dal pianerottolo sottostante accanto a {{scenarioChar \"band_peer\"}}, con un bicchiere in mano e un sorriso divertito prima di rituffarsi nella folla.\n"
    "Russell Sinclair: \"Vai a parlarle, amico, alla console audio quaggiù ci penso io.\""
)

JASPER_GREETINGS = [
    {
        "id": "scene-jasper-welcome-day",
        "name": "SUCC Welcome Day",
        "description": "26 agosto 2024. Welcome Day sul Lunar Quad della SUCC: l'arrivo con tutta la famiglia (Noah, Malachia, Jasper, Alyssa, Erik, Logan ed Edric), Wulfnic con la maglietta gag che iscrive Zefir in versione punk come cugino dall'Islanda, e l'incontro con Scarlett, Sierra e Finn.",
        "messages": [
            {"id": "msg-js-0-1", "speaker_slot": "father", "content": js_g0_m1},
            {"id": "msg-js-0-2", "speaker_slot": "maternal_grandfather", "content": js_g0_m2},
            {"id": "msg-js-0-3", "speaker_slot": "brother", "content": js_g0_m3}
        ],
        "speaker_slot": "father",
        "content": js_g0_m1,
        "linked_persona_ids": [JASPER_PERSONA_ID]
    },
    {
        "id": "scene-jasper-wyrm-304",
        "name": "01. Wyrm Hall Suite 304",
        "description": "Resina per saldature, macchinette da tatuaggio, le battute di Russ Sinclair ed Echo che rileva anomalie sulla rete del campus.",
        "messages": [
            {"id": "msg-js-1-1", "speaker_slot": "cousin", "content": js_g1_m1},
            {"id": "msg-js-1-2", "speaker_slot": "cousin", "content": js_g1_m2},
            {"id": "msg-js-1-3", "speaker_slot": "cousin", "content": js_g1_m3}
        ],
        "speaker_slot": "cousin",
        "content": js_g1_m1,
        "linked_persona_ids": [JASPER_PERSONA_ID]
    },
    {
        "id": "scene-jasper-roof-hack",
        "name": "02. Sessione di Hacking sul Tetto di Wyrm Hall",
        "description": "Brezza notturna sul tetto di ghiaia, antenna parabolica direzionale fissata alla ringhiera e intrusione nella telemetria del campus.",
        "messages": [
            {"id": "msg-js-2-1", "speaker_slot": "brother", "content": js_g2_m1},
            {"id": "msg-js-2-2", "speaker_slot": "brother", "content": js_g2_m2},
            {"id": "msg-js-2-3", "speaker_slot": "brother", "content": js_g2_m3}
        ],
        "speaker_slot": "brother",
        "content": js_g2_m1,
        "linked_persona_ids": [JASPER_PERSONA_ID]
    },
    {
        "id": "scene-jasper-quad-tension",
        "name": "03. Tensione sul Prato Centrale",
        "description": "Confronto vicino alla fontana di granito con Vincent Campbell, disinnescato dall'intervento di Jared Thompson e Stan.",
        "messages": [
            {"id": "msg-js-3-1", "speaker_slot": "eldest_brother", "content": js_g3_m1},
            {"id": "msg-js-3-2", "speaker_slot": "eldest_brother", "content": js_g3_m2},
            {"id": "msg-js-3-3", "speaker_slot": "brother", "content": js_g3_m3}
        ],
        "speaker_slot": "eldest_brother",
        "content": js_g3_m1,
        "linked_persona_ids": [JASPER_PERSONA_ID]
    },
    {
        "id": "scene-jasper-warehouse-rave",
        "name": "04. Rave Underground di DJ Frequency al Porto",
        "description": "Subwoofer che fanno tremare le ossa, luci stroboscopiche e il live set di DJ Frequency nel capannone sul canale.",
        "messages": [
            {"id": "msg-js-4-1", "speaker_slot": "band_peer", "content": js_g4_m1},
            {"id": "msg-al-4-2", "speaker_slot": "band_peer", "content": js_g4_m2},
            {"id": "msg-js-4-3", "speaker_slot": "band_peer", "content": js_g4_m3}
        ],
        "speaker_slot": "band_peer",
        "content": js_g4_m1,
        "linked_persona_ids": [JASPER_PERSONA_ID]
    },
    {
        "id": "scene-jasper-bro-halloween",
        "name": "05. Festa di Halloween della Beta Rho Omega",
        "description": "Festeggiamenti di Halloween nella villa a tre piani dei BRO, lanterne intagliate e un momento con Scarlett Rose sulla balconata.",
        "messages": [
            {"id": "msg-js-5-1", "speaker_slot": "band_peer", "content": js_g5_m1},
            {"id": "msg-js-5-2", "speaker_slot": "eldest_brother", "content": js_g5_m2},
            {"id": "msg-js-5-3", "speaker_slot": "band_peer", "content": js_g5_m3}
        ],
        "speaker_slot": "band_peer",
        "content": js_g5_m1,
        "linked_persona_ids": [JASPER_PERSONA_ID]
    }
]

def apply_italian_greetings():
    for g_list in [ALYSSA_GREETINGS, JASPER_GREETINGS]:
        for g in g_list:
            assert g['speaker_slot'] == g['messages'][0]['speaker_slot']
            assert g['content'] == g['messages'][0]['content']
            for m in g['messages']:
                assert '—' not in m['content'], f"Em-dash found in {m['id']}"
                assert '*' not in m['content'], f"Asterisk found in {m['id']}"

    with open(ALYSSA_PATH, 'r', encoding='utf-8') as f:
        al_data = json.load(f)
    al_data['greetings'] = ALYSSA_GREETINGS
    with open(ALYSSA_PATH, 'w', encoding='utf-8') as f:
        json.dump(al_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Saved {len(ALYSSA_GREETINGS)} Italian greetings to {ALYSSA_PATH.name}")

    with open(JASPER_PATH, 'r', encoding='utf-8') as f:
        js_data = json.load(f)
    js_data['greetings'] = JASPER_GREETINGS
    with open(JASPER_PATH, 'w', encoding='utf-8') as f:
        json.dump(js_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Saved {len(JASPER_GREETINGS)} Italian greetings to {JASPER_PATH.name}")

if __name__ == "__main__":
    apply_italian_greetings()
