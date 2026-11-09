"""
Empirical Challenger Test Suite for Milestone 1: Vault Second Brain Knowledge Documentation
Author: challenger_m1_1
Target: knowledge/Lore_Worldbuilding/*.md, docs/world/Svartulfr_World_Doc.md, EXTERNAL_RESOURCES_INDEX.md
"""

import os
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(r"e:\repository\SvartulfrVerse")
VAULT_DIR = REPO_ROOT / "knowledge" / "Lore_Worldbuilding"
WORLD_DOC = REPO_ROOT / "docs" / "world" / "Svartulfr_World_Doc.md"
INDEX_DOC = VAULT_DIR / "EXTERNAL_RESOURCES_INDEX.md"

NEW_ARTICLES = [
    "ACADEMIC_INSTITUTIONS_ST_BRUGGE_AND_SUCC.md",
    "APPLIED_RUNIC_CRYSTALLOGRAPHY_AND_MAGITECH.md",
    "PLANAR_COSMOLOGY_ABYSSAL_VS_VOID_MAGIC.md",
    "FATHER_REVAZHAEL_AND_SUPERIOR_DEMONS.md",
    "ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md",
    "DCC_SECURITY_CAMPUS_INTEGRATION_AND_ATHLETICS.md",
]

all_passed = True
results = []

def report(check_name: str, passed: bool, details: str = ""):
    global all_passed
    if not passed:
        all_passed = False
    status = "PASS" if passed else "FAIL"
    msg = f"[{status}] {check_name}"
    if details:
        msg += f"\n       Details: {details}"
    results.append(msg)
    print(msg)

print("=" * 70)
print("EMPIRICAL CHALLENGER AUDIT: MILESTONE 1")
print("=" * 70)

# -------------------------------------------------------------
# TEST 1: Rigorous Unicode Dash Stress-Test
# -------------------------------------------------------------
print("\n--- TEST 1: Rigorous Unicode Dash Scan ---")
FORBIDDEN_DASHES = {
    '\u2014': "EM DASH (—)",
    '\u2013': "EN DASH (–)",
    '\u2015': "HORIZONTAL BAR (―)",
    '\u2E3A': "TWO-EM DASH (⸺)",
    '\u2E3B': "THREE-EM DASH (⸻)",
    '\uFE58': "SMALL EM DASH (﹘)",
    '\uFF0D': "FULLWIDTH HYPHEN-MINUS (－)",
}

for fname in NEW_ARTICLES + ["EXTERNAL_RESOURCES_INDEX.md"]:
    fpath = VAULT_DIR / fname
    if not fpath.exists():
        report(f"File exists: {fname}", False, "File not found!")
        continue
    content = fpath.read_text(encoding="utf-8")
    found_dashes = []
    for line_idx, line in enumerate(content.splitlines(), start=1):
        for char in line:
            if char in FORBIDDEN_DASHES:
                found_dashes.append((line_idx, FORBIDDEN_DASHES[char], line[:80]))
    if found_dashes:
        details = "; ".join([f"Line {l}: {t} in '{snip}'" for l, t, snip in found_dashes[:5]])
        report(f"Dash scan in {fname}", False, f"{len(found_dashes)} violations found: {details}")
    else:
        report(f"Dash scan in {fname}", True, "Zero forbidden Unicode dashes.")

# Check the synchronized lines in docs/world/Svartulfr_World_Doc.md
if WORLD_DOC.exists():
    wlines = WORLD_DOC.read_text(encoding="utf-8").splitlines()
    check_line_numbers = [291, 870, 873, 1044]  # 1-indexed
    sync_dash_violations = []
    for ln in check_line_numbers:
        if ln <= len(wlines):
            line = wlines[ln - 1]
            for char in line:
                if char in FORBIDDEN_DASHES:
                    sync_dash_violations.append((ln, FORBIDDEN_DASHES[char], line[:80]))
    if sync_dash_violations:
        details = "; ".join([f"Line {l}: {t}" for l, t, _ in sync_dash_violations])
        report("Dash scan in Svartulfr_World_Doc synchronized lines", False, details)
    else:
        report("Dash scan in Svartulfr_World_Doc synchronized lines", True, "Zero forbidden dashes in synced lines.")

