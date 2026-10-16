# -*- coding: utf-8 -*-
import json
import os
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "exports", "Svartulfr_Export.json"), encoding="utf-8") as f:
    w = json.load(f)

print("=== WORLD SCENARIOS IN exports/Svartulfr_Export.json ===")
for s in w.get("world_scenarios", []):
    print(f"\nID: {s.get('id')} | NAME: {s.get('name')}")
    for k, v in s.items():
        if k == "premade_scenes":
            print(f"  premade_scenes ({len(v)}):")
            for i, ps in enumerate(v):
                print(f"    [{i+1}] id={ps.get('id')} | desc={ps.get('description')} | text_len={len(ps.get('scene_text',''))} | keys={list(ps.keys())}")
        elif k == "resolved_characters":
            print(f"  resolved_characters ({len(v)}): {[c.get('display_name') for c in v]}")
        else:
            print(f"  {k}: {v}")

print("\n=== SCENARIO SCRIPTS IN scripts/ ===")
for p in sorted(glob.glob(os.path.join(ROOT, "scripts", "*scenario*"))):
    print(" ", os.path.basename(p))
