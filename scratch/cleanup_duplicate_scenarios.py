import urllib.request
import json
import time

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': 'Bearer ' + token,
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json'
}

CANONICAL_WHITELIST = {
    'char_scenario_1DC43ggb6mB8YLJDJKrU4', # Master Omnibus
    'char_scenario_88N1eQXqkbydKX9q9XQzp', # Villa Douglas
    'char_scenario_rrUCdBPH6WTNyBnQkMAKR', # Underworld Sindacato
    'char_scenario_Kq4mJEBH83j7Q7DdVfFnF', # SUCC Jasper Route
    'char_scenario_CKgwq246DyCj1NNTBV9rt', # SUCC Alyssa Route
    'char_scenario_eqtRNnDpKbxDp7dmJmq6E', # DMHA Dungeons
    'char_scenario_nLC84wrHdrbB6P3DEhwKb', # Camp Mystic
}

DUPLICATES_TO_DELETE = [
    # Batch 1 (17:43 UTC)
    'char_scenario_WdajqL3eJtT3GydxhDRT4',
    'char_scenario_kw42g8J3NjBfKf7QW8zAG',
    'char_scenario_Mfxz4Ym8QaECU6MjfmWG3',
    'char_scenario_664yrxUXYwNUUJfyf7da7',
    'char_scenario_8GtdBd6dU7tPF481ekrKe',
    # Batch 2 (20:51 UTC)
    'char_scenario_T7pEVxFkq6U7RRH4EXbRR',
    'char_scenario_MNR6jXtPRQARNzkRf2PyW',
    'char_scenario_VNNPz6mVrfqeyfndzwzbP',
    'char_scenario_dcpMDF2W8ecgDhhw3nKLj',
    'char_scenario_hcDjXtBKbL3PBRFmAB7ed',
    'char_scenario_kdjkFrpR1TBLte7ykUDyL',
]

print("=== STARTING DELETION OF 11 DUPLICATE SCENARIOS ===")

for idx, sid in enumerate(DUPLICATES_TO_DELETE):
    if sid in CANONICAL_WHITELIST:
        print(f"SAFETY ABORT: {sid} is in canonical whitelist!")
        continue

    url = f"https://app.wyvern.chat/api/character-scenarios/{sid}"
    req = urllib.request.Request(url, headers=headers, method='DELETE')
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode('utf-8')
            print(f"[{idx+1}/{len(DUPLICATES_TO_DELETE)}] Deleted {sid} -> HTTP {resp.status} ({body})")
    except Exception as e:
        print(f"[{idx+1}/{len(DUPLICATES_TO_DELETE)}] Error deleting {sid}: {e}")
    time.sleep(1.5)

print("\n=== POST-CLEANUP VERIFICATION VIA GET /api/character-scenarios/mine ===")
ver_url = "https://app.wyvern.chat/api/character-scenarios/mine?limit=50"
req_ver = urllib.request.Request(ver_url, headers=headers)
with urllib.request.urlopen(req_ver, timeout=15) as resp:
    data = json.loads(resp.read().decode('utf-8'))

remaining = data.get('items', [])
print(f"Total remaining scenarios: {data.get('total')} (Items returned: {len(remaining)})")

for idx, sc in enumerate(remaining):
    sid = sc.get('id')
    name = sc.get('name')
    is_whitelisted = sid in CANONICAL_WHITELIST
    print(f"  {idx+1}. [{sid}] '{name}' -> Whitelisted: {is_whitelisted}")

assert data.get('total') == 7, f"Expected 7 scenarios, got {data.get('total')}"
print("\nSUCCESS: Exactly 7 canonical scenarios remain active on Wyvern!")
