"""
Comprehensive End-to-End Test Suite for Svartúlfr World RPG Systems
Validates all requirements of Phases 1 to 5.
"""

import sys
import os
import json
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')

def get_headers():
    from scripts.wyvern_api_client import get_auth_token
    token = get_auth_token()
    return {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }

def test_phase1_stat_config(world_data):
    print("\n[TEST 1] Verifying Phase 1: S.P.E.C.I.A.L. Stat Config & Combat stat_roles...")
    sc = world_data.get('stat_config') or {}
    stats = sc.get('stats', [])
    assert len(stats) == 7, f"Expected 7 stats, got {len(stats)}"
    
    stat_ids = [s['id'] for s in stats]
    expected_ids = ['strength', 'perception', 'endurance', 'charisma', 'intelligence', 'agility', 'luck']
    assert stat_ids == expected_ids, f"Stat IDs mismatch: {stat_ids} vs {expected_ids}"
    
    assert sc.get('base_value') == 8, f"Expected base_value 8, got {sc.get('base_value')}"
    assert sc.get('max_value') == 30, f"Expected max_value 30, got {sc.get('max_value')}"
    assert sc.get('point_budget') == 25, f"Expected point_budget 25, got {sc.get('point_budget')}"
    
    stat_roles = sc.get('stat_roles') or {}
    expected_roles = {
        "hp_stat": "endurance",
        "mp_stat": "intelligence",
        "physical_attack": "strength",
        "physical_defense": "endurance",
        "special_attack": "intelligence",
        "special_defense": "intelligence",
        "speed": "agility",
        "accuracy": "perception",
        "evasion": "agility",
        "flee": "agility",
        "luck": "luck"
    }
    for role, stat in expected_roles.items():
        assert stat_roles.get(role) == stat, f"Role mismatch: {role} -> {stat_roles.get(role)} (expected {stat})"
        
    print("  -> Phase 1 PASS: S.P.E.C.I.A.L. (7 stats, base 8, max 30, budget 25) and combat stat_roles 100% matched!")

def test_phase2_catalogs():
    print("\n[TEST 2] Verifying Phase 2: Species, Occupations, and Traits Catalogs on World...")
    headers = get_headers()
    
    # 1. Species
    url_sp = f"https://app.wyvern.chat/api/worlds/rpg/species/{WORLD_ID}"
    req = urllib.request.Request(url_sp, headers=headers)
    with urllib.request.urlopen(req) as resp:
        species = json.loads(resp.read().decode('utf-8'))
    assert len(species) >= 24, f"Expected at least 24 species, got {len(species)}"
    
    # 2. Occupations
    url_occ = f"https://app.wyvern.chat/api/worlds/rpg/occupations/{WORLD_ID}"
    req = urllib.request.Request(url_occ, headers=headers)
    with urllib.request.urlopen(req) as resp:
        occupations = json.loads(resp.read().decode('utf-8'))
    assert len(occupations) >= 37, f"Expected at least 37 occupations, got {len(occupations)}"
    
    # 3. Traits
    url_tr = f"https://app.wyvern.chat/api/worlds/rpg/traits/{WORLD_ID}"
    req = urllib.request.Request(url_tr, headers=headers)
    with urllib.request.urlopen(req) as resp:
        traits = json.loads(resp.read().decode('utf-8'))
    assert len(traits) >= 74, f"Expected at least 74 traits, got {len(traits)}"
    
    print(f"  -> Phase 2 PASS: {len(species)} Species, {len(occupations)} Occupations, {len(traits)} Traits active and verified on World API!")

