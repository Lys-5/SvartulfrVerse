import urllib.request
import urllib.error
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

candidate_ids = [
    '_CgYT8fHXpDC4crjmegQF7',
    '_zwXR42HXhnnpq7UKYce9Y',
    '_tK3pKDLKBqJN3JxHpAWqG',
    '_YpX47fNraQFw2dD7TdycJ',
]

for wid in candidate_ids:
    url = f"https://app.wyvern.chat/api/worlds/{wid}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"EXISTS: {wid} | Name: '{data.get('name')}' | Created: {data.get('created_at')} | Locations: {data.get('locations_count')} | Lexicon: {data.get('lexicon_count')} | Status: {data.get('status')}")
    except urllib.error.HTTPError as e:
        print(f"NOT FOUND {wid}: {e.code}")
