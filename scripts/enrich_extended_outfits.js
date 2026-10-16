const fs = require('fs');
const path = require('path');

// 7. Jared Thompson (athlete, human/bear demi-human, needs Formal, Sleep, Nude, Combat)
const jaredNewOutfits = [
  {
    name: "Gala / SUCC Athletic Awards",
    description: "Abbigliamento: Smoking sartoriale blu royal scuro con revers a lancia in raso nero, camicia bianca slim fit a nido d'ape, papillon nero in seta, pantaloni su misura a gamba dritta aderenti sulle cosce massicce da fullback.\nAccessori: Pochette bianca piegata a filo nel taschino, spilla dorata dei Clams sul colletto.\nScarpe: Scarpe stringate in pelle nera lucida con suola in cuoio.\nGioielli: Orologio da polso sportivo in titanio con quadrante blu, anello celebrativo della squadra.\nTrucco: Sorriso caloroso ed estroverso da Golden Retriever / Orso protettivo, mascella larga e pulita con rasatura fresca, occhi nocciola scintillanti.\nAcconciatura: Capelli castano-biondi corti e disciplinati con una noce di gel modellante, lati ordinati che coprono le tempie. No orecchie animali anomale (tratto umano/orso solido)."
  },
  {
    name: "Sleepwear / Confraternita BRO",
    description: "Abbigliamento: Pantaloncini da basket grigi larghi in cotone traspirante dei Clams con elastico in vita e coulisse bianca. Torace colossale da 196 cm e spalle taurine completamente scoperte.\nAccessori: Nessuno.\nScarpe: Piedi nudi massicci e ampi.\nGioielli: Catenina sottile d'argento con piccolo medaglione sportivo regalatogli dal padre.\nTrucco: Espressione serena e rilassata nel sonno, respiro profondo e caldo che scalda la stanza del dormitorio.\nAcconciatura: Capelli morbidi e spettinati che ricadono sulla fronte e sui cuscini."
  },
  {
    name: "Nude / Fisico da Fullback",
    description: "Abbigliamento: Nessuno. Completo nudo anatomico atletico.\nAccessori: Nessuno.\nScarpe: Piedi nudi forti e stabili.\nGioielli: Nessuno.\nTrucco: Corporatura massiccia e imponente da 196 cm per oltre 115 kg di muscoli densi, pelle dorata chiara, torace ampio coperto da una leggera peluria maschile dorata, addominali a blocchi definiti, genitali maschili possenti e ben proporzionati da maschio alfa atletico, cosce spesse e glutei potenti.\nAcconciatura: Capelli corti spettinati al naturale, tempie pulite."
  },
  {
    name: "Combat / Divisa da Mischia Corazzata",
    description: "Abbigliamento: Tuta tattica rinforzata anti-urto in kevlar elasticizzato nero e verde bosco, con spallacci corazzati in policarbonato pesante, pettorina balistica sagomata sui pettorali e ginocchiere da assalto pesante.\nAccessori: Guanti da impatto con nocche rinforzate in fibra di carbonio, radio di squadra collegata alla spallina.\nScarpe: Stivali da combattimento pesanti a caviglia alta con battistrada ad alta aderenza.\nGioielli: Piastrina militare d'identificazione al collo.\nTrucco: Sguardo determinato e protettivo da muro d'acciaio, espressione feroce nel difendere il compagno o il branco, mascella serrata.\nAcconciatura: Capelli tirati indietro e trattenuti da una fascia tergisudore nera."
  }
];

