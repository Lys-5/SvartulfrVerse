import json
import re

with open(r'exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])
real_chars = {c['id']: c for c in chars if len(c.get('long_summary') or '') > 100}

# Filter out G1 (17) and G3 (69/72)
g1_names_lower = [
    'erik douglas', 'malachia douglas bloodmoon', 'noah douglas bloodmoon',
    'jasper douglas bloodmoon', 'alyssa douglas bloodmoon', 'logan douglas',
    'edric douglas', 'lord cornelius douglas', 'magnus douglas iii',
    'elizabeth duskwood', 'wulfnic bloodmoon', 'ut berg', 'zefir hvitskog',
    'fenris', 'nixara bloodmoon', 'kaladin nargathon', 'marcus thornfield'
]

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

g2_list = []
for cid, c in real_chars.items():
    name = c.get('display_name') or c.get('name') or ''
    if not is_g1(name) and not is_g3(name):
        g2_list.append(c)

print(f"Total G2 characters: {len(g2_list)}")

# Check ages and birthdays
with_birthdate = [c for c in g2_list if c.get('birthdate')]
without_birthdate = [c for c in g2_list if not c.get('birthdate')]
print(f"G2 with birthdate: {len(with_birthdate)}")
print(f"G2 without birthdate: {len(without_birthdate)}")

# Extract AGE and BIRTHDAY patterns from long_summary / summary
print("\nExtracting Age/Birthday info for G2 without birthdate:")
for c in without_birthdate[:25]:
    dn = c.get('display_name')
    ls = c.get('long_summary') or ''
    s = c.get('summary') or ''
    text = ls + ' ' + s
    
    age_match = re.search(r'AGE:\s*([^;\]\n]+)', text, re.I)
    bday_match = re.search(r'BIRTH(?:DAY|DATE):\s*([^;\]\n]+)', text, re.I)
    
    age_str = age_match.group(1).strip() if age_match else 'N/A'
    bday_str = bday_match.group(1).strip() if bday_match else 'N/A'
    print(f"  {dn:30s} | ID: {c.get('id'):22s} | Age: {age_str[:15]:15s} | BDay: {bday_str[:20]}")
