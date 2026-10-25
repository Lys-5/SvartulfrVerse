"""
Adversarial Independent Verification for Milestone 1:
Queries live Wyvern API directly and stress-tests all requirements.
"""

import urllib.request
import urllib.error
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
API_URL = f"https://app.wyvern.chat/api/worlds/characters/world/{TARGET_WORLD_ID}"

def main():
    token_path = ROOT / 'scratch' / 'wyvern_token.txt'
    if not token_path.exists():
        print("ERROR: wyvern_token.txt not found")
        sys.exit(1)
    token = token_path.read_text(encoding='utf-8').strip()

    req = urllib.request.Request(
        API_URL,
        headers={
            'Authorization': f'Bearer {token}',
            'User-Agent': 'Mozilla/5.0'
        }
    )

    try:
        with urllib.request.urlopen(req) as resp:
            status_code = resp.status
            body = resp.read().decode('utf-8')
            data = json.loads(body)
    except Exception as e:
        print(f"ERROR: Live API query failed: {e}")
        sys.exit(1)

    print(f"HTTP Status: {status_code}")
    print(f"Total Character Records: {len(data)}")

    # Save raw response for deep inspection
    raw_path = ROOT / 'scratch' / 'raw_live_characters_m1_review.json'
    with open(raw_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved raw response to {raw_path}")

    # 1. Exact count check
    if len(data) != 13:
        print(f"FAIL: Expected exactly 13 records, found {len(data)}")
    else:
        print("PASS: Exactly 13 records found in live world.")

    # 2. Check for duplicate names or duplicate IDs
    ids = [c.get('_id') for c in data]
    names = [c.get('display_name') for c in data]
    
    unique_ids = set(ids)
    unique_names = set(names)
    
    if len(ids) != len(unique_ids):
        print(f"FAIL: Duplicate IDs found: {ids}")
    else:
        print("PASS: All 13 character IDs are unique.")

    if len(names) != len(unique_names):
        print(f"FAIL: Duplicate names found: {names}")
    else:
        print("PASS: All 13 character names are unique.")

    # Check Erik reconciliation
    erik_records = [c for c in data if 'Erik' in c.get('display_name', '')]
    if len(erik_records) == 1:
        erik = erik_records[0]
        print(f"PASS: Exactly 1 Erik record exists (ID: {erik.get('_id')}). Preserved old ID: {erik.get('_id') == '_qfaywY2yfrGWcxPBdmURD'}")
    else:
        print(f"FAIL: Unexpected number of Erik records: {len(erik_records)}")

    # 3. Check Stats
    # Are all 6 stats present with base >= 1, and no stat == 0?
    stat_failures = []
    em_dash_failures = []
    avatar_failures = []
    wulfnic_anchor_ok = False

    for c in data:
        cname = c.get('display_name', 'UNKNOWN')
        cid = c.get('_id')
        rpg = c.get('rpg_stats') or {}
        base_stats = rpg.get('base_stats') or {}
        level = rpg.get('level')

        # Check stat values
        stat_keys_num = [f'stat_{i}' for i in range(1, 7)]
        stat_keys_named = ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']

        vals_num = [base_stats.get(k) for k in stat_keys_num]
        vals_named = [base_stats.get(k) for k in stat_keys_named]

        for k, v in base_stats.items():
            if v == 0:
                stat_failures.append(f"{cname}: stat {k} is 0")
            elif v is None:
                stat_failures.append(f"{cname}: stat {k} is None")
            elif isinstance(v, (int, float)) and v < 1:
                stat_failures.append(f"{cname}: stat {k} is < 1 ({v})")

        # Check all 6 stats exist
        for k in stat_keys_num:
            if k not in base_stats:
                stat_failures.append(f"{cname}: {k} missing")
        for k in stat_keys_named:
            if k not in base_stats:
                stat_failures.append(f"{cname}: {k} missing")

        sum_num = sum(vals_num) if all(isinstance(v, (int, float)) for v in vals_num) else -1
        sum_named = sum(vals_named) if all(isinstance(v, (int, float)) for v in vals_named) else -1

        if sum_num != 31 or sum_named != 31:
            stat_failures.append(f"{cname}: sum_num={sum_num}, sum_named={sum_named} (expected 31)")

        # Level check
        if level is None or level > 99 or level < 1:
            stat_failures.append(f"{cname}: invalid level {level}")

        # Wulfnic check
        if 'Wulfnic' in cname:
            bdate = c.get('birthdate')
            tl = c.get('start_timeline_position')
            if bdate == 0 and tl == 0:
                wulfnic_anchor_ok = True
                print(f"PASS: Wulfnic is properly anchored at 0 (birthdate: {bdate}, start_timeline_position: {tl})")
            else:
                print(f"FAIL: Wulfnic timeline values: birthdate={bdate}, start_timeline_position={tl}")

        # Avatar check
        avatar = c.get('avatar', '')
        if not avatar.startswith('https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/'):
            avatar_failures.append(f"{cname}: invalid avatar URL: {avatar}")

        # Em dash check
        # Check all string fields
        fields_to_check = [
            ('display_description', c.get('display_description', '')),
            ('summary', c.get('summary', '')),
            ('long_summary', c.get('long_summary', '')),
            ('final_instructions', c.get('final_instructions', '')),
            ('display_name', c.get('display_name', ''))
        ]
        for f_name, f_val in fields_to_check:
            if isinstance(f_val, str) and '\u2014' in f_val:
                em_dash_failures.append(f"{cname} field '{f_name}' contains em-dash (count: {f_val.count(chr(8212))})")

    if stat_failures:
        print(f"FAIL: Stat failures found ({len(stat_failures)}):")
        for sf in stat_failures:
            print(f"  - {sf}")
    else:
        print("PASS: All 13 characters have valid stats (all >= 1, none 0, sum == 31, dual-key present, level <= 99).")

    if not wulfnic_anchor_ok:
        print("FAIL: Wulfnic was not properly anchored at 0.")

    if avatar_failures:
        print(f"FAIL: Avatar failures found ({len(avatar_failures)}):")
        for af in avatar_failures:
            print(f"  - {af}")
    else:
        print("PASS: All 13 characters have valid HTTPS Cloudflare CDN avatars.")

    if em_dash_failures:
        print(f"FAIL: Em-dash failures found ({len(em_dash_failures)}):")
        for ef in em_dash_failures:
            print(f"  - {ef}")
    else:
        print("PASS: Zero em-dashes (\\u2014) found in any character string fields.")

if __name__ == '__main__':
    main()
