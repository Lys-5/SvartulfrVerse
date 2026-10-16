# -*- coding: utf-8 -*-
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_oct14_markers_in_lorebooks():
    print("=== CHECKING OCT 14 UPDATES (Wolf Names, Birth-Runes, RPG Batch 1 & 2, Naming/Rune Rituals) ===")
    
    # 1. Check Snapshot (scratch/backup_consolidated_snapshot/)
    snap_lb1 = os.path.join(ROOT, "scratch", "backup_consolidated_snapshot", "lorebook_svartulfr_I.json")
    snap_npc = os.path.join(ROOT, "scratch", "backup_consolidated_snapshot", "lorebook_npc_primary.json")
    
    # 2. Check lorebooks/source/
    src_lb1 = os.path.join(ROOT, "lorebooks", "source", "Svartulfr_Lorebook_I.json")
    src_npc = os.path.join(ROOT, "lorebooks", "source", "Svartulfr_NPC_Primary.json")
    
    # 3. Check FINAL/
    fin_lb1 = os.path.join(ROOT, "FINAL", "Svartulfr_Lorebook_I.json")
    fin_npc1 = os.path.join(ROOT, "FINAL", "Svartulfr_NPC_Primary.json")
    fin_npc2 = os.path.join(ROOT, "FINAL", "Svartulfr_NPC_Secondary.json")

    for label, path in [
        ("SNAP Lorebook I", snap_lb1),
        ("SRC  Lorebook I", src_lb1),
        ("FIN  Lorebook I", fin_lb1),
        ("SNAP NPC Primary", snap_npc),
        ("SRC  NPC Primary", src_npc),
        ("FIN  NPC Primary", fin_npc1),
        ("FIN  NPC Secondary", fin_npc2),
    ]:
        if not os.path.exists(path):
            print(f"{label}: MISSING")
            continue
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        entries = d.get("entries", d.get("lexicon", []))
        if isinstance(entries, dict):
            entries = list(entries.values())
        names = [e.get("name") or e.get("comment") or "" for e in entries]
        all_text = "\n".join(e.get("content", "") for e in entries)
        has_naming = any("Naming Tradition" in n for n in names) or "Lycanthrope Naming Tradition" in all_text
        has_rune = any("Birth-Rune" in n for n in names) or "BIRTH_RUNE:" in all_text
        has_rpg = "RPG STATS & TRAITS:" in all_text
        has_ulfr = "Ulfr" in all_text
        has_svartr = "Svartr" in all_text
        print(f"{label:20} | entries={len(entries):3} | NamingTrad={has_naming} | BirthRune={has_rune} | RPG_Block={has_rpg} | Ulfr={has_ulfr} | Svartr={has_svartr}")

    print("\n=== CHECKING FINAL CARDS FOR OCT 14 & OCT 15 UPDATES ===")
    for fn in sorted(os.listdir(os.path.join(ROOT, "FINAL"))):
        if fn.endswith("_card.json"):
            p = os.path.join(ROOT, "FINAL", fn)
            with open(p, encoding="utf-8") as f:
                c = json.load(f)
            desc = c.get("description", "")
            ext = c.get("extensions", {})
            rpg = ext.get("rpg_stats", {})
            base_stats = rpg.get("base_stats", {})
            stat_sum = sum(base_stats.values()) if isinstance(base_stats, dict) else 0
            traits = rpg.get("traits", [])
            print(f"{fn:36} | name={c.get('name'):32} | BIRTH_RUNE={'BIRTH_RUNE:' in desc} | RPG_in_desc={'RPG STATS & TRAITS:' in desc} | rpg_lv={rpg.get('level')} | stat_sum={stat_sum} | traits={len(traits)} | outfits={len(ext.get('outfits',[]))}")

    print("\n=== CHECKING SNAPSHOT MINE STANDALONE CHARACTERS vs FINAL CARDS ===")
    snap_mine = os.path.join(ROOT, "scratch", "backup_consolidated_snapshot", "mine_standalone_characters.json")
    if os.path.exists(snap_mine):
        with open(snap_mine, encoding="utf-8") as f:
            mc = json.load(f)
        for ch in mc:
            desc = ch.get("description", "")
            print(f"SNAP /mine: {ch.get('id')} | {ch.get('name') or ch.get('display_name'):32} | desc_len={len(desc):5} | BIRTH_RUNE={'BIRTH_RUNE:' in desc} | RPG_in_desc={'RPG STATS & TRAITS:' in desc} | outfits={len(ch.get('outfits',[]))}")

    print("\n=== CHECKING SNAPSHOT WORLD CHARACTERS (113) vs EXPORTS/Svartulfr_Export.json (108) ===")
    snap_wc_p = os.path.join(ROOT, "scratch", "backup_consolidated_snapshot", "world_characters.json")
    exp_p = os.path.join(ROOT, "exports", "Svartulfr_Export.json")
    if os.path.exists(snap_wc_p) and os.path.exists(exp_p):
        with open(snap_wc_p, encoding="utf-8") as f:
            snap_wc = json.load(f)
        with open(exp_p, encoding="utf-8") as f:
            exp_wc = json.load(f).get("world_characters", [])
        snap_ids = {c["id"]: c for c in snap_wc}
        exp_ids = {c["id"]: c for c in exp_wc}
        missing_in_exp = set(snap_ids.keys()) - set(exp_ids.keys())
        print(f"Snap world_characters: {len(snap_wc)} | Exports world_characters: {len(exp_wc)}")
        print("Characters in Oct 14 Snapshot but MISSING in exports/Svartulfr_Export.json:")
        for mid in missing_in_exp:
            c = snap_ids[mid]
            print(f"  - {mid}: {c.get('display_name') or c.get('first_name')}")
        
        # Check if exports/Svartulfr_Export.json has Oct 14 updates
        erik_snap = snap_ids.get("_d44gDc8N18kkbEhAcfUCG", {})
        erik_exp = exp_ids.get("_d44gDc8N18kkbEhAcfUCG", {})
        print(f"Erik in SNAP: name='{erik_snap.get('display_name')}', BIRTH_RUNE={'BIRTH_RUNE' in erik_snap.get('long_summary','')}, rpg_traits={len(erik_snap.get('rpg_stats',{}).get('traits',[]))}")
        print(f"Erik in EXP : name='{erik_exp.get('display_name')}', BIRTH_RUNE={'BIRTH_RUNE' in erik_exp.get('long_summary','')}, rpg_traits={len(erik_exp.get('rpg_stats',{}).get('traits',[]))}")

if __name__ == "__main__":
    check_oct14_markers_in_lorebooks()
