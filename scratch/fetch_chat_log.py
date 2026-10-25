import json
import urllib.request
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = TOKEN_PATH.read_text(encoding='utf-8').strip()

CHAT_ID = "chat_log_qUdWrgx232YGtwDE2318a"
url = f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_ID}"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

req = urllib.request.Request(url, headers=headers, method="GET")

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print("HTTP", resp.status)
        print("Keys:", list(data.keys()))
        # Print relevant settings keys
        for k in ['settings', 'narrator', 'overrides', 'generation_params', 'prompt_assembly', 'assistant_id', 'narrator_profile_id']:
            if k in data:
                print(f"--- {k} ---")
                print(json.dumps(data[k], indent=2))
        # If there's a settings object, check inside it
        if 'settings' in data and isinstance(data['settings'], dict):
            print("Settings keys:", list(data['settings'].keys()))
        ROOT.joinpath('scratch', 'chat_log_snapshot.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
        print("Saved snapshot to scratch/chat_log_snapshot.json")
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code, e.reason)
    print(e.read().decode()[:500])
except Exception as e:
    print("Error:", e)
