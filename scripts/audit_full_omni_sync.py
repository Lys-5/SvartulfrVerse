"""
Comprehensive Audit Verification Script for Omni-Parity Across Svartulfr Verse
"""
import os
import sys
import json
import re
import urllib.request

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.sync_from_wyvern_web import get_auth_token

WORLD_ID = "_YpX47fNraQFw2dD7TdycJ"

def api_get(url, token):
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def main():
    token = get_auth_token()
    print("=" * 70)
    print("RUNNING COMPREHENSIVE OMNI-PARITY & RPG AUDIT")
    print("=" * 70)
    
    # 1. World Scenarios
    print("\n--- 1. AUDITING WORLD SCENARIOS ON API ---")
    w_scens = api_get(f"https://app.wyvern.chat/api/worlds/scenarios/world/{WORLD_ID}", token)
    print(f"Total World Scenarios on API: {len(w_scens)}")
    assert len(w_scens) >= 4, f"Expected at least 4 World Scenarios, found {len(w_scens)}"
    for s in w_scens:
        sid = s.get('id')
        name = s.get('name') or s.get('title')
        loc = (s.get('location') or {}).get('id') if isinstance(s.get('location'), dict) else (s.get('location') or s.get('location_id'))
        char_pool = s.get('included_character_pool', [])
        scenes = s.get('premade_scenes', [])
        print(f"  [OK] World Scenario: '{name}' (ID: {sid}) | Loc: {loc} | Chars: {len(char_pool)} | Scenes: {len(scenes)}")
        assert loc == "_aPqjQX8UBNTC9y2tEUdX3", f"Scenario {sid} location should be Lunar Quad, got {loc}"
        assert len(scenes) > 0, f"Scenario {sid} has no premade scenes"

    # 2. Standalone Character Scenarios
    print("\n--- 2. AUDITING STANDALONE CHARACTER SCENARIOS ON API ---")
    standalone_ids = [
        'char_scenario_CKgwq246DyCj1NNTBV9rt',
        'char_scenario_Kq4mJEBH83j7Q7DdVfFnF'
    ]
    for sid in standalone_ids:
        sc = api_get(f"https://app.wyvern.chat/api/character-scenarios/{sid}", token)
        name = sc.get('name')
        world_link = sc.get('linked_world_id')
        slots = sc.get('slots', [])
        script = sc.get('startup_script', '')
        print(f"  [OK] Standalone Scenario: '{name}' (ID: {sid}) | WorldLink: {world_link} | Slots: {len(slots)} | ScriptLen: {len(script)}")
        assert world_link == WORLD_ID, f"Scenario {sid} linked_world_id is {world_link}"
        assert len(script) > 500, f"Scenario {sid} startup_script too short or empty"
        assert "fbecc738-f9f7-4426-b8a1-a237b8ad922c" in script, "USD missing from script"
        assert "8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a" in script, "DMHA Cr missing from script"
        for slot in slots:
            assert slot.get('unavailable_count') == 0, f"Slot {slot.get('key')} has unavailable_count != 0"

    # 3. Lorebook NPC Secondary & Ariadne Cirillo
    print("\n--- 3. AUDITING LOREBOOK NPC SECONDARY & ARIADNE CIRILLO ---")
    sec_lb = api_get("https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV", token)
    lexicon = sec_lb.get('lexicon', sec_lb.get('entries', []))
    print(f"Total Secondary Lorebook entries on API: {len(lexicon)}")
    assert len(lexicon) == 211, f"Expected 211 entries, got {len(lexicon)}"
    
    ari = next((e for e in lexicon if 'Ariadne' in str(e.get('name'))), None)
    assert ari is not None, "Ariadne Cirillo not found in Secondary Lorebook"
    print(f"  [OK] Ariadne Cirillo found (Entry ID: {ari.get('entry_id') or ari.get('id')})")
    print(f"       Content length: {len(ari.get('content', ''))} chars")
    assert len(ari.get('content', '')) > 2000, f"Ariadne content truncated! Length: {len(ari.get('content', ''))}"
    assert "RPG STATS & TRAITS:" in ari.get('content', ''), "Ariadne missing RPG block"
    assert "—" not in ari.get('content', ''), "Em-dash found in Ariadne content"
    assert "{{age}}" not in ari.get('content', ''), "{{age}} macro found in Ariadne content"

    # 4. Local Final Files Parity
    print("\n--- 4. AUDITING LOCAL FINAL FILES PARITY ---")
    for fname in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
        fpath = os.path.join(ROOT_DIR, 'FINAL', fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        entries = d.get('entries', [])
        lex = d.get('lexicon', [])
        assert len(entries) == len(lex), f"{fname}: entries ({len(entries)}) != lexicon ({len(lex)})"
        print(f"  [OK] {fname}: {len(entries)} entries, entries == lexicon verified.")

    print("\n" + "=" * 70)
    print("ALL AUDIT CHECKS PASSED WITH 100% COMPLIANCE!")
    print("=" * 70)

if __name__ == '__main__':
    main()
