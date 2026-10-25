import urllib.request
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://app.wyvern.chat/api/worlds/_LUbtXbQzR6qFNE43tw9Wm", headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Name:", data.get('name'))
        print("Creator:", data.get('creator', {}).get('displayName'))
        print("Created:", data.get('created_at'))
except Exception as e:
    print("Error:", e)