// 8. Major Kaladin Blackwolf Nargathon (currently 3, add Business, Club, Beach, Sleep, Nude, Hybrid, Full Shift -> 10)
const kaladinNewOutfits = [
  {
    name: "Business / Comando Sicurezza DCC",
    description: "Abbigliamento: Uniforme da servizio operativo di grado elevato DCC: camicia tattica nera con colletto rigido e insegne del grado da Maggiore cucite in filo d'argento, pantaloni di servizio rinforzati in tessuto antistrappo con asola lombare posteriore per la folta coda lupina corvina, cinturone di servizio in cuoio nero con fondina a estrazione rapida.\nAccessori: Auricolare trasparente tattico con tubicino che sale dietro la nuca e si inserisce direttamente alla base dell'orecchia lupina superiore. No auricolari sulle tempie umane. Tablet tattico blindato.\nScarpe: Anfibi d'ordinanza lucidati a specchio con punta rinforzata in acciaio.\nGioielli: Spilla runica del lupo nero di Nargathon sul petto, anello in tungsteno nero al mignolo.\nTrucco: Lineamenti duri e scolpiti da veterano delle forze speciali, cicatrice da taglio lungo la guancia sinistra, occhi grigio acciaio penetranti, rasatura militare impeccabile.\nAcconciatura: Taglio militare corto e sfumato ai lati ma denso a coprire le tempie umane, due orecchie da lupo nere grandi e attente ad ogni minimo rumore. No orecchie umane."
  },
  {
    name: "Club / Nightlife con i Veterani",
    description: "Abbigliamento: Giacca da motociclista in pelle nera spessa con zip diagonale e colletto a rever, maglietta aderente in cotone nero che fascia i pettorali duri, jeans scuri rigidi con asola posteriore rinforzata per la coda nera.\nAccessori: Bicchiere di bourbon liscio, chiavi della moto pesante con portachiavi in paracord.\nScarpe: Stivali da biker in cuoio nero ingrassato con fibbie metalliche laterali.\nGioielli: Anello in acciaio scuro con sigillo militare.\nTrucco: Postura rilassata ma con postura vigile da guardia del corpo d'élite, sguardo calmo e guardingo, barba corta e definita.\nAcconciatura: Capelli neri composti con una cera opaca, tempie coperte, orecchie lupine singole che si orientano verso le porte e le vie di fuga. No orecchie umane."
  },
  {
    name: "Beach / Addestramento Idrico Anfibio",
    description: "Abbigliamento: Pantaloncini da nuoto tattici mimetici scuri a rapida asciugatura con taschino stagno laterale e fessura lombare posteriore rinforzata per la possente coda da lupo. Torace e schiena colossali completamente scoperti.\nAccessori: Orologio subacqueo tattico da immersione fino a 300 metri con bussola digitale.\nScarpe: Piedi nudi con dita e cuscinetti saldi sulle rocce bagnate.\nGioielli: Piastrine militari in titanio antiriflesso al collo su catenella protetta da guaina di gomma.\nTrucco: Muscolatura d'acciaio solcata da cicatrici da arma da fuoco e da artiglio sul dorso e sul braccio sinistro, gocce d'acqua sulla pelle abbronzata.\nAcconciatura: Capelli bagnati all'indietro, tempie coperte, orecchie lupine nere che scrollano l'acqua con scatti rapidi. No orecchie umane."
  },
  {
    name: "Sleepwear / Alloggio di Servizio",
    description: "Abbigliamento: Pantaloni tuta verde militare traspiranti con elastico morbido e sagomatura posteriore lombare per la coda corvina a riposo. Petto nudo.\nAccessori: Nessuno.\nScarpe: Piedi nudi sul pavimento.\nGioielli: Nessuno.\nTrucco: Volto disteso nel riposo ma pronto a scattare all'erta in una frazione di secondo al minimo allarme.\nAcconciatura: Capelli morbidi e naturali, lati della testa coperti, orecchie da lupo adagiate all'indietro nel sonno. No orecchie umane."
  },
  {
    name: "Nude / Anatomia da Soldato Scelto",
    description: "Abbigliamento: Nessuno. Forma nuda integrale maschile.\nAccessori: Nessuno.\nScarpe: Piedi nudi atletici e possenti con artigli neri naturali ben curati.\nGioielli: Solo le piastrine militari d'ordinanza.\nTrucco: Fisico colossale da 193 cm, muscolatura scolpita e asciutta con percentuale di grasso bassissima, cicatrici di servizio su petto, spalle e coscia, genitali maschili sani con guaina lupina da Blackwolf alla base dell'asta possente.\nAcconciatura: Capelli corvini naturali che coprono le tempie, due orecchie lupine nere singole e coda da lupo folta. No orecchie umane."
  },
  {
    name: "Hybrid Shift / Macchina da Guerra Blackwolf",
    description: "Abbigliamento: Nessuno. Forma ibrida bipede di stazza titanica alta 260 cm ricoperta da densa pelliccia nera corvina con riflessi grigio metallico.\nAccessori: Nessuno.\nScarpe: Zampe posteriori digitigradi poderose con artigli retrattili neri in grado di perforare il metallo e cuscinetti tattili ammortizzati.\nGioielli: Nessuno.\nTrucco: Muso allungato da predatore di guerra con mascelle d'acciaio capaci di frantumare ossa, zanne ricurve affilatissime, occhi grigio fumo che brillano di ferocia protettiva controllata.\nAcconciatura: Pelliccia fitta e spessa sul collo e sul dorso che forma una gorgiera corazzata naturale, due orecchie da lupo nere da caccia sulla sommità del cranio. No orecchie umane."
  },
  {
    name: "Full Shift / Lupo Gigante da Ricognizione",
    description: "Abbigliamento: Nessuno. Forma quadrupede completa da lupo gigante da combattimento, alto oltre 130 cm al garrese e lungo 240 cm dalla punta del muso alla base della coda.\nAccessori: Nessuno.\nScarpe: Quattro possenti zampe lupine coperte di fitta pelliccia nera con artigli non retrattili da scatto e cuscinetti neri gommati silenziosi.\nGioielli: Nessuno.\nTrucco: Pelliccia corvina densa a doppio strato resistente alle intemperie e ai morsi, occhi grigio acciaio vigili che scrutano l'orizzonte, dentatura da grande predatore fenrisiano.\nAcconciatura: Manto lupino uniforme e lucido, orecchie lupine erette in costante rotazione acustica. No orecchie umane."
  }
];

