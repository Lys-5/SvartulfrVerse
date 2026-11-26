import json
from pathlib import Path

files_to_check = [
    Path('FINAL/Edric_Douglas_card.json'),
    Path('FINAL/Erik_Douglas_card.json'),
    Path('FINAL/Jasper_Douglas_Bloodmoon_card.json'),
    Path('FINAL/Logan_Douglas_card.json'),
    Path('FINAL/Mackenzie_Sanchez_Rogers_card.json'),
    Path('FINAL/Malachia_Douglas_Bloodmoon_card.json'),
    Path('FINAL/Noah_Douglas_Bloodmoon_card.json'),
    Path('FINAL/Wulfnic_Bloodmoon_card.json'),
    Path('FINAL/Svartulfr_NPC_Primary.json'),
    Path('FINAL/Svartulfr_NPC_Secondary.json'),
    Path('FINAL/Svartulfr_Lorebook_I.json'),
    Path('FINAL/Svartulfr_Lorebook_II.json'),
    Path('FINAL/Svartulfr_Lorebook_III.json'),
    Path('FINAL/Svartulfr_Location.json'),
]

print("="*80)
print("EM-DASH SCAN (\\u2014) ACROSS ALL RELEVANT JSON FILES")
print("="*80)

def find_emdashes(obj, path=""):
    findings = []
    if isinstance(obj, str):
        if "—" in obj:
            # count occurrences
            count = obj.count("—")
            findings.append((path, count, obj[:80]))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            findings.extend(find_emdashes(v, f"{path}.{k}" if path else k))
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            findings.extend(find_emdashes(item, f"{path}[{idx}]"))
    return findings

for f in files_to_check:
    if not f.exists():
        print(f"File not found: {f}")
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        try:
            data = json.load(fp)
            found = find_emdashes(data)
            if found:
                print(f"[FOUND EM-DASH] {f}: {len(found)} occurrences:")
                for p, cnt, snip in found[:5]:
                    print(f"  {p} ({cnt}x): {snip}...")
            else:
                print(f"[OK] {f}: 0 em-dashes")
        except Exception as e:
            print(f"[ERROR] {f}: {e}")