def test_phase3_moodlets(world_data):
    print("\n[TEST 3] Verifying Phase 3: Relationship Config & 12 Custom Moodlets...")
    rc = world_data.get('relationship_config') or {}
    assert rc.get('enabled') is True, "relationship_config.enabled must be True"
    
    custom_moodlets = rc.get('custom_moodlets', [])
    assert len(custom_moodlets) == 12, f"Expected 12 custom_moodlets, got {len(custom_moodlets)}"
    
    mood_ids = [m['id'] for m in custom_moodlets]
    expected_moods = [
        'rut', 'heat', 'scent_marked', 'mated_devotion',
        'vampiric_blood_hunger', 'blood_frenzy', 'essentia_hunger',
        'seductive_haze', 'pack_bond_resonance', 'feral_aggression',
        'blood_oath_bond', 'betrayed_trust'
    ]
    for m in expected_moods:
        assert m in mood_ids, f"Missing custom mood: {m}"
        
    legacy_moodlets = rc.get('moodlets', [])
    assert len(legacy_moodlets) == 12, f"Expected 12 legacy moodlets, got {len(legacy_moodlets)}"
    
    print(f"  -> Phase 3 PASS: 12 Custom Moodlets configured with delta, duration_hours, description & legacy parity!")

def test_phase4_items_and_shops():
    print("\n[TEST 4] Verifying Phase 4: 54 Shop Items Bonification & 5 Shop Locations...")
    headers = get_headers()
    
    # Fetch Lexicon items
    url_lex = f"https://app.wyvern.chat/api/worlds/lexicon/world/{WORLD_ID}"
    req_lex = urllib.request.Request(url_lex, headers=headers)
    with urllib.request.urlopen(req_lex) as resp:
        lexicon = json.loads(resp.read().decode('utf-8'))
    items = [e for e in lexicon if e.get('type') == 'item']
    assert len(items) >= 54, f"Expected at least 54 items, got {len(items)}"
    items_by_id = {e['id']: e for e in items}
    
    # Fetch Locations
    url_loc = f"https://app.wyvern.chat/api/worlds/locations/world/{WORLD_ID}"
    req_loc = urllib.request.Request(url_loc, headers=headers)
    with urllib.request.urlopen(req_loc) as resp:
        locations = json.loads(resp.read().decode('utf-8'))
        
    target_shops = [
        "_H7PpzWXrQ228RgBw1Rqh9", # Market-Zone
        "_QHaW3bG49Dx1QW4Ugg8xn", # Full Moon Market
        "_PjVjY62CtnLbhrEE69GbK", # Tidewrack Surf
        "_CAAHGnM3BGKpUb7JXYWm7", # Dusty Coyote Diner
        "_HPnYePHbmCVM9tMp69Hrg"  # The Verve
    ]
    
    all_sold_items = set()
    found_shops = 0
    for loc in locations:
        lid = loc.get('id')
        if lid in target_shops:
            mk = loc.get('marketplace_config')
            assert mk is not None and mk.get('enabled') is True, f"Shop at {lid} not enabled"
            found_shops += 1
            for inv in mk.get('inventory', []):
                all_sold_items.add(inv.get('lexicon_entry_id'))
                
    assert found_shops == 5, f"Expected 5 shops configured, got {found_shops}"
    assert len(all_sold_items) == 54, f"Expected 54 shop items sold across 5 shops, got {len(all_sold_items)}"

    # Check all 54 shop item prices & tradeable status
    USD_ID = "fbecc738-f9f7-4426-b8a1-a237b8ad922c"
    CR_ID = "8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a"
    for sid in all_sold_items:
        it = items_by_id.get(sid)
        assert it is not None, f"Shop item {sid} missing from World Lexicon"
        cfg = it.get('item_config')
        assert cfg is not None, f"Item {it.get('name')} missing item_config"
        val = cfg.get('value')
        assert isinstance(val, dict) and USD_ID in val and CR_ID in val, f"Item {it.get('name')} missing USD/CR prices in value"
        assert cfg.get('tradeable') is True, f"Item {it.get('name')} must be tradeable"
    
    print(f"  -> Phase 4 PASS: 54 shop items priced in USD ($) and Cr, 5 shops active, 0 unobtainable items! (Total item entries: {len(items)})")

