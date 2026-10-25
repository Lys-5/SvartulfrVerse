import json

cards = [
    ("Erik", "FINAL/Erik_Douglas_card.json"),
    ("Malachia", "FINAL/Malachia_Douglas_Bloodmoon_card.json"),
    ("Noah", "FINAL/Noah_Douglas_Bloodmoon_card.json"),
    ("Logan", "FINAL/Logan_Douglas_card.json"),
    ("Wulfnic", "FINAL/Wulfnic_Bloodmoon_card.json"),
    ("Mackenzie", "FINAL/Mackenzie_Sanchez_Rogers_card.json"),
    ("Edric", "FINAL/Edric_Douglas_card.json")
]

for name, path in cards:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    desc = data.get("description", "")
    em_dashes = desc.count("—")
    age_macros = desc.count("{{age}}")
    asterisks = desc.count("*")
    print(f"{name} ({path}):")
    print(f"  Length: {len(desc)}")
    print(f"  Em-dashes ('—'): {em_dashes}")
    print(f"  Age macros ('{{{{age}}}}'): {age_macros}")
    print(f"  Asterisks ('*'): {asterisks}")
    if em_dashes > 0:
        print(f"  WARNING: {em_dashes} em-dashes found in {name}")
    if age_macros > 0:
        print(f"  WARNING: {age_macros} age macros found in {name}")
    if asterisks > 0:
        # Check where asterisks appear
        lines_with_ast = [line for line in desc.splitlines() if "*" in line]
        print(f"  Lines with asterisks ({len(lines_with_ast)}):")
        for l in lines_with_ast[:3]:
            print(f"    {repr(l[:100])}")
