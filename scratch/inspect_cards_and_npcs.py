import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'

# 1. Check all cards in FINAL/ for RPG STATS & TRAITS and [INSTRUCTIONS
print("=== CARDS IN FINAL/ ===")
for p in sorted(FINAL.glob('*_card.json')):
    c = json.loads(p.read_text(encoding='utf-8'))
    desc = c.get('description', '')
    phi = c.get('post_history_instructions', '')
    has_rpg = 'RPG STATS & TRAITS:' in desc
    has_instr = '[INSTRUCTIONS' in desc
    rpg_snip = ''
    if has_rpg:
        rpg_snip = desc[desc.index('RPG STATS & TRAITS:'):].splitlines()[:3]
    print(f"  {p.name:36s} | id={c.get('id')} | outfits={len(c.get('outfits', [])):2d} | phi={bool(phi)} | instr={has_instr} | rpg={rpg_snip}")

# 2. Check the 5 entries in NPC Secondary (Thrakgor, Crowe, Morgeth, Thorvald, Harald)
sec = json.loads((FINAL / 'Svartulfr_NPC_Secondary.json').read_text(encoding='utf-8'))
print("\n=== LAST 5 ENTRIES IN NPC SECONDARY ===")
for idx in range(len(sec['lexicon']) - 5, len(sec['lexicon'])):
    e = sec['lexicon'][idx]
    print(f"--- #{idx}: {e.get('name')} ---")
    print(e.get('content'))

# 3. Print all [INSTRUCTIONS...] matches in NPC Primary and NPC Secondary
for lb_name in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / lb_name).read_text(encoding='utf-8'))
    print(f"\n=== [INSTRUCTIONS] IN {lb_name} ===")
    for idx, e in enumerate(lb['lexicon']):
        content = e.get('content', '')
        matches = re.findall(r'\[INSTRUCTIONS:.*?\]', content, flags=re.DOTALL)
        if matches:
            print(f"  #{idx:02d} {e.get('name')}: {len(matches)} match(es) -> {matches[0][:100]!r}")
