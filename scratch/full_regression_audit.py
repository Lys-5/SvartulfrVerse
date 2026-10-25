import json
import pathlib
import urllib.request
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'AuditorBot/1.0',
    'Accept': 'application/json'
}

def api_get(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return e.code, None

print("==================== FULL REGRESSION VERIFICATION ====================")

# 1. Characters Mine
status, mine_data = api_get('https://app.wyvern.chat/api/characters/mine')
assert status == 200, f"Expected 200, got {status}"
chars = mine_data.get('characters', [])
print(f"[CHECK 1] /characters/mine: status={status}, count={len(chars)}")
assert len(chars) == 8, f"Expected exactly 8 characters, got {len(chars)}"

approved_ids = {
    '_QPea6g4Q1QfeYCVHCLMPR': 'Erik Ulfr Douglas',
    '_RDfz7XzTpM23LpPALVXHM': 'Malachia Björn Douglas Bloodmoon',
    '_t4J9aQNJM36cUKAP4wB4U': 'Jasper Svartr Douglas Bloodmoon',
    '_zFLUjV8aVxQRAfQxGcAcY': 'Noah Loki Douglas Bloodmoon',
    '_TbRM3EdxDjHFgqztTbCpL': 'Edric Douglas',
    '_T8Ywcr9FEqNf9JxbK6eHP': 'Logan Dominic Járn Douglas',
    '_HEQQbbRFwKdG8QE2Fh1z1': 'Wulfnic Báleygr Bloodmoon',
    '_zn24784jfcchQ7EwCyAnm': 'Mackenzie Sanchez-Rogers'
}
live_ids = {c.get('id') for c in chars}
assert live_ids == set(approved_ids.keys())
print("  All 8 approved character IDs verified in /characters/mine.")

# 2. Jared Thompson Deletion
status, _ = api_get('https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9')
print(f"[CHECK 2] Jared Thompson card: status={status} (404 expected)")
assert status == 404, f"Expected 404 for deleted Jared, got {status}"

# 3. Alyssa Scenario
status, alyssa_sc = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_CKgwq246DyCj1NNTBV9rt')
print(f"[CHECK 3] Alyssa Scenario: status={status}, rev={alyssa_sc.get('revision')}, slots={len(alyssa_sc.get('slots', []))}, greetings={len(alyssa_sc.get('greetings', []))}")
assert status == 200
assert alyssa_sc.get('revision') == 11
assert len(alyssa_sc.get('slots', [])) == 8
assert len(alyssa_sc.get('greetings', [])) == 7
for s in alyssa_sc.get('slots', []):
    assert s.get('unavailable_count') == 0, f"Slot {s.get('key')} has unavailable_count != 0"
for i, g in enumerate(alyssa_sc.get('greetings', [])):
    assert g['speaker_slot'] == g['messages'][0]['speaker_slot'], f"Alyssa G{i} speaker_slot mismatch"
    assert g['content'] == g['messages'][0]['content'], f"Alyssa G{i} content mismatch"
    assert '\u2014' not in g['content'], f"Alyssa G{i} em-dash in content"
    for j, m in enumerate(g['messages']):
        assert '\u2014' not in m['content'], f"Alyssa G{i} M{j} em-dash in content"
        for ret in ['best_friend', 'roommate', 'friend', 'quarterback', 'childhood_friend', 'sports_rival']:
            assert f'{{{{scenarioChar "{ret}"}}}}' not in m['content'], f"Alyssa G{i} M{j} has {ret}"
print("  Alyssa Scenario: All slot invariants, greetings invariants, and macro replacements verified.")

# 4. Jasper Scenario
status, jasper_sc = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_Kq4mJEBH83j7Q7DdVfFnF')
print(f"[CHECK 4] Jasper Scenario: status={status}, rev={jasper_sc.get('revision')}, slots={len(jasper_sc.get('slots', []))}, greetings={len(jasper_sc.get('greetings', []))}")
assert status == 200
assert jasper_sc.get('revision') == 5
assert len(jasper_sc.get('slots', [])) == 8
assert len(jasper_sc.get('greetings', [])) == 6
for s in jasper_sc.get('slots', []):
    assert s.get('unavailable_count') == 0, f"Slot {s.get('key')} has unavailable_count != 0"
    assert len(s.get('pool', [])) == 0, f"Slot {s.get('key')} pool not empty"
for i, g in enumerate(jasper_sc.get('greetings', [])):
    assert g['speaker_slot'] == g['messages'][0]['speaker_slot'], f"Jasper G{i} speaker_slot mismatch"
    assert g['content'] == g['messages'][0]['content'], f"Jasper G{i} content mismatch"
    assert '\u2014' not in g['content'], f"Jasper G{i} em-dash in content"
    for j, m in enumerate(g['messages']):
        assert '\u2014' not in m['content'], f"Jasper G{i} M{j} em-dash in content"
        for ret in ['crush', 'male_roommate', 'friend', 'quarterback', 'childhood_friend', 'sports_rival', 'twin']:
            assert f'{{{{scenarioChar "{ret}"}}}}' not in m['content'], f"Jasper G{i} M{j} has {ret}"
print("  Jasper Scenario: All slot invariants, greetings invariants, and macro replacements verified.")

# 5. Lorebook Primary
status, lb_prim = api_get('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC')
print(f"[CHECK 5] Lorebook Primary: status={status}, entries={len(lb_prim.get('lexicon', []))}")
assert status == 200
assert len(lb_prim.get('lexicon', [])) == 99

check_prim_entries = {
    '4NzXF4_0hYxmN7Idltzpw': ('Scarlett Rose', 4777, ['_qXgBMbFYJfc84hbLHhe92'], []),
    'ijy8vrlphNv19-p-gbYuY': ('Sierra Cruz', 5117, ['_pnrXbkWqcgmFAf3meRWFY'], []),
    'YCxAqNoShpefVvk0_Pc7i': ("Russell 'Russ' Sinclair", 5505, ['_wn6DkCcg3Xqa2Xpx9ttnT'], []),
    'ekdQjq63xP7HtNuaPQJQE': ('Stanley Davies Jr.', 8008, ['_Xd3NhKnRJByMTtdb6PjxJ'], []),
    'RM6rcwv8MlY1XWaCTQp0M': ('Jared Thompson', 8696, ['_xJVPtBLL3dxy69RLKL9X9'], []),
    'alyssa_world_dossier_2b54a223': ('Alyssa Hvit Douglas Bloodmoon', 16957, ['_6exg3yPfe2eCDK4hTftkh'], ['persona_1786335754946']),
    'Vcj4h2TL4Usola2A4OOl6': ('Jasper Svartr Douglas Bloodmoon', 14483, ['_t4J9aQNJM36cUKAP4wB4U'], ['1792155173728']),
    'C-JisFj8qA1tsFEqZKevk': ('Erik Ulfr Douglas', 0, ['_QPea6g4Q1QfeYCVHCLMPR'], None),
    'jDuJtzirlEZC3K_ArIufh': ('Malachia Björn Douglas Bloodmoon', 0, ['_RDfz7XzTpM23LpPALVXHM'], None),
    'H2JX-NkHRiJ2FzoekC5ZZ': ('Noah Loki Douglas Bloodmoon', 0, ['_zFLUjV8aVxQRAfQxGcAcY'], None),
    'tAcrWLtWSDGf3xJJRwUOM': ('Logan Dominic Járn Douglas', 0, ['_T8Ywcr9FEqNf9JxbK6eHP'], None),
    'HhuMluMmIIENUei3bX6ed': ('Wulfnic Báleygr Bloodmoon', 0, ['_HEQQbbRFwKdG8QE2Fh1z1'], None),
    'BXi3sENAVYB8OKF80Q9Su': ('Mackenzie Sanchez-Rogers', 0, ['_zn24784jfcchQ7EwCyAnm'], None),
}

for eid, (name, min_desc, exp_chars, exp_personas) in check_prim_entries.items():
    entry = next(e for e in lb_prim['lexicon'] if e.get('entry_id') == eid)
    if min_desc > 0:
        assert len(entry.get('content', '')) >= min_desc, f"{name} content len too short"
        assert entry.get('type') == 'npc', f"{name} type != npc"
        assert entry.get('selective') is False, f"{name} selective != False"
        assert entry.get('custom_avatar_regex') is True, f"{name} custom_avatar_regex != True"
        assert entry.get('lines_parsed') == 1, f"{name} lines_parsed != 1"
        assert entry.get('avatar_activation_regex'), f"{name} missing avatar_activation_regex"
        assert entry.get('npc_info'), f"{name} missing npc_info"
    if exp_chars:
        assert entry.get('ignored_characters') == exp_chars, f"{name} ignored_characters mismatch: {entry.get('ignored_characters')} != {exp_chars}"
    if exp_personas is not None:
        assert entry.get('ignored_personas') == exp_personas, f"{name} ignored_personas mismatch: {entry.get('ignored_personas')} != {exp_personas}"
print("  Lorebook Primary: All 13 target entries verified with exact schema, native suppression, and descriptions.")

# 6. Lorebook Secondary
status, lb_sec = api_get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV')
print(f"[CHECK 6] Lorebook Secondary: status={status}, entries={len(lb_sec.get('lexicon', []))}")
assert status == 200
edric = next(e for e in lb_sec['lexicon'] if e.get('entry_id') == 'h-ttmlgJYeRXqyDvQjSX7')
assert edric.get('ignored_characters') == ['_TbRM3EdxDjHFgqztTbCpL']
print("  Lorebook Secondary: Edric Douglas native suppression verified.")

# 7. Local File System Checks
final_cards = sorted([f.name for f in (ROOT / 'FINAL').glob('*_card.json')])
arch_cards = sorted([f.name for f in (ROOT / 'ARCHIVIO' / 'cards_legacy').glob('*_card.json')])
final_sc = sorted([f.name for f in (ROOT / 'FINAL' / 'scenarios').glob('*.json')])
arch_sc = sorted([f.name for f in (ROOT / 'ARCHIVIO' / 'scenarios').glob('*.json')])

print(f"\n[CHECK 7] Local File System:")
print(f"  FINAL/ cards count: {len(final_cards)} (expected 8)")
assert len(final_cards) == 8
print(f"  ARCHIVIO/cards_legacy/ cards count: {len(arch_cards)} (expected 6)")
assert len(arch_cards) == 6
print(f"  FINAL/scenarios/ count: {len(final_sc)} (expected 2)")
assert len(final_sc) == 2
print(f"  ARCHIVIO/scenarios/ count: {len(arch_sc)} (expected 4)")
assert len(arch_sc) == 4

# Check synchronization between FINAL and lorebooks/optimized
for lb_name in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    f_txt = (ROOT / 'FINAL' / lb_name).read_text(encoding='utf-8')
    o_txt = (ROOT / 'lorebooks' / 'optimized' / lb_name).read_text(encoding='utf-8')
    assert f_txt == o_txt, f"{lb_name} mismatch between FINAL/ and lorebooks/optimized/"
    print(f"  FINAL/{lb_name} matches lorebooks/optimized/{lb_name} byte-for-byte.")

print("\n======================================================================")
print("100% OF ALL REGRESSION AUDIT CHECKS PASSED PERFECTLY!")
print("======================================================================")
