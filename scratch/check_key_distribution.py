import os
import json
import sys
from collections import Counter

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
p1 = os.path.join(PROJECT_ROOT, "FINAL", "Svartulfr_NPC_Primary.json")
p2 = os.path.join(PROJECT_ROOT, "FINAL", "Svartulfr_NPC_Secondary.json")

d1 = json.load(open(p1, "r", encoding="utf-8"))["lexicon"]
d2 = json.load(open(p2, "r", encoding="utf-8"))["lexicon"]

counts = Counter()
single_key_npcs = []
zero_key_npcs = []

for idx, e in enumerate(d1):
    k_len = len(e.get("keys", []))
    counts[k_len] += 1
    if k_len == 0:
        zero_key_npcs.append(("Primary", idx, e.get("name")))
    elif k_len == 1:
        single_key_npcs.append(("Primary", idx, e.get("name"), e.get("keys")))

for idx, e in enumerate(d2):
    k_len = len(e.get("keys", []))
    counts[k_len] += 1
    if k_len == 0:
        zero_key_npcs.append(("Secondary", idx, e.get("name")))
    elif k_len == 1:
        single_key_npcs.append(("Secondary", idx, e.get("name"), e.get("keys")))

print("Distribution of key counts across all 416 NPCs:")
for k, v in sorted(counts.items()):
    print(f"  {k} keys: {v} NPCs")

print(f"\nZero-key NPCs: {len(zero_key_npcs)}")
for z in zero_key_npcs:
    print(f"  {z}")

print(f"\nSingle-key NPCs: {len(single_key_npcs)}")
for s in single_key_npcs:
    print(f"  {s}")