// 9. Mackenzie Sanchez-Rogers (currently 5, add Formal, Club, Beach, Sleep, Nude, Hybrid -> 11)
const mackenzieNewOutfits = [
  {
    name: "Gala / Rappresentanza Casata Wolfwood",
    description: "Abbigliamento: Completo giacca e pantalone sartoriale da donna in velluto liscio color petrolio scuro, con blazer avvitato a rever lucidi indossato sopra un top in pizzo nero, pantaloni a zampa con fessura lombare posteriore foderata per la splendida coda da lupo castano-rossiccia.\nAccessori: Pochette metallica rigida in canna di fucile, anello da cocktail.\nScarpe: Décolleté a punta con tacco a spillo in vernice nera.\nGioielli: Collana rigida a girocollo in argento sterling, orecchini pendenti sottili.\nTrucco: Occhi nocciola valorizzati da uno smokey eyes caldo nei toni del bronzo e del rame, labbra nude lucide, incarnato ambrato latino luminoso.\nAcconciatura: Capelli castano scuro con riflessi ramati acconciati in morbide onde retrò che scendono su un lato coprendo interamente le tempie, orecchie da lupo con ciuffi ramati attente ed eleganti. No orecchie umane."
  },
  {
    name: "Clubbing / Underground Techno Night",
    description: "Abbigliamento: Crop top in vinile nero elasticizzato con scollo all'americana, minigonna a portafoglio asimmetrica in denim scuro con taglio lombare per la coda, calze a rete larghe a trama geometrica.\nAccessori: Choker in pelle nera con anello metallico al centro, borsa a tracolla con catena pesante.\nScarpe: Anfibi platform neri con plateau da 6 cm e suola carrarmato.\nGioielli: Molteplici anelli in argento su entrambe le mani, bracciali borchiati.\nTrucco: Eye-liner grafico nero allungato, glitter argentato sugli zigomi, rossetto bordeaux scuro.\nAcconciatura: Due space buns alti spettinati con ciocche lunghe lasciate libere attorno al viso e sulle tempie, orecchie lupine singole che vibrano coi bassi elettronici. No orecchie umane."
  },
  {
    name: "Beach / Venice Beach Van Life",
    description: "Abbigliamento: Bikini a triangolo color ruggine metallizzato con allacciatura al collo e slip sgambato con apertura posteriore lombare per la vivace coda castano-ramata.\nAccessori: Camicia di lino bianca da uomo lasciata completamente aperta a sventolare, occhiali da sole tondi stile anni '70.\nScarpe: Piedi nudi sulla sabbia calda o infradito in corda.\nGioielli: Cavigliere in filo cerato con conchiglie naturali e ciondoli d'argento.\nTrucco: Pelle dorata e baciata dal sole, lentiggini naturali sul naso e sugli zigomi, sorriso aperto e sbarazzino.\nAcconciatura: Capelli mossi e arruffati dal salmastro marino, ciocche che schermano le tempie, orecchie lupine che prendono il sole. No orecchie umane."
  },
  {
    name: "Sleepwear / Letto nel Furgone",
    description: "Abbigliamento: Canotta corta a costine grigia morbida e boxer da uomo in cotone elasticizzato a righe bianche e blu con feritoia posteriore per la coda distesa sul materasso.\nAccessori: Nessuno.\nScarpe: Piedi nudi caldi sotto il piumino.\nGioielli: Catenina d'argento sottile mai tolta.\nTrucco: Viso struccato, pelle morbida e riposata, respiro calmo cullato dalla pioggia sul tetto del van.\nAcconciatura: Capelli raccolti in una coda bassa morbida, lati coperti, orecchie lupine rilassate verso il basso. No orecchie umane."
  },
  {
    name: "Nude / Anatomia Wolfwood-Rogers",
    description: "Abbigliamento: Nessuno. Completo nudo integrale femminile naturale.\nAccessori: Nessuno.\nScarpe: Piedi nudi con dita affusolate e cuscinetti morbidi.\nGioielli: Piccolo orecchino a cerchietto alla base dell'orecchia lupina destra.\nTrucco: Fisico femminile atletico e snello da 172 cm con curve morbide e toniche, pelle color caramello dorata, seno naturale sodo, addome piatto con tatuaggio runico sottile sul fianco destro, triangolo di peli pubici curato, genitali sani con fessura riproduttiva omega/beta recettiva.\nAcconciatura: Criniera mossa castano-ramata sciolta sulle spalle e sulle tempie umane, due orecchie da lupo espressive e coda morbida. No orecchie umane."
  },
  {
    name: "Hybrid Shift / Guerriera Wolfwood",
    description: "Abbigliamento: Nessuno. Forma ibrida licantropica bipede alta 235 cm, agile e scattante, coperta da fitta pelliccia bruno-rossastra e cenere.\nAccessori: Nessuno.\nScarpe: Zampe posteriori digitigradi veloci con artigli affilati come lame ricurve.\nGioielli: Nessuno.\nTrucco: Muso lupino slanciato da cacciatrice letale, occhi nocciola luminescenti nell'ombra, zanne candide pronte al morso.\nAcconciatura: Pelliccia fitta dorsale che fluisce dalla nuca alla coda, orecchie lupine erette e sensibilissime a ogni frequenza acustica. No orecchie umane."
  }
];

