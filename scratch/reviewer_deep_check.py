import sys
import os
import json
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
SNAPSHOT_PATH = os.path.join(ROOT_DIR, 'scratch', 'world_new_deployed.json')
BASE_URL = 'https://app.wyvern.chat/api'
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

def get_headers():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token = f.read().strip()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

def api_get(endpoint):
    url = f"{BASE_URL}{endpoint}" if endpoint.startswith('/') else f"{BASE_URL}/{endpoint}"
    req = urllib.request.Request(url, headers=get_headers(), method='GET')
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read().decode('utf-8'))

def main():
    print("=== REVIEWER DEEP AUDIT: R3, R4, R5 ===")
    
    # 1. Fetch live environments
    st_e, live_envs = api_get(f'/worlds/environments/world/{WORLD_ID}')
    print(f"Environments fetched: status {st_e}, count: {len(live_envs)}")
    env_by_id = {}
    for e in live_envs:
        eid = e.get('id') or e.get('_id')
        env_by_id[eid] = e
        print(f"  Env: '{e.get('name')}' (ID: {eid}) | Keys: {e.get('keys')[:4]} | Desc len: {len(e.get('description', ''))}")
    
    # Check 7 canonical env names
    expected_envs = [
        "California Coast",
        "SUCC campus",
        "Solarton",
        "Blackwood",
        "Seven Hills",
        "DMHA HQ & Guild District",
        "Voidspace/Otherworld"
    ]
    env_names = [e.get('name') for e in live_envs]
    missing_envs = set(expected_envs) - set(env_names)
    print(f"Missing environments: {missing_envs}")
    assert len(missing_envs) == 0, f"Missing environments: {missing_envs}"

    # 2. Fetch live locations
    st_l, live_locs = api_get(f'/worlds/locations/world/{WORLD_ID}')
    print(f"\nLocations fetched: status {st_l}, count: {len(live_locs)}")
    loc_by_id = {}
    roots = []
    children = []
    orphans = []
    verve = None

    for loc in live_locs:
        lid = loc.get('id') or loc.get('_id')
        loc_by_id[lid] = loc
        if loc.get('name') == 'The Verve':
            verve = loc

    for lid, loc in loc_by_id.items():
        pl = loc.get('parent_location')
        if not pl:
            roots.append(loc)
        else:
            pid = pl.get('id') or pl.get('_id') if isinstance(pl, dict) else pl
            if pid not in loc_by_id:
                orphans.append((loc.get('name'), lid, pid))
            else:
                children.append(loc)

    print(f"Roots: {len(roots)}")
    for r in roots:
        print(f"  Root: '{r.get('name')}' (ID: {r.get('id') or r.get('_id')})")
    print(f"Children (nested): {len(children)}")
    print(f"Orphans: {len(orphans)}")
    if orphans:
        for o in orphans:
            print(f"  ORPHAN: {o}")

    # Check environment references of locations
    invalid_env_locs = []
    for loc in live_locs:
        eid = loc.get('environment') or loc.get('environment_id')
        if isinstance(eid, dict):
            eid = eid.get('id') or eid.get('_id')
        if eid not in env_by_id:
            invalid_env_locs.append((loc.get('name'), eid))
    print(f"Locations with invalid environment reference: {len(invalid_env_locs)}")

    # Check The Verve
    print("\n--- The Verve Deep Check ---")
    if verve:
        vid = verve.get('id') or verve.get('_id')
        vpl = verve.get('parent_location')
        vpid = vpl.get('id') or vpl.get('_id') if isinstance(vpl, dict) else vpl
        parent_loc = loc_by_id.get(vpid)
        pname = parent_loc.get('name') if parent_loc else "UNKNOWN"
        print(f"The Verve ID: {vid}")
        print(f"Parent Location Name: {pname} (ID: {vpid})")
        print(f"Keys: {verve.get('keys')}")
        print(f"Secondary Keys: {verve.get('secondary_keys')}")
        print(f"Included Lexicon Entries: {verve.get('included_lexicon_entries')}")
        print(f"Description sample: {verve.get('description', '')[:200]}...")
        print(f"Context Description: {verve.get('context_description', '')[:200]}...")
    else:
        print("ERROR: The Verve NOT FOUND!")

    # 3. Fetch live lexicon
    st_lex, live_lex = api_get(f'/worlds/lexicon/world/{WORLD_ID}')
    print(f"\nLexicon fetched: status {st_lex}, count: {len(live_lex)}")
    
    scan_persona_false = [e.get('name') for e in live_lex if not e.get('scan_persona')]
    whole_words_false = [e.get('name') for e in live_lex if not e.get('whole_words_only')]
    em_dash_entries = []
    for e in live_lex:
        n = e.get('name', '')
        c = e.get('content', '')
        if '—' in n or '—' in c:
            em_dash_entries.append(n)
    
    print(f"scan_persona == False: {len(scan_persona_false)}")
    print(f"whole_words_only == False: {len(whole_words_false)}")
    print(f"Entries with em-dash (—): {len(em_dash_entries)}")
    if em_dash_entries:
        print(f"  Sample em-dash entries: {em_dash_entries[:5]}")

    ignored_chars_count = sum(1 for e in live_lex if e.get('ignored_characters'))
    ignored_personas_count = sum(1 for e in live_lex if e.get('ignored_personas'))
    print(f"Entries with ignored_characters: {ignored_chars_count}")
    print(f"Entries with ignored_personas: {ignored_personas_count}")
    
    # Check specific suppression for Jasper and Alyssa
    jasper_entries = [e for e in live_lex if 'jasper' in e.get('name', '').lower() and e.get('type') == 'npc']
    alyssa_entries = [e for e in live_lex if 'alyssa' in e.get('name', '').lower() and e.get('type') == 'npc']
    for je in jasper_entries:
        print(f"Jasper NPC entry: '{je.get('name')}' | ignored_personas: {je.get('ignored_personas')} | ignored_characters: {je.get('ignored_characters')}")
    for ae in alyssa_entries:
        print(f"Alyssa NPC entry: '{ae.get('name')}' | ignored_personas: {ae.get('ignored_personas')} | ignored_characters: {ae.get('ignored_characters')}")

    # 4. Check Linked Characters
    st_lc, live_lc = api_get(f'/worlds/linked-characters/{WORLD_ID}')
    print(f"\nLinked Characters fetched: status {st_lc}, count: {len(live_lc)}")
    for lc in live_lc:
        cid = lc.get('id') or lc.get('_id') or lc.get('character_id')
        char_obj = lc.get('character', {}) if isinstance(lc.get('character'), dict) else lc
        cname = char_obj.get('name') or lc.get('name')
        print(f"  Linked: '{cname}' (ID: {cid})")

    # 5. Snapshot Zod parity
    print("\n--- Snapshot Zod Parity Check ---")
    with open(SNAPSHOT_PATH, 'r', encoding='utf-8') as f:
        snap = json.load(f)
    snap_entries = snap.get('entries')
    snap_lex = snap.get('lexicon')
    print(f"Snapshot entries is list: {isinstance(snap_entries, list)} (len: {len(snap_entries) if snap_entries else 0})")
    print(f"Snapshot lexicon is list: {isinstance(snap_lex, list)} (len: {len(snap_lex) if snap_lex else 0})")
    is_identical = (json.dumps(snap_entries) == json.dumps(snap_lex))
    print(f"entries == lexicon byte-for-byte identical: {is_identical}")

if __name__ == '__main__':
    main()
