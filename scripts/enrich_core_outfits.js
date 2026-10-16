const fs = require('fs');
const path = require('path');

const token = fs.readFileSync('scratch/wyvern_token.txt', 'utf8').trim();

// 1. Erik Douglas (currently 6 outfits, add Gala/Formal, Party/Club, Beach/Terme, Sleep -> 10)
const erikNewOutfits = [
  {
    name: "Gala di Casata / Formal Douglas",
    description: "Abbigliamento: Smoking su misura in lana pettinata nera a due bottoni con revers in raso di seta, camicia bianca su misura in cotone egiziano con colletto diplomatico e polsini francesi, pantaloni sartoriali neri a taglio dritto con apertura lombare rinforzata per la coda lupina folta grigio scuro.\nAccessori: Gemelli in argento con incisione della runa Tiwaz, pochette da taschino bianca in seta pura.\nScarpe: Scarpe stringate modello Oxford in pelle lucida nera spazzolata a mano.\nGioielli: Anello con sigillo della Casata Douglas in platino all'anulare sinistro, orologio da polso d'epoca in acciaio inossidabile.\nTrucco: Lineamenti severi e maturi, barba scura brizzolata perfettamente rifinita a 4 mm, sguardo ambrato glaciale e imponente da Prime Alpha, cicatrice sottile sul sopracciglio sinistro.\nAcconciatura: Capelli castano scuro brizzolati portati all'indietro con pomata opaca, tempie umane completamente coperte da ciocche fitte, due grandi orecchie da lupo grigio scuro e argento erette sulla sommità del capo. No orecchie umane."
  },
  {
    name: "The Verve VIP / Clubbing",
    description: "Abbigliamento: Camicia in seta nera aperta sui primi due bottoni che lascia intravedere il petto massiccio e scolpito, giacca destrutturata in pelle nera scamosciata morbida, pantaloni chino neri aderenti con asola sartoriale posteriore rinforzata per il passaggio della folta coda lupina.\nAccessori: Bicchiere di whisky di malto d'annata con ghiaccio, portafoglio in pelle nera sottile.\nScarpe: Stivaletti chelsea in cuoio nero opaco con suola in gomma ammortizzata.\nGioielli: Collana sottile in cordoncino di cuoio con ciondolo d'argento grezzo raffigurante la zanna di Fenris, anello d'argento runico.\nTrucco: Espressione rilassata ma vigile da predatore dominante, occhi ambrati luminosi nella penombra del club, leggera ombra di barba serale.\nAcconciatura: Capelli lunghi fino al collo lasciati cadere naturalmente con alcune ciocche morbide sul viso, tempie coperte, orecchie lupine singole attente ai bassi del locale. No orecchie umane."
  },
  {
    name: "Beach / Terme di Branco",
    description: "Abbigliamento: Boxer da bagno tecnici neri a pantaloncino con elastico in vita e cordino regolabile, dotati di apertura lombare sagomata posteriore rinforzata per consentire il libero movimento della folta coda da lupo grigio-nera.\nAccessori: Telo mare in spugna spessa nera con stemma ricamato Douglas, occhiali da sole polarizzati scuri con lenti rettangolari.\nScarpe: Piedi nudi sulla sabbia o sul bordo piscina in pietra termale, con unghie spesse e arcuate.\nGioielli: Anello con sigillo in platino indossato costantemente, collana in cuoio resistente all'acqua.\nTrucco: Gocce d'acqua che scivolano sui muscoli pettorali e dorsali massicci, pelle bronzea baciata dal sole, cicatrici di battaglia visibili sul torace.\nAcconciatura: Capelli bagnati tirati all'indietro dalle mani, tempie coperte da ciocche corvine, orecchie da lupo bagnate ma perfettamente reattive sulla testa. No orecchie umane."
  },
  {
    name: "Sleepwear / Padronale",
    description: "Abbigliamento: Pantaloni morbidi da notte in jersey di cotone elasticizzato grigio antracite, a gamba dritta, con elastico in vita morbido e ampia apertura lombare posteriore per accogliere la folta coda lupina a riposo. Petto nudo e possente esposto.\nAccessori: Nessuno.\nScarpe: Piedi nudi sul parquet in rovere massiccio della camera da letto padronale.\nGioielli: Solo la fede e l'anello con sigillo Douglas.\nTrucco: Espressione distesa e protettiva, respiro profondo e regolare, aura feromonale Alpha calda e calmante.\nAcconciatura: Capelli scarmigliati e morbidi sul cuscino, ciocche che coprono interamente la zona delle tempie, orecchie lupine adagiate all'indietro in modalità riposo. No orecchie umane."
  }
];

