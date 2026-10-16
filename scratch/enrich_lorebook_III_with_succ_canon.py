import json
import pathlib
import re
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

# Load current Lorebook III
lb3_path = ROOT / 'FINAL' / 'Svartulfr_Lorebook_III.json'
lb3 = json.load(lb3_path.open(encoding='utf-8'))

# Load official canon entries from io-succ.uwu.ai
canon_entries = json.load((ROOT / 'scratch' / 'io_succ_canon_entries.json').open(encoding='utf-8'))

def clean_text(t):
    if not t:
        return ""
    # remove em-dashes
    t = t.replace('—', ', ').replace('–', '-')
    # remove markdown bold/italics asterisks
    t = re.sub(r'\*\*([^*]+)\*\*', r'\1', t)
    t = re.sub(r'\*([^*]+)\*', r'\1', t)
    # canon university name
    t = t.replace('Southern Union Monster College', 'Supernatural University of Central California')
    t = t.replace('Solarton University', 'Supernatural University of Central California (SUCC)')
    return t.strip()

# Umbrella keys to remove
BROAD_KEYS = {
    'college', 'student', 'university', 'campus', 'dorm', 'dormitory', 'housing',
    'sports', 'field', 'lecture', 'classroom', 'school', 'faculty', 'class',
    'alpha', 'beta', 'omega', 'werewolf', 'vampire', 'human', 'demihuman',
    'minotaur', 'dragon', 'succubus', 'incubus', 'magic'
}

def clean_keys(keys):
    res = []
    for k in keys:
        if not k:
            continue
        # Split commas if packed
        parts = [p.strip() for p in k.split(',') if p.strip()]
        for p in parts:
            if p.lower() not in BROAD_KEYS and len(p) > 2:
                if p not in res:
                    res.append(p)
    return res if res else [keys[0]] if keys else ["SUCC"]

# Map canon entries into structured dictionary by normalized name
canon_map = {}
for e in canon_entries:
    comm = e.get('comment') or e.get('name') or ''
    # clean emoji and prefixes
    clean_comm = re.sub(r'[^\w\s]', '', comm).strip()
    canon_map[clean_comm.lower()] = e

print(f"Loaded {len(canon_map)} canon entries from io-succ.uwu.ai")

# Types for entries
ENTRY_TYPES = {
    'founding of succ': ('concept', 'Fondazione SUCC (2002)'),
    'supernatural degrees': ('concept', 'Corsi di Laurea e Facoltà SUCC'),
    'rivalry with cums': ('concept', 'Rivalità Accademica SUCC vs CUMS'),
    'campus locations': ('location', 'Campus SUCC - Luoghi e Strutture Principali'),
    'solarton': ('location', 'Cittadina di Solarton, California'),
    'solarton locations': ('location', 'Solarton - Luoghi e Distretti Cittadini'),
    'supernatural university of central california': ('concept', 'Supernatural University of Central California (SUCC)'),
    'anti-vampire legislation': ('concept', 'Legislazione Anti-Vampiri (California)'),
    'california university of magical sciences': ('faction', 'California University of Magical Sciences (CUMS)'),
    'supernatural  human alliance': ('faction', 'Supernatural & Human Alliance (SHA)'),
    'setting  general modern fantasy': ('concept', 'Modern Fantasy - Quadro Istituzionale SUCC'),
    'hex valley': ('location', 'Hex Valley (Sede CUMS)'),
    '1999 nocturnal crisis': ('event', 'Crisi Notturna del 1999 (Solarton)'),
    'succ bulls': ('faction', 'SUCC Bulls (Squadra Football Americano)'),
    'succ bears': ('faction', 'SUCC Bears (Squadra Hockey su Ghiaccio)'),
    'student body population': ('concept', 'Demografia e Popolazione Studentesca SUCC'),
    'frats  sororities': ('faction', 'Fraternite e Confraternite Universitarie (Greek Life)'),
    'sports  succ': ('concept', 'Programmi Sportivi Universitari SUCC'),
    'time/schedules': ('concept', 'Orari Accademici e Routine Quotidiana SUCC'),
    'dorms': ('location', 'Wyrm Dormitories e Alloggi Studenteschi SUCC'),
    'anime club': ('faction', 'SUCC Anime & Manga Club'),
    'the pack': ('faction', 'The Pack (Branco Studentesco Mannaro SUCC)'),
    'bigfeet hiking club': ('faction', 'Bigfeet Hiking Club'),
    'vampire  undead association': ('faction', 'Associazione Vampiri e Non-Morti (VUA)'),
    'grave mistake band': ('faction', 'Grave Mistake (Band Garage-Rock del Campus)'),
    'confraternita beta rho omega bro': ('faction', 'Confraternita Beta Rho Omega (BRO)'),
    'confraternita omega phi the clams': ('faction', 'Confraternita Omega Phi (The Clams)'),
    'modern fantasy contatti esterni dellunderworld': ('concept', 'Contatti Esterni dell\'Underworld (Los Angeles / Solarton)'),
    'ballantine family': ('faction', 'Famiglia Ballantine (Sindicato Vampirico)'),
    'ambrosia': ('item', 'Ambrosia (Sostanza Alchemica Illecita)'),
    'supernatural underworld': ('faction', 'Supernatural Underworld di Los Angeles'),
    'the sinners': ('faction', 'The Sinners (Gang Motociclistica Minotauri)'),
    'distretto commerciale di solarton': ('location', 'Distretto Commerciale di Solarton'),
    'solarton town square  full moon festival': ('event', 'Solarton Town Square & Festival della Luna Piena')
}

