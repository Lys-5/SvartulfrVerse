import urllib.request, json
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

ids = [
    'char_scenario_CKgwq246DyCj1NNTBV9rt',
    'char_scenario_Kq4mJEBH83j7Q7DdVfFnF',
    'char_scenario_1DC43ggb6mB8YLJDJKrU4',
    '_2MTWKjxrQPdQVaz9y4Q7H'
]

for sid in ids:
    print(f"=== Testing {sid} ===")
    for prefix in ['/api/scenarios/', '/api/worlds/scenarios/']:
        url = 'https://app.wyvern.chat' + prefix + sid
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as r:
                res = json.loads(r.read().decode('utf-8'))
                title = res.get('title') or res.get('name')
                print(f"  {prefix}{sid} -> 200 OK! Title: {title}")
        except Exception as e:
            print(f"  {prefix}{sid} -> {e}")
