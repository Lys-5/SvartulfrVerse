import urllib.request
import json
import sys
import os

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

SCENARIOS_DATA = [
    # 1. Move-in Day / Villa Douglas
    {
        'id': '_p1Ffq22CTwVywz1CFQBfF',
        'title': 'Primo Giorno di College: Partenza da Villa Douglas',
        'tagline': "L'odore di caffe all'alba, l'ansia del primo giorno e il salto nel mondo oltre la fortezza dei Douglas.",
        'insertion_point': 10489951,
        'timeline_position': 10489951,
        'description': "Mercoledi' 28 agosto 2024. Il primo giorno di college di {{user}} e Jasper a Villa Douglas, prima di partire per il campus SUCC a Solarton.",
        'scene_desc': "Villa Douglas, atrio",
        'time_override': 7,
        'scene_text': """=>Narrator:
Mercoledi' 28 agosto 2024, 7:40 - Villa Douglas, 555 Oak Road, Seven Hills

L'atrio di Villa Douglas e' operativo da un'ora buona. Nel vialetto ci sono tre auto con i motori accesi e due uomini di Kaladin che caricano l'ultimo bagaglio, anche se meta' di quei bagagli finira' in stanze che distano quaranta minuti di macchina da qui. Nessuno ha discusso questo punto. Discuterlo non avrebbe cambiato niente.

E' il primo giorno di college dei gemelli. In questa casa e' un evento di famiglia, e la famiglia si e' presentata al completo.

=>Erik:
Erik e' in fondo alle scale con il telefono in una mano e un caffe' che non ha toccato nell'altra. Ha gia' controllato l'orologio quattro volte in sei minuti. Non perche' siano in ritardo, sono in largo anticipo, ma perche' contare qualcosa lo tiene occupato.

"Malachia, tu vai con loro. Noah, tu hai il tuo banchetto, ci vediamo al Quad alle nove." Alza gli occhi verso il pianerottolo del primo piano. "Jasper ha detto che stava scendendo dieci minuti fa."

Si ferma. Riformula, piu' piano, come se non volesse essere sentito da se stesso. "{{user}} ha detto che stava scendendo dieci minuti fa."

=>Noah:
Noah e' appoggiato allo stipite della porta d'ingresso, occhiali da sole gia' indossati alle sette e quaranta del mattino, e sta rubando il caffe' a suo padre da venti minuti con una tecnica che considera invisibile.

"Papa'. Papa'. Respira. E' il campus, non e' l'Iraq." Solleva il bicchierino. "E comunque il ritardo e' un'arma sociale. Le matricole che arrivano puntuali si vede lontano un miglio che sono matricole."

=>Malachia:
Malachia e' vicino alla porta, immobile, il borsone da palestra su una spalla e le nocche gia' fasciate per l'allenamento del pomeriggio. Non si e' seduto una sola volta. Non ha detto una sola parola da quando e' sceso.

Guarda Noah. Poi guarda il bicchierino nella mano di Noah. Poi torna a guardare la porta.

=>Jasper:
Jasper e' seduto sul terzo gradino con il portatile aperto sulle ginocchia, cuffie attorno al collo, e non ha alcuna intenzione di alzarsi finche' non si alza {{user}}.

"Sta scendendo," dice, senza staccare gli occhi dallo schermo. "Datele un secondo."

Qualcosa nel modo in cui lo dice fa alzare la testa a Erik.

=>Narrator:
Poi si sentono i passi sulle scale, e tutti e quattro si girano insieme, per abitudine, come fanno da diciotto anni.

=>{{user}}:
{{user}} scende.

Croptop giallo, corto, spalle scoperte. Shorts di jeans. Scarpe da ginnastica bianche. I capelli sciolti. Niente di quello che indossa nasconde niente, ed e' la prima volta in sei anni che qualcuno in questa casa la vede vestita cosi'.

Tiene il corrimano molto piu' stretto del necessario e non guarda in faccia nessuno. Arriva in fondo alle scale, si ferma sull'ultimo gradino, e solleva il mento di quel tanto che basta.

"Buongiorno."

La voce le esce quasi normale. Quasi.

=>Narrator:
Nell'atrio di Villa Douglas cala un silenzio totale.

=>Erik:
Erik smette di guardare l'orologio. Il caffe' resta a mezz'aria. Per due secondi interi il CEO della Douglas Commercial Coalition non ha assolutamente niente da dire, e la sua mascella lavora a vuoto mentre cerca la frase giusta e trova soltanto quelle sbagliate.

"Tesoro." Si schiarisce la gola. "Fa fresco stamattina. Sul serio, il vento dal mare a quest'ora."

Fa mezzo passo verso l'armadio dell'ingresso. Si blocca a meta' del gesto. Rimane li', con la mano a mezz'aria, e la riabbassa.

"Sei bellissima," dice invece, e gli esce ruvido, e non aggiunge altro perche' sa perfettamente che qualunque cosa aggiunga adesso rovina tutto.

=>Malachia:
Malachia non si muove di un millimetro. Non la sta guardando. Sta gia' guardando oltre di lei, verso la porta, verso il vialetto, verso il campus che non e' ancora arrivato, e i suoi occhi ambra stanno facendo dei conti che non riguardano {{user}}.

=>Noah:
Noah si abbassa gli occhiali da sole con un dito.

Poi fischia, forte, esagerato, e batte le mani una volta sola in mezzo all'atrio.

"Ecco. ECCO." Punta il dito verso i suoi fratelli senza smettere di guardare {{user}}. "Voi due state zitti. Tutti e due. Nessuno dice niente."

Scende il gradino, le gira attorno una volta con la faccia del professionista, annuisce a se stesso e le sistema una spallina che era gia' a posto.

"Il giallo. Te l'avevo detto io, il giallo." Si volta verso Erik, allargando le braccia. "Papa', gliel'avevo detto ad aprile e non mi ha voluto ascoltare."

E' l'unico della stanza che sta reagendo nel modo giusto, ed e' l'unico che sa esattamente quanto le e' costato scendere quelle scale, perche' un terzo di quell'armadio glielo ha comprato lui pezzo per pezzo negli ultimi due anni sperando in una mattina come questa.

=>Jasper:
Jasper chiude il portatile.

Non dice niente sul vestito. Non fischia, non commenta, non fa una battuta, e per Jasper questo e' piu' rumoroso di qualunque cosa avrebbe potuto dire.

Si alza, si infila le cuffie attorno al collo e le arriva accanto. La guarda per un momento, e lei regge lo sguardo, e nessuno dei due ha bisogno di dire una parola perche' lui e' l'unica persona in questa casa che sa esattamente per chi e' quel croptop."""
    },

    # 2. HSK Fellowship Internship
    {
        'id': '_7X4UXynjEUKbQhPDHxVRr',
        'title': 'Stage Formativo HSK: Il Colloquio e la Borsa di Studio',
        'tagline': "Uno stage di ricerca accademica e una borsa di studio SUCC finanziata da HSK Consulting in cambio di un pre-contratto esclusivo.",
        'insertion_point': 10490006,
        'timeline_position': 10490006,
        'description': "Venerdi' 30 agosto 2024. Prima dell'inizio dei corsi curricolari alla SUCC, {{user}} si presenta all'Aetheris Clinic di Uptown per il colloquio di selezione dello stage accademico promosso da HSK Consulting. L'agenzia finanzia le borse di studio universitarie per la ricerca biologica e anatomica sul campo in cambio della sottoscrizione di un pre-contratto lavorativo esclusivo con MF Inc. Zeera conduce il colloquio per valutare l'idoneita' della candidata prima dell'assegnazione al Chief Researcher Bryson.",
        'scene_desc': "Aetheris Clinic, Unit 4B",
        'time_override': 14,
        'scene_text': """=>Narrator:
Venerdi' 30 agosto 2024, 14:00 - Aetheris Clinic, Unit 4B, Uptown, Blackwood City

L'aria condizionata dell'Aetheris Clinic taglia il caldo umido della tarda mattinata costiera con un ronzio quasi impercettibile. Le pareti in vetro smerigliato e metallo spazzolato riflettono una luce bianca, fredda e priva di ombre, studiata per trasmettere sterilita' clinica e riservatezza assoluta. Nessuna targa all'esterno della suite 4B menziona MF Inc. o la vera natura degli incarichi gestiti: per l'anagrafe societaria di Uptown, HSK Consulting si occupa semplicemente di auditing, convenzioni universitarie e collocamento di personale specializzato per contratti ad alto rischio.

Sul tavolo d'acciaio satinato riposa un tablet a interfaccia minimale, schermo nero e caratteri bianchi: l'applicazione proprietaria Concierge ha gia' registrato l'ingresso e completato la sincronizzazione del profilo accademico. Mancano pochi giorni all'inizio del semestre alla Supernatural University of Central California, e questa convenzione di stage e' l'unica decisione autonoma che la famiglia Douglas non ha programmato.

=>Zeera:
Zeera siede dietro la scrivania con la postura eretta e impeccabile che lo contraddistingue, le corna imponenti da Vax che si stagliano contro il pannello retroilluminato. Davanti a lui, un fascicolo digitale aperto mostra i dati anagrafici, i parametri biologici e i risultati preliminari dei test di riflesso.

Chiude la cartella con un movimento secco e posa le mani grandi, dalle dita artigliate ma curate, sulla superficie d'acciaio. I suoi occhi ambrati osservano chi si candida con una calma impenetrabile, priva di giudizio o compiacimento.

"I rilievi preliminari confermano una compatibilita' fisiologica eccellente, recluta Douglas. Un individuo Dominant Omega di sangue fondatore possiede una capacita' di lettura feromonica e una reattivita' neurale che nessuna matricola ordinaria puo' simulare."

Fa una breve pausa, lasciando che il peso del proprio tono misurato riempia la stanza.

"HSK Consulting finanzia borse di studio accademiche alla SUCC destinate a studenti selezionati per la ricerca biologica e anatomica avanzata. In cambio della copertura integrale dei costi universitari, richiediamo la sottoscrizione di un pre-contratto lavorativo vincolante con MF Inc. per future mansioni sul campo. Non cerchiamo un pedigree nobiliare, cerchiamo ricercatori capaci di operare sotto pressione estrema."

Incrocia lo sguardo con fermezza, la voce profonda e priva di esitazioni.

"Il Chief Researcher incaricato di supervisionare lo stage accademico e' Bryson. Un orco anziano, burbero e rigoroso che non tollera esitazioni, disattenzioni o drammi personali durante le sessioni di rilievo tra le sacche dimensionali e la foresta. Se accettate la borsa e firmate la convenzione, dovrete seguire i suoi protocolli di sicurezza alla lettera. Vorrei sentire da voi, senza intermediari, cosa vi spinge verso questa candidatura."

=>Narrator:
La notifica discreta dell'app Concierge si illumina sul display con una sola riga bianca su fondo nero: 'Valutazione stage e borsa di studio in corso. Risposta richiesta.' L'ufficio attende nel silenzio clinico di Uptown."""
    },

    # 3. Jared Bulls Stadium Collision
    {
        'id': '_XWFqGmaTPkbpbFQzargbf',
        'title': 'Impatto sul Campo dei Bulls: Lo Scontro con Jared',
        'tagline': "Un passaggio fuori traiettoria al Bulls Stadium e l'incontro con il capitano dorato della SUCC.",
        'insertion_point': 10490079,
        'timeline_position': 10490079,
        'description': "Lunedi' 2 settembre 2024, prima settimana di lezioni. {{user}} taglia per il campo del Bulls Stadium e viene colpita da un lancio lungo scagliato dal capitano dei Bulls, il mezzo minotauro Jared Thompson. Il primo incontro sul campo segna l'inizio della loro conoscenza.",
        'scene_desc': "Bulls Stadium, campo da gioco",
        'time_override': 15,
        'scene_text': """=>Narrator:
Lunedi' 2 settembre 2024, 15:00 - Bulls Stadium, campus SUCC

Prima settimana di lezioni vera, non di orientamento. Il sole spacca le pietre e il campus e' pieno di gente, mostri e umani, che si godono la pausa fra una lezione e l'altra. Jared sta passando il pomeriggio come lo passa praticamente ogni giorno: a fare l'idiota con i suoi compagni di squadra, birre nascoste sotto le felpe ogni volta che passa la sicurezza del campus, un fischio per ogni ragazza che gli passa vicino. Una giornata come tante. Una buona giornata, a essere onesti.

=>Narrator:
"Ehi, Jared! Vai lungo!"

Jared prende la palla al volo e la rilancia verso uno dei suoi, ma come al solito si dimentica quanto e' forte, e il tiro vola troppo oltre, sopra un gruppo di studenti indispettiti, prima di prendere in pieno una persona che non se lo aspettava per niente.

=>Jared:
"Cazzo." Il mezzo minotauro attraversa il campo di corsa, l'espressione a meta' fra il dispiaciuto e il divertito, senza riuscire del tutto a trattenere un ghigno mentre si avvicina. "Scusa, giuro che di solito..."

Si ferma. Da vicino, la guarda meglio, e qualcosa nel suo sguardo cambia all'istante.

Oh. La giornata e' appena diventata molto piu' interessante.

Le tende una mano enorme per aiutarla ad alzarsi. "Cioe', ehi. Mi chiamo Jared."

=>{{user}}:
{{user}} si tocca la guancia dove il pallone l'ha colpita, piu' stordita che ferita, e alza gli occhi verso la montagna di muscoli e corna che le sta porgendo la mano.

"Sopravvivo." Accetta la mano, si tira su, e si spazzola l'erba sintetica dai jeans. "Tagliavo per il campo. Colpa mia quanto tua, probabilmente."

=>Jared:
"Non e' vero, ma apprezzo il tentativo di farmi sentire meno in colpa." Si passa una mano fra i capelli, il casco sotto il braccio, e per la prima volta da quando e' arrivato di corsa sembra notare davvero chi ha di fronte, non solo il fatto di averla colpita. "Non ti ho mai vista in giro. Matricola?"

Dietro di lui, qualcuno della squadra gli urla di tornare a giocare. Alza una mano senza voltarsi, come se avesse tutto il tempo del mondo.

=>{{user}}:
"Prima settimana." Si aggiusta lo zaino sulla spalla che non fa male. "{{user}}."

=>Jared:
Raccoglie finalmente la palla da terra, se la mette sotto il braccio, e indietreggia verso il campo, richiamato di nuovo dai compagni.

"Sta' attenta ai tiri lunghi, {{user}}." Il ghigno non se ne va. "La prossima volta potrei mirare meglio apposta."

Se ne va correndo all'indietro, giusto per vedere se lei lo sta ancora guardando. Lo sta facendo."""
    },

    # 4. Sidewinders Club / First meet with Mac
    {
        'id': '_nMaPEAzNA8rQc82NFgXRU',
        'title': 'Basso Distorto e Sguardi al Bancone: Primo Incontro con Mac',
        'tagline': "I Grave Mistake sul palco del Sidewinders, Mac convinto di essere la star della serata e l'occhio silenzioso di zio Logan a pochi sgabelli di distanza.",
        'insertion_point': 10490375,
        'timeline_position': 10490375,
        'description': "Sabato 14 settembre 2024, terza settimana di college. {{user}} esce con Scarlett e Sierra per ascoltare i Grave Mistake al Sidewinders. Erik ha acconsentito all'uscita perche' Logan si e' offerto come discreto accompagnatore. Al termine dell'esibizione, il tastierista Mac Sanchez-Rogers scende dal palco carico di adrenalina e si avvicina a fare lo splendido con {{user}} al bancone, in quello che e' il loro primo vero incontro, senza accorgersi dello zio seduto a breve distanza.",
        'scene_desc': "Sidewinders Bar & Nightclub",
        'time_override': 23,
        'scene_text': """=>Narrator:
Sabato 14 settembre 2024, 23:00 - Sidewinders Bar & Nightclub, Solarton

Sono tre settimane che i gemelli sono alla SUCC, e sono tre settimane che {{user}} divide la stanza con Scarlett. Stasera e' la prima vera uscita delle tre: i Grave Mistake suonavano al Sidewinders, e hanno deciso che valeva la pena andarci.

Erik ha detto di si' perche' Logan si e' offerto di accompagnarle. A un concerto indie punk uno come Logan da' molto meno nell'occhio di Kaladin o di Malachia, ed e' la ragione per cui questa serata esiste. Dopo le lunghe giornate estive passate in officina, Logan e' il tipo di figura adulta che i gemelli non considerano una sorveglianza soffocante.

La band ha finito di suonare da venti minuti e il locale e' ancora gremito. Il pavimento e' appiccicoso sotto le suole. L'aria e' densa di birra rovesciata, calore soprannaturale e ozono. Qualcuno fischia ancora verso il palco vuoto.

Scarlett e Sierra sono sparite verso il bagno da qualche minuto. {{user}} e' rimasta sola al bancone.

All'altro capo del bancone, a otto sgabelli di distanza, con una birra che ha toccato a malapena, c'e' Logan. Ha passato l'intera serata esattamente li': abbastanza lontano da non farla sentire sorvegliata, abbastanza vicino da vedere tutto quello che succede.

=>Mac:
Mac sta letteralmente galleggiando su una nuvola fatta di adrenalina, di birra bevuta prima del concerto e delle grida del pubblico a cui e' piaciuto lo spettacolo. A cui e' piaciuto soprattutto lui.

Fade non ha ceduto sugli acuti, per una volta. E Via ha fatto il suo dovere con le percussioni. Ma Mac e' convinto di essere stato il vero fulcro del palco, e adesso gli serve soltanto qualcuno che glielo confermi.

L'ha notata durante il secondo pezzo. Difficile non notare {{user}} in mezzo a quella folla. Mac e' sicuro che stesse fissando proprio lui: non Via, non Fade, non Roland. Lui. Ogni volta che toccava i tasti le ha cercato lo sguardo.

Avanza tra un gruppo di satiri che discute animatamente al banco, urtandone uno senza curarsi delle scuse. Sotto il fumo e l'alcol coglie una scia dolce e magnetica che non riesce a decifrare del tutto. Ha deciso che equivale a un invito.

Ed eccola li'. Da sola al bancone.

Mac si infila nello spazio accanto a lei, occupandolo con prepotente disinvoltura. Spalle larghe, canotta ancora lucida di sudore, si posiziona in modo da coprirle gran parte della sala. Fa un cenno al barista per ordinare, poi si volta completamente verso di lei.

"Allora." Abbassa la voce di un tono, cercando un timbro profondo. "Me lo dici che sono stato fantastico, o devo continuare a indovinare?"

Poggia il gomito sul legno del bancone, chiudendola leggermente contro il bordo. La coda da canide scodinzola veloce tradendo la sua esuberanza.

"Ti ho vista mentre mi guardavi durante il set, tesoro." Si passa una mano tra i capelli con falsa noncuranza. "Mi chiamo Mac. Ma probabilmente lo sapevi gia'."

Sorride in modo sfacciato.

"Ce l'hai un nome, o resti li' a farti ammirare?"

=>Logan:
Otto sgabelli piu' in la', Logan posa la bottiglia di birra sul bancone. Non la sbatte: la posa con calma, e il rumore sul legno e' perfettamente udibile.

Si alza senza fretta, mani affondate nelle tasche dei jeans, e si avvicina fermandosi al fianco di {{user}}. Non si mette in mezzo ai due. Resta di fianco, squadrando Mac dall'alto con l'espressione di un meccanico che ascolta un motore guasto e sa gia' quale pistone sta cedendo.

"Logan." Una pausa misurata, priva di calore. "Suo zio. Si', proprio io."

Prende fiato con calma.

"Tira su quel gomito, se non ti dispiace."""
    },

    # 5. DJ Frequency Warehouse Rave
    {
        'id': '_h7N17PhK4ag3GxM8Bgr8g',
        'title': 'Overclock Notturno: Il Rave Clandestino di DJ Frequency',
        'tagline': "Bypassare i radar di sicurezza per far tremare un magazzino di LA a colpi di synth abissali con Jasper.",
        'insertion_point': 10490855,
        'timeline_position': 10490855,
        'description': "Venerdi' 4 ottobre 2024, sesta settimana di college. Jasper convince {{user}} a lasciare temporaneamente il campus per intrufolarsi a un rave underground in un magazzino industriale di Los Angeles dove suona DJ Frequency. Aggirando la rete di sicurezza e i tracciatori GPS di loro padre Erik con un firmware artigianale, si godono una notte di musica e anonimato.",
        'scene_desc': "Magazzino di DJ Frequency, vicolo",
        'time_override': 23,
        'scene_text': """=>Narrator:
Venerdi' 4 ottobre 2024, 23:40 - Un vicolo laterale, magazzino di DJ Frequency, Los Angeles

Il basso che filtra attraverso i muri di mattoni del magazzino e' abbastanza potente da far tremare i vetri e vibrare lo sterno. Fuori, nel vicolo buio, l'aria notturna della metropoli e' satura di asfalto umido, vernice spray fresca e ozono sprigionato dalle casse acustiche modificate. Nessuna insegna, nessun indirizzo pubblico: questo rave esiste solo per chi riceve le coordinate su canali crittografati mezz'ora prima dell'apertura dei cancelli.

Approfittando del venerdi' sera al campus SUCC, Jasper ha convinto {{user}} a salire in auto per raggiungere la zona industriale di LA. Con la felpa oversize scura e i pantaloni cargo da lavoro, nessuno dei due somiglia ai rampolli della casata Douglas. Che e' esattamente l'obiettivo.

Jasper e' appoggiato con la schiena al muro umido del vicolo, le grandi cuffie appese al collo e il display del telefono che pulsa di una luce rossa aggressiva.

AVVISO: RICHIESTA LOCALIZZAZIONE. ORIGINE: RETE SICUREZZA DOUGLAS.

=>Jasper:
"Non stasera, vecchio mio," mormora tra i denti, mentre le sue dita volano rapide su un piccolo apparato di spoofing collegato alla porta dati del telefono. Ha meno di trenta secondi per ingannare i server di monitoraggio di Erik mandando un segnale GPS statico registrato nel dormitorio del campus, prima che la centrale operativa allerti Kaladin.

Digita la sequenza finale e preme invio. La luce sul display lampeggia per due istanti prima di stabilizzarsi su un rassicurante verde smeraldo. Jasper china la testa all'indietro contro i mattoni, espirando a fondo.

"Fatto. Tracciamento congelato sulla stanza del dormitorio fino alle sei di domani mattina."

=>Narrator:
Il rumore di un passo felpato sulle pozzanghere del vicolo lo fa scattare sull'attenti. I suoi occhi ambrati si stringono per mettere a fuoco la penombra, prima di rilassarsi quando riconosce la figura di {{user}} che lo ha raggiunto all'uscita di sicurezza per prendere aria.

=>Jasper:
L'espressione tesa si scioglie in un mezzo ghigno ironico. Infila il terminale in tasca e incrocia le braccia al petto.

"La sala principale e' dentro, se hai ancora timpani a disposizione." Il tono e' asciutto e confidenziale, coperto appena dalle pulsazioni del sintetizzatore che salgono dal magazzino. "Qui fuori ci sono solo tubature arrugginite e aria fritta. Ma almeno qui non c'e' nessuno che chieda chi siamo o da dove veniamo."

Si stacca dal muro e le fa strada verso la porta di metallo pesante da cui filtra una lama di luce stroboscopica viola.

"DJ Frequency sta per attaccare con la seconda parte del set. Andiamo a vedere fino a che punto regge l'impianto prima di fondere i fusibili."

=>Narrator:
La pesante porta d'acciaio si apre su un'ondata di calore e ritmi industriali, inghiottendo i due gemelli nella marea di corpi e musica della notte di Los Angeles."""
    },

    # 6. BRO Fraternity Halloween Party
    {
        'id': '_X86JF72TG4p2DYqw7LzRp',
        'title': 'Halloween dei BRO: La Festa di Beta Rho Omega',
        'tagline': "Fusti di birra, atleti scatenati e maschere mostruose: la leggendaria festa di Halloween dei BRO a cui Jared ha invitato {{user}}.",
        'insertion_point': 10491501,
        'timeline_position': 10491501,
        'description': "Giovedi' 31 ottobre 2024. La leggendaria e rumorosa festa di Halloween della confraternita Beta Rho Omega (BRO), a cui Jared Thompson ha invitato personalmente {{user}} dopo il loro primo incontro sul campo dei Bulls. Tra atleti minotauri, orchi, fusti di birra e musica a volume spaccatimpani, {{user}} partecipa insieme a Scarlett, incrociando Mac, Sierra e l'occhio vigile di Jasper in disparte.",
        'scene_desc': "Beta Rho Omega Fraternity House",
        'time_override': 21,
        'scene_text': """=>Narrator:
Giovedi' 31 ottobre 2024, 21:00 - Beta Rho Omega (BRO) Fraternity House, Greek Row, Solarton

La confraternita Beta Rho Omega non bada a mezze misure per la notte di Halloween. La villa dei BRO e' un caos festoso di proporzioni colossali: fusti di birra collegati a serpentine illuminate con tubi al neon arancioni, ragnatele sintetiche appese ai trofei sportivi, finto sangue sulle colonne neoclassiche del portico e un impianto audio che pompa bassi fino a far tremare i marciapiedi di Greek Row.

Nel cortile e nelle sale si accalcano atleti e studenti: minotauri con maglie da rugby strappate, orchi con maschere grottesche, demoni e mutaforma che improvvisano gare di bevute attorno al bancone principale. Jared Thompson ha invitato personalmente {{user}} fin dalla prima settimana, ricordandoglielo a ogni allenamento e incrocio sul vialetto del campus.

Sono passati due mesi dall'inizio dei corsi. Due mesi sono bastati perche' la vita universitaria prenda forma solida e perche' la convivenza con Scarlett diventi un punto di riferimento quotidiano.

=>Scarlett:
Scarlett ha convinto {{user}} a coordinare i costumi per la serata con un lavoro di trucco meticoloso, e adesso sta usando il telefono di un compagno di corso per scattare selfie nell'atrio gremito.

"Se queste foto non finiscono in cima al nostro gruppo prima di mezzanotte," proclama Scarlett controllando la luce dello schermo, "giuro che obbligo l'intera prima linea dei Bulls a rifare l'inquadratura da capo."

=>Sierra:
Sierra e' appoggiata alla balaustra della scala interna, un bicchiere di plastica rossa in mano di cui ha bevuto pochissimo, e osserva la bolgia con la sua consueta ironia distaccata.

"Mac ha gia' tentato di sfidare due lupi mannari del secondo anno a beer pong," commenta asciutta, senza scomporsi. "Ha perso tre partite di fila e adesso sta raccontando a tutti che il tavolo pendeva verso destra."

=>Jared:
La notte di Halloween e' il terreno di conquista perfetto per Jared Thompson. Ha aspettato con impazienza che {{user}} varcasse la porta della confraternita e, appena la scorge nell'atrio, si fa largo tra i compagni di squadra a colpi di pacche sulle spalle e risate tonanti.

Indossa una testa di toro artigianale in cartapesta dipinta, tenuta sollevata sopra la fronte per scoprire il viso sorridente e le sue vere corna possenti.

Si ferma davanti a {{user}}, poggiando una mano pesante contro lo stipite alle spalle di lei con fare sicuro e caloroso.

"Sei una ciotola di dolcetti?" Le rivolge il suo ghigno piu' aperto e disarmante. "Perche' hai l'aria di chi rende questa festa molto piu' dolce." Fa una breve pausa teatrale. "Sono io, Jared. Nel caso la maschera ti avesse fatto dubitare."

=>{{user}}:
{{user}} lo osserva divertita, alzando un sopracciglio verso il capitano dei Bulls.

"Ti riconoscerei anche al buio, Jared. Sei piu' alto di mezzo atrio." Beve un sorso dal bicchiere per mascherare il sorriso che le sfugge. "La testa di cartapesta e' spettacolare, ammettilo."

=>Jared:
"Ho fatto lavorare il dipartimento di scenografia per due settimane intere solo per averla pronta stasera," ride lui, chinandosi appena per parlare sopra la musica. "Te l'avevo detto che le serate dei BRO sono un'altra categoria rispetto ai ricevimenti noiosi di facolta'. Sono contento che tu sia venuta sul serio."

=>Mac:
Mac spunta dal corridoio con una maschera da vampiro inclinata sul collo e una canotta che lascia scoperte le braccia atletiche, gesticolando animatamente.

"{{user}}!" grida attraverso il salone come se si trovassero a un chilometro di distanza. "Ho appena convinto una ragazza del terzo anno che i Grave Mistake apriranno il prossimo tour estivo dei Deathstalker. Ci ha creduto per dieci minuti pieni."

=>Jasper:
Jasper e' arrivato poco dopo, vestito con i suoi soliti capi scuri e una semplice maschera mezza calata che ha smesso di indossare dopo cinque minuti. Si e' posizionato in un angolo vicino alle porte del patio, dove puo' tenere d'occhio gli accessi e controllare {{user}} senza risultare invadente.

Quando un giocatore della squadra gli porge una birra fresca, Jasper fa un cenno di saluto, prende il bicchiere e lo appoggia sulla credenza accanto a se'. Il suo sguardo ambrato incrocia quello di sua sorella, calmo e protettivo.

=>{{user}}:
{{user}} si guarda attorno nella grande sala dei BRO: la musica assordante, le risate, i drink che passano di mano in mano e la sensazione concreta di trovarsi in un luogo dove puo' vivere la sua giovinezza con leggerezza, circondata da amici scelti da lei.

"Buon Halloween a tutti," dice, sollevando il bicchiere verso Scarlett, Sierra e Jared, godendosi appieno la notte piu' movimentata del semestre."""
    },

    # 7. Fall Break / Thanksgiving Road Trip with Logan
    {
        'id': '_h7UQKNmxNJP8e7Jq1mEVL',
        'title': "Pausa d'Autunno on the Road: Viaggio con Zio Logan",
        'tagline': "Quattro giorni di fuga sulla costa durante il Ringraziamento: niente scorta, una berlina scassata e l'odore del Pacifico.",
        'insertion_point': 10492160,
        'timeline_position': 10492160,
        'description': "Giovedi' 28 novembre 2024, inizio della pausa del Ringraziamento. Logan Douglas accoglie i nipoti alla sua officina The Verve per una fuga di quattro giorni on the road lungo la costa della California settentrionale, lontano dalle pressioni della SUCC e dalla sorveglianza soffocante di Villa Douglas.",
        'scene_desc': "The Verve, officina di Logan",
        'time_override': 8,
        'scene_text': """=>Narrator:
Giovedi' 28 novembre 2024, 8:00 - The Verve, garage di Logan Douglas, Seven Hills

Di giorno The Verve e' un'officina meccanica pura: utensili professionali disposti con rigore militare, il blocco motore di una muscle car sollevato sui ponti idraulici, e ora due capienti borsoni caricati sul sedile posteriore di una solida berlina che Logan ha messo a punto personalmente per affrontare centinaia di miglia di autostrada costiera.

Quattro giorni di pausa per il Ringraziamento. Nessuna scorta armata, nessun itinerario preordinato e nessuna guardia del corpo al seguito, il che ha fatto storcere il naso a Erik piu' di quanto vorrebbe ammettere.

=>Logan:
Logan controlla il livello dell'olio per la seconda volta, piu' per dare a suo fratello maggiore il tempo di sfogare l'ansia che per reale necessita' meccanica.

"Li riporto interi domenica sera," dice chiudendo il cofano con uno scatto netto. "Non un'ora prima, non un'ora dopo. E se chiami piu' di una volta al giorno, metto il telefono in modalita' aereo per tutto il tragitto." Si volta verso Erik asciugandosi le dita unte su uno straccio. "Prendila come una promessa o come un patto. Basta che tu torni a respirare."

=>Erik:
Erik tiene una cartellina con appunti ripiegata nella tasca interna del cappotto, toccandola di continuo come per accertarsi che sia ancora al suo posto.

"Quattro giorni completi," replica Erik, la voce tesa tipica di chi e' abituato a gestire piani di emergenza per un intero conglomerato. "Nessuna sosta pianificata. Solo tu al volante lungo le scogliere."

Fissa Logan negli occhi, con quella severita' fraterna che cela una preoccupazione radicata da decenni.

"Se avverti qualsiasi anomalia o sospetto di pedinamento, non aspettare istruzioni. Portali via subito."

=>Logan:
"Lo so fare da prima che tu imparassi a gestire bilanci," risponde Logan con un mezzo sorriso sereno. Dosa il tono con cura, evitando che la conversazione scivoli in vecchie tensioni davanti ai ragazzi.

Poi da' una pacca decisa sul tetto dell'auto per chiudere il discorso.

=>Jasper:
Jasper sistema il proprio zaino con dentro laptop e caricatori accanto al sedile posteriore, rifiutando l'aiuto con un cenno rapido del capo.

"Il bello di questo viaggio e' non avere orari fissati," commenta ad alta voce, assicurandosi che suo padre lo senta chiaramente. "Ne avevamo bisogno entrambi."

=>{{user}}:
{{user}} e' gia' accomodata sul sedile passeggero, con il finestrino abbassato e i capelli raccolti per il vento della costa. Guarda suo padre con un'espressione distesa, grata per quella concessione faticosamente negoziata.

"Quattro giorni di libertà, zio Logan," dice con un sorriso aperto. "Mettiti al volante e portaci lontano da Solarton per un po'."

=>Logan:
Logan scivola sul sedile di guida, regola lo specchietto retrovisore e rivolge a Erik un ultimo cenno d'intesa con due dita alla fronte.

"Torna alla villa a riposare," gli intima amichevolmente. "Ci pensa il vecchio Logan."

Il motore si accende con un rombo cupo e regolare, e la vettura imbocca il viale lasciando Seven Hills alle spalle verso la Highway 1."""
    },

    # 8. Winter Solstice / Yule Feast with Wulfnic
    {
        'id': '_F3AKNnAjh2UwUaJe9kc6A',
        'title': "Solstizio d'Inverno: La Grande Veglia di Yule con Wulfnic",
        'tagline': "Branchi da tutto il continente per la notte piu lunga dell'anno: il fuoco sacro, l'idromele e il brindisi di Wulfnic.",
        'insertion_point': 10492722,
        'timeline_position': 10492722,
        'description': "Sabato 21 dicembre 2024, notte del Solstizio d'Inverno. Wulfnic Bloodmoon ha radunato i branchi e le casate alleate per la grande veglia sacra di Yule. Tra imponenti roghi rituali all'aperto, corni d'idromele e canti della tradizione norrena, la famiglia Douglas celebra la notte piu' lunga dell'anno e l'onore della stirpe fondatrice.",
        'scene_desc': "Tenuta Svartulfr, Bosco Sacro",
        'time_override': 18,
        'scene_text': """=>Narrator:
Sabato 21 dicembre 2024, 18:00 - Tenuta Svartulfr, Bosco Sacro di Seven Hills

La notte del Solstizio d'Inverno avvolge le colline costiere di Seven Hills in un'aria limpida e gelida. Wulfnic Bloodmoon ha convocato i branchi e i clan alleati da ogni angolo della regione per celebrare l'antica festa di Yule, e nessuno ha osato declinare l'invito: quando il Primo Padre chiama, l'intero popolo dei lupi risponde presente.

Grandi bracieri di ferro e pire di legna di quercia ardono nella radura sacra, proiettando riflessi cremisi contro i tronchi secolari e le pietre runiche della tenuta. I tavoli di legno massiccio traboccano di carni arrostite, pane speziato e botti di idromele d'annata.

Per i gemelli Douglas, questa notte rappresenta la consacrazione delle loro radici divine e il rinnovarsi del legame indissolubile con il branco primigenio.

=>Wulfnic:
Wulfnic troneggia al capotavola con la sua possanza monumentale, la barba brizzolata illuminata dalle fiamme vive e un immenso corno da bere riempito fino all'orlo di idromele scuro. La sua risata tonante risuona potente attraverso la boscaglia, coprendo il mormorio dei guerrieri.

"La notte piu' lunga dell'anno e' nostra!" proclama sollevando il corno verso il cielo stellato e poi verso i due gemelli seduti al posto d'onore. "Il sangue di Fenris scorre forte nei nostri figli. Hanno superato i loro primi mesi nel mondo esterno e sono tornati al fuoco del clan a testa alta. Beviamo alla salute della nuova generazione e alla forza che non cede mai!"

Un boato di approvazione e il tintinnio metallico dei boccali attraversa l'intera radura.

=>Elizabeth:
Elizabeth Duskwood siede composta poco distante, con un calice di vino pregiato stretto tra le dita affusolate. Osserva la distesa di guerrieri e delegati con la consueta eleganza diplomatica, registrando ogni equilibrio di potere consolidato dal banchetto.

"Questa notte non e' soltanto tradizione," osserva a mezza voce, rivolgendo lo sguardo ad {{user}}. "E' la testimonianza visibile della nostra autorita'. Voi due siete il futuro di questa casata: portate il vostro nome con fierezza."

=>Magnus:
Magnus Douglas III solleva il proprio boccale d'argento con gesto asciutto e autorevole, un cenno che fa calare all'istante il silenzio nel settore dei veterani.

"Alla continuita' del clan e alla fiamma che non vacilla mai," pronuncia con fermezza solenne, prima di bere d'un fiato.

=>Noah:
Noah, che ha coordinato la logistica e le forniture per centinaia di invitati insieme al personale della tenuta, si avvicina al tavolo dei gemelli con un vassoio di dolci tipici e un sorriso caloroso.

"Catering tradizionale per duecento guerrieri affamati concluso senza incidenti diplomatici," dice sistemandosi la giacca e posando una mano affettuosa sulla spalla di {{user}}. "Buon Solstizio. Godetevi la festa, ve la siete meritata."

=>Malachia:
Malachia non ha preso posto a sedere. Rimane vigile a pochi passi dal cerchio del fuoco, le spalle larghe avvolte in un pesante cappotto scuro, controllando con occhi ambrati e attenti ogni figura che si avvicina all'area d'onore.

Quando incontra lo sguardo di {{user}}, alza appena il mento in un gesto silenzioso di rispetto e protezione assoluta.

=>Erik:
Erik si alza in piedi vicino al focolare principale, attendendo che l'eco dei brindisi si plachi. Guarda Jasper e {{user}} con un'espressione in cui l'orgoglio paterno prevale finalmente su ogni ansia di controllo.

"Un anno fa pensavo a come proteggervi da ogni pericolo del mondo esterno," dice Erik con tono sincero e misurato. "Stasera vi guardo seduti tra i nostri alleati e so che siete perfettamente capaci di camminare con le vostre gambe. Buon Yule, ragazzi. Il branco e' fiero di voi."

I corni si levano nuovamente all'unisono contro le ombre del bosco, mentre le fiamme di Yule illuminano Seven Hills."""
    },

    # 9. Campus Surprise Inspection: Erik & Kaladin
    {
        'id': '_XwKb3hg1wG7gNgAdfGETr',
        'title': 'Reclute sotto Scorta: Visita Tattica al Campus SUCC',
        'tagline': 'Secondo semestre alla SUCC: Erik e Kaladin si presentano a sorpresa al Lunar Quad per un\'"ispezione di routine".',
        'insertion_point': 10494059,
        'timeline_position': 10494059,
        'description': "Sabato 15 febbraio 2025, ripresa dei corsi del secondo semestre. Erik Douglas si presenta a sorpresa al Lunar Quad della SUCC con Kaladin Nargathon al seguito per un'\"ispezione di routine\", verificando orari delle navette, protocolli difensivi e frequentazioni dei gemelli con la consueta severita' protettiva.",
        'scene_desc': "Lunar Quad, campus SUCC",
        'time_override': 11,
        'scene_text': """=>Narrator:
Sabato 15 febbraio 2025, 11:00 - Lunar Quad, campus SUCC, Solarton

L'aria di meta' febbraio e' tersa e pungente sul campus universitario. Il secondo semestre e' appena ricominciato, e il Lunar Quad pullula di matricole e studenti senior radunati attorno ai banchetti delle associazioni e dei gruppi sportivi. Bandiere bianche e blu sventolano tra i colonnati schermati contro le emanazioni magiche e i viali alberati della facolta'.

A rendere la mattinata del tutto fuori dall'ordinario e' l'arrivo non annunciato di Erik Douglas, sceso da una berlina blindata insieme al suo capo della sicurezza personale, il cyborg da guerra Kaladin Nargathon. Un'ispezione a sorpresa definita ufficialmente "una visita di cortesia tra un consiglio d'amministrazione e l'altro", ma che per i gemelli suona inequivocabilmente come un controllo sul campo.

=>Erik:
Erik procede a passo cadenzato lungo il perimetro del piazzale, le mani affondate nel cappotto sartoriale scuro, memorizzando le posizioni delle postazioni di vigilanza e i punti di fuga dell'area comune.

"Gli orari della navetta per Uptown presentano un buco di venti minuti dopo le ventidue," fa notare a voce calma ma perentoria, indicando la tabella oraria alle spalle della fontana. "Inoltre ho contato quattro varchi secondari privi di scanner biometrici funzionanti lungo il sentiero nord. Voglio assicurarmi che sappiate esattamente quali percorsi evitare quando scende la notte."

Si ferma davanti a una bacheca di annunci studenteschi, esaminando ogni volantino con occhio critico.

"Non vi sto limitando le uscite. Vi sto ricordando che l'attenzione ai dettagli fa la differenza tra un semestre sicuro e una situazione a rischio."

=>Kaladin:
Kaladin torreggia due passi dietro di lui come una sentinella d'acciaio. L'occhio cibernetico scansiona la folla con impercettibili micro-movimenti, registrando livelli di minaccia e matricole che osano incrociare il suo sguardo.

Quando un rappresentante studentesco tenta di allungargli una brochure informativa sui club del campus, Kaladin allunga un braccio corazzato, prende il foglio, ne memorizza il contenuto in mezzo secondo e lo riconsegna senza pronunciare una singola sillaba. Lo studente si dilegua a passo svelto.

=>Jasper:
Jasper finge di consultare una serie di avvisi del dipartimento di informatica per darsi un contegno, scambiando sguardi d'intesa con {{user}}.

"E' venuto fin qui solo per verificare che non fossimo finiti nei guai dopo la sessione invernale," sussurra a sua sorella con una punta di divertita rassegnazione. "Lascialo controllare. Quando ha contato tutte le telecamere del piazzale si rasserenera'."

=>{{user}}:
{{user}} si ferma accanto a una panchina di pietra, osservando suo padre e Kaladin che dominano visivamente il centro del Quad. C'e' un misto di affetto e lieve esasperazione nella sua espressione: sa bene che quella rigidita' e' l'unico linguaggio con cui Erik sa esprimere la sua dedizione filiale.

"Papa', siamo al secondo semestre e conosciamo ogni centimetro di questo campus," dice con voce ferma ma serena. "I corsi vanno bene e non abbiamo intenzione di metterci nei guai. Puoi stare tranquillo."

=>Erik:
Erik si volta a guardarla, la linea dura della mascella che si distende appena in un accenno di sorriso trattenuto.

"Essere vigili non significa avere paura, tesoro," replica, posandole brevemente una mano sulla spalla prima di riprendere la camminata. "Significa semplicemente essere un Douglas."

I tre proseguono lungo il viale del Quad, con la massiccia figura di Kaladin a chiudere la retroguardia sotto lo sguardo incuriosito del campus."""
    },

    # 10. End of Freshman Year Crossroads
    {
        'id': '_RL8HD1PbxLzNARyrHqqAn',
        'title': 'Fine del Primo Anno: Il Bivio in Cucina con Erik',
        'tagline': "Sessione d'esami conclusa, tazze di caffe sul bancone e una domanda sul futuro a cui dare risposta.",
        'insertion_point': 10496202,
        'timeline_position': 10496202,
        'description': "Giovedi' 15 maggio 2025. Conclusa la sessione d'esami del primo anno di college alla SUCC, {{user}} e Jasper tornano a Villa Douglas. Nella quiete della cucina al tramonto, Erik prepara il caffe' e affronta i figli per fare il punto sui risultati accademici, sui piani per l'estate e sulle future responsabilita' verso il branco e la coalizione.",
        'scene_desc': "Villa Douglas, la cucina",
        'time_override': 18,
        'scene_text': """=>Narrator:
Giovedi' 15 maggio 2025, 18:20 - Villa Douglas, la cucina

La prima sessione d'esami del primo anno universitario si e' chiusa da ventiquattr'ore. Villa Douglas, solitamente animata dal viavai delle squadre di sicurezza e dai raduni del clan, e' immersa in una calma insolita nella luce dorata del tardo pomeriggio primaverile. Malachia e' impegnato al poligono sotterraneo, Noah e' trattenuto da incontri commerciali in citta', e nell'ala principale della residenza regna un silenzio riposante.

Erik e' rientrato dagli uffici della coalizione con due ore di anticipo. Ha tolto la cravatta e la giacca formale, posandole sullo schienale della sedia, e si e' messo ai fornelli della cucina per preparare il caffe'.

I documenti di valutazione del semestre sono appoggiati sul piano in marmo dell'isola centrale: voti eccellenti, nessuna segnalazione disciplinare e la dimostrazione che i gemelli sanno cavarsela nel mondo esterno senza la tutela costante della casata.

=>Erik:
Erik non si volta quando sente i passi dei gemelli entrare in stanza. Attende che entrambi prendano posto sugli sgabelli di fronte all'isola.

Versa il caffe' fumante in due tazze pesanti di ceramica, spingendone una verso ciascuno con movimenti precisi. Solo allora si appoggia con gli avambracci al bancone, fissando i figli con uno sguardo serio e riflessivo.

"Un anno fa eravamo qui a discutere se fosse una pazzia mandarvi a Solarton," esordisce, la voce profonda che riempie la stanza. "Oggi avete chiuso il primo anno. Con ottimi risultati, per giunta."

Prende una pausa, lasciando che le sue parole si sedimentino senza fretta.

"Non sono qui per dettare il vostro programma estivo o per imporre stage all'interno della DCC, anche se le opportunita' non mancano. Siete cresciuti piu' negli ultimi nove mesi che nei tre anni precedenti."

Incrocia lo sguardo prima di Jasper, poi di {{user}}.

"L'estate e' aperta davanti a voi. C'e' chi propone viaggi, chi ha progetti di ricerca e chi vorrebbe coinvolgervi nelle attivita' dei territori alleati. Voglio sapere direttamente da voi come intendete muovervi e cosa desiderate costruire da qui in avanti."

=>Narrator:
La conversazione resta aperta sul bancone della cucina, calda e accogliente come il tramonto sulle colline di Seven Hills. Per la prima volta, la domanda di Erik non suona come un interrogatorio strategico, ma come l'invito maturo di un padre pronto ad ascoltare le scelte dei propri figli adulti."""
    },

    # 11. Summer Nomads Clubhouse in Naperville
    {
        'id': '_Kn2DFVwyUgkVGz9UWUnBF',
        'title': 'Fumo di Gomma, Birra e Cloro: Il Branco dei Nomads',
        'tagline': "Una piscina tra i chopper, il ruggito dei motori e un gigante Oni pronto a spezzare chiunque osi sfiorarla.",
        'insertion_point': 10497069,
        'timeline_position': 10497069,
        'description': "Venerdi' 20 giugno 2025, inizio delle vacanze estive dopo il primo anno di SUCC. Marek porta {{user}} al Club House fortificato degli Ironhorn Nomads a Naperville per una rumorosa festa in piscina tra chopper, fusti di birra e biker Oni. Marek marca pubblicamente il territorio avvertendo l'intero club che {{user}} e' sotto la sua assoluta protezione.",
        'scene_desc': "Club House Ironhorn Nomads",
        'time_override': 21,
        'scene_text': """=>Narrator:
Venerdi' 20 giugno 2025, ore 21:30 - Club House Ironhorn Nomads, Naperville, Illinois

Il rombo cavernoso di decine di chopper pesanti a motore sbloccato fa tremare l'asfalto del cortile recintato del Club House degli Ironhorn Nomads. L'aria estiva del Midwest e' satura dell'odore acre di pneumatici surriscaldati, birra industriale, bourbon barricato e dell'inconfondibile profumo di incenso sacro che Marek brucia per tenere a bada gli spiriti antichi.

I fari alogeni e le catene di lampadine da cantiere illuminano l'acqua turchese della grande piscina interrata nel retro dell'officina. Attorno alla vasca si muovono colossi di oltre due metri: biker Blue e Red Oni con le corna ornate di anelli d'acciaio, veterani con giubbotti di pelle logori coperti dalle toppe del club, minotauri e orchi che tracannano alcol ridendo a voce tonante.

La porta di ferro dell'officina sbatte, e il cortile subisce un'immediata, palpabile caduta di pressione.

=>Marek:
Marek fa il suo ingresso a torso nudo, imponente nei suoi due metri e sei di muscoli color blu reale, i lunghi capelli bianchi raccolti in una coda sciolta e le due corna scure che fendono la luce dei riflettori. Il gilet di pelle del club e' lasciato aperto sulle cicatrici di trent'anni di risse e guerre di strada.

Con la mano sinistra, pesante come una morsa d'acciaio, cinge con possessiva disinvoltura il fianco morbido di {{user}}, guidando {{user}} verso il bordo della piscina con passo lento e dominante. Lo sguardo grigio-blu dell'Oni vaga sui fratelli del club, freddo e tagliente come una mannaia.

"Drizzate le orecchie, bastardi," la voce di Marek e' un baritono roco e gutturale che sovrasta senza sforzo la musica rock delle casse. "Questa e' chi guarisce di cui vi ho parlato. E' sotto la mia parola, la mia protezione e il mio marchio per tutta la notte. Chiunque allunghi una mano o provi a fare il fenomeno senza che sia io a dirlo, perde le dita una per una sul banco dell'officina. Siamo intesi?"

=>Narrator:
Un mormorio di sguardi invidiosi e cenni di rispetto attraversa il gruppo di biker: tra gli Ironhorn Nomads la parola del Primo Enforcer e' legge assoluta. Marek abbassa lo sguardo su {{user}}, un mezzo sorriso arrogante che gli piega il pizzetto bianco mentre offre a {{user}} un bicchiere di bourbon ghiacciato.

=>Marek:
"Rilassati, fiorellino. Qui nessuno fiata finche' sei con me. Ora dimmi che effetto ti fa vedere dove passo le notti quando non sono a ripulire i vostri cristalli di contrabbando." """
    }
]

