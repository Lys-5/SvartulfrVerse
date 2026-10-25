import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'

out = []
out.append("=== CARDS IN FINAL/ ===")
for p in sorted(FINAL.glob('*_card.json')):
    c = json.loads(p.read_text(encoding='utf-8'))
    desc = c.get('description', '')
    phi = c.get('post_history_instructions', '')
    has_rpg = 'RPG STATS & TRAITS:' in desc
    has_instr = '[INSTRUCTIONS' in desc
    rpg_snip = ''
    if has_rpg:
        rpg_snip = desc[desc.index('RPG STATS & TRAITS:'):]
    out.append(f"--- {p.name} (id={c.get('id')}, outfits={len(c.get('outfits', []))}, phi={bool(phi)}, instr={has_instr}) ---")
    out.append(rpg_snip if has_rpg else "NO RPG STATS & TRAITS BLOCK")

sec = json.loads((FINAL / 'Svartulfr_NPC_Secondary.json').read_text(encoding='utf-8'))
out.append("\n=== LAST 5 ENTRIES IN NPC SECONDARY ===")
for idx in range(len(sec['lexicon']) - 5, len(sec['lexicon'])):
    e = sec['lexicon'][idx]
    out.append(f"--- #{idx}: {e.get('name')} ---")
    out.append(e.get('content'))

(ROOT / 'scratch' / 'cards_and_5npcs_rpg.txt').write_text('\n'.join(out), encoding='utf-8')
print("Wrote scratch/cards_and_5npcs_rpg.txt")
