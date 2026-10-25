import json

with open('FINAL/Svartulfr_Lorebook_I.json', 'r', encoding='utf-8') as f:
    lb1 = json.load(f)

e = lb1['entries'][217]
print("=== LB1 ENTRY 217 ===")
print("comment:", e.get('comment'))
for line in e.get('content', '').split('\n'):
    if 'Edric' in line or '12' in line or '13' in line or 'Presentazione' in line:
        print("  ", line)
