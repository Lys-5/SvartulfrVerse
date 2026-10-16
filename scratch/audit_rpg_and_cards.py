# -*- coding: utf-8 -*-
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "FINAL", "Svartulfr_NPC_Primary.json"), encoding="utf-8") as f:
    npc1 = json.load(f)["entries"]

print("=== ENTRIES IN FINAL/Svartulfr_NPC_Primary.json (RPG STATS & TRAITS) ===")
targets = [
    "Erik", "Logan", "Jasper", "Malachia", "Noah", "Edric", "Wulfnic",
    "Zefir", "Ut", "Kaladin", "Archer", "Mackenzie", "Finnegan", "Zeera",
    "Jared", "Elizabeth", "Magnus", "Cornelius", "Nixara", "Echo", "user"
]
for i, e in enumerate(npc1):
    c = e.get("content", "")
    name = e.get("name", "")
    if "RPG STATS & TRAITS" in c or any(n.lower() in name.lower() for n in targets):
        rpg_part = (
            c.split("RPG STATS & TRAITS:")[1][:130].replace("\n", " ")
            if "RPG STATS & TRAITS:" in c
            else "MISSING RPG BLOCK!"
        )
        print(f"[{i:3}] {name:35} | {rpg_part}")

print("\n=== COMPARING FINAL/*_card.json vs FINAL/Svartulfr_NPC_Primary.json ===")
for fn in sorted(os.listdir(os.path.join(ROOT, "FINAL"))):
    if fn.endswith("_card.json"):
        with open(os.path.join(ROOT, "FINAL", fn), encoding="utf-8") as f:
            card = json.load(f)
        cname = card.get("name", "")
        cdesc = card.get("description", "")
        print(f"CARD: {fn:35} | {cname:32} | desc_len={len(cdesc)} | has_RPG_block={'RPG STATS & TRAITS:' in cdesc}")
