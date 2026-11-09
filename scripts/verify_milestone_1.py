import sys
import pathlib

def run_verification():
    print("=" * 60)
    print("MILESTONE 1 VERIFICATION AUDIT")
    print("=" * 60)
    
    files_to_check = [
        "knowledge/Lore_Worldbuilding/ACADEMIC_INSTITUTIONS_ST_BRUGGE_AND_SUCC.md",
        "knowledge/Lore_Worldbuilding/APPLIED_RUNIC_CRYSTALLOGRAPHY_AND_MAGITECH.md",
        "knowledge/Lore_Worldbuilding/PLANAR_COSMOLOGY_ABYSSAL_VS_VOID_MAGIC.md",
        "knowledge/Lore_Worldbuilding/FATHER_REVAZHAEL_AND_SUPERIOR_DEMONS.md",
        "knowledge/Lore_Worldbuilding/ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md",
        "knowledge/Lore_Worldbuilding/DCC_SECURITY_CAMPUS_INTEGRATION_AND_ATHLETICS.md",
    ]
    
    modified_files = [
        "knowledge/Lore_Worldbuilding/EXTERNAL_RESOURCES_INDEX.md",
    ]
    
    # 1. Existence and size of 6 knowledge vault files
    print("\n--- Check 1: Existence and File Size (> 1,000 bytes) ---")
    all_exist = True
    for p in files_to_check:
        path = pathlib.Path(p)
        if not path.exists():
            print(f"[FAIL] Missing file: {p}")
            all_exist = False
        else:
            size = path.stat().st_size
            if size <= 1000:
                print(f"[FAIL] File too small ({size} bytes): {p}")
                all_exist = False
            else:
                print(f"[PASS] {p} ({size} bytes)")
    assert all_exist, "Check 1 Failed!"
    
    # 2. Check for 0 em-dashes (—) across all created and modified files
    print("\n--- Check 2: Zero Em-Dashes (\u2014) ---")
    all_zero_em_dash = True
    for p in files_to_check + modified_files:
        path = pathlib.Path(p)
        content = path.read_text(encoding="utf-8")
        em_count = content.count("\u2014")
        if em_count > 0:
            print(f"[FAIL] {em_count} em-dashes found in {p}")
            all_zero_em_dash = False
        else:
            print(f"[PASS] 0 em-dashes in {p}")
    assert all_zero_em_dash, "Check 2 Failed!"

    # Also verify synchronized lines in docs/world/Svartulfr_World_Doc.md
    print("\n--- Check 2b: Synchronized Lines in docs/world/Svartulfr_World_Doc.md ---")
    doc_path = pathlib.Path("docs/world/Svartulfr_World_Doc.md")
    doc_content = doc_path.read_text(encoding="utf-8")
    sync_keywords = ["Father Rev, an ancient Superior Demon", "St. Brugge Private Academy", "Dal 26 agosto 2024", "Suite 3, condivisa da Alyssa Douglas"]
    for kw in sync_keywords:
        assert kw in doc_content, f"Missing synchronized keyword in Svartulfr_World_Doc.md: {kw}"
        print(f"[PASS] Found synchronized snippet: {kw}")
    
    # 3. Strict positive framing (0 negative ear framing, 0 forbidden lamia locomotion tokens)
    print("\n--- Check 3: Strict Positive Framing ---")
    negative_phrases = ["no human ears", "senza orecchie umane", "prive di orecchie umane", "without human ears", "lacks human ears"]
    all_positive = True
    for p in files_to_check + modified_files + ["docs/world/Svartulfr_World_Doc.md"]:
        path = pathlib.Path(p)
        content = path.read_text(encoding="utf-8").lower()
        for phrase in negative_phrases:
            if phrase in content:
                print(f"[FAIL] Negative framing phrase '{phrase}' found in {p}")
                all_positive = False
    
    # Sierra Cruz locomotion check
    forbidden_sierra_words = [r"\bfeet\b", r"\bfoot\b", r"\blegs\b", r"\bshoes\b", r"\bwalk\b", r"\bstep\b"]
    for p in files_to_check:
        path = pathlib.Path(p)
        raw_text = path.read_text(encoding="utf-8")
        if "Sierra" in raw_text:
            for line in raw_text.splitlines():
                if "Sierra" in line:
                    import re
                    for pat in forbidden_sierra_words:
                        if re.search(pat, line, re.IGNORECASE):
                            print(f"[FAIL] Forbidden lamia term '{pat}' in {p}: {line}")
                            all_positive = False
    
    if all_positive:
        print("[PASS] Zero occurrences of negative ear framing and forbidden lamia terms detected across all inspected files.")
    assert all_positive, "Check 3 Failed!"
    
    # 4. EXTERNAL_RESOURCES_INDEX.md reflects updated knowledge vault articles
    print("\n--- Check 4: EXTERNAL_RESOURCES_INDEX.md Reflection ---")
    index_path = pathlib.Path("knowledge/Lore_Worldbuilding/EXTERNAL_RESOURCES_INDEX.md")
    index_content = index_path.read_text(encoding="utf-8")
    for f in files_to_check:
        fname = pathlib.Path(f).name
        assert fname in index_content, f"Missing vault article reference in index: {fname}"
        print(f"[PASS] Index references {fname}")
    assert "Second Brain Knowledge Vault (Worldbuilding)" in index_content, "Missing category in index"
    print("[PASS] Second Brain Knowledge Vault category confirmed in EXTERNAL_RESOURCES_INDEX.md")
    
    print("\n" + "=" * 60)
    print("ALL MILESTONE 1 VERIFICATION CHECKS PASSED (100% OK)")
    print("=" * 60)

if __name__ == "__main__":
    run_verification()
