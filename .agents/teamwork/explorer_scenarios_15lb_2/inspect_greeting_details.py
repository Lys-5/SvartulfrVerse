import json
import urllib.request
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

url = 'https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())

greetings = data['greetings']
print("=== Greeting 0 (empty linked_persona_ids) ===")
print(json.dumps({k: v for k, v in greetings[0].items() if k != 'content' and k != 'messages'}, indent=2))
print("Greeting 0 messages count:", len(greetings[0].get('messages', [])))

print("\n=== Greeting 2 (linked_persona_ids with Alyssa) ===")
print(json.dumps({k: v for k, v in greetings[2].items() if k != 'content' and k != 'messages'}, indent=2))
print("Greeting 2 messages count:", len(greetings[2].get('messages', [])))
print("Greeting 2 linked_personas object:", greetings[2].get('linked_personas'))

print("\n=== Greeting 3 (linked_persona_ids with Jasper) ===")
print(json.dumps({k: v for k, v in greetings[3].items() if k != 'content' and k != 'messages'}, indent=2))
print("Greeting 3 linked_personas object:", greetings[3].get('linked_personas'))
