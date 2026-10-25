import urllib.request
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://app.wyvern.chat/api/worlds/public?limit=50", headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Total in public:", data.get('total'))
        print("Count in public:", len(data.get('worlds', [])))
        for w in data.get('worlds', []):
            if w.get('creator', {}).get('uid') == '2r4fVpvImte5dbljedLkZJxre2d2':
                print("FOUND USER WORLD IN PUBLIC:", w.get('id'), w.get('name'))
except Exception as e:
    print("Error:", e)
