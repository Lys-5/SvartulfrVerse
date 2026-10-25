import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import urllib.request
import json
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

chat_id = "chat_log_PJx1W1rg3WUzRM7MnQrkN"

for ep in [
    f'https://app.wyvern.chat/api/new/chat-logs/{chat_id}',
    f'https://app.wyvern.chat/api/chat-logs/{chat_id}'
]:
    req = urllib.request.Request(ep, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"SUCCESS {ep}:")
            print("  easy_parameters:", data.get('easy_parameters'))
            print("  easy_parameters_enabled:", data.get('easy_parameters_enabled'))
            print("  parameters:", data.get('parameters'))
            break
    except Exception as e:
        print(f"Error {ep}: {e}")
