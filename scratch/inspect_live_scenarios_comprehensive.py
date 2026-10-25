import requests
import json
import pathlib
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

ALYSSA_ID = "char_scenario_CKgwq246DyCj1NNTBV9rt"
JASPER_ID = "char_scenario_Kq4mJEBH83j7Q7DdVfFnF"

def run_inspection():
    token_file = ROOT / 'scratch' / 'wyvern_token.txt'
    token = token_file.read_text(encoding='utf-8').strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    scenarios = [
        {
            'name': 'Alyssa Route',
            'id': ALYSSA_ID,
            'local_path': ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json',
            'expected_greetings': 7,
            'expected_slots': ['twin', 'childhood_friend', 'best_friend']
        },
        {
            'name': 'Jasper Route',
            'id': JASPER_ID,
            'local_path': ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json',
            'expected_greetings': 6,
            'expected_slots': ['twin', 'childhood_friend', 'crush']
        }
    ]

    all_passed = True

    print("======================================================================")
    print("COMPREHENSIVE HTTP & API LIVE INSPECTION OF SUCC SCENARIOS")
    print("======================================================================")

    for sc in scenarios:
        name = sc['name']
        sc_id = sc['id']
        local_path = sc['local_path']
        exp_count = sc['expected_greetings']
        exp_slots = sc['expected_slots']

        print(f"\n[INSPECTING] {name} ({sc_id})...")
        
        # 1. Fetch remote live state
        url = f"https://app.wyvern.chat/api/character-scenarios/{sc_id}"
        resp = requests.get(url, headers=headers)
        assert resp.status_code == 200, f"HTTP status failed: {resp.status_code}"
        remote = resp.json()

        # 2. Read local state
        with open(local_path, 'r', encoding='utf-8') as f:
            local = json.load(f)

        remote_greetings = remote.get('greetings', [])
        local_greetings = local.get('greetings', [])

        print(f"  HTTP Status: 200 OK")
        print(f"  Remote Revision: {remote.get('revision')}, Local Revision: {local.get('revision')}")
        print(f"  Remote Greetings: {len(remote_greetings)}, Local Greetings: {len(local_greetings)}")

        # Check counts
        if len(remote_greetings) != exp_count:
            print(f"  FAIL: Expected {exp_count} greetings, found {len(remote_greetings)}")
            all_passed = False
        else:
            print(f"  PASS: Greeting count is exactly {exp_count}")

        # Check Greeting 0
        g0 = remote_greetings[0]
        print(f"  Greeting 0 Name: '{g0.get('name')}'")
        if g0.get('name') != "SUCC Welcome Day":
            print(f"  FAIL: Expected 'SUCC Welcome Day', got '{g0.get('name')}'")
            all_passed = False
        else:
            print("  PASS: Greeting 0 titled 'SUCC Welcome Day'")

        if g0.get('speaker_slot') != exp_slots[0]:
            print(f"  FAIL: Expected speaker_slot '{exp_slots[0]}', got '{g0.get('speaker_slot')}'")
            all_passed = False
        else:
            print(f"  PASS: Greeting 0 speaker_slot == '{exp_slots[0]}'")

        msgs = g0.get('messages', [])
        if len(msgs) != 3:
            print(f"  FAIL: Expected 3 messages, got {len(msgs)}")
            all_passed = False
        else:
            print("  PASS: 3 messages in Greeting 0")

        actual_slots = [m.get('speaker_slot') for m in msgs]
        if actual_slots != exp_slots:
            print(f"  FAIL: Expected message slots {exp_slots}, got {actual_slots}")
            all_passed = False
        else:
            print(f"  PASS: Message slots match exactly: {actual_slots}")

        # Invariants check
        if g0.get('speaker_slot') != msgs[0].get('speaker_slot'):
            print("  FAIL: Invariant violation: greeting.speaker_slot != messages[0].speaker_slot")
            all_passed = False
        else:
            print("  PASS: Invariant holds: greeting.speaker_slot == messages[0].speaker_slot")

        if g0.get('content') != msgs[0].get('content'):
            print("  FAIL: Invariant violation: greeting.content != messages[0].content")
            all_passed = False
        else:
            print("  PASS: Invariant holds: greeting.content == messages[0].content")

        # Required lore mentions
        g0_text = " ".join([m.get('content', '') for m in msgs]) + " " + g0.get('description', '')
        required_mentions = [
            ("August 26, 2024", "Date August 26, 2024"),
            ("Lunar Quad", "Location Lunar Quad"),
            ("Chancellor Archer Wolfwood", "Chancellor Archer Wolfwood"),
            ("SUCC", "SUCC Campus")
        ]
        for term, label in required_mentions:
            if term not in g0_text:
                print(f"  FAIL: Missing mention of {label}")
                all_passed = False
            else:
                print(f"  PASS: Verified {label}")

        # Main stage speech mention
        has_speech = "speech" in g0_text.lower() or "address" in g0_text.lower()
        has_stage = "stage" in g0_text.lower()
        if not (has_speech and has_stage):
            print("  FAIL: Missing mention of speech on main stage")
            all_passed = False
        else:
            print("  PASS: Verified Archer Wolfwood preparing speech on main stage")

        # Formatting discipline on all greetings
        em_dash_violations = 0
        asterisk_violations = 0
        quote_violations = 0
        for g_i, gr in enumerate(remote_greetings):
            for m_i, msg in enumerate(gr.get('messages', [])):
                txt = msg.get('content', '')
                if '—' in txt:
                    em_dash_violations += 1
                    print(f"    VIOLATION (em-dash): g[{g_i}] m[{m_i}]")
                if '*' in txt:
                    asterisk_violations += 1
                    print(f"    VIOLATION (asterisk): g[{g_i}] m[{m_i}]")
                if '"' in txt and txt.count('"') % 2 != 0:
                    quote_violations += 1
                    print(f"    VIOLATION (quotes): g[{g_i}] m[{m_i}]")

        if em_dash_violations == 0 and asterisk_violations == 0 and quote_violations == 0:
            print("  PASS: Zero formatting violations across all remote greetings (0 em-dash, 0 asterisks, balanced quotes)")
        else:
            print(f"  FAIL: Formatting violations (em-dash: {em_dash_violations}, asterisk: {asterisk_violations}, quotes: {quote_violations})")
            all_passed = False

        # Parity check between local and remote greetings
        if len(local_greetings) == len(remote_greetings):
            for idx in range(len(local_greetings)):
                assert local_greetings[idx]['name'] == remote_greetings[idx]['name']
                assert local_greetings[idx]['speaker_slot'] == remote_greetings[idx]['speaker_slot']
                assert local_greetings[idx]['content'] == remote_greetings[idx]['content']
            print("  PASS: Full parity confirmed between local and remote greetings")

    print("\n======================================================================")
    if all_passed:
        print("ALL ACCEPTANCE CRITERIA VERIFIED AND PASSED!")
    else:
        print("SOME VERIFICATIONS FAILED!")
        sys.exit(1)
    print("======================================================================")

if __name__ == "__main__":
    run_inspection()
