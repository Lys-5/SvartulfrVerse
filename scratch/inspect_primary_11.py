import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
ids = [
    '2TBKoO687RDfWiTVFMbaJ', # Marek
    'zlW_PSDs-w17mZqXA8WOY', # Kian
    'w-wcHqVIIvpNhN2kJh_NW', # Goran
    'T-11cZKiuLPINjkJwyiQ0', # Radek
    'p6pFnpGB9kQihhdPqcuht', # Echo
    'TG-Nl8HyTHt4QWaUW4nhm', # Dominic Rogers
    '4NzXF4_0hYxmN7Idltzpw', # Scarlett Rose
    'ijy8vrlphNv19-p-gbYuY', # Sierra Cruz
    'YCxAqNoShpefVvk0_Pc7i', # Russell 'Russ' Sinclair
    '98DR0Xp_0gCt65iaWdEHC', # Daniel "Danny" Boone
    '-cqjaQ-D7fXpypzGFhwJW', # Zero
]

for e in d['lexicon']:
    if e['entry_id'] in ids:
        print(f"=== {e['entry_id']} | {e['name']} ===")
        print(e['content'][:1500])
        print()
