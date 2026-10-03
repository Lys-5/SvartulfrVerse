import json
import urllib.request
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
PERSONA_ID = 'persona_1786335754946'
CARD_ID = '_MXcEC8Y6B3BNm3b1ttHj6'

FULL_OUTFIT_DESCRIPTIONS = {
    "naked": """Abbigliamento: Completamente nuda, priva di indumenti. Corporatura minuta a clessidra con pelle chiara e liscia, seno pesante e voluminoso DD-cup con piccoli capezzoli rosa, addome piatto, fianchi larghi con marcatura lunare a mezzaluna sul fianco sinistro. Folta coda da lupo caramello con punta nera ed orecchie lupine erette.
Accessori: Nessuno.
Scarpe: Piedi nudi con unghie curate al naturale.
Gioielli: Anello all'ombelico in argento con ciondolo a luna crescente pendente; sottili cerchietti d'argento fissati lungo la cartilagine delle orecchie da lupo; anello con sigillo Douglas d'argento all'anulare sinistro; tatuaggio runico Gebo ben visibile sul polso sinistro.
Trucco: Viso completamente pulito al naturale, acqua e sapone; labbra idratate con balsamo trasparente.
Acconciatura: Lunghi capelli castano caramello lasciati totalmente sciolti in morbide onde setose che scendono lungo la schiena fino al coccige, incorniciando il viso e lasciando scoperte le orecchie lupine sulla sommità del capo.""",

    "tactic": """Abbigliamento: Tuta tattica bianca in tessuto tecnico incantato antistrappo, leggero e flessibile. Top bianco a collo alto senza maniche con schiena, spalle e braccia scoperte, chiuso sul petto abbondante DD-cup con cerniere rinforzate e fibbie metalliche piatte. Pantaloni cargo bianchi sagomati con tasche piatte laterali e fessura posteriore rinforzata per la coda caramello con punta nera.
Accessori: Cintura tattica medica modulare in polimero rinforzato bianco attorno alla vita, equipaggiata con scomparti per fiale di pozioni rigenerative, bende emostatiche e bisturi chirurgico in acciaio; guantini tecnici bianchi senza dita con grip sul palmo.
Scarpe: Stivali da esplorazione bianchi a metà polpaccio in cuoio trattato con suola sagomata antiscivolo e allacciatura rapida con ganci rinforzati.
Gioielli: Piccoli cerchietti piatti in argento titanio aderenti alle orecchie da lupo; cordino nero al collo con piccolo ciondolo runico protettivo d'argento; anello all'ombelico visibile nello spazio inferiore del top; anello con sigillo Douglas e tatuaggio Gebo al polso sinistro.
Trucco: Minimalista e pratico; fondotinta opacizzante leggero resistente al sudore, balsamo labbra trasparente e tocco leggero di mascara waterproof nero sulle ciglia.
Acconciatura: Capelli castano caramello tirati saldamente all'indietro in una coda di cavallo alta e compatta assicurata da un elastico tecnico rinforzato; orecchie lupine completamente libere, erette e scoperte.""",

    "summer": """Abbigliamento: Top a portafoglio color giallo girasole in cotone leggero con maniche ad aletta e balze lungo i bordi, allacciato sul davanti con un fiocco appena sotto il seno pesante DD-cup, lasciando scoperta la fascia addominale. Shorts corti in denim chiaro sfrangiato a vita media, sagomati sui fianchi larghi con apertura ad asola rinforzata sul retro per la folta coda da lupo.
Accessori: Borsa a tracolla estiva in paglia intrecciata naturale con tracolla sottile in cuoio miele; occhiali da sole tondi con lenti sfumate ambrate e montatura metallica sottile portati infilati nello scollo del top.
Scarpe: Scarpe da ginnastica basse in tela di cotone bianco ottico con suola in gomma e stringhe coordinate, indossate senza calzini visibili.
Gioielli: Anello all'ombelico in argento sterling con pendente a luna crescente; serie di tre cerchietti sottili d'argento su ciascuna orecchia da lupo; braccialetto rigido d'argento al polso destro e collana sottile a catenina con piccolo ciondolo a sole; anello Douglas e tatuaggio Gebo visibile al polso sinistro.
Trucco: Luminoso ed estivo; crema idratante colorata con finitura glow, tocco generoso di blush pesca fresco sulle guance e sul ponte del naso, mascara marrone delicato e lucidalabbra lucido al gusto ciliegia.
Acconciatura: Capelli castano caramello lasciati completamente sciolti in lunghe onde morbide e voluminose scalate fino al coccige, con due piccole treccine bohémien laterali che arretrano dietro le orecchie lupine lasciandole in primo piano.""",

    "winter": """Abbigliamento: Maglione oversize a coste grosse in pura lana color panna avorio, lavorato a trecce, con scollo a barca asimmetrico che scivola lasciando scoperta una spalla nuda, indossato senza reggiseno sotto il filato morbido e pesante. Leggings termici neri coprenti ad alta elasticità con apertura posteriore rifinita per consentire il movimento della folta coda da lupo.
Accessori: Scaldamuscoli in lana a maglia grossa color sabbia calzati sopra i leggings; manicotti senza dita in lana crema coordinata; borsa a sacca in morbida pelle marrone cioccolato con chiusura a coulisse.
Scarpe: Stivaletti invernali imbottiti scamosciati color caramello con suola in gomma antiscivolo e risvolto in pelliccia sintetica bianca.
Gioielli: Cerchietti d'argento lucido incastonati sulla cartilagine delle orecchie da lupo; catenina sottile in argento con ciondolo a cristallo di quarzo ialino pendente sul petto; anello con sigillo Douglas sulla mano sinistra e tatuaggio Gebo al polso.
Trucco: Incarnato vellutato e idratato; leggero tocco di blush rosato freddo sulle guance per un effetto fresco; mascara nero delicato e balsamo labbra idratante tonalità rosa antico opaco.
Acconciatura: Lunghi capelli caramello raccolti a mezza coda posteriore con un fermaglio a molletta in legno intagliato, lasciando scendere le lunghezze sulle spalle e liberando il collo e le orecchie da lupo che emergono dal morbido colletto.""",

    "beach": """Abbigliamento: Bikini due pezzi bianco ottico in microfibra liscia ad asciugatura rapida. Top a triangolo scorrevole con coppe bordate e laccetti sottili allacciati dietro la nuca e alla schiena che fasciano il seno voluminoso DD-cup. Slip brasiliana a vita bassa con laccetti regolabili annodati sui fianchi, posizionato con taglio anatomico esattamente sotto la radice della folta coda da lupo caramello con punta nera.
Accessori: Pareo corto semitrasparente in mussola bianca legato asimmetricamente a lato vita; grande borsa da spiaggia in tela beige con manici in corda intrecciata; occhiali da sole oversize quadrati con montatura tartarugata.
Scarpe: Piedi nudi con sottile cavigliera a filo cerato e conchiglie kauri attorno alla caviglia destra; unghie curate al naturale.
Gioielli: Anello all'ombelico in argento con luna crescente pendente che riflette la luce; cerchietti d'argento sottili lungo i bordi delle orecchie da lupo; collana girocollo con piccole perline bianche e turchesi; anello con sigillo Douglas al dito e tatuaggio Gebo ben visibile al polso.
Trucco: Totalmente waterproof e fresco; crema solare protettiva effetto invisibile, mascara resistente all'acqua sulle ciglia superiori e olio labbra nutriente trasparente effetto bagnato.
Acconciatura: Capelli castano caramello sciolti e bagnati a onde naturali, tirati leggermente indietro dietro le orecchie lupine per lasciarle erette e scoperte.""",

    "sleep": """Abbigliamento: T-shirt nera oversize in cotone pettinato consumato e morbido, con scollo tondo svasato che cade oltre una spalla e orlo che arriva a metà coscia; slip a vita bassa in morbidissimo cotone a costine bianco con elastico sottile sagomato sotto la base della coda.
Accessori: Nessuna borsa; tazza da notte in ceramica tenuta tra le mani.
Scarpe: Piedi nudi con pelle curata e idratata.
Gioielli: Anello con sigillo Douglas in argento sterling portato all'anulare della mano sinistra; anello all'ombelico con luna pendente d'argento; piccoli cerchietti d'argento piatti alle orecchie da lupo; tatuaggio Gebo evidente sul polso sinistro.
Trucco: Completamente struccata e detersa; crema viso notte idratante e un leggero velo di burrocacao nutriente al burro di karité sulle labbra.
Acconciatura: Capelli castano caramello raccolti sommariamente in uno chignon alto disordinato (messy bun) fermato da uno scrunchie morbido in seta color champagne, con ciocche libere che ricadono sul collo e contornano le orecchie lupine rilassate.""",

    "fest": """Abbigliamento: Abito cerimoniale lungo stile impero in pura seta fluida color bianco lunare con ricami serici in filo d'argento metallizzato lungo la scollatura e il busto sagomato. Gonna a più strati di georgette trasparente con profondo spacco laterale sulla coscia e spacco posteriore cerimoniale bordato d'argento disegnato per far ricadere liberamente la folta coda da lupo caramello e nera.
Accessori: Stola cerimoniale in chiffon semitrasparente bianco latte bordata di piccole frange argentate drappeggiata sui gomiti; piccolo borsellino rigido a sacchetto in velluto bianco con cordoncino d'argento.
Scarpe: Sandali bassi in pelle laminata argento con cinturini sottili a spirale che risalgono attorno al polpaccio, allacciati con piccole fibbie d'argento.
Gioielli: Diadema a catenella d'argento sulla fronte con una pietra di luna a goccia centrale pendente tra le sopracciglia; catenelle d'argento sagomate attorno alla base delle orecchie da lupo; collana collier rigida d'argento al collo; anello con sigillo Douglas e bracciale cerimoniale con rune lunari al polso sinistro sopra il tatuaggio Gebo.
Trucco: Sofisticato e luminoso; incarnato con polvere illuminante d'argento sugli zigomi e sull'arco di cupido, linea sottile di eyeliner alato nero sfumato, ombretto shimmer bianco argento e labbra color petalo di rosa con gloss perlato.
Acconciatura: Lunghi capelli castano caramello parzialmente acconciati a corona con trecce elfiche intrecciate con boccioli freschi di fiori di luna bianchi, mentre le lunghezze posteriori ricadono a onde sinuose fino alle anche; orecchie lupine ritte e incorniciate dai gioielli serici.""",

    "academy": """Abbigliamento: Uniforme ufficiale della Divisione Medica dell'Accademia: giacca doppiopetto in tessuto sagomato bianco puro con revers a lancia, profili decorativi verde smeraldo sui polsini e bottoni araldici d'argento con stemma inciso. Camicia bianca con colletto rigido e cravattino sottile in seta verde bosco. Minigonna a pieghe fitte in lana grigio antracite con fessura su misura rinforzata sul retro per la coda caramello con punta nera.
Accessori: Fascia da braccio elastica verde smeraldo della Divisione Medica dell'Accademia appuntata alla manica sinistra con spilla d'argento a croce runica; borsa a cartella medica a tracolla in cuoio marrone scuro con fibbie d'ottone; stetoscopio medico con tubi in caucciù verde menta attorno al collo.
Scarpe: Stivali alti al ginocchio in cuoio nero opaco con allacciatura frontale a stringhe e cerniera interna, dotati di solida suola ortopedica da campo in gomma naturale.
Gioielli: Piccoli orecchini a lobo geometrici in argento sulle orecchie lupine; anello con sigillo Douglas alla mano sinistra; orologio analogico con quadrante a secondi al polso; tatuaggio Gebo visibile alla giuntura del polso sinistro.
Trucco: Sobrio, professionale e pulito; correttore leggero, mascara nero allungante, un velo di cipria trasparente opacizzante e un rossetto idratante color nude opaco.
Acconciatura: Capelli castano caramello pettinati lisci e ordinati, con le sezioni laterali fissate all'indietro da due forcine piatte in metallo argentato dietro le orecchie lupine, mentre la lunghezza posteriore scende compatta lungo la schiena.""",

    "sport": """Abbigliamento: Completo tecnico da allenamento bicolore giallo girasole e blu navy. Top sportivo a reggiseno da corsa a compressione giallo con fascia elastica sottoseno rinforzata e spalline larghe a vogatore incrociate sulla schiena. Giacca a vento tecnica antivento e antipioggia blu scuro con zip centrale e profili catarifrangenti gialli, indossata aperta. Pantaloncini ciclisti corti a vita alta in lycra blu navy contenitiva, provvisti di fessura ergonomica a occhiello per l'uscita della coda al coccige.
Accessori: Polsini parasudore in spugna elasticizzata blu navy su entrambi i polsi; borraccia sportiva termica in alluminio con beccuccio rapido e laccetto da polso; auricolari sportivi wireless ergonomici ad archetto.
Scarpe: Scarpe da corsa ad alte prestazioni con intersuola ammortizzata color bianco e giallo neon, suola in gomma tassellata e calzini corti traspiranti invisibili.
Gioielli: Anello all'ombelico d'argento semplice e piatto; orecchini a cerchietto sportivo in titanio alle orecchie da lupo; anello Douglas assicurato a una cordicella nascosta sotto il top sportivo; tatuaggio Gebo al polso coperto a metà dal polsino di spugna.
Trucco: Nessun trucco pesante; crema solare ad assorbimento immediato effetto asciutto e balsamo labbra nutriente protettivo opaco.
Acconciatura: Capelli castano caramello tirati indietro in una coda di cavallo alta ed elastica legata con uno scrunchie sportivo antiscivolo, con la ciocca della coda intrecciata; orecchie lupine orientate all'indietro per l'aerodinamica.""",

    "spring": """Abbigliamento: Abito midi aderente in morbida maglina di cotone a coste sottili color blu oceano pastello, con scollatura a cuore pronunciata e spalline larghe. Maniche corte sagomate, taglio aderente lungo i fianchi a clessidra e spacco laterale fino a metà coscia sinistra, con cucitura posteriore modificata e aperta sul fondo schiena per la folta coda caramello con punta nera.
Accessori: Borsetta a tracolla piccola in ecopelle color sabbia con catenella dorata e chiusura a scatto; cardigan corto traforato in filo di cotone bianco avorio tenuto ripiegato su un braccio.
Scarpe: Sandali bassi alla schiava in cuoio miele naturale con sottili listini intrecciati che si allacciano con un fiocchetto alla caviglia.
Gioielli: Collana sottile a catenina d'oro bianco con un ciondolo floreale a margherita; due piccoli cerchietti d'argento e un brillantino punto luce su ciascuna orecchia da lupo; anello Douglas d'argento all'anulare; anello all'ombelico con ciondolo a luna visibile dal tessuto; tatuaggio Gebo sul polso.
Trucco: Fresco e primaverile; base leggera con BB cream idratante, guance ravvivate da un blush color pesca dorata, ombretto sfumato color champagne perlato, mascara incurvante marrone e lucidalabbra idratante tonalità pesca albicocca.
Acconciatura: Capelli castano caramello lasciati sciolti in morbide onde naturali e soffici che ricadono sul petto e lungo la schiena, impreziositi da una piccola molletta a forma di fiore di ciliegio su un lato che tiene libera l'orecchia da lupo corrispondente.""",

    "hybrid": """Abbigliamento: Nessun capo di vestiario né indumento indosso. Anatomia da lupo mannaro bipede di 185 cm, con corporatura muscolosa ma snella e slanciata. Folto mantello serico color caramello dorato che copre l'intero corpo, sfumando sul petto e sul ventre in una luminosa marcatura a pelo bianco lunare a forma di cuore perfetto. Gambe a struttura digitigrade con cuscinetti plantari scuri e artigli ricurvi neri venati d'oro sia alle zampe superiori che inferiori. Grande e maestosa coda caramello con punta nera pronunciata.
Accessori: Nessuno.
Scarpe: Nessuna calzatura; potenti zampe digitigradi con polpastrelli ammortizzanti neri e artigli retrattili d'ebano dorato.
Gioielli: Il pesante anello con sigillo d'argento della famiglia Douglas resta incastonato al dito anulare sinistro della zampa; marcatura runica Gebo impressa misticamente tra i fasci di pelo del polso sinistro; occhi grandi verde menta che conservano espressività umana.
Trucco: Aspetto naturale biologico lupino; muso corto da lupo con tartufo nero lucido, labbra scure e folte vibrisse chiare.
Acconciatura: Gorgiera di pelliccia più lunga e vaporosa attorno al collo e alle spalle che sfuma nella chioma di pelo caramello sulla nuca; orecchie lupine grandi, mobili ed erette sulla cima della testa.""",

    "fullshift": """Abbigliamento: Nessun vestito; forma quadrupede lupina completa di dimensioni superiori alla norma (Hvit, la Luna Bianca). Doppio mantello fitto, soffice e lucido di colore caramello dorato caldo lungo il dorso, il collo e la parte superiore dei fianchi, che degrada in bianco lunare immacolato e luminescente sul muso, sulla fronte, sul petto (marcatura a cuore), sul ventre e su tutte e quattro le zampe. Sulla groppa posteriore sinistra spicca una distinta marcatura di pelo bianco a forma di luna crescente. Coda da lupo foltissima e vaporosa con punta d'ebano nero netto.
Accessori: Nessuno.
Scarpe: Nessuna calzatura; quattro zampe da lupo con cuscinetti plantari soffici e resistenti, unghie nere affilate.
Gioielli: Pesante anello con sigillo d'argento della casata Douglas assicurato a un sottile cordino di cuoio scuro intrecciato, annodato alla base del collo e parzialmente sepolto nella foltissima gorgiera di pelo bianco del petto.
Trucco: Aspetto interamente lupino; occhi grandi a mandorla color verde menta limpido, tartufo umido e nero carbone, dentatura affilata con canini pronunciati ma priva di ferinità minacciosa.
Acconciatura: Folta gorgiera leonina di pelo morbido che avvolge l'intera cassa toracica e il collo; orecchie lupine grandi, spesse e foderate di morbido pelo bianco all'interno, sempre all'erta e mobili in cima al cranio.""",

    "formal": """Abbigliamento: Tailleur formale sartoriale d'alta classe color avorio in crêpe di lana leggera. Giacca monopetto sagomata con scollo a V profondo e rever a lancia profilati in seta tono su tono, abbottonata con un singolo bottone rivestito sotto il seno generoso DD-cup. Sotto la giacca, camicetta in georgette di pura seta color verde menta chiaro con abbottonatura nascosta. Minigonna a tubino coordinata avorio a vita alta con taglio sartoriale e spacco posteriore centrale su misura per la coda di lupo caramello con punta nera.
Accessori: Pochette da sera rigida a busta in pelle lucida color avorio con bordo metallico argentato e catenella opzionale; guanti corti da guida in pelle traforata color burro.
Scarpe: Décolleté a punta in pelle verniciata color avorio con tacco a stiletto da 10 cm e plateau interno invisibile che slancia la figura minuta.
Gioielli: Set coordinato di perle d'acqua dolce e argento rodiato: collana girocollo di piccole perle con pendente centrale a goccia d'argento, orecchini a cerchio in argento con perle pendenti sulle orecchie da lupo; anello con sigillo Douglas e bracciale rigido d'argento sul polso sinistro sopra il tatuaggio Gebo; anello all'ombelico non visibile sotto gli indumenti.
Trucco: Elegante ed impeccabile; fondotinta a lunga tenuta dall'effetto satinato naturale, contouring delicato sugli zigomi, ombretto sfumato nei toni della terra e champagne con sottile riga di eyeliner nero grafismo fine, mascara nero volumizzante e rossetto satinato color rosa antico/malva.
Acconciatura: Capelli castano caramello disciplinati in onde larghe e brillanti in stile vintage Hollywood, con riga laterale profonda e ciocche pettinate con precisione; orecchie lupine accuratamente pettinate che emergono fiere dalla chioma formale.""",

    "clinic": """Abbigliamento: Camice medico professionale da laboratorio in cotone bianco candido pesante e antimacchia, lunghezza a tre quarti fino a metà coscia, tagliato con maniche lunghe risvoltate agli avambracci e portato aperto. Al di sotto indossa una blusa senza maniche in jersey elasticizzato bianco con elegante scollo a barca che fascia il seno DD-cup. Leggings neri opachi e coprenti a tre quarti (appena sotto il ginocchio), dotati di una fessura elastica posteriore sagomata per il passaggio confortevole della folta coda da lupo caramello e nera.
Accessori: Stetoscopio medico professionale nero con testina in metallo satinato poggiato attorno al collo; cartellino identificativo badge magnetico con foto clinica spillato sul colletto del camice; penna a sfera medica con luce a pupillometro e forbici smusse infilate nel taschino superiore del camice; orologio digitale in silicone nero al polso destro per il calcolo dei parametri vitali.
Scarpe: Scarpe da ginnastica basse in tela nera stile Converse All Star con punta e suola in gomma bianca vulcanizzata, stringhe bianche e soletta interna anatomica per la postura.
Gioielli: Orecchini a cerchietto piccoli in titanio sterile anallergico su entrambe le orecchie da lupo; anello con sigillo Douglas al dito anulare sinistro; tatuaggio runico Gebo esposto sul polso sinistro sotto le maniche risvoltate del camice; anello all'ombelico coperto dalla blusa.
Trucco: Pulito, sobrio e naturale; correttore mirato per illuminare lo sguardo, una spolverata di cipria traslucida anti-lucido sulla zona T, un tocco di blush rosato salutare sulle gote, mascara leggero e balsamo idratante protettivo trasparente sulle labbra.
Acconciatura: Capelli castano caramello raccolti meticolosamente in una coda di cavallo alta e salda con un elastico in gomma antimicrobico, senza ciuffi ribelli sul viso; orecchie da lupo ritte, pulite e completamente scoperte per il monitoraggio uditivo.""",

    "biker": """Abbigliamento: Giacca corta modello biker in vera pelle nera pesante con finitura semilucida, chiusura a cerniera asimmetrica argentata e ampi rever con borchie a pressione cromate, portata aperta. Top a tubino color giallo girasole in tessuto fasciante senza spalline che avvolge il seno prosperoso DD-cup, lasciando nuda la gola, le spalle e la parte superiore della cassa toracica. Pantaloni aderenti in pelle nera con inserti a costine trapuntate sulle ginocchia, vita media e apertura posteriore rinforzata con rivetti metallici per la folta coda caramello con punta nera.
Accessori: Guanti da moto in pelle nera senza dita con nocche imbottite e chiusura in velcro; casco da moto nero opaco custom con fessure aerodinamiche protette per le orecchie lupine (tenuto sottobraccio); borsa da gamba tattica in cordura nera con cinghie regolabili alla coscia destra per riporre patente e chiavi.
Scarpe: Stivali da motociclista alti fino a metà stinco in cuoio nero ingrassato, con punta arrotondata rinforzata, spesse fibbie laterali in metallo argentato brunito e suola a carrarmato ad alta aderenza.
Gioielli: Girocollo a collarino in pelle nera con piccola placchetta centrale in acciaio inciso; cerchietti d'argento e un piccolo piercing a barra d'acciaio sulla cartilagine delle orecchie da lupo; anello Douglas d'argento; tatuaggio Gebo al polso sinistro ben visibile oltre il bordo del guanto.
Trucco: Deciso e grintoso; base viso matte a lunga tenuta, smokey eyes sfumato nei toni del marrone caldo e carbone attorno agli occhi verde menta con kajal nero nella rima interna, mascara nero intenso e rossetto cremoso color nude nocciola a prova di vento.
Acconciatura: Lunghi capelli castano caramello pettinati all'indietro e intrecciati in una singola, spessa e resistente treccia a spina di pesce che ricade al centro della schiena senza svolazzare; orecchie lupine scoperte, erette e attente.""",

    "dinner": """Abbigliamento: Abito da sera lungo a sirena in prezioso raso di seta blu oltremare notte con riflessi luminosi. Corpetto strutturato con scollatura generosa ad anello drappeggiata sul busto DD-cup, sostenuto da spalline gioiello sottilissime. Linea fasciante che abbraccia i fianchi larghi prima di aprirsi dolcemente a campana verso l'orlo, arricchita da un ingegnoso drappeggio posteriore sagomato dal sarto per consentire alla folta coda di lupo caramello e nera di fuoriuscire elegantemente senza pieghe anomale sul raso.
Accessori: Scialle stola rettangolare in garza di seta trasparente blu notte profilata di minuscole paillettes argento, portata drappeggiata sulle braccia; clutch da sera rigida gioiello in metallo argentato martellato con chiusura a cristallo sfaccettato.
Scarpe: Sandali gioiello da sera in raso blu scuro con cinturino a listini incrociati sul collo del piede, tacco a spillo cromato da 11 cm e suola laccata.
Gioielli: Parure in oro bianco e zaffiri blu: collier con pendente a goccia di zaffiro taglio brillante posato sul décolleté; orecchini pendenti con zaffiri e diamanti che scintillano pendendo dalla punta delle orecchie lupine; bracciale tennis di brillanti al polso sinistro posizionato appena sopra il tatuaggio Gebo; anello Douglas al dito.
Trucco: Raffinato da gran sera; incarnato radioso scolpito ad arte, ombretto blu notte sfumato con pagliuzze dorate che intensifica il verde degli occhi, ciglia volumizzate a ventaglio con mascara extra-black e rossetto liquido a lunga durata color mora satinato.
Acconciatura: Capelli castano caramello pettinati e raccolti in un morbido chignon basso alla francese dietro la nuca, con ciocche ondulate e setose lasciate scendere ad arte a incorniciare il collo e le clavicole; orecchie lupine erette dal raccolto, pulite e valorizzate dai pendenti gioiello.""",

    "angelo moreno couture": """Abbigliamento: Abito haute couture esclusivo modello "Ocean Shadow" firmato dallo stilista Angelo Moreno. Realizzato in innovativo tessuto fluido iridescente e cangiante che muta cromaticamente dal blu abisso al verde smeraldo e ametista liquido a seconda dell'angolatura della luce. Corpetto a corsetto sagomato con stecche flessibili interne su misura per il busto generoso DD-cup, scollo a cuore geometrico con micro-spalline invisibili in tulle illusion. Gonna fluida asimmetrica a panneggi scivolati con uno spacco strategico rinforzato sul retro da cui scivola la folta coda da lupo caramello e nera.
Accessori: Minaudière gioiello da passerella a forma di prisma sfaccettato in metacrilato blu petrolio e titanio; stola eterea in velo di seta metallizzata ametista lunga fino al pavimento, fissata agli avambracci con due manicotti invisibili.
Scarpe: Sandali gladiatore haute couture in vernice laccata blu notte metallizzato, con tacco scultura geometrico in metallo cromato e sottili stringhe in raso di seta che risalgono incrociandosi con precisione millimetrica lungo la caviglia e il polpaccio.
Gioielli: Fermagli e barrette geometriche in cristallo di rocca sfaccettato e ametista grezza incastonati tra i capelli sciolti che riflettono prismaticamente la luce; ear-cuff scultorei in titanio brunito modellati esattamente lungo i bordi cartilaginei delle orecchie da lupo; anello Douglas in argento e bracciale a scultura continua che incornicia il tatuaggio Gebo al polso sinistro.
Trucco: Alta moda sofisticato e artistico; base ultra-glow effetto pelle di vetro (glass skin), sfumatura occhi duo-chrome verde/blu petrolio con micro-glitter luminescenti lungo l'arcata e la rima inferiore, eyeliner grafico sottilissimo, ciglia lunghe e definite, labbra rimpolpate con gloss trasparente a specchio con riflessi freddi.
Acconciatura: Lunghi capelli castano caramello trattati a specchio e pettinati in ampie onde fluide liquide che ricadono fino alle anche; sezioni laterali impreziosite dai cristalli che mantengono aperte e protagoniste le orecchie lupine erette."""
}