# -------------------------------------------------------------
# TEST 2: Negative Framing & Anatomical Invariants Stress-Test
# -------------------------------------------------------------
print("\n--- TEST 2: Negative Framing & Anatomical Invariants ---")
NEGATIVE_EAR_PATTERNS = [
    r"(?:no|without|lacks?|lacking|absence\s+of|devoid\s+of|prive?|senza|non\s+hanno|nessun[a-z]*)\s+[^.\n]*?(?:human\s+ears|orecchie\s+umane)",
    r"(?:human\s+ears|orecchie\s+umane)\s+[^.\n]*?(?:missing|absent|lacking|non\s+esistenti|assenti)",
    r"--no\s+human\s+ears",  # Should not be in lore text
]

for fname in NEW_ARTICLES:
    fpath = VAULT_DIR / fname
    content = fpath.read_text(encoding="utf-8")
    violations = []
    for pattern in NEGATIVE_EAR_PATTERNS:
        matches = list(re.finditer(pattern, content, re.IGNORECASE))
        if matches:
            for m in matches:
                violations.append(m.group(0))
    if violations:
        report(f"Positive ear framing in {fname}", False, f"Violations: {violations}")
    else:
        report(f"Positive ear framing in {fname}", True, "Clean positive formulation.")

# Sierra Cruz anatomical check: strictly 0 legs, feet, knees, shoes, walk, step
SIERRA_FORBIDDEN_WORDS = [r"\blegs?\b", r"\bfeet\b", r"\bfoot\b", r"\bknees?\b", r"\bshoes?\b", r"\bgambe\b", r"\bpiedi\b", r"\bpiede\b", r"\bginocch[io]\b", r"\bscarpe\b"]
for fname in NEW_ARTICLES:
    fpath = VAULT_DIR / fname
    content = fpath.read_text(encoding="utf-8")
    if "Sierra Cruz" in content or "Sierra" in content:
        # Extract sentences mentioning Sierra
        sentences = re.split(r'[.!?\n]', content)
        sierra_violations = []
        for s in sentences:
            if "Sierra" in s:
                for fw in SIERRA_FORBIDDEN_WORDS:
                    if re.search(fw, s, re.IGNORECASE):
                        # Make sure it's not explicitly saying "zero legs" or "limbless"
                        sierra_violations.append(f"Suspicious word '{fw}' in sentence: '{s.strip()}'")
        if sierra_violations:
            report(f"Sierra Cruz anatomy in {fname}", False, "; ".join(sierra_violations))
        else:
            report(f"Sierra Cruz anatomy in {fname}", True, "Proper slithering/limbless formulation.")

# Scarlett Rose check: candy-pink hair, candy-pink eyes, two scarlet horns when her profile is described
for fname in NEW_ARTICLES:
    fpath = VAULT_DIR / fname
    content = fpath.read_text(encoding="utf-8")
    if "### 3.2 Academic Tracks" in content and "Scarlett Rose" in content:
        has_candy_pink = "candy-pink" in content.lower()
        has_horns = "scarlet horns" in content.lower() or "corna scarlatte" in content.lower()
        if has_candy_pink and has_horns:
            report(f"Scarlett Rose attributes in {fname}", True, "Has candy-pink hair/eyes and scarlet horns.")
        else:
            report(f"Scarlett Rose attributes in {fname}", False, f"candy-pink: {has_candy_pink}, horns: {has_horns}")

# Check Canonical Filename Orthography for Alyssa
alyssa_file_canonical = (VAULT_DIR / "ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md").exists()
alyssa_file_actual = (VAULT_DIR / "ALISSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md").exists()
if alyssa_file_actual and not alyssa_file_canonical:
    report("Canonical Filename Orthography (Alyssa vs Alissa)", False, "File named ALISSA_... instead of canonical ALYSSA_... (inside content uses Alyssa throughout).")
else:
    report("Canonical Filename Orthography (Alyssa vs Alissa)", True, "File named ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md.")

