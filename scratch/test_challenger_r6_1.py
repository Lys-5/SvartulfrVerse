import json
import pathlib
import urllib.request
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'ChallengerBot/1.0',
    'Accept': 'application/json'
}

def api_get(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return e.code, None

print("=== CHALLENGER R6-1 EMPIRICAL AUDIT ===")

# Test 1: Query live Wyvern API for both scenarios
status_alyssa, alyssa = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_CKgwq246DyCj1NNTBV9rt')
status_jasper, jasper = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_Kq4mJEBH83j7Q7DdVfFnF')

print(f"Alyssa scenario status: {status_alyssa}, rev: {alyssa.get('revision')}")
print(f"Jasper scenario status: {status_jasper}, rev: {jasper.get('revision')}")

# Test 2: Inspect all greeting message texts
# Assert 0 occurrences of {{scenarioChar, 0 orphan macro tokens, 0 em-dashes
print("\n--- Inspecting Alyssa Greetings ---")
alyssa_scenarioChar_matches = []
alyssa_em_dash_matches = []
alyssa_orphan_macro_matches = []

macro_regex = re.compile(r'\{\{([^\}]+)\}\}')

for i, g in enumerate(alyssa.get('greetings', [])):
    # Check greeting content
    g_content = g.get('content', '')
    if '\u2014' in g_content:
        alyssa_em_dash_matches.append((i, 'greeting_content', g_content))
    for m_obj in macro_regex.finditer(g_content):
        tag = m_obj.group(1).strip()
        if 'scenarioChar' in tag:
            alyssa_scenarioChar_matches.append((i, 'greeting_content', tag))
        elif tag not in ['user', 'char']:
            alyssa_orphan_macro_matches.append((i, 'greeting_content', tag))

    for j, msg in enumerate(g.get('messages', [])):
        m_content = msg.get('content', '')
        if '\u2014' in m_content:
            alyssa_em_dash_matches.append((i, f'msg_{j}', m_content))
        for m_obj in macro_regex.finditer(m_content):
            tag = m_obj.group(1).strip()
            if 'scenarioChar' in tag:
                alyssa_scenarioChar_matches.append((i, f'msg_{j}', tag))
            elif tag not in ['user', 'char']:
                alyssa_orphan_macro_matches.append((i, f'msg_{j}', tag))

print(f"Alyssa {{scenarioChar occurrences: {len(alyssa_scenarioChar_matches)}")
for match in alyssa_scenarioChar_matches:
    print(f"  Greeting {match[0]} ({match[1]}): {match[2]}")
print(f"Alyssa em-dash occurrences: {len(alyssa_em_dash_matches)}")
print(f"Alyssa orphan macro occurrences: {len(alyssa_orphan_macro_matches)}")

print("\n--- Inspecting Jasper Greetings ---")
jasper_scenarioChar_matches = []
jasper_em_dash_matches = []
jasper_orphan_macro_matches = []

for i, g in enumerate(jasper.get('greetings', [])):
    g_content = g.get('content', '')
    if '\u2014' in g_content:
        jasper_em_dash_matches.append((i, 'greeting_content', g_content))
    for m_obj in macro_regex.finditer(g_content):
        tag = m_obj.group(1).strip()
        if 'scenarioChar' in tag:
            jasper_scenarioChar_matches.append((i, 'greeting_content', tag))
        elif tag not in ['user', 'char']:
            jasper_orphan_macro_matches.append((i, 'greeting_content', tag))

    for j, msg in enumerate(g.get('messages', [])):
        m_content = msg.get('content', '')
        if '\u2014' in m_content:
            jasper_em_dash_matches.append((i, f'msg_{j}', m_content))
        for m_obj in macro_regex.finditer(m_content):
            tag = m_obj.group(1).strip()
            if 'scenarioChar' in tag:
                jasper_scenarioChar_matches.append((i, f'msg_{j}', tag))
            elif tag not in ['user', 'char']:
                jasper_orphan_macro_matches.append((i, f'msg_{j}', tag))

print(f"Jasper {{scenarioChar occurrences: {len(jasper_scenarioChar_matches)}")
for match in jasper_scenarioChar_matches:
    print(f"  Greeting {match[0]} ({match[1]}): {match[2]}")
print(f"Jasper em-dash occurrences: {len(jasper_em_dash_matches)}")
print(f"Jasper orphan macro occurrences: {len(jasper_orphan_macro_matches)}")

# Test 3: Check all slots in both live scenarios (unavailable_count == 0)
print("\n--- Inspecting Slots Invariant (unavailable_count == 0) ---")
alyssa_slots = alyssa.get('slots', [])
jasper_slots = jasper.get('slots', [])

print(f"Alyssa slots count: {len(alyssa_slots)}")
for s in alyssa_slots:
    print(f"  Slot '{s.get('key')}': pool_len={len(s.get('pool', []))}, unavailable_count={s.get('unavailable_count')}")
    assert s.get('unavailable_count') == 0, f"Alyssa slot {s.get('key')} unavailable_count != 0"

print(f"Jasper slots count: {len(jasper_slots)}")
for s in jasper_slots:
    print(f"  Slot '{s.get('key')}': pool_len={len(s.get('pool', []))}, unavailable_count={s.get('unavailable_count')}")
    assert s.get('unavailable_count') == 0, f"Jasper slot {s.get('key')} unavailable_count != 0"

# Test 4: Verify speaker_slot invariant across all 13 greetings
print("\n--- Inspecting Speaker Slot Invariants ---")
alyssa_slot_keys = {s['key'] for s in alyssa_slots}
jasper_slot_keys = {s['key'] for s in jasper_slots}

print("Alyssa greetings (7 total):")
for i, g in enumerate(alyssa.get('greetings', [])):
    msg0 = g['messages'][0]
    print(f"  G{i} '{g.get('label')}': g.speaker_slot={g.get('speaker_slot')}, m0.speaker_slot={msg0.get('speaker_slot')}, msgs_len={len(g.get('messages', []))}")
    assert g['speaker_slot'] == msg0['speaker_slot'], f"Alyssa G{i} speaker_slot mismatch!"
    assert g['content'] == msg0['content'], f"Alyssa G{i} content mismatch!"
    assert g['speaker_slot'] in alyssa_slot_keys, f"Alyssa G{i} speaker_slot not in slots!"
    for j, m in enumerate(g.get('messages', [])):
        assert m.get('speaker_slot') in alyssa_slot_keys, f"Alyssa G{i} M{j} speaker_slot not in slots!"

print("Jasper greetings (6 total):")
for i, g in enumerate(jasper.get('greetings', [])):
    msg0 = g['messages'][0]
    print(f"  G{i} '{g.get('label')}': g.speaker_slot={g.get('speaker_slot')}, m0.speaker_slot={msg0.get('speaker_slot')}, msgs_len={len(g.get('messages', []))}")
    assert g['speaker_slot'] == msg0['speaker_slot'], f"Jasper G{i} speaker_slot mismatch!"
    assert g['content'] == msg0['content'], f"Jasper G{i} content mismatch!"
    assert g['speaker_slot'] in jasper_slot_keys, f"Jasper G{i} speaker_slot not in slots!"
    for j, m in enumerate(g.get('messages', [])):
        assert m.get('speaker_slot') in jasper_slot_keys, f"Jasper G{i} M{j} speaker_slot not in slots!"

# Test 5: Query live Wyvern API for Jared Thompson (_xJVPtBLL3dxy69RLKL9X9)
print("\n--- Querying Jared Thompson Card ---")
jared_status, jared_body = api_get('https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9')
print(f"Jared Thompson status: {jared_status} (expected: 404)")
assert jared_status == 404, f"Expected 404 for Jared, got {jared_status}"

# Test 6: Query /characters/mine (assert exactly 8 approved cards)
print("\n--- Querying /characters/mine ---")
mine_status, mine_body = api_get('https://app.wyvern.chat/api/characters/mine')
print(f"/characters/mine status: {mine_status}")
assert mine_status == 200, f"Expected 200, got {mine_status}"

mine_chars = mine_body.get('characters', [])
print(f"Total cards in /characters/mine: {len(mine_chars)}")
for c in mine_chars:
    print(f"  ID: {c.get('id')} | Name: {c.get('name')}")

approved_map = {
    '_QPea6g4Q1QfeYCVHCLMPR': 'Erik Ulfr Douglas',
    '_RDfz7XzTpM23LpPALVXHM': 'Malachia Björn Douglas Bloodmoon',
    '_t4J9aQNJM36cUKAP4wB4U': 'Jasper Svartr Douglas Bloodmoon',
    '_zFLUjV8aVxQRAfQxGcAcY': 'Noah Loki Douglas Bloodmoon',
    '_TbRM3EdxDjHFgqztTbCpL': 'Edric Douglas',
    '_T8Ywcr9FEqNf9JxbK6eHP': 'Logan Dominic Járn Douglas',
    '_HEQQbbRFwKdG8QE2Fh1z1': 'Wulfnic Báleygr Bloodmoon',
    '_zn24784jfcchQ7EwCyAnm': 'Mackenzie Sanchez-Rogers'
}

mine_ids = {c.get('id') for c in mine_chars}
assert mine_ids == set(approved_map.keys()), f"Mine IDs mismatch! Got {mine_ids}"
assert len(mine_chars) == 8, f"Expected 8 cards, got {len(mine_chars)}"

print("\n=== SUMMARY OF RESULTS ===")
print("All assertions evaluated.")
