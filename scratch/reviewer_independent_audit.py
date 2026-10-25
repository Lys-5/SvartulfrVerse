import json
import pathlib
import requests

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

CANONICAL_LOREBOOK_IDS = [
    '_gwwCxCfQ6PQaLEjAQVpJL',  # Svartúlfr - Lorebook I
    '_HfG7TeV6MJyj6bxMwxkpt',  # Svartúlfr - Lorebook II
    '_9zWTGqYJNJ4BCDMj8gfcD',  # Svartúlfr - Lorebook III
    '_EjXxkmPVhpCXg8xABpFkK',  # Svartúlfr - Location
    '_Uht3Ckz44JBDrPnUHq7LV',  # Svartúlfr - NPC Secondary
    '_zwEqgEEzh12X6gHVmMKKC',  # Svartúlfr - NPC Primary
    '_GV1KyHVY1RMbCnWgLkzDG',  # A0 Behavioral Realism
    '_GbWJbkhgLzWexMHrjyUUc',  # A1 Physics
    '_FaVcHfmrqcaJq8pa3WmRw',  # A2 Social Realism
    '_BbrRgrcdGPMLEbBU2b6xk',  # A3 Medical Realism
    '_gchmML4Q478zdFjhXf8rN',  # A4 Cultural Realism
    '_brNyzEdhzNAyxK8xC8hhm',  # A5 Sex Position
    '_YtKLMTwyMxNf1DNYqBx1t',  # A5.5 Scene Tone
    '_b9HgpUXtAW8VmTy82BPDV',  # A6 World Realism
    '_c8bEm1bWphwqFBXWRPrV8'   # A7 Queer Realism
]

ALYSSA_PERSONA_ID = 'persona_1786335754946'
JASPER_PERSONA_ID = '1792155173728'

