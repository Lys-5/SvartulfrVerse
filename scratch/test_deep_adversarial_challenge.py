import json
import glob
import os
import re

def deep_adversarial_audit():
    scenario_files = sorted(glob.glob("FINAL/scenarios/*.json"))
    export_file = "exports/Mine_Characters_Export.json"
    active_cards = {c["id"]: c.get("name") for c in json.load(open(export_file, encoding="utf-8")) if "id" in c}
    
    print("=" * 80)
    print("DEEP ADVERSARIAL CHALLENGE & VERBATIM EXTRACTION")
    print("=" * 80)
    
    # 1. Asterisk audit
    print("\n--- 1. ASTERISK & THOUGHT AUDIT ---")
    asterisk_found = []
    for sf in scenario_files:
        fname = os.path.basename(sf)
        data = json.load(open(sf, encoding="utf-8"))
        for g_i, g in enumerate(data.get("greetings", [])):
            for m_i, m in enumerate(g.get("messages", [])):
                content = m.get("content", "")
                if "*" in content:
                    asterisk_found.append((fname, g_i, m_i, content))
    print(f"Total messages with asterisks across all scenarios: {len(asterisk_found)}")
    for fname, g_i, m_i, content in asterisk_found:
        print(f"  {fname} G{g_i} M{m_i}:")
        for match in re.finditer(r'\*([^*]+)\*', content):
            print(f"    Thought text: '*{match.group(1)}*'")
            
    # 2. Dialogue & Quoting inspection
    print("\n--- 2. DIALOGUE & SPEECH TAG VERIFICATION ---")
    dialogue_snippets = []
    unquoted_speech_suspects = []
    speech_verbs = [r'\bsaid\b', r'\basked\b', r'\breplied\b', r'\bmuttered\b', r'\bshouted\b', r'\bwhispered\b', r'\bsnarled\b', r'\bcalled\b']
    for sf in scenario_files:
        fname = os.path.basename(sf)
        data = json.load(open(sf, encoding="utf-8"))
        for g_i, g in enumerate(data.get("greetings", [])):
            for m_i, m in enumerate(g.get("messages", [])):
                content = m.get("content", "")
                quotes = re.findall(r'"([^"]*)"', content)
                for q in quotes:
                    dialogue_snippets.append((fname, g_i, m_i, q))
                # Check for speech verbs not immediately followed or preceded by quotes
                for sv in speech_verbs:
                    for line in content.split("\n"):
                        if re.search(sv, line, re.IGNORECASE) and '"' not in line:
                            unquoted_speech_suspects.append((fname, g_i, m_i, line))
                            
    print(f"Total quoted dialogue passages found: {len(dialogue_snippets)}")
    print(f"Sample quoted dialogue passages (first 5):")
    for fname, g_i, m_i, q in dialogue_snippets[:5]:
        print(f"  [{fname} G{g_i} M{m_i}] \"{q}\"")
        
    print(f"\nUnquoted speech verb suspects (verbs without double-quotes on line): {len(unquoted_speech_suspects)}")
    for fname, g_i, m_i, line in unquoted_speech_suspects:
        print(f"  Suspect in {fname} G{g_i} M{m_i}: {line[:100]}")

    # 3. Name prefix stress test
    print("\n--- 3. NAME PREFIX ADVERSARIAL SCAN ---")
    prefix_violations = []
    for sf in scenario_files:
        fname = os.path.basename(sf)
        data = json.load(open(sf, encoding="utf-8"))
        for g_i, g in enumerate(data.get("greetings", [])):
            for m_i, m in enumerate(g.get("messages", [])):
                content = m.get("content", "")
                for line_idx, line in enumerate(content.split("\n")):
                    line_s = line.strip()
                    if ":" in line_s:
                        left_part = line_s.split(":")[0].strip()
                        # If left_part is short (like a character name)
                        if len(left_part.split()) <= 4 and re.match(r'^[A-Z\{\}][a-zA-Z\s\(\)"\'-]+$', left_part):
                            prefix_violations.append((fname, g_i, m_i, line_idx, line_s))
                            
    print(f"Potential name prefix violations found: {len(prefix_violations)}")
    for fname, g_i, m_i, line_idx, line_s in prefix_violations:
        print(f"  {fname} G{g_i} M{m_i} L{line_idx}: {line_s[:80]}")

    # 4. Verbatim character constraint extracts
    print("\n--- 4. VERBATIM CHARACTER CONSTRAINT EXTRACTS ---")
    
    # Russ Sinclair
    succ_jasper = json.load(open("FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json", encoding="utf-8"))
    for s in succ_jasper.get("slots", []):
        if s.get("key") == "male_roommate":
            print(f"  Russ Sinclair Slot: {s}")
            
    # Scarlett Rose
    succ_alyssa = json.load(open("FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json", encoding="utf-8"))
    for s in succ_alyssa.get("slots", []):
        if s.get("key") == "best_friend":
            print(f"  Scarlett Rose Slot (Alyssa route): {s}")
    for s in succ_jasper.get("slots", []):
        if s.get("key") == "crush":
            print(f"  Scarlett Rose Slot (Jasper route): {s}")

    # Finnegan Novak
    for s in succ_alyssa.get("slots", []):
        if s.get("key") == "childhood_friend":
            print(f"  Finnegan Novak Slot (Alyssa route): {s}")
    for s in succ_jasper.get("slots", []):
        if s.get("key") == "childhood_friend":
            print(f"  Finnegan Novak Slot (Jasper route): {s}")
    # Extract Finnegan in text
    for name, r_data in [("Alyssa", succ_alyssa), ("Jasper", succ_jasper)]:
        content = json.dumps(r_data)
        for sentence in re.split(r'[\.\n]', content):
            if "Finnegan" in sentence:
                print(f"  Finnegan mention in {name}: {sentence.strip()[:120]}")

    # Jean-Luc Virtuoso
    underworld = json.load(open("FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json", encoding="utf-8"))
    for s in underworld.get("slots", []):
        if s.get("key") == "sinners_leader":
            print(f"  Jean-Luc Virtuoso Slot: {s}")
    u_content = json.dumps(underworld)
    for sentence in re.split(r'[\.\n]', u_content):
        if "Jean-Luc" in sentence:
            print(f"  Jean-Luc mention: {sentence.strip()[:120]}")

    # Villa Douglas 7 males
    villa = json.load(open("FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json", encoding="utf-8"))
    print(f"  Villa Douglas Slots ({len(villa.get('slots', []))}):")
    for s in villa.get("slots", []):
        pid = s.get("pool", [{}])[0].get("character_id")
        pname = active_cards.get(pid, "UNKNOWN")
        print(f"    Slot '{s.get('key')}': label='{s.get('label')}', card_id='{pid}' ({pname})")

    # DMHA scenario cast
    dmha = json.load(open("FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json", encoding="utf-8"))
    print(f"  DMHA Scenario Slots ({len(dmha.get('slots', []))}):")
    for s in dmha.get("slots", []):
        pid = s.get("pool", [{}])[0].get("character_id") if s.get("pool") else "NONE"
        pname = active_cards.get(pid, "NPC / Open") if pid != "NONE" else "NPC / Open"
        print(f"    Slot '{s.get('key')}': label='{s.get('label')}', card_id='{pid}' ({pname})")

    # Camp Mystic shuttle & supervision
    camp = json.load(open("FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json", encoding="utf-8"))
    print(f"  Camp Mystic Greetings ({len(camp.get('greetings', []))}):")
    for i, g in enumerate(camp.get("greetings", [])):
        print(f"    Greeting {i}: title='{g.get('title')}', msgs={len(g.get('messages', []))}")
        for m_idx, m in enumerate(g.get("messages", [])):
            first_line = m.get("content", "").split("\n")[0]
            print(f"      m{m_idx}: {first_line[:90]}")
    print("  Camp Mystic startup_script snippet:")
    script = camp.get("startup_script", "")
    for line in script.split("\n"):
        if any(k in line for k in ["supervisor", "Marcus", "Celeste", "gender", "persona"]):
            print(f"    {line.strip()}")

if __name__ == "__main__":
    deep_adversarial_audit()
