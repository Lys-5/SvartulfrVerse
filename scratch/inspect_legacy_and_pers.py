import json
import glob
import re

print("=== ARCHIVIO/cards_legacy/ ===")
for p in sorted(glob.glob("ARCHIVIO/cards_legacy/*_card.json")):
    d = json.load(open(p, encoding="utf-8"))
    desc = d.get("description", "")
    pers = d.get("personality", "")
    headers = re.findall(r"^([A-Z][A-Z0-9 &'\"/\(\)\-,]+):", desc, flags=re.M)
    has_bracket = desc.lstrip().startswith("[")
    has_bs = "BACKSTORY:" in desc
    has_fp = ("FAMILY & PACK:" in desc) or ("CLAN AND COMPANY:" in desc)
    has_vb = "VOICE & BEHAVIOR:" in desc
    print(f"LEGACY CARD {p}: len={len(desc)}, bracket={has_bracket}, bs={has_bs}, fp={has_fp}, vb={has_vb}, pers_bracket={pers.lstrip().startswith('[')}")
    print("   headers:", headers)

print("\n=== FULL PERSONALITY OF 8 FINAL CARDS ===")
for p in sorted(glob.glob("FINAL/*_card.json")):
    d = json.load(open(p, encoding="utf-8"))
    pers = d.get("personality", "")
    print(f"--- {p} ---")
    print(pers)
