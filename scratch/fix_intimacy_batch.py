import urllib.request
import json
import os
import re
import sys
import time

def get_auth_token():
    ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
    leveldb_dir = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\Default\IndexedDB\https_app.wyvern.chat_0.indexeddb.leveldb'
    if not os.path.exists(leveldb_dir):
        raise FileNotFoundError(f"LevelDB directory not found at {leveldb_dir}")

    rt = None
    for fname in os.listdir(leveldb_dir):
        fpath = os.path.join(leveldb_dir, fname)
        if fname.endswith(('.ldb', '.log')):
            try:
                with open(fpath, 'rb') as f:
                    content = f.read()
                    matches = re.findall(b'AMf-v[a-zA-Z0-9_-]{50,}', content)
                    if matches:
                        rt = matches[0].decode('latin1')
                        break
            except Exception:
                pass

    if not rt:
        raise ValueError("Could not find Firebase refresh token in Chrome IndexedDB.")

    refresh_url = f'https://securetoken.googleapis.com/v1/token?key={ak}'
    payload = json.dumps({'grant_type': 'refresh_token', 'refresh_token': rt}).encode('utf-8')
    req = urllib.request.Request(refresh_url, data=payload, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        return data['id_token']

world_id = '_CgYT8fHXpDC4crjmegQF7'

def put_lexicon(token, lex_id, payload):
    url = f'https://app.wyvern.chat/api/worlds/lexicon/{lex_id}'
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        return resp.getcode(), json.loads(resp.read().decode('utf-8'))

def get_world_lexicon(token):
    url = f'https://app.wyvern.chat/api/worlds/lexicon/world/{world_id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, headers=headers, method='GET')
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def main():
    batch_num = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    with open('docs/claude_project_docs/Intimacy_Profiles_Missing_Party_Conditions_Snapshot_2026-09-27.json', 'r', encoding='utf-8') as f:
        snapshot = json.load(f)

    # Filter out already disabled duplicates (Jean-Luc, Dante obsolete)
    active_items = [item for item in snapshot if item.get('enabled', True)]
    print(f'Total active items needing fix: {len(active_items)}')

    # 69 items -> 3 batches of 23
    batch_size = 23
    start_idx = (batch_num - 1) * batch_size
    end_idx = min(start_idx + batch_size, len(active_items))
    batch_items = active_items[start_idx:end_idx]

    print(f'Running Batch {batch_num}: items {start_idx} to {end_idx - 1} ({len(batch_items)} items)')

    token = get_auth_token()
    results = []

    for i, item in enumerate(batch_items):
        lex_id = item['id']
        name = item['name']
        att_id = item['attached_world_character_id']
        
        target_conditions = [{'mode': 'has_any', 'character_ids': [att_id]}]
        payload = {
            'party_conditions': target_conditions,
            'priority': 100
        }

        print(f'[{start_idx + i + 1}/{len(active_items)}] Updating {name} ({lex_id}) -> att_id: {att_id}...', end=' ')
        
        try:
            status, resp_data = put_lexicon(token, lex_id, payload)
            if status == 200:
                print('PUT 200 OK')
                results.append({'id': lex_id, 'name': name, 'att_id': att_id, 'status': 'PUT_OK'})
            else:
                print(f'FAILED: status {status}')
                results.append({'id': lex_id, 'name': name, 'att_id': att_id, 'status': 'FAILED', 'code': status})
        except Exception as e:
            print(f'ERROR: {e}')
            results.append({'id': lex_id, 'name': name, 'att_id': att_id, 'status': 'ERROR', 'error': str(e)})
        
        time.sleep(0.5)

    # Post-batch verification via GET all
    print('\nVerifying batch results with fresh GET from world...')
    fresh_lex = get_world_lexicon(token)
    fresh_map = {l['id']: l for l in fresh_lex}

    verified_count = 0
    for res in results:
        lid = res['id']
        att_id = res['att_id']
        fresh = fresh_map.get(lid)
        expected_conds = [{'mode': 'has_any', 'character_ids': [att_id]}]
        if fresh and fresh.get('party_conditions') == expected_conds and fresh.get('priority') == 100:
            verified_count += 1
            res['verified'] = True
        else:
            res['verified'] = False
            print(f"VERIFICATION FAILURE for {res['name']} ({lid}): {fresh.get('party_conditions') if fresh else 'NOT_FOUND'}")

    print(f'Batch {batch_num} Verification: {verified_count}/{len(results)} successfully verified live!')

    out_file = f'docs/claude_project_docs/Intimacy_Fix_Batch_{batch_num}_Results.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f'Results saved to {out_file}.\n')

if __name__ == '__main__':
    main()
