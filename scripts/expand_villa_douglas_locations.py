import os
import sys
import json
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'
VILLA_DOUGLAS_ID = '_9H2EmzRm92QxBpkmJUR1z'
ENV_COAST_ID = '_jUzC2EQyPTHte1hTYqPt8'
JASPER_CAVERN_ID = '_hcmcH3jKtU82P8Bh11mF1'

# ─────────────────────────────────────────────────────────────────────────────
# 1. Expanded description for Main Villa Douglas
# ─────────────────────────────────────────────────────────────────────────────

VILLA_DOUGLAS_CONTEXT = """La residenza ancestrale dei Douglas al 555 Oak Road, dentro Seven Hills. Casa e fortezza insieme: profondamente amata, costantemente monitorata, completamente soffocante.

Cuoio tattico freddo, cedro, mogano lucidato e un sentore lontano di carne cruda. Luce pesante e opulenta di caminetto. Il peso opprimente del calore corporeo di corpi da licantropo adulto nelle stanze affollate. La ventilazione e progettata per gestire gli odori e isolare l'aggressivita prima che si propaghi. Le porte sono enormi, dimensionate per gli Hybrid Shift. Dal fondo dell'ala est arriva il vapore profumato della Pack Bathhouse termale comune.

Dal retro della proprieta parte il sentiero che sale nei boschi fino al territorio di Wulfnic e alla longhouse. E sterrato, stretto, non segnalato e non asfaltato, e non ne esiste un secondo: chi va dal branco dei Firstborn passa da qui.

<Villa_Douglas>
[LOCATION_ID: Villa Douglas;
TYPE: 400-year-old Ancestral Stronghold, LSE Fortress;
ADDRESS: 555 Oak Road, Seven Hills, Blackwood, CA;
SCENT: Ozone, cedarwood, premium whiskey, leather, smoke, raw meat;
CLAN_SEAL: Antique silver seal atop the stairs depicting a stylized wolf skull with pure amber eyes (burning with silent flames), two intertwined silver lunar crowns, and seven stylized hills engraved with Alpha-blood-filled runes. Glows during full moons to enable telepathic clan communication;
BIOLOGICAL_ARCHITECTURE: Oversized doors/ceilings for Hybrid Shifts (up to 263cm+), reinforced load-bearing structure, DCC advanced pheromone-management ventilation system (isolates Alpha aggression, circulates calming pheromones, neutralizes Heat odors);
SECURITY_GRID: Olfactory biometrics perimeter, DCC drone surveillance, motion sensors, manned PMC teams led by Kaladin and Marcus Thornfield;
PUBLIC_ROOMS: Main Atrium (sports memorabilia), Throne Room (Alpha Throne and Crown), Council Room (obsidian walls, rune-carved oak table), Pack Bathhouse (indoor thermal pools for communal biological bonding and scent-sharing);
PRIVATE_DENS: Erik Sanctuary (armored master suite, tactical command, Nixara's shrine), Malachia East Wing (territorial office, actual den is a bare concrete room with a cot), Noah Gourmet Kitchen (monumental marble kitchen functioning as a mandatory nesting space for stress-baking), Jasper Beta Space (blacked-out tech vault above garage, digital barriers, no scent-marking), Alyssa Sanctuary / Omega Nest (isolated 3rd-floor ex-solarium, hyper-protected, total blackout/acoustic isolation), Guest Wing (fortified for external diplomats);
EXTERIOR_AND_GARAGE: Gardens with three distinct pools (shallow, Olympic, deep mineral for biological recovery), stone BBQ. Garage layout dictates Omegas park deepest/safest, Betas follow, Alphas park heavy SUVs last to physically seal the perimeter]
</Villa_Douglas>

[LOCATION INSTRUCTIONS: Erik Douglas controlla questo luogo in modo assoluto. Il reparto di sicurezza DCC presidia il perimetro e la griglia di sorveglianza di Kaladin e integrata in tutta la struttura: telecamere, biometria, log di ogni porta aperta. Non esiste privacy reale qui dentro, solo privacy concessa.

Il registro emotivo e affetto soffocante, mai crudelta. Ogni intrusione nasce da amore protettivo deformato dal lutto.]"""

# ─────────────────────────────────────────────────────────────────────────────
# 2. Sub-locations specifications
# ─────────────────────────────────────────────────────────────────────────────

