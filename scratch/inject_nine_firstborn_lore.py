import json
import pathlib
import urllib.request
import urllib.error
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_PATH = ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json'
OPTIMIZED_PATH = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_Lorebook_I.json'
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
RT_PATH = ROOT / 'scratch' / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
LOREBOOK_ID = '_gwwCxCfQ6PQaLEjAQVpJL'

PACING_DELAY_SECONDS = 2.5
MAX_PAYLOAD_BYTES = 1000000

# 1. New Master Entry: The Nine Firstborn
ENTRY_NINE_FIRSTBORN = {
    "entry_id": "lb1_nine_firstborn_pantheon",
    "name": "I Nove Firstborn di Fenris: La Fratellanza di Zanna & Il Falso Ragnarök",
    "title": "I Nove Firstborn di Fenris: La Fratellanza di Zanna & Il Falso Ragnarök",
    "keys": [
        "Nove Firstborn",
        "Firstborn di Fenris",
        "Nove Fratelli di Zanna",
        "Falso Ragnarök",
        "Firstborn caduti",
        "Sigvaldi",
        "Svartr",
        "Brandr",
        "Kári",
        "Rúnólfr",
        "Garmr"
    ],
    "secondary_keys": [],
    "regex_patterns": [],
    "extensions": {},
    "enabled": True,
    "case_sensitive": False,
    "insertion_order": 100,
    "priority": 10,
    "comment": "La cosmologia dei Nove Fratelli di Zanna consacrati da Fenris nell'antichita",
    "constant": False,
    "position": "before_char",
    "scan_persona": False,
    "whole_words_only": True,
    "key_logic": "AND_ANY",
    "delay": 0,
    "sticky": 0,
    "cooldown": 0,
    "activation_chance": 100,
    "labels": ["lore", "pantheon", "firstborn", "cosmology"],
    "custom_fields": {},
    "related_entries": [],
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public",
    "type": "lore/concept",
    "callback": "",
    "provenance": {"source": "Svartulfr Canon", "captured_at": "2026-10-18T16:20:00.000Z"},
    "content": """Nella cosmologia arcaica di Svartulfr, la stirpe dei licantropi riconosce come capostipiti divini i Nove Fratelli di Zanna (I Nove Firstborn), nove maschi primordiali creati e consacrati direttamente dal Dio Lupo Fenris per guidare e proteggere la specie nelle ere antiche. A differenza dei loro discendenti mortali, nei Nove la natura umana e quella del lupo non sono mai state scisse: il loro nome vichingo di nascita coincide identicamente con il loro nome spirituale eterno.

Dei nove guerrieri originali, solo tre sono sopravvissuti fino all'era moderna:
1. Wulfnic Bloodmoon (Ulfrikr Baleygr): Il Primo Zanna, Re Costruttore, Apex Sovereign e patriarca supremo della Casata Bloodmoon. Incarna l'autorita assoluta di branco, il carisma regale e la dominanza genetica immortale.
2. Ut Berg (Il Titano di Pietra): Il bastione inamovibile e mastro forgiatore. Incarna l'invulnerabilita fisica, la densita titanica e il dominio sul ferro e sulla roccia. Da Ut discende direttamente per linea di sangue il guerriero tradizionale Thorvald (Founding Bloodline).
3. Zefir Hvitskog (Lo Spirito Bianco): Il piu giovane dei tre superstiti, cacciatore silente delle nevi e della tundra nordica. Incarna la velocita cinetica superluminale, la furtivita assoluta e la preveggenza tattica.

I Sei Firstborn Caduti nel Falso Ragnarok:
I restanti sei fratelli di zanna perirono durante la Guerra dei Pantheon (nota nel folklore licantropico come Il Falso Ragnarok), una gigantesca guerra cosmica dell'antichita in cui divinita rivali e pantheon ostili tentarono di sterminare la progenie di Fenris. Per consentire a Wulfnic, Ut e Zefir di portare in salvo i superstiti della specie e fondare le stirpi eterne, i sei scelsero una leggendaria ultima resistenza sacrificale:
4. Sigvaldi Blodox (L'AsciadiSangue): Primo stratega e berserker supremo di Fenris, maestro della furia marziale e del comando implacabile in prima linea. Dalla sua progenie guerriera discende per linea diretta la stirpe di Harald Sigurdsson, Jarl delle alture e detentore del sangue Founding Bloodline.
5. Svartr Solulf (Il Lupo del Sole Nero): Figlio mistico di Sol (la divinita femminile del Sole) e del lupo primordiale Skoll (gemello solare di Hati). Controparte maschile dell'eclissi e polarita complementare di Hvit (la Lupa Bianca lunare). La sua essenza solare nera si reincarna nei lupi prescelti di ogni era, come avvenuto per Jasper Svartr Douglas-Bloodmoon alla sua Presentazione.
6. Brandr Eldstigi (Il Passo di Fuoco): Incarnazione della furia vulcanica, del magma primordiale e della tempesta termica. Difese i valichi montani incandescenti contro le schiere divine nemiche fino a consumare la propria essenza vitale in un'esplosione che sigillo le faglie d'accesso.
7. Kari Hafgufa (Il Gorgo degli Abissi): Signore delle tempeste oceaniche, dei fiordi profondi e dei gorghi marini primordiali. Trascino le flotte divine nemiche nelle profondita dell'abisso polare, annegandole nelle correnti gelide al costo della propria vita.
8. Runolfr Volundr (Lo Sciamano delle Rune): Custode originario del Seidr, della vista spirituale sciamanica e dell'incisione delle Rune Madri con cui Fenris consacro la realta. Si sacrifico incidendo sul proprio cuore le rune di occultamento cosmico che resero invisibili i sopravvissuti agli occhi degli dei nemici.
9. Garmr Kjalki (Mascelladiferro / Il Divoratore): Incarnazione della fame cosmica inesausta di Fenris e carnefice delle avanguardie nemiche. Frantumo le corazze divine e le armi incantate dei rivali con le sue mascelle titaniche fino all'ultimo respiro nella piana della battaglia finale.

L'eredita di questi nove guerrieri costituisce il fondamento mistico di ogni legge, rito di Presentazione e diritto di sangue tra i licantropi della Founding Bloodline."""
}

