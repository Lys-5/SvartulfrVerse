import urllib.request
import json
import time

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': 'Bearer ' + token,
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json'
}

with open('scratch/live_character_scenarios_all.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total items in cache: {len(items)}")

detailed_scenarios = []

for idx, sc in enumerate(items):
    sid = sc.get('id')
    name = sc.get('name')
    url = f"https://app.wyvern.chat/api/character-scenarios/{sid}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            slots = data.get('slots', [])
            slot_keys = [s.get('key') for s in slots]
            greetings = data.get('greetings', [])
            greeting_titles = [g.get('title') for g in greetings]
            vis = data.get('visibility')
            rev = data.get('revision')
            upd = data.get('updated_at')
            detailed_scenarios.append({
                'idx': idx + 1,
                'id': sid,
                'name': name,
                'visibility': vis,
                'revision': rev,
                'slots_count': len(slots),
                'slot_keys': slot_keys,
                'greetings_count': len(greetings),
                'greeting_titles': greeting_titles,
                'updated_at': upd
            })
            print(f"[{idx+1:2d}] {sid} | Rev: {rev} | Vis: {vis} | Slots: {len(slots)} {slot_keys[:3]} | Greetings: {len(greetings)} | Name: {name}")
    except Exception as e:
        print(f"[{idx+1:2d}] {sid} | ERROR: {e}")
    time.sleep(0.5)

with open('scratch/detailed_19_scenarios.json', 'w', encoding='utf-8') as f:
    json.dump(detailed_scenarios, f, indent=2, ensure_ascii=False)

print("\nSaved detailed inspection to scratch/detailed_19_scenarios.json")