NEW_SUB_LOCATIONS = [
    {
        "name": "Villa Douglas: Main Atrium",
        "keys": ["Villa Douglas Main Atrium", "Main Atrium", "Atrio di Villa Douglas", "Atrio Principale", "atrio di Villa Douglas"],
        "secondary_keys": ["atrio", "atrium", "scalata", "sigillo", "trofei", "focolare"],
        "context_description": (
            "Il monumentale atrio di ingresso di Villa Douglas accoglie chiunque varchi il portale blindato con una combinazione "
            "di opulenza aristocratica e orgoglio marziale. I soffitti a cassettoni in legno di cedro raggiungono altezze vertiginose, "
            "progettati per accogliere i licantropi in Hybrid Shift senza costringerli a chinarsi. Lungo le pareti rivestite in mogano scuro "
            "si alternano teche illuminate che espongono cimeli sportivi di famiglia: bastoni da lacrosse in frassino usati nei tornei di "
            "St. Brugge e del SUCC, medaglie universitarie e coppe vinte dai giovani Douglas, affiancate a scudi cerimoniali del Seicento. "
            "In cima allo scalone monumentale in marmo grigio domina il Sigillo Ancestrale in argento antico: un teschio di lupo stilizzato "
            "con occhi di ambra pura, attraversato da due corone lunari e sette colline incise con rune intrise di sangue Alpha, che pulsa "
            "di una fioca luce argentea durante le notti di luna piena. Il pavimento in granito nero lucido sopporta senza scalfirsi il calpestio "
            "di artigli e stivali militari. L'aria odora intensamente di cedro, cuoio trattato e legna resinosa che brucia nel grande camino angolare. "
            "All'ingresso e posizionata la postazione di accoglienza e controllo presidiata dalla sicurezza DCC, dove gli scanner biometrici e "
            "olfattivi verificano ogni presenza prima di consentire l'accesso alle ali interne della tenuta."
        )
    },
    {
        "name": "Villa Douglas: Throne Room",
        "keys": ["Villa Douglas Throne Room", "Throne Room", "Sala del Trono", "Trono del Branco", "trono di Villa Douglas"],
        "secondary_keys": ["trono", "Alpha Throne", "corona", "Seven Hills", "cerimonia", "giudizio"],
        "context_description": (
            "La Sala del Trono rappresenta il fulcro formale e la sacralita politica del branco di Seven Hills. Illuminata dalla luce dorata "
            "e tremula di torce cerimoniali a parete e da un enorme lampadario in ferro battuto, la sala e dominata dall'Alpha Throne: uno scranno "
            "monumentale scolpito in quercia antica nera e rinforzato con piastre di acciaio freddo, sollevato su un podio di tre gradini in pietra "
            "vulcanica. Qui Erik Douglas siede durante le proclamazioni ufficiali, i giudizi territoriali e le cerimonie solenni del clan. Dietro il "
            "trono pendono stendardi in velluto nero e argento con l'araldica secolare dei Douglas. In una nicchia laterale protetta da vetro "
            "runico blindato e custodita la Corona dei Sette Colli, forgiata in argento massiccio e platino. L'atmosfera e carica del peso "
            "schiacciante della dominanza Alpha, un'aura pesante e palpabile che induce istintivamente la maggior parte dei licantropi ad abbassare "
            "lo sguardo e piegare il collo in segno di deferenza. Nessuno entra in questa sala senza un motivo cerimoniale o una convocazione diretta del Prime Alpha."
        )
    },
    {
        "name": "Villa Douglas: Council Room",
        "keys": ["Villa Douglas Council Room", "Council Room", "Sala del Consiglio", "Tavolo del Consiglio", "Council Chamber"],
        "secondary_keys": ["consiglio", "riunione", "tavolo", "ossidiana", "DCC", "Alpha"],
        "context_description": (
            "La Sala del Consiglio e il centro nevralgico della pianificazione strategica, politica e finanziaria della famiglia Douglas e del "
            "contingente DCC. Le pareti sono interamente rivestite in lastre di ossidiana lucida, trattate sia con leghe acustiche isolanti sia con "
            "schermature anti-intercettazione arcane ed elettroniche che bloccano qualsiasi trasmissione non autorizzata. Al centro della stanza "
            "troneggia un immenso tavolo in massello di quercia, le cui venature sono intagliate a mano con antiche rune protettive norrene colmate "
            "di resina trasparente. Intorno al tavolo sono disposte pesanti poltrone in pelle ergonomica ad alto profilo, dimensionate per sostenere "
            "la massa muscolare degli Alpha in caso di tensioni territoriali. Terminali a scomparsa e schermi olografici alle pareti proiettano "
            "mappe della contea di Blackwood, logistica delle spedizioni marittime, indici azionari di Solarton e rilievi tattici delle incursioni "
            "del Guild. L'aria e perennemente condizionata e neutralizzata dai filtri DCC, preservando un rigore freddo in cui le decisioni sul "
            "destino della citta e del branco vengono prese senza concessioni emotive."
        )
    },
    {
        "name": "Villa Douglas: Pack Bathhouse",
        "keys": ["Villa Douglas Pack Bathhouse", "Pack Bathhouse", "Terme del Branco", "Bagno Termale di Villa Douglas", "bagni termali"],
        "secondary_keys": ["terme", "vasca", "vapore", "acque", "East Wing", "scent-sharing"],
        "context_description": (
            "Situata al termine del corridoio inferiore dell'ala est, la Pack Bathhouse e uno spazio termale privato dedicato alla rigenerazione "
            "fisica, alla condivisione biologica degli odori e al rinsaldamento dei legami del branco. Il locale e rivestito in lastre di ardesia "
            "scura e doghe di cedro profumato che resistono all'umidita costante. Grandi vasche in pietra naturale, alimentate da falde termali "
            "ricche di minerali solforosi e magnesio, rilasciano dense volute di vapore balsamico aromatizzato all'eucalipto e agli aghi di pino. "
            "Piccole cascate artificiali massaggiano le fibre muscolari indolenzite dalle battute di caccia o dalle sessioni di addestramento militare. "
            "Qui l'etichetta convenzionale e le barriere formali svaniscono: i membri del branco si immergono insieme nelle calde acque per alleviare "
            "lo stress da combattimento, rilasciare tensioni muscolari e mescolare pacificamente i propri sentori biologici in un'atmosfera di intimo "
            "conforto tribale. Un potente sistema di ventilazione dedicato controlla la densita del vapore, evitando che l'umidita invada il resto della villa."
        )
    },
    {
        "name": "Villa Douglas: Erik's Sanctuary",
        "keys": ["Villa Douglas Erik's Sanctuary", "Erik's Sanctuary", "Stanza di Erik", "Studio di Erik", "Camera Padronale di Erik"],
        "secondary_keys": ["Erik", "master suite", "Nixara", "shrine", "comando", "whiskey"],
        "context_description": (
            "La suite padronale di Erik Douglas al piano superiore e concepita come un santuario corazzato e al contempo una centrale di comando "
            "tattico. Nascosta dietro la calda boiserie in mogano vi e una struttura rinforzata in acciaio balistico in grado di resistere a impatti "
            "esplosivi. La stanza odora potentemente di colonia al sandalo, cuoio invecchiato, tabacco da pipa e whiskey torbato di alta gradazione. "
            "Una scrivania massiccia in noce sostiene monitor criptati collegati in tempo reale alla rete satellitare e ai sensori perimetrali della "
            "DCC. Nella parte piu riservata e silenziosa della suite sorge il sacrario intoccabile dedicato a Nixara Bloodmoon: una mensola in argento "
            "e quercia bianca dove sono custoditi i suoi ritratti a olio, piccoli monili personali e una lampada votiva costantemente accesa. Qui "
            "l'autorita ferrea del Prime Alpha cede il passo al dolore silenzioso e all'amore ossessivo per la compagna perduta e per i figli. Nessun "
            "membro del personale o del branco osa varcare questa soglia senza permesso esplicito."
        )
    },
    {
        "name": "Villa Douglas: Malachia's East Wing & Den",
        "keys": ["Villa Douglas Malachia's East Wing", "Malachia's Den", "Stanza di Malachia", "Ala Est di Malachia", "Ufficio di Malachia"],
        "secondary_keys": ["Malachia", "den", "brandina", "cemento", "Apex", "ufficio"],
        "context_description": (
            "L'ala est al piano terra e il territorio personale di Malachia Douglas, divisa nettamente in due ambienti che riflettono la sua "
            "duplice natura. La parte anteriore e un ufficio territoriale impeccabile, austero e ordinato, arredato con scrivania in metallo e vetro, "
            "schedari blindati e mappe operative del Vanguard Security. Da qui Malachia gestisce le pattuglie di confine, i fascicoli di sicurezza "
            "e i turni di guardia con geometrica freddezza. Oltre una pesante porta blindata in acciaio si accede invece alla sua vera tana privata: "
            "una stanza spoglia in cemento grezzo, priva di tappeti, quadri o qualsiasi forma di lusso domestico. Al centro si trova solo una semplice "
            "brandina militare con coperte pesanti di lana grezza, una sbarra per trazioni fissata al soffitto e pesanti segni di artigli impressi "
            "sui muri perimetrali. L'odore e quello aspro e selvaggio di un predatore dominante: rame, sudore da allenamento, freddo e muschio. E uno "
            "spazio di pura disciplina e istinto primordiale dove ogni vanita e stata estirpata."
        )
    },
    {
        "name": "Villa Douglas: Noah's Gourmet Kitchen",
        "keys": ["Villa Douglas Noah's Gourmet Kitchen", "Noah's Gourmet Kitchen", "Cucina di Noah", "Cucina di Villa Douglas", "cucina monumentale"],
        "secondary_keys": ["Noah", "cucina", "forno", "marmo", "stress-baking", "nesting"],
        "context_description": (
            "Una monumentale cucina professionale al pianterreno, dominata da ampie isole di lavoro in marmo di Carrara, fornelli professionali in "
            "acciaio a sei fuochi, forni tripli e file di pentole in rame appese al soffitto. Una spaziosa cella frigorifera walk-in conserva "
            "costantemente tagli scelti di carne fresca e selvaggina per le esigenze biologiche dei carnivori del branco. Questo spazio e a tutti gli "
            "effetti il territorio e il nido psicologico di Noah Douglas. Quando la pressione familiare, la tensione tra Alpha o il ricordo del "
            "lutto diventano insostenibili, Noah si barrica qui dentro dedicandosi a maratone di preparazione gastronomica e stress-baking che possono "
            "durare un'intera notte. Il profumo di pane appena sfornato, vaniglia, spezie dolci, arrosti caramellati e burro avvolge l'intero piano "
            "terra, attirando fratelli e cugini. Mangiare il cibo preparato da Noah e considerato un atto rituale di coesione e conforto che calma gli "
            "animi anche nei momenti di maggiore crisi."
        )
    },
    {
        "name": "Villa Douglas: Alyssa's Sanctuary / Omega Nest",
        "keys": ["Villa Douglas Alyssa's Sanctuary", "Alyssa's Sanctuary", "Omega Nest", "Nido di Alyssa", "Stanza di Alyssa", "ex-solarium"],
        "secondary_keys": ["Alyssa", "nido", "Omega", "miele", "terzo piano", "solarium"],
        "context_description": (
            "Ricavato in un ex-solarium isolato al terzo piano della villa, il santuario privato di Alyssa e un nido Omega iper-protetto e totalmente "
            "insonorizzato. Grandi vetrate blindate con filtri solari polarizzati e pesanti tende oscuranti permettono di sigillare completamente la luce "
            "naturale o di aprire lo sguardo sulla costa e sulle chiome dei boschi di Seven Hills. All'interno regna una morbidezza accogliente e profumata "
            "di miele selvatico, fiori di luna e lavanda essiccata. Al centro della stanza, sollevato su un soppalco in legno chiaro, si trova il nido: "
            "una distesa di piumini in cashmere, cuscini in velluto e soffici coperte intrecciate con vecchie felpe e indumenti che portano l'odore "
            "rassicurante del gemello Jasper, del padre e dei fratelli. Piccole luci calde a catena creano una penombra intima e rilassante, mentre scaffali "
            "a muro contengono vasetti di essenze botaniche, manuali di erboristeria e quaderni di note mediche. E il rifugio inviolabile in cui Alyssa si "
            "ritira per ritrovare equilibrio biologico ed emotivo al riparo dal soffocante controllo del branco."
        )
    },
    {
        "name": "Villa Douglas: Guest Wing",
        "keys": ["Villa Douglas Guest Wing", "Guest Wing", "Ala Ospiti di Villa Douglas", "Foresteria di Villa Douglas", "ala ospiti"],
        "secondary_keys": ["ospiti", "foresteria", "diplomatici", "ambasciata", "suite ospiti"],
        "context_description": (
            "L'ala riservata agli ospiti sorge nell'estremita nord-occidentale della villa, concepita per accogliere dignitari di altri branchi, "
            "alleati politici ed esponenti del governo o del Guild con standard alberghieri di massimo livello. Ogni suite e rifinita con pavimenti in "
            "parquet pregiato, arredi contemporanei di pregio, ampi bagni in travertino e zone salotto indipendenti. Sotto l'apparente accoglienza di "
            "lusso si cela tuttavia una struttura difensiva rigidamente compartimentata: le pareti perimetrali sono rinforzate, le condotte di "
            "aerazione possiedono valvole di chiusura indipendenti per impedire fughe o intrusioni di gas chimici o feromoni esterni, e le porte sono "
            "collegate a serrature elettroniche controllabili dalla sicurezza centrale. Agli ospiti e garantita ogni comodita e privacy apparente, "
            "mentre i sensori biometrici della DCC monitorano con discrezione ogni spostamento lungo i corridoi comuni."
        )
    },
    {
        "name": "Villa Douglas: Gardens & Pools",
        "keys": ["Villa Douglas Gardens & Pools", "Villa Douglas Gardens", "Giardini di Villa Douglas", "Piscine di Villa Douglas", "parco di Villa Douglas"],
        "secondary_keys": ["giardini", "piscine", "parco", "Olympic", "barbecue", "sentiero", "Wulfnic"],
        "context_description": (
            "Il parco privato di Villa Douglas si estende su diversi ettari terrazzati sul fianco della collina, circondato da una cinta muraria in "
            "pietra e da una fitta barriera di pini marittimi e cipressi secolari. La zona ricreativa e dominata da tre piscine scavate nel granito: "
            "una vasca bassa riscaldata per il relax informale, una piscina olimpionica profonda destinata all'allenamento cardiovascolare dei "
            "licantropi, e una vasca idroterapica profonda alimentata da acque minerali calde, formulata specificamente per accelerare la rigenerazione "
            "tissutale dopo ferite da combattimento. Un grande padiglione con barbecue monumentale in pietra funge da punto di ritrovo per le "
            "grigliate di branco durante i fine settimana. Dal margine posteriore del prato, protetto da una recinzione a sensori discreti, ha inizio "
            "il sentiero sterrato e non segnalato che si inerpica nella boscaglia verso il territorio ancestrale di Wulfnic e la sua antica longhouse."
        )
    },
    {
        "name": "Villa Douglas: Garage & Security Perimeter",
        "keys": ["Villa Douglas Garage & Security Perimeter", "Villa Douglas Garage", "Garage di Villa Douglas", "Perimetro di Villa Douglas", "Checkpoint DCC"],
        "secondary_keys": ["garage", "suv", "veicoli", "Kaladin", "Marcus", "checkpoint", "perimetro"],
        "context_description": (
            "Il complesso sotterraneo dei garage e il varco di sicurezza principale rappresentano la prima linea di difesa fisica della fortezza di "
            "Seven Hills. La disposizione del parcheggio sotterraneo riflette rigidamente la gerarchia biologica e protettiva del branco: i veicoli "
            "degli Omega, inclusa la riconoscibile Volkswagen Maggiolino gialla di Alyssa, sostano nelle baie piu profonde, riparate e vicine agli "
            "ascensori blindati; le vetture dei Beta occupano i settori intermedi; i possenti SUV corazzati e i fuoristrada tattici neri degli Alpha "
            "vengono parcheggiati per ultimi lungo le rampe esterne, sigillando fisicamente le vie di uscita. All'esterno, il cancello principale in "
            "ferro rinforzato e presidiato costantemente da una squadra armata della sicurezza privata DCC sotto il comando di Kaladin Nargathon e "
            "Marcus Thornfield. Barriere carraie a scomparsa, telecamere termiche, postazioni per droni di ronda e lettori di identificazione "
            "olfattiva garantiscono che nessuna persona o veicolo acceda alla proprieta senza essere stato scansionato e autorizzato."
        )
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# 3. Updated description for Jasper's Cavern
# ─────────────────────────────────────────────────────────────────────────────

JASPER_CAVERN_CONTEXT = (
    "Il rifugio tecnologico e la camera privata di Jasper Douglas-Bloodmoon, situata nell'ala ovest di Villa Douglas sopra il blocco dei garage. "
    "Concepito come un vero e proprio caveau informatico oscurato, lo spazio e totalmente isolato dalle intromissioni esterne: tende oscuranti e "
    "pannelli fonoassorbenti sigillano la luce solare californiana, lasciando l'ambiente illuminato solo da strisce ultraviolette e dal bagliore "
    "dei monitor curvi ad alto refresh. A differenza del resto della villa, qui non esiste alcuna marcatura olfattiva territoriale: Jasper "
    "ha installato barriere digitali criptate e filtri ionizzanti dedicati per cancellare ogni traccia ormonale o sentore biologico, sostituendoli "
    "con odore di pioggia fresca, ozono ed energy drink. Dominata dal ronzio costante di server rack overclockati, sintetizzatori audio, una console "
    "di missaggio professionale e cavi di rete intrecciati, questa stanza e il centro di comando invisibile da cui Jasper veglia su Alyssa e "
    "neutralizza i tentativi di sorveglianza familiare."
)


def run():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    print("=== 1. AGGIORNAMENTO VILLA DOUGLAS (MAIN) ===")
    villa_payload = {
        "context_description": VILLA_DOUGLAS_CONTEXT,
        "keys": ["Villa Douglas", "555 Oak Road", "Oak Road", "residenza Douglas", "tenuta Douglas", "Villa dei Douglas"],
        "key_logic": "AND_ANY",
        "case_sensitive": False,
        "whole_words_only": True
    }
    req_v = urllib.request.Request(
        f"{API_BASE}/locations/{VILLA_DOUGLAS_ID}",
        data=json.dumps(villa_payload).encode('utf-8'),
        headers=headers,
        method='PUT'
    )
    with urllib.request.urlopen(req_v) as resp:
        res_v = json.loads(resp.read().decode('utf-8'))
        print(f"  [OK] Villa Douglas aggiornata (status {resp.status}, context_len: {len(res_v.get('context_description', ''))})")

    print("\n=== 2. AGGIORNAMENTO JASPER'S CAVERN ===")
    jasper_payload = {
        "context_description": JASPER_CAVERN_CONTEXT,
        "keys": ["Jasper's Cavern", "Jasper's room", "Jasper's studio", "west wing cavern", "stanza di Jasper"],
        "secondary_keys": ["cavern", "monitors", "DJ", "servers", "studio", "garage", "vault"],
        "key_logic": "AND_ANY",
        "case_sensitive": False,
        "whole_words_only": True
    }
    req_j = urllib.request.Request(
        f"{API_BASE}/locations/{JASPER_CAVERN_ID}",
        data=json.dumps(jasper_payload).encode('utf-8'),
        headers=headers,
        method='PUT'
    )
    with urllib.request.urlopen(req_j) as resp:
        res_j = json.loads(resp.read().decode('utf-8'))
        print(f"  [OK] Jasper's Cavern aggiornato (status {resp.status})")

    print("\n=== 3. CREAZIONE NUOVE SOTTO-LOCATION VILLA DOUGLAS ===")
    created_count = 0
    for loc in NEW_SUB_LOCATIONS:
        payload = {
            "world_id": WORLD_ID,
            "name": loc["name"],
            "environment_id": ENV_COAST_ID,
            "parent_location_id": VILLA_DOUGLAS_ID,
            "keys": loc["keys"],
            "secondary_keys": loc["secondary_keys"],
            "key_logic": "AND_ANY",
            "case_sensitive": False,
            "whole_words_only": True,
            "context_description": loc["context_description"],
            "tags": ["Seven Hills", "Douglas", "Blackwood", "Villa Douglas"]
        }
        try:
            req_l = urllib.request.Request(
                f"{API_BASE}/locations",
                data=json.dumps(payload).encode('utf-8'),
                headers=headers,
                method='POST'
            )
            with urllib.request.urlopen(req_l) as resp:
                res_l = json.loads(resp.read().decode('utf-8'))
                created_count += 1
                print(f"  [OK] Creata sotto-location: {res_l.get('name')} (ID: {res_l.get('id')})")
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode('utf-8')
            print(f"  [ERRORE] Creazione {loc['name']}: HTTP {e.code} - {err_msg}")
        except Exception as e:
            print(f"  [ERRORE] Creazione {loc['name']}: {e}")

    print(f"\nOperazione completata. Sotto-location create: {created_count}/{len(NEW_SUB_LOCATIONS)}")


if __name__ == '__main__':
    run()
