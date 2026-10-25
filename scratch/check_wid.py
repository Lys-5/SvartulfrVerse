import urllib.request
import urllib.error
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

for wid in ['_CgYT8fHXpDC4crjmegQF7', '_YpX47fNraQFw2dD7TdycJ']:
    try:
        req = urllib.request.Request(f"https://app.wyvern.chat/api/worlds/{wid}", headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"ID: {wid} | Name: '{data.get('name')}' | Created: {data.get('created_at')} | Locations: {data.get('locations_count')} | Lexicon: {data.get('lexicon_count')}")
    except urllib.error.HTTPError as e:
        print(f"ID: {wid} -> {e.code}")
