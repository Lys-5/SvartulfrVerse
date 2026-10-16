import urllib.request
import urllib.error
import json
import pathlib
import time
import base64
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
LOG_PATH = ROOT / 'scratch' / 'deployment_log.json'
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
API_BASE = 'https://app.wyvern.chat/api'

RT_PATH = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\74bb3384-9979-419b-80ab-c29e070cbffe\scratch\refresh_token.txt')
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'

PACING_DELAY_SECONDS = 2.5
MAX_PAYLOAD_BYTES = 1000000  # Wyvern proxy HTTP 413 threshold (~1MB)

TARGET_LOREBOOKS = [
    {
        'id': '_gwwCxCfQ6PQaLEjAQVpJL',
        'file': 'Svartulfr_Lorebook_I.json',
        'expected_entries': 219,
        'title': 'Svartúlfr - Lorebook I',
    },
    {
        'id': '_HfG7TeV6MJyj6bxMwxkpt',
        'file': 'Svartulfr_Lorebook_II.json',
        'expected_entries': 143,
        'title': 'Svartúlfr - Lorebook II',
    },
    {
        'id': '_9zWTGqYJNJ4BCDMj8gfcD',
        'file': 'Svartulfr_Lorebook_III.json',
        'expected_entries': 35,
        'title': 'Svartúlfr - Lorebook III (SUCC & Underworld)',
    },
    {
        'id': '_EjXxkmPVhpCXg8xABpFkK',
        'file': 'Svartulfr_Location.json',
        'expected_entries': 196,
        'title': 'Svartúlfr - Location',
    },
    {
        'id': '_zwEqgEEzh12X6gHVmMKKC',
        'file': 'Svartulfr_NPC_Primary.json',
        'expected_entries': 106,
        'title': 'Svartúlfr - NPC Primary',
    },
    {
        'id': '_Uht3Ckz44JBDrPnUHq7LV',
        'file': 'Svartulfr_NPC_Secondary.json',
        'expected_entries': 310,
        'title': 'Svartúlfr - NPC Secondary',
    },
]

def ensure_valid_token():
    token = WT_PATH.read_text(encoding='utf-8').strip() if WT_PATH.exists() else ''
    needs_refresh = True
    if token:
        try:
            parts = token.split('.')
            payload = json.loads(base64.b64decode(parts[1] + '==').decode('utf-8'))
            exp = payload.get('exp', 0)
            now = time.time()
            if exp - now > 300:
                print(f"[TOKEN] Token valid for next {int(exp - now)}s.")
                needs_refresh = False
            else:
                print(f"[TOKEN] Token expiring in {int(exp - now)}s, refreshing...")
        except Exception as e:
            print(f"[TOKEN] Token parse failed: {e}")

    if needs_refresh:
        if RT_PATH.exists():
            rt = RT_PATH.read_text(encoding='utf-8').strip()
            body = json.dumps({'grant_type': 'refresh_token', 'refresh_token': rt}).encode('utf-8')
            req = urllib.request.Request(
                f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}',
                data=body,
                headers={'Content-Type': 'application/json'}
            )
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                token = data['id_token']
                WT_PATH.write_text(token, encoding='utf-8')
                print("[TOKEN] Token successfully refreshed and written to scratch/wyvern_token.txt.")
        else:
            print("[TOKEN] RT_PATH does not exist, keeping existing token.")
    return token


