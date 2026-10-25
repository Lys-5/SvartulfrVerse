import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
import sys
sys.path.append(str(ROOT / 'scratch'))
import refresh_token

token = refresh_token.refresh()
headers = {"Authorization": f"Bearer {token}", "User-Agent": "Mozilla/5.0"}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()

print("--- 1. Fetching Assistant ---")
status, asst = fetch("https://app.wyvern.chat/api/simple-assistant-config/simple_assistant_xRfBnV7wq48QppqbPPpTM")
print(f"Status: {status}")
if status == 200:
    print(f"Assistant title: {asst.get('title')}, kind: {asst.get('kind')}")
else:
    print(asst)

print("\n--- 2. Fetching Prompt Assembly ---")
status, pa = fetch("https://app.wyvern.chat/api/prompt-assembly/pha_kWkWUAfTJTF9q72c2bC98")
print(f"Status: {status}")
if status == 200:
    print(f"Prompt Assembly name: {pa.get('name')}, blocks: {len(pa.get('blocks', []))}")
else:
    print(pa)

print("\n--- 3. Fetching Chat Log ---")
status, chat = fetch("https://app.wyvern.chat/api/new/chat-logs/chat_log_qUdWrgx232YGtwDE2318a")
print(f"Status: {status}")
if status == 200:
    print("Chat log keys:", list(chat.keys()))
    # Let's save chat log keys and overrides to a json file for inspection
    with open('scratch/live_chat_log.json', 'w', encoding='utf-8') as f:
        json.dump(chat, f, indent=2, ensure_ascii=False)
    print("Saved to scratch/live_chat_log.json")
else:
    print(chat)
