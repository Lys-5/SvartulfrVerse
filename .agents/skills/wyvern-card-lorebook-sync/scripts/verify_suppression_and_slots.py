import requests
import json
import pathlib
import sys

def verify_system(token_path='scratch/wyvern_token.txt'):
    token_file = pathlib.Path(token_path)
    if not token_file.exists():
        print(f"Error: Token file not found at {token_path}")
        return False

    token = token_file.read_text(encoding='utf-8').strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'AuditorBot/1.0',
        'Accept': 'application/json'
    }

    print("=== Wyvern Suppression & Slot Verification ===")
    
    # 1. Characters Mine
    try:
        r_mine = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
        if r_mine.status_code == 200:
            chars = r_mine.json().get('characters', [])
            print(f"[OK] /characters/mine: {len(chars)} active characters found")
            for c in chars:
                print(f"     - {c.get('id')}: {c.get('name')}")
        else:
            print(f"[FAIL] /characters/mine HTTP {r_mine.status_code}")
    except Exception as e:
        print(f"[ERROR] /characters/mine request: {e}")

    # 2. Check Scenarios
    scenarios = [
        ('char_scenario_CKgwq246DyCj1NNTBV9rt', 'SUCC Route Alyssa'),
        ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'SUCC Route Jasper')
    ]
    for sid, sname in scenarios:
        try:
            r_scen = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sid}', headers=headers)
            if r_scen.status_code == 200:
                data = r_scen.json()
                slots = data.get('slots', [])
                unavail = [s['key'] for s in slots if s.get('unavailable_count', 0) > 0]
                if not unavail:
                    print(f"[OK] Scenario {sname} ({sid}): rev {data.get('revision')}, {len(slots)} slots, all unavailable_count=0")
                else:
                    print(f"[WARN] Scenario {sname} has unavailable slots: {unavail}")
            else:
                print(f"[FAIL] Scenario {sname} HTTP {r_scen.status_code}")
        except Exception as e:
            print(f"[ERROR] Scenario {sname}: {e}")

    # 3. Check Primary Lorebook
    try:
        r_lb = requests.get('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
        if r_lb.status_code == 200:
            lb_data = r_lb.json()
            entries = lb_data.get('lexicon', lb_data.get('entries', []))
            print(f"[OK] Primary Lorebook: {len(entries)} entries found")
            # Verify Alyssa and Jasper
            for e in entries:
                eid = e.get('entry_id')
                if eid in ['alyssa_world_dossier_2b54a223', 'Vcj4h2TL4Usola2A4OOl6']:
                    name = e.get('name')
                    sel = e.get('selective')
                    ig_p = e.get('ignored_personas', [])
                    ig_c = e.get('ignored_characters', [])
                    print(f"     - {name} ({eid}): type={e.get('type')}, selective={sel}, ignored_personas={ig_p}, ignored_characters={ig_c}")
        else:
            print(f"[FAIL] Primary Lorebook HTTP {r_lb.status_code}")
    except Exception as e:
        print(f"[ERROR] Primary Lorebook: {e}")

    print("=== Verification Finished ===")
    return True

if __name__ == '__main__':
    verify_system()