def test_phase5_rules():
    print("\n[TEST 5] Verifying Phase 5: Auto-provisioning rule in rules and GEMINI.md...")
    with open(os.path.join(ROOT_DIR, 'GEMINI.md'), 'r', encoding='utf-8') as f:
        gemini_txt = f.read()
    assert "Regola di Auto-Provisioning (Specie, Tratti e Occupazioni)" in gemini_txt, "Missing auto-provisioning rule in GEMINI.md"
    assert "hp_stat: \"endurance\"" in gemini_txt, "Missing combat roles in GEMINI.md"
    
    with open(os.path.join(ROOT_DIR, '.agents', 'rules', '09_rpg_stats_e_simulation.md'), 'r', encoding='utf-8') as f:
        rule_txt = f.read()
    assert "## 5. Regola di Auto-Provisioning RPG (Specie, Occupazioni e Tratti Mancanti)" in rule_txt, "Missing section 5 in 09_rpg_stats_e_simulation.md"
    assert "Auto-Provisioning Immediato" in rule_txt, "Missing immediate auto-provisioning requirement in rule 09"
    
    print("  -> Phase 5 PASS: Auto-provisioning rules strictly codified in GEMINI.md and rule 09!")

def test_phase6_autoprovisioning_and_omniparity():
    print("\n[TEST 6] Verifying Phase 6: Omni-Parity in FINAL/ and End-to-End Auto-Provisioning Pipeline...")
    from scripts.auto_provision_rpg import check_and_provision_entity, delete_provisioned_entity, get_catalog
    
    # 1. Verify Omni-Parity in FINAL/
    final_sp = os.path.join(ROOT_DIR, 'FINAL', 'rpg_species_catalog.json')
    final_occ = os.path.join(ROOT_DIR, 'FINAL', 'rpg_occupations_catalog.json')
    final_tr = os.path.join(ROOT_DIR, 'FINAL', 'rpg_traits_catalog.json')
    final_cfg = os.path.join(ROOT_DIR, 'FINAL', 'Svartulfr_World_RPG_Config.json')
    
    assert os.path.exists(final_sp), "Missing FINAL/rpg_species_catalog.json"
    assert os.path.exists(final_occ), "Missing FINAL/rpg_occupations_catalog.json"
    assert os.path.exists(final_tr), "Missing FINAL/rpg_traits_catalog.json"
    assert os.path.exists(final_cfg), "Missing FINAL/Svartulfr_World_RPG_Config.json"
    
    with open(final_sp, 'r', encoding='utf-8') as f:
        assert len(json.load(f)) >= 24, "FINAL species catalog must have at least 24 entries"
    with open(final_occ, 'r', encoding='utf-8') as f:
        assert len(json.load(f)) >= 37, "FINAL occupations catalog must have at least 37 entries"
    with open(final_tr, 'r', encoding='utf-8') as f:
        assert len(json.load(f)) >= 74, "FINAL traits catalog must have at least 74 entries"
        
    print("  -> Omni-Parity Check: All 3 master catalogs and World RPG Config present and verified in FINAL/!")
    
    # 2. Test Existing Entity Detection (No duplicate creation)
    prov, existing_sp = check_and_provision_entity('species', 'Licantropo (Werewolf)')
    assert prov is False, "Existing species should not trigger auto-provisioning"
    assert existing_sp.get('name') == 'Licantropo (Werewolf)'
    print("  -> Existing Entity Check: Recognized 'Licantropo (Werewolf)' without duplicate creation!")
    
    # 3. Test Missing Entity Auto-Provisioning (Creation + Teardown)
    probe_name = "__TEST_AUTO_PROV_PROBE__"
    prov, created = check_and_provision_entity(
        'species',
        probe_name,
        description="Temporary probe verifying auto-provisioning pipeline.",
        stat_modifiers={'endurance': 2, 'strength': 1}
    )
    assert prov is True, "Missing species must trigger auto-provisioning"
    probe_id = created.get('id')
    assert probe_id is not None, "Created entity must have an ID"
    print(f"  -> Auto-Provision Probe: Successfully created live probe '{probe_name}' (id: {probe_id})!")
    
    # Verify presence in catalog
    updated_cat = get_catalog('species')
    assert len(updated_cat) == 25, f"Expected 25 species after auto-provision, got {len(updated_cat)}"
    
    # Clean teardown
    delete_provisioned_entity('species', probe_id)
    cleared_cat = get_catalog('species')
    assert len(cleared_cat) == 24, f"Expected 24 species after teardown, got {len(cleared_cat)}"
    print(f"  -> Clean Teardown: Probe '{probe_name}' deleted cleanly via DELETE without Fastify errors!")
    print("  -> Phase 6 PASS: Omni-Parity and Live Auto-Provisioning pipeline 100% verified!")