def main():
    token = get_auth_token()
    print("Token ottenuto.\n")

    # 1. Fetch live Persona
    req_p = urllib.request.Request(f'https://app.wyvern.chat/api/user-personas/{PERSONA_ID}', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    persona = json.loads(urllib.request.urlopen(req_p).read().decode('utf-8'))

    # 2. Fetch live Card
    card = get_char(token, CARD_ID)

    # 3. Update outfits in Card
    updated_card_outfits = []
    for o in card['outfits']:
        k = o['name'].lower()
        new_desc = FULL_OUTFIT_DESCRIPTIONS.get(k)
        if new_desc:
            o_copy = dict(o)
            o_copy['description'] = new_desc.strip()
            updated_card_outfits.append(o_copy)
        else:
            print(f"[WARN CARD] Nessuna descrizione per '{o['name']}'")
            updated_card_outfits.append(o)

    # 4. Update outfits in Persona
    updated_persona_outfits = []
    for o in persona['outfits']:
        k = o['name'].lower()
        new_desc = FULL_OUTFIT_DESCRIPTIONS.get(k)
        if new_desc:
            o_copy = dict(o)
            o_copy['description'] = new_desc.strip()
            updated_persona_outfits.append(o_copy)
        else:
            print(f"[WARN PERSONA] Nessuna descrizione per '{o['name']}'")
            updated_persona_outfits.append(o)

    # 5. PUT Card
    print("=== Aggiornamento Card World ===")
    put_char(token, CARD_ID, {'outfits': updated_card_outfits})
    card_ver = get_char(token, CARD_ID)
    print(f"Card verificata! {len(card_ver['outfits'])} outfits.")

    # 6. PUT Persona
    print("\n=== Aggiornamento Persona Utente ===")
    persona_payload = dict(persona)
    persona_payload['outfits'] = updated_persona_outfits
    put_url = f'https://app.wyvern.chat/api/user-personas/{PERSONA_ID}'
    req_put = urllib.request.Request(
        put_url,
        data=json.dumps(persona_payload).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='PUT'
    )
    with urllib.request.urlopen(req_put) as resp:
        res = json.loads(resp.read().decode('utf-8'))
    
    # Verify Persona
    req_ver = urllib.request.Request(put_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    persona_ver = json.loads(urllib.request.urlopen(req_ver).read().decode('utf-8'))
    print(f"Persona verificata! {len(persona_ver['outfits'])} outfits.")

    print("\nTutti i 17 outfit sono ora arricchiti con abbigliamento, accessori, scarpe, gioielli, trucco e acconciatura su entrambe le schede!")

if __name__ == '__main__':
    main()
