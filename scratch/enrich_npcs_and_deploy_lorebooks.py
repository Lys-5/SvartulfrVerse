import json
import pathlib
import re
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'
FINAL_DIR = ROOT / 'FINAL'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}

def api_put(endpoint: str, payload: dict):
    url = f"{API_BASE}{endpoint}"
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read().decode('utf-8')
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='ignore')
        print(f"HTTP {e.code} on PUT {endpoint}: {err_body[:300]}")
        return e.code, {'error': err_body}

# -------------------------------------------------------------
# 1. Build Avatar Resolution Map
# -------------------------------------------------------------
print("=== 1. BUILDING AVATAR MAP ===")
following = json.load(open(ROOT / 'ARCHIVIO/janitor_sources/janitor_following_canon_characters.json', encoding='utf-8')).get('characters', [])
favs = json.load(open(ROOT / 'ARCHIVIO/janitor_sources/janitor_favorites_candidates.json', encoding='utf-8')).get('characters', [])

avatar_map = {}

# Seed known high-priority avatars
avatar_map['marek'] = 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c1fc8935-46c7-4534-d0b4-2f27acae3200/public'
avatar_map['russ'] = 'https://ella.janitorai.com/bot-avatars/9yrobVTbiGDRLHlS6GtIz.webp'
avatar_map['russell russ'] = 'https://ella.janitorai.com/bot-avatars/9yrobVTbiGDRLHlS6GtIz.webp'
avatar_map['neon purr'] = 'https://ella.janitorai.com/bot-avatars/k67CEqNxObTdZSrsJvV7k.webp'

for c in following + favs:
    nm = c.get('name', '').strip()
    av = c.get('avatar', '').strip()
    if nm and av:
        url = f'https://ella.janitorai.com/bot-avatars/{av}'
        avatar_map[nm.lower()] = url
        clean = re.sub(r'\[.*?\]|\(.*?\)|\|.*', '', nm).strip().lower()
        if clean:
            avatar_map[clean] = url
        parts = clean.split()
        if len(parts) >= 2:
            first_last = f"{parts[0]} {parts[-1]}"
            avatar_map[first_last] = url

# Also check scratch/backup_final_preimport
for p in ROOT.glob('scratch/backup_final_preimport/*.json'):
    try:
        data = json.load(open(p, encoding='utf-8'))
        for e in data.get('entries', data.get('lexicon', [])):
            nm = e.get('name')
            av = e.get('avatar')
            if nm and av and '98e2d06d' not in av and av.startswith('http'):
                avatar_map[nm.strip().lower()] = av
    except Exception:
        pass

print(f"Indexed {len(avatar_map)} name->avatar mappings.")

# -------------------------------------------------------------
# 2. Helper to parse NPC names and construct regex & npc_info
# -------------------------------------------------------------
TITLES = {'Major', 'Captain', 'Coach', 'Assistant Coach', 'Dean', 'Chief', 'Warchief', 'Doctor', 'Dr.', 'Professor', 'Prof.'}

