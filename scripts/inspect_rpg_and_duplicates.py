import urllib.request
import json
import os
import re
import sys

def get_auth_token():
    ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
    leveldb_dir = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\Default\IndexedDB\https_app.wyvern.chat_0.indexeddb.leveldb'
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

def test_api():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    world_id = '_CgYT8fHXpDC4crjmegQF7'

    # Check Alyssa character directly from API
    alyssa_id = '_MXcEC8Y6B3BNm3b1ttHj6'
    url = f'https://app.wyvern.chat/api/worlds/characters/{alyssa_id}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        alyssa = json.loads(resp.read().decode('utf-8'))
    print("Alyssa API keys:", list(alyssa.keys()))
    print("Alyssa level:", alyssa.get('level'))
    print("Alyssa rpg_stats:", alyssa.get('rpg_stats'))
    print("Alyssa species_id:", alyssa.get('species_id'))
    print("Alyssa occupation_id:", alyssa.get('occupation_id'))

    # Check endpoints for blueprints
    endpoints = [
        f'https://app.wyvern.chat/api/worlds/blueprints/world/{world_id}',
        f'https://app.wyvern.chat/api/worlds/{world_id}/blueprints',
        f'https://app.wyvern.chat/api/blueprints',
        f'https://app.wyvern.chat/api/blueprints/world/{world_id}',
        f'https://app.wyvern.chat/api/worlds/rpg-classes',
        f'https://app.wyvern.chat/api/worlds/species',
        f'https://app.wyvern.chat/api/species',
        f'https://app.wyvern.chat/api/occupations'
    ]
    for ep in endpoints:
        try:
            r = urllib.request.Request(ep, headers=headers)
            with urllib.request.urlopen(r) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                print(f"SUCCESS: {ep} -> {type(data)} (keys/len: {list(data.keys()) if isinstance(data, dict) else len(data)})")
                if isinstance(data, list) and len(data) > 0:
                    print("  Sample item:", data[0])
                elif isinstance(data, dict):
                    for k in list(data.keys())[:3]:
                        print(f"  {k}:", str(data[k])[:100])
        except urllib.error.HTTPError as e:
            print(f"FAILED ({e.code}): {ep}")
        except Exception as e:
            print(f"ERROR: {ep} -> {e}")

if __name__ == '__main__':
    test_api()