// 2. Malachia Douglas Bloodmoon (currently 8, add Casual/Street, Beach/Terme, Sleep -> 11)
const malachiaNewOutfits = [
  {
    name: "Casual / Streetwear Blackwood",
    description: "Abbigliamento: T-shirt nera pesante oversize in cotone da 240 g/m² con girocollo rinforzato, giacca di jeans lavaggio nero slavato con cuciture a contrasto, pantaloni cargo neri tattici con tasche laterali a soffietto e apertura lombare posteriore rinforzata per la possente coda lupina nera carbone.\nAccessori: Zaino monospalla tattico in cordura nera, smartphone blindato con cover in titanio.\nScarpe: Scarponcini da trekking urbani neri impermeabili con suola carrarmato.\nGioielli: Bracciale in maglia d'acciaio pesante al polso destro, torque runico Thurisaz inciso sul polso sinistro.\nTrucco: Sguardo intenso e scuro da Alpha dominante, mascella forte con barba incolta di due giorni, labbra piene e serie.\nAcconciatura: Capelli neri lunghi e mossi parzialmente raccolti in un mezzo chignon alto (half-bun), lati della testa fittamente coperti da ciocche scure, orecchie da lupo nere maestose ed erette. No orecchie umane."
  },
  {
    name: "Beach / Sorgenti Calde",
    description: "Abbigliamento: Costume da bagno a pantaloncino nero opaco sportivo con cuciture rinforzate e sagomatura posteriore lombare elasticizzata per la coda lupina. Petto colossale e dorsali ampi scoperti.\nAccessori: Occhiali da sole neri a goccia, telo mare in microfibra pesante.\nScarpe: Piedi nudi con artigli forti e cuscinetti reattivi sulla pietra calda.\nGioielli: Catenina sottile in titanio con ciondolo triangolare spezzato.\nTrucco: Pelle ambrata dorata, texture muscolare densa e definita con cicatrici da scontro sui fianchi e sulle spalle.\nAcconciatura: Capelli bagnati arruffati dal vento oceanico che coprono le tempie, orecchie lupine nere che vibrano al suono delle onde. No orecchie umane."
  },
  {
    name: "Sleepwear / Notte del Branco",
    description: "Abbigliamento: Pantaloni tuta morbidi in morbido felpato nero senza coulisse metalliche, con asola sartoriale posteriore che lascia libera la coda nera di muoversi nel sonno. Torace possente completamente scoperto.\nAccessori: Nessuno.\nScarpe: Piedi nudi.\nGioielli: Nessuno durante il sonno.\nTrucco: Viso rilassato nel sonno ma con l'istinto territoriale sempre vigile, respiro profondo da predatore dominante.\nAcconciatura: Capelli sciolti e spettinati che ricadono sul guanciale coprendo i lati della testa, orecchie lupine singole morbide e piegate nel sonno. No orecchie umane."
  }
];

// 3. Noah Douglas Bloodmoon (currently 8, add Party/Club -> 9)
const noahNewOutfits = [
  {
    name: "Party / Solarton Nightlife",
    description: "Abbigliamento: Camicia in raso di seta blu notte scuro con colletto sbottonato e maniche arrotolate fino ai gomiti, pantaloni sartoriali a sigaretta grigio fumo con taglio lombare posteriore perfetto per la folta coda lupina sfumata, cintura sottile in pelle fiore con fibbia in palladio.\nAccessori: Bicchiere da cocktail lowball in cristallo molato, smartphone sottile in lega leggera.\nScarpe: Scarpe stringate derby bordeaux lucide con suola in cuoio naturale.\nGioielli: Anello raffinato in oro bianco all'indice destro, catenina d'argento con piccolo ciondolo a prisma esagonale.\nTrucco: Sorriso sottile e magnetico da Delta astuto, occhi ambrati brillanti che analizzano ogni persona nella stanza, rasatura impeccabile.\nAcconciatura: Capelli castano dorato ondulati pettinati con morbidezza ma con precisione chirurgica, tempie celate dai capelli, orecchie da lupo color sabbia e ambra inclinate con garbo verso gli interlocutori. No orecchie umane."
  }
];

