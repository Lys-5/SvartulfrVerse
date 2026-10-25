import json

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

all_entries = [("Primary", e) for e in prim.get('lexicon', [])] + [("Secondary", e) for e in sec.get('lexicon', [])]

em_dash_matches = []
en_dash_matches = []

for origin, e in all_entries:
    eid = e.get('entry_id', '')
    name = e.get('name', '')
    content = e.get('content', '')
    
    # check explicit codepoints
    if '\u2014' in content:
        cnt = content.count('\u2014')
        em_dash_matches.append((origin, eid, name, cnt))
    if '\u2013' in content:
        cnt = content.count('\u2013')
        en_dash_matches.append((origin, eid, name, cnt))

print(f"Total entries with \\u2014 (em-dash): {len(em_dash_matches)}, total count: {sum(x[3] for x in em_dash_matches)}")
for x in em_dash_matches:
    print(f"  {x}")

print(f"Total entries with \\u2013 (en-dash): {len(en_dash_matches)}, total count: {sum(x[3] for x in en_dash_matches)}")
for x in en_dash_matches[:10]:
    print(f"  {x}")
