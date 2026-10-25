import json

target_map_primary = {
    "C-JisFj8qA1tsFEqZKevk": "Erik Ulfr Douglas",
    "jDuJtzirlEZC3K_ArIufh": "Malachia Björn Douglas Bloodmoon",
    "H2JX-NkHRiJ2FzoekC5ZZ": "Noah Loki Douglas Bloodmoon",
    "tAcrWLtWSDGf3xJJRwUOM": "Logan Járn Douglas",
    "HhuMluMmIIENUei3bX6ed": "Wulfnic Báleygr Bloodmoon",
    "BXi3sENAVYB8OKF80Q9Su": "Mackenzie Sanchez-Rogers"
}

with open("FINAL/Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    pdata = json.load(f)

print("Checking Primary entries vs lexicon for 6 targets:")
for tid, name in target_map_primary.items():
    e_entry = next((x for x in pdata["entries"] if x.get("entry_id") == tid), None)
    l_entry = next((x for x in pdata["lexicon"] if x.get("entry_id") == tid), None)
    print(f"{name} ({tid}):")
    print(f"  found in entries: {e_entry is not None}, in lexicon: {l_entry is not None}")
    if e_entry and l_entry:
        diff_keys = []
        for k in set(e_entry.keys()) | set(l_entry.keys()):
            if e_entry.get(k) != l_entry.get(k):
                diff_keys.append(k)
        print(f"  diff keys: {diff_keys}")

target_map_secondary = {
    "h-ttmlgJYeRXqyDvQjSX7": "Edric Douglas"
}

with open("FINAL/Svartulfr_NPC_Secondary.json", "r", encoding="utf-8") as f:
    sdata = json.load(f)

print("\nChecking Secondary entries vs lexicon for Edric:")
for tid, name in target_map_secondary.items():
    e_entry = next((x for x in sdata["entries"] if x.get("entry_id") == tid), None)
    l_entry = next((x for x in sdata["lexicon"] if x.get("entry_id") == tid), None)
    print(f"{name} ({tid}):")
    print(f"  found in entries: {e_entry is not None}, in lexicon: {l_entry is not None}")
    if e_entry and l_entry:
        diff_keys = []
        for k in set(e_entry.keys()) | set(l_entry.keys()):
            if e_entry.get(k) != l_entry.get(k):
                diff_keys.append(k)
        print(f"  diff keys: {diff_keys}")