# Divine Marks check: Mani left hip, Sol right hip
for fname in NEW_ARTICLES:
    fpath = VAULT_DIR / fname
    content = fpath.read_text(encoding="utf-8")
    if "Mark of Mani" in content or "Maniulfr" in content:
        mani_left_hip = bool(re.search(r"Mark\s+of\s+Mani.*?left\s+hip", content, re.IGNORECASE))
        report(f"Mani mark location in {fname}", mani_left_hip, "Mark of Mani properly located on left hip.")
    if "Mark of Sol" in content or "Solulfr" in content:
        sol_right_hip = bool(re.search(r"Mark\s+of\s+Sol.*?right\s+hip", content, re.IGNORECASE))
        report(f"Sol mark location in {fname}", sol_right_hip, "Mark of Sol properly located on right hip.")

# -------------------------------------------------------------
# TEST 3: Link Graph & Cross-Reference Integrity
# -------------------------------------------------------------
print("\n--- TEST 3: Link Graph & Cross-Reference Resolution ---")
broken_links = []
total_links = 0

for fname in NEW_ARTICLES:
    fpath = VAULT_DIR / fname
    content = fpath.read_text(encoding="utf-8")
    
    # Standard Markdown Links: [label](target)
    md_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for label, target in md_links:
        total_links += 1
        # Ignore external web links
        if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
            continue
        # Split target and anchor
        parts = target.split('#', 1)
        target_file = parts[0]
        anchor = parts[1] if len(parts) > 1 else None
        
        if target_file:
            resolved_path = (fpath.parent / target_file).resolve()
            if not resolved_path.exists():
                broken_links.append((fname, f"Target file missing: {target} (resolved to {resolved_path})"))
            elif anchor:
                target_content = resolved_path.read_text(encoding="utf-8")
                # Basic heading slug check
                expected_heading = anchor.replace('-', ' ')
                if expected_heading.lower() not in target_content.lower():
                    broken_links.append((fname, f"Anchor #{anchor} might not exist in {target_file}"))
        elif anchor:
            # Anchor in same file
            expected_heading = anchor.replace('-', ' ')
            if expected_heading.lower() not in content.lower():
                broken_links.append((fname, f"Self-anchor #{anchor} might not exist in {fname}"))

    # Wikilinks: [[target]] or [[target|alias]]
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
    for wl in wikilinks:
        total_links += 1
        target = wl.split('|')[0].strip()
        target_fpath = (VAULT_DIR / f"{target}.md")
        if not target_fpath.exists() and not (VAULT_DIR / target).exists():
            broken_links.append((fname, f"Broken wikilink [[{wl}]]"))

if broken_links:
    for src, err in broken_links:
        report(f"Link integrity in {src}", False, err)
else:
    report("Internal Link Graph", True, f"All {total_links} links resolved cleanly to existing files.")

# Check EXTERNAL_RESOURCES_INDEX references to new articles
index_content = INDEX_DOC.read_text(encoding="utf-8")
for article in NEW_ARTICLES:
    present_in_index = article in index_content
    report(f"Index references {article}", present_in_index, "Referenced in Section 3.11 & 5")

# -------------------------------------------------------------
# TEST 4: Metadata Headers & Frontmatter Consistency
# -------------------------------------------------------------
print("\n--- TEST 4: Metadata Header Schema Validation ---")
for fname in NEW_ARTICLES:
    fpath = VAULT_DIR / fname
    content = fpath.read_text(encoding="utf-8")
    lines = content.splitlines()
    has_title = lines[0].startswith("# ")
    has_version = bool(re.search(r"\*\*Version:\*\*\s*\d+\.\d+", content))
    has_date = bool(re.search(r"\*\*Date:\*\*\s*2026-\d{2}-\d{2}", content))
    has_classification = bool(re.search(r"\*\*Classification:\*\*", content))
    has_authority = bool(re.search(r"\*\*Authority:\*\*", content))
    has_cross_ref = "## " in content and "Cross-References" in content
    
    header_valid = has_title and has_version and has_date and has_classification and has_authority and has_cross_ref
    details = f"Title: {has_title}, Version: {has_version}, Date: {has_date}, Class: {has_classification}, Auth: {has_authority}, CrossRef: {has_cross_ref}"
    report(f"Metadata header schema for {fname}", header_valid, details)

