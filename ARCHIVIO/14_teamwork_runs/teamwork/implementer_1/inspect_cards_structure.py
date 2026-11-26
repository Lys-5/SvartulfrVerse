import json
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')

target_files = [
    'FINAL/Erik_Douglas_card.json',
    'FINAL/Logan_Douglas_card.json',
    'FINAL/Malachia_Douglas_Bloodmoon_card.json',
    'FINAL/Noah_Douglas_Bloodmoon_card.json',
    'FINAL/Wulfnic_Bloodmoon_card.json'
]

for tf in target_files:
    p = ROOT / tf
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"File: {p.name}")
    print(f"  Keys: {list(data.keys())[:10]}...")
    print(f"  Current Avatar: {data.get('avatar')}")
    print(f"  ID: {data.get('id')}")
    print(f"  Name: {data.get('name')}")