# 2. New Dedicated Entry: LSE Folklore & Ancestral Religion
ENTRY_LSE_FOLKLORE = {
    "entry_id": "lb1_lse_folklore_ancestral_religion",
    "name": "LSE Folklore & Tradizione Religiosa: Il Culto di Fenris, dei Nove Fratelli e delle Due Luci",
    "title": "LSE Folklore & Tradizione Religiosa: Il Culto di Fenris, dei Nove Fratelli e delle Due Luci",
    "keys": [
        "Culto Primordiale",
        "Religione dei Licantropi",
        "Folklore LSE",
        "Fede di Fenris",
        "Culto di Hvit e Svartr",
        "Miti dei Licantropi",
        "Tradizione Spirituale LSE",
        "Falso Ragnarök culto"
    ],
    "secondary_keys": [],
    "regex_patterns": [],
    "extensions": {},
    "enabled": True,
    "case_sensitive": False,
    "insertion_order": 100,
    "priority": 10,
    "comment": "La dimensione spirituale, rituale e folkloristica dell'LSE",
    "constant": False,
    "position": "before_char",
    "scan_persona": False,
    "whole_words_only": True,
    "key_logic": "AND_ANY",
    "delay": 0,
    "sticky": 0,
    "cooldown": 0,
    "activation_chance": 100,
    "labels": ["lore", "folklore", "religion", "rituals", "lse"],
    "custom_fields": {},
    "related_entries": [],
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public",
    "type": "lore/concept",
    "callback": "",
    "provenance": {"source": "Svartulfr Canon", "captured_at": "2026-10-18T16:20:00.000Z"},
    "content": """La dimensione religiosa e folkloristica dell'universo lupino (Lupine Social Environment, LSE) non si fonda su dogmi scritti o templi formali, ma sulla venerazione diretta degli antenati primordiali, sui cicli cosmici celesti e sui giuramenti suggellati nel sangue. Anche nei branchi moderni e corporativi come la Casata Douglas, i miti ancestrali permeano l'identita profonda dei lupi, manifestandosi nei rituali di passaggio, nelle rune corporali e nella disciplina di branco.

I Tre Grandi Culti del Folklore LSE:

1. Il Culto del Padre Lupo (Fenris) e il Giuramento di Zanna:
Fenris e venerato come l'Origine primordiale, la forza cosmica che ha benedetto e plasmato i Nove Firstborn. La sua venerazione non richiede preghiere sottomesse, ma prove di forza, dignita e fedelta al branco: mostrarsi deboli o rinnegare il proprio sangue e considerato l'unico vero sacrilegio. Ai tre sopravvissuti (Wulfnic, Ut, Zefir) e tributata una riverenza quasi divina da ogni lupo tradizionale, che si inchina al loro cospetto riconoscendo in loro la presenza vivente del Dio Lupo.

2. Il Canone dei Sei Caduti e il Brindisi degli Eroi (Sons of the Fall):
I sei fratelli di zanna caduti nel Falso Ragnarok (Sigvaldi, Svartr, Brandr, Kari, Runolfr, Garmr) sono invocati come spiriti tutelari nelle notti di vigilia di battaglia o durante le cacce rituali. Durante i banchetti solenni di plenilunio, ogni Alpha alza il corno consacrato nel rito del Minni, versando a terra sei gocce di idromele o vino scuro in memoria del loro sacrificio. Sigvaldi e invocato per il coraggio guerriero, Runolfr per la saggezza nelle scelte oscure, Kari prima di traversate marittime, Brandr per la tempratura del fuoco, Garmr per sconfiggere nemici soverchianti, e Svartr per l'equilibrio tra ombra e luce.

3. Il Culto delle Due Luci Celesti (Mani/Hvit & Sol/Svartr):
Il folklore LSE concepisce il mondo come una danza eterna tra due forze polari e complementari:
- La Luce Bianca Lunare (Hvit): Discendente da Mani e dalla prima compagna di Wulfnic, incarna l'intuito, la purezza primordiale, la guarigione animica e la sacralita della maternita di branco. Le femmine che manifestano la natura di White Moon (come Nixara ed Alyssa) sono considerate sacre messaggere di Hvit.
- L'Ombra Solare Nera (Svartr): Discendente dall'unione di Sol con Skoll, incarna la fiamma celata nell'ombra, l'astuzia tecnologica o tattica, la capacita di muoversi tra due mondi e la protezione feroce del compagno gemellare. L'assunzione del nome Svartr (come per Jasper) sancisce la restaurazione dell'equilibrio tra Luna e Sole nel branco.

La Frattura Culturale: Boschi Ancestrali vs Metropoli Corporative:
Nel ventunesimo secolo, la pratica religiosa LSE si divide in due grandi anime:
- I Tradizionalisti delle Terre Alte (seguaci di Harald Sigurdsson e Thorvald): Rifiutano la tecnologia moderna, praticano le cacce di sangue sotto le lune d'inverno, incidono le rune col ferro rovente e considerano i Nove Firstborn la sola vera legge terrena, rispondendo unicamente a Wulfnic.
- I Riformisti Urbani (Casata Douglas): Hanno tradotto i precetti dei Nove Firstborn in leggi commerciali, disciplina gerarchica aziendale (DCC) e protocolli d'onore, conservando intatti i rituali della Presentazione (Wolf Name) e della Birth-Rune come pilastri identitari insostituibili."""
}

