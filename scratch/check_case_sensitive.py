import os, json, re

for fname in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    path = os.path.join('FINAL', fname)
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"=== {fname} ===")
    case_sens_counts = {}
    for idx, e in enumerate(d['lexicon']):
        cs = e.get('case_sensitive')
        case_sens_counts[cs] = case_sens_counts.get(cs, 0) + 1
    print("case_sensitive counts:", case_sens_counts)
