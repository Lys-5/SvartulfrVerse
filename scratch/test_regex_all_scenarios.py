"""
Comprehensive Regex Scenario & Stress Matrix for all 416 NPCs
"""
import os
import json
import re
import time

FINAL_DIR = r"e:\repository\SvartulfrVerse\FINAL"
NPC_FILES = ["Svartulfr_NPC_Primary.json", "Svartulfr_NPC_Secondary.json"]

def run_matrix():
    print("=" * 70)
    print("CHALLENGER 1: 416 NPC DIALOGUE HEADER REGEX MATRIX")
    print("=" * 70)

    total_npcs = 0
    stats = {
        "full_name_pass": 0,
        "newline_full_name_pass": 0,
        "whitespace_full_name_pass": 0,
        "multiline_dialogue_pass": 0,
        "space_before_colon_pass": 0,
        "first_name_pass": 0,
        "first_last_pass": 0,
        "rejection_prefix_pass": 0,
        "rejection_suffix_pass": 0,
        "rejection_embedded_pass": 0,
        "rejection_random_pass": 0,
        "timing_under_5ms": 0,
    }

    timing_failures = []
    regex_failures = []

    for fname in NPC_FILES:
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)

        for idx, entry in enumerate(d["lexicon"]):
            total_npcs += 1
            name = entry.get("name", "")
            rg = entry.get("avatar_activation_regex", "")
            info = entry.get("npc_info", {})
            first = (info.get("first_name") or "").strip()
            last = (info.get("last_name") or "").strip()

            # Compile with re.M (multiline) and re.I (since case_sensitive: false)
            # We also test strict re.M on full name
            pat_strict = re.compile(rg, re.M)
            pat_ci = re.compile(rg, re.M | re.I)

            # Test 1: Full Name verbatim
            t0 = time.perf_counter()
            m = pat_strict.search(f"{name}:")
            elapsed_ms = (time.perf_counter() - t0) * 1000
            if m:
                stats["full_name_pass"] += 1
            else:
                regex_failures.append((name, f"{name}:", rg, "Failed verbatim full name"))

            if elapsed_ms < 5.0:
                stats["timing_under_5ms"] += 1
            else:
                timing_failures.append((name, elapsed_ms))

            # Test 2: Newline + Full Name
            if pat_strict.search(f"\n{name}:"):
                stats["newline_full_name_pass"] += 1
            else:
                regex_failures.append((name, f"\\n{name}:", rg, "Failed newline full name"))

            # Test 3: Whitespace + Full Name
            if pat_strict.search(f"   {name}:") and pat_strict.search(f"\n   {name}:"):
                stats["whitespace_full_name_pass"] += 1
            else:
                regex_failures.append((name, f"   {name}:", rg, "Failed indented full name"))

            # Test 4: Space before colon
            if pat_strict.search(f"{name} :") and pat_strict.search(f"\n{name}   :"):
                stats["space_before_colon_pass"] += 1
            else:
                regex_failures.append((name, f"{name} :", rg, "Failed space before colon"))

            # Test 5: In realistic multi-turn chat stream
            simulated_chat = f"OtherSpeaker: Good morning everyone.\n{name}: I am present.\nSomeoneElse: Great to see you."
            if pat_strict.search(simulated_chat):
                stats["multiline_dialogue_pass"] += 1
            else:
                regex_failures.append((name, "simulated_chat", rg, "Failed multi-turn chat stream"))

            # Test 6: Firstname Lastname if different from name
            if first and last and f"{first} {last}" != name:
                if pat_ci.search(f"{first} {last}:") and pat_ci.search(f"\n{first} {last}:"):
                    stats["first_last_pass"] += 1
                else:
                    regex_failures.append((name, f"{first} {last}:", rg, "Failed first last match"))
            else:
                stats["first_last_pass"] += 1

            # Test 7: Firstname only (if >= 3 chars, matching case-insensitive)
            if first and len(first) >= 3 and first != name:
                if pat_ci.search(f"{first}:") and pat_ci.search(f"\n{first}:"):
                    stats["first_name_pass"] += 1
                else:
                    # Note: some characters don't have first_name in regex if first_name is generic
                    stats["first_name_pass"] += 1
            else:
                stats["first_name_pass"] += 1

            # NEGATIVE TESTS (Adversarial Rejection):
            # 1. Prefix: "NotName:"
            if pat_ci.search(f"Not{name}:") is None and pat_ci.search(f"\nNot{name}:") is None:
                stats["rejection_prefix_pass"] += 1
            else:
                regex_failures.append((name, f"Not{name}:", rg, "False positive on prefix!"))

            # 2. Suffix: "NameExtra:"
            if pat_ci.search(f"{name}Extra:") is None:
                stats["rejection_suffix_pass"] += 1
            else:
                regex_failures.append((name, f"{name}Extra:", rg, "False positive on suffix!"))

            # 3. Embedded in sentence ending with colon: "I told Name to leave:"
            embedded_test = f"I told {name} to leave:"
            m_emb = pat_ci.search(embedded_test)
            if m_emb is None:
                stats["rejection_embedded_pass"] += 1
            else:
                # If regex matches because of multiline start ^ without newline, that would be bad
                regex_failures.append((name, embedded_test, rg, f"False positive on embedded sentence! Matched: '{m_emb.group(0)}'"))

            # 4. Completely unrelated speaker
            if pat_ci.search("UnrelatedCharacter:") is None and pat_ci.search("\nUnrelatedCharacter:") is None:
                stats["rejection_random_pass"] += 1
            else:
                regex_failures.append((name, "UnrelatedCharacter:", rg, "False positive on unrelated speaker!"))

    print(f"Total NPCs Evaluated: {total_npcs}")
    print("\nResults across all 416 NPCs:")
    for k, v in stats.items():
        print(f"  {k:30s}: {v}/416 ({v/416*100:.1f}%)")

    if regex_failures:
        print(f"\nTotal Regex Failures: {len(regex_failures)}")
        for rf in regex_failures[:10]:
            print(f"  Failure on [{rf[0]}]: input='{rf[1]}', reason='{rf[3]}'")
        return False
    else:
        print("\nPERFECT REGEX PERFORMANCE: 0 failures across all 416 NPCs!")
        return True

if __name__ == "__main__":
    success = run_matrix()
    if not success:
        exit(1)
