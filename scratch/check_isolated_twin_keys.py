import json

lorebooks = [
    'FINAL/Svartulfr_Lorebook_I.json',
    'FINAL/Svartulfr_Lorebook_II.json',
    'FINAL/Svartulfr_Lorebook_III.json',
    'FINAL/Svartulfr_Location.json',
    'FINAL/Svartulfr_NPC_Primary.json',
    'FINAL/Svartulfr_NPC_Secondary.json'
]
single_keys = {}
for lb in lorebooks:
    d = json.load(open(lb, encoding='utf-8'))
    for idx, e in enumerate(d.get('entries', [])):
        for k in e.get('keys', []):
            kl = k.lower()
            if kl in ['alyssa', 'jasper']:
                clean_n = e.get('name', '').encode('ascii', 'ignore').decode('ascii')
                single_keys.setdefault(kl, []).append((lb, idx, clean_n, e.get('keys'), e.get('selective'), e.get('secondary_keys')))

for kl, lst in single_keys.items():
    print(f'=== Trigger key "{kl}" ===')
    for item in lst:
        print(' ', item[0], 'idx=' + str(item[1]), item[2])
        print('    keys:', item[3])
        print('    selective:', item[4], 'sec_keys:', item[5])
