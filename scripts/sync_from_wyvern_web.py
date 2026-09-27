import urllib.request
import json
import os
import re
import sys

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

def sync_world(world_id='_CgYT8fHXpDC4crjmegQF7'):
    print(f"Starting sync from Wyvern Web API for World ID: {world_id}...")
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    exports_dir = os.path.join(base_dir, 'exports')
    os.makedirs(exports_dir, exist_ok=True)

    master_export_path = os.path.join(exports_dir, 'Svartulfr_Export.json')
    backup_path = os.path.join(exports_dir, 'Svartulfr_Export_pre_web_sync.json')

    # Backup existing export
    if os.path.exists(master_export_path):
        with open(master_export_path, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(old_data, f, indent=2, ensure_ascii=False)
        print(f"Backed up existing export to: {backup_path}")

    # Fetch World metadata
    w_url = f'https://app.wyvern.chat/api/worlds/{world_id}'
    req = urllib.request.Request(w_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        world_obj = json.loads(resp.read().decode('utf-8'))
    print(f"Fetched World: {world_obj.get('name')} (Updated: {world_obj.get('updated_at')})")

    endpoints_mapping = [
        ('world_characters', 'characters'),
        ('world_locations', 'locations'),
        ('world_environments', 'environments'),
        ('world_lexicon_entries', 'lexicon'),
        ('world_scenarios', 'scenarios'),
        ('world_maps', 'maps'),
        ('world_eras', 'eras'),
        ('world_parties', 'parties'),
        ('world_timeline_events', 'timeline-events'),
        ('world_gedcom_trees', 'gedcom-trees')
    ]

    export_payload = {
        'world': world_obj
    }

    for table_name, api_resource in endpoints_mapping:
        url = f'https://app.wyvern.chat/api/worlds/{api_resource}/world/{world_id}'
        try:
            r = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(r) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if isinstance(data, list):
                    items = data
                elif isinstance(data, dict) and 'items' in data:
                    items = data['items']
                else:
                    items = []
                export_payload[table_name] = items
                print(f"  - {table_name:25}: {len(items)} items")
        except Exception as e:
            print(f"  - {table_name:25}: Error ({e}), setting to []")
            export_payload[table_name] = []

    # Write master export
    with open(master_export_path, 'w', encoding='utf-8') as f:
        json.dump(export_payload, f, indent=2, ensure_ascii=False)
    print(f"\nSuccessfully wrote updated master export to: {master_export_path}")
    print(f"File size: {os.path.getsize(master_export_path):,} bytes")

if __name__ == '__main__':
    world_id = sys.argv[1] if len(sys.argv) > 1 else '_CgYT8fHXpDC4crjmegQF7'
    sync_world(world_id)
