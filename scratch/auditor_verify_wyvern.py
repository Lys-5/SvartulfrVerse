import urllib.request
import urllib.error
import json
import pathlib
import time
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
FINAL_DIR = ROOT / 'FINAL'

LOREBOOKS = [
    {
        'id': '_gwwCxCfQ6PQaLEjAQVpJL',
        'file': 'Svartulfr_Lorebook_I.json',
        'expected_entries': 219,
        'title': 'Svartúlfr - Lorebook I',
        'is_npc': False
    },
    {
        'id': '_HfG7TeV6MJyj6bxMwxkpt',
        'file': 'Svartulfr_Lorebook_II.json',
        'expected_entries': 143,
        'title': 'Svartúlfr - Lorebook II',
        'is_npc': False
    },
    {
        'id': '_9zWTGqYJNJ4BCDMj8gfcD',
        'file': 'Svartulfr_Lorebook_III.json',
        'expected_entries': 35,
        'title': 'Svartúlfr - Lorebook III (SUCC & Underworld)',
        'is_npc': False
    },
    {
        'id': '_EjXxkmPVhpCXg8xABpFkK',
        'file': 'Svartulfr_Location.json',
        'expected_entries': 196,
        'title': 'Svartúlfr - Location',
        'is_npc': False
    },
    {
        'id': '_zwEqgEEzh12X6gHVmMKKC',
        'file': 'Svartulfr_NPC_Primary.json',
        'expected_entries': 106,
        'title': 'Svartúlfr - NPC Primary',
        'is_npc': True
    },
    {
        'id': '_Uht3Ckz44JBDrPnUHq7LV',
        'file': 'Svartulfr_NPC_Secondary.json',
        'expected_entries': 310,
        'title': 'Svartúlfr - NPC Secondary',
        'is_npc': True
    },
]

BROAD_KEYS = {
    "solarton", "succ", "blackwood", "vampire", "werewolf", "college", 
    "student", "alpha", "omega", "cums", "hex valley", "demi-human", 
    "demihuman", "human", "anthro", "beastfolk"
}

def audit():
    token = WT_PATH.read_text(encoding='utf-8').strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'AuditorBot/1.0'
    }

    results = []
    total_entries_count = 0
    spurious_npc_count = 0
    umbrella_keys_found = []
    age_macro_count = 0
    invalid_npc_avatar_count = 0
    content_mismatches = 0

    print("=" * 70)
    print("INDEPENDENT FORENSIC AUDIT: LIVE WYVERN API QUERY")
    print("=" * 70)

    for idx, lb in enumerate(LOREBOOKS, start=1):
        lid = lb['id']
        expected = lb['expected_entries']
        title = lb['title']
        fname = lb['file']
        is_npc_lb = lb['is_npc']

        url = f'https://app.wyvern.chat/api/lorebooks/{lid}'
        req = urllib.request.Request(url, headers=headers, method='GET')
        
        t0 = time.time()
        with urllib.request.urlopen(req, timeout=30) as resp:
            elapsed = time.time() - t0
            status = resp.status
            resp_headers = dict(resp.headers)
            body = resp.read().decode('utf-8')
            data = json.loads(body)

        lexicon = data.get('lexicon', [])
        entries = data.get('entries', [])
        actual_count = len(lexicon)
        total_entries_count += actual_count

        print(f"\n[{idx}/6] {title} ({lid})")
        print(f"  HTTP Status: {status}")
        print(f"  Response Latency: {elapsed:.3f}s")
        print(f"  Cloud Lexicon entries: {actual_count} (expected: {expected})")
        print(f"  Server Date Header: {resp_headers.get('Date', 'N/A')}")
        print(f"  Content-Type: {resp_headers.get('Content-Type', 'N/A')}")

        # Check parity with local file
        local_data = json.loads((FINAL_DIR / fname).read_text(encoding='utf-8'))
        local_lexicon = local_data.get('lexicon', [])
        
        if len(local_lexicon) != actual_count:
            print(f"  [ERROR] Parity mismatch! Local {len(local_lexicon)} vs Cloud {actual_count}")
            content_mismatches += 1

        # Check individual entries in cloud response
        for entry in lexicon:
            # Pillar 1 check on non-NPC
            if not is_npc_lb:
                # check if spurious fields exist
                if 'npc_info' in entry:
                    spurious_npc_count += 1
                if entry.get('custom_avatar_regex') is True:
                    spurious_npc_count += 1
                if 'lines_parsed' in entry:
                    spurious_npc_count += 1
            else:
                # Pillar 2 check on NPC
                keys = entry.get('keys', [])
                for k in keys:
                    if k.strip().lower() in BROAD_KEYS:
                        umbrella_keys_found.append((entry.get('name', 'Unknown'), k))
                
                # Pillar 4 check on NPC
                avatar = entry.get('avatar', '')
                if not avatar or not isinstance(avatar, str) or not avatar.startswith('http'):
                    invalid_npc_avatar_count += 1
                if entry.get('custom_avatar_regex') is not True:
                    invalid_npc_avatar_count += 1
                if entry.get('lines_parsed') != 1:
                    invalid_npc_avatar_count += 1

            # Pillar 3 check
            text = entry.get('text', '')
            keys_str = " ".join(entry.get('keys', []))
            if '{{age}}' in text.lower() or '{{age}}' in keys_str.lower():
                age_macro_count += 1

        results.append({
            'id': lid,
            'title': title,
            'status': status,
            'latency': round(elapsed, 3),
            'cloud_count': actual_count,
            'expected_count': expected,
            'pass': (status == 200 and actual_count == expected)
        })

        # Pacing delay
        time.sleep(2.5)

    print("\n" + "=" * 70)
    print("AUDIT SUMMARY RESULTS:")
    print("=" * 70)
    print(f"Total Cloud Entries Verified: {total_entries_count} / 1009")
    print(f"Spurious NPC metadata found on non-NPC entries: {spurious_npc_count}")
    print(f"Umbrella keywords on NPC trigger keys: {len(umbrella_keys_found)} {umbrella_keys_found}")
    print(f"Residual {{age}} macros found: {age_macro_count}")
    print(f"Invalid NPC avatar/regex entries: {invalid_npc_avatar_count}")
    print(f"Content parity mismatches: {content_mismatches}")

    out_record = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'total_entries_count': total_entries_count,
        'results': results,
        'spurious_npc_count': spurious_npc_count,
        'umbrella_keys_found': umbrella_keys_found,
        'age_macro_count': age_macro_count,
        'invalid_npc_avatar_count': invalid_npc_avatar_count,
        'content_mismatches': content_mismatches,
        'all_passed': (
            total_entries_count == 1009 and 
            spurious_npc_count == 0 and 
            len(umbrella_keys_found) == 0 and 
            age_macro_count == 0 and 
            invalid_npc_avatar_count == 0 and 
            content_mismatches == 0 and
            all(r['pass'] for r in results)
        )
    }

    out_file = ROOT / 'scratch' / 'auditor_api_verification.json'
    out_file.write_text(json.dumps(out_record, indent=2), encoding='utf-8')
    print(f"Results written to {out_file}")
    return out_record['all_passed']

if __name__ == '__main__':
    ok = audit()
    if not ok:
        sys.exit(1)