// 4. Logan Douglas (currently 7, add Casual/Home, Beach/Terme, Sleep -> 10)
const loganNewOutfits = [
  {
    name: "Casual / Casa e Relax",
    description: "Abbigliamento: Canotta a costine grigio mélange in cotone morbido aderente sui muscoli pettorali, felpa aperta con cappuccio in cotone nero slacciata, pantaloni tuta larghi e comodi in cotone scuro con apertura lombare posteriore rinforzata per la coda lupina grigio ferro.\nAccessori: Chiavi inglesi e tazza termica da caffè americano in acciaio.\nScarpe: Calzettoni pesanti in lana grigia o ciabatte ergonomiche in gomma nera.\nGioielli: Anello in ferro battuto con incisione della runa Eihwaz, bracciale in cuoio intrecciato consumato.\nTrucco: Espressione calma e accogliente da Beta pacificatore, occhi ambrati caldi, barba scura con qualche riflesso argentato ben curata.\nAcconciatura: Capelli castano-grigi corti ai lati ma fitti a coprire le tempie umane, orecchie lupine grigie rilassate verso l'alto. No orecchie umane."
  },
  {
    name: "Beach / Seven Hills Spa",
    description: "Abbigliamento: Pantaloncini da bagno sportivi in tessuto tecnico elasticizzato blu navy a rapida asciugatura, dotati di feritoia lombare posteriore per la coda grigio ferro.\nAccessori: Asciugamano in lino grezzo chiaro, occhiali da sole sportivi avvolgenti.\nScarpe: Sandali infradito in cuoio resistente all'acqua o piedi nudi.\nGioielli: Bracciale in paracord impermeabile nero e verde scuro.\nTrucco: Spalle larghe e braccia tatuate con motivi nordici e nodi celtici, gocce di vapore sulla pelle tonica.\nAcconciatura: Capelli umidi pettinati all'indietro, tempie coperte, orecchie lupine singole che si scrollano le gocce d'acqua. No orecchie umane."
  },
  {
    name: "Sleepwear / Riposo Notturno",
    description: "Abbigliamento: Pantaloni pigiama a quadri scuri in flanella di cotone traspirante, morbidi sui fianchi con asola posteriore per la coda lupina distesa. Petto nudo.\nAccessori: Nessuno.\nScarpe: Piedi nudi.\nGioielli: Nessuno a letto.\nTrucco: Lineamenti distesi e sereni, respiro calmo da guardiano fidato del branco.\nAcconciatura: Capelli liberi e arruffati dal riposo, lati della testa coperti, orecchie da lupo abbassate in rilassamento totale. No orecchie umane."
  }
];

