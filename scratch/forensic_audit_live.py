"""
Independent Forensic Audit Script for Svartúlfr World (_YpX47fNraQFw2dD7TdycJ)
Auditor: auditor_1_integrity
Executes direct live HTTP requests to Wyvern Web API and collects forensic evidence.
"""

import sys
import os
import json
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
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
    print("=" * 80)
    print(f"FORENSIC AUDIT: LIVE QUERY TO WYVERN WEB API FOR WORLD '{WORLD_ID}'")
    print("=" * 80)

    # 1. Direct GET endpoints
    print("\n[Audit 1: Live Cloud Queries]")
    endpoints = {
        'world': f'/worlds/{WORLD_ID}',
        'environments': f'/worlds/environments/world/{WORLD_ID}',
        'locations': f'/worlds/locations/world/{WORLD_ID}',
        'lexicon': f'/worlds/lexicon/world/{WORLD_ID}',
        'linked_characters': f'/worlds/linked-characters/{WORLD_ID}'
    }

    live_data = {}
    status_codes = {}

    for name, ep in endpoints.items():
        try:
            status, data = api_get(ep)
            status_codes[name] = status
            live_data[name] = data
            count = len(data) if isinstance(data, list) else 1
            print(f"  * {ep} -> HTTP {status} (Records: {count})")
        except urllib.error.HTTPError as e:
            status_codes[name] = e.code
            print(f"  ! {ep} -> HTTP ERROR {e.code}")
            sys.exit(1)

    world = live_data['world']
    envs = live_data['environments']
    locs = live_data['locations']
    lex = live_data['lexicon']
    linked = live_data['linked_characters']

    # 2. Forensic Core Invariants
    print("\n[Audit 2: Structural & State Invariants]")
    print(f"  World ID: {world.get('id') or world.get('_id')}")
    print(f"  World Name: {world.get('name')}")
    print(f"  Visibility: {world.get('visibility')}")
    print(f"  World Age: {world.get('world_age')}")
    print(f"  Calendar Epoch Year: {world.get('calendar', {}).get('start_year')}")
    print(f"  Environments Count: {len(envs)}")
    print(f"  Locations Count: {len(locs)}")
    print(f"  Lexicon Entries Count: {len(lex)}")
    print(f"  Linked Characters Count: {len(linked)}")

    # 3. Location Topology Audit (Orphans, Parents)
    print("\n[Audit 3: Location Topology & Orphan Detection]")
    loc_ids = set(l.get('id') or l.get('_id') for l in locs)
    roots = []
    nested = []
    orphans = []
    verve_entry = None

    for l in locs:
        lid = l.get('id') or l.get('_id')
        lname = l.get('name')
        if lname == 'The Verve':
            verve_entry = l
        pl = l.get('parent_location')
        if not pl:
            roots.append((lid, lname))
        else:
            pid = pl.get('id') or pl.get('_id') if isinstance(pl, dict) else pl
            if pid not in loc_ids:
                orphans.append((lid, lname, pid))
            else:
                nested.append((lid, lname, pid))

    print(f"  Roots count: {len(roots)}")
    print(f"  Nested count: {len(nested)}")
    print(f"  Orphans count: {len(orphans)}")
    if orphans:
        print(f"  CRITICAL ORPHANS FOUND: {orphans}")
    else:
        print("  PASS: Zero orphaned locations confirmed.")

    # 4. Check The Verve
    print("\n[Audit 4: The Verve Secret Bar Audit]")
    if verve_entry:
        v_parent = verve_entry.get('parent_location')
        v_pid = v_parent.get('id') or v_parent.get('_id') if isinstance(v_parent, dict) else v_parent
        parent_loc_obj = next((x for x in locs if (x.get('id') or x.get('_id')) == v_pid), None)
        parent_name = parent_loc_obj.get('name') if parent_loc_obj else None
        print(f"  The Verve ID: {verve_entry.get('id') or verve_entry.get('_id')}")
        print(f"  Parent Location: {parent_name} ({v_pid})")
        print(f"  Included Lexicon Entries: {verve_entry.get('included_lexicon_entries')}")
    else:
        print("  FAIL: The Verve not found in locations list!")

    # 5. Full Simulation Engine Configuration
    print("\n[Audit 5: Simulation Engine & Anti-Bloat Configuration]")
    features = world.get('world_features', {})
    print(f"  inventory: {features.get('inventory')}")
    print(f"  currency: {features.get('currency')}")
    print(f"  combat: {features.get('combat')}")
    print(f"  rpg_stats: {features.get('rpg_stats')}")
    print(f"  relationships: {features.get('relationships')}")
    print(f"  show_party_stats: {features.get('show_party_stats')} (Anti-bloat expectation: False)")
    print(f"  show_species_info: {features.get('show_species_info')} (Anti-bloat expectation: False)")
    print(f"  ships: {features.get('ships')} (Anti-bloat expectation: False)")
    print(f"  creature_catcher: {features.get('creature_catcher')} (Anti-bloat expectation: False)")

    stat_config = world.get('stat_config', {})
    stats = stat_config.get('stats', [])
    stat_abbrs = [s.get('abbreviation') for s in stats]
    print(f"  Stat count: {len(stats)}, Abbreviations: {stat_abbrs}")
    print(f"  Base value: {stat_config.get('base_value')}, Point budget: {stat_config.get('point_budget')}")

    combat = world.get('combat_ruleset', {})
    print(f"  Combat Model: {combat.get('model')}")

    currencies = world.get('currencies', [])
    print(f"  Currencies: {[(c.get('symbol'), c.get('name'), c.get('is_primary')) for c in currencies]}")

    moodlets = world.get('relationship_config', {}).get('moodlets', [])
    print(f"  Moodlets count: {len(moodlets)}")

    # 6. Linked Characters Audit
    print("\n[Audit 6: Linked Characters Identification]")
    core_expected = {
        '_t4J9aQNJM36cUKAP4wB4U': 'Jasper',
        '_QPea6g4Q1QfeYCVHCLMPR': 'Erik',
        '_T8Ywcr9FEqNf9JxbK6eHP': 'Logan',
        '_RDfz7XzTpM23LpPALVXHM': 'Malachia',
        '_zFLUjV8aVxQRAfQxGcAcY': 'Noah',
        '_TbRM3EdxDjHFgqztTbCpL': 'Edric',
        '_HEQQbbRFwKdG8QE2Fh1z1': 'Wulfnic',
        '_zn24784jfcchQ7EwCyAnm': 'Mackenzie'
    }
    found_linked_ids = []
    for c in linked:
        if isinstance(c, dict):
            cid = c.get('id') or c.get('_id') or c.get('character_id') or (c.get('character', {}).get('id') if isinstance(c.get('character'), dict) else None)
            cname = c.get('name') or (c.get('character', {}).get('name') if isinstance(c.get('character'), dict) else None)
            found_linked_ids.append((cid, cname))
        else:
            found_linked_ids.append((c, 'Unknown'))

    print(f"  Found {len(found_linked_ids)} linked characters:")
    for cid, cname in found_linked_ids:
        exp_name = core_expected.get(cid, 'UNEXPECTED')
        print(f"    - ID: {cid} ({cname}) -> Expected: {exp_name}")

    # 7. Format Discipline & Em-Dash Audit
    print("\n[Audit 7: Format Discipline & Em-Dash Forensic Scan]")
    em_dash_hits = []

    def check_text(entity_type, entity_id, entity_name, field, text):
        if not text or not isinstance(text, str):
            return
        if '\u2014' in text:
            count = text.count('\u2014')
            em_dash_hits.append({
                'entity_type': entity_type,
                'entity_id': entity_id,
                'entity_name': entity_name,
                'field': field,
                'count': count,
                'sample': text[:100]
            })

    # Check World
    for field in ['name', 'description', 'tagline', 'system_prompt_override', 'base_instructions', 'final_instructions', 'context_description']:
        check_text('World', WORLD_ID, world.get('name'), field, world.get(field))

    # Check Environments
    for e in envs:
        eid = e.get('id') or e.get('_id')
        ename = e.get('name')
        for f in ['name', 'description', 'context_description', 'brief_context_description', 'final_instructions']:
            check_text('Environment', eid, ename, f, e.get(f))

    # Check Locations
    for l in locs:
        lid = l.get('id') or l.get('_id')
        lname = l.get('name')
        for f in ['name', 'description', 'context_description', 'brief_context_description', 'final_instructions']:
            check_text('Location', lid, lname, f, l.get(f))

    # Check Lexicon
    for entry in lex:
        xid = entry.get('id') or entry.get('_id')
        xname = entry.get('name')
        for f in ['name', 'content']:
            check_text('Lexicon', xid, xname, f, entry.get(f))

    print(f"  Total Em-dash violations found in entity fields: {len(em_dash_hits)}")
    for hit in em_dash_hits:
        print(f"    ! [{hit['entity_type']}] ID={hit['entity_id']} Name='{hit['entity_name']}' Field='{hit['field']}' Count={hit['count']} Sample: {repr(hit['sample'])}")

    # 8. Check Plain Text & Quotes Narration Rules in Prompts & Instructions
    print("\n[Audit 8: Quote Rules and Narration Discipline in Prompts]")
    f_inst = world.get('final_instructions', '')
    sys_prompt = world.get('system_prompt_override', '')
    b_inst = world.get('base_instructions', '')

    print(f"  'dialogue in quotes' in final_instructions: {'dialogue in quotes' in f_inst}")
    print(f"  'actions and narration in plain text' in final_instructions: {'actions and narration in plain text' in f_inst}")
    print(f"  'asterisks reserved for internal thoughts' in final_instructions: {'asterisks reserved for internal thoughts' in f_inst}")
    print(f"  'Never use the em dash' in final_instructions: {'Never use the em dash' in f_inst}")
    print(f"  'Format Discipline' in system_prompt_override: {'Format Discipline' in sys_prompt}")
    print(f"  'Italian' language directive in system_prompt_override: {'Italian' in sys_prompt}")
    print(f"  'D20 + S.P.E.C.I.A.L.' resolution engine in system_prompt_override: {'S.P.E.C.I.A.L.' in sys_prompt}")

    print("\n" + "=" * 80)
    print("LIVE AUDIT SCRIPT EXECUTION FINISHED")
    print("=" * 80)

if __name__ == '__main__':
    main()
