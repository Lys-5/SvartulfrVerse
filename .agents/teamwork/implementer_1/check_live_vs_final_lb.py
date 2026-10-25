import json
import requests
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

r = requests.get('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
live_data = r.json()

with open(ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    local_data = json.load(f)

print("Live entries count:", len(live_data.get('lexicon', [])))
print("Local entries count:", len(local_data.get('lexicon', [])))

diffs = 0
for le, fe in zip(live_data.get('lexicon', []), local_data.get('lexicon', [])):
    if le.get('name') != fe.get('name'):
        print(f"Name mismatch: {le.get('name')} vs {fe.get('name')}")
        diffs += 1
    if le.get('avatar') != fe.get('avatar'):
        print(f"{le.get('name')} avatar mismatch: live={le.get('avatar')} vs local={fe.get('avatar')}")
        diffs += 1

print(f"Total diffs: {diffs}")
