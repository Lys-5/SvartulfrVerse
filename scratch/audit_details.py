# -*- coding: utf-8 -*-
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("=== 1. CHECKING exports/Mine_Characters_Export.json & Mine_Lorebooks_Export.json ===")
mc_p = os.path.join(ROOT, "exports", "Mine_Characters_Export.json")
if os.path.exists(mc_p):
    with open(mc_p, encoding="utf-8") as f:
        mc = json.load(f)
    chars = mc if isinstance(mc, list) else mc.get("characters", mc.get("results", []))
    print(f"Mine_Characters_Export.json count: {len(chars)}")
    for c in chars[:25]:
        if isinstance(c, dict):
            print(f"  - {c.get('id')} | {c.get('name') or c.get('display_name')} | updated={c.get('updated_at')}")

ml_p = os.path.join(ROOT, "exports", "Mine_Lorebooks_Export.json")
if os.path.exists(ml_p):
    with open(ml_p, encoding="utf-8") as f:
        ml = json.load(f)
    lbs = ml if isinstance(ml, list) else ml.get("lorebooks", ml.get("results", []))
    print(f"Mine_Lorebooks_Export.json count: {len(lbs)}")
    for l in lbs:
        if isinstance(l, dict):
            print(f"  - {l.get('id')} | {l.get('name')} | entries={len(l.get('lexicon', l.get('entries', [])))} | updated={l.get('updated_at')}")

print("\n=== 2. CHECKING ALL 16 DIGITALIS ENTRIES ACROSS FINAL/ ===")
DIGITALIS_NAMES = {
    "The Hothouse", "Seedpod", "Narcissus", "Taproot", "Digitalis", "The Ovary",
    "Nectary", "Graft", "Tendril", "Collars", "The Trials", "The Host",
    "The Gallery", "Hemlock", "Hemlock Biosciences", "Cameras", "Rules",
    "Jun's Coping Mechanism", "Mei", "Bao", "The Gardener", "Wen Guo",
    "Dr Negin Tabasi", "Rene Legaspi", "Aikawa Keisuke"
}
for fn in sorted(os.listdir(os.path.join(ROOT, "FINAL"))):
    if fn.startswith("Svartulfr_") and fn.endswith(".json"):
        with open(os.path.join(ROOT, "FINAL", fn), encoding="utf-8") as f:
            d = json.load(f)
        for i, e in enumerate(d.get("entries", [])):
            nm = e.get("name", "")
            if nm in DIGITALIS_NAMES or any(dn.lower() == nm.lower() for dn in DIGITALIS_NAMES):
                print(f"  {fn:30} [{i:3}] {nm:28} | enabled={e.get('enabled')}")

print("\n=== 3. CHECKING ZERO IN FINAL/Svartulfr_NPC_Primary.json ===")
with open(os.path.join(ROOT, "FINAL", "Svartulfr_NPC_Primary.json"), encoding="utf-8") as f:
    npc1 = json.load(f)["entries"]
for i, e in enumerate(npc1):
    if e.get("name") == "Zero":
        print(f"Zero [{i}]:\n{e.get('content')}")