enriched_entries = []
enriched_lexicon = []

existing_entries_by_name = {}
for e in lb3.get('entries', []):
    comm = e.get('comment') or e.get('name') or ''
    clean_comm = re.sub(r'[^\w\s]', '', comm).strip().lower()
    existing_entries_by_name[clean_comm] = e

all_keys_to_process = list(ENTRY_TYPES.keys())

for key_norm, (entry_type, display_name) in ENTRY_TYPES.items():
    # Source text: canon or existing
    source_e = canon_map.get(key_norm) or existing_entries_by_name.get(key_norm)
    
    # If not found directly, check partial matches
    if not source_e:
        for cm_k, cm_v in canon_map.items():
            if key_norm in cm_k or cm_k in key_norm:
                source_e = cm_v
                break
    if not source_e:
        for ex_k, ex_v in existing_entries_by_name.items():
            if key_norm in ex_k or ex_k in key_norm:
                source_e = ex_v
                break

    if not source_e:
        continue

    # Content
    raw_content = source_e.get('content', '')
    clean_c = clean_text(raw_content)

    # Keys
    raw_keys = source_e.get('key') or source_e.get('keys') or [display_name]
    keys = clean_keys(raw_keys)

    entry_id = f"succ_lb3_{len(enriched_entries)+1:03d}"

    # Wyvern entry
    entry_obj = {
        "uid": len(enriched_entries),
        "key": keys,
        "keysecondary": source_e.get('keysecondary', []),
        "comment": display_name,
        "content": clean_c,
        "constant": False,
        "selective": len(source_e.get('keysecondary', [])) > 0,
        "selectiveLogic": 0,
        "order": 100,
        "position": 0,
        "disable": False,
        "excludeRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "matchWholeWords": True,
        "preventRecursion": True,
        "enabled": True,
        "priority": 10
    }
    enriched_entries.append(entry_obj)

    # Wyvern Lexicon item
    lexicon_obj = {
        "entry_id": entry_id,
        "name": display_name,
        "type": entry_type,
        "keys": keys,
        "secondary_keys": source_e.get('keysecondary', []),
        "key_logic": "AND_ANY" if len(source_e.get('keysecondary', [])) > 0 else "ANY",
        "content": clean_c,
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    }
    enriched_lexicon.append(lexicon_obj)

print(f"Enriched Lorebook III contains: {len(enriched_entries)} entries and {len(enriched_lexicon)} lexicon items!")

# Update LB3 dict
lb3['name'] = 'Svartúlfr - Lorebook III (SUCC & Underworld)'
lb3['entries'] = enriched_entries
lb3['lexicon'] = enriched_lexicon

# Save back to FINAL
lb3_path.write_text(json.dumps(lb3, indent=2, ensure_ascii=False), encoding='utf-8')
print("Successfully written FINAL/Svartulfr_Lorebook_III.json")

# Deploy to Wyvern API
body = json.dumps({'lexicon': enriched_lexicon, 'entries': enriched_entries}).encode('utf-8')
req_put = urllib.request.Request(
    'https://app.wyvern.chat/api/lorebooks/_9zWTGqYJNJ4BCDMj8gfcD',
    data=body,
    headers=headers,
    method='PUT'
)

try:
    with urllib.request.urlopen(req_put) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"Lorebook III PUT Success! Status: {resp.status}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8')
    print(f"Lorebook III PUT HTTPError: {e.code} - {err_body}")
    # Fallback to sending only lexicon if payload too big
    if e.code == 413 or 'large' in err_body.lower():
        print("Retrying with lexicon array only...")
        body_lex = json.dumps({'lexicon': enriched_lexicon}).encode('utf-8')
        req_put2 = urllib.request.Request(
            'https://app.wyvern.chat/api/lorebooks/_9zWTGqYJNJ4BCDMj8gfcD',
            data=body_lex,
            headers=headers,
            method='PUT'
        )
        with urllib.request.urlopen(req_put2) as resp2:
            print(f"Lorebook III PUT Lexicon-only Success! Status: {resp2.status}")
except Exception as e:
    print(f"Lorebook III Sync Error: {e}")
