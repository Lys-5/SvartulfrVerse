import json

cards = [
    "FINAL/Erik_Douglas_card.json",
    "FINAL/Malachia_Douglas_Bloodmoon_card.json",
    "FINAL/Noah_Douglas_Bloodmoon_card.json",
    "FINAL/Jasper_Douglas_Bloodmoon_card.json",
    "FINAL/Wulfnic_Bloodmoon_card.json"
]

for c in cards:
    d = json.load(open(c, encoding="utf-8"))
    name = d.get("name", "")
    desc = d.get("description", "")
    header = desc[:desc.find("]") + 1] if "]" in desc else desc[:200]
    print(f"CARD: {c} -> {name}")
    print(f"   HEADER: {header}\n")
