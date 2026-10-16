# -*- coding: utf-8 -*-
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIGITALIS_MARKERS = [
    "Cutting 01",
    "Cutting 02",
    "Cutting 03",
    "Tendril (HM-7)",
    "The Hothouse:",
    "Seedpod (the Closet):",
    "Narcissus (the Mirror Room):",
    "Taproot (the Confession Room):",
    "Digitalis: Cold War missile silo",
    "The Ovary: the Host's bedroom",
    "Nectary (the Rain Room):",
    "Graft (the Cuff Room):",
    "Cuttings and {{user}} the Host",
    "Jun's beloved Shiba Inu",
    "younger half sister of Jun",
    "Jun traits(Tendril keyed his body",
    "Hemlock Biosciences: Delaware biotech",
    "drone Rene named Gnat",
    "Jun dies if he orgasms within three metres",
    "Rene/Keisuke's red triggers",
    "Industrial walk in freezer at minus 10 degrees",
    "strictly between Jun and {{user}}",
    "the only unmedicated person in Digitalis",
    "forty anonymous paying viewers",
]

BROAD_KEYS = {"solarton", "succ", "blackwood", "losangeles", "underworld"}

def check_lorebooks(folder, files):
    print(f"\n================ {folder} ================")
    for fn in files:
        p = os.path.join(ROOT, folder, fn)
        if not os.path.exists(p):
            print(f"MISSING: {p}")
            continue
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        raw_entries = d.get("entries", d.get("lexicon", []))
        if isinstance(raw_entries, dict):
            entries = [(k, v) for k, v in raw_entries.items()]
        else:
            entries = [(str(i), v) for i, v in enumerate(raw_entries)]

        enabled_cnt = 0
        dig_hits = []
        merged_hits = []
        sugar = []
        broad_npc = []
        leak_hits = []
        instr_hits = []
        sel_empty = []

        for idx, e in entries:
            c = e.get("content", "")
            name = e.get("name", e.get("comment", ""))
            is_en = e.get("enabled") if "enabled" in e else not e.get("disable", False)
            if is_en:
                enabled_cnt += 1

            if any(m in c for m in DIGITALIS_MARKERS):
                dig_hits.append((idx, name, is_en))

            if "WARDROBE & NOTABLE OUTFITS:\n- Faculty Daily:" in c:
                merged_hits.append(("Alicia Faculty Daily", idx, name))
            if "Descended from rural frontier wolf stock" in c:
                merged_hits.append(("Danny Boone cowboy", idx, name))
            if "Independent campus presence. Dean values brotherhood" in c or "Dean carries the heavy pressure of athletic perfection" in c:
                merged_hits.append(("Dean 6'2 athlete", idx, name))
            if "Veteran enforcer tied to old-school Los Angeles" in c:
                merged_hits.append(("Vito Marino LA enforcer", idx, name))
            if c.count("FAMILY & PACK:") > 1:
                merged_hits.append(("Multiple FAMILY & PACK", idx, name))

            if "sugar moon" in name.lower():
                sugar.append((idx, name, is_en))

            keys = e.get("keys", e.get("key", []))
            is_npc = (
                e.get("type") == "npc"
                or c.startswith("[NAME:")
                or c.startswith("[ENTITY:")
                or "NPC" in fn
            )
            if is_npc and name != "Modern Fantasy: Contatti Esterni dell'Underworld":
                bk = [k for k in keys if str(k).lower().strip() in BROAD_KEYS]
                if bk:
                    broad_npc.append((idx, name, bk))

            if ".md" in c or "FanOC_Roster" in c or "vedi Project" in c:
                leak_hits.append((idx, name))

            if "Format discipline: dialogue in quotes" in c:
                instr_hits.append((idx, name))

            sec_keys = e.get("secondary_keys", e.get("keysecondary", []))
            if e.get("selective") is True and not sec_keys:
                sel_empty.append((idx, name))

        print(f"File: {fn} | Total={len(entries)} (Enabled={enabled_cnt}, Disabled={len(entries)-enabled_cnt})")
        print(f"  - Digitalis hits ({len(dig_hits)}): {dig_hits}")
        print(f"  - Merged sheets unfixed ({len(merged_hits)}): {merged_hits}")
        if sugar:
            print(f"  - Sugar Moon ({len(sugar)}): {sugar}")
        print(f"  - NPCs with broad keys ({len(broad_npc)}): {broad_npc[:8]}")
        print(f"  - Path/Project leakage ({len(leak_hits)}): {leak_hits}")
        print(f"  - Redundant [INSTRUCTIONS] ({len(instr_hits)}): {instr_hits[:5]}")
        if sel_empty:
            print(f"  - selective=True with empty secondary ({len(sel_empty)}): {sel_empty[:5]}")

check_lorebooks("lorebooks/source", [
    "Svartulfr_Lorebook_I.json",
    "Svartulfr_Lorebook_II.json",
    "Svartulfr_Lorebook_III.json",
    "Svartulfr_Location.json",
    "Svartulfr_NPC_Primary.json",
])

check_lorebooks("lorebooks/optimized", [
    "Svartulfr_Lorebook_I.json",
    "Svartulfr_Lorebook_II.json",
    "Svartulfr_Lorebook_III.json",
    "Svartulfr_Location.json",
    "Svartulfr_NPC_Primary.json",
])

check_lorebooks("FINAL", [
    "Svartulfr_Lorebook_I.json",
    "Svartulfr_Lorebook_II.json",
    "Svartulfr_Lorebook_III.json",
    "Svartulfr_Location.json",
    "Svartulfr_NPC_Primary.json",
    "Svartulfr_NPC_Secondary.json",
])

print("\n================ CARDS IN FINAL/ ================")
for fn in sorted(os.listdir(os.path.join(ROOT, "FINAL"))):
    if fn.endswith("_card.json"):
        p = os.path.join(ROOT, "FINAL", fn)
        with open(p, encoding="utf-8") as f:
            c = json.load(f)
        ext = c.get("extensions", {})
        print(f"Card: {fn} | name={c.get('name')} | desc_len={len(c.get('description',''))} | outfits={len(ext.get('outfits',[]))} | lexicon={len(ext.get('lexicon',[]))}")

print("\n================ WORLD SCENARIOS IN EXPORTS ================")
exp_p = os.path.join(ROOT, "exports", "Svartulfr_Export.json")
if os.path.exists(exp_p):
    with open(exp_p, encoding="utf-8") as f:
        w = json.load(f)
    print("Export keys:", list(w.keys()))
    for k in w.keys():
        if isinstance(w[k], list):
            print(f"  {k}: {len(w[k])} items")
        elif isinstance(w[k], dict):
            print(f"  {k}: dict with keys {list(w[k].keys())[:10]}")
    scens = w.get("world_scenarios", w.get("scenarios", []))
    for s in scens:
        print(f"  Scenario: {s.get('id')} | {s.get('name') or s.get('title')} | chars={len(s.get('characters', s.get('starting_party', [])))} | loc={s.get('starting_location_id') or s.get('location_id')}")
