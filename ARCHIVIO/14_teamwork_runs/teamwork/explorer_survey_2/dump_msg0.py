import urllib.request
import json
import pathlib

token = pathlib.Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
chat_id = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
url = f"https://app.wyvern.chat/api/new/chat-logs/{chat_id}"

req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
data = json.loads(resp.read().decode('utf-8'))

msg0 = data['messages'][0]
pathlib.Path('.agents/teamwork/explorer_survey_2/chat_msg0.json').write_text(json.dumps(msg0, indent=2, ensure_ascii=False), encoding='utf-8')
print("Saved msg0 to .agents/teamwork/explorer_survey_2/chat_msg0.json")
print("Message ID:", msg0.get('id'))
print("Content length:", len(msg0.get('content', '')))
print("Number of swipes:", len(msg0.get('swipes', [])))
if msg0.get('swipes'):
    print("Swipe 0 content length:", len(msg0['swipes'][0].get('content', '')))
