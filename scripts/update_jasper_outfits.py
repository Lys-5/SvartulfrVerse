import sys
import json
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
JASPER_ID = '_x3VY2kcbaDbKyCqywGeET'

jasper_outfits = [
    {
        "id": "outfit-1790647968603-j01",
        "name": "Casual / Home",
        "avatar": "",
        "description": "Abbigliamento: Felpa oversize con cappuccio in morbido cotone nero slavato con grafica streetwear sbiadita e tascone a marsupio frontale, indossata sopra una t-shirt scura in jersey leggero. Pantaloni jogger neri con polsini elastici alle caviglie e coulisse in vita, dotati di apertura posteriore rinforzata per consentire piena mobilità alla folta coda da lupo color castano caramello con punta nera.\nAccessori: Cuffie wireless professionali circumaurali nere e verde acido portate attorno al collo. Smartwatch multifunzione modificato per il bypassing e lo slicing informatico al polso sinistro. Chiavette USB di backup agganciate a un moschettone nero alla vita.\nScarpe: Sneakers alte high-top in tela nera con suola in gomma bianca consumata e stringhe allentate.\nGioielli: Anello con sigillo della casata Douglas d'argento massiccio all'anulare sinistro. Piercing barbells d'argento a entrambi i capezzoli sotto gli indumenti. Sottili cerchietti piatti in titanio scuro lungo la cartilagine dell'orecchio lupino sinistro. Tatuaggio runico Gebo e Mannaz visibile sulla faccia interna del polso sinistro.\nTrucco: Viso completamente al naturale, privo di cosmetici. Leggera ombra di barba incolta sul mento e labbra idratate con balsamo neutro.\nAcconciatura: Taglio wolf-cut spettinato color castano caramello con ciocche disordinate che ricadono sulla fronte e attorno agli occhi verde menta. Orecchie lupine singole castano caramello con punte nere erette sulla sommità del capo, completamente scoperte e mobili."
    },
    {
        "id": "outfit-1790647968603-j02",
        "name": "Campus",
        "avatar": "",
        "description": "Abbigliamento: T-shirt in cotone pettinato grigio antracite a girocollo con logo vintage sbiadito da conferenza tech o band underground. Pantaloni cargo tecnici grigio fumo a vestibilità rilassata, provvisti di ampie tasche laterali a soffietto con cinghie regolabili e asola posteriore rifinita per la coda da lupo caramello con estremità nera.\nAccessori: Borsa a tracolla messenger tattica idrorepellente in cordura nera contenente laptop corazzato, cavi e unità hardware esterne. Auricolari wireless in-ear neri inseriti nelle orecchie lupine. Smartwatch da programmazione al polso sinistro.\nScarpe: Sneakers da skate in camoscio grigio e nero con suola vulcanizzata piatta e lacci neri piatti.\nGioielli: Anello d'argento con sigillo Douglas all'anulare sinistro. Serie di piercing a barretta e cerchietti in titanio sulle orecchie lupine. Barbells d'argento ai capezzoli sotto la t-shirt. Tatuaggio runico combinato Gebo e Mannaz sulla piega del polso sinistro.\nTrucco: Nessun cosmetico. Pelle chiara e pulita, occhiaie leggere visibili da lavoro notturno al computer, labbra al naturale.\nAcconciatura: Capelli castano caramello disordinati e scalati in un wolf-cut asimmetrico con ciuffi che scendono sugli occhi verde menta. Orecchie lupine caramello con sfumature scure ben visibili tra le ciocche superiori."
    },
    {
        "id": "outfit-1790647968603-j03",
        "name": "Tactical Guild (Spell-Hacker Infiltrator)",
        "avatar": "",
        "description": "Abbigliamento: Felpa tattica da infiltrazione in shadow-silk grigio scuro fonoassorbente e idrorepellente con pannelli protettivi in kevlar su spalle e avambracci, cappuccio sagomato con alloggiamenti per le orecchie lupine e colletto aperto sul retro. Maglia a compressione traspirante nera a maniche lunghe a contatto con la pelle. Pantaloni cargo operativi neri antistrappo multi-tasche con alloggiamenti modulari e fessura anatomica rinforzata per la coda da lupo color caramello con punta nera.\nAccessori: Cinturone modulare nero a sgancio rapido con tasche rigide per bypass prismatici, cipher spikes e batterie di mana. Tracolla diagonale magnetica sulla schiena con fodero rigido contenente la Katana in Vetro di Drago di Nixara. Smartwatch olografico tattico ad alta frequenza al polso sinistro. Guanti tecnici tattici da hacker senza dita con inserti in microfibra conduttiva per schermi touch. Cuffie antirumore ad attenuazione frequenziale da ricognizione adagiate attorno al collo.\nScarpe: Stivali da combattimento neri a taglio medio con suola vibram ammortizzata a profilo silenzioso e allacciatura rapida in paracord.\nGioielli: Anello con sigillo Douglas d'argento all'anulare sinistro. Piercing d'argento ai capezzoli sotto la maglia. Tre cerchietti neri in titanio opaco sull'orecchio lupino sinistro. Tatuaggio runico protettivo Gebo e Mannaz al polso sinistro.\nTrucco: Pittura tattica opaca antiriflesso grigio fumo su zigomi e setto nasale per azzerare il riverbero luminoso. Labbra al naturale.\nAcconciatura: Capelli castano caramello raccolti parzialmente con una fascia elastica tecnica nera sotto il cappuccio sagomato. Orecchie da lupo singole caramello con estremità scure che fuoriescono dalle apposite feritoie del cappuccio, libere di muoversi."
    },
    {
        "id": "outfit-1790647968603-j04",
        "name": "The Abyssal Armor (Summoned Demonic Steel)",
        "avatar": "",
        "description": "Abbigliamento: Corazza completa in acciaio demoniaco nero fumo evocata magicamente, composta da pettorale sagomato a piastre sovrapposte che assorbono la luce, spallacci articolati laminati, parabracci incisi con rune d'occultamento luminescenti e cosciali scanalati. Gambali segmentati con giunture flessibili in maglia d'ombra e apertura anatomica lombare sagomata per la coda da lupo caramello con punta scura.\nAccessori: Fodero dorsale magnetico forgiato in ferro abissale contenente la Katana in Vetro di Drago di Nixara. Foderi laterali alle cosce con due pugnali da parata ricurvi in acciaio nero. Guanti d'arme metallici affilati a cinque dita con artigli d'acciaio demoniaco integrati. Cappuccio metallico spettrale che avvolge il capo lasciando visibili solo gli occhi verde menta.\nScarpe: Schinieri e calzari corazzati in acciaio demoniaco articolato con suole ferrate ad assorbimento d'impatto.\nGioielli: Anello con sigillo Douglas d'argento mantenuto sotto il guanto d'arme. Cerchietti in ferro abissale inseriti sulle orecchie lupine. Tatuaggio runico Gebo e Mannaz sul polso sinistro visibile tra gli spacchi delle placche runiche dell'avambraccio.\nTrucco: Ombreggiatura naturale del viso oscurata dal cappuccio d'acciaio fumo. Sguardo evidenziato dal contrasto tra la penombra del metallo e il verde menta acceso degli occhi.\nAcconciatura: Ciocche castano caramello compresse sotto il copricapo corazzato. Orecchie lupine caramello alloggiate nelle aperture apposite ricavate ai lati del cappuccio demoniaco."
    },
    {
        "id": "outfit-1790647968603-j05",
        "name": "Underground DJ / The Verve",
        "avatar": "",
        "description": "Abbigliamento: Felpa smanicata oversize con ampio cappuccio in tessuto tecnico nero opaco con grafiche geometriche riflettenti e profili ciano luminescenti reattivi agli UV, lasciata aperta sul davanti. Canotta nera in mesh traforato elasticizzato a scollo profondo che mostra il torace asciutto e definito. Pantaloni jogger tecnici neri a vita bassa con tasche asimmetriche, cinghie pendenti e apertura anatomica rinforzata per la coda da lupo caramello con punta nera.\nAccessori: Cuffie professionali da monitoraggio DJ sovraurali con archetto imbottito calzate sulle orecchie o attorno al collo. Guantini da mixaggio senza dita in pelle sintetica nera e tessuto tecnico grippante. Bracciali biometrici a led con display programmabile su frequenze ciano sincronizzate ai bpm. Catena a maglie d'argento agganciata ai passanti laterali dei pantaloni.\nScarpe: Sneakers high-top futuristiche in pelle nera con suola spessa in gomma trasparente dotata di inserti luminosi a led ciano e cavigliere imbottite.\nGioielli: Anello con sigillo Douglas d'argento all'anulare sinistro. Orecchini a cerchio e cuff a clip in argento e titanio nero su entrambe le orecchie lupine. Barbells d'argento ai capezzoli visibili attraverso la trama della canotta traforata. Tatuaggio runico Gebo al polso sinistro.\nTrucco: Due linee grafiche orizzontali luminescenti ciano reattive alla luce nera stese sotto gli occhi. Pelle chiara e pulita con finitura satinata e labbra al naturale.\nAcconciatura: Taglio wolf-cut spettinato castano caramello con lunghe ciocche scalate che ricadono sul viso. Cappuccio della felpa abbassato sulle spalle o tenuto morbido per lasciare scoperte le orecchie lupine erette."
    },
    {
        "id": "outfit-1790647968603-j06",
        "name": "Formal / Gala",
        "avatar": "",
        "description": "Abbigliamento: Abito sartoriale due pezzi in lana pettinata color antracite scuro con rever a lancia in raso nero. Camicia formale bianca in popeline di cotone lasciata sbottonata ai primi due bottoni sul colletto senza cravatta con maniche leggermente tirate sugli avambracci. Pantaloni sartoriali a gamba dritta coordinati con taglio sartoriale posteriore invisibile e rifinito per la coda da lupo caramello con punta nera.\nAccessori: Giacca portata aperta senza chiusura dei bottoni. Gemelli da polso in argento con incisione stilizzata del lupo Douglas. Smartwatch da slicing schermato da un polsino o tenuto sotto la manica. Cintura in cuoio nero opaco con fibbia rettangolare in argento spazzolato.\nScarpe: Scarpe modello francesina stringate in pelle nera lucida con suola sottile in cuoio e cuciture tono su tono.\nGioielli: Anello con sigillo Douglas in argento massiccio all'anulare sinistro. Cerchietti sottili e piatti d'argento lucido allineati lungo la cartilagine dell'orecchio lupino sinistro. Fermacravatta d'argento portato nel taschino della giacca. Tatuaggio runico Gebo e Mannaz sul polso sinistro coperto dal polsino della camicia.\nTrucco: Viso rasato di fresco con pelle idratata e pulita a finitura opaca. Labbra protette da un velo di balsamo neutro.\nAcconciatura: Capelli castano caramello pettinati all'indietro con pomata lucida ma con ciocche ribelli del wolf-cut che ricadono spontaneamente sulla fronte. Orecchie lupine caramello dritte ed eleganti, con pelo spazzolato e rifinito."
    },
    {
        "id": "outfit-1790647968603-j07",
        "name": "Sleepwear",
        "avatar": "",
        "description": "Abbigliamento: T-shirt oversize sbiadita in cotone morbido grigio melange o nero con scollo tondo allargato e stampa vintage da concerto rock. Pantaloncini corti da notte in jersey di cotone nero a gamba larga con elastico e coulisse in vita, provvisti di ampia fessura posteriore per consentire piena mobilità alla folta coda da lupo caramello con estremità nera.\nAccessori: Nessuno.\nScarpe: Piedi completamente scalzi con unghie curate al naturale.\nGioielli: Anello con sigillo Douglas all'anulare sinistro. Sottili cerchietti d'argento sulle orecchie da lupo. Barbells in argento ai capezzoli. Tatuaggio runico Gebo e Mannaz visibile sul polso sinistro.\nTrucco: Viso completamente pulito e struccato, pelle fresca e idratata al naturale. Labbra morbide e idratate con balsamo neutro.\nAcconciatura: Capelli castano caramello completamente spettinati e arruffati, lasciati cadere liberi sulla fronte e sul collo. Orecchie lupine caramello rilassate, morbide e rivolte leggermente all'indietro o abbassate in posizione di riposo."
    },
    {
        "id": "outfit-1790647968603-j08",
        "name": "Beach",
        "avatar": "",
        "description": "Abbigliamento: Pantaloncini da surf a mezza coscia in tessuto tecnico elasticizzato ad asciugatura rapida a fondo nero con sfumature geometriche verde acido e ciano, dotati di chiusura frontale in velcro, coulisse regolabile e apertura posteriore rinforzata per la coda da lupo caramello con punta scura. Busto e addome completamente nudi che mettono in risalto la corporatura asciutta e i muscoli tonici.\nAccessori: Custodia impermeabile rigida trasparente per smartphone agganciata con un moschettone in polimero al passante dei pantaloncini. Occhiali da sole squadrati neri con lenti specchiate ciano polarizzate a protezione UV. Telo mare in microfibra grigio scuro portato arrotolato a tracolla.\nScarpe: Infradito da spiaggia nere con suola ergonomica in gomma sagomata, o piedi nudi a contatto con la sabbia.\nGioielli: Anello con sigillo Douglas in argento sterling all'anulare sinistro. Cordino nero al collo con piccolo pendente impermeabile in titanio. Serie di cerchietti in titanio resistenti alla salsedine sulle orecchie lupine. Piercing barbells d'argento ai capezzoli. Tatuaggio runico Gebo al polso sinistro ben visibile sulla pelle.\nTrucco: Protezione solare trasparente a rapido assorbimento con effetto opaco su viso, spalle e dorso. Labbra protette con stick solare idratante.\nAcconciatura: Capelli castano caramello mossi e scompigliati dalla brezza marina e dalla salsedine, pettinati all'indietro solo con le dita. Orecchie lupine caramello libere ed erette sulla testa, sensibili al rumore delle onde."
    },
    {
        "id": "outfit-1790647968603-j09",
        "name": "Full Shift",
        "avatar": "",
        "description": "Abbigliamento: Nessuno. Forma quadrupede lupina completa da lupo gigante (dire wolf) della Founding Bloodline. Pelliccia fitta, corta e lucente color castano caramello uniforme su tutto il corpo, con sfumature più scure lungo la linea dorsale e la punta della coda completamente nera, priva di marchi lunari bianchi. Corporatura slanciata, muscolosa e agile, progettata per la velocità e la corsa scattante.\nAccessori: Nessuno. Tutto l'equipaggiamento tecnologico, i vestiti e i dispositivi hardware vengono rimossi prima della trasformazione per evitare danni.\nScarpe: Zampe da lupo poderose con cuscinetti plantari neri callosi e resistenti, artigli retrattili neri affilati e adatti alla trazione rapida su qualsiasi terreno.\nGioielli: Nessuno. La magia della trasformazione assorbe temporaneamente gli ornamenti metallici, mentre il tatuaggio runico di Gebo e Mannaz rimane impresso a livello eterico nella struttura spirituale del lupo.\nTrucco: Muso da lupo affusolato e asciutto al naturale. Dentatura ferale perfetta con zanne candide. Occhi color verde menta vividi, luminosi, intelligenti e calcolatori.\nAcconciatura: Mantello animale folto e compatto con una criniera più densa sul collo e sulle spalle. Grandi orecchie da lupo caramello con bordo esterno nero, mobili a 180 gradi per captare ogni frequenza e vibrazione sonora."
    },
    {
        "id": "outfit-1790647968603-j10",
        "name": "Hybrid Shift",
        "avatar": "",
        "description": "Abbigliamento: Nessuno. Forma ibrida bipede di 223 cm (7'4\") di altezza, con massa muscolare agile, scattante e definita, ottimizzata per la velocità e le manovre di evasione. Pelliccia fitta e serica color castano caramello che riveste torso, arti e dorso, con la schiena leggermente più scura e la lunga coda lupina caramello con punta nera, interamente priva di marcature bianche lunari.\nAccessori: Nessuno.\nScarpe: Arti inferiori digitigradi con zampe ibride plantari rinforzate, cuscinetti elastici neri e artigli lupini affilati a contatto diretto col terreno.\nGioielli: Nessun ornamento fisico. Il legame runico Gebo e Fenris pulsa come una luminescenza argentata intermittente sottopelle lungo la muscolatura dell'avambraccio sinistro. Piccoli barbells metallici assorbiti a livello energetico.\nTrucco: Maschera facciale lupina con muso allungato e mandibola articolata. Canini affilati e occhi verde menta brillanti ed estremamente vigili. Finitura del pelo asciutta e priva di trattamenti artificiali.\nAcconciatura: Folta criniera castano caramello che corre lungo la nuca e la spina dorsale fino alla base della coda. Orecchie lupine appuntite ed erette sulla sommità del cranio, capaci di appiattirsi contro il capo durante i movimenti ad alta velocità."
    }
]

