import urllib.request
import json

token = open('scratch/wyvern_token.txt', 'r', encoding='utf-8').read().strip()
cids = ['_93Rrpm1bDdytjzBqAp99P', '_nbEC7qk3NgU1LDfpQN9BW', '_9AycMJGa4fjy6pn6kgxGj']

for cid in cids:
    url = f'https://app.wyvern.chat/api/characters/{cid}'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print('=== Character:', cid, '===')
            print('Name:', data.get('name'))
            print('Title:', data.get('title'))
            print('Tagline:', data.get('tagline'))
            scen = data.get('scenario') or ''
            print('Scenario preview:', scen[:400])
            greetings = data.get('greetings', [])
            print('Greetings count:', len(greetings))
            for i, g in enumerate(greetings):
                gname = g.get('name') or g.get('title') or 'No title'
                print(f'  Greeting {i+1}: {gname}')
            with open(f'scratch/kakihara_{cid}.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f'Error fetching {cid}: {e}')
