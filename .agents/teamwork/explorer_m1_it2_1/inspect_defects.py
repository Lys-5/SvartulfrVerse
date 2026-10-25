import json
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent
primary_path = repo_root / "FINAL/Svartulfr_NPC_Primary.json"
secondary_path = repo_root / "FINAL/Svartulfr_NPC_Secondary.json"

target_names = [
    # Primary (10)
    "Hugh Rivers", "Dominic Rogers", 'Daniel "Danny" Boone', "Harrison Black",
    "Marcus O'Connor", "Helena Weiss", "Harlan Beaumont", 'Federico "Riki" Savini',
    "Eris Davies", "Elizabeth Duskwood",
    # Secondary (10)
    "Alicia Virtuoso", "Ariadne Cirillo", "Luisa Sanchez Rogers",
    "Alistair Ambrose DeVille", "Damien Bishop", "Adelin Coso",
    "Professor Marit Christiansen", "Professor Mollusk Moreau",
    "Campus Staff Rat", "Graham Purcell"
]

def check(path, label):
    data = json.load(open(path, encoding="utf-8"))
    for e in data["lexicon"]:
        name = e.get("name")
        if name in target_names:
            reg = e.get("avatar_activation_regex", "")
            npc_info = e.get("npc_info", {})
            print(f"[{label}] {name}")
            print(f"   last_name: {repr(npc_info.get('last_name'))}")
            print(f"   middle_names in npc_info: {'middle_names' in npc_info} (value: {npc_info.get('middle_names')})")
            print(f"   regex: {reg}\n")

check(primary_path, "Primary")
check(secondary_path, "Secondary")
