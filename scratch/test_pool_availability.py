import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

p = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
scen = json.load(p.open(encoding='utf-8'))

for s in scen['slots']:
    for c in s['pool']:
        cid = c['character_id']
        req = urllib.request.Request(f'https://app.wyvern.chat/api/characters/{cid}', headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                ch = data.get('character', data)
                creator = ch.get('creator', {}).get('uid') or ch.get('creator_uid')
                visibility = ch.get('visibility')
                status = ch.get('status')
                print(f"Slot '{s['key']}': id={cid}, name={ch.get('name')}, creator={creator}, visibility={visibility}, status={status}")
        except urllib.error.HTTPError as e:
            print(f"Slot '{s['key']}': id={cid} - HTTP {e.code}")