# -------------------------------------------------------------
# TEST 5: Comprehensive Coverage Oracle of 6 Core Themes
# -------------------------------------------------------------
print("\n--- TEST 5: 6 Core Themes Comprehensive Coverage Oracle ---")

# Theme 1: St. Brugge Private Academy
t1_file = VAULT_DIR / "ACADEMIC_INSTITUTIONS_ST_BRUGGE_AND_SUCC.md"
t1_text = t1_file.read_text(encoding="utf-8")
t1_checks = [
    ("Gothic architecture / ward-locked libraries", "Gothic" in t1_text and "Ward-Locked" in t1_text),
    ("Curriculum (magic, history, alchemy, demonology, runes)", "Elder Futhark" in t1_text and "Alchemy" in t1_text),
    ("Alyssa & Jasper attendance", "Alyssa and Jasper" in t1_text and "preschool through their middle" in t1_text),
    ("Father Revazhael tutorials", "Father Revazhael" in t1_text and "private instruction" in t1_text),
    ("Erik Douglas / Wulfnic knowledge", "Jarl Erik Douglas" in t1_text and "Wulfnic" in t1_text),
]
for desc, res in t1_checks:
    report(f"Theme 1 (St. Brugge): {desc}", res)

# Theme 2: Father Revazhael (Superior Demon)
t2_file = VAULT_DIR / "FATHER_REVAZHAEL_AND_SUPERIOR_DEMONS.md"
t2_text = t2_file.read_text(encoding="utf-8")
t2_checks = [
    ("Superior Demon / Greater Incubus", "Ancient Superior Demon" in t2_text and "Greater Incubus" in t2_text),
    ("Secret True Name Revazhael & submission vulnerability", "Revazhael" in t2_text and "true name" in t2_text.lower() and "submission" in t2_text.lower()),
    ("Ethos of consent", "unyielding consent" in t2_text.lower()),
    ("Physical description & scent", "6'2\"" in t2_text and "vanilla" in t2_text.lower() and "horns" in t2_text.lower()),
    ("Abyssal Armor & twin daggers invocation", "Mor'gath xul vrak'thar, kor'eth zaram" in t2_text),
    ("Refuge Key & Kobal butler", "La Dimora del Rifugio" in t2_text and "Kobal" in t2_text),
    ("SUCC ARO resident & TIT handyman", "Alpha Rho Omega" in t2_text and "handyman" in t2_text.lower()),
]
for desc, res in t2_checks:
    report(f"Theme 2 (Father Revazhael): {desc}", res)

# Theme 3: Applied Runic Crystallography & Resonant Cylinders
t3_file = VAULT_DIR / "APPLIED_RUNIC_CRYSTALLOGRAPHY_AND_MAGITECH.md"
t3_text = t3_file.read_text(encoding="utf-8")
t3_checks = [
    ("Elder Futhark + crystal lattices", "Elder Futhark" in t3_text and "crystal lattices" in t3_text.lower()),
    ("Spell-freezing mechanics", "Incantesimi Congelati" in t3_text or "Spell Freezing" in t3_text),
    ("Cylinder dimensions & snap activation", ("8 to 10 cm" in t3_text or "index-finger" in t3_text) and "snap" in t3_text.lower()),
    ("Comparison table vs commercial DMHA", "Commercial DMHA Guild Cylinders" in t3_text and "40-50%" in t3_text),
    ("Individual resonance tuning", "harmonic frequency" in t3_text.lower() or "individual aura" in t3_text.lower()),
    ("Alyssa & Jasper twin collaboration", "Alyssa" in t3_text and "Jasper" in t3_text and "Sound and Acoustic Engineering" in t3_text),
]
for desc, res in t3_checks:
    report(f"Theme 3 (Crystallography & Cylinders): {desc}", res)