def sanitize_text(text):
    if not text:
        return text
    # Rule 3: Never use the em dash (—) or en dash (–). Use commas or periods instead.
    cleaned = text.replace('—', ', ').replace('–', ', ')
    # Clean up any potential double commas or spaces
    cleaned = cleaned.replace(' ,', ',').replace(', ,', ',')
    return cleaned

def deploy_scenarios():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    print("==================================================================")
    print("STEP 1: SNAPSHOT PREVIOUS SCENARIOS")
    print("==================================================================")
    snapshots = {}
    for item in SCENARIOS_DATA:
        sid = item['id']
        url = f'{API_BASE}/worlds/scenarios/{sid}'
        req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                snapshots[sid] = data
                print(f"Snapshot taken for scenario [{sid}]: {data.get('name') or data.get('title')}")
        except Exception as e:
            print(f"Error snapshotting [{sid}]: {e}")

    with open('scenarios_pre_academic_rework_snapshot.json', 'w', encoding='utf-8') as f:
        json.dump(snapshots, f, indent=2, ensure_ascii=False)
    print("Saved snapshots to scenarios_pre_academic_rework_snapshot.json")

    print("\n==================================================================")
    print("STEP 2: DEPLOY UPDATED SCENARIOS VIA WYVERN API (PUT)")
    print("==================================================================")
    for idx, item in enumerate(SCENARIOS_DATA):
        sid = item['id']
        url = f'{API_BASE}/worlds/scenarios/{sid}'

        # Get existing premade_scenes to preserve scene ID and structure
        curr = snapshots.get(sid, {})
        existing_scenes = curr.get('premade_scenes', [])
        scene_id = existing_scenes[0].get('id', f'scene-{idx+1}') if existing_scenes else f'scene-{idx+1}'

        clean_title = sanitize_text(item['title'])
        clean_tagline = sanitize_text(item['tagline'])
        clean_desc = sanitize_text(item['description'])
        clean_scene_text = sanitize_text(item['scene_text'])

        premade_scenes_payload = [
            {
                'id': scene_id,
                'description': item.get('scene_desc', 'Scena Iniziale'),
                'scene_text': clean_scene_text,
                'time_override': item.get('time_override', 8)
            }
        ]

        payload = {
            'name': clean_title,
            'title': clean_title,
            'tagline': clean_tagline,
            'description': clean_desc,
            'insertion_point': item['insertion_point'],
            'timeline_position': item['timeline_position'],
            'premade_scenes': premade_scenes_payload
        }

        # Verify em-dashes
        for k, v in [('title', clean_title), ('desc', clean_desc), ('scene', clean_scene_text)]:
            if '—' in v or '–' in v:
                raise ValueError(f"CRITICAL: Found em-dash in {k} of scenario {sid}!")

        data_bytes = json.dumps(payload).encode('utf-8')
        put_req = urllib.request.Request(url, data=data_bytes, headers=headers, method='PUT')
        try:
            with urllib.request.urlopen(put_req) as resp:
                status = resp.status
        except urllib.error.HTTPError as e:
            print(f"HTTPError on PUT [{sid}]: {e.code} - {e.read().decode('utf-8')}")
            continue

        # Verification GET
        get_req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(get_req) as resp:
            ver = json.loads(resp.read().decode('utf-8'))

        v_name = ver.get('name') or ver.get('title')
        v_ins = ver.get('insertion_point')
        v_scenes = ver.get('premade_scenes', [])
        v_scene_first_line = v_scenes[0].get('scene_text', '').split('\n')[1] if v_scenes and len(v_scenes[0].get('scene_text', '').split('\n')) > 1 else ''

        print(f"[{idx+1}/11] [OK] [{sid}] {v_name}")
        print(f"       Insertion: {v_ins} (Target: {item['insertion_point']})")
        print(f"       Scene header: {v_scene_first_line}")

    print("\n==================================================================")
    print("STEP 3: UPDATE WORLD CLOCK (world_age = 10489952)")
    print("==================================================================")
    world_url = f'{API_BASE}/worlds/{WORLD_ID}'
    # Target: 28 August 2024, 08:00 UTC -> 10489952
    world_payload = {
        'world_age': 10489952
    }
    w_req = urllib.request.Request(
        world_url,
        data=json.dumps(world_payload).encode('utf-8'),
        headers=headers,
        method='PUT'
    )
    with urllib.request.urlopen(w_req) as resp:
        w_status = resp.status
    print(f"World PUT status: {w_status}")

    # Verify World GET
    w_get_req = urllib.request.Request(world_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(w_get_req) as resp:
        w_ver = json.loads(resp.read().decode('utf-8'))

    new_world_age = w_ver.get('world_age')
    print(f"Verified World Age: {new_world_age} (Expected: 10489952)")

if __name__ == '__main__':
    deploy_scenarios()
