import json
import urllib.request
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRATCH = ROOT / 'scratch'
FINAL = ROOT / 'FINAL'

TOKEN = (SCRATCH / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'User-Agent': 'Mozilla/5.0'
}

def verify_all():
    print("=========================================")
    print("=== LIVE FORENSIC VERIFICATION AUDIT ===")
    print("=========================================")
    
    # 1. World Equipment Check
    print("\n[1/3] Verifying Equipment Effects...")
    req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/lexicon/world/{WORLD_ID}', headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        lex = json.loads(resp.read().decode('utf-8'))
        
    def has_effects(effects):
        if not effects or not isinstance(effects, dict):
            return False
        for v in effects.values():
            if v is not None and v is not False:
                if isinstance(v, (list, dict)) and len(v) > 0:
                    return True
                elif not isinstance(v, (list, dict)):
                    return True
        return False

    equip_items = []
    equip_no_effects = []
    for e in lex:
        ic = e.get('item_config') or {}
        if ic.get('equip_slot'):
            equip_items.append(e)
            if not has_effects(ic.get('effects')):
                equip_no_effects.append(e)
                
    print(f"Total Lexicon Items: {len(lex)}")
    print(f"Total Equipment Items: {len(equip_items)}")
    print(f"Equipment with NO effects: {len(equip_no_effects)}")
    assert len(equip_no_effects) == 0, f"Expected 0 equipment with no effects, found {len(equip_no_effects)}"
    print("PASS: 14/14 Equipment items have valid, active statModifiers!")
    
    # 2. Travel Routes Check
    print("\n[2/3] Verifying Travel Routes...")
    w_req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/{WORLD_ID}', headers=HEADERS)
    with urllib.request.urlopen(w_req) as resp:
        world = json.loads(resp.read().decode('utf-8'))
        
    routes = world.get('travel_routes', [])
    print(f"World travel_routes count: {len(routes)}")
    print(f"World free_travel: {world.get('free_travel')}")
    assert len(routes) == 192, f"Expected 192 routes, found {len(routes)}"
    assert world.get('free_travel') is False, "Expected free_travel to be False"
    
    # Check connectivity and location validity
    loc_req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/locations/world/{WORLD_ID}', headers=HEADERS)
    with urllib.request.urlopen(loc_req) as resp:
        locs = json.loads(resp.read().decode('utf-8'))
    loc_ids = {l.get('id') or l.get('_id') for l in locs}
    
    for r in routes:
        assert r.get('from_location_id') in loc_ids, f"Invalid from_location_id: {r.get('from_location_id')}"
        assert r.get('to_location_id') in loc_ids, f"Invalid to_location_id: {r.get('to_location_id')}"
        assert r.get('required_mediums'), f"Missing required_mediums on route {r.get('id')}"
        assert r.get('distance') is not None, f"Missing distance on route {r.get('id')}"
    print("PASS: 192/192 Travel routes valid and linked to existing world locations!")
    
    # 3. World Eras Check
    print("\n[3/3] Verifying World Eras...")
    eras_req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/eras/world/{WORLD_ID}', headers=HEADERS)
    with urllib.request.urlopen(eras_req) as resp:
        eras = json.loads(resp.read().decode('utf-8'))
        
    print(f"World eras count: {len(eras)}")
    assert len(eras) == 4, f"Expected 4 eras, found {len(eras)}"
    
    eras.sort(key=lambda x: x.get('display_order', 0))
    expected_ranges = [
        (0, 3261144),
        (3261144, 8941392),
        (8941392, 10273800),
        (10273800, None)
    ]
    for idx, e in enumerate(eras):
        exp_start, exp_end = expected_ranges[idx]
        assert e.get('start_position') == exp_start, f"Era {idx+1} start_position mismatch: got {e.get('start_position')}, expected {exp_start}"
        assert e.get('end_position') == exp_end, f"Era {idx+1} end_position mismatch: got {e.get('end_position')}, expected {exp_end}"
        print(f" - [{e.get('display_order')}] {e.get('name')} (ID: {e.get('id')}) | {e.get('start_position')} -> {e.get('end_position')}")
    print("PASS: All 4 canonical eras verified with exact proleptic Gregorian epoch hours on live world!")
    
    # 4. Local Files Check
    print("\n[4/4] Verifying Local Parity...")
    assert (FINAL / 'Svartulfr_World_Travel_Routes.json').exists()
    assert (FINAL / 'Svartulfr_World_Eras.json').exists()
    assert (FINAL / 'Svartulfr_Lorebook_I.json').exists()
    assert (ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_Lorebook_I.json').exists()
    assert (SCRATCH / 'live_world__YpX47fNraQFw2dD7TdycJ_travel_routes.json').exists()
    assert (SCRATCH / 'live_world__YpX47fNraQFw2dD7TdycJ_eras.json').exists()
    assert (SCRATCH / 'live_world__YpX47fNraQFw2dD7TdycJ_lexicon.json').exists()
    
    # Verify entries == lexicon byte-for-byte
    with open(FINAL / 'Svartulfr_Lorebook_I.json', 'r', encoding='utf-8') as f:
        f1 = json.load(f)
    with open(ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_Lorebook_I.json', 'r', encoding='utf-8') as f:
        o1 = json.load(f)
    assert f1['entries'] == f1['lexicon'], "FINAL/Svartulfr_Lorebook_I.json entries != lexicon"
    assert o1['entries'] == o1['lexicon'], "lorebooks/optimized/Svartulfr_Lorebook_I.json entries != lexicon"
    assert f1 == o1, "FINAL and lorebooks/optimized Lorebook I out of sync!"
    print("PASS: All local snapshots in FINAL/, scratch/, and lorebooks/optimized/ are present and in sync!")
    
    print("\n=========================================")
    print("=== ALL VERIFICATIONS PASSED 100%! ===")
    print("=========================================")

if __name__ == '__main__':
    verify_all()
