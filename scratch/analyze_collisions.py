import os
import json
import sys
from collections import defaultdict

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
p1 = os.path.join(PROJECT_ROOT, "FINAL", "Svartulfr_NPC_Primary.json")
p2 = os.path.join(PROJECT_ROOT, "FINAL", "Svartulfr_NPC_Secondary.json")

d1 = json.load(open(p1, "r", encoding="utf-8"))["lexicon"]
d2 = json.load(open(p2, "r", encoding="utf-8"))["lexicon"]

key_to_npcs = defaultdict(list)
for fname, d in [("Primary", d1), ("Secondary", d2)]:
    for idx, e in enumerate(d):
        for k in e.get("keys", []):
            key_to_npcs[k.strip().lower()].append((fname, idx, e))

collisions = {k: v for k, v in key_to_npcs.items() if len(v) > 1}

print(f"Total Collisions: {len(collisions)}\n")
for k, npcs in sorted(collisions.items()):
    # Check if all instances are actually the SAME NPC (e.g. duplicate key in same entry)
    unique_npcs = set((fname, e["entry_id"]) for fname, idx, e in npcs)
    print(f"=== Collision Key: '{k}' (Used in {len(npcs)} entries, {len(unique_npcs)} unique NPCs) ===")
    for fname, idx, e in npcs:
        print(f"  [{fname} #{idx}] '{e['name']}' (ID: {e['entry_id']}):")
        print(f"      All keys: {e.get('keys')}")
        print(f"      Secondary: {e.get('secondary_keys')}")
        print(f"      Selective: {e.get('selective')}")
    print()