// 5. Edric Douglas (currently 2, add Casual Street, Gala/Formal, Party/Club, Beach, Sleep, Nude, Hybrid Shift -> 9)
const edricNewOutfits = [
  {
    name: "Streetwear / Solarton Friends",
    description: "Abbigliamento: Hoodie oversize con cappuccio in cotone garzato bordeaux con logo vintage, jeans neri slim-fit strappati alle ginocchia con fessura lombare rinforzata posteriore per la vivace coda da lupo grigio cenere.\nAccessori: Cuffie audio wireless attorno al collo, skateboard da cruiser sottobraccio.\nScarpe: Sneakers da skate nere e bianche con lacci larghi.\nGioielli: Catenina d'argento con medaglietta d'acciaio sportiva.\nTrucco: Viso giovanile ed energico da diciassettenne, occhi ambrati vivaci e curiosi, pelle liscia e pulita.\nAcconciatura: Capelli castano scuro arruffati con frangia sbarazzina che cade sulla fronte e copre le tempie, due orecchie da lupo giovanili ed espressive sempre in movimento. No orecchie umane."
  },
  {
    name: "Gala / Formale Giovani Douglas",
    description: "Abbigliamento: Abito sartoriale giovanile due pezzi blu notte in lana fresca, camicia azzurro polvere con colletto all'italiana, cravatta sottile bordeaux in seta, pantaloni eleganti con taglio lombare posteriore perfetto per la coda.\nAccessori: Pochette bianca a punta nel taschino, spilla in argento della Casata Douglas sul risvolto.\nScarpe: Scarpe stringate in pelle marrone testa di moro spazzolata.\nGioielli: Orologio da polso con cinturino in cuoio regalatogli dal padre.\nTrucco: Postura composta ma ancora leggermente impacciata dall'etichetta rigida, sguardo orgoglioso di appartenere al branco.\nAcconciatura: Capelli pettinati con riga laterale ordinata e cera leggera, tempie schermate dai capelli, orecchie lupine ben ritte e composte. No orecchie umane."
  },
  {
    name: "Party / Festa Studentesca",
    description: "Abbigliamento: T-shirt grafica vintage nera di una band rock, camicia di flanella aperta a quadri rossi e neri, jeans scuri con asola posteriore per la coda.\nAccessori: Boccale di birra rossa in plastica, braccialetti in silicone del festival studentesco.\nScarpe: Sneakers in tela alte con suola in gomma.\nGioielli: Braccialetto in cuoio intrecciato.\nTrucco: Risata aperta e gioviale, guance leggermente arrossate dal calore della festa, sguardo fiero e amichevole.\nAcconciatura: Capelli mossi e voluminosi, tempie coperte, orecchie da lupo che si muovono al ritmo della musica. No orecchie umane."
  },
  {
    name: "Beach / Pomeriggio in Piscina",
    description: "Abbigliamento: Boxer da mare a pantaloncino con motivo tropicale scuro e cordino regolabile, con apertura posteriore lombare rinforzata per la coda che sventola felice.\nAccessori: Occhiali da sole sportivi colorati, palla da beach volley sottobraccio.\nScarpe: Ciabatte da piscina o piedi nudi sull'erba.\nGioielli: Nessuno in acqua.\nTrucco: Fisico giovane e asciutto, muscoli definiti dall'atletica leggera e dalle corse di branco, sorriso radioso.\nAcconciatura: Capelli bagnati che cadono sugli occhi, orecchie lupine bagnate che spruzzano gocce d'acqua con uno scrollo vivace. No orecchie umane."
  },
  {
    name: "Sleepwear / Notte in Camera",
    description: "Abbigliamento: Maglietta grigia a maniche corte morbida e pantaloni corti da pigiama in cotone elasticizzato con ampia asola posteriore per la coda.\nAccessori: Controller da gaming wireless sulla scrivania.\nScarpe: Piedi nudi o calzini corti in cotone.\nGioielli: Nessuno.\nTrucco: Espressione rilassata e un po' assonnata dopo ore passate a giocare o a studiare.\nAcconciatura: Capelli spettinati e ribelli, tempie coperte, orecchie lupine morbide appoggiate sui capelli. No orecchie umane."
  },
  {
    name: "Nude / Anatomia Giovanile",
    description: "Abbigliamento: Nessuno. Completo nudo naturale.\nAccessori: Nessuno.\nScarpe: Piedi nudi atletici con archi plantari forti e artigli naturali.\nGioielli: Piccolo ciondolo in corda attorno al collo.\nTrucco: Corporatura giovane ma robusta da 182 cm, pelle ambrata integra, muscolatura tonica in sviluppo, genitali maschili sani con guaina lupina giovanile alla base.\nAcconciatura: Capelli scarmigliati al naturale che coprono le tempie, due orecchie lupine singole e folta coda color cenere. No orecchie umane."
  },
  {
    name: "Hybrid Shift / Addestramento Bipede",
    description: "Abbigliamento: Nessuno. Pura forma ibrida licantropica bipede da 230 cm con muscolatura espansa e densa ricoperta da folta pelliccia grigio fumo e nera.\nAccessori: Nessuno.\nScarpe: Zampe posteriori digitigradi con cuscinetti neri gommati e artigli ricurvi affilati in grado di affondare nella terra.\nGioielli: Nessuno.\nTrucco: Muso allungato con zanne prominenti e affilate, occhi ambrati che brillano di luminescenza dorata, narici fremiti dall'odore del branco.\nAcconciatura: Pelliccia fitta che fluisce dalla criniera dorsale senza alcuna soluzione di continuità, orecchie da lupo grandi e appuntite sulla sommità. No orecchie umane."
  }
];

