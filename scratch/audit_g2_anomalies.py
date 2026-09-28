"""
Audit sistematico delle 86 schede G2 dal Svartulfr_Export.json.
Controlla: long_summary vuoto, summary vuoto, display_description vuoto,
outfits <5, speech_examples <5, attitudes mancanti Alyssa/Jasper,
birthdate mancante, start_timeline_position mancante o != birthdate,
final_instructions mancante, {{user}} residuo, em-dash residuo,
is_global false, e markdown grassetto ** residuo.
"""
import json
import re

with open(r'd:\SvartulfrVerse\exports\Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])
real_chars = {c['id']: c for c in chars if len(c.get('long_summary') or '') > 100}

# G1 IDs (17)
g1_names_lower = [
    'erik douglas', 'malachia douglas bloodmoon', 'noah douglas bloodmoon',
    'jasper douglas bloodmoon', 'alyssa douglas bloodmoon', 'logan douglas',
    'edric douglas', 'lord cornelius douglas', 'magnus douglas iii',
    'elizabeth duskwood', 'wulfnic bloodmoon', 'ut berg', 'zefir hvitskog',
    'fenris', 'nixara bloodmoon', 'kaladin nargathon', 'marcus thornfield'
]

# G3 names (69) - these are NOT G2
g3_names_lower = [
    'adrian locke', 'aeril royen', 'aiden anderson', 'alad c.',
    'alistair deville', 'amelia deville', 'amerian de vian', 'angui',
    'aris thorne', 'arran parker', 'arthur grey', 'arturo cardona',
    'ashton crowley', 'atlas teague', 'august reed', 'bartholomew',
    'bram beaumont', 'caien vaelion', 'caim morningstar', 'cato',
    'charles', 'cyrus camden', 'dallas rhodes', 'damien bishop',
    'emil', 'emlyn danes', 'eric grey', 'everett rottmore',
    'finn the satyr', 'gabriel', 'garrett locke', 'gianni luciano',
    'graham purcell', 'ignis', 'jake thompson', 'jayce collins',
    'julian bieri', 'kade leavis', 'kai mitchell', 'kai monroe',
    'lennox mckay', 'levi graham', 'lestat', 'madge', 'marek',
    'miles airhardt', 'milo grayson', 'neon purr', 'nic lucero',
    'nickolas wolffe', 'park jae-sung', 'persephone',
    'rafael callaway', 'raymond', 'rhett moore', 'rifle maddox',
    'roger', 'romeo', 'rue', 'sawyer shephard',
    'siebren dijkstra', 'talia grimwood', 'vale roberts',
    'vargus', 'vasile ionescu', 'venera dolce', 'vero walker',
    'warg', 'wren lark', 'xaiden nershatar', 'zaire ziisis'
]

def is_g1(name):
    return name.lower() in g1_names_lower

def is_g3(name):
    nl = name.lower()
    return any(g3n in nl or nl in g3n for g3n in g3_names_lower)

# Find G2 characters
g2_chars = []
for cid, c in real_chars.items():
    name = c.get('display_name') or c.get('name') or ''
    if not is_g1(name) and not is_g3(name):
        g2_chars.append(c)

print(f"G2 characters found: {len(g2_chars)}")

# Alyssa and Jasper IDs for attitude check
alyssa_id = None
jasper_id = None
for c in chars:
    dn = (c.get('display_name') or '').lower()
    if 'alyssa douglas' in dn:
        alyssa_id = c['id']
    if 'jasper douglas' in dn:
        jasper_id = c['id']

print(f"Alyssa ID: {alyssa_id}, Jasper ID: {jasper_id}")

# Audit
anomalies = []

for c in g2_chars:
    name = c.get('display_name') or c.get('name') or ''
    cid = c['id']
    issues = []
    
    # 1. long_summary check
    ls = c.get('long_summary') or ''
    if len(ls) < 500:
        issues.append(f"long_summary troppo corto ({len(ls)} chars)")
    
    # 2. summary check
    s = c.get('summary') or ''
    if len(s) < 20:
        issues.append(f"summary vuoto/troppo corto ({len(s)} chars)")
    
    # 3. display_description check
    dd = c.get('display_description') or ''
    if len(dd) < 5:
        issues.append("display_description vuota")
    
    # 4. outfits count
    outfits = c.get('outfits') or []
    if len(outfits) < 5:
        issues.append(f"outfits: {len(outfits)}/5")
    
    # 5. speech_examples count
    se = c.get('speech_examples') or []
    if len(se) < 5:
        issues.append(f"speech_examples: {len(se)}/5")
    
    # 6. attitudes check (Alyssa + Jasper)
    attitudes = c.get('attitudes') or []
    att_targets = [a.get('target_id') for a in attitudes]
    if alyssa_id and alyssa_id not in att_targets:
        issues.append("MISSING Attitude -> Alyssa")
    if jasper_id and jasper_id not in att_targets:
        issues.append("MISSING Attitude -> Jasper")
    if len(attitudes) == 0:
        issues.append("ZERO attitudes!")
    
    # 7. birthdate check
    bd = c.get('birthdate')
    if bd is None:
        issues.append("birthdate NULL")
    
    # 8. start_timeline_position check
    stp = c.get('start_timeline_position')
    if stp is None:
        issues.append("start_timeline_position NULL")
    elif bd is not None and stp != bd:
        issues.append(f"birthdate ({bd}) != start_timeline_position ({stp})")
    
    # 9. final_instructions check
    fi = c.get('final_instructions') or ''
    if len(fi) < 10:
        issues.append("final_instructions vuoto")
    
    # 10. {{user}} residuo
    all_text = ' '.join([
        ls, s, dd, fi,
        ' '.join([se_item.get('text', '') for se_item in se]),
        ' '.join([a.get('reasoning', '') for a in attitudes])
    ])
    if '{{user}}' in all_text:
        issues.append("{{user}} TROVATO!")
    
    # 11. em-dash residuo
    if '\u2014' in all_text:
        issues.append("Em-dash trovato")
    
    # 12. markdown bold ** residuo
    if '**' in all_text:
        issues.append("Grassetto markdown ** trovato")
    
    # 13. is_global check
    ig = c.get('is_global')
    if ig is not True:
        issues.append(f"is_global: {ig} (dovrebbe essere true)")
    
    if issues:
        anomalies.append((name, cid, issues))

# Output
anomalies.sort(key=lambda x: len(x[2]), reverse=True)

print(f"\n{'='*80}")
print(f"AUDIT G2 COMPLETATO: {len(g2_chars)} schede analizzate")
print(f"Schede con anomalie: {len(anomalies)}")
print(f"Schede pulite: {len(g2_chars) - len(anomalies)}")
print(f"{'='*80}\n")

if anomalies:
    for name, cid, issues in anomalies:
        print(f"\n--- {name} ({cid}) ---")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")

# Summary by issue type
issue_counts = {}
for _, _, issues in anomalies:
    for issue in issues:
        key = issue.split('(')[0].split(':')[0].strip()
        issue_counts[key] = issue_counts.get(key, 0) + 1

print(f"\n{'='*80}")
print("RIEPILOGO PER TIPO DI ANOMALIA:")
for k, v in sorted(issue_counts.items(), key=lambda x: -x[1]):
    print(f"  {v:3d}x  {k}")
