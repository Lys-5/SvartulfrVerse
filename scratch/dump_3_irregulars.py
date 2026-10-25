import json

sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))
s_lex = sec.get('lexicon', [])

target_ids = {
    "NQd7n3QacMcK-TzowQ2LE": "Bruce",
    "oov5UWuVhZ3RGgoxMkaTS": "Campus Staff Rat",
    "Og7V6v67guXXAaP0_PsTM": "Adrian"
}

for e in s_lex:
    eid = e.get('entry_id')
    if eid in target_ids:
        print(json.dumps(e, indent=2))
