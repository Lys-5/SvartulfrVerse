import sys
import json
import pathlib
import urllib.request

root = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.insert(0, str(root / 'scratch'))
import refresh_token

token = refresh_token.refresh()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'AuditorBot/1.0',
    'Accept': 'application/json'
}

test_ids = [
    'persona_1786335754946', 'user_persona_VnRF2xGeG1C4xByDF9h9R',
    '1792155173728', 'user_persona_bGDFCEtKDzVmgbCmHJWEW',
    '1791389790053', 'user_persona_Chhp2NRN1kkVVPXCGQb8C'
]

for pid in test_ids:
    url = f"https://app.wyvern.chat/api/user-personas/{pid}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"GET {pid} -> {resp.status} | name={data.get('name')}, id={data.get('id')}, persona_id={data.get('persona_id')}")
    except Exception as e:
        print(f"GET {pid} -> ERROR: {e}")
