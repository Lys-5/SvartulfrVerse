import sys, os
sys.path.insert(0, os.getcwd())
import urllib.request, json
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
chat_id = 'chat_log_PJx1W1rg3WUzRM7MnQrkN'

req = urllib.request.Request(f'https://app.wyvern.chat/api/new/chat-logs/{chat_id}', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for k in ['world', 'world_data', 'world_party', 'environment_config', 'memory', 'world_scenario_id']:
    print(f"=== {k} ===")
    val = data.get(k)
    print(json.dumps(val, indent=2)[:1000] if val else 'None')
