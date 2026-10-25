import urllib.request
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': 'Bearer ' + token,
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json'
}

req = urllib.request.Request('https://app.wyvern.chat/api/character-scenarios', headers=headers)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(f"Total scenarios found: {len(data)}")
        for s in data:
            print(f"ID: {s.get('id')} | Title: {s.get('title')} | Created: {s.get('created_at')}")
except Exception as e:
    print(f"Error: {e}")