def parse_npc(name: str, keys: list, content: str):
    clean_name = name.strip()
    
    # Check titles
    title = ""
    for t in TITLES:
        if clean_name.startswith(t + " "):
            title = t
            clean_name = clean_name[len(t)+1:].strip()
            break
            
    # Extract nickname inside quotes e.g. Daniel "Danny" Boone
    nicknames = []
    nick_match = re.findall(r'["\']([^"\']+)["\']', clean_name)
    if nick_match:
        nicknames.extend(nick_match)
        clean_name = re.sub(r'["\'][^"\']+["\']', '', clean_name)
        clean_name = re.sub(r'\s+', ' ', clean_name).strip()
        
    parts = clean_name.split()
    if len(parts) == 1:
        first = parts[0]
        last = ""
    elif len(parts) == 2:
        first = parts[0]
        last = parts[1]
    else:
        first = parts[0]
        last = parts[-1]
        
    # Check content for ALIASES:
    alias_match = re.search(r'ALIASES:\s*([^;\]\n]+)', content)
    if alias_match:
        for a in alias_match.group(1).split(','):
            a_clean = a.strip()
            if a_clean and a_clean not in nicknames and len(a_clean) > 1:
                nicknames.append(a_clean)
                
    # Also add distinct keys that look like nicknames
    for k in keys:
        k_str = k.strip()
        if k_str and k_str not in nicknames and k_str not in [first, last, name] and len(k_str) > 2:
            if not any(k_str.lower() == broad for broad in ['solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'omega', 'alpha', 'beta']):
                nicknames.append(k_str)
                
    # Build unique search patterns for regex
    patterns = []
    # 1. Exact full name
    patterns.append(name.strip())
    # 2. Title + First or Title + Last
    if title:
        patterns.append(f"{title} {first}")
        if last:
            patterns.append(f"{title} {last}")
            patterns.append(f"{title} {first} {last}")
    # 3. Clean full name if different
    if clean_name and clean_name != name.strip():
        patterns.append(clean_name)
    # 4. First + Last
    if first and last and f"{first} {last}" not in patterns:
        patterns.append(f"{first} {last}")
    # 5. Nickname + Last
    for nick in nicknames[:2]:
        if last:
            patterns.append(f"{nick} {last}")
        patterns.append(nick)
    # 6. First name alone (only if unique/length >= 3)
    if len(first) >= 3 and first not in patterns:
        patterns.append(first)
        
    # Deduplicate while preserving order
    seen = set()
    final_patterns = []
    for p in patterns:
        p_clean = p.strip()
        if p_clean and p_clean.lower() not in seen:
            seen.add(p_clean.lower())
            final_patterns.append(re.escape(p_clean))
            
    # Compile multiline regex: (?:^|\n)\s*(?:Pat1|Pat2|...)\s*:
    regex_str = r"(?:^|\n)\s*(?:" + "|".join(final_patterns) + r")\s*:"
    
    npc_info = {
        "first_name": first,
        "last_name": last,
        "nicknames": nicknames,
        "titles": [title] if title else []
    }
    
    return regex_str, npc_info

# -------------------------------------------------------------
# 3. Process NPC Primary and Secondary Lorebooks
# -------------------------------------------------------------
LOREBOOKS = [
    ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json'),
    ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json'),
]

for lb_id, fname in LOREBOOKS:
    fpath = FINAL_DIR / fname
    lb_data = json.loads(fpath.read_text(encoding='utf-8'))
    entries = lb_data.get('entries', [])
    print(f"\nProcessing {fname} ({len(entries)} entries)...")
    
    updated_count = 0
    avatar_updated_count = 0
    
    for entry in entries:
        nm = entry.get('name', '').strip()
        keys = entry.get('keys', [])
        content = entry.get('content', '')
        current_avatar = entry.get('avatar', '')
        
        # Resolve avatar if missing or placeholder
        if not current_avatar or '98e2d06d' in current_avatar:
            resolved = avatar_map.get(nm.lower())
            if not resolved:
                clean = re.sub(r'\[.*?\]|\(.*?\)|\|.*', '', nm).strip().lower()
                resolved = avatar_map.get(clean)
            if not resolved:
                for k in keys:
                    if k.strip().lower() in avatar_map:
                        resolved = avatar_map[k.strip().lower()]
                        break
            if resolved:
                entry['avatar'] = resolved
                avatar_updated_count += 1
                
        # Build regex & npc_info
        regex_str, npc_info = parse_npc(nm, keys, content)
        entry['type'] = 'npc'
        entry['custom_avatar_regex'] = True
        entry['avatar_activation_regex'] = regex_str
        entry['lines_parsed'] = 1
        entry['npc_info'] = npc_info
        updated_count += 1
        
    print(f"  -> Generated regex & npc_info for {updated_count} entries.")
    print(f"  -> Resolved real avatars for {avatar_updated_count} entries.")
    
    # Save back to FINAL file
    lb_data['entries'] = entries
    lb_data['lexicon'] = entries
    fpath.write_text(json.dumps(lb_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"  -> Saved {fname} locally.")
    
    # Deploy to Wyvern API with full top-level metadata
    payload = {
        'name': lb_data.get('name'),
        'description': lb_data.get('description'),
        'visibility': 'private',
        'rating': 'explicit',
        'scan_depth': lb_data.get('scan_depth', 5),
        'token_budget': lb_data.get('token_budget', 5000),
        'recursive_scanning': lb_data.get('recursive_scanning', True),
        'entries': entries,
        'lexicon': entries
    }
    
    st, res = api_put(f"/lorebooks/{lb_id}", payload)
    print(f"PUT /api/lorebooks/{lb_id} -> HTTP {st} (entries: {len(entries)})")

# -------------------------------------------------------------
# 4. Update Character Cards (Marek, Russ, Neon Purr)
# -------------------------------------------------------------
print("\n=== 4. UPDATING CHARACTER CARD AVATARS ===")
CARDS_TO_UPDATE = [
    ('_cL86CRDAYABmaBWgdLQNw', 'Marek_card.json', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c1fc8935-46c7-4534-d0b4-2f27acae3200/public'),
    ('_x4F8TKXcU6naKT2CpKdHN', 'Russ_card.json', 'https://ella.janitorai.com/bot-avatars/9yrobVTbiGDRLHlS6GtIz.webp'),
    ('_2EezhhEVdL677DULVdE9h', 'Neon_Purr_card.json', 'https://ella.janitorai.com/bot-avatars/k67CEqNxObTdZSrsJvV7k.webp'),
]

for cid, fname, av_url in CARDS_TO_UPDATE:
    cpath = FINAL_DIR / fname
    card = json.loads(cpath.read_text(encoding='utf-8'))
    card['avatar'] = av_url
    cpath.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
    
    st, res = api_put(f"/characters/{cid}", {"avatar": av_url})
    print(f"PUT /api/characters/{cid} ({fname}) avatar -> HTTP {st} | {av_url}")

# -------------------------------------------------------------
# 5. Update Master Scenario with NPC Formatting Instruction
# -------------------------------------------------------------
print("\n=== 5. UPDATING MASTER SCENARIO ===")
SCENARIO_ID = 'char_scenario_1DC43ggb6mB8YLJDJKrU4'
scen_path = FINAL_DIR / 'Svartulfr_Master_Scenario.json'
scen_data = json.loads(scen_path.read_text(encoding='utf-8'))

npc_instruction = (
    "\n\n[NPC FORMATTING DISCIPLINE]: When secondary NPCs or background characters speak or take action, "
    "always output their dialogue on a new line prefixed with their exact full name and a colon "
    "(e.g., 'Santiago Herrera: [dialogue/action]'). Never blend NPC dialogue anonymously into narration."
)

if "[NPC FORMATTING DISCIPLINE]" not in scen_data.get('scenario', ''):
    scen_data['scenario'] = scen_data.get('scenario', '') + npc_instruction
    scen_path.write_text(json.dumps(scen_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print("Appended [NPC FORMATTING DISCIPLINE] to local scenario.")

# PUT to Wyvern API
st, res = api_put(f"/character-scenarios/{SCENARIO_ID}", scen_data)
print(f"PUT /api/character-scenarios/{SCENARIO_ID} -> HTTP {st} (Revision: {res.get('revision')})")

print("\n=== ALL NPC METADATA ENRICHMENTS & DEPLOYS COMPLETE ===")