SCENARIOS = [
    ('Villa Douglas', ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_Villa_Douglas.json', 'char_scenario_88N1eQXqkbydKX9q9XQzp', 'dual', 5),
    ('Camp Mystic', ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_Camp_Mystic.json', 'char_scenario_nLC84wrHdrbB6P3DEhwKb', 'dual', 4),
    ('DMHA Dungeons', ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_DMHA_Dungeons.json', 'char_scenario_eqtRNnDpKbxDp7dmJmq6E', 'dual', 4),
    ('Underworld Sindacato', ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_Underworld_Sindacato.json', 'char_scenario_rrUCdBPH6WTNyBnQkMAKR', 'dual', 4),
    ('SUCC Route Alyssa', ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'char_scenario_CKgwq246DyCj1NNTBV9rt', 'alyssa', 6),
    ('SUCC Route Jasper', ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json', 'char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'jasper', 5),
    ('Master Scenario', ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json', 'char_scenario_1DC43ggb6mB8YLJDJKrU4', 'master', 29),
]

token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json',
    'User-Agent': 'ReviewerAgent/1.0'
}

print('=== STARTING INDEPENDENT FORENSIC AUDIT ===')
total_greetings_audited = 0
em_dash_violations = []

for name, path, sc_id, mode, exp_greetings in SCENARIOS:
    print(f'\n--- Auditing: {name} ({sc_id}) ---')
    assert path.exists(), f'File not found: {path}'
    with open(path, 'r', encoding='utf-8') as f:
        local_raw = f.read()
        local_data = json.loads(local_raw)

    # Check em-dash
    if '\u2014' in local_raw:
        em_dash_violations.append((name, 'local_raw contains em-dash'))

    # Local Lorebook checks
    lb_ids = local_data.get('lorebook_ids', [])
    assert len(lb_ids) == 15, f'{name}: local lorebook count {len(lb_ids)} != 15'
    assert lb_ids == CANONICAL_LOREBOOK_IDS, f'{name}: local lorebooks order mismatch'
    print('  [PASS] Local Lorebooks: 15/15 EXACT canonical match')

    # Visibility check
    vis = local_data.get('visibility')
    assert vis == 'private', f'{name}: visibility is {vis}, expected private'
    print(f'  [PASS] Local Visibility: {vis}')

    # Local Greetings check
    greetings = local_data.get('greetings', [])
    assert len(greetings) == exp_greetings, f'{name}: greetings count {len(greetings)} != {exp_greetings}'
    print(f'  [PASS] Local Greetings Count: {len(greetings)} (expected {exp_greetings})')

    dual_cnt = 0
    alyssa_cnt = 0
    jasper_cnt = 0

    for idx, g in enumerate(greetings):
        total_greetings_audited += 1
        pids = g.get('linked_persona_ids', [])
        gname = g.get('name', f'Greeting {idx}')
        
        # Check em-dash in greeting
        g_str = json.dumps(g, ensure_ascii=False)
        if '\u2014' in g_str:
            em_dash_violations.append((name, f'Greeting {idx} ({gname}) contains em-dash'))

        if mode == 'dual':
            assert set(pids) == {ALYSSA_PERSONA_ID, JASPER_PERSONA_ID}, f'Greeting {idx} invalid pids: {pids}'
            dual_cnt += 1
        elif mode == 'alyssa':
            assert pids == [ALYSSA_PERSONA_ID], f'Greeting {idx} invalid pids: {pids}'
            alyssa_cnt += 1
        elif mode == 'jasper':
            assert pids == [JASPER_PERSONA_ID], f'Greeting {idx} invalid pids: {pids}'
            jasper_cnt += 1
        elif mode == 'master':
            if '[FemPOV]' in gname:
                assert pids == [ALYSSA_PERSONA_ID], f'FemPOV greeting {idx} invalid pids: {pids}'
                alyssa_cnt += 1
            elif '[MalePOV]' in gname:
                assert pids == [JASPER_PERSONA_ID], f'MalePOV greeting {idx} invalid pids: {pids}'
                jasper_cnt += 1
            else:
                assert set(pids) == {ALYSSA_PERSONA_ID, JASPER_PERSONA_ID}, f'Shared greeting {idx} invalid pids: {pids}'
                dual_cnt += 1

    print(f'  [PASS] Local Greetings Persona Distribution: Dual={dual_cnt}, Alyssa={alyssa_cnt}, Jasper={jasper_cnt}')

    # Live API Check
    resp = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sc_id}', headers=headers)
    assert resp.status_code == 200, f'Live API returned {resp.status_code}'
    live_data = resp.json()

    live_rev = live_data.get('revision')
    loc_rev = local_data.get('revision')
    assert live_rev == loc_rev, f'Revision mismatch: live={live_rev} vs local={loc_rev}'
    assert live_data.get('visibility') == 'private', f'Live visibility is {live_data.get("visibility")}'
    live_lbs = live_data.get('lorebook_ids', [])
    assert len(live_lbs) == 15, f'Live lorebooks count {len(live_lbs)} != 15'
    assert live_lbs == CANONICAL_LOREBOOK_IDS, f'Live lorebooks mismatch canonical order'
    
    live_greetings = live_data.get('greetings', [])
    assert len(live_greetings) == exp_greetings, f'Live greetings count {len(live_greetings)} != {exp_greetings}'
    
    for idx, (lg, vg) in enumerate(zip(greetings, live_greetings)):
        assert lg.get('linked_persona_ids') == vg.get('linked_persona_ids'), f'Greeting {idx} persona mismatch between local and live'

    print(f'  [PASS] Live API: HTTP 200, Rev {live_rev}, 15 LBs matched, Greetings matched')

print(f'\nTotal Greetings Audited: {total_greetings_audited}')
print(f'Em-dash Violations: {len(em_dash_violations)}')
if em_dash_violations:
    for v in em_dash_violations:
        print('  VIOLATION:', v)
else:
    print('Zero em-dash violations found!')
print('\n=== AUDIT COMPLETE: ALL ASSERTIONS PASSED ===')
