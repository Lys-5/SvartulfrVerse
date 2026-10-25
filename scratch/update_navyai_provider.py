import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}

url = 'https://app.wyvern.chat/api/providers/custom/_WwxWntJxMzFWfQ4RYghQN'
payload = {
    "name": "NavyAI (Local Proxy Rotator)",
    "api_url": "http://127.0.0.1:5005/v1",
    "browser_only": True,
    "no_key": True,
    "chat_completion_only": True,
    "api_type": "openai",
    "api_architecture": "openai"
}

req = urllib.request.Request(url, method='PUT', headers=headers, data=json.dumps(payload).encode('utf-8'))
try:
    with urllib.request.urlopen(req) as resp:
        print("PUT Provider status:", resp.status)
        print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"PUT Provider failed: {e.code} {e.read().decode('utf-8')}")
