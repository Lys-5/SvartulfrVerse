import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
final_dir = ROOT / 'FINAL'

cards = {
    'Scarlett Rose': final_dir / 'Scarlett_Rose_card.json',
    'Sierra Cruz': final_dir / 'Sierra_Cruz_card.json',
    "Russell 'Russ' Sinclair": final_dir / 'Russ_card.json',
    'Stanley Davies Jr.': final_dir / 'Stan_Davies_Jr_card.json',
    'Jared Thompson': final_dir / 'Jared_Thompson_card.json',
    'Alyssa Hvit Douglas Bloodmoon': final_dir / 'Alyssa_Douglas_Bloodmoon_card.json'
}

for name, path in cards.items():
    d = json.load(open(path, 'r', encoding='utf-8'))
    print(f"\n==================================================")
    print(f"NAME: {name}")
    print(f"File: {path.name}")
    print(f"Card Name: {d.get('name')}")
    print(f"Chat Name: {d.get('chat_name')}")
    print(f"Avatar: {d.get('avatar')}")
    print(f"Desc length: {len(d.get('description', ''))}")
    print(f"Has outfits: {len(d.get('outfits', []))} outfits")
    print(f"First 150 chars: {repr(d.get('description', '')[:150])}")
