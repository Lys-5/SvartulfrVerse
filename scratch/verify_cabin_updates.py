import json

def verify_file(filepath, expected_len):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    entries = data.get('entries', [])
    lexicon = data.get('lexicon', [])
    assert len(entries) == expected_len, f"{filepath} entries len {len(entries)} != {expected_len}"
    assert len(lexicon) == expected_len, f"{filepath} lexicon len {len(lexicon)} != {expected_len}"
    for i in range(expected_len):
        assert entries[i]['content'] == lexicon[i]['content'], f"Mismatch at idx {i} in {filepath}"
    print(f"SUCCESS: {filepath} passed length ({expected_len}) and entry==lexicon check.")

verify_file('FINAL/Svartulfr_Location.json', 225)
verify_file('FINAL/Svartulfr_NPC_Secondary.json', 211)

with open('FINAL/Svartulfr_Location.json', 'r', encoding='utf-8') as f:
    loc = json.load(f)

for idx in [209, 217, 223]:
    e = loc['entries'][idx]
    c = e['content']
    print(f"Checking Location idx {idx} ({e['comment']}):")
    print(f"  Em-dash count: {c.count('—')}")
    print(f"  Asterisk count: {c.count('*')}")
    print(f"  Keys: {e['keys']}")
    print(f"  Sec Keys: {e.get('secondary_keys')}")
    print(f"  Key logic: {e.get('key_logic')}")
    print(f"  Priority: {e.get('priority')}, Position: {e.get('position')}")

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    npc = json.load(f)

e = npc['entries'][151]
c = e['content']
print(f"Checking NPC idx 151 ({e['comment']}):")
print(f"  Em-dash count: {c.count('—')}")
print(f"  Asterisk count: {c.count('*')}")
for line in c.split('\n'):
    if 'AFFILIATION' in line or 'Lake Wolf' in line or 'Ironwood' in line:
        print("  ", line)
