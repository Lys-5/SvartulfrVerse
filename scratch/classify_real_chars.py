import json

with open(r'd:\SvartulfrVerse\exports\Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])
real_chars = [c for c in chars if len(c.get('long_summary') or '') > 100]

g1_names = [
    'Erik Douglas', 'Malachia Douglas Bloodmoon', 'Noah Douglas Bloodmoon',
    'Jasper Douglas Bloodmoon', 'Alyssa Douglas Bloodmoon', 'Logan Douglas',
    'Edric Douglas', 'Lord Cornelius Douglas', 'Magnus Douglas III',
    'Elizabeth Duskwood', 'Wulfnic Bloodmoon', 'Ut Berg', 'Zefir Hvitskog',
    'Fenris', 'Nixara Bloodmoon', 'Kaladin Nargathon', 'Marcus Thornfield'
]

g2_names = [
    # Council
    'Cass Harrow', 'Naomi Black', 'Darius Vale', 'Bianca Rossi', 'Dominic Chen',
    'Aurora Night', 'Eclipse Noir', 'Isobel Blackwater', 'Helena Weiss',
    'Marcus O\'Connor', 'Vito Marino', 'Angelo Moreno', 'Federico "Riki" Savini',
    'Harlan Beaumont', 'Zeera', 'Brak Ironfist', 'Barrow', 'Harrison Black',
    'Abel Vilas', 'Cassian Aralas', 'Marlowe Voss',
    # Band
    'Fade Greymoor', 'Mackenzie Sanchez-Rogers', 'Roland Vickers', 'Viola Carter',
    # Athletes
    'Vincent Campbell', 'Finnegan Novak', 'Jared Thompson', 'Santiago Herrera',
    'Bailey Rogers', 'Tomas Matthews',
    # Frat & Sororities
    'Scarlett Rose', 'Sierra', 'Janice Thompson', 'Andrew Campbell',
    'Brittany Willow', 'Javier Reyes', 'Rev',
    # Staff
    'Professor Loewe', 'Ariadne Cirillo', 'Dullahan', 'Barkley Rover',
    'Adelin Coso', 'Coach Mithers', 'Hideo Reid', 'Professor Mollusk Moreau',
    'Professor Marit Christiansen',
    # Featured Students
    'Casey Williams', 'Chase Anderson', 'Stanley Davies Jr.', 'Roman Blackwood',
    'Kolya Varenkov', 'Iordan R. Vess', 'Oskar', 'Tate', 'Nikolaj Jökull',
    # Sinners
    'Jean-Luc Virtuoso', 'Alicia Virtuoso', 'Dante', 'Zero', 'Dr. Arthur Sinclair',
    'GLUTTONY - Kevin', 'ENVY - Siobhan', 'GREED - Roxie',
    # Ballantines
    'Ruaraidh "Rory" Ballantine', 'Sullivan "Sully" Jones', 'Harper Aries', 'Daniel "Danny" Boone',
    # Core Allies & Relatives
    'Eithne Dal\'Kereth', 'Yael', 'Bryson', 'Dominic Rogers', 'Luisa Sanchez Rogers', 'Allegra Lumsden'
]

def clean_name(n):
    return (n or '').strip().lower()

g1_clean = [clean_name(n) for n in g1_names]
g2_clean = [clean_name(n) for n in g2_names]

classified = []
g3_chars = []

for c in real_chars:
    cname = c.get('display_name') or c.get('name') or ''
    cname_clean = clean_name(cname)
    
    # check match
    match_g1 = any(gn in cname_clean or cname_clean in gn for gn in g1_clean)
    match_g2 = any(gn in cname_clean or cname_clean in gn for gn in g2_clean)
    
    if match_g1:
        c['assigned_group'] = 'G1'
    elif match_g2:
        c['assigned_group'] = 'G2'
    else:
        c['assigned_group'] = 'G3'
        g3_chars.append(c)

print(f"Total real: {len(real_chars)}")
print(f"G1 count: {len([c for c in real_chars if c.get('assigned_group') == 'G1'])}")
print(f"G2 count: {len([c for c in real_chars if c.get('assigned_group') == 'G2'])}")
print(f"G3 count: {len(g3_chars)}")

print("\n--- G3 CHARACTERS LIST ---")
for c in sorted(g3_chars, key=lambda x: x.get('display_name') or x.get('name')):
    name = c.get('display_name') or c.get('name')
    print(f"- {name} (ID: {c['id']})")