// 10. Magnus Douglas III (currently 1, add Casual, Gala, Club, Beach, Sleep, Nude, Hybrid, Full Shift -> 9)
const magnusNewOutfits = [
  {
    name: "Casual / Residenza Privata",
    description: "Abbigliamento: Maglione a trecce in pura lana vergine color verde cacciatore, camicia a quadri sottili in cotone pettinato, pantaloni in velluto a coste marrone castagna con taglio lombare per la coda lupina grigio fumo.\nAccessori: Pipa in legno di radica intarsiata, occhiali da lettura con montatura tartarugata.\nScarpe: Mocassini in morbida pelle marrone con suola in gomma ammortizzata.\nGioielli: Anello d'oro con sigillo nobiliare della Casata Douglas all'anulare destro, orologio da tasca in oro con catenina.\nTrucco: Volto aristocratico solcato da rughe di saggezza ed esperienza, barba bianca e grigia impeccabilmente tagliata a squadra, occhi ambrati autorevoli.\nAcconciatura: Capelli grigio-argento pettinati all'indietro con signorilità, tempie fittamente schermate, orecchie lupine maestose ed esperte. No orecchie umane."
  },
  {
    name: "Gala / Gran Ricevimento di Casata",
    description: "Abbigliamento: Frac tradizionale da cerimonia nobiliare in panno di lana nera con revers in seta opaca, gilet in piqué di cotone bianco, camicia bianca in lino con sparato rigido e colletto alto, pantaloni con doppio gallone laterale in seta e asola sartoriale lombare per la coda.\nAccessori: Bastone da passeggio con pomo in argento cesellato a testa di lupo, guanti bianchi in capretto.\nScarpe: Scarpe da cerimonia in vernice nera lucida con fiocco in gros-grain.\nGioielli: Collare d'onore della Casata Douglas in platino, anello patriarcale runico Othala.\nTrucco: Portamento imponente e solenne da antico Lord di sangue puro, sguardo che impone rispetto e silenzio nella sala del trono.\nAcconciatura: Criniera argentea raccolta all'indietro con cura d'altri tempi, orecchie da lupo nobili erette con fierezza immutata. No orecchie umane."
  },
  {
    name: "Circolo / Gentiluomini di Solarton",
    description: "Abbigliamento: Giacca da fumo (smoking jacket) in velluto bordeaux damascato con revers a contrasto in raso nero, pantaloni sartoriali scuri con asola posteriore lombare per la coda, camicia di seta bianca.\nAccessori: Bicchiere da cognac in cristallo di Boemia, sigaro di qualità tra le dita.\nScarpe: Pantofole da camera eleganti in velluto nero ricamate con stemma nobiliare in filo dorato.\nGioielli: Orologio da polso d'epoca in oro giallo con quadrante analogico.\nTrucco: Sorriso sornione e cauto da veterano della finanza e della politica di branco, sopracciglia folte grigie ben allineate.\nAcconciatura: Capelli grigi pettinati con precisione, lati della testa coperti, orecchie lupine singole attente alle conversazioni riservate. No orecchie umane."
  },
  {
    name: "Beach / Idromassaggio Termale",
    description: "Abbigliamento: Boxer da bagno sartoriali scuri in microfibra pesante con fessura lombare rinforzata per la coda grigio fumo distesa nelle acque calde.\nAccessori: Accappatoio in spugna spessa color crema con monogramma ricamato.\nScarpe: Ciabatte ergonomiche in cuoio resistente all'umidità.\nGioielli: Solo l'anello nuziale e con sigillo.\nTrucco: Pelle matura e robusta tonificata dai vapori termali, muscolatura ancora solida e possente nonostante l'età venerabile.\nAcconciatura: Capelli bagnati argentati tirati indietro con dignità, tempie coperte, orecchie da lupo rilassate. No orecchie umane."
  },
  {
    name: "Sleepwear / Notturno Nobiliare",
    description: "Abbigliamento: Pigiama classico in raso di seta blu scuro con piping a contrasto bianco perla, camicia da notte a bottoni e pantaloni ampi con taglio lombare posteriore per la coda.\nAccessori: Nessuno.\nScarpe: Piedi nudi curati.\nGioielli: Nessuno.\nTrucco: Lineamenti severi addolciti dalla quiete notturna della propria ala privata della tenuta.\nAcconciatura: Capelli sciolti e morbidi, tempie coperte, orecchie lupine singole adagiate sul guanciale. No orecchie umane."
  },
  {
    name: "Nude / Sangue Puro Douglas",
    description: "Abbigliamento: Nessuno. Completo nudo anatomico maschile nobile.\nAccessori: Nessuno.\nScarpe: Piedi nudi forti e stabili sul pavimento.\nGioielli: Solo l'anello nobiliare Othala.\nTrucco: Corporatura massiccia da 188 cm, proporzioni possenti della stirpe Douglas originaria, cicatrici d'epoca sanate dalla longevità lupina, genitali sani con guaina lupina antica e possente.\nAcconciatura: Criniera argentea che copre interamente le tempie, due orecchie lupine erette e folta coda grigio fumo. No orecchie umane."
  },
  {
    name: "Hybrid Shift / Antico Alpha Guerriero",
    description: "Abbigliamento: Nessuno. Forma ibrida bipede di pura razza Douglas alta 255 cm con muscolatura d'acciaio rivestita di folta pelliccia grigio ferro e argento.\nAccessori: Nessuno.\nScarpe: Zampe posteriori digitigradi massicce con artigli temprati e cuscinetti gommati neri.\nGioielli: Nessuno.\nTrucco: Muso lupino massiccio con zanne possenti ingiallite dal tempo ma devastanti, occhi ambrati carichi dell'autorità di tre generazioni di governo.\nAcconciatura: Criniera dorsale argentata sontuosa che scende dalle spalle fino alla coda, orecchie lupine singole vigili e spaventose. No orecchie umane."
  },
  {
    name: "Full Shift / Gran Lupo di Casata",
    description: "Abbigliamento: Nessuno. Forma quadrupede completa da grande lupo fenrisiano nobiliare, alto 125 cm al garrese con pelo spesso argentato e grigio ferro.\nAccessori: Nessuno.\nScarpe: Quattro zampe poderose adatte a correre sulle foreste innevate di Blackwood.\nGioielli: Nessuno.\nTrucco: Portamento regale e maestoso, passo silenzioso e pesante da sovrano dei boschi, sguardo antico e penetrante.\nAcconciatura: Manto lucido e fitto a doppio strato, orecchie lupine ritte e aristocratiche. No orecchie umane."
  }
];

