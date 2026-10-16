import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

# Check Ariadne in NPC Primary & Secondary
for fname in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    data = json.loads((ROOT / 'FINAL' / fname).read_text(encoding='utf-8'))
    entries = data.get('lexicon') or data.get('entries') or []
    for idx, e in enumerate(entries):
        if 'Ariadne' in e.get('name', '') or 'Cirillo' in e.get('name', ''):
            print(f"Found Ariadne in {fname} idx={idx}: {e.get('name')}")

# Check Rogers Bargain Motors in entire repo
print("\nSearching Rogers Bargain Motors:")
for p in ROOT.glob('**/*.json'):
    if 'node_modules' in str(p) or '.git' in str(p):
        continue
    try:
        txt = p.read_text(encoding='utf-8', errors='ignore')
        if "Rogers' Bargain Motors" in txt:
            print(f"  -> {p.relative_to(ROOT)}")
    except Exception:
        pass
