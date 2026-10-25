import urllib.request
import json
import time

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()

def api_put(endpoint, payload):
    url = f'https://app.wyvern.chat/api{endpoint}'
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='PUT'
    )
    res = urllib.request.urlopen(req, timeout=30)
    return res.status, json.loads(res.read())

deploy_targets = [
    {
        'id': '_HfG7TeV6MJyj6bxMwxkpt',
        'file': 'FINAL/Svartulfr_Lorebook_II.json',
        'name': 'Svartúlfr - Lorebook II'
    },
    {
        'id': '_9zWTGqYJNJ4BCDMj8gfcD',
        'file': 'FINAL/Svartulfr_Lorebook_III.json',
        'name': 'Svartúlfr - Lorebook III'
    },
    {
        'id': '_EjXxkmPVhpCXg8xABpFkK',
        'file': 'FINAL/Svartulfr_Location.json',
        'name': 'Svartúlfr - Location'
    }
]

print("=== DEPLOYING UPDATED LOREBOOKS TO APP.WYVERN.CHAT ===")

for target in deploy_targets:
    lid = target['id']
    fpath = target['file']
    tname = target['name']
    
    with open(fpath, 'r', encoding='utf-8') as f:
        src = json.load(f)
    
    entries = src.get('lexicon') or src.get('entries') or []
    payload = {
        'name': src.get('name', tname),
        'description': src.get('description', ''),
        'visibility': src.get('visibility', 'private'),
        'rating': src.get('rating', 'explicit'),
        'scan_depth': src.get('scan_depth', 5),
        'token_budget': src.get('token_budget', 5000),
        'recursive_scanning': src.get('recursive_scanning', True),
        'lexicon': entries
    }
    
    print(f"Deploying {tname} ({lid}) - items={len(entries)}...")
    st, res = api_put(f'/lorebooks/{lid}', payload)
    print(f"  -> Result: status={st}, live_lexicon={len(res.get('lexicon', []))}")
    time.sleep(2.5)

print("\nDeployment completed successfully!")
