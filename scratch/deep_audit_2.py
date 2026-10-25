import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
OPT = ROOT / 'lorebooks' / 'optimized'

print("=== 1. CHECKING CAMP MYSTIC IN SVARTULFR_LOCATION.JSON ===")
loc_lb = json.loads((FINAL / 'Svartulfr_Location.json').read_text(encoding='utf-8'))
for e in loc_lb['entries']:
    if 'camp mystic' in e.get('name', '').lower():
        print("Found in Svartulfr_Location.json:", e['name'])
        print("Keys:", e.get('keys'))
        print("Secondary keys:", e.get('secondary_keys'))
        print("Content:\n", e.get('content'))

print("\n=== 2. CHECKING ALL 35 ENTRIES OF SVARTULFR_LOREBOOK_III.JSON ===")
lb3 = json.loads((FINAL / 'Svartulfr_Lorebook_III.json').read_text(encoding='utf-8'))
for idx, e in enumerate(lb3['entries']):
    print(f"  [{idx:02d}] {e.get('name')} (type={e.get('type')}, keys={e.get('keys')})")

print("\n=== 3. CHECKING ALL 14 CARDS & 3 PERSONAS FOR RESIDUAL ISSUES ===")
all_cards = sorted(FINAL.glob('*_card.json')) + sorted((FINAL / 'personas').glob('*.json'))
for p in all_cards:
    d = json.loads(p.read_text(encoding='utf-8'))
    raw = json.dumps(d, ensure_ascii=False)
    issues = []
    if '—' in raw:
        # check which field has em-dash
        fields_with_em = [k for k, v in d.items() if isinstance(v, str) and '—' in v]
        for o in d.get('outfits', []):
            if '—' in json.dumps(o, ensure_ascii=False):
                fields_with_em.append(f"outfit:{o.get('name')}")
        issues.append(f"em-dash in {fields_with_em}")
    if '{{pronoun' in raw:
        issues.append("residual {{pronoun...}}")
    if '{{age}}' in raw:
        issues.append("residual {{age}}")
    if 'MGT' in raw or 'RES' in raw or 'WIT' in raw or 'PRS' in raw or 'SCT' in raw:
        # check if word boundary
        if re.search(r'\b(MGT|RES|WIT|PRS|SCT)\b', raw):
            issues.append("legacy 6-stat acronym")
    if 'Ascended Alpha' in raw:
        issues.append("Ascended Alpha")
    if '[INSTRUCTIONS:' in raw:
        issues.append("[INSTRUCTIONS:")
    # Check {{user}} in description, long_summary, personality, summary, character_note, system_prompt
    for k in ('description', 'long_summary', 'personality', 'summary', 'character_note', 'system_prompt'):
        v = d.get(k, '')
        if isinstance(v, str) and '{{user}}' in v:
            # Find context of {{user}}
            contexts = [m.group(0) for m in re.finditer(r'.{0,40}\{\{user\}\}.{0,40}', v)]
            issues.append(f"{{{{user}}}} in {k}: {contexts}")
    # Check outfits count and schema
    outfits = d.get('outfits', [])
    for o in outfits:
        if not ('id' in o and 'name' in o and 'description' in o):
            issues.append(f"bad outfit schema: {list(o.keys())}")
    print(f"{p.name}: outfits={len(outfits)}, issues={issues}")

print("\n=== 4. CHECKING ALL 6 LOREBOOKS FOR RESIDUAL ISSUES ===")
for fn in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / fn).read_text(encoding='utf-8'))
    opt_lb = json.loads((OPT / fn).read_text(encoding='utf-8'))
    entries = lb.get('entries', [])
    issues = []
    if lb != opt_lb:
        issues.append("FINAL != optimized")
    if 'lexicon' in lb and lb['lexicon'] != entries:
        issues.append("entries != lexicon")
    for idx, e in enumerate(entries):
        c = e.get('content', '')
        if '{{user}}' in c or '{{user}}' in e.get('name', ''):
            issues.append(f"entry {idx} ({e.get('name')}) has {{{{user}}}}")
        if '{{pronoun' in c:
            issues.append(f"entry {idx} ({e.get('name')}) has {{{{pronoun}}}}")
        if '{{age}}' in c:
            issues.append(f"entry {idx} ({e.get('name')}) has {{{{age}}}}")
        if '[INSTRUCTIONS:' in c:
            issues.append(f"entry {idx} ({e.get('name')}) has [INSTRUCTIONS:")
        if '—' in c or '*' in c:
            issues.append(f"entry {idx} ({e.get('name')}) has — or *")
        if re.search(r'\b(MGT|RES|WIT|PRS|SCT)\b', c):
            issues.append(f"entry {idx} ({e.get('name')}) has legacy 6-stat")
        if e.get('selective') is True and not e.get('secondary_keys'):
            issues.append(f"entry {idx} ({e.get('name')}) has selective=True with empty secondary_keys")
        if not e.get('keys'):
            issues.append(f"entry {idx} ({e.get('name')}) has empty keys")
        if e.get('enabled') is False:
            issues.append(f"entry {idx} ({e.get('name')}) is disabled")
    print(f"{fn}: {len(entries)} entries, issues={issues}")
