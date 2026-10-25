import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
final_dir = ROOT / 'FINAL'

cards = {
    'Scarlett': final_dir / 'Scarlett_Rose_card.json',
    'Sierra': final_dir / 'Sierra_Cruz_card.json',
    'Russ': final_dir / 'Russ_card.json',
    'Stan': final_dir / 'Stan_Davies_Jr_card.json',
    'Jared': final_dir / 'Jared_Thompson_card.json',
    'Alyssa': final_dir / 'Alyssa_Douglas_Bloodmoon_card.json',
}

for name, path in cards.items():
    data = json.loads(path.read_text(encoding='utf-8'))
    desc = data.get('description', '')
    avatar = data.get('avatar', '')
    print(f"{name}: desc len={len(desc)}, avatar={avatar}")
    assert len(desc) > 2000, f"{name} desc len too short: {len(desc)}"
    assert '\u2014' not in desc, f"{name} has em-dash"
    assert '{{age}}' not in desc, f"{name} has {{age}}"
    assert '{{user}}' not in desc, f"{name} has {{user}}"
    assert '\ufffd' not in desc, f"{name} has corruption"
    assert avatar.startswith('http'), f"{name} invalid avatar: {avatar}"

print("All 6 cards verified successfully!")
