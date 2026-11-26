import json
import urllib.request

TOKEN_PATH = r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt'
with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'ExplorerR73/1.0',
    'Accept': 'application/json'
}

core_ids = {
    'C-JisFj8qA1tsFEqZKevk': 'Erik Ulfr Douglas',
    'jDuJtzirlEZC3K_ArIufh': 'Malachia Björn Douglas Bloodmoon',
    'H2JX-NkHRiJ2FzoekC5ZZ': 'Noah Loki Douglas Bloodmoon',
    'tAcrWLtWSDGf3xJJRwUOM': 'Logan Járn Douglas',
    'HhuMluMmIIENUei3bX6ed': 'Wulfnic Báleygr Bloodmoon',
    'BXi3sENAVYB8OKF80Q9Su': 'Mackenzie Sanchez-Rogers',
    'h-ttmlgJYeRXqyDvQjSX7': 'Edric Douglas'
}

print("=== Live Primary Check for Core IDs ===")
url = "https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=30) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for e in data.get('lexicon', []):
    eid = e.get('entry_id')
    if eid in core_ids:
        print(f"ID: {eid} ({core_ids[eid]}):")
        print(f"  type: {e.get('type')}")
        print(f"  avatar: {repr(e.get('avatar'))}")
        print(f"  content_len: {len(e.get('content', ''))}")
        print(f"  ignored_characters: {e.get('ignored_characters')}")

print("\n=== Live Secondary Check for Edric ===")
url_sec = "https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV"
req_sec = urllib.request.Request(url_sec, headers=headers)
with urllib.request.urlopen(req_sec, timeout=30) as resp:
    data_sec = json.loads(resp.read().decode('utf-8'))

for e in data_sec.get('lexicon', []):
    eid = e.get('entry_id')
    if eid in core_ids:
        print(f"ID: {eid} ({core_ids[eid]}):")
        print(f"  type: {e.get('type')}")
        print(f"  avatar: {repr(e.get('avatar'))}")
        print(f"  content_len: {len(e.get('content', ''))}")
        print(f"  ignored_characters: {e.get('ignored_characters')}")
