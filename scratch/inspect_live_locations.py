import json
import urllib.request

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

url = 'https://app.wyvern.chat/api/worlds/locations/world/_CgYT8fHXpDC4crjmegQF7'
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print(f"Locations count for _CgYT8fHXpDC4crjmegQF7: {len(data)}")
        if data:
            print("Location keys:", list(data[0].keys()))
            print("Sample location:")
            # Find a child location
            sample = None
            for l in data:
                if l.get('parent_location'):
                    sample = l
                    break
            if not sample:
                sample = data[0]
            print(json.dumps({
                'id': sample.get('id'),
                'name': sample.get('name'),
                'parent_location': sample.get('parent_location'),
                'environment': sample.get('environment'),
                'keys': sample.get('keys'),
                'included_lexicon_entries': sample.get('included_lexicon_entries')
            }, indent=2))
except Exception as e:
    print("Error:", e)
