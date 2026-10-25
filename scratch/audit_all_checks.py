import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

# 1. Check all 14 cards and 2 personas for RPG blocks, AGE, LEVEL, Ascended Alpha, etc.
for p in sorted(FINAL.glob('*_card.json')) + sorted((FINAL / 'personas').glob('*.json')):
    data = json.loads(p.read_text(encoding='utf-8'))
    desc = data.get('description', '')
    age_m = re.search(r'AGE:\s*([^;\]]+)', desc)
    lvl_m = re.search(r'\[LEVEL:\s*(\d+)', desc, re.I)
    rpg_m = re.search(r'(RPG STATS & TRAITS:.*)', desc, re.S)
    asc_m = re.findall(r'Ascended Alpha', json.dumps(data), re.I)
    user_m = re.findall(r'\{\{user\}\}', desc)
    out.append(f"FILE: {p.name} | AGE: {age_m.group(1) if age_m else 'N/A'} | LEVEL_IN_TEXT: {lvl_m.group(1) if lvl_m else 'N/A'} | rpg_stats.level: {(data.get('rpg_stats') or {}).get('level')} | AscendedAlpha: {len(asc_m)} | {{user}} in desc: {len(user_m)}")
    if rpg_m:
        out.append("  " + "\n  ".join(rpg_m.group(1).splitlines()[:4]))

# 2. Check the 5 new NPC Secondary entries
s2 = json.loads((FINAL / 'Svartulfr_NPC_Secondary.json').read_text(encoding='utf-8'))
for idx, e in enumerate(s2.get('entries', [])):
    if idx >= 105:
        out.append(f"\nNPC Secondary #{idx}: {e.get('name')}")
        out.append(e.get('content', ''))

# 3. Check where {{user}} or {{pronoun...}} appears across all 6 lorebooks
for lb_file in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / lb_file).read_text(encoding='utf-8'))
    for idx, e in enumerate(lb.get('entries', [])):
        c = e.get('content', '')
        k = json.dumps(e.get('keys', []))
        if '{{user}}' in c or '{{pronoun' in c or '{{user}}' in k:
            out.append(f"\nLOREBOOK {lb_file} #{idx} ({e.get('name')}) keys={e.get('keys')}:")
            for line in c.splitlines():
                if '{{user}}' in line or '{{pronoun' in line:
                    out.append(f"  LINE: {line[:200]}")

# 4. Check generic keys in NPC Primary & Secondary
GENERIC_KEYS = {'the compound', 'solarton pd', 'barista', 'bartender', 'professor', 'hex valley'}
for lb_file in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / lb_file).read_text(encoding='utf-8'))
    for idx, e in enumerate(lb.get('entries', [])):
        ks = e.get('keys', [])
        bad = [k for k in ks if k.strip().lower() in GENERIC_KEYS]
        if bad:
            out.append(f"BAD KEY in {lb_file} #{idx} ({e.get('name')}): {bad} (all keys: {ks})")

(ROOT / 'scratch' / 'audit_all_checks.txt').write_text('\n'.join(out), encoding='utf-8')
print("Done audit_all_checks")
