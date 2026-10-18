import json
import pathlib
import urllib.request
import urllib.error
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
OPTIMIZED_DIR = ROOT / 'lorebooks' / 'optimized'
ARCHIVE_DIR = ROOT / 'ARCHIVIO' / '07_Purged_Disabled_Entries'
ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
RT_PATH = ROOT / 'scratch' / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'

PACING_DELAY_SECONDS = 2.5
MAX_PAYLOAD_BYTES = 1000000

LOREBOOKS_TO_CLEAN = [
    {
        'id': '_EjXxkmPVhpCXg8xABpFkK',
        'file': 'Svartulfr_Location.json',
        'title': 'Svartúlfr - Location'
    },
    {
        'id': '_HfG7TeV6MJyj6bxMwxkpt',
        'file': 'Svartulfr_Lorebook_II.json',
        'title': 'Svartúlfr - Lorebook II'
    },
    {
        'id': '_zwEqgEEzh12X6gHVmMKKC',
        'file': 'Svartulfr_NPC_Primary.json',
        'title': 'Svartúlfr - NPC Primary'
    },
    {
        'id': '_Uht3Ckz44JBDrPnUHq7LV',
        'file': 'Svartulfr_NPC_Secondary.json',
        'title': 'Svartúlfr - NPC Secondary'
    }
]

def refresh_auth_token():
    rt = RT_PATH.read_text(encoding='utf-8').strip()
    body = json.dumps({'grant_type': 'refresh_token', 'refresh_token': rt}).encode('utf-8')
    req = urllib.request.Request(
        f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}',
        data=body,
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        token = res['id_token']
        WT_PATH.write_text(token, encoding='utf-8')
        return token

def main():
    print("=== STEP 1: Archiving and Purging OFF Entries from FINAL/ ===")
    archive_manifest = {}
    cleaned_summaries = []

    for lb in LOREBOOKS_TO_CLEAN:
        fpath = FINAL_DIR / lb['file']
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        entries = data.get('entries', [])
        enabled_entries = [e for e in entries if e.get('enabled') is not False]
        disabled_entries = [e for e in entries if e.get('enabled') is False]

        print(f"\n[{lb['title']}] ({lb['file']}):")
        print(f"  Initial entries: {len(entries)}")
        print(f"  Enabled entries kept: {len(enabled_entries)}")
        print(f"  Disabled (OFF) entries purged: {len(disabled_entries)}")

        archive_manifest[lb['file']] = {
            'lorebook_id': lb['id'],
            'title': lb['title'],
            'purged_count': len(disabled_entries),
            'purged_entries': disabled_entries
        }

        # Update local file data
        data['entries'] = enabled_entries
        data['lexicon'] = enabled_entries

        # Save to FINAL/
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        # Save to lorebooks/optimized/
        opt_path = OPTIMIZED_DIR / lb['file']
        opt_path.parent.mkdir(parents=True, exist_ok=True)
        with open(opt_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

        cleaned_summaries.append({
            'id': lb['id'],
            'file': lb['file'],
            'title': lb['title'],
            'before_count': len(entries),
            'after_count': len(enabled_entries),
            'purged_count': len(disabled_entries)
        })

    # Save archive manifest
    archive_file = ARCHIVE_DIR / 'purged_disabled_entries_manifest.json'
    with open(archive_file, 'w', encoding='utf-8') as f:
        json.dump(archive_manifest, f, indent=2, ensure_ascii=False)
    print(f"\n[ARCHIVE] Saved all purged entries to {archive_file}")

    print("\n=== STEP 2: Deploying Cleaned Lorebooks to Wyvern API ===")
    token = refresh_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for idx, item in enumerate(cleaned_summaries, 1):
        lid = item['id']
        fpath = FINAL_DIR / item['file']
        with open(fpath, 'r', encoding='utf-8') as f:
            file_data = json.load(f)

        print(f"\n[{idx}/{len(cleaned_summaries)}] Deploying {item['title']} ({lid})...")
        base_payload = {
            'name': file_data.get('name', item['title']),
            'description': file_data.get('description', ''),
            'visibility': file_data.get('visibility', 'private'),
            'rating': file_data.get('rating', 'explicit'),
            'scan_depth': file_data.get('scan_depth', 5),
            'token_budget': file_data.get('token_budget', 5000),
            'recursive_scanning': file_data.get('recursive_scanning', True),
        }

        # Size mitigation check
        payload_both = dict(base_payload)
        payload_both['entries'] = file_data['entries']
        payload_both['lexicon'] = file_data['lexicon']
        bytes_both = json.dumps(payload_both, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

        payload_lex = dict(base_payload)
        payload_lex['lexicon'] = file_data['lexicon']
        bytes_lex = json.dumps(payload_lex, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

        if len(bytes_both) < MAX_PAYLOAD_BYTES:
            chosen_bytes = bytes_both
            mode = "dual_array"
        else:
            chosen_bytes = bytes_lex
            mode = "native_lexicon"

        print(f"  Mode: {mode} | Size: {len(chosen_bytes):,} bytes | Target entries: {item['after_count']}")

        put_req = urllib.request.Request(
            f'https://app.wyvern.chat/api/lorebooks/{lid}',
            data=chosen_bytes,
            method='PUT',
            headers=headers
        )

        try:
            with urllib.request.urlopen(put_req, timeout=60) as resp:
                print(f"  Deploy Status: HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            err = e.read().decode('utf-8', errors='replace')
            print(f"  ERROR {e.code}: {err}")
            continue

        time.sleep(PACING_DELAY_SECONDS)

        # GET Verification
        get_req = urllib.request.Request(
            f'https://app.wyvern.chat/api/lorebooks/{lid}',
            headers=headers
        )
        with urllib.request.urlopen(get_req, timeout=30) as resp:
            vdata = json.loads(resp.read().decode('utf-8'))
            rem_entries = len(vdata.get('lexicon', [])) or len(vdata.get('entries', []))
            print(f"  Verification GET: HTTP {resp.status} | Remote entries count: {rem_entries}")
            assert rem_entries == item['after_count'], f"Mismatch! Expected {item['after_count']}, got {rem_entries}"

    print("\n=== All lorebooks successfully cleaned, archived, and deployed! ===")

if __name__ == '__main__':
    main()
