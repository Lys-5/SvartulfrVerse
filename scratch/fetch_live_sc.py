import urllib.request
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()

url = 'https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4'
req = urllib.request.Request(
    url,
    headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
)

with urllib.request.urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode('utf-8'))

print("Live Scenario ID:", data.get('id'))
print("Live Scenario Name:", data.get('name'))
print("Live Revision:", data.get('revision'))
print("Live system_prompt len:", len(data.get('system_prompt', '') or ''))
print("Live final_instructions len:", len(data.get('final_instructions', '') or ''))

print("\n=== LIVE SLOTS ===")
for s in data.get('slots', []):
    print(f"Key: {s.get('key'):20} | char_id: {s.get('character_id')} | pool: {len(s.get('character_pool', []))} | default_role: {s.get('default_role')}")

with open('scratch/live_scenario_fetched.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, indent=2, ensure_ascii=False)