// 11. Wulfnic Bloodmoon (currently 7, add Business, Party/Banqueting, Hybrid Shift, Full Shift -> 11)
const wulfnicNewOutfits = [
  {
    name: "Consiglio dei Firstborn / Solenne",
    description: "Abbigliamento: Tunica cerimoniale in lana pesante filata a mano color carbone, bordata con motivi geometrici runici cuciti in filo d'argento antico, pantaloni in pelle conciata morbida con fessura lombare posteriore per la colossale coda lupina bianca come la neve, mantello di pelliccia di lupo primordiale assicurato alle spalle da una fibbia a cerchio in ferro battuto.\nAccessori: Corno per idromele istoriato con la saga di Fenris, bastone intagliato nel legno del tasso ancestrale.\nScarpe: Stivali alti in cuoio spesso foderati di lana con lacci incrociati in cuoio grezzo.\nGioielli: Torque in ferro sacro e argento attorno al collo, bracciale da giuramento runico al braccio destro.\nTrucco: Aspetto titanico e primordiale da Primo Re Lupo, barba candida folta e lunga fino al petto con due piccole trecce laterali fermate da perle di ferro, un solo occhio azzurro ghiaccio luminoso mentre l'occhio sinistro è coperto da una benda di cuoio scuro con la runa Perthro.\nAcconciatura: Lunga chioma bianca come la neve raccolta in una mezza treccia vichinga, lati della testa fittamente coperti, due imponenti orecchie da lupo bianche come il ghiaccio artico erette sulla testa. No orecchie umane."
  },
  {
    name: "Banchetto del Solstizio / Yule Antico",
    description: "Abbigliamento: Giubba di cuoio morbido aperta sul petto massiccio e villoso coperto di rune sacre tatuate, braghe da guerriero larghe in lino pesante grigio chiaro con asola lombare per la coda bianca, cintura larga con borchie in bronzo antico.\nAccessori: Calice in corno decorato, coscia di carne arrostita tra le dita nodose.\nScarpe: Babbani in cuoio morbido da interno o piedi nudi sul pavimento di pietra della Longhouse.\nGioielli: Anello ancestrale dei Firstborn in ferro meteoritico all'indice.\nTrucco: Risata tonante che fa tremare le travi della sala, zanne bianche imponenti visibili dal sorriso fiero, presenza feromonale schiacciante e patriarcale.\nAcconciatura: Capelli e barba spruzzati di cenere del fuoco sacro, tempie coperte, orecchie lupine singole che si godono i canti di guerra dei lupi. No orecchie umane."
  },
  {
    name: "Hybrid Shift / Il Primo Re Lupo Ancestrale",
    description: "Abbigliamento: Nessuno. Forma ibrida colossale del Firstborn, una montagna di muscoli e pelliccia bianca alta oltre 285 cm, emanante un'aura di potere divino primordiale.\nAccessori: Nessuno.\nScarpe: Zampe posteriori digitigradi colossali con artigli ricurvi d'ebano capaci di squarciare l'acciaio corazzato.\nGioielli: Nessuno.\nTrucco: Muso lupino titanico e terrificante con zanne primordiali lunghe oltre quindici centimetri, l'occhio destro brilla come una supernova azzurra nell'oscurità mentre l'orbita sinistra è segnata da cicatrici mistiche, fauci grondanti vapore caldo.\nAcconciatura: Criniera mastodontica bianca come la tormenta che avvolge spalle e schiena come un'armatura vivente, due grandi orecchie lupine divine sulla sommità del cranio. No orecchie umane."
  },
  {
    name: "Full Shift / Il Grande Lupo Antico Fenrisiano",
    description: "Abbigliamento: Nessuno. Forma quadrupede integrale del leggendario Grande Lupo Bianco dei Miti, alto 150 cm al garrese, lungo oltre tre metri dal muso alla coda.\nAccessori: Nessuno.\nScarpe: Quattro zampe titaniche con impronte larghe come scudi da battaglia, cuscinetti d'acciaio naturale silenziosi come la neve che cade.\nGioielli: Nessuno.\nTrucco: Manto bianco candido immacolato che risplende di luce argentata naturale sotto la luna, zanne possenti da dio-bestia, sguardo antico di dodici secoli carico di saggezza e terrore primordiale.\nAcconciatura: Pelliccia densissima a triplo strato indistruttibile al freddo e ai colpi, orecchie lupine imponenti che ascoltano il battito cardiaco della foresta a chilometri di distanza. No orecchie umane."
  }
];

