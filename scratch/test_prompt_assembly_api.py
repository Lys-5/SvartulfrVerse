import urllib.request
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

endpoints = [
    "https://app.wyvern.chat/api/prompt-assembly",
    "https://app.wyvern.chat/api/prompt-assemblies",
    "https://app.wyvern.chat/api/prompt-assembly/usable",
    "https://app.wyvern.chat/api/prompt-assembly/mine",
    "https://app.wyvern.chat/api/exploreSearch/prompt-assemblies?page=1&limit=5"
]

for ep in endpoints:
    req = urllib.request.Request(ep, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"SUCCESS {ep} -> Status: {resp.status}")
            if isinstance(data, list):
                print(f"   List len: {len(data)}")
                if len(data) > 0:
                    print(f"   Item 0 id: {data[0].get('id')} name: {data[0].get('name')}")
            elif isinstance(data, dict):
                print(f"   Keys: {list(data.keys())}")
                if 'results' in data:
                    print(f"   Results len: {len(data['results'])}")
                if 'assemblies' in data:
                    print(f"   Assemblies len: {len(data['assemblies'])}")
    except urllib.error.HTTPError as e:
        print(f"HTTPError {ep} -> {e.code}: {e.reason}")
    except Exception as e:
        print(f"Error {ep} -> {e}")
