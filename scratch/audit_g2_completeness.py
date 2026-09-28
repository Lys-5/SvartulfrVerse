"""
Audit G2 - fase 2: identifica schede gia lavorate vs schede grezze.
Conta anche personaggi "sconosciuti" (non in G1, non in G3 ma finiti nel conteggio).
"""
import json

with open(r'd:\SvartulfrVerse\exports\Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])
real_chars = [c for c in chars if len(c.get('long_summary') or '') > 100]

g1_names_lower = [
    'erik douglas', 'malachia douglas bloodmoon', 'noah douglas bloodmoon',
    'jasper douglas bloodmoon', 'alyssa douglas bloodmoon', 'logan douglas',
    'edric douglas', 'lord cornelius douglas', 'magnus douglas iii',
    'elizabeth duskwood', 'wulfnic bloodmoon', 'ut berg', 'zefir hvitskog',
    'fenris', 'nixara bloodmoon', 'kaladin nargathon', 'marcus thornfield'
]

g3_names_partial = [
    'adrian locke', 'aeril', 'aiden anderson', 'alad', 'alistair deville',
    'amelia deville', 'amerian', 'aris thorne', 'arran parker',
    'arthur grey', 'arturo cardona', 'ashton crowley', 'atlas teague',
    'august reed', 'bartholomew', 'bram beaumont', 'caien', 'caim morningstar',
    'cato', 'charles deville', 'cyrus camden', 'dallas rhodes',
    'damien bishop', 'emlyn danes', 'eric grey', 'everett rottmore',
    'finn the satyr', 'gabriel', 'garrett locke', 'gianni luciano',
    'graham purcell', 'ignis', 'jake thompson', 'jayce collins',
    'julian bieri', 'kade leavis', 'kai mitchell', 'kai monroe',
    'lennox mckay', 'levi graham', 'lestat', 'madge', 'miles airhardt',
    'milo grayson', 'neon purr', 'nic lucero', 'nickolas wolffe',
    'park jae-sung', 'persephone', 'rafael callaway', 'rhett moore',
    'rifle maddox', 'roger', 'romeo', 'rue', 'sawyer shephard',
    'siebren dijkstra', 'talia grimwood', 'vale roberts', 'vargus',
    'vasile ionescu', 'venera dolce', 'vero walker', 'warg', 'wren lark',
    'xaiden', 'zaire', 'professor kiwetin', 'angui'
]

def classify(name):
    nl = name.lower().strip()
    if nl in g1_names_lower:
        return 'G1'
    for g3n in g3_names_partial:
        if g3n in nl or nl in g3n:
            return 'G3'
    return 'G2'

# Classify all real chars
g2_list = []
unknown = []
for c in real_chars:
    name = c.get('display_name') or c.get('name') or ''
    cls = classify(name)
    if cls == 'G2':
        outfits = len(c.get('outfits') or [])
        attitudes = len(c.get('attitudes') or [])
        se = len(c.get('speech_examples') or [])
        bd = 'si' if c.get('birthdate') is not None else 'no'
        fi = 'si' if len(c.get('final_instructions') or '') > 10 else 'no'
        ig = 'si' if c.get('is_global') == True else 'no'
        g2_list.append({
            'name': name,
            'id': c['id'],
            'ls_len': len(c.get('long_summary') or ''),
            'outfits': outfits,
            'attitudes': attitudes,
            'speech_ex': se,
            'birthdate': bd,
            'final_instr': fi,
            'is_global': ig,
        })

# Sort by pipeline completeness
def completeness(r):
    score = 0
    if r['outfits'] >= 5: score += 1
    if r['attitudes'] >= 2: score += 1
    if r['speech_ex'] >= 5: score += 1
    if r['birthdate'] == 'si': score += 1
    if r['final_instr'] == 'si': score += 1
    if r['is_global'] == 'si': score += 1
    return score

g2_list.sort(key=lambda r: completeness(r), reverse=True)

print(f"TOTALE G2: {len(g2_list)} personaggi")
print()

# Group by completeness
worked = [r for r in g2_list if completeness(r) >= 4]
partial = [r for r in g2_list if 1 <= completeness(r) < 4]
raw = [r for r in g2_list if completeness(r) == 0]

print(f"=== PIPELINE COMPLETA O QUASI ({len(worked)}) ===")
for r in worked:
    print(f"  [{completeness(r)}/6] {r['name']:40s} out={r['outfits']} att={r['attitudes']} se={r['speech_ex']} bd={r['birthdate']} fi={r['final_instr']} gl={r['is_global']}")

print(f"\n=== PIPELINE PARZIALE ({len(partial)}) ===")
for r in partial:
    print(f"  [{completeness(r)}/6] {r['name']:40s} out={r['outfits']} att={r['attitudes']} se={r['speech_ex']} bd={r['birthdate']} fi={r['final_instr']} gl={r['is_global']}")

print(f"\n=== IMPORT GREZZO ({len(raw)}) ===")
for r in raw:
    print(f"  [{completeness(r)}/6] {r['name']:40s} out={r['outfits']} att={r['attitudes']} se={r['speech_ex']} bd={r['birthdate']} fi={r['final_instr']} gl={r['is_global']}")

# Check for names I might not expect
print(f"\n=== PERSONAGGI G2 NON PREVISTI (verifica manuale) ===")
expected_g2_names = [
    'angelo moreno', 'vito marino', 'bianca rossi', 'aurora night',
    'cass harrow', 'eclipse noir', 'federico', 'isobel blackwater',
    'dominic chen', 'helena weiss', 'abel vilas', 'tomas matthews',
    'fade greymoor', 'mackenzie', 'roland vickers', 'viola', 'via carter',
    'vincent campbell', 'finnegan novak', 'jared thompson',
    'santiago herrera', 'bailey rogers', 'tomas', 'scarlett',
    'sierra', 'janice thompson', 'andrew campbell', 'brittany',
    'javier reyes', 'rev', 'professor loewe', 'richard loewe',
    'ariadne cirillo', 'dullahan', 'barkley rover', 'adelin coso',
    'coach mithers', 'hideo reid', 'mollusk moreau', 'marit christiansen',
    'casey williams', 'chase anderson', 'stanley davies jr',
    'roman blackwood', 'kolya', 'iordan', 'oskar', 'tate',
    'nikolaj', 'jean-luc virtuoso', 'alicia virtuoso', 'dante',
    'zero', 'arthur sinclair', 'kevin', 'siobhan', 'roxie',
    'rory ballantine', 'ruaraidh', 'sully', 'sullivan', 'harper aries',
    'danny boone', 'daniel', 'eithne', 'yael', 'bryson',
    'dominic rogers', 'luisa sanchez', 'allegra lumsden',
    'archer wolfwood', 'hank thompson', 'eris davies',
    'jasmin thompson', 'stanley davies sr', 'russ sinclair',
    'dean', 'eric', 'raymond',
    'danya', 'marcus o\'connor',
]

for r in g2_list:
    nl = r['name'].lower()
    matched = False
    for en in expected_g2_names:
        if en in nl or nl in en:
            matched = True
            break
    if not matched:
        print(f"  ?  {r['name']} ({r['id']})")
