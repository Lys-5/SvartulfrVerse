import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
url = 'https://app.wyvern.chat/api/connections/_e134BGYwKcRbteXnhAkLn'

# Let's test different field names:
tests = [
    {"selected_provider": "_x3jXXcbELnhK36PUTb8Te"},
    {"provider": "_x3jXXcbELnhK36PUTb8Te"},
    {"provider_id": "_x3jXXcbELnhK36PUTb8Te"},
    {"custom_provider": "_x3jXXcbELnhK36PUTb8Te"},
    {"custom_provider_id": "_x3jXXcbELnhK36PUTb8Te"},
    {"selectedProvider": "_x3jXXcbELnhK36PUTb8Te"},
    {"selected_provider_id": "_x3jXXcbELnhK36PUTb8Te"},
]

for t in tests:
    field_name = list(t.keys())[0]
    req = urllib.request.Request(
        url,
        method='PUT',
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
        data=json.dumps(t).encode('utf-8')
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            sp = data.get('selected_provider')
            print(f"Testing {field_name} -> selected_provider: {sp if sp is None else sp.get('name') or sp.get('id')}")
            if sp:
                print("FOUND WORKING FIELD:", field_name)
                break
    except Exception as e:
        print(f"Testing {field_name} -> Error: {e}")
