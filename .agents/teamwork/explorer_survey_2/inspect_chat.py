import urllib.request
import json
import pathlib

token = pathlib.Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
chat_id = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
url = f"https://app.wyvern.chat/api/new/chat-logs/{chat_id}"

req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
data = json.loads(resp.read().decode('utf-8'))

print("Top keys:", list(data.keys()))
print("message_count:", data.get('message_count'))
print("total:", data.get('total'))

messages = data.get('messages', [])
print(f"Total messages in response: {len(messages)}")
for i, m in enumerate(messages):
    print(f"[{i}] id={m.get('id')} index={m.get('index')} char={m.get('character', {}).get('name') if isinstance(m.get('character'), dict) else m.get('character')} len={len(m.get('content', ''))}")
    print(f"     content snippet: {m.get('content', '')[:100]}...")