# Theme 4: Planar Cosmology (Abyssal vs Void Magic)
t4_file = VAULT_DIR / "PLANAR_COSMOLOGY_ABYSSAL_VS_VOID_MAGIC.md"
t4_text = t4_file.read_text(encoding="utf-8")
t4_checks = [
    ("Deep Infernal Abyss vs Interstitial Void", "Deep Infernal Abyss" in t4_text and "Interstitial Space" in t4_text),
    ("Exothermic vs Endothermic", "Exothermic" in t4_text and "Endothermic" in t4_text),
    ("Sovereign authority vs entropy", "Sovereign Authority" in t4_text and "Entropy" in t4_text),
    ("Ontological comparison matrix", "Ontological Comparison Matrix" in t4_text),
    ("Sierra Cruz academic observation", "Sierra Cruz" in t4_text and "monografia seria" in t4_text),
]
for desc, res in t4_checks:
    report(f"Theme 4 (Abyssal vs Void Magic): {desc}", res)

# Theme 5: Alyssa Field Credentials & Sanctuary
t5_file = VAULT_DIR / "ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md"
t5_text = t5_file.read_text(encoding="utf-8")
t5_checks = [
    ("Pre-Med at SUCC", "Pre-Med" in t5_text),
    ("Certified Guild Healer Rank A", "Certified Guild Healer" in t5_text and "Rank A" in t5_text),
    ("Hunter ID ADB-555 & SR3S Pass", "ADB-555" in t5_text and "SR3S" in t5_text),
    ("Absolute Pacifist Vow & Dragon Glass Katana given to Jasper", "Absolute Pacifist Vow" in t5_text and "Dragon Glass Katana" in t5_text),
    ("Dimensional Pochette with crystal glassware", "Dimensional Pochette" in t5_text and "distillation" in t5_text.lower()),
    ("Suite 3 Bed Nest & Wolfy plush", "Bed Nest" in t5_text and "Wolfy" in t5_text),
]
for desc, res in t5_checks:
    report(f"Theme 5 (Alyssa Credentials): {desc}", res)

# Theme 6: Jasper Hunter & KSA
t6_checks = [
    ("Acoustic & Sound Engineering at SUCC", "Acoustic and Sound Engineering" in t5_text),
    ("Registered Guild Hunter Rank A", "Registered Guild Hunter" in t5_text and "Rank A" in t5_text),
    ("Hunter ID JDB-555 & SR3S Pass", "JDB-555" in t5_text and "SR3S" in t5_text),
    ("Dragon Glass Katana & Abyssal Armor", "Dragon Glass Katana" in t5_text and "Abyssal Armor" in t5_text),
    ("Runic Translation & Harmonic Attunement", "translator of ancient runes" in t5_text.lower()),
    ("Welcome Fest KSA intimidation", "Kappa Sigma Alpha" in t5_text and "Welcome Fest" in t5_text),
]
for desc, res in t6_checks:
    report(f"Theme 6 (Jasper Credentials): {desc}", res)

# Additional Theme: DCC Security & Athletics
t7_file = VAULT_DIR / "DCC_SECURITY_CAMPUS_INTEGRATION_AND_ATHLETICS.md"
t7_text = t7_file.read_text(encoding="utf-8")
t7_checks = [
    ("Chancellor Archer Wolfwood + Erik Douglas accord", "Chancellor Archer Wolfwood" in t7_text and "Erik Douglas" in t7_text),
    ("Bears hockey head coach & 05:30 AM practices", "Bears" in t7_text and "05:30 AM" in t7_text),
    ("Major Kaladin Nargathon + Chief Warg", "Kaladin Nargathon" in t7_text and "Chief Warg" in t7_text),
    ("Biometric drones & CCTV feeds", "Biometric Drones" in t7_text and "CCTV" in t7_text),
    ("Barkley Rover golden retriever demi-human", "Barkley Rover" in t7_text and "golden retriever" in t7_text.lower()),
    ("Greek Row (TIT, ARO, ASS, KSA)", "TIT" in t7_text and "ARO" in t7_text and "ASS" in t7_text and "KSA" in t7_text),
]
for desc, res in t7_checks:
    report(f"Additional Theme (DCC & Athletics): {desc}", res)

print("\n" + "=" * 70)
if all_passed:
    print(f"VERDICT: ALL {len(results)} CHECKS PASSED EMPIRICALLY (100% OK)")
else:
    print(f"VERDICT: FAILURES DETECTED IN SUITE")
print("=" * 70)

sys.exit(0 if all_passed else 1)