def main():
    token = get_auth_token()
    if not token:
        print("Error: Could not get auth token")
        return

    print("Fetching Jasper live card...")
    char = get_char(token, JASPER_ID)
    print("Live character:", char.get("display_name"))
    print("Current outfits count:", len(char.get("outfits", [])))

    # Preserve any existing avatars or extra fields if any
    existing_outfits_map = {o.get("id"): o for o in char.get("outfits", [])}
    for new_o in jasper_outfits:
        oid = new_o["id"]
        if oid in existing_outfits_map:
            exist = existing_outfits_map[oid]
            if exist.get("avatar"):
                new_o["avatar"] = exist["avatar"]

    # Send PUT request with partial body
    print("Updating outfits on Wyvern API...")
    body = {"outfits": jasper_outfits}
    res = put_char(token, JASPER_ID, body)
    print("PUT response received:", bool(res))

    # Verify via fresh GET
    print("Verifying via GET...")
    updated_char = get_char(token, JASPER_ID)
    verified_outfits = updated_char.get("outfits", [])
    print(f"Verified outfits count: {len(verified_outfits)}")
    all_ok = True
    for i, o in enumerate(verified_outfits):
        print(f"[{i}] {o.get('name')}: {len(o.get('description', ''))} chars")
        if "Abbigliamento:" not in o.get('description', '') or "Acconciatura:" not in o.get('description', ''):
            all_ok = False
            print("  WARNING: Missing schema keys in", o.get('name'))

    if all_ok:
        print("\nSUCCESS: All 10 outfits for Jasper standardized and verified!")
    else:
        print("\nWARNING: Some outfits did not match expected structure.")

if __name__ == "__main__":
    main()