def main():
    print("=" * 70)
    print("WYVERN API LIVE DEPLOYMENT & VERIFICATION — MILESTONE R3")
    print("=" * 70)

    token = ensure_valid_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    deployment_record = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'pacing_delay_seconds': PACING_DELAY_SECONDS,
        'total_expected_entries': sum(lb['expected_entries'] for lb in TARGET_LOREBOOKS),
        'deployments': [],
        'post_verification': [],
        'overall_status': 'IN_PROGRESS'
    }

    total_deployed = 0
    total_verified = 0

    # STEP 1: LIVE PUT DEPLOYMENT
    print("\n--- STEP 1: PUT /api/lorebooks/{id} (Live Deployment) ---")
    for idx, lb in enumerate(TARGET_LOREBOOKS, start=1):
        lid = lb['id']
        fname = lb['file']
        expected_cnt = lb['expected_entries']
        title = lb['title']
        fpath = FINAL_DIR / fname

        print(f"\n[{idx}/6] Deploying {title} ({lid})...")
        print(f"  Source file: {fpath}")

        file_data = json.loads(fpath.read_text(encoding='utf-8'))
        entries_data = file_data.get('entries', [])
        lexicon_data = file_data.get('lexicon', [])

        assert len(entries_data) == expected_cnt, f"Local entries count mismatch for {fname}: {len(entries_data)} != {expected_cnt}"
        assert len(lexicon_data) == expected_cnt, f"Local lexicon count mismatch for {fname}: {len(lexicon_data)} != {expected_cnt}"

        # Construct standard top-level payload
        base_payload = {
            'name': file_data.get('name', title),
            'description': file_data.get('description', ''),
            'visibility': file_data.get('visibility', 'private'),
            'rating': file_data.get('rating', 'explicit'),
            'scan_depth': file_data.get('scan_depth', 5),
            'token_budget': file_data.get('token_budget', 5000),
            'recursive_scanning': file_data.get('recursive_scanning', True),
        }

        # Try dual-array first if it fits under 1MB limit; otherwise use native lexicon array
        payload_both = dict(base_payload)
        payload_both['entries'] = entries_data
        payload_both['lexicon'] = lexicon_data
        bytes_both = json.dumps(payload_both, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

        payload_lex = dict(base_payload)
        payload_lex['lexicon'] = lexicon_data
        bytes_lex = json.dumps(payload_lex, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

        if len(bytes_both) < MAX_PAYLOAD_BYTES:
            chosen_payload_bytes = bytes_both
            payload_type = 'dual_array (entries + lexicon)'
        else:
            chosen_payload_bytes = bytes_lex
            payload_type = 'native_lexicon (size mitigation for proxy 1MB limit)'

        print(f"  Payload type: {payload_type} | Size: {len(chosen_payload_bytes):,} bytes | Entries: {len(entries_data)}")

        url = f'{API_BASE}/lorebooks/{lid}'
        req = urllib.request.Request(url, data=chosen_payload_bytes, headers=headers, method='PUT')

        t0 = time.time()
        put_status = None
        put_response = None

        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                put_status = resp.status
                t_elapsed = round(time.time() - t0, 3)
                resp_raw = resp.read().decode('utf-8')
                put_response = json.loads(resp_raw)
                print(f"  --> HTTP {put_status} OK (elapsed: {t_elapsed}s)")
                saved_lex = len(put_response.get('lexicon', []))
                saved_ent = len(put_response.get('entries', []))
                print(f"  --> Server confirmed saved - Lexicon: {saved_lex}, Entries: {saved_ent}")
                total_deployed += saved_lex
        except urllib.error.HTTPError as e:
            if e.code == 413:
                print(f"  --> HTTP 413 on {payload_type}, retrying with native lexicon payload...")
                t0_retry = time.time()
                req_retry = urllib.request.Request(url, data=bytes_lex, headers=headers, method='PUT')
                with urllib.request.urlopen(req_retry, timeout=90) as resp_retry:
                    put_status = resp_retry.status
                    t_elapsed = round(time.time() - t0_retry, 3)
                    resp_raw = resp_retry.read().decode('utf-8')
                    put_response = json.loads(resp_raw)
                    payload_type = 'native_lexicon (fallback after 413)'
                    chosen_payload_bytes = bytes_lex
                    print(f"  --> Retry HTTP {put_status} OK (elapsed: {t_elapsed}s)")
                    saved_lex = len(put_response.get('lexicon', []))
                    saved_ent = len(put_response.get('entries', []))
                    print(f"  --> Server confirmed saved - Lexicon: {saved_lex}, Entries: {saved_ent}")
                    total_deployed += saved_lex
            else:
                error_msg = e.read().decode('utf-8', errors='ignore')
                print(f"  --> FAILED HTTP {e.code}: {error_msg[:300]}")
                sys.exit(f"ABORT: PUT failed on {lid} with HTTP {e.code}")
        except Exception as e:
            t_elapsed = round(time.time() - t0, 3)
            error_msg = str(e)
            print(f"  --> FAILED EXCEPTION: {error_msg}")
            sys.exit(f"ABORT: PUT failed on {lid} with exception: {error_msg}")

        deploy_record = {
            'id': lid,
            'title': title,
            'file': fname,
            'payload_type': payload_type,
            'http_status': put_status,
            'response_time_seconds': t_elapsed,
            'payload_bytes': len(chosen_payload_bytes),
            'entries_sent': len(entries_data),
            'lexicon_sent': len(lexicon_data),
            'server_confirmed_lexicon': len(put_response.get('lexicon', [])),
            'server_confirmed_entries': len(put_response.get('entries', [])),
            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        }
        deployment_record['deployments'].append(deploy_record)

        print(f"  [Pacing] Waiting {PACING_DELAY_SECONDS}s before next operation...")
        time.sleep(PACING_DELAY_SECONDS)

    print(f"\nAll 6 PUT deployments completed successfully! Total entries deployed: {total_deployed}")

    # STEP 2: POST-DEPLOYMENT VERIFICATION VIA GET
    print("\n--- STEP 2: GET /api/lorebooks/{id} (Post-Deployment Cloud Verification) ---")
    for idx, lb in enumerate(TARGET_LOREBOOKS, start=1):
        lid = lb['id']
        expected_cnt = lb['expected_entries']
        title = lb['title']

        print(f"\n[{idx}/6] Verifying {title} ({lid})...")
        url = f'{API_BASE}/lorebooks/{lid}'
        req = urllib.request.Request(url, headers=headers, method='GET')

        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                get_status = resp.status
                t_elapsed = round(time.time() - t0, 3)
                resp_raw = resp.read().decode('utf-8')
                get_response = json.loads(resp_raw)

                cloud_lexicon = get_response.get('lexicon', [])
                cloud_entries = get_response.get('entries', [])
                cloud_cnt = len(cloud_lexicon)

                print(f"  --> HTTP {get_status} OK (elapsed: {t_elapsed}s)")
                print(f"  --> Cloud Lexicon Count: {cloud_cnt} (expected: {expected_cnt})")
                print(f"  --> Cloud Entries Count: {len(cloud_entries)}")
                print(f"  --> Cloud Name: {repr(get_response.get('name'))}")
                print(f"  --> Cloud Rating: {get_response.get('rating')}, Visibility: {get_response.get('visibility')}")

                assert get_status == 200, f"Expected HTTP 200, got {get_status}"
                assert cloud_cnt == expected_cnt, f"Cloud lexicon count {cloud_cnt} != expected {expected_cnt}"

                total_verified += cloud_cnt

                verify_record = {
                    'id': lid,
                    'title': title,
                    'file': lb['file'],
                    'http_status': get_status,
                    'response_time_seconds': t_elapsed,
                    'cloud_lexicon_count': cloud_cnt,
                    'cloud_entries_count': len(cloud_entries),
                    'expected_count': expected_cnt,
                    'verified': (cloud_cnt == expected_cnt),
                    'cloud_name': get_response.get('name'),
                    'cloud_rating': get_response.get('rating'),
                    'cloud_visibility': get_response.get('visibility'),
                    'cloud_scan_depth': get_response.get('scan_depth'),
                    'cloud_token_budget': get_response.get('token_budget'),
                    'cloud_recursive_scanning': get_response.get('recursive_scanning'),
                    'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                }
                deployment_record['post_verification'].append(verify_record)
        except Exception as e:
            print(f"  --> GET VERIFICATION FAILED: {e}")
            sys.exit(f"ABORT: GET verification failed on {lid}: {e}")

        print(f"  [Pacing] Waiting {PACING_DELAY_SECONDS}s before next verification...")
        time.sleep(PACING_DELAY_SECONDS)

    print("\n" + "=" * 70)
    print(f"POST-DEPLOYMENT CLOUD VERIFICATION SUCCESSFUL!")
    print(f"Total cloud entries verified: {total_verified} / 1,009")
    print("=" * 70)

    deployment_record['total_verified_entries'] = total_verified
    deployment_record['overall_status'] = 'SUCCESS'

    LOG_PATH.write_text(json.dumps(deployment_record, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\nDeployment log written to {LOG_PATH}")

if __name__ == '__main__':
    main()
