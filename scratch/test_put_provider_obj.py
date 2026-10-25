import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
url = 'https://app.wyvern.chat/api/connections/_e134BGYwKcRbteXnhAkLn'

# Get provider data
prov_url = 'https://app.wyvern.chat/api/providers/_x3jXXcbELnhK36PUTb8Te'
req = urllib.request.Request(prov_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    prov_data = json.loads(resp.read().decode())

payload = {
    "selected_provider": prov_data,
    "use_browser_request": True,
    "custom_model_id": "free-tier-master"
}

req = urllib.request.Request(
    url,
    method='PUT',
    headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
    data=json.dumps(payload).encode('utf-8')
)

try:
    with urllib.request.urlopen(req) as resp:
        print("PUT Connection status:", resp.status)
        data = json.loads(resp.read().decode())
        print("Updated conn selected_provider:", data.get('selected_provider'))
        print("Updated conn use_browser_request:", data.get('use_browser_request'))
except urllib.error.HTTPError as e:
    print(f"PUT Connection error: {e.code} {e.read().decode()}")
