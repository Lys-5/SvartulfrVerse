import json

dual_files = [
    ('Villa Douglas', 'FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json', 5),
    ('Camp Mystic', 'FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json', 4),
    ('DMHA Dungeons', 'FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json', 4),
    ('Underworld Sindacato', 'FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json', 4),
]

for name, fpath, expected_len in dual_files:
    with open(fpath, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    greetings = d['greetings']
    assert len(greetings) == expected_len
    for i, g in enumerate(greetings):
        pids = g.get('linked_persona_ids')
        assert pids == ['persona_1786335754946', '1792155173728'] or pids == ['1792155173728', 'persona_1786335754946'], f'{name} g[{i}] failed: {pids}'
    print(f'[OK] {name}: {len(greetings)} greetings all have dual personas')

with open('FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'r', encoding='utf-8') as fp:
    d = json.load(fp)
assert len(d['greetings']) == 6
for i, g in enumerate(d['greetings']):
    assert g.get('linked_persona_ids') == ['persona_1786335754946'], f"Alyssa g[{i}] failed: {g.get('linked_persona_ids')}"
print('[OK] SUCC Route Alyssa: 6 greetings all have Alyssa persona only')

with open('FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json', 'r', encoding='utf-8') as fp:
    d = json.load(fp)
assert len(d['greetings']) == 5
for i, g in enumerate(d['greetings']):
    assert g.get('linked_persona_ids') == ['1792155173728'], f"Jasper g[{i}] failed: {g.get('linked_persona_ids')}"
print('[OK] SUCC Route Jasper: 5 greetings all have Jasper persona only')

with open('FINAL/Svartulfr_Master_Scenario.json', 'r', encoding='utf-8') as fp:
    d = json.load(fp)
greetings = d['greetings']
assert len(greetings) == 29
fem_cnt = 0
male_cnt = 0
shared_cnt = 0
for i, g in enumerate(greetings):
    pids = g.get('linked_persona_ids')
    gname = g.get('name', '')
    if '[FemPOV]' in gname:
        assert pids == ['persona_1786335754946'], f"Master FemPOV g[{i}] failed: {pids}"
        fem_cnt += 1
    elif '[MalePOV]' in gname:
        assert pids == ['1792155173728'], f"Master MalePOV g[{i}] failed: {pids}"
        male_cnt += 1
    else:
        assert set(pids) == {'persona_1786335754946', '1792155173728'}, f"Master shared g[{i}] failed: {pids}"
        shared_cnt += 1

assert fem_cnt == 7, f'FemPOV count {fem_cnt} != 7'
assert male_cnt == 6, f'MalePOV count {male_cnt} != 6'
assert shared_cnt == 16, f'Shared count {shared_cnt} != 16'
print(f'[OK] Master Scenario: 29 greetings verified (Shared={shared_cnt}, FemPOV={fem_cnt}, MalePOV={male_cnt})')

print("\n--- MASTER SCENARIO GREETINGS DETAIL ---")
with open('FINAL/Svartulfr_Master_Scenario.json', 'r', encoding='utf-8') as fp:
    d = json.load(fp)
for i, g in enumerate(d['greetings']):
    print(f"{i:02d} | {g.get('linked_persona_ids')} | {g.get('name')}")
