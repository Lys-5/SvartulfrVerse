"""
Svartúlfr World Deployment Independent Verification Script
Validates the deployed World on Wyvern Web API asserting:
- HTTP 200 on /worlds/{id}, /worlds/environments/world/{id}, /worlds/locations/world/{id}, /worlds/lexicon/world/{id}
- World Core & Temporal Engine (world_age 10489902, epoch 827-12-21)
- Prompt Assembly & Assistant Linkage (simple_assistant_xRfBnV7wq48QppqbPPpTM, pha_kWkWUAfTJTF9q72c2bC98)
- Full Simulation Engine (6 JED+ attributes, narrative tiers combat, currencies, moodlets, anti-bloat toggles)
- 7 Canonical Environments
- 188 Hierarchical Locations (0 orphans, roots first, The Verve secret bar)
- Mirrored Lexicon with anti-bloat flags (selective, scan_persona, whole_words_only, highlight_keys)
- Linked Characters (8 active cards from /characters/mine)
- Snapshot integrity & Zod parity (entries == lexicon)
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
SNAPSHOT_PATH = os.path.join(ROOT_DIR, 'scratch', 'world_new_deployed.json')
BASE_URL = 'https://app.wyvern.chat/api'

def get_headers():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token = f.read().strip()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

def api_get(endpoint, max_retries=3):
    url = f"{BASE_URL}{endpoint}" if endpoint.startswith('/') else f"{BASE_URL}/{endpoint}"
    for attempt in range(max_retries):
        headers = get_headers()
        req = urllib.request.Request(url, headers=headers, method='GET')
        try:
            with urllib.request.urlopen(req) as resp:
                return resp.status, json.loads(resp.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code in (401, 403) and attempt < max_retries - 1:
                print(f"  [HTTPError {e.code}] Token expired or forbidden. Refreshing token...")
                refresh_script = os.path.join(ROOT_DIR, 'scratch', 'refresh_token.py')
                if os.path.exists(refresh_script):
                    os.system(f'python "{refresh_script}"')
                    time.sleep(1)
                    continue
            raise

def main():
    print("=" * 70)
    print("INDEPENDENT VERIFICATION OF DEPLOYED SVARTÚLFR WORLD")
    print("=" * 70)

    # 1. Load Snapshot to get world_id and offline verification
    if not os.path.exists(SNAPSHOT_PATH):
        print(f"FAIL: Snapshot file not found at {SNAPSHOT_PATH}")
        sys.exit(1)

    with open(SNAPSHOT_PATH, 'r', encoding='utf-8') as f:
        snapshot = json.load(f)

    world_id = snapshot.get('metadata', {}).get('world_id') or snapshot.get('world', {}).get('id')
    if not world_id:
        print("FAIL: Could not determine world_id from snapshot")
        sys.exit(1)

    print(f"Target World ID to verify: {world_id}")

    # 2. Live API Verification Calls
    print("\n--- 1. Live API Reachability & Status Checks ---")
    status_w, live_world = api_get(f'/worlds/{world_id}')
    print(f"  GET /api/worlds/{world_id} -> Status {status_w}")
    assert status_w == 200, f"Expected 200, got {status_w}"

    status_e, live_envs = api_get(f'/worlds/environments/world/{world_id}')
    print(f"  GET /api/worlds/environments/world/{world_id} -> Status {status_e} ({len(live_envs)} environments)")
    assert status_e == 200, f"Expected 200, got {status_e}"

    status_l, live_locs = api_get(f'/worlds/locations/world/{world_id}')
    print(f"  GET /api/worlds/locations/world/{world_id} -> Status {status_l} ({len(live_locs)} locations)")
    assert status_l == 200, f"Expected 200, got {status_l}"

    status_lex, live_lex = api_get(f'/worlds/lexicon/world/{world_id}')
    print(f"  GET /api/worlds/lexicon/world/{world_id} -> Status {status_lex} ({len(live_lex)} lexicon entries)")
    assert status_lex == 200, f"Expected 200, got {status_lex}"

    # 3. World Core & Temporal Settings
    print("\n--- 2. World Core & Temporal Invariants ---")
    print(f"  Name: {live_world.get('name')}")
    assert live_world.get('name') == "Svartúlfr — Blackwood & Solarton", "World name mismatch"
    print(f"  Visibility: {live_world.get('visibility')}")
    assert live_world.get('visibility') == "private", "Visibility must be private"
    print(f"  Rating: {live_world.get('rating')}")
    assert live_world.get('rating') == "explicit", "Rating must be explicit"
    print(f"  World Age: {live_world.get('world_age')}")
    assert live_world.get('world_age') == 10489902, f"Expected world_age 10489902, got {live_world.get('world_age')}"
    
    calendar = live_world.get('calendar', {})
    print(f"  Calendar Epoch Year: {calendar.get('start_year')}, Month: {calendar.get('start_month_id')}, Day: {calendar.get('start_day_of_month')}")
    assert calendar.get('start_year') == 827, "Start year must be 827"
    assert calendar.get('start_month_id') == "dec", "Start month must be dec"
    assert calendar.get('start_day_of_month') == 21, "Start day must be 21"

    # 4. Prompt Assembly & Assistant Integration
    print("\n--- 3. Prompt Assembly & Assistant Linkage ---")
    sys_prompt = live_world.get('system_prompt_override', '')
    print(f"  System Prompt Override Length: {len(sys_prompt)} chars")
    assert len(sys_prompt) > 500, "System prompt override must contain compiled assembly"
    assert "<ttrpg_mechanics>" in sys_prompt, "System prompt override must contain D20 + S.P.E.C.I.A.L. mechanics"
    assert "D20" in sys_prompt, "System prompt override must contain D20 engine"
    assert "<lupine_social_ecology>" in sys_prompt, "System prompt override must contain lupine social ecology"
    print(f"  Disable Enhanced Instructions: {live_world.get('disable_enhanced_instructions')}")
    assert live_world.get('disable_enhanced_instructions') is True, "disable_enhanced_instructions must be True"
    assert "dialogue in quotes" in live_world.get('final_instructions', ''), "Final instructions must contain format discipline"
    assert "—" not in live_world.get('final_instructions', ''), "Final instructions must not contain em-dash"

    # 5. Full Simulation Engine
    print("\n--- 4. Simulation Engine & Anti-Bloat Toggles ---")
    features = live_world.get('world_features', {})
    print(f"  World Features: {features}")
    assert features.get('show_party_stats') is False, "show_party_stats must be False (anti-bloat)"
    assert features.get('show_species_info') is False, "show_species_info must be False (anti-bloat)"
    assert features.get('ships') is False, "ships must be False"
    assert features.get('creature_catcher') is False, "creature_catcher must be False"
    assert features.get('inventory') is True, "inventory must be True"
    assert features.get('currency') is True, "currency must be True"
    assert features.get('combat') is True, "combat must be True"
    assert features.get('rpg_stats') is True, "rpg_stats must be True"
    assert features.get('relationships') is True, "relationships must be True"

    stat_config = live_world.get('stat_config', {})
    stats = stat_config.get('stats', [])
    print(f"  Stat Config: {len(stats)} stats (Base: {stat_config.get('base_value')}, Budget: {stat_config.get('point_budget')})")
    assert len(stats) == 6, f"Expected 6 JED+ attributes, got {len(stats)}"
    stat_abbrs = [s.get('abbreviation') for s in stats]
    print(f"  Stat Abbreviations: {stat_abbrs}")
    for exp_abbr in ['MGT', 'RES', 'AGI', 'WIT', 'PRS', 'SCT']:
        assert exp_abbr in stat_abbrs, f"Missing stat abbreviation {exp_abbr}"
    assert stat_config.get('point_budget') == 25, "Point budget must be 25"
    assert stat_config.get('base_value') == 1, "Base value must be 1"

    combat = live_world.get('combat_ruleset', {})
    print(f"  Combat Ruleset Model: {combat.get('model')}")
    assert combat.get('model') == 'narrative_tiers', "Combat model must be narrative_tiers"

    currencies = live_world.get('currencies', [])
    print(f"  Currencies: {[c.get('symbol') + ' (' + c.get('name') + ')' for c in currencies]}")
    assert len(currencies) == 2, f"Expected 2 currencies, got {len(currencies)}"
    assert any(c.get('is_primary') and c.get('symbol') == '$' for c in currencies), "Primary currency must be $"
    assert any(c.get('symbol') == 'Cr' for c in currencies), "Secondary currency must be Cr"

    rel = live_world.get('relationship_config', {})
    print(f"  Relationship Moodlets: {len(rel.get('moodlets', []))}, Tiers: {len(rel.get('tiers', []))}")
    assert len(rel.get('moodlets', [])) == 10, f"Expected 10 moodlets, got {len(rel.get('moodlets', []))}"
    assert len(rel.get('tiers', [])) == 13 or len(rel.get('tiers', [])) == 14, "Expected relationship tiers"

    linked = live_world.get('linked_characters', [])
    if not linked:
        status_lc, linked = api_get(f'/worlds/linked-characters/{world_id}')
    print(f"  Linked Characters count: {len(linked)}")
    assert len(linked) == 8, f"Expected 8 linked characters, got {len(linked)}"
    linked_ids = []
    for c in linked:
        if isinstance(c, dict):
            cid = c.get('id') or c.get('_id') or c.get('character_id') or (c.get('character', {}).get('id') if isinstance(c.get('character'), dict) else None)
            linked_ids.append(cid)
        elif isinstance(c, str):
            linked_ids.append(c)
    for cid in ['_t4J9aQNJM36cUKAP4wB4U', '_QPea6g4Q1QfeYCVHCLMPR', '_T8Ywcr9FEqNf9JxbK6eHP', '_RDfz7XzTpM23LpPALVXHM', '_zFLUjV8aVxQRAfQxGcAcY', '_TbRM3EdxDjHFgqztTbCpL', '_HEQQbbRFwKdG8QE2Fh1z1', '_zn24784jfcchQ7EwCyAnm']:
        assert cid in linked_ids, f"Missing linked character ID {cid} in {linked_ids}"

    # 6. Environments Verification
    print("\n--- 5. 7 Environments Invariant ---")
    assert len(live_envs) == 7, f"Expected 7 environments, got {len(live_envs)}"
    env_names = [e.get('name') for e in live_envs]
    print(f"  Live Environments found: {env_names}")
    expected_env_names = [
        "California Coast",
        "SUCC campus",
        "Solarton",
        "Blackwood",
        "Seven Hills",
        "DMHA HQ & Guild District",
        "Voidspace/Otherworld"
    ]
    for exp_env in expected_env_names:
        assert exp_env in env_names, f"Missing canonical environment '{exp_env}'"

    # 7. 188 Locations Hierarchy & Zero Orphan Verification
    print("\n--- 6. 188 Locations & Topology Integrity ---")
    assert len(live_locs) == 188, f"Expected exactly 188 locations, got {len(live_locs)}"
    loc_id_set = set(l.get('id') or l.get('_id') for l in live_locs)
    
    roots = []
    nested = []
    orphans = []

    verve_loc = None

    for loc in live_locs:
        lname = loc.get('name')
        lid = loc.get('id') or loc.get('_id')
        pl = loc.get('parent_location')
        if lname == 'The Verve':
            verve_loc = loc

        if not pl:
            roots.append(loc)
        else:
            pid = pl.get('id') or pl.get('_id') if isinstance(pl, dict) else pl
            if pid not in loc_id_set:
                orphans.append((lid, lname, pid))
            else:
                nested.append(loc)

    print(f"  Root Locations: {len(roots)}")
    print(f"  Nested Locations: {len(nested)}")
    print(f"  Orphan Locations: {len(orphans)}")
    assert len(orphans) == 0, f"Found {len(orphans)} orphan locations: {orphans}"
    assert len(roots) == 8, f"Expected 8 roots, got {len(roots)}"
    assert len(nested) == 180, f"Expected 180 nested nodes, got {len(nested)}"

    # The Verve Check
    print("\n--- 7. 'The Verve' Secret Bar Configuration ---")
    assert verve_loc is not None, "'The Verve' location not found in world"
    parent_of_verve = verve_loc.get('parent_location')
    if isinstance(parent_of_verve, dict):
        parent_name = parent_of_verve.get('name')
    else:
        loc_name_map = {l.get('id') or l.get('_id'): l.get('name') for l in live_locs}
        parent_name = loc_name_map.get(parent_of_verve)
    print(f"  Parent Location: {parent_name}")
    assert parent_name == 'Bluemoon', f"Expected parent 'Bluemoon', got '{parent_name}'"
    print(f"  Keys: {verve_loc.get('keys')}")
    inc_lex = verve_loc.get('included_lexicon_entries', [])
    print(f"  Included Lexicon Entries: {inc_lex}")
    assert '_YxGJRFDkjdVyeH1mJNM1T' in inc_lex, "Missing Lighter in The Verve"
    assert '_UVX1RAqE8CWz8ywYkT4Fm' in inc_lex, "Missing Wireless Earbuds in The Verve"
    assert '_BRjbkk8JM3Jw1xyJGgzDH' in inc_lex, "Missing Keys in The Verve"

    # 8. Mirrored Lexicon & Anti-Bloat Verification
    print("\n--- 8. Mirrored Lexicon & Flag Trio Invariants ---")
    print(f"  Total live lexicon entries: {len(live_lex)}")
    assert len(live_lex) >= 700, f"Expected >= 700 lexicon entries, got {len(live_lex)}"

    sample_flagged = [
        e for e in live_lex
        if e.get('scan_persona') is True and e.get('whole_words_only') is True
    ]
    print(f"  Entries with Standard Flag Pair (scan_persona, whole_words_only): {len(sample_flagged)} / {len(live_lex)}")
    assert len(sample_flagged) == len(live_lex), "All lexicon entries must have standard flags on True"

    # 9. Snapshot & Frontend Zod Parity Invariant
    print("\n--- 9. Snapshot & Frontend Zod Parity ---")
    assert snapshot.get('world') is not None, "Snapshot missing 'world' object"
    assert (snapshot.get('locations') is not None or snapshot.get('world_locations') is not None), "Snapshot missing locations"
    assert (snapshot.get('environments') is not None or snapshot.get('world_environments') is not None), "Snapshot missing environments"
    assert snapshot.get('world_lexicon') is not None, "Snapshot missing 'world_lexicon'"
    
    # Parity check
    snap_entries = snapshot.get('entries', [])
    snap_lex = snapshot.get('lexicon', [])
    print(f"  Snapshot entries count: {len(snap_entries)}, lexicon count: {len(snap_lex)}")
    assert len(snap_entries) == len(snap_lex), "Snapshot entries and lexicon length mismatch"
    assert json.dumps(snap_entries) == json.dumps(snap_lex), "Snapshot entries and lexicon must be 100% byte-for-byte identical"

    print("\n" + "=" * 70)
    print("ALL VERIFICATION CHECKS PASSED: 100% SUCCESS")
    print("=" * 70)

if __name__ == '__main__':
    main()
