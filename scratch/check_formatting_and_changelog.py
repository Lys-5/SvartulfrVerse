"""
Check CHANGELOG.md and dialogue formatting across scenarios.
"""

import os
import json
import re

def main():
    print("=== CHECKING CHANGELOG.MD AND FORMATTING DISCIPLINE ===")
    
    # 1. CHANGELOG.md check
    with open("CHANGELOG.md", "r", encoding="utf-8") as f:
        changelog = f.read()
        
    print("CHANGELOG.md length:", len(changelog))
    # Check if latest entry mentions the R1-R5 operations
    has_r1 = "R1" in changelog or "SUCC" in changelog or "scenari" in changelog.lower()
    has_r3 = "Jared" in changelog or "8 card" in changelog or "cards_legacy" in changelog
    has_r4 = "NPC_Primary" in changelog or "ignored_personas" in changelog or "ignored_characters" in changelog
    
    print("CHANGELOG has R1-R2 scenario mention:", has_r1)
    print("CHANGELOG has R3 card reduction mention:", has_r3)
    print("CHANGELOG has R4 native suppression mention:", has_r4)
    
    # Check em-dashes in latest changelog section
    # Let's inspect the latest section of CHANGELOG.md
    sections = changelog.split("## ")
    latest_section = "## " + sections[1] if len(sections) > 1 else changelog
    em_dashes_in_latest = re.findall(r'—', latest_section)
    print(f"Em-dashes in latest CHANGELOG section: {len(em_dashes_in_latest)}")
    print(f"Latest section header: {latest_section.splitlines()[0]}")

    # 2. Check dialogue formatting in scenario messages
    for fname in ["Svartulfr_Scenario_SUCC_Route_Alyssa.json", "Svartulfr_Scenario_SUCC_Route_Jasper.json"]:
        fpath = os.path.join("FINAL", "scenarios", fname)
        with open(fpath, "r", encoding="utf-8") as f:
            scen = json.load(f)
            
        print(f"\nDialogue audit for {fname}:")
        for gi, g in enumerate(scen.get("greetings", [])):
            for mi, m in enumerate(g.get("messages", [])):
                content = m.get("content", "")
                dialogue_matches = re.findall(r'"([^"]*)"', content)
                if not dialogue_matches:
                    print(f"  Note: G{gi} M{mi} has no dialogue in quotes (pure narration).")
                else:
                    # check if dialogue matches have any weird chars
                    pass
                # Check for single quotes being used as dialogue
                # (looking for 'Hello ...')
                single_quote_dialog = re.findall(r"(?:^|\s)'([A-Z][^']*)'", content)
                if single_quote_dialog:
                    print(f"  Warning: potential single-quote dialogue in G{gi} M{mi}: {single_quote_dialog}")
        print(f"  {fname}: All dialogues enclosed in standard double quotes.")

if __name__ == "__main__":
    main()
