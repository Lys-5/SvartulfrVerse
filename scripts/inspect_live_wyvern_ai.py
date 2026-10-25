import urllib.request
import json

with open('scratch/wyvern_token.txt', 'r') as f:
    token = f.read().strip()

def get(url):
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

providers = get('https://app.wyvern.chat/api/providers/custom')
print(f"Total custom providers: {len(providers)}")
for p in providers:
    print(f"- Provider id: {p.get('id')}, name: {p.get('name')}, url: {p.get('api_url')}")

connections = get('https://app.wyvern.chat/api/connections/user')
print(f"\nUser connections total: {connections.get('total')}")
for c in connections.get('connections', []):
    print(f"- Connection id: {c.get('id')}, name: {c.get('name')}, model: {c.get('custom_model_id')}, provider: {c.get('selected_provider', {}).get('name')}")
