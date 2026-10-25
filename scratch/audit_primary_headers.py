import json
import re

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
p_lex = prim.get('lexicon', [])

print("=== DETAILED HEADER AUDIT FOR PRIMARY LOREBOOK (99 entries) ===")

entries_summary = []

for idx, e in enumerate(p_lex):
    eid = e.get('entry_id', '')
    name = e.get('name', '')
    content = e.get('content', '')
    
    # 1. Bracket start
    starts_bracket = content.strip().startswith('[')
    
    # 2. Check for BACKSTORY
    has_bs = 'BACKSTORY:' in content
    
    # 3. Check for FAMILY & PACK or CLAN AND COMPANY or equivalents
    has_fp = 'FAMILY & PACK:' in content
    has_cc = 'CLAN AND COMPANY:' in content or 'CLAN & COMPANY:' in content
    # any other family/clan variant?
    fam_variants = re.findall(r'^[A-Z0-9\s&/\-]+(?:FAMILY|PACK|CLAN|COMPANY)[A-Z0-9\s&/\-]*:', content, re.M)
    
    # 4. Check for VOICE & BEHAVIOR or variants
    has_vb = 'VOICE & BEHAVIOR:' in content
    voice_variants = re.findall(r'^[A-Z0-9\s&/\-]+VOICE[A-Z0-9\s&/\-]*:', content, re.M)
    
    # 5. Thematic closure
    # check for thematic section at end
    lines = [l.strip() for l in content.strip().split('\n') if l.strip()]
    last_headers = []
    for l in lines[-5:]:
        if (l.startswith('[') and l.endswith(']') and ';' not in l) or (re.match(r'^[A-Z0-9\s&/\-]+:', l) and not l.startswith('http')):
            last_headers.append(l)
            
    entries_summary.append({
        'id': eid,
        'name': name,
        'type': e.get('type'),
        'starts_bracket': starts_bracket,
        'has_bs': has_bs,
        'has_fp': has_fp,
        'has_cc': has_cc,
        'fam_variants': fam_variants,
        'has_vb': has_vb,
        'voice_variants': voice_variants,
        'last_headers': last_headers,
        'len': len(content)
    })

print(f"Total entries: {len(entries_summary)}")
missing_bs = [x for x in entries_summary if not x['has_bs']]
print(f"\nEntries missing 'BACKSTORY:' ({len(missing_bs)}):")
for x in missing_bs:
    print(f"  - {x['id']} ({x['name']}) [type={x['type']}, len={x['len']}]")

missing_fam = [x for x in entries_summary if not (x['has_fp'] or x['has_cc'])]
print(f"\nEntries missing 'FAMILY & PACK:' / 'CLAN AND COMPANY:' ({len(missing_fam)}):")
for x in missing_fam:
    print(f"  - {x['id']} ({x['name']}) fam_variants={x['fam_variants']}")

missing_vb = [x for x in entries_summary if not x['has_vb']]
print(f"\nEntries missing 'VOICE & BEHAVIOR:' ({len(missing_vb)}):")
for x in missing_vb:
    print(f"  - {x['id']} ({x['name']}) voice_variants={x['voice_variants']}")
