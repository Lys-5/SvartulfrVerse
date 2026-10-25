import urllib.request
import json
import time

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()

def api_put(endpoint, payload):
    url = f'https://app.wyvern.chat/api{endpoint}'
    data = json.dumps(payload).encode('utf-8')
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
    res = urllib.request.urlopen(req, timeout=15)
    return res.status, json.loads(res.read())

print("=== 1. DEPLOYING HARDENED LOREBOOK II ===")
lb2 = json.load(open('FINAL/Svartulfr_Lorebook_II.json', encoding='utf-8'))
st, res = api_put('/lorebooks/_HfG7TeV6MJyj6bxMwxkpt', lb2)
print(f"Lorebook II -> status={st} lexicon={len(res.get('lexicon', []))}")
time.sleep(2.5)

print("\n=== 2. DEPLOYING HARDENED NPC PRIMARY ===")
npcp = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
st, res = api_put('/lorebooks/_zwEqgEEzh12X6gHVmMKKC', npcp)
print(f"NPC Primary -> status={st} lexicon={len(res.get('lexicon', []))}")
time.sleep(2.5)

print("\n=== 3. DEPLOYING MASTER SCENARIO (REV 21) ===")
sc = json.load(open('FINAL/Svartulfr_Master_Scenario.json', encoding='utf-8'))
st, res = api_put('/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', sc)
print(f"Master Scenario -> status={st} rev={res.get('revision')}")

print("\nAll deployments complete!")
