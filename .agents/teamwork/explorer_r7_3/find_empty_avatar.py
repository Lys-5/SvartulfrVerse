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

url = "https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=30) as resp:
    data = json.loads(resp.read().decode('utf-8'))

lex = data.get('lexicon', [])
for i, e in enumerate(lex):
    if not e.get('avatar'):
        print(f"Live empty avatar entry: index={i}, id={e.get('entry_id')}, name={e.get('name')}, keys={e.get('keys')}, avatar={repr(e.get('avatar'))}")

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    local_data = json.load(f)

for i, e in enumerate(local_data.get('entries', [])):
    if e.get('entry_id') == 'RM6rcwv8MlY1XWaCTQp0M' or (not e.get('avatar')):
        print(f"Local entry: index={i}, id={e.get('entry_id')}, name={e.get('name')}, avatar={repr(e.get('avatar'))}")
