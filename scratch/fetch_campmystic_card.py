import urllib.request
import json

token = open('scratch/wyvern_token.txt', 'r', encoding='utf-8').read().strip()
cid = '_L3143TCBCzH7QPwUVKE6p'
url = f'https://app.wyvern.chat/api/characters/{cid}'
req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        with open('scratch/campmystic_full_card.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Successfully saved scratch/campmystic_full_card.json!")
        print("ID:", data.get('id'))
        print("Greetings len:", len(data.get('greetings', [])))
        for i, g in enumerate(data.get('greetings', [])):
            name = (g.get('name') or g.get('title') or 'No title').encode('ascii', errors='replace').decode('ascii')
            print(f"  Greeting {i+1}: {name}")
except Exception as e:
    print('Error:', e)
