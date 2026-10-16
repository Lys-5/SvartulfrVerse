import os
import json
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
p1 = os.path.join(PROJECT_ROOT, "FINAL", "Svartulfr_NPC_Primary.json")
p2 = os.path.join(PROJECT_ROOT, "FINAL", "Svartulfr_NPC_Secondary.json")

d1 = json.load(open(p1, "r", encoding="utf-8"))["lexicon"]
d2 = json.load(open(p2, "r", encoding="utf-8"))["lexicon"]

targets = [
    "Vito Marino", "Naomi Black", "Marcus O'Connor", "Isobel Blackwater",
    "Helena Weiss", "Eclipse Noir", "Dominic Chen", "Darius Vale",
    "Cass Harrow", "Bianca Rossi", "Barrow", "Aurora Night",
    "Cato", "Brittany Willow", "Zeera Darkfire", "Harlan Beaumont",
    "Brak Ironfist", "Malachia Björn Douglas Bloodmoon"
]

all_npcs = d1 + d2
for t in targets:
    for e in all_npcs:
        if t in e.get("name", ""):
            print(f"{e.get('name')}:")
            print(f"  keys: {e.get('keys')}")
            print(f"  sec_keys: {e.get('secondary_keys')}")
            print(f"  selective: {e.get('selective')}")
