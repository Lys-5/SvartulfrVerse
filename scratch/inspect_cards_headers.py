import json
import glob

cards = glob.glob("FINAL/*_card.json") + glob.glob("ARCHIVIO/cards_legacy/*_card.json")
for c in cards:
    d = json.load(open(c, encoding="utf-8"))
    name = d.get("name", "")
    desc = d.get("description", "")
    first_bracket = desc[:desc.find("]") + 1] if "]" in desc else desc[:200]
    print(f"CARD: {c} -> {name}")
    print(f"   HEADER: {first_bracket}\n")
