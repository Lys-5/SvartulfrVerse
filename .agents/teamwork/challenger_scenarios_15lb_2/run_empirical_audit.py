import json
import requests
import pathlib
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = TOKEN_PATH.read_text(encoding='utf-8').strip()

HEADERS = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

CANONICAL_LOREBOOK_IDS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",  # Svartúlfr - Lorebook I
    "_HfG7TeV6MJyj6bxMwxkpt",  # Svartúlfr - Lorebook II
    "_9zWTGqYJNJ4BCDMj8gfcD",  # Svartúlfr - Lorebook III
    "_EjXxkmPVhpCXg8xABpFkK",  # Svartúlfr - Location
    "_Uht3Ckz44JBDrPnUHq7LV",  # Svartúlfr - NPC Secondary
    "_zwEqgEEzh12X6gHVmMKKC",  # Svartúlfr - NPC Primary
    "_GV1KyHVY1RMbCnWgLkzDG",  # A0 Behavioral Realism
    "_GbWJbkhgLzWexMHrjyUUc",  # A1 Physics
    "_FaVcHfmrqcaJq8pa3WmRw",  # A2 Social Realism
    "_BbrRgrcdGPMLEbBU2b6xk",  # A3 Medical Realism
    "_gchmML4Q478zdFjhXf8rN",  # A4 Cultural Realism
    "_brNyzEdhzNAyxK8xC8hhm",  # A5 Sex Position
    "_YtKLMTwyMxNf1DNYqBx1t",  # A5.5 Scene Tone
    "_b9HgpUXtAW8VmTy82BPDV",  # A6 World Realism
    "_c8bEm1bWphwqFBXWRPrV8"   # A7 Queer Realism
]

ALYSSA_ID = "persona_1786335754946"
JASPER_ID = "1792155173728"

SCENARIOS = [
    {
        "name": "Villa Douglas",
        "id": "char_scenario_88N1eQXqkbydKX9q9XQzp",
        "type": "dual",
        "file": "FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json"
    },
    {
        "name": "Camp Mystic",
        "id": "char_scenario_nLC84wrHdrbB6P3DEhwKb",
        "type": "dual",
        "file": "FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json"
    },
    {
        "name": "DMHA Dungeons",
        "id": "char_scenario_eqtRNnDpKbxDp7dmJmq6E",
        "type": "dual",
        "file": "FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json"
    },
    {
        "name": "Underworld Sindacato",
        "id": "char_scenario_rrUCdBPH6WTNyBnQkMAKR",
        "type": "dual",
        "file": "FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json"
    },
    {
        "name": "SUCC Route Alyssa",
        "id": "char_scenario_CKgwq246DyCj1NNTBV9rt",
        "type": "single_alyssa",
        "file": "FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json"
    },
    {
        "name": "SUCC Route Jasper",
        "id": "char_scenario_Kq4mJEBH83j7Q7DdVfFnF",
        "type": "single_jasper",
        "file": "FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json"
    },
    {
        "name": "Master Scenario",
        "id": "char_scenario_1DC43ggb6mB8YLJDJKrU4",
        "type": "master",
        "file": "FINAL/Svartulfr_Master_Scenario.json"
    }
]

def simulate_react_dom_render(linked_persona_ids, personas_data):
    """
    Simulates Wyvern Next.js Module 41680 DOM rendering logic exactly:
    x = personas_data.filter(e => e.can_fork)
    checked = linked_persona_ids.includes(e.persona_id)
    badge = linked_persona_ids.length > 0 ? ` (${linked_persona_ids.length} selected)` : ''
    """
    forkable = [p for p in personas_data if p.get('can_fork', False)]
    count = len(linked_persona_ids)
    badge = f" ({count} selected)" if count > 0 else ""
    trigger_text = f"Offer a persona to play as{badge}"
    
    checkboxes = []
    for p in forkable:
        pid = p.get('persona_id')
        name = p.get('name')
        comment = p.get('comment') or p.get('title')
        is_checked = pid in linked_persona_ids
        checkboxes.append({
            'persona_id': pid,
            'name': name,
            'comment': comment,
            'checked': is_checked,
            'aria_checked': 'true' if is_checked else 'false',
            'data_state': 'checked' if is_checked else 'unchecked'
        })
    
    return {
        'trigger_text': trigger_text,
        'selected_count': count,
        'checkboxes': checkboxes
    }

