import sys
import json
import urllib.request
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
BASE_URL = 'https://app.wyvern.chat/api/worlds/characters'

# ─── Outfit descriptions to inject ────────────────────────────────────────────
# Format: { character_id: { outfit_name: description } }
OUTFIT_DESCRIPTIONS = {

    # ── KALADIN NARGATHON ─────────────────────────────────────────────────────
    '_b7QqV43D8pU1tewx4qenY': {
        'Duty / Tactical (Default)': (
            "Black tactical gear built for function, not intimidation, though it does both. "
            "Fitted plate carrier over a compression shirt, cargo pants, boots broken in from years of wear, "
            "sidearm holstered at the hip, earpiece almost always in. No insignia, no unit patches, nothing that "
            "identifies him beyond the DCC crest on the shoulder. This is the outfit Kaladin defaults to whenever "
            "he is on duty at Villa Douglas, which is most of the time."
        ),
        'Off-Duty / Casual': (
            "A plain henley or grey t-shirt, dark jeans, boots he never quite swaps for anything softer. "
            "Even off-duty Kaladin dresses like he might need to move fast, nothing loose, nothing that catches "
            "on a doorframe. The only real difference from his tactical look is the absence of the plate carrier "
            "and the sidearm, though the earpiece is rarely far from reach."
        ),
        'Formal / Family Event': (
            "A charcoal suit, no tie, top button undone, the closest Kaladin comes to blending in at a family "
            "function. He still stands slightly apart from the room, back never fully to a door, drink usually "
            "untouched. Worn only for the rare formal occasion the Douglas family requires his presence at rather "
            "than his protection."
        ),
        'Full Shift': (
            "His complete quadrupedal wolf form, born from Project Blackwolf rather than natural bloodline, and "
            "already larger than a natural Alpha's full wolf shift before the mutation is accounted for. His fur "
            "is mutated black, thicker and rougher than a natural wolf's coat, and his eyes burn solid red the "
            "instant he commits to the shift, a total loss of the pale grey he carries as a man. Larger fangs "
            "and claws than the shift should produce mark him unmistakably as Gamma-7 work. He moves with the "
            "same calculating precision he has on two legs: silent, exact, never wasted motion."
        ),
        'Hybrid Shift': (
            "His bipedal hybrid form, scaled well past a natural Alpha's shift before the Blackwolf mutation "
            "adds anything further. Dense functional muscle on a frame the program pushed past its limits. "
            "His fur turns mutated black, his claws and fangs grow well beyond what a normal hybrid produces, "
            "and his pale grey eyes burn a solid flat red. He uses this form only on duty, and only when "
            "Vanguard Security needs more than a man can give, never to intimidate for its own sake."
        ),
    },

    # ── WULFNIC BLOODMOON ─────────────────────────────────────────────────────
    '_W9PLYt9ERTBJBXqKQL2en': {
        'Sanctuary / Longhouse': (
            "Dentro il Longhouse di Svartulfr, Wulfnic si muove in abiti da casa antichi e pesanti: una lunga "
            "tunica in lana grezza scura, allacciata in vita da una cintura di cuoio intrecciata con fibbia di "
            "ferro. I suoi lunghi capelli argentati sono sciolti o raccolti in due trecce laterali. I piedi nudi "
            "battono le assi di legno antico senza fare rumore. Nessun mantello, nessun accessorio cerimoniale. "
            "Solo la scure rituale appoggiata vicino al focolare centrale, sempre a portata di mano."
        ),
        'Ceremonial / Formal': (
            "La tenuta cerimoniale completa della Fede di Fenris: pesante tunica di lana nera con ricami runici "
            "dorati sulle maniche e sul colletto, sopra cui cade il mantello di pelliccia di lupo bianca, il "
            "segno del Jarl. Le trecce argentate sono intrecciate con sottili strisce di cuoio e rune scolpite "
            "nell'osso. Alle mani portenti anelli scolpiti in argento antico con rune di potere. La scure "
            "cerimoniale con il manico in legno di yew e la lama incisa con i Nove Nomi di Fenris pende alla "
            "cintura. La sua presenza in questa tenuta svuota le stanze di qualsiasi rumore."
        ),
        'Rest': (
            "Una veste di riposo in tessuto di lana grezza color cenere, lunga fino alle ginocchia, senza "
            "cintura. I capelli sono sciolti e cadono pesanti sulle spalle e sul petto. Nessun accessorio, "
            "nessun anello, nessun segno di rango. In questa forma Wulfnic assomiglia a qualsiasi anziano lupo "
            "comune, finche non si volta e si vedono le cicatrici antiche e gli occhi sintetici che non dormono "
            "mai davvero."
        ),
        'Shoreline': (
            "Quando accompagna i nipoti verso la costa, Wulfnic porta pantaloni pesanti in tela grezza scura "
            "e una camicia di lana aperta sul petto, con le maniche arrotolate oltre i gomiti. I piedi nudi "
            "nella sabbia o nella pietra. Il mantello di pelliccia rimane al Longhouse. L'unico elemento "
            "invariato sono gli anelli runici alle mani e il coltello da caccia alla cintura, affilato come "
            "il primo giorno."
        ),
        'Vigil / Watch': (
            "La tenuta da veglia e da guardia: tunica di lana spessa con cappuccio basso, mantello da viaggio "
            "in pelle di cervo conciata a mano, stivali di cuoio pesante con le suole rinforzate. Si confonde "
            "con la foresta meglio di qualsiasi lupo comune nonostante la sua statura di 248 cm. In questa "
            "tenuta rimane immobile per ore ai margini del bosco di Blackwood, osservando la Villa Douglas "
            "dall'esterno, come ha fatto ogni notte da quando Nixara non c'e piu."
        ),
        'The Gag Shirt': (
            "Jasper gli ha regalato a Natale una t-shirt nera con la scritta in stampatello bianco: "
            "\"World's Okayest Alpha\". Wulfnic non capisce cosa significhi. La indossa comunque, "
            "perche Jasper ha riso quando gliela metteva e questo gli basta. La t-shirt e chiaramente "
            "taglia XXL umana, quindi aderisce alla sua cassa toracica come una canottiera. La porta "
            "abbinata ai pantaloni da Longhouse e agli stivali di cuoio, ignaro totalmente dell'effetto "
            "che produce."
        ),
        'Full Shift': (
            "La forma quadrupede completa di Wulfnic e una delle pochissime cose al mondo che fanno "
            "ammutolire Erik Douglas. Un lupo argentato di dimensioni impossibili, spalle che raggiungono "
            "il petto di un adulto, mantello spesso come tappeto invernale. Gli occhi sintetici rimangono "
            "inalterati: ghiaccio puro che non riflette la luce come dovrebbe. Si muove in silenzio assoluto "
            "nonostante la massa, lasciando impronte profonde 10 cm nella terra. La Fede di Fenris lo chiama "
            "Hvit-Ulfr, il Lupo Bianco di Fenris."
        ),
        'Hybrid Shift': (
            "La forma bipede ibrida raggiunge i 280 cm di altezza, larghezza delle spalle paragonabile a un "
            "portale. La pelliccia e argentata con sfumature quasi bianche sulle zampe e sul petto. Le mani "
            "ibride conservano ancora gli anelli runici, miracolosamente integri nella transizione. Gli occhi "
            "sintetici diventano due pozze di luce fredda nell'oscurita. La sua voce in questa forma e ancora "
            "riconoscibile come la sua: Old Norse, lento, assolutamente immune al panico."
        ),
    },

    # ── ZEFIR HVITSKOG ────────────────────────────────────────────────────────
    '_FJhtBq4xUM4aUWpaJAPYF': (lambda: {
        'White Ghost Scout Shroud': (
            "Il suo look abituale da studente universitario ribelle, costruito con cura per sembrare "
            "totalmente incurante. Un top nero strappato e consumato ai bordi, jeans neri a vita bassa "
            "completamente distrutti, strappi profondi sulle cosce e alle ginocchia. Sopra, il pezzo "
            "centrale: un ampio mantello bianco latte con cappuccio profondissimo, tessuto di origine "
            "sconosciuta che non si macchia mai e non trattiene polvere o odori. Le Dr. Martens nere, "
            "mai allacciate, consumate da anni. Agli orecchi una fila di piercing in argento antico. "
            "La pelle e innaturalmente perfetta. I tatuaggi tribali antichi sul collo e sulle braccia "
            "sembrano spostarsi leggermente se osservati di lato. Il suo odore e gelido: ozono, brina, "
            "neve fresca. Quando abbassa il cappuccio, il mohawk bianco neve e i capelli rasati sui lati "
            "rendono immediatamente chiaro che non e un semplice studente."
        ),
    })(),

    # ── UT BERG ───────────────────────────────────────────────────────────────
    '_NYtBzeKNkm3pedHMnYaka': {
        'Firstborn Berserker Garb': (
            "Una flanella oversize a quadri rossi e neri, indossata aperta su una canottiera di cotone "
            "grezzo che non esiste in taglia sufficientemente grande per lui e che quindi e perennemente "
            "tesa al limite. Pantaloni da lavoro in canvas indistruttibile, il tessuto indurito da anni "
            "di uso, sporco di terra e resina di pino nella versione da foresta, pulito ma stropicciato "
            "nella versione da Villa. Stivali di cuoio su misura, l'unica concessione moderna, perche "
            "nessun calzolaio standard produce il numero necessario. Pesanti anelli di ferro grezzo alle "
            "braccia, portati con la stessa naturalezza con cui altri portano un orologio. Nessun capo "
            "sotto la vita piu elaborato del necessario. Nessuna giacca: Ut e immune al freddo. Quando "
            "e tempo di caccia o di combattimento, la flanella va via e rimane solo la canottiera, con "
            "le rune di guerra tracciate in cenere sulle spalle e sul collo."
        ),
    },

    # ── NIXARA BLOODMOON ─────────────────────────────────────────────────────
    '_fmzBDjDn3Gnq2hXKy7tY6': {
        'Dragonblade Matriarch Battle Dress': (
            "L'abito da battaglia della Luna Bianca, tramandato dalla tradizione della Fede di Fenris e "
            "indossato da Nixara nelle cerimonie e nelle cacce rituali. Pantaloni aderenti in pelle "
            "conciata a mano color antracite, infilati in stivali alti fino al ginocchio con fibbie in "
            "argento. Corpetto strutturato in cuoio lavorato con rune di protezione incise sul petto e "
            "sulle spalle, lascia le braccia libere per il movimento. Una lunga gonna asimmetrica in "
            "tessuto scuro da guerra, aperta sulla gamba destra per la mobilita, scende dietro come un "
            "mantello corto. I capelli biondi sono raccolti in trecce strette e fermati in cima alla "
            "testa. Agli avambracci, bracciali in argento con le rune degli Antenati. L'odore di Nixara "
            "era lavanda selvatica e luna piena, e in questa tenuta quell'odore si mescolava con l'odore "
            "del cuoio antico e del legno di yew. Non indossava gioielli salvo l'anello con il sigillo "
            "dei Bloodmoon, ereditato da suo padre Wulfnic."
        ),
    },

    # ── MARCUS THORNFIELD ─────────────────────────────────────────────────────
    '_PCC1PLfcGrdw2VfMnhVcL': {
        'DCC Heavy Security Tactical': (
            "L'equipaggiamento tattico DCC pesante, una versione potenziata di quello che indossa Kaladin "
            "con l'aggiunta di protezioni balistiche rinforzate su spalle e avambracci. Tuta da combattimento "
            "nera monomateriale, plate carrier ad alto profilo con piastre ceramiche, ginocchiere integrate. "
            "Stivali da assalto pesanti con puntale rinforzato. Non porta mai meno di due sidearm, una "
            "olstered alla coscia destra e una sotto l'ascella sinistra. Il casco tattico a guscio pieno "
            "rimane spesso agganciato alla cintura piuttosto che in testa: Marcus preferisce sentire l'aria "
            "intorno a se. Come Kaladin porta il crest DCC sulla spalla, ma la sua patch di unita e tolta "
            "da anni. La mutazione Gamma-7 e visibile quando e sotto pressione: il pelo del collo si "
            "ispidisce, gli occhi scivolano verso il rosso metallico. In questa tenuta nessuno a Villa "
            "Douglas fa domande che non vuole sentire rispondere."
        ),
    },

    # ── MAGNUS DOUGLAS III ────────────────────────────────────────────────────
    '_jeJTbxLcrYWXNWYPDx4ph': {
        'Cancelleria & Alta Finanza': (
            "Un completo sartoriale su misura in lana italiana grigio ardesia, taglio inglese tradizionale "
            "con le spalle strutturate e le giacche abbottonate fino all'ultimo bottone. Camicia bianca "
            "con colletto rigido e gemelli in argento con il sigillo di Casa Douglas, la stessa incisione "
            "del sigillo usata dal 1666. Cravatta in seta blu notte, nodo Windsor, mai allentata. "
            "Scarpe Oxford in cuoio nero lucidato ogni mattina. Capelli bianchi argentati, tagliati "
            "corti ai lati e piu lunghi in cima, pettinati all'indietro con la precisione di chi ha "
            "imparato a presentarsi in una corte inglese del XVII secolo. Nessun orologio moderno: "
            "porta un orologio da tasca in argento, meccanico, regalo di Cornelius nel 1856. Non usa "
            "telefoni in pubblico. Il suo unico accessorio informale e il sigaro che tiene spento "
            "tra le dita durante le riunioni di consiglio."
        ),
    },

    # ── LORD CORNELIUS DOUGLAS ─────────────────────────────────────────────────
    '_rJKYcCt61hQa8XRamHEdM': {
        'Abito Coloniale Formale DCC': (
            "Lord Cornelius Douglas compare nelle riunioni di famiglia in quello che puo essere "
            "descritto solo come un abito da governatore coloniale del XVII secolo perfettamente "
            "conservato: cappotto lungo in velluto nero con bottoni dorati incisi con lo stemma di "
            "casa Douglas, gilet ricamato in seta avorio, camicia con jabot in pizzo, pantaloni "
            "al ginocchio con calze bianche e fibbie in argento alle scarpe. I capelli neri lunghi "
            "sono raccolti in una coda bassa legata con un nastro nero. Una spada da lato cerimoniale "
            "in argento e ferro pende alla cintura: non e decorativa. Al dito, il sigillo originale "
            "di Casa Douglas, fuso nel 1666, lo stesso che Magnus porta in copia incisa. Porta questa "
            "tenuta non per nostalgia ma perche semplicemente non ha mai visto un motivo valido per "
            "cambiare. L'unica concessione al XXI secolo e che il cappotto e stato rifoderato con "
            "tessuto moderno ignifugo. Nessun altro adattamento."
        ),
    },

    # ── ELIZABETH DUSKWOOD ────────────────────────────────────────────────────
    '_EwPN1te7qtUKYEx4NLgag': {
        'Pack Matriarch / Tradizionale': (
            "Elizabeth si muove in abiti morbidi e di qualita alta, mai ostentati. Vestiti a linea A "
            "in tessuti naturali, lana cashmere o cotone pesante, nei toni del grigio tortora, del "
            "bianco sporco, del blu polvere. Sempre una sciarpa leggera sulle spalle o avvolta al "
            "collo, che porta il suo profumo, lavanda e libri antichi, anche lontano da lei. "
            "Scarpe basse in cuoio morbido, mai tacchi, perche trascorre le mattine accovacciata "
            "nel nido della nursery con i cuccioli. Capelli bianchi con tracce di argento, tagliati "
            "alla nuca, tenuti con una forcina semplice. Nessun gioiello vistoso: solo la fede "
            "nuziale in platino e gli orecchini a bottone in quarzo fumee che porta dalla notte "
            "della sua presentazione nel 1966, quando scelse Magnus di sua spontanea volonta. "
            "La cosa che si nota di piu non e l'abito ma il modo in cui sta ferma: schiena dritta, "
            "mani in grembo, attenzione totale su chi le parla."
        ),
    },
}


