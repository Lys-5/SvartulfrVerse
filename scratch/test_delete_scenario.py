import urllib.request
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': 'Bearer ' + token,
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json'
}

test_id = 'char_scenario_MdbWc4gXbDqXHKrXY7YFx' # From Batch 1 (Underworld duplicate)
url = f"https://app.wyvern.chat/api/character-scenarios/{test_id}"

req = urllib.request.Request(url, headers=headers, method='DELETE')
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print(f"DELETE status: {resp.status}")
        body = resp.read().decode('utf-8')
        print(f"DELETE body: {body}")
except urllib.error.HTTPError as e:
    print(f"DELETE failed with HTTP {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"DELETE error: {e}")
