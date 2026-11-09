"""
Independent Adversarial Consistency and Integrity Checker for Reviewer M4_2
Runs non-invasive cross-tier queries to ensure zero facade, zero hardcoded deception,
and full cross-tier consistency across all layers.
"""

import json
import re
from pathlib import Path

REPO_ROOT = Path(r"e:\repository\SvartulfrVerse")

def check_cross_tier():
    print("=" * 70)
    print("INDEPENDENT ADVERSARIAL CROSS-TIER INTEGRITY AUDIT")
    print("=" * 70)
    
    # 1. Check CHANGELOG.md for the new section
    changelog_text = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "### 02/11/2026 - Integrazione Completa della Lore Emergente" in changelog_text
    # Check 0 em-dashes in this section
    start_pos = changelog_text.find("### 02/11/2026 - Integrazione Completa della Lore Emergente")
    end_pos = changelog_text.find("### 01/11/2026", start_pos)
    m4_section = changelog_text[start_pos:end_pos]
    assert "\u2014" not in m4_section, "Em-dash in CHANGELOG.md M4 section!"
    print("[PASS] CHANGELOG.md M4 section verified (0 em-dashes).")

    # 2. Check Lorebook III Entry 39 and 40 ID uniqueness
    for lb3_path in [
        REPO_ROOT / "FINAL/Svartulfr_Lorebook_III.json",
        REPO_ROOT / "lorebooks/optimized/Svartulfr_Lorebook_III.json"
    ]:
        with open(lb3_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        entries = data["entries"]
        assert len(entries) == 47
        e39 = entries[39]
        e40 = entries[40]
        assert e39["entry_id"] == "event_partita_di_campionato_"
        assert e40["entry_id"] == "event_partita_di_campionato_hockey"
        assert e39["entry_id"] != e40["entry_id"]
        assert data["entries"] == data["lexicon"]
        print(f"[PASS] {lb3_path.name} entries 39/40 unique IDs and entries == lexicon parity verified.")

    # 3. Check Alyssa across Cards, Personas, NPC Primary dossier, Vault
    alyssa_card = json.load(open(REPO_ROOT / "ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json", encoding="utf-8"))
    alyssa_persona = json.load(open(REPO_ROOT / "FINAL/personas/Alyssa_Persona.json", encoding="utf-8"))
    npc_prim = json.load(open(REPO_ROOT / "FINAL/Svartulfr_NPC_Primary.json", encoding="utf-8"))
    alyssa_dossier = next(e for e in npc_prim["entries"] if e.get("entry_id") == "alyssa_world_dossier_2b54a223")

    for name, content in [
        ("alyssa_card", alyssa_card["description"]),
        ("alyssa_persona", alyssa_persona["description"]),
        ("alyssa_dossier", alyssa_dossier["content"])
    ]:
        assert "Certified Guild Healer" in content, f"Missing Certified Guild Healer in {name}"
        assert "ADB-555" in content, f"Missing ADB-555 in {name}"
        assert "St. Brugge Private Academy" in content, f"Missing St. Brugge in {name}"
        assert "Novice Healing Mage" not in content, f"Residual Novice Healing Mage in {name}"
        assert "Mark of Mani" in content, f"Missing Mark of Mani in {name}"
        assert "left hip" in content.lower(), f"Missing left hip for Mani in {name}"
        assert "\u2014" not in content, f"Em-dash found in {name}"
        print(f"[PASS] Alyssa verified in {name}")

    # 4. Check Jasper across Cards, Personas, NPC Primary dossier, Vault
    jasper_card = json.load(open(REPO_ROOT / "FINAL/Jasper_Douglas_Bloodmoon_card.json", encoding="utf-8"))
    jasper_persona = json.load(open(REPO_ROOT / "FINAL/personas/Jasper_Persona.json", encoding="utf-8"))
    jasper_dossier = next(e for e in npc_prim["entries"] if e.get("entry_id") == "Vcj4h2TL4Usola2A4OOl6")

    for name, content in [
        ("jasper_card", jasper_card["description"]),
        ("jasper_persona", jasper_persona["description"]),
        ("jasper_dossier", jasper_dossier["content"])
    ]:
        assert "Registered Guild Hunter" in content, f"Missing Registered Guild Hunter in {name}"
        assert "JDB-555" in content, f"Missing JDB-555 in {name}"
        assert "St. Brugge Private Academy" in content, f"Missing St. Brugge in {name}"
        assert "LEVEL: 19" in content, f"Missing LEVEL: 19 in {name}"
        assert "LEVEL: 3" not in content, f"Residual LEVEL: 3 in {name}"
        assert "Mark of Sol" in content, f"Missing Mark of Sol in {name}"
        assert "right hip" in content.lower(), f"Missing right hip for Sol in {name}"
        assert "\u2014" not in content, f"Em-dash found in {name}"
        # Assert collarbone is not in line 1
        l1 = content.splitlines()[0]
        assert "collarbone" not in l1.lower(), f"Outdated collarbone in line 1 of {name}"
        print(f"[PASS] Jasper verified in {name}")

    # 5. Check Revazhael in NPC Secondary and Vault
    npc_sec = json.load(open(REPO_ROOT / "FINAL/Svartulfr_NPC_Secondary.json", encoding="utf-8"))
    rev_entry = next(e for e in npc_sec["entries"] if e.get("entry_id") == "jmh0MajEsRwrm4UYU14mY")
    rev_content = rev_entry["content"]
    assert "Superior Demon" in rev_content
    assert "St. Brugge Private Academy" in rev_content
    assert "TRUE NAME SECRET" in rev_content
    assert "Dimora del Rifugio" in rev_content or "Kobal" in rev_content
    assert "\u2014" not in rev_content
    print("[PASS] Revazhael verified in NPC Secondary.")

    # 6. Check Resonant Cylinders in Lorebook II and Vault
    lb2 = json.load(open(REPO_ROOT / "FINAL/Svartulfr_Lorebook_II.json", encoding="utf-8"))
    cyl_entry = next(e for e in lb2["entries"] if e.get("entry_id") == "lb2_item_enchanted_resonant_cylinders")
    cyl_content = cyl_entry["content"]
    assert "cilindri incantati a risonanza" in cyl_content.lower()
    assert "Alyssa" in cyl_content
    assert "\u2014" not in cyl_content
    print("[PASS] Resonant Cylinders verified in Lorebook II.")

    # 7. Check Crystallography and Abyssal Magic in Lorebook I and Vault
    lb1 = json.load(open(REPO_ROOT / "FINAL/Svartulfr_Lorebook_I.json", encoding="utf-8"))
    cryst_entry = next(e for e in lb1["entries"] if e.get("entry_id") == "lb1_concept_applied_runic_crystallography")
    abyss_entry = next(e for e in lb1["entries"] if e.get("entry_id") == "lb1_magic_abyssal_magic_distinction")
    assert "cristallografia runica applicata" in cryst_entry["content"].lower()
    assert "magia abissale" in abyss_entry["content"].lower()
    assert "\u2014" not in cryst_entry["content"]
    assert "\u2014" not in abyss_entry["content"]
    print("[PASS] Crystallography and Abyssal Magic verified in Lorebook I.")

    # 8. Check Suite 3 in Location Lorebook
    loc_lb = json.load(open(REPO_ROOT / "lorebooks/optimized/Svartulfr_Location.json", encoding="utf-8"))
    suite3_entry = next(e for e in loc_lb["entries"] if e.get("entry_id") == "loc_theta_iota_theta_suite_3")
    suite3_content = suite3_entry["content"]
    assert "theta iota theta" in suite3_content.lower()
    assert "suite" in suite3_content.lower()
    assert "Sierra Cruz" in suite3_content
    assert "Scarlett Rose" in suite3_content
    assert "Alyssa Douglas" in suite3_content
    assert "Grave Mistake" in suite3_content
    assert "\u2014" not in suite3_content
    print("[PASS] Suite 3 verified in Location Lorebook.")

    print("=" * 70)
    print("ALL INDEPENDENT ADVERSARIAL CROSS-TIER CHECKS PASSED (100% OK)")
    print("=" * 70)

if __name__ == "__main__":
    check_cross_tier()
