import json
import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'User-Agent': 'AuditorBot/1.0'}

# 1. Compare Primary
with open(ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    local_p = json.load(f)
r_p = requests.get('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers).json()

local_p_eids = {e['entry_id']: e['name'] for e in local_p.get('lexicon', [])}
live_p_eids = {e['entry_id']: e['name'] for e in r_p.get('lexicon', [])}

print("=== PRIMARY DIFF ===")
print("Local count:", len(local_p_eids), "Live count:", len(live_p_eids))
diff_p_local_not_live = set(local_p_eids.keys()) - set(live_p_eids.keys())
diff_p_live_not_local = set(live_p_eids.keys()) - set(local_p_eids.keys())
print("Local entries not in live:", [(eid, local_p_eids[eid]) for eid in diff_p_local_not_live])
print("Live entries not in local:", [(eid, live_p_eids[eid]) for eid in diff_p_live_not_local])

# 2. Compare Secondary
with open(ROOT / 'FINAL' / 'Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    local_s = json.load(f)
r_s = requests.get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers).json()

local_s_eids = {e['entry_id']: e['name'] for e in local_s.get('lexicon', [])}
live_s_eids = {e['entry_id']: e['name'] for e in r_s.get('lexicon', [])}

print("\n=== SECONDARY DIFF ===")
print("Local count:", len(local_s_eids), "Live count:", len(live_s_eids))
diff_s_local_not_live = set(local_s_eids.keys()) - set(live_s_eids.keys())
diff_s_live_not_local = set(live_s_eids.keys()) - set(local_s_eids.keys())
print("Local entries not in live:", [(eid, local_s_eids[eid]) for eid in diff_s_local_not_live])
print("Live entries not in local:", [(eid, live_s_eids[eid]) for eid in diff_s_live_not_local])
