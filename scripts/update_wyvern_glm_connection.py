import urllib.request
import json

with open('scratch/wyvern_token.txt', 'r') as f:
    token = f.read().strip()

url = 'https://app.wyvern.chat/api/connections/_YjmGAE9zPFgEQgYKaGXYq'

payload = {
    "parameters": {
        "max_tokens": {
            "value": 4096,
            "definition": {"type": "number"}
        },
        "temperature": {
            "value": 0.75,
            "definition": {"type": "number"}
        },
        "top_p": {
            "value": 0.95,
            "definition": {"type": "number"}
        },
        "frequency_penalty": {
            "value": 0.1,
            "definition": {"type": "number"}
        },
        "presence_penalty": {
            "value": 0.05,
            "definition": {"type": "number"}
        }
    }
}

req = urllib.request.Request(
    url,
    method='PUT',
    headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    },
    data=json.dumps(payload).encode('utf-8')
)

try:
    with urllib.request.urlopen(req) as resp:
        print("PUT Connection status:", resp.status)
        data = json.loads(resp.read().decode('utf-8'))
        print("PUT Connection response:")
        print(json.dumps(data.get('parameters', {}), indent=2))
except urllib.error.HTTPError as e:
    print(f"PUT failed: {e.code} {e.reason}: {e.read().decode('utf-8')}")