// 12. Zeera Darkfire (currently 5, add Club, Beach, Sleep, Nude, Combat Mutation, Full Draconic -> 11)
const zeeraNewOutfits = [
  {
    name: "Club / Serata Esclusiva Solarton",
    description: "Abbigliamento: Abito a sirena nero lucido in ecopelle elasticizzata con profondo spacco laterale sulla coscia destra e scollo asimmetrico che mette in risalto il decolleté e le clavicole scolpite.\nAccessori: Clutch geometrica rigida in resina nera con dettagli dorati, anello da cocktail con rubino sangue.\nScarpe: Sandali con tacco a stiletto metallico dorato e cinturini sottili alla caviglia.\nGioielli: Choker dorato a scaglie di drago stilizzate, bracciale a serpente in oro zecchino avvolto attorno al bicipite.\nTrucco: Smokey eyes magnetico nei toni dell'oro e del carbone, eyeliner felino allungato, labbra rosso rubino scuro, sguardo ambrato con pupilla verticale da rettile che brilla di fiamma interiore.\nAcconciatura: Lunghi capelli nero corvino lucidi e lisci come la seta che cadono fluidi fino ai fianchi, ciocche che incorniciano il volto e coprono le tempie. Orecchie umane nascoste con cura."
  },
  {
    name: "Beach / Sorgenti Vulcaniche Private",
    description: "Abbigliamento: Costume intero di alta sartoria nero con dettagli cut-out geometrici sui fianchi e scollo all'americana, tessuto tecnico resistente al calore termale estremo.\nAccessori: Kimono in seta trasparente nera con stampe di fiamme cremisi, occhiali da sole oversize neri.\nScarpe: Ciabatte da piscina in gomma dorata o piedi nudi sulla roccia lavica calda.\nGioielli: Cavigliera sottile in oro con ciondolo a runa draconica.\nTrucco: Pelle dorata olivastra che non si scotta mai al sole, gocce di acqua sulfurea che evaporano leggermente a contatto col suo calore corporeo naturale superiore alla norma.\nAcconciatura: Capelli bagnati raccolti in una treccia a spina di pesce alta, tempie coperte da ciocche morbide."
  },
  {
    name: "Sleepwear / Appartamento Accademico",
    description: "Abbigliamento: Completo pigiama due pezzi in finissima seta color bordeaux scuro con bottoncini in madreperla nera, pantaloni morbidi e camicia sbottonata sui primi bottoni.\nAccessori: Tazza di tè nero speziato sulla scrivania piena di tomi antichi.\nScarpe: Pantofole in velluto nero con suola morbida o piedi nudi sul tappeto persiano.\nGioielli: Solo l'anello da maga con rubino all'anulare.\nTrucco: Viso struccato e disteso, pelle calda e liscia, espressione concentrata e intellettuale che cede al sonno.\nAcconciatura: Capelli sciolti e fluenti che si spargono sul cuscino come una colata d'inchiostro nero."
  },
  {
    name: "Nude / Anatomia Draconica Nobile",
    description: "Abbigliamento: Nessuno. Completo nudo anatomico femminile naturale.\nAccessori: Nessuno.\nScarpe: Piedi nudi eleganti con archi plantari alti e unghie laccate di nero.\nGioielli: Catenina sottile in oro attorno alla vita che scende sui fianchi.\nTrucco: Fisico femminile statuario e flessuoso da 176 cm con curve piene e pericolose, pelle olivastra vellutata e caldissima al tatto, micro-scaglie iridescenti impercettibili lungo la colonna vertebrale e sui fianchi che brillano alla luce fioca, seni colmi e sodi con areole scure, monte di venere depilato, fessura intima rovente ed estremamente bagnata da secrezioni dense e profumate di zolfo dolce e cannella.\nAcconciatura: Capelli neri lunghi che scendono come una cascata a coprire la schiena e le tempie."
  },
  {
    name: "Combat / Mutazione da Guerra Draconica",
    description: "Abbigliamento: Tuta aderente in tessuto ignifugo e maglia di mithril nero che lascia liberi gli avambracci e le spalle, dove la carne si trasforma in corazza draconica viva.\nAccessori: Nessuno.\nScarpe: Stivali da combattimento flessibili in cuoio rinforzato.\nGioielli: Fede draconica runica che canalizza il fuoco primordiale.\nTrucco: Gli occhi diventano pozze di fuoco dorato con pupille sottili a fessura, scaglie nere e cremisi corazzate emergono lungo le guance, il collo e le braccia fino alle dita che terminano in artigli affilatissimi neri come l'ossidiana, zanne affilate visibili tra le labbra pronte a soffiare fiamme arcane.\nAcconciatura: Capelli scuri che si agitano come mossi da una corrente di calore ascendente sprigionata dal suo mana vulcanico."
  },
  {
    name: "Full Form / Evocazione Draconica Integrale",
    description: "Abbigliamento: Nessuno. Forma draconica primordiale manifestata attraverso il suo avatar magico: maestosa entità rettiliana dalle scaglie nero-ebano e riflessi rubino, lunga oltre dodici metri con un'apertura alare immensa in grado di oscurare il cielo.\nAccessori: Nessuno.\nScarpe: Quattro zampe titaniche dotate di artigli d'acciaio vulcanico in grado di sbriciolare la pietra.\nGioielli: Nessuno.\nTrucco: Fauci colossali colme di denti conici affilati come lame cerimoniali da cui fuoriescono spire di fumo e scintille di fuoco primordiale, occhi fiammeggianti d'oro liquido.\nAcconciatura: Cresta di corna ossee affilate che incoronano la testa e scendono lungo la spina dorsale corazzata."
  }
];