// 6. Elizabeth Duskwood (currently 1, add Casual, Business, Gala, Party, Beach, Sleep, Nude, Hybrid -> 9)
const elizabethNewOutfits = [
  {
    name: "Casual / Residenza Duskwood",
    description: "Abbigliamento: Maglione a collo alto in morbido cachemire panna, pantaloni a palazzo in lana pettinata verde bosco scuro con apertura lombare sartoriale per la maestosa coda lupina argentea.\nAccessori: Tazza di porcellana con infuso di erbe del bosco, libro rilegato in pelle antica.\nScarpe: Pantofole in velluto verde smeraldo con suola sottile in cuoio.\nGioielli: Orecchini a goccia in argento antico montati con pietre di luna, anello di matriarca Duskwood all'anulare.\nTrucco: Bellezza aristocratica matura e senza tempo, pelle di porcellana lunare, occhi azzurro ghiaccio intensi, labbra color rosa antico.\nAcconciatura: Lunghi capelli biondo cenere e argento raccolti parzialmente con un fermaglio in filigrana d'argento, tempie coperte da ciocche ondulate, due orecchie da lupo argenteo erette e aristocratiche. No orecchie umane."
  },
  {
    name: "Business / Conclave delle Casate",
    description: "Abbigliamento: Tailleur sartoriale doppiopetto grigio perla con bottoni in madreperla argentata, camicia in seta pura con colletto lavallière annodato con grazia, gonna a tubino longuette con spacco lombare rinforzato per la coda.\nAccessori: Cartella portadocumenti in pelle pregiata con sigillo in ceralacca Duskwood.\nScarpe: Décolleté a punta in pelle grigia spazzolata con tacco a rocchetto medio.\nGioielli: Spilla nobiliare raffigurante il ramo di betulla e il lupo in platino e zaffiri.\nTrucco: Espressione inflessibile e regale da Matriarca di Sangue Puro, occhi chiarissimi che scrutano ogni alleato e rivale.\nAcconciatura: Capelli raccolti in un'acconciatura a chignon regale che lascia morbide onde a coprire le tempie, orecchie lupine singole impassibili e attente. No orecchie umane."
  },
  {
    name: "Gala / Solstizio d'Inverno",
    description: "Abbigliamento: Abito lungo da sera in velluto blu notte notte con scollo a barchetta ricamato con cristalli d'argento e perle, corpetto sagomato e gonna ampia con asola lombare foderata per la splendida coda argentea.\nAccessori: Guanti lunghi da sera in raso bianco avorio, stola in tessuto pesante argentato.\nScarpe: Scarpe da sera gioiello con cinturino alla caviglia.\nGioielli: Diadema sottile in platino a motivi di fogliame runico Berkano, collana di perle naturali a tre fili.\nTrucco: Trucco raffinato con sfumatura grigio fumo sugli occhi glaciali, portamento imperioso e materno al contempo.\nAcconciatura: Acconciatura sontuosa intrecciata con fili d'argento, orecchie da lupo maestose che svettano con grazia sovrana. No orecchie umane."
  },
  {
    name: "Party / Soirée Aristocratica",
    description: "Abbigliamento: Abito da cocktail midi in chiffon di seta nero con ricami floreali in pizzo chantilly grigio argento, aderente sul busto e svasato sui fianchi con fessura lombare per la coda.\nAccessori: Pochette rigida in madreperla e argento, calice di vino d'annata.\nScarpe: Sandali eleganti con listini sottili in raso nero.\nGioielli: Bracciale rigido in argento cesellato a mano con motivi di rami sacri.\nTrucco: Sorriso enigmatico e diplomatico, sguardi taglienti e misurati, pelle luminosa.\nAcconciatura: Onde morbide argentee che incorniciano il volto e schermano completamente le tempie, orecchie lupine singole che captano ogni bisbiglio della sala. No orecchie umane."
  },
  {
    name: "Beach / Sorgenti Private Duskwood",
    description: "Abbigliamento: Costume intero elegante modellante nero con profondo scollo sulla schiena e apertura lombare rinforzata per il passaggio della folta coda lupina argentea.\nAccessori: Kimono estivo in seta stampata a motivi di betulla da indossare aperto, occhiali da sole da diva.\nScarpe: Sandali infradito in cuoio intrecciato argento.\nGioielli: Cavigliera sottile in argento all'articolazione destra.\nTrucco: Pelle idratata e luminosa dalle acque sulfuree termali, sguardo rilassato lontano dagli intrighi politici.\nAcconciatura: Capelli raccolti in una treccia morbida laterale, tempie coperte, orecchie da lupo argentine rilassate. No orecchie umane."
  },
  {
    name: "Sleepwear / Alcova Matriarcale",
    description: "Abbigliamento: Camicia da notte lunga fino alle caviglie in finissima seta color avorio con spalline sottili e profonda apertura lombare posteriore per la coda distesa tra i cuscini.\nAccessori: Nessuno.\nScarpe: Piedi nudi curati.\nGioielli: Solo la fede d'argento antico.\nTrucco: Viso completamente privo di trucco, lineamenti nobili sereni nel riposo solitario, respiro pacato.\nAcconciatura: Capelli sciolti lunghi fino alla vita che avvolgono le spalle come un manto argentato, orecchie lupine soffici ripiegate. No orecchie umane."
  },
  {
    name: "Nude / Sangue Puro Antico",
    description: "Abbigliamento: Nessuno. Pura forma nuda anatomica.\nAccessori: Nessuno.\nScarpe: Piedi nudi nobili con archi alti e cuscinetti delicati.\nGioielli: Ciondolo della runa Berkano su catenina d'argento al collo.\nTrucco: Fisico femminile giunonico e regale da 178 cm, pelle lattea priva di imperfezioni, seni pieni e armoniosi, ventre piatto con la runa della fertilità incisa con inchiostro sacro d'argento alla base dell'ombelico, monte di venere curato.\nAcconciatura: Criniera argentea che copre interamente la zona delle tempie umane, due orecchie lupine nobili e maestose. No orecchie umane."
  },
  {
    name: "Hybrid Shift / Matriarca da Guerra",
    description: "Abbigliamento: Nessuno. Forma ibrida bipede di pura stirpe licantropica alta 245 cm con pelliccia color argento e platino luminosa.\nAccessori: Nessuno.\nScarpe: Zampe posteriori digitigradi poderose con artigli argentei affilati come rasoi.\nGioielli: Nessuno.\nTrucco: Muso lupino affilato ed elegante, zanne candide velenose al tocco magico, occhi azzurro fosforescente carichi di autorità materna e protettiva.\nAcconciatura: Pelliccia dorsale folta che si fonde con la criniera lunare, orecchie lupine singole svettanti e spaventose. No orecchie umane."
  }
];

// Helper to append outfits without duplicates
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

// Update the 6 family members first
console.log('=== ENRICHING CORE DOUGLAS OUTFITS ===');
appendOutfits('FINAL/Erik_Douglas_card.json', erikNewOutfits);
appendOutfits('FINAL/Malachia_Douglas_Bloodmoon_card.json', malachiaNewOutfits);
appendOutfits('FINAL/Noah_Douglas_Bloodmoon_card.json', noahNewOutfits);
appendOutfits('FINAL/Logan_Douglas_card.json', loganNewOutfits);
appendOutfits('FINAL/Edric_Douglas_card.json', edricNewOutfits);
appendOutfits('FINAL/Elizabeth_Duskwood_card.json', elizabethNewOutfits);