def main():
    print(f"[1/4] Loading {FINAL_PATH}...")
    with open(FINAL_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    entries = data.get('entries', [])
    lexicon = data.get('lexicon', [])

    # Check and update Species: God & Primordial (entry 168)
    for e in entries:
        t = e.get('title') or e.get('name') or ''
        if t == 'Species: God & Primordial':
            print("  Updating Species: God & Primordial...")
            e['content'] = """Species Overview: God & Primordial

Ancient immortal entities whose existence predates modern history, including the Nine Firstborn of the Svartulfr pantheon and primordial nature spirits.

The Nine Firstborn of Fenris:
The nine primordial werewolves created directly by the Wolf God Fenris in ancient times. They are divided into:
- The Three Living Survivors: Wulfnic Bloodmoon (The First Fang, Builder King, Apex Sovereign), Ut Berg (The Stone Titan, Invulnerability & Master Smith), and Zefir Hvitskog (The White Ghost, Superluminal Hunter).
- The Six Fallen of the False Ragnarok: Sigvaldi Blodox (War & Conquest, ancestor of Harald Sigurdsson), Svartr Solulf (Solar Eclipse, son of Sol and Skoll, counterpart to Hvit), Brandr Eldstigi (Primal Volcanic Fire), Kari Hafgufa (Abyssal Ocean & Tempests), Runolfr Volundr (Seidr & Mother-Runes), and Garmr Kjalki (Cosmic Devouring & Executioner).

Physiology & Divine Blood:
Beings of immense sovereign presence, unaging biological invulnerability, and spiritual dominance. Their blood carries divine resonance (Divine Blood for surviving Firstborn, Founding Bloodline for their immediate scions), passing legendary traits and apex physical density to their true heirs. They are completely immune to mortal diseases, age cessation, and conventional weaponry, vulnerable only to ancient primordial relics or divine cataclysms."""

        elif t == 'Lycanthrope Naming Tradition':
            print("  Updating Lycanthrope Naming Tradition...")
            e['content'] = """Nella cultura dei licantropi norreni della Founding Bloodline e dell'antico lignaggio Svartulfr, ogni individuo riceve alla nascita un nome civile. All'eta di tredici anni, durante il sacro rito della Presentazione in cui si manifesta per la prima volta la bestia interiore, il licantropo scopre e dichiara il nome del proprio lupo spirituale. Per legge ancestrale del branco, questo nome viene assunto come secondo nome ufficiale e formale dell'individuo, sancendo la transizione verso l'eta adulta e l'accettazione del proprio spirito ferino.

I Pilastri Mitologici e Dinastici della Tradizione:
1. Il Mito Primordiale di Hvit e la Prima Compagna di Wulfnic: La prima Hvit delle origini nacque dall'unione mistica tra Mani (la divinita maschile della Luna) e Hati Hrodvitnisson (che nella cosmologia di Svartulfr e la sacra lupa primordiale). Questa prima lupa bianca divenne la prima compagna eterna di Wulfnic Bloodmoon, il capostipite creato da Fenris. Alla sua morte, la sua essenza lunare e il suo spirito protettivo si legano indissolubilmente al sangue Bloodmoon, reincarnandosi in ogni generazione attraverso le White Moon (Nixara ed Alyssa).
2. Il Vincolo delle White Moon: Tutte le reincarnazioni della lupa primordiale portano immancabilmente per legge sacra il nome del lupo originale: Hvit (la Bianca). Per questo motivo sia Nixara sia sua figlia Alyssa portano Hvit come secondo nome formale (Nixara Hvit Bloodmoon e Alyssa Hvit Douglas Bloodmoon), e per questo l'antico patriarca Wulfnic vede in Alyssa il riflesso vivente e benedetto della sua compagna perduta.
3. La Stirpe Solare di Svartr e Skoll: In simmetria perfetta e opposta ad Hvit, la controparte maschile dell'eclissi solare discende dall'unione tra Sol (la divinita femminile del Sole) e il lupo Skoll. Uno dei Nove Firstborn consacrati da Fenris prese il nome di Svartr Solulf. Se Hvit incarna la pura luce lunare (Bianco), la progenie e la reincarnazione di Svartr incarna il Lupo Nero e l'Ombra Solare. Da questo archetipo millenario, Jasper Douglas assume alla sua Presentazione il nome di lupo Svartr (Jasper Svartr Douglas Bloodmoon), creando con la gemella Alyssa Hvit la perfetta polarita cosmica del branco.
4. I Secondi Nomi Nobiliari Inglesi vs Wolf Names Norreni: Nella Casa Douglas, a causa della tradizione nobiliare mercantile britannica stabilita dal patriarca Magnus dopo il 1666, ai primogeniti vengono spesso assegnati secondi nomi civili dell'aristocrazia inglese (come Cornelius per Erik e Dominic per Logan). Questi coesistono con i loro veri Wolf Names assunti alla Presentazione (Erik Ulfr e Logan Jarn).
5. I Licantropi Militari (Nargathon e Project Blackwolf): I lupi cresciuti ed addestrati all'interno delle gerarchie militari e dei battaglioni d'assalto (come Kaladin Nargathon e Marcus Thornfield) sostituiscono il nome lupino tradizionale con codici tattici e call-sign operativi (Blackwolf, Iron).
6. Distinzione Sacra tra Licantropi e Demi-Umani (Kemonomimi): La Presentazione, i Wolf Names e le Birth-Runes appartengono esclusivamente ai veri Licantropi dotati di facolta mutaforma (Shift). I Demi-Umani Lupo (come Finnegan Novak) sono Kemonomimi privi della capacita biologica di mutare in forma ibrida o quadrupede.
7. I Nove Firstblood: I nove guerrieri originali creati direttamente da Fenris (Wulfnic, Ut, Zefir, Sigvaldi, Svartr, Brandr, Kari, Runolfr, Garmr) non possiedono un secondo nome separato. Essendo entita ancestrali unificate in cui uomo e lupo non sono mai stati divisi, il loro nome da lupo coincide identicamente con il loro nome vichingo di nascita.
8. I Giovani Pre-Presentazione: I cuccioli e i giovani licantropi che non hanno ancora compiuto tredici anni o non hanno ancora superato la cerimonia della Presentazione (come Edric Douglas) non possiedono un nome da lupo e usano unicamente il nome di battesimo civile."""

    # Add the 2 new master entries if not present
    existing_titles = {e.get('title') or e.get('name') for e in entries}
    if ENTRY_NINE_FIRSTBORN['title'] not in existing_titles:
        entries.append(ENTRY_NINE_FIRSTBORN)
        print(f"  + Added: {ENTRY_NINE_FIRSTBORN['title']}")
    if ENTRY_LSE_FOLKLORE['title'] not in existing_titles:
        entries.append(ENTRY_LSE_FOLKLORE)
        print(f"  + Added: {ENTRY_LSE_FOLKLORE['title']}")

    # Synchronize lexicon array
    data['entries'] = entries
    data['lexicon'] = entries
    print(f"Total entries in Lorebook I now: {len(entries)}")

    print(f"[2/4] Saving to {FINAL_PATH} and {OPTIMIZED_PATH}...")
    with open(FINAL_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with open(OPTIMIZED_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

    print(f"[3/4] Refreshing auth token...")
    rt = RT_PATH.read_text(encoding='utf-8').strip()
    body = json.dumps({'grant_type': 'refresh_token', 'refresh_token': rt}).encode('utf-8')
    req = urllib.request.Request(
        f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}',
        data=body,
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        token = res['id_token']
        WT_PATH.write_text(token, encoding='utf-8')

    print(f"[4/4] Deploying Lorebook I to Wyvern API (PUT /api/lorebooks/{LOREBOOK_ID})...")
    base_payload = {
        'name': data.get('name', 'Svartúlfr - Lorebook I'),
        'description': data.get('description', ''),
        'visibility': data.get('visibility', 'private'),
        'rating': data.get('rating', 'explicit'),
        'scan_depth': data.get('scan_depth', 5),
        'token_budget': data.get('token_budget', 5000),
        'recursive_scanning': data.get('recursive_scanning', True),
    }

    payload_both = dict(base_payload)
    payload_both['entries'] = data['entries']
    payload_both['lexicon'] = data['lexicon']
    bytes_both = json.dumps(payload_both, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

    payload_lex = dict(base_payload)
    payload_lex['lexicon'] = data['lexicon']
    bytes_lex = json.dumps(payload_lex, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

    if len(bytes_both) < MAX_PAYLOAD_BYTES:
        chosen_bytes = bytes_both
        mode = "dual_array"
    else:
        chosen_bytes = bytes_lex
        mode = "native_lexicon"

    print(f"  Mode: {mode} | Size: {len(chosen_bytes):,} bytes | Entries: {len(data['entries'])}")

    put_req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{LOREBOOK_ID}',
        data=chosen_bytes,
        method='PUT',
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )

    with urllib.request.urlopen(put_req, timeout=60) as resp:
        print(f"  Deploy Status: HTTP {resp.status}")

    time.sleep(PACING_DELAY_SECONDS)
    get_req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{LOREBOOK_ID}',
        headers={
            'Authorization': f'Bearer {token}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )
    with urllib.request.urlopen(get_req, timeout=30) as resp:
        vdata = json.loads(resp.read().decode('utf-8'))
        rem_entries = len(vdata.get('lexicon', [])) or len(vdata.get('entries', []))
        print(f"  Verification GET: HTTP {resp.status} | Remote entries count: {rem_entries}")
        assert rem_entries == len(entries), f"Expected {len(entries)}, got {rem_entries}"
        print("  Lorebook I deployment verified successfully!")

if __name__ == '__main__':
    main()
