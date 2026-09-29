import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])

g1_names = [
    'erik douglas', 'malachia douglas bloodmoon', 'noah douglas bloodmoon',
    'jasper douglas bloodmoon', 'alyssa douglas bloodmoon', 'logan douglas',
    'edric douglas', 'lord cornelius douglas', 'magnus douglas iii',
    'elizabeth duskwood', 'wulfnic bloodmoon', 'ut berg', 'zefir hvitskog',
    'fenris', 'nixara bloodmoon', 'kaladin nargathon', 'marcus thornfield'
]

# G2 names (86)
g2_names = [
    # Council (21)
    'cass harrow', 'naomi black', 'darius vale', 'bianca rossi', 'dominic chen',
    'aurora night', 'eclipse noir', 'isobel blackwater', 'helena weiss',
    "marcus o'connor", 'vito marino', 'angelo moreno', 'federico "riki" savini',
    'federico savini', 'harlan "huck" beaumont', 'harlan beaumont', 'zeera',
    'brak ironfist', 'barrow', 'harrison black', 'abel vilas', 'cassian aralas', 'marlowe voss',
    # Grave Mistake (4)
    'fade greymoor', 'mackenzie sanchez-rogers', 'roland vickers', 'viola carter', 'via carter',
    # Athletes (6)
    'vincent campbell', 'finnegan novak', 'jared thompson', 'santiago herrera',
    'bailey rogers', 'tomas matthews',
    # Frat / Sorority (6)
    'scarlett rose', 'sierra', 'janice thompson', 'andrew campbell', 'andy campbell',
    'brittany willow', 'rev',
    # Five Cocketeers & Roommates (5)
    'russ sinclair', 'dean', 'eric', 'raymond', 'javier reyes',
    # Staff / Faculty (10)
    'archer wolfwood', 'professor loewe', 'richard loewe', 'ariadne cirillo', 'dullahan', 'coach d',
    'barkley rover', 'adelin coso', 'coach mithers', 'hideo reid',
    'professor mollusk moreau', 'mollusk moreau', 'professor marit christiansen', 'marit christiansen',
    # Featured Students (9)
    'casey williams', 'chase anderson', 'stanley davies jr.', 'stanley davies jr',
    'roman blackwood', 'kolya varenkov', 'iordan r. vess', 'iordan vess', 'oskar', 'tate', 'nikolaj jökull', 'nikolaj jokull',
    # Featured Alumni & Familiari (4)
    'hank thompson', 'jasmin thompson', 'stanley davies sr.', 'stanley davies sr', 'eris davies',
    # Sinners (8)
    'jean-luc virtuoso', 'alicia virtuoso', 'dante', 'zero', 'dr. arthur sinclair', 'arthur sinclair',
    'gluttony - kevin', 'kevin', 'envy - siobhan', 'siobhan', 'greed - roxie', 'roxie',
    # Ballantines (4)
    'ruaraidh "rory" ballantine', 'ruaraidh ballantine', 'rory ballantine',
    'sullivan "sully" jones', 'sullivan jones', 'sully jones',
    'harper aries', 'daniel "danny" boone', 'daniel boone', 'danny boone',
    # Core Allies (6)
    "eithne dal'kereth", 'yael', 'bryson', 'dominic rogers', 'luisa sanchez rogers', 'luisa sanchez', 'allegra lumsden'
]

def clean(n):
    return (n or '').strip().lower()

g1_set = set(g1_names)
g2_set = set(g2_names)

def get_group(char):
    name = clean(char.get('display_name') or char.get('first_name', '') + ' ' + char.get('last_name', ''))
    # Exact match first
    for g1 in g1_set:
        if g1 == name: return 'G1'
    for g2 in g2_set:
        if g2 == name: return 'G2'
    # Partial / substring match
    for g1 in g1_set:
        if len(g1) > 4 and (g1 in name or name in g1): return 'G1'
    for g2 in g2_set:
        if len(g2) > 4 and (g2 in name or name in g2): return 'G2'
    return 'G3'

groups = {'G1': [], 'G2': [], 'G3': []}
for c in chars:
    grp = get_group(c)
    groups[grp].append(c)

print(f'Total chars: {len(chars)}')
print(f'G1 count: {len(groups["G1"])}')
print(f'G2 count: {len(groups["G2"])}')
print(f'G3 count: {len(groups["G3"])}')
g3_real = [c for c in groups['G3'] if len(c.get('long_summary') or '') > 100]
g3_stub = [c for c in groups['G3'] if len(c.get('long_summary') or '') <= 100]
print(f'G3 real: {len(g3_real)}, G3 stub: {len(g3_stub)}')
