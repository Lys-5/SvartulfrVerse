import json
import urllib.request

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

world_id = "_cxKHCnMgQXzMrrWpTHBE8"

# 1. Test link character on _cxKHCnMgQXzMrrWpTHBE8
cid = "_t4J9aQNJM36cUKAP4wB4U" # Jasper Douglas
url = f'https://app.wyvern.chat/api/worlds/linked-characters/{world_id}'
payload = {'character_id': cid}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
try:
    with urllib.request.urlopen(req) as resp:
        print("linkCharacter Status:", resp.status)
        data = json.loads(resp.read().decode('utf-8'))
        print("linkCharacter response:", data)
except urllib.error.HTTPError as e:
    print(f"linkCharacter HTTP Error {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("linkCharacter Error:", e)

# 2. Get linked characters
get_url = f'https://app.wyvern.chat/api/worlds/linked-characters/{world_id}'
req_get = urllib.request.Request(get_url, headers=headers)
try:
    with urllib.request.urlopen(req_get) as resp:
        print("getLinkedCharacters Status:", resp.status)
        gdata = json.loads(resp.read().decode('utf-8'))
        print("getLinkedCharacters response count:", len(gdata))
        print("Response:", gdata)
except urllib.error.HTTPError as e:
    print(f"getLinkedCharacters HTTP Error {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("getLinkedCharacters Error:", e)
