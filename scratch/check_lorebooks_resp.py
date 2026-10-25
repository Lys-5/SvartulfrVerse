import urllib.request
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://app.wyvern.chat/api/lorebooks/user/2r4fVpvImte5dbljedLkZJxre2d2", headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print("Keys in lorebooks resp:", list(data.keys()))
    for lb in data.get('lorebooks', []):
        print("LB:", lb.get('id'), lb.get('name'), lb.get('visibility'))