def get_char(token, char_id):
    url = f'{BASE_URL}/{char_id}?world_id={WORLD_ID}'
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    })
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode('utf-8'))


def put_char(token, char_id, body):
    url = f'{BASE_URL}/{char_id}?world_id={WORLD_ID}'
    data = json.dumps(body).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='PUT', headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    })
    with urllib.request.urlopen(req) as r:
        return r.status


def run():
    token = get_auth_token()
    print('Token obtained.\n')

    for char_id, outfit_map in OUTFIT_DESCRIPTIONS.items():
        char = get_char(token, char_id)
        name = char.get('display_name', char_id)
        outfits = char.get('outfits', [])

        updated = 0
        for outfit in outfits:
            outfit_name = outfit.get('name', '')
            if outfit_name in outfit_map:
                outfit['description'] = outfit_map[outfit_name]
                updated += 1

        if updated == 0:
            print(f'[SKIP] {name}: no matching outfit names found')
            continue

        status = put_char(token, char_id, {'outfits': outfits})
        print(f'[{status}] {name}: updated {updated}/{len(outfits)} outfits')

        # Verify
        verify = get_char(token, char_id)
        filled = sum(1 for o in verify.get('outfits', []) if len(o.get('description', '')) > 10)
        print(f'       -> Verify: {filled}/{len(verify.get("outfits",[]))} outfits have description')

    print('\nDone.')


if __name__ == '__main__':
    run()