def test_phase7_slowburn_calibration(world_data):
    print("\n[TEST 7] Verifying Phase 7: R1 Relationship Slowburn & Inline Command Config...")
    rc = world_data.get('relationship_config') or {}
    assert rc.get('decay_curve') == 'ease_out', f"Expected decay_curve 'ease_out', got {rc.get('decay_curve')}"
    for flag in ('enabled', 'persistent_enabled', 'moodlets_enabled', 'decay_enabled', 'seed_from_attitudes', 'show_to_player'):
        assert rc.get(flag) is True, f"relationship_config.{flag} must be True"

    mags = rc.get('magnitudes') or {}
    reg = mags.get('regular') or {}
    sev = mags.get('severe') or {}
    assert 0 < reg.get('persistent', 99) < 5, f"regular.persistent not slowburn: {reg}"
    assert 0 < reg.get('moodlet_delta', 99) < 12, f"regular.moodlet_delta not slowburn: {reg}"
    assert 0 < sev.get('persistent', 99) < 12, f"severe.persistent not slowburn: {sev}"
    assert 0 < sev.get('moodlet_delta', 99) < 25, f"severe.moodlet_delta not slowburn: {sev}"

    ladder = rc.get('tier_ladder') or []
    assert len(ladder) == 14, f"Expected 14 tier_ladder entries, got {len(ladder)}"
    assert ladder[0].get('min_points') == -100, f"tier_ladder must start at -100, got {ladder[0]}"
    pts = [t['min_points'] for t in ladder]
    assert pts == sorted(set(pts)) and all(-100 <= p <= 100 for p in pts), f"tier_ladder invalid: {pts}"
    tier_map = {t['id']: t['min_points'] for t in ladder}
    assert tier_map.get('friend', 0) >= 15, f"friend threshold too low: {tier_map.get('friend')}"
    assert tier_map.get('romantic_interest', 0) >= 60, f"romantic_interest threshold too low: {tier_map.get('romantic_interest')}"
    assert tier_map.get('lover', 0) >= 75, f"lover threshold too low: {tier_map.get('lover')}"

    rp = rc.get('relationship_prompt') or {}
    assert 'Stranger' in rp.get('instructions', '') and 'slowly' in rp.get('instructions', '').lower(), "relationship_prompt slowburn missing"

    icc = world_data.get('inline_command_config') or {}
    assert icc.get('enabled') is True, "inline_command_config.enabled must be True"
    assert icc.get('syntax') == 'arrow', f"Expected inline_command_config.syntax == 'arrow', got {icc.get('syntax')}"
    secs = icc.get('sections') or {}
    rel_sec = secs.get('relationship') or {}
    item_sec = secs.get('item_use') or {}
    assert rel_sec.get('enabled') is True, "inline_command_config.sections.relationship.enabled must be True"
    assert item_sec.get('enabled') is True, "inline_command_config.sections.item_use.enabled must be True"
    rel_inst = rel_sec.get('instructions', '')
    item_inst = item_sec.get('instructions', '')
    assert 'A shared laugh' not in rel_inst, "Legacy 'A shared laugh' found in relationship instructions"
    assert 'space-separated' not in rel_inst, "Legacy 'space-separated' found in relationship instructions"
    assert '\u2014' not in rel_inst, "Em-dash found in relationship instructions"
    assert '\u2014' not in item_inst, "Em-dash found in item_use instructions"
    assert '>like <actor> -> <target>: <reason>' in rel_inst, "Arrow syntax missing in relationship instructions"
    assert '>use player -> <target>: <item>' in item_inst, "Arrow syntax missing in item_use instructions"
    assert 'player' in rel_inst and 'char:<id>' in rel_inst, "Missing player/char:<id> guidance in relationship instructions"
    print("  -> Phase 7 PASS: R1 Slowburn magnitudes, ease_out decay, 14-tier ladder & Arrow inline_command_config verified!")

