import json

p_primary = 'FINAL/Svartulfr_NPC_Primary.json'
p_secondary = 'FINAL/Svartulfr_NPC_Secondary.json'

d_p = json.load(open(p_primary, encoding='utf-8'))
d_s = json.load(open(p_secondary, encoding='utf-8'))

targets_primary = ['Erik', 'Malachia', 'Noah', 'Logan', 'Wulfnic', 'Mackenzie']
print("=== TARGETS IN PRIMARY ===")
for e in d_p.get('lexicon', []):
    for t in targets_primary:
        if t.lower() in e.get('name', '').lower():
            print(f"Primary match for {t}: id={e.get('entry_id')}, name={e.get('name')}, content_len={len(e.get('content', ''))}")

print("\n=== TARGETS IN SECONDARY ===")
for e in d_s.get('lexicon', []):
    if 'edric' in e.get('name', '').lower():
        print(f"Secondary match for Edric: id={e.get('entry_id')}, name={e.get('name')}, content_len={len(e.get('content', ''))}")
