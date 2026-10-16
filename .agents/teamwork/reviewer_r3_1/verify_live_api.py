import urllib.request
import urllib.error
import json
import pathlib
import time
import sys

WT_PATH = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt')
API_BASE = 'https://app.wyvern.chat/api'
PACING_DELAY = 2.5

TARGET_LOREBOOKS = [
    {
        'id': '_gwwCxCfQ6PQaLEjAQVpJL',
        'expected_entries': 219,
        'expected_name': 'Svartúlfr - Lorebook I',
        'is_npc': False,
    },
    {
        'id': '_HfG7TeV6MJyj6bxMwxkpt',
        'expected_entries': 143,
        'expected_name': 'Svartúlfr - Lorebook II',
        'is_npc': False,
    },
    {
        'id': '_9zWTGqYJNJ4BCDMj8gfcD',
        'expected_entries': 35,
        'expected_name': 'Svartúlfr - Lorebook III (SUCC & Underworld)',
        'is_npc': False,
    },
    {
        'id': '_EjXxkmPVhpCXg8xABpFkK',
        'expected_entries': 196,
        'expected_name': 'Svartúlfr - Location',
        'is_npc': False,
    },
    {
        'id': '_zwEqgEEzh12X6gHVmMKKC',
        'expected_entries': 106,
        'expected_name': 'Svartúlfr - NPC Primary',
        'is_npc': True,
    },
    {
        'id': '_Uht3Ckz44JBDrPnUHq7LV',
        'expected_entries': 310,
        'expected_name': 'Svartúlfr - NPC Secondary',
        'is_npc': True,
    },
]

def main():
    token = WT_PATH.read_text(encoding='utf-8').strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Reviewer-R3-Independent-Audit)'
    }

    results = []
    total_entries = 0
    total_age_macros = 0
    spurious_non_npc_metadata = 0
    npc_missing_avatar = 0
    npc_missing_regex = 0
    npc_umbrella_keys = 0

    BROAD_KEYS_CHECK = {"solarton", "succ", "blackwood", "vampire", "werewolf", "college", "student", "alpha", "omega", "pack leader", "blackwood council", "demon representative", "human representative"}

    print("======================================================================")
    print("INDEPENDENT LIVE WYVERN API AUDIT — REVIEWER R3")
    print("======================================================================")

    for idx, target in enumerate(TARGET_LOREBOOKS, start=1):
        lid = target['id']
        expected_cnt = target['expected_entries']
        expected_name = target['expected_name']
        is_npc_lb = target['is_npc']

        url = f'{API_BASE}/lorebooks/{lid}'
        req = urllib.request.Request(url, headers=headers, method='GET')
        t0 = time.time()

        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                status = resp.status
                elapsed = round(time.time() - t0, 3)
                data = json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            print(f"FAILED on {lid}: {e}")
            sys.exit(1)

        name = data.get('name')
        rating = data.get('rating')
        visibility = data.get('visibility')
        scan_depth = data.get('scan_depth')
        token_budget = data.get('token_budget')
        recursive_scanning = data.get('recursive_scanning')

        lexicon = data.get('lexicon', [])
        entries = data.get('entries', [])
        cnt = len(lexicon)
        total_entries += cnt

        print(f"[{idx}/6] {lid} -> HTTP {status} (elapsed {elapsed}s)")
        print(f"      Name: {name} (expected: {expected_name})")
        print(f"      Rating: {rating}, Visibility: {visibility}, Scan Depth: {scan_depth}, Token Budget: {token_budget}, Recursive: {recursive_scanning}")
        print(f"      Cloud Lexicon Count: {cnt} (expected: {expected_cnt}) | Cloud Entries Count: {len(entries)}")

        # Deep inspect entries
        for e in lexicon:
            text = json.dumps(e, ensure_ascii=False)
            if '{{age}}' in text:
                total_age_macros += 1
                print(f"      [ALERT] {lid} has residual {{{{age}}}}: {e.get('name') or e.get('comment')}")

            entry_type = (e.get('type') or '').lower()
            keys = [k.strip().lower() for k in e.get('keys', [])]
            secondary_keys = [k.strip().lower() for k in e.get('secondary_keys', [])]

            if is_npc_lb or entry_type == 'npc':
                # NPC checks
                avatar = e.get('avatar', '')
                if not avatar or not avatar.startswith('http'):
                    npc_missing_avatar += 1
                if not e.get('custom_avatar_regex') or e.get('lines_parsed') != 1 or not e.get('avatar_activation_regex'):
                    npc_missing_regex += 1
                for bk in BROAD_KEYS_CHECK:
                    if bk in keys:
                        # Check if it's exact compound name vs umbrella key
                        npc_umbrella_keys += 1
                        print(f"      [ALERT NPC BROAD KEY] {e.get('name') or e.get('comment')} has primary key: {bk}")
                    if bk in secondary_keys and bk == 'alpha':
                        npc_umbrella_keys += 1
                        print(f"      [ALERT NPC BROAD KEY] {e.get('name') or e.get('comment')} has secondary key: {bk}")
            else:
                # Non-NPC checks
                if 'npc_info' in e:
                    spurious_non_npc_metadata += 1
                if e.get('custom_avatar_regex') or e.get('lines_parsed') is not None or e.get('avatar_activation_regex'):
                    spurious_non_npc_metadata += 1
                if e.get('avatar') == "":
                    spurious_non_npc_metadata += 1

        match_count = (cnt == expected_cnt)
        match_name = (name == expected_name)
        results.append({
            'id': lid,
            'name': name,
            'status': status,
            'elapsed': elapsed,
            'count': cnt,
            'expected_count': expected_cnt,
            'match_count': match_count,
            'match_name': match_name,
            'rating': rating,
            'visibility': visibility
        })

        if idx < len(TARGET_LOREBOOKS):
            time.sleep(PACING_DELAY)

    print("\n----------------------------------------------------------------------")
    print("SUMMARY AUDIT REPORT:")
    print(f"Total Cloud Entries: {total_entries} (expected 1009)")
    print(f"Total Residual {{{{age}}}} Macros: {total_age_macros} (expected 0)")
    print(f"Spurious Non-NPC Metadata occurrences: {spurious_non_npc_metadata} (expected 0)")
    print(f"NPC Missing/Invalid Avatars: {npc_missing_avatar} (expected 0)")
    print(f"NPC Missing/Invalid Multiline Regex: {npc_missing_regex} (expected 0)")
    print(f"NPC Umbrella Keys found: {npc_umbrella_keys} (expected 0)")
    all_ok = (
        total_entries == 1009 and
        total_age_macros == 0 and
        spurious_non_npc_metadata == 0 and
        npc_missing_avatar == 0 and
        npc_missing_regex == 0 and
        npc_umbrella_keys == 0 and
        all(r['status'] == 200 and r['match_count'] for r in results)
    )
    print(f"ALL AUDIT CRITERIA MET: {all_ok}")
    print("======================================================================")

if __name__ == '__main__':
    main()
