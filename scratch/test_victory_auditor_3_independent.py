import json
import pathlib
import re
import urllib.request
import urllib.error
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
API_BASE = 'https://app.wyvern.chat/api'

token = TOKEN_PATH.read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'VictoryAuditor3/1.0 (IndependentVerification)'
}

results = {
    'phase_a_timeline': {},
    'phase_b_integrity': {},
    'phase_c_execution': {},
    'failures': []
}

def fail(category, msg):
    print(f"[FAIL] {category}: {msg}")
    results['failures'].append(f"{category}: {msg}")

def success(category, msg):
    print(f"[PASS] {category}: {msg}")

def http_get(url):
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            data = resp.read()
            return status, json.loads(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return None, str(e)

print("=" * 70)
print("INDEPENDENT VICTORY AUDIT — Svartulfr Verse Scenario Sync & Card Reduction")
print("=" * 70)

# =========================================================================
# TEST SUITE 1: Live Wyvern API Verification
# =========================================================================
print("\n--- [1] Live Wyvern API Verification ---")

# 1.1 /api/characters/mine
status, data = http_get(f"{API_BASE}/characters/mine")
if status != 200:
    fail("API-CharactersMine", f"Expected HTTP 200, got {status}")
else:
    approved_cards = {
        '_QPea6g4Q1QfeYCVHCLMPR': 'Erik Ulfr Douglas',
        '_RDfz7XzTpM23LpPALVXHM': 'Malachia Björn Douglas Bloodmoon',
        '_t4J9aQNJM36cUKAP4wB4U': 'Jasper Svartr Douglas Bloodmoon',
        '_zFLUjV8aVxQRAfQxGcAcY': 'Noah Loki Douglas Bloodmoon',
        '_TbRM3EdxDjHFgqztTbCpL': 'Edric Douglas',
        '_T8Ywcr9FEqNf9JxbK6eHP': 'Logan Dominic Járn Douglas',
        '_HEQQbbRFwKdG8QE2Fh1z1': 'Wulfnic Báleygr Bloodmoon',
        '_zn24784jfcchQ7EwCyAnm': 'Mackenzie Sanchez-Rogers'
    }
    cards = data if isinstance(data, list) else data.get('characters', [])
    card_dict = {c.get('character_id') or c.get('id'): c.get('name') for c in cards}
    
    if len(cards) == 8:
        success("API-CharactersMine", f"Exactly 8 characters found in /characters/mine (HTTP 200)")
    else:
        fail("API-CharactersMine", f"Expected exactly 8 characters, got {len(cards)}: {list(card_dict.keys())}")
        
    mismatched = set(approved_cards.keys()) ^ set(card_dict.keys())
    if not mismatched:
        success("API-CharactersMine", f"All 8 approved character IDs match exact specification")
    else:
        fail("API-CharactersMine", f"Character ID mismatch: diff={mismatched}")

# 1.2 Deleted card Jared Thompson (_xJVPtBLL3dxy69RLKL9X9)
status, _ = http_get(f"{API_BASE}/characters/_xJVPtBLL3dxy69RLKL9X9")
if status == 404:
    success("API-DeletedCard", "Jared Thompson (_xJVPtBLL3dxy69RLKL9X9) returns HTTP 404 (authentic deletion)")
else:
    fail("API-DeletedCard", f"Expected HTTP 404 for Jared Thompson, got {status}")

# 1.3 Active Scenarios: Alyssa Route (char_scenario_CKgwq246DyCj1NNTBV9rt)
status, sc_alyssa = http_get(f"{API_BASE}/character-scenarios/char_scenario_CKgwq246DyCj1NNTBV9rt")
if status != 200:
    fail("API-ScenarioAlyssa", f"Expected HTTP 200, got {status}")
else:
    rev = sc_alyssa.get('revision', 0)
    success("API-ScenarioAlyssa", f"Alyssa Route HTTP 200, revision {rev}")
    if rev < 11:
        fail("API-ScenarioAlyssa", f"Expected revision >= 11, got {rev}")
        
    slots = sc_alyssa.get('slots', [])
    if len(slots) == 8:
        success("API-ScenarioAlyssa", f"All 8 slots present")
    else:
        fail("API-ScenarioAlyssa", f"Expected 8 slots, got {len(slots)}")
        
    bad_unavailable = [s['key'] for s in slots if s.get('unavailable_count', 0) != 0]
    if not bad_unavailable:
        success("API-ScenarioAlyssa", "All 8 slots have unavailable_count == 0")
    else:
        fail("API-ScenarioAlyssa", f"Slots with unavailable_count != 0: {bad_unavailable}")
        
    # Check retired slot pools are empty
    retired_keys = ['best_friend', 'roommate', 'childhood_friend', 'quarterback', 'friend', 'sports_rival']
    non_empty_retired = [s['key'] for s in slots if s['key'] in retired_keys and len(s.get('pool', [])) > 0]
    if not non_empty_retired:
        success("API-ScenarioAlyssa", "All retired NPC slots have pool: []")
    else:
        fail("API-ScenarioAlyssa", f"Retired slots with non-empty pool: {non_empty_retired}")
        
    # Check active slots have valid pools
    active_slots = {'twin': '_t4J9aQNJM36cUKAP4wB4U', 'crush': '_zn24784jfcchQ7EwCyAnm'}
    for skey, expected_cid in active_slots.items():
        slot_obj = next((s for s in slots if s['key'] == skey), None)
        if slot_obj and any(p.get('character_id') == expected_cid for p in slot_obj.get('pool', [])):
            success("API-ScenarioAlyssa", f"Active slot '{skey}' correctly retains card ID {expected_cid}")
        else:
            fail("API-ScenarioAlyssa", f"Active slot '{skey}' missing expected card ID {expected_cid}")
            
    # Check greetings
    greetings = sc_alyssa.get('greetings', [])
    if len(greetings) == 7:
        success("API-ScenarioAlyssa", "Exactly 7 greetings present")
    else:
        fail("API-ScenarioAlyssa", f"Expected 7 greetings, got {len(greetings)}")
        
    g0_name = greetings[0].get('name') or greetings[0].get('title') if greetings else None
    if g0_name == "SUCC Welcome Day":
        success("API-ScenarioAlyssa", "Greeting 0 is 'SUCC Welcome Day'")
    else:
        fail("API-ScenarioAlyssa", f"Greeting 0 title mismatch: {g0_name}")
        
    # Macro check in greetings
    raw_alyssa_str = json.dumps(sc_alyssa)
    retired_macros = [f'scenarioChar "{k}"' for k in retired_keys]
    found_macros = [m for m in retired_macros if m in raw_alyssa_str]
    if not found_macros:
        success("API-ScenarioAlyssa", "Zero orphaned macros for retired NPC slots")
    else:
        fail("API-ScenarioAlyssa", f"Found orphaned macros: {found_macros}")
        
    # Invariant: greeting.speaker_slot == messages[0].speaker_slot and greeting.content == messages[0].content
    inv_failures = []
    slot_keys = {s['key'] for s in slots}
    for idx, g in enumerate(greetings):
        msgs = g.get('messages', [])
        if not msgs:
            inv_failures.append(f"G{idx} has empty messages")
            continue
        if g.get('speaker_slot') != msgs[0].get('speaker_slot'):
            inv_failures.append(f"G{idx} speaker_slot mismatch: {g.get('speaker_slot')} != {msgs[0].get('speaker_slot')}")
        if g.get('content') != msgs[0].get('content'):
            inv_failures.append(f"G{idx} content mismatch with msgs[0]")
        for midx, m in enumerate(msgs):
            if m.get('speaker_slot') not in slot_keys:
                inv_failures.append(f"G{idx} msg{midx} invalid speaker_slot: {m.get('speaker_slot')}")
    if not inv_failures:
        success("API-ScenarioAlyssa", "All 7 greetings satisfy speaker_slot and message resolution invariants")
    else:
        fail("API-ScenarioAlyssa", f"Greeting invariant failures: {inv_failures}")

# 1.4 Active Scenarios: Jasper Route (char_scenario_Kq4mJEBH83j7Q7DdVfFnF)
status, sc_jasper = http_get(f"{API_BASE}/character-scenarios/char_scenario_Kq4mJEBH83j7Q7DdVfFnF")
if status != 200:
    fail("API-ScenarioJasper", f"Expected HTTP 200, got {status}")
else:
    rev = sc_jasper.get('revision', 0)
    success("API-ScenarioJasper", f"Jasper Route HTTP 200, revision {rev}")
    if rev < 5:
        fail("API-ScenarioJasper", f"Expected revision >= 5, got {rev}")
        
    slots = sc_jasper.get('slots', [])
    if len(slots) == 8:
        success("API-ScenarioJasper", f"All 8 slots present")
    else:
        fail("API-ScenarioJasper", f"Expected 8 slots, got {len(slots)}")
        
    bad_unavailable = [s['key'] for s in slots if s.get('unavailable_count', 0) != 0]
    if not bad_unavailable:
        success("API-ScenarioJasper", "All 8 slots have unavailable_count == 0")
    else:
        fail("API-ScenarioJasper", f"Slots with unavailable_count != 0: {bad_unavailable}")
        
    retired_keys_jasper = ['twin', 'male_roommate', 'crush', 'ai_companion', 'childhood_friend', 'quarterback', 'friend', 'sports_rival']
    non_empty_retired = [s['key'] for s in slots if s['key'] in retired_keys_jasper and len(s.get('pool', [])) > 0]
    if not non_empty_retired:
        success("API-ScenarioJasper", "All retired NPC slots have pool: []")
    else:
        fail("API-ScenarioJasper", f"Retired slots with non-empty pool: {non_empty_retired}")
        
    greetings = sc_jasper.get('greetings', [])
    if len(greetings) == 6:
        success("API-ScenarioJasper", "Exactly 6 greetings present")
    else:
        fail("API-ScenarioJasper", f"Expected 6 greetings, got {len(greetings)}")
        
    g0_name_j = greetings[0].get('name') or greetings[0].get('title') if greetings else None
    if g0_name_j == "SUCC Welcome Day":
        success("API-ScenarioJasper", "Greeting 0 is 'SUCC Welcome Day'")
    else:
        fail("API-ScenarioJasper", f"Greeting 0 title mismatch: {g0_name_j}")
        
    raw_jasper_str = json.dumps(sc_jasper)
    retired_macros = [f'scenarioChar "{k}"' for k in retired_keys_jasper]
    found_macros = [m for m in retired_macros if m in raw_jasper_str]
    if not found_macros:
        success("API-ScenarioJasper", "Zero orphaned macros for retired NPC slots")
    else:
        fail("API-ScenarioJasper", f"Found orphaned macros: {found_macros}")
        
    inv_failures = []
    slot_keys = {s['key'] for s in slots}
    for idx, g in enumerate(greetings):
        msgs = g.get('messages', [])
        if not msgs:
            inv_failures.append(f"G{idx} has empty messages")
            continue
        if g.get('speaker_slot') != msgs[0].get('speaker_slot'):
            inv_failures.append(f"G{idx} speaker_slot mismatch: {g.get('speaker_slot')} != {msgs[0].get('speaker_slot')}")
        if g.get('content') != msgs[0].get('content'):
            inv_failures.append(f"G{idx} content mismatch with msgs[0]")
        for midx, m in enumerate(msgs):
            if m.get('speaker_slot') not in slot_keys:
                inv_failures.append(f"G{idx} msg{midx} invalid speaker_slot: {m.get('speaker_slot')}")
    if not inv_failures:
        success("API-ScenarioJasper", "All 6 greetings satisfy speaker_slot and message resolution invariants")
    else:
        fail("API-ScenarioJasper", f"Greeting invariant failures: {inv_failures}")

# 1.5 Live Lorebook Primary (_zwEqgEEzh12X6gHVmMKKC)
status, lb_primary = http_get(f"{API_BASE}/lorebooks/_zwEqgEEzh12X6gHVmMKKC")
if status != 200:
    fail("API-LorebookPrimary", f"Expected HTTP 200, got {status}")
else:
    entries = lb_primary.get('lexicon', [])
    success("API-LorebookPrimary", f"Lorebook Primary returned HTTP 200 with {len(entries)} entries")
    if len(entries) != 99:
        fail("API-LorebookPrimary", f"Expected 99 entries, got {len(entries)}")
        
    target_npcs = {
        '4NzXF4_0hYxmN7Idltzpw': 'Scarlett Rose',
        'ijy8vrlphNv19-p-gbYuY': 'Sierra Cruz',
        'YCxAqNoShpefVvk0_Pc7i': "Russell 'Russ' Sinclair",
        'ekdQjq63xP7HtNuaPQJQE': 'Stanley Davies Jr.',
        'RM6rcwv8MlY1XWaCTQp0M': 'Jared Thompson',
        'alyssa_world_dossier_2b54a223': 'Alyssa Hvit Douglas Bloodmoon'
    }
    
    entries_by_id = {e.get('entry_id'): e for e in entries}
    for eid, name in target_npcs.items():
        entry = entries_by_id.get(eid)
        if not entry:
            fail("API-LorebookPrimary", f"Target NPC {name} ({eid}) missing in live Lorebook")
            continue
        content = entry.get('content', '')
        if len(content) < 2000:
            fail("API-LorebookPrimary", f"{name} content length < 2000 chars ({len(content)})")
        else:
            success("API-LorebookPrimary", f"{name} has full JED+ description ({len(content)} chars)")
            
        if entry.get('type') != 'npc':
            fail("API-LorebookPrimary", f"{name} type is '{entry.get('type')}', expected 'npc'")
            
        avatar = entry.get('avatar', '')
        if not (avatar.startswith('https://') and ('imagedelivery.net' in avatar or 'janitorai.com' in avatar)):
            fail("API-LorebookPrimary", f"{name} invalid avatar: {avatar}")
            
        if not entry.get('custom_avatar_regex') or entry.get('lines_parsed') != 1:
            fail("API-LorebookPrimary", f"{name} custom_avatar_regex or lines_parsed invalid")
            
        regex = entry.get('avatar_activation_regex', '')
        if not (r'(?:^|\n)\s*' in regex and ':' in regex):
            fail("API-LorebookPrimary", f"{name} avatar_activation_regex invalid: {regex}")
            
        npc_info = entry.get('npc_info')
        if not (isinstance(npc_info, dict) and npc_info.get('first_name')):
            fail("API-LorebookPrimary", f"{name} npc_info missing or invalid")
            
        # Suppression checks
        if eid == 'alyssa_world_dossier_2b54a223':
            # Alyssa should have ignored_personas containing persona_1786335754946
            if 'persona_1786335754946' in entry.get('ignored_personas', []):
                success("API-LorebookPrimary", "Alyssa has native persona collision protection (ignored_personas)")
            else:
                fail("API-LorebookPrimary", f"Alyssa missing 'persona_1786335754946' in ignored_personas: {entry.get('ignored_personas')}")
            if '_6exg3yPfe2eCDK4hTftkh' in entry.get('ignored_characters', []):
                success("API-LorebookPrimary", "Alyssa has card collision protection (ignored_characters)")
            else:
                fail("API-LorebookPrimary", f"Alyssa missing card ID in ignored_characters")

# Check Jasper in Primary too
jasper_entry = next((e for e in entries if e.get('entry_id') == 'Vcj4h2TL4Usola2A4OOl6'), None)
if jasper_entry:
    if '1792155173728' in jasper_entry.get('ignored_personas', []) and '_t4J9aQNJM36cUKAP4wB4U' in jasper_entry.get('ignored_characters', []):
        success("API-LorebookPrimary", "Jasper has native suppression configured (ignored_personas and ignored_characters)")
    else:
        fail("API-LorebookPrimary", "Jasper missing native suppression IDs")
else:
    fail("API-LorebookPrimary", "Jasper entry Vcj4h2TL4Usola2A4OOl6 missing")

# 1.6 Live Lorebook Secondary (_Uht3Ckz44JBDrPnUHq7LV)
status, lb_secondary = http_get(f"{API_BASE}/lorebooks/_Uht3Ckz44JBDrPnUHq7LV")
if status != 200:
    fail("API-LorebookSecondary", f"Expected HTTP 200, got {status}")
else:
    sec_entries = lb_secondary.get('lexicon', [])
    success("API-LorebookSecondary", f"Lorebook Secondary returned HTTP 200 with {len(sec_entries)} entries")
    if len(sec_entries) != 211:
        fail("API-LorebookSecondary", f"Expected 211 entries, got {len(sec_entries)}")

# =========================================================================
# TEST SUITE 2: Local Filesystem Integrity & Mirroring
# =========================================================================
print("\n--- [2] Local Filesystem Integrity & Mirroring ---")

# 2.1 FINAL/scenarios vs ARCHIVIO/scenarios
final_scenarios = [p.name for p in (ROOT / 'FINAL' / 'scenarios').glob('*.json')]
expected_final_sc = ['Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'Svartulfr_Scenario_SUCC_Route_Jasper.json']
if sorted(final_scenarios) == sorted(expected_final_sc):
    success("FS-Scenarios", f"FINAL/scenarios contains exactly the 2 active SUCC scenarios: {final_scenarios}")
else:
    fail("FS-Scenarios", f"FINAL/scenarios mismatch: expected {expected_final_sc}, found {final_scenarios}")

archived_scenarios = [p.name for p in (ROOT / 'ARCHIVIO' / 'scenarios').glob('*.json')]
expected_archived_sc = [
    'Svartulfr_Scenario_Camp_Mystic.json',
    'Svartulfr_Scenario_DMHA_Dungeons.json',
    'Svartulfr_Scenario_Underworld_Sindacato.json',
    'Svartulfr_Scenario_Villa_Douglas.json'
]
if sorted(archived_scenarios) == sorted(expected_archived_sc):
    success("FS-Scenarios", f"ARCHIVIO/scenarios contains exactly the 4 retired scenarios: {archived_scenarios}")
else:
    fail("FS-Scenarios", f"ARCHIVIO/scenarios mismatch: expected {expected_archived_sc}, found {archived_scenarios}")

# 2.2 FINAL/ character cards vs ARCHIVIO/cards_legacy
final_cards = [p.name for p in (ROOT / 'FINAL').glob('*_card.json')]
expected_final_cards = [
    'Edric_Douglas_card.json',
    'Erik_Douglas_card.json',
    'Jasper_Douglas_Bloodmoon_card.json',
    'Logan_Douglas_card.json',
    'Mackenzie_Sanchez_Rogers_card.json',
    'Malachia_Douglas_Bloodmoon_card.json',
    'Noah_Douglas_Bloodmoon_card.json',
    'Wulfnic_Bloodmoon_card.json'
]
if sorted(final_cards) == sorted(expected_final_cards):
    success("FS-Cards", f"FINAL contains exactly the 8 approved cards: {final_cards}")
else:
    fail("FS-Cards", f"FINAL cards mismatch: expected {expected_final_cards}, found {final_cards}")

archived_cards = [p.name for p in (ROOT / 'ARCHIVIO' / 'cards_legacy').glob('*.json')]
expected_archived_cards = [
    'Alyssa_Douglas_Bloodmoon_card.json',
    'Jared_Thompson_card.json',
    'Russ_card.json',
    'Scarlett_Rose_card.json',
    'Sierra_Cruz_card.json',
    'Stan_Davies_Jr_card.json'
]
if sorted(archived_cards) == sorted(expected_archived_cards):
    success("FS-Cards", f"ARCHIVIO/cards_legacy contains exactly the 6 retired cards: {archived_cards}")
else:
    fail("FS-Cards", f"ARCHIVIO/cards_legacy mismatch: expected {expected_archived_cards}, found {archived_cards}")

# 2.3 Parity between FINAL and lorebooks/optimized for NPC Primary
local_primary_path = ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json'
opt_primary_path = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json'
if local_primary_path.exists() and opt_primary_path.exists():
    lp = json.loads(local_primary_path.read_text(encoding='utf-8'))
    op = json.loads(opt_primary_path.read_text(encoding='utf-8'))
    if len(lp.get('lexicon', [])) == len(op.get('lexicon', [])) == 99:
        success("FS-Parity", "FINAL/Svartulfr_NPC_Primary and lorebooks/optimized have identical 99 entries")
    else:
        fail("FS-Parity", f"Length mismatch: FINAL={len(lp.get('lexicon', []))}, opt={len(op.get('lexicon', []))}")
    if len(lp.get('entries', [])) == len(lp.get('lexicon', [])):
        success("FS-Parity", "FINAL/Svartulfr_NPC_Primary entries and lexicon arrays have identical count (99)")
    else:
        fail("FS-Parity", f"entries ({len(lp.get('entries', []))}) != lexicon ({len(lp.get('lexicon', []))})")
else:
    fail("FS-Parity", "Missing Svartulfr_NPC_Primary.json in FINAL or lorebooks/optimized")

# =========================================================================
# TEST SUITE 3: Formatting & Repository Discipline
# =========================================================================
print("\n--- [3] Formatting & Discipline Checks ---")

# 3.1 Em-dash check in FINAL/scenarios/*.json
for p in (ROOT / 'FINAL' / 'scenarios').glob('*.json'):
    content = p.read_text(encoding='utf-8')
    if '\u2014' in content or '—' in content:
        fail("Format-EmDash", f"Em-dash detected in {p.name}")
    else:
        success("Format-EmDash", f"Zero em-dashes in {p.name}")

# 3.2 Broad keywords check on NPC entries in Svartulfr_NPC_Primary and Secondary
broad_keys = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}
for fname in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb_data = json.loads((ROOT / 'FINAL' / fname).read_text(encoding='utf-8'))
    violations = []
    for e in lb_data.get('lexicon', []):
        if e.get('type') == 'npc':
            keys_lower = {k.lower() for k in e.get('keys', [])}
            hit = keys_lower & broad_keys
            if hit:
                violations.append(f"{e.get('name')} ({e.get('entry_id')}): {hit}")
    if not violations:
        success("Discipline-BroadKeys", f"Zero umbrella keywords on NPC entries in {fname}")
    else:
        fail("Discipline-BroadKeys", f"Umbrella keywords on NPCs in {fname}: {violations[:5]}")

print("\n" + "=" * 70)
print(f"AUDIT SUMMARY: {len(results['failures'])} failures detected.")
if results['failures']:
    print("FAILED ASSERTIONS:")
    for f in results['failures']:
        print(f"  - {f}")
else:
    print("ALL INDEPENDENT VERIFICATION ASSERTIONS PASSED WITH 100% SUCCESS.")
print("=" * 70)
