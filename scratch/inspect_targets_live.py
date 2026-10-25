import urllib.request
import json
import pathlib
import sys

WT_PATH = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt')
cache_path = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\live_primary_lorebook.json')

token = WT_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json',
    'User-Agent': 'AuditorBot/1.0'
}

url = 'https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC'
print("Fetching lorebook from Wyvern API...", flush=True)
req = urllib.request.Request(url, headers=headers, method='GET')
try:
    with urllib.request.urlopen(req, timeout=45) as resp:
        print(f"HTTP Status: {resp.status}", flush=True)
        raw = resp.read().decode('utf-8')
        cache_path.write_text(raw, encoding='utf-8')
        print(f"Saved {len(raw)} bytes to {cache_path}", flush=True)
        data = json.loads(raw)
except Exception as e:
    print(f"Error fetching: {e}", flush=True)
    if cache_path.exists():
        print("Using existing cache...", flush=True)
        data = json.loads(cache_path.read_text(encoding='utf-8'))
    else:
        sys.exit(1)

lexicon = data.get('lexicon', data.get('entries', []))
print(f"Wyvern API live entries count: {len(lexicon)}", flush=True)

target_ids = {
    '4NzXF4_0hYxmN7Idltzpw': 'Scarlett Rose',
    'ijy8vrlphNv19-p-gbYuY': 'Sierra Cruz',
    'YCxAqNoShpefVvk0_Pc7i': "Russell 'Russ' Sinclair",
    'ekdQjq63xP7HtNuaPQJQE': 'Stanley Davies Jr.',
    'RM6rcwv8MlY1XWaCTQp0M': 'Jared Thompson',
    'alyssa_world_dossier_2b54a223': 'Alyssa Hvit Douglas Bloodmoon',
    'Vcj4h2TL4Usola2A4OOl6': 'Jasper (Reference)'
}

print("\n--- CHECKING TARGET IDS IN LIVE WYVERN API ---", flush=True)
for tid, tname in target_ids.items():
    found_by_id = [e for e in lexicon if e.get('id') == tid]
    found_by_name = [e for e in lexicon if any(tname.lower() in str(k).lower() for k in e.get('keys', []))]
    print(f"\nTarget: {tname} (ID: {tid})", flush=True)
    print(f"  found by ID: {len(found_by_id)}", flush=True)
    if found_by_id:
        e = found_by_id[0]
        print(f"    id: {e.get('id')}, type: {e.get('type')}, keys: {e.get('keys')}, sec_keys: {e.get('secondary_keys')}, selective: {e.get('selective')}, key_logic: {e.get('key_logic')}, avatar: {e.get('avatar')}, content len: {len(e.get('content',''))}", flush=True)
        print(f"    regex: {e.get('avatar_activation_regex')}, npc_info: {e.get('npc_info')}", flush=True)
    print(f"  found by Name: {len(found_by_name)}", flush=True)
    if found_by_name:
        for e in found_by_name:
            print(f"    id: {e.get('id')}, type: {e.get('type')}, keys: {e.get('keys')}, sec_keys: {e.get('secondary_keys')}, selective: {e.get('selective')}, key_logic: {e.get('key_logic')}, avatar: {e.get('avatar')}, content len: {len(e.get('content',''))}", flush=True)
            print(f"    regex: {e.get('avatar_activation_regex')}, npc_info: {e.get('npc_info')}", flush=True)