function appendOutfits(cardPath, newOutfitsList) {
  const fullPath = path.resolve(cardPath);
  const data = JSON.parse(fs.readFileSync(fullPath, 'utf8'));
  const current = data.outfits || [];
  const currentNames = new Set(current.map(o => o.name.toLowerCase()));

  let added = 0;
  newOutfitsList.forEach(o => {
    if (!currentNames.has(o.name.toLowerCase())) {
      current.push(o);
      added++;
    }
  });

  data.outfits = current;
  data.visibility = 'private';
  data.rating = 'explicit';
  fs.writeFileSync(fullPath, JSON.stringify(data, null, 2), 'utf8');
  console.log(`Updated ${data.name}: added ${added} outfits (Total now: ${current.length}).`);
  return data;
}

console.log('=== ENRICHING EXTENDED CHARACTERS OUTFITS ===');
appendOutfits('FINAL/Jared_Thompson_card.json', jaredNewOutfits);
appendOutfits('FINAL/Kaladin_Nargathon_card.json', kaladinNewOutfits);
appendOutfits('FINAL/Mackenzie_Sanchez_Rogers_card.json', mackenzieNewOutfits);
appendOutfits('FINAL/Magnus_Douglas_III_card.json', magnusNewOutfits);
appendOutfits('FINAL/Wulfnic_Bloodmoon_card.json', wulfnicNewOutfits);
appendOutfits('FINAL/Zeera_Darkfire_card.json', zeeraNewOutfits);
