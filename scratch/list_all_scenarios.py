import urllib.request
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': 'Bearer ' + token,
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json'
}

# Try with limit=50 or pagination
url = 'https://app.wyvern.chat/api/character-scenarios/mine?limit=100'
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode('utf-8'))
except Exception as e:
    print("Error fetching with limit=100:", e)
    data = None

if data:
    total = data.get('total')
    items = data.get('items', [])
    print(f"Total scenarios reported: {total}")
    print(f"Items returned: {len(items)}\n")
    
    with open('scratch/live_character_scenarios_all.json', 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    for idx, sc in enumerate(items):
        sc_id = sc.get('id')
        sc_name = sc.get('name')
        created = sc.get('created_at')
        updated = sc.get('updated_at')
        vis = sc.get('visibility')
        slots = len(sc.get('slots', []))
        greetings = len(sc.get('greetings', []))
        print(f"{idx+1:2d}. [{sc_id}] '{sc_name}' | Vis: {vis} | Slots: {slots} | Greetings: {greetings} | Created: {created} | Updated: {updated}")
else:
    # Try page by page if limit parameter is ignored
    items = []
    page = 1
    while True:
        url = f'https://app.wyvern.chat/api/character-scenarios/mine?page={page}&limit=12'
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        batch = data.get('items', [])
        if not batch:
            break
        items.extend(batch)
        print(f"Page {page}: got {len(batch)} items")
        if len(items) >= data.get('total', 0):
            break
        page += 1

    with open('scratch/live_character_scenarios_all.json', 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    print(f"\nTotal collected: {len(items)}\n")
    for idx, sc in enumerate(items):
        sc_id = sc.get('id')
        sc_name = sc.get('name')
        created = sc.get('created_at')
        updated = sc.get('updated_at')
        vis = sc.get('visibility')
        slots = len(sc.get('slots', []))
        greetings = len(sc.get('greetings', []))
        print(f"{idx+1:2d}. [{sc_id}] '{sc_name}' | Vis: {vis} | Slots: {slots} | Greetings: {greetings} | Created: {created} | Updated: {updated}")
