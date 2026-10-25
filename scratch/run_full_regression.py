import requests, json, pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

print('=== 1. VERIFYING SCENARIOS ===')
scenarios = [
    ('char_scenario_CKgwq246DyCj1NNTBV9rt', 'Alyssa Route', 7),
    ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'Jasper Route', 6)
]
for sid, name, expected_greetings in scenarios:
    r = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sid}', headers=headers)
    assert r.status_code == 200, f'{name} GET failed: {r.status_code}'
    d = r.json()
    assert len(d.get('greetings', [])) == expected_greetings, f'{name} greetings mismatch'
    slots = d.get('slots', [])
    assert len(slots) == 8, f'{name} slots count mismatch'
    for s in slots:
        sk = s.get('key')
        uc = s.get('unavailable_count', 0)
        assert uc == 0, f'{name} slot {sk} has unavailable_count: {uc}'
    print(f'  {name} verified: status 200, rev {d.get("revision")}, {len(slots)} slots (all unavailable_count=0), {len(d.get("greetings"))} greetings')

print('\n=== 2. VERIFYING LOREBOOKS ===')
# NPC Primary
r_prim = requests.get('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
assert r_prim.status_code == 200
prim_data = r_prim.json()
entries = prim_data.get('lexicon', prim_data.get('entries', []))
assert len(entries) == 99, f'Expected 99 entries in Primary, got {len(entries)}'

# Check 7 key characters in Primary
key_eids = {
    '4NzXF4_0hYxmN7Idltzpw': ('Scarlett Rose', 4777, ['_qXgBMbFYJfc84hbLHhe92'], []),
    'ijy8vrlphNv19-p-gbYuY': ('Sierra Cruz', 5117, ['_pnrXbkWqcgmFAf3meRWFY'], []),
    'YCxAqNoShpefVvk0_Pc7i': ("Russell 'Russ' Sinclair", 5505, ['_wn6DkCcg3Xqa2Xpx9ttnT'], []),
    'ekdQjq63xP7HtNuaPQJQE': ('Stanley Davies Jr.', 8008, ['_Xd3NhKnRJByMTtdb6PjxJ'], []),
    'RM6rcwv8MlY1XWaCTQp0M': ('Jared Thompson', 8696, ['_xJVPtBLL3dxy69RLKL9X9'], []),
    'alyssa_world_dossier_2b54a223': ('Alyssa Hvit Douglas Bloodmoon', 16957, ['_6exg3yPfe2eCDK4hTftkh'], ['persona_1786335754946']),
    'Vcj4h2TL4Usola2A4OOl6': ('Jasper Svartr Douglas Bloodmoon', 14483, ['_t4J9aQNJM36cUKAP4wB4U'], ['1792155173728'])
}
entry_map = {e.get('entry_id'): e for e in entries}
for eid, (exp_name, min_len, exp_chars, exp_personas) in key_eids.items():
    assert eid in entry_map, f'Missing entry {eid}'
    e = entry_map[eid]
    assert e.get('type') == 'npc', f'{exp_name} type is {e.get("type")}, expected npc'
    assert e.get('selective') is False, f'{exp_name} selective is {e.get("selective")}, expected False'
    assert len(e.get('content', '')) >= min_len, f'{exp_name} content len {len(e.get("content", ""))} < {min_len}'
    assert e.get('ignored_characters') == exp_chars, f'{exp_name} ignored_characters mismatch: {e.get("ignored_characters")}'
    assert e.get('ignored_personas') == exp_personas, f'{exp_name} ignored_personas mismatch: {e.get("ignored_personas")}'
    print(f'  {exp_name} ({eid}) verified: npc, selective=False, len={len(e.get("content"))}, ignored_chars={e.get("ignored_characters")}, ignored_personas={e.get("ignored_personas")}')

# Secondary (Edric)
r_sec = requests.get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers)
assert r_sec.status_code == 200
sec_entries = {e.get('entry_id'): e for e in r_sec.json().get('lexicon', [])}
edric = sec_entries.get('h-ttmlgJYeRXqyDvQjSX7')
assert edric is not None
assert edric.get('ignored_characters') == ['_TbRM3EdxDjHFgqztTbCpL']
print('  Edric Douglas in Secondary verified: ignored_characters=[_TbRM3EdxDjHFgqztTbCpL]')

print('\n=== 3. VERIFYING CHARACTERS ===')
r_chars = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
assert r_chars.status_code == 200
mine_chars = r_chars.json().get('characters', [])
assert len(mine_chars) == 8, f'Expected 8 cards in mine, got {len(mine_chars)}'
print(f'  /characters/mine has exactly {len(mine_chars)} cards:')
for c in mine_chars:
    print('   -', c.get('id'), '->', c.get('name'))

final_cards = sorted([f.name for f in (ROOT / 'FINAL').glob('*card.json')])
assert len(final_cards) == 8, f'Expected 8 card JSONs in FINAL/, got {len(final_cards)}'
print(f'  FINAL/ has exactly {len(final_cards)} cards')

arch_cards = sorted([f.name for f in (ROOT / 'ARCHIVIO' / 'cards_legacy').glob('*card.json')])
assert len(arch_cards) == 6, f'Expected 6 card JSONs in ARCHIVIO/cards_legacy/, got {len(arch_cards)}'
print(f'  ARCHIVIO/cards_legacy/ has exactly {len(arch_cards)} cards')

arch_scenarios = sorted([f.name for f in (ROOT / 'ARCHIVIO' / 'scenarios').glob('*.json')])
assert len(arch_scenarios) == 4, f'Expected 4 scenario JSONs in ARCHIVIO/scenarios/, got {len(arch_scenarios)}'
print(f'  ARCHIVIO/scenarios/ has exactly {len(arch_scenarios)} scenarios')

final_scenarios = sorted([f.name for f in (ROOT / 'FINAL' / 'scenarios').glob('*.json')])
assert len(final_scenarios) == 2, f'Expected 2 scenario JSONs in FINAL/scenarios/, got {len(final_scenarios)}'
print(f'  FINAL/scenarios/ has exactly {len(final_scenarios)} scenarios')

print('\n=== ALL REGRESSION CHECKS PASSED 100%! ===')
