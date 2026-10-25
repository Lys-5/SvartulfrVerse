import urllib.request
import json

with open('scratch/wyvern_token.txt', 'r') as f:
    token = f.read().strip()

url = 'https://app.wyvern.chat/api/providers'

payload = {
    "name": "Local Free Proxy",
    "api_type": "openai",
    "api_url": "http://127.0.0.1:5005/v1",
    "api_architecture": "openai",
    "chat_completion_only": True,
    "no_key": True,
    "browser_only": True,
    "capabilities": ["chat"],
    "allowed_params": []
}

req = urllib.request.Request(
    url,
    method='POST',
    headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    },
    data=json.dumps(payload).encode('utf-8')
)

try:
    with urllib.request.urlopen(req) as resp:
        print("POST Provider status:", resp.status)
        data = json.loads(resp.read().decode('utf-8'))
        print("Created provider:", json.dumps(data, indent=2))
        with open("scratch/created_local_provider.json", "w") as f:
            json.dump(data, f, indent=2)
except urllib.error.HTTPError as e:
    print(f"POST Provider failed: {e.code} {e.reason}: {e.read().decode('utf-8')}")