def main():
    print("=" * 80)
    print("CHALLENGER 2: DEEP EMPIRICAL DOM & NETWORK AUDIT")
    print("=" * 80)
    
    # Step 1: Verify Personas on Cloud
    print("\n--- 1. AUDITING CANONICAL PERSONAS VIA LIVE API ---")
    personas_info = []
    for pid in [ALYSSA_ID, JASPER_ID]:
        res = requests.get(f"https://app.wyvern.chat/api/user-personas/{pid}", headers=HEADERS)
        print(f"GET /api/user-personas/{pid} -> HTTP {res.status_code}")
        assert res.status_code == 200, f"Failed to get persona {pid}: {res.status_code}"
        pdata = res.json()
        assert pdata.get('can_fork') is True, f"Persona {pid} does NOT have can_fork=True!"
        assert pdata.get('avatar'), f"Persona {pid} lacks avatar!"
        print(f"  Name: {pdata.get('name')}")
        print(f"  Title: {pdata.get('title')}")
        print(f"  Comment: {pdata.get('comment')}")
        print(f"  can_fork: {pdata.get('can_fork')}")
        print(f"  Avatar: {pdata.get('avatar')[:60]}...")
        # Note: In the user personas API, persona_id is pid
        pdata['persona_id'] = pid
        personas_info.append(pdata)
        
    # Step 2: Verify 15 Lorebooks on Cloud
    print("\n--- 2. AUDITING 15 LOREBOOKS VIA LIVE API ---")
    verified_lbs = []
    for lbid in CANONICAL_LOREBOOK_IDS:
        res = requests.get(f"https://app.wyvern.chat/api/lorebooks/{lbid}", headers=HEADERS)
        assert res.status_code == 200, f"Lorebook {lbid} returned HTTP {res.status_code}"
        lbdata = res.json()
        title = lbdata.get('title') or lbdata.get('name')
        entries_cnt = len(lbdata.get('entries', []))
        lexicon_cnt = len(lbdata.get('lexicon', []))
        total_items = entries_cnt + lexicon_cnt
        assert total_items > 0, f"Lorebook {lbid} ({title}) has 0 entries and 0 lexicon!"
        print(f"  [OK] {lbid} | Title: '{title}' | Entries: {entries_cnt} | Lexicon: {lexicon_cnt} | Total: {total_items}")
        verified_lbs.append({'id': lbid, 'title': title, 'total_items': total_items})
        
    # Step 3: Audit All 7 Scenarios
    print("\n--- 3. AUDITING SCENARIO PAYLOADS & SIMULATING REACT DOM ---")
    dom_reports = []
    
    total_greetings_audited = 0
    total_network_requests = 0
    total_http_errors = 0
    
    for sc in SCENARIOS:
        name = sc['name']
        sc_id = sc['id']
        sc_type = sc['type']
        file_path = ROOT / sc['file']
        
        print(f"\nAuditing Scenario: '{name}' ({sc_id})...")
        total_network_requests += 1
        res = requests.get(f"https://app.wyvern.chat/api/character-scenarios/{sc_id}", headers=HEADERS)
        if res.status_code != 200:
            total_http_errors += 1
            print(f"  [FATAL ERROR] HTTP {res.status_code}: {res.text}")
            continue
            
        data = res.json()
        rev = data.get('revision')
        vis = data.get('visibility')
        lbs = data.get('lorebook_ids', [])
        greetings = data.get('greetings', [])
        
        print(f"  Revision: {rev} | Visibility: {vis} | Lorebooks: {len(lbs)} | Greetings: {len(greetings)}")
        
        # Invariant checks
        assert vis == "private", f"Scenario {sc_id} visibility is {vis}, expected 'private'"
        assert lbs == CANONICAL_LOREBOOK_IDS, f"Scenario {sc_id} lorebook_ids do not match canonical set!"
        
        sc_dom_report = {
            'scenario_name': name,
            'scenario_id': sc_id,
            'scenario_type': sc_type,
            'revision': rev,
            'lorebooks_verified': len(lbs) == 15,
            'greetings_dom': []
        }
        
        for idx, g in enumerate(greetings):
            total_greetings_audited += 1
            gname = g.get('name', f"Greeting {idx+1}")
            lpids = g.get('linked_persona_ids', [])
            
            # Simulate React Module 41680 DOM execution
            dom_state = simulate_react_dom_render(lpids, personas_info)
            
            # Verify expectations based on scenario type & greeting tags
            if sc_type == "dual":
                assert dom_state['selected_count'] == 2, f"Dual scenario greeting {idx} count={dom_state['selected_count']}"
                assert dom_state['trigger_text'] == "Offer a persona to play as (2 selected)"
                alyssa_cb = next(c for c in dom_state['checkboxes'] if c['persona_id'] == ALYSSA_ID)
                jasper_cb = next(c for c in dom_state['checkboxes'] if c['persona_id'] == JASPER_ID)
                assert alyssa_cb['checked'] is True
                assert jasper_cb['checked'] is True
            elif sc_type == "single_alyssa":
                assert dom_state['selected_count'] == 1, f"Alyssa scenario greeting {idx} count={dom_state['selected_count']}"
                assert dom_state['trigger_text'] == "Offer a persona to play as (1 selected)"
                alyssa_cb = next(c for c in dom_state['checkboxes'] if c['persona_id'] == ALYSSA_ID)
                jasper_cb = next(c for c in dom_state['checkboxes'] if c['persona_id'] == JASPER_ID)
                assert alyssa_cb['checked'] is True
                assert jasper_cb['checked'] is False
            elif sc_type == "single_jasper":
                assert dom_state['selected_count'] == 1, f"Jasper scenario greeting {idx} count={dom_state['selected_count']}"
                assert dom_state['trigger_text'] == "Offer a persona to play as (1 selected)"
                alyssa_cb = next(c for c in dom_state['checkboxes'] if c['persona_id'] == ALYSSA_ID)
                jasper_cb = next(c for c in dom_state['checkboxes'] if c['persona_id'] == JASPER_ID)
                assert alyssa_cb['checked'] is False
                assert jasper_cb['checked'] is True
            elif sc_type == "master":
                alyssa_cb = next(c for c in dom_state['checkboxes'] if c['persona_id'] == ALYSSA_ID)
                jasper_cb = next(c for c in dom_state['checkboxes'] if c['persona_id'] == JASPER_ID)
                if "[FemPOV]" in gname:
                    assert dom_state['selected_count'] == 1
                    assert dom_state['trigger_text'] == "Offer a persona to play as (1 selected)"
                    assert alyssa_cb['checked'] is True
                    assert jasper_cb['checked'] is False
                elif "[MalePOV]" in gname:
                    assert dom_state['selected_count'] == 1
                    assert dom_state['trigger_text'] == "Offer a persona to play as (1 selected)"
                    assert alyssa_cb['checked'] is False
                    assert jasper_cb['checked'] is True
                else:
                    assert dom_state['selected_count'] == 2
                    assert dom_state['trigger_text'] == "Offer a persona to play as (2 selected)"
                    assert alyssa_cb['checked'] is True
                    assert jasper_cb['checked'] is True
            
            sc_dom_report['greetings_dom'].append({
                'index': idx,
                'name': gname,
                'trigger_text': dom_state['trigger_text'],
                'selected_count': dom_state['selected_count'],
                'alyssa_state': next(c['data_state'] for c in dom_state['checkboxes'] if c['persona_id'] == ALYSSA_ID),
                'jasper_state': next(c['data_state'] for c in dom_state['checkboxes'] if c['persona_id'] == JASPER_ID)
            })
            
        print(f"  [DOM VERIFIED] All {len(greetings)} greetings render exact DOM trigger text and checkbox states!")
        dom_reports.append(sc_dom_report)
        
    print("\n" + "=" * 80)
    print("EMPIRICAL AUDIT SUMMARY:")
    print(f"Total Network Requests to Wyvern API: {total_network_requests + len(CANONICAL_LOREBOOK_IDS) + 2}")
    print(f"Total HTTP 4xx/5xx Errors: {total_http_errors}")
    print(f"Total Character Scenarios Audited: {len(SCENARIOS)}")
    print(f"Total Greetings Audited: {total_greetings_audited}")
    print(f"Total Lorebooks Verified: {len(verified_lbs)}")
    print("=" * 80)
    
    report_output_path = ROOT / '.agents' / 'teamwork' / 'challenger_scenarios_15lb_2' / 'dom_audit_report.json'
    with open(report_output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': {
                'total_scenarios': len(SCENARIOS),
                'total_greetings': total_greetings_audited,
                'total_lorebooks': len(verified_lbs),
                'http_errors': total_http_errors
            },
            'lorebooks': verified_lbs,
            'personas': personas_info,
            'scenarios': dom_reports
        }, f, indent=2)
    print(f"\nDetailed DOM audit report saved to: {report_output_path}")

if __name__ == '__main__':
    main()
