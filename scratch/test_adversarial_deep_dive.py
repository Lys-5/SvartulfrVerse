import json
import pathlib
import sys
import requests

ROOT = pathlib.Path(r"e:\repository\SvartulfrVerse")
TOKEN_PATH = ROOT / "scratch" / "wyvern_token.txt"

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def inspect_deep_edge_cases():
    token = TOKEN_PATH.read_text(encoding="utf-8").strip()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    files = [
        ("Villa Douglas", ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Villa_Douglas.json", "char_scenario_88N1eQXqkbydKX9q9XQzp"),
        ("Camp Mystic", ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Camp_Mystic.json", "char_scenario_nLC84wrHdrbB6P3DEhwKb"),
        ("DMHA Dungeons", ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_DMHA_Dungeons.json", "char_scenario_eqtRNnDpKbxDp7dmJmq6E"),
        ("Underworld Sindacato", ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Underworld_Sindacato.json", "char_scenario_rrUCdBPH6WTNyBnQkMAKR"),
        ("SUCC Route Alyssa", ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Alyssa.json", "char_scenario_CKgwq246DyCj1NNTBV9rt"),
        ("SUCC Route Jasper", ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Jasper.json", "char_scenario_Kq4mJEBH83j7Q7DdVfFnF"),
        ("Master Scenario", ROOT / "FINAL" / "Svartulfr_Master_Scenario.json", "char_scenario_1DC43ggb6mB8YLJDJKrU4"),
    ]

    print("=" * 80)
    print("DEEP DIVE: LOREBOOKS ARRAY, FORMATTING DISCIPLINE & MASTER GREETINGS AUDIT")
    print("=" * 80)

    # 1. Audit Master Scenario Greetings POV labeling & Persona Consistency
    master_file = ROOT / "FINAL" / "Svartulfr_Master_Scenario.json"
    with open(master_file, "r", encoding="utf-8") as f:
        master_data = json.load(f)

    print("\n--- MASTER SCENARIO GREETINGS TABLE (29 TOTAL) ---")
    fempov = []
    malepov = []
    neutral = []
    for idx, g in enumerate(master_data["greetings"]):
        name = g.get("name", "")
        pids = g.get("linked_persona_ids", [])
        speaker = g.get("speaker_slot", "")
        desc = g.get("description", "")
        
        # Check text references
        has_fem_tag = "[FemPOV]" in name
        has_male_tag = "[MalePOV]" in name
        
        tag_type = "FemPOV" if has_fem_tag else ("MalePOV" if has_male_tag else "Neutral")
        if tag_type == "FemPOV":
            fempov.append(idx)
        elif tag_type == "MalePOV":
            malepov.append(idx)
        else:
            neutral.append(idx)

        print(f"[{idx:02d}] Tag: {tag_type:<7} | Slot: {speaker:<15} | PIDs: {pids} | Name: {name[:45]}")

    print(f"\nSummary counts: FemPOV={len(fempov)}, MalePOV={len(malepov)}, Neutral={len(neutral)} (Total: {len(master_data['greetings'])})")
    assert len(fempov) == 7, f"Expected 7 FemPOV, got {len(fempov)}"
    assert len(malepov) == 6, f"Expected 6 MalePOV, got {len(malepov)}"
    assert len(neutral) == 16, f"Expected 16 Neutral, got {len(neutral)}"

    # 2. Check for em-dashes (—) across all scenario files
    print("\n--- EM-DASH AUDIT ACROSS ALL SCENARIO FILES ---")
    em_dash_violations = []
    for name, fpath, sc_id in files:
        raw_text = fpath.read_text(encoding="utf-8")
        em_count = raw_text.count("—")
        if em_count > 0:
            em_dash_violations.append((name, fpath.name, em_count))
            print(f"  [NOTE] {name}: {em_count} em-dashes found")
        else:
            print(f"  [CLEAN] {name}: 0 em-dashes")

    # 3. Check embedded 'lorebooks' object array vs 'lorebook_ids'
    print("\n--- EMBEDDED 'lorebooks' OBJECT ARRAY INTEGRITY ---")
    for name, fpath, sc_id in files:
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        lb_ids = d.get("lorebook_ids", [])
        embedded_lbs = d.get("lorebooks", [])
        if embedded_lbs:
            emb_ids = [lb.get("id") for lb in embedded_lbs]
            print(f"  {name}: {len(lb_ids)} lb_ids, {len(embedded_lbs)} embedded lorebooks. All embedded in lb_ids? {set(emb_ids).issubset(set(lb_ids))}")
        else:
            print(f"  {name}: {len(lb_ids)} lb_ids, embedded 'lorebooks' is absent/empty.")

    # 4. Check CHANGELOG.md entry
    print("\n--- CHANGELOG.md ENTRY AUDIT ---")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    has_entry = "Suite Unificata dei 15 Lorebook & Integrazione \"Offer a Persona to Play As\"" in changelog
    print(f"  CHANGELOG.md contains milestone title: {has_entry}")
    has_alyssa = "persona_1786335754946" in changelog
    has_jasper = "1792155173728" in changelog
    print(f"  CHANGELOG.md documents Alyssa ID: {has_alyssa}")
    print(f"  CHANGELOG.md documents Jasper ID: {has_jasper}")

if __name__ == "__main__":
    inspect_deep_edge_cases()