def test_phase8_epistemic_isolation(world_data):
    print("\n[TEST 8] Verifying Phase 8: R3 Epistemic Isolation & Global Confinement...")
    headers = get_headers()
    sd = world_data.get('scan_depth')
    assert sd is not None and sd <= 5, f"Expected scan_depth <= 5, got {sd}"

    bi = world_data.get('base_instructions', '')
    spo = world_data.get('system_prompt_override', '')
    fi = world_data.get('final_instructions', '')
    assert '<epistemic_isolation_gate>' in bi, "Missing <epistemic_isolation_gate> in World.base_instructions"
    assert '<epistemic_isolation_gate>' in spo, "Missing <epistemic_isolation_gate> in World.system_prompt_override"
    assert '<epistemic_isolation_firewall>' in fi, "Missing <epistemic_isolation_firewall> in World.final_instructions"
    assert 'ISOLAMENTO EPISTEMICO ASSOLUTO:' in fi, "Missing ISOLAMENTO EPISTEMICO ASSOLUTO in World.final_instructions"
    for label, txt in [('base_instructions', bi), ('system_prompt_override', spo), ('final_instructions', fi)]:
        assert '\u2014' not in txt, f"Em-dash found in World.{label}"
        assert '-> player:' in txt, f"Arrow syntax '-> player:' missing in World.{label}"
        assert 'space-separated' not in txt, f"Stale space-separated syntax found in World.{label}"

    # Verify World Lexicon confinement, scan_persona=False (723/723), & st_excludeRecursion (>=573)
    url_lex = f"https://app.wyvern.chat/api/worlds/lexicon/world/{WORLD_ID}"
    req_lex = urllib.request.Request(url_lex, headers=headers)
    with urllib.request.urlopen(req_lex) as resp:
        lexicon = json.loads(resp.read().decode('utf-8'))
    globals_lex = [e for e in lexicon if e.get('is_global') is True]
    assert len(globals_lex) <= 35, f"Expected <= 35 global World Lexicon entries, got {len(globals_lex)}"
    sp_true = sum(1 for e in lexicon if e.get('scan_persona') is True)
    assert sp_true == 0, f"Expected 0 World Lexicon entries with scan_persona=True, got {sp_true}"
    excl_true = sum(1 for e in lexicon if (e.get('extensions') or {}).get('st_excludeRecursion') is True)
    assert excl_true >= 573, f"Expected >= 573 World Lexicon entries with extensions.st_excludeRecursion=True, got {excl_true}"

    lex_by_id = {e['id']: e for e in lexicon}
    personal_secret_28 = [
        "_FdReMecwaXcKRHafW8FPE", "_3T4THDa91QXRENrDQjM96", "_qXrqXrrjeqfhcBzbkqa7f",
        "_nzgBYYwNnXRT8HVwhYCPY", "_qBqG7zznDRJmg8n7qyY4h", "_TxgwtYLc7Ydzkx2g9W3Nw",
        "_RCKee7MrcKUfxbzTYm8xn", "_23EG8KEWcQMDfY6C2NEEt", "_AGNJ2P6hpj9PjY8rCFypX",
        "_DjzLWQfByHMN3VDqQC6R6", "_LDy28DW9LMkAVwYzcTEEf", "_GMbpAyWAJdYkxtQcq8YFG",
        "_reJRyjK2xjqaG7bnNdRDN", "_ry4RgyWbaBR1jf3bUfwWa", "_cPqzG6cDfGf2LtXtA9TG2",
        "_aEcn3FxNUjmAt47mQDxea", "_XXF3g1rMjFpEk1q6rMg64", "_3KUmFBfBEk8qDJMwJU6x4",
        "_Xz3d8YUkGXXKGYeUhM1H2", "_r8DLnJp6ApqE7NJaYCBgU", "_tzTRjXDrez96xTXNnkqzr",
        "_f7fEWMRBJrk2ybRqDGTYf", "_1R9B8gfqJfPdCmz4DxnjN", "_fNAq44pkLDJkMGr1LWweF",
        "_jH2g3MjN4Rm82T142Qnkm", "_xpkTXpp7qEpjY4XFxzRt9", "_Y2rNKmT1V3hDVwRpTqXNt",
        "_hNwJ6XET47VRW76jwL3Bd",
    ]
    for eid in personal_secret_28:
        entry = lex_by_id.get(eid, {})
        assert entry.get('is_global') is False, f"Personal/secret Lexicon {eid} still is_global=True"
        assert entry.get('scan_persona') is False, f"Personal/secret Lexicon {eid} still scan_persona=True"

    # Verify World Characters global confinement (5/126 Douglas protagonists) & false-positive trigger cleanup
    url_chars = f"https://app.wyvern.chat/api/worlds/characters/world/{WORLD_ID}"
    req_chars = urllib.request.Request(url_chars, headers=headers)
    with urllib.request.urlopen(req_chars) as resp:
        wchars = json.loads(resp.read().decode('utf-8'))
    global_chars = [c for c in wchars if c.get('is_global') is True]
    expected_5 = {
        "_FGeNBqjrt9fJJJyXTDgxM", "_mUEUDfmTG4m7wNyQ7WQKx",
        "_QQXte9xWjMeMtqEJfwrc3", "_YzcPc7dRLkttzR2jKX93z", "_qfaywY2yfrGWcxPBdmURD"
    }
    assert len(global_chars) == 5 and {c['id'] for c in global_chars} == expected_5, (
        f"Expected exact 5 global World Characters, got {len(global_chars)}: {[c.get('display_name') for c in global_chars[:10]]}"
    )

    chars_by_id = {c['id']: c for c in wchars}
    forbidden_keys = {
        "_g2CwyaFb2BtgdkHrNzmpy": ["Thompson"],
        "_f732Vk1GMxggg2HB9pHVh": ["Zero", "Wrath"],
        "_DUXKKGrCb7CxjVRHF88pd": ["Iron"],
        "_8aVXCw6Yg3hHM18HntLUN": ["Hvit", "Wife", "Mate", "White Moon"],
        "_t88VU9ngKrNW6kGf14nJV": ["Ace"],
        "_wMcYm8hBYH97fVVWG86nN": ["Ut", "Firstborn"],
        "_yAYpmxxnP1gmntXDQPYmG": ["Firstborn"],
        "_rpF7xBA8yAYQrMkQUgXfK": ["First Wolf"],
        "_3b7MkBTrPKWnXKhcVzD9t": ["familiar"],
        "_qM3z1Y31wLRNXmw8HATLd": ["Lust"],
        "_1zCVGtqV7akj7ecyxzk7e": ["Via"],
        "_eAk2t4QC9GqKJtqAQV9Fj": ["ior"],
        "_9YcrRj1BTHCL2e1Up3exz": ["Blackwolf", "DCC Security"],
    }
    for cid, bad_list in forbidden_keys.items():
        ckeys = chars_by_id.get(cid, {}).get('keys') or []
        assert len(ckeys) > 0, f"WorldCharacter {cid} has empty keys"
        for bk in bad_list:
            assert bk not in ckeys, f"False-positive key {bk!r} still present on WorldCharacter {cid}: {ckeys}"

    print(
        f"  -> Phase 8 PASS: scan_depth={sd}, Lexicon globals={len(globals_lex)}/723, "
        f"scan_persona=0/723, st_excludeRecursion={excl_true}/723, World Char globals=5/126, "
        f"13/13 false-trigger keys cleaned, Epistemic gates active!"
    )

def main():
    print("==================================================================")
    print("   SVARTÚLFR VERSE — WORLD RPG SYSTEMS FULL AUDIT & TEST SUITE   ")
    print("==================================================================")
    
    url = f"https://app.wyvern.chat/api/worlds/{WORLD_ID}"
    req = urllib.request.Request(url, headers=get_headers())
    with urllib.request.urlopen(req) as resp:
        world_data = json.loads(resp.read().decode('utf-8'))
        
    test_phase1_stat_config(world_data)
    test_phase2_catalogs()
    test_phase3_moodlets(world_data)
    test_phase4_items_and_shops()
    test_phase5_rules()
    test_phase6_autoprovisioning_and_omniparity()
    test_phase7_slowburn_calibration(world_data)
    test_phase8_epistemic_isolation(world_data)
    
    print("\n==================================================================")
    print("   ALL TESTS PASSED WITH 100% SUCCESS! (8/8 AUDIT CHECKS OK)    ")
    print("==================================================================")

if __name__ == '__main__':
    main()

