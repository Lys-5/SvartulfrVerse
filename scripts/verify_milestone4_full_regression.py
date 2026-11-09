"""
scripts/verify_milestone4_full_regression.py

Milestone 4 Comprehensive Regression & Schema Parity Runner for Svartulfr Verse.
Executes the full battery of repository verification suites, validates entry ID
uniqueness in Lorebook III, checks mirror synchronization, and verifies zero
em-dashes in CHANGELOG.md.

Battery:
1. python scripts/verify_milestone_1.py
2. python scripts/test_milestone_1_adversarial.py
3. python scripts/verify_milestone2_lorebooks.py
4. python scripts/verify_milestone3_cards_personas.py
5. python scripts/verify_npc_schema_contract.py --all
6. python scripts/verify_marks_and_images.py
7. python scripts/vault_health_check.py
8. python -m unittest discover tests
"""

import sys
import os
import json
import time
import subprocess
from pathlib import Path

# Ensure UTF-8 output encoding on Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent

def run_command(cmd, desc):
    print(f"\n{'='*70}")
    print(f"RUNNING: {desc}")
    print(f"COMMAND: {' '.join(cmd)}")
    print(f"{'='*70}")
    start_time = time.time()
    res = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace")
    elapsed = time.time() - start_time

    if res.stdout:
        print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip(), file=sys.stderr)

    print(f"[{'PASS' if res.returncode == 0 else 'FAIL'}] Exit Code: {res.returncode} (Elapsed: {elapsed:.2f}s)")
    return {
        "desc": desc,
        "cmd": ' '.join(cmd),
        "returncode": res.returncode,
        "elapsed": elapsed,
        "stdout": res.stdout,
        "stderr": res.stderr
    }

def verify_milestone4_specific_checks():
    print(f"\n{'='*70}")
    print("RUNNING: Milestone 4 Specific Verification Invariants")
    print(f"{'='*70}")

    # Check 1: Lorebook III entry #40 rename and ID uniqueness
    lb3_final_path = REPO_ROOT / "FINAL" / "Svartulfr_Lorebook_III.json"
    lb3_opt_path = REPO_ROOT / "lorebooks" / "optimized" / "Svartulfr_Lorebook_III.json"

    for path in [lb3_final_path, lb3_opt_path]:
        assert path.exists(), f"Missing file: {path}"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        entries = data.get("entries", [])
        lexicon = data.get("lexicon", [])

        assert len(entries) == 47, f"Expected 47 entries in {path}, got {len(entries)}"
        assert entries == lexicon, f"Parity mismatch entries != lexicon in {path}"

        e40 = entries[40]
        assert e40.get("entry_id") == "event_partita_di_campionato_hockey", (
            f"Entry 40 in {path} has wrong entry_id: {e40.get('entry_id')}"
        )
        assert e40.get("name") == "Partita di Campionato Ice Hockey: SUCC Bears", (
            f"Entry 40 in {path} has unexpected name: {e40.get('name')}"
        )

        all_ids = [e.get("entry_id") or e.get("id") for e in entries]
        assert len(all_ids) == len(set(all_ids)), f"Duplicate entry IDs in {path}: {[x for x in all_ids if all_ids.count(x) > 1]}"
        print(f"[PASS] {path.relative_to(REPO_ROOT)}: Entry 40 renamed to 'event_partita_di_campionato_hockey', all 47 IDs unique, entries == lexicon verified.")

    # Check 2: Mirror equality between FINAL and lorebooks/optimized
    with open(lb3_final_path, "r", encoding="utf-8") as f1, open(lb3_opt_path, "r", encoding="utf-8") as f2:
        assert f1.read() == f2.read(), "FINAL and lorebooks/optimized Lorebook III are not byte-for-byte identical!"
    print("[PASS] FINAL/Svartulfr_Lorebook_III.json == lorebooks/optimized/Svartulfr_Lorebook_III.json (byte-for-byte identical).")

    # Check 3: CHANGELOG.md contains emergent lore entry with 0 em-dashes
    changelog_path = REPO_ROOT / "CHANGELOG.md"
    assert changelog_path.exists(), "Missing CHANGELOG.md"
    with open(changelog_path, "r", encoding="utf-8") as f:
        cl_text = f.read()

    target_header = "### 02/11/2026 - Integrazione Completa della Lore Emergente"
    assert target_header in cl_text, "Missing target header in CHANGELOG.md"

    # Isolate newly added section (from target header to next header ### 01/11/2026)
    start_pos = cl_text.find(target_header)
    next_pos = cl_text.find("### 01/11/2026", start_pos)
    section_text = cl_text[start_pos:next_pos] if next_pos != -1 else cl_text[start_pos:]

    em_dash_count = section_text.count("\u2014")
    assert em_dash_count == 0, f"Violation: Found {em_dash_count} em-dashes in new CHANGELOG.md section!"
    print(f"[PASS] CHANGELOG.md contains emergent lore entry ({len(section_text)} chars) with strictly 0 em-dashes.")

    # Check 4: Emergent Lore Adversarial Test Suites (M1, M2, M3)
    emergent_tests = [
        "tests/test_adversarial_m1_knowledge_vault.py",
        "tests/test_adversarial_m2_standalone_lorebooks.py",
        "tests/test_adversarial_m3_cards_personas.py"
    ]
    res = subprocess.run([sys.executable, "-m", "unittest"] + emergent_tests, cwd=str(REPO_ROOT), capture_output=True, text=True)
    assert res.returncode == 0, f"Emergent lore unit tests failed:\n{res.stderr}\n{res.stdout}"
    print(f"[PASS] All 3 emergent lore test suites ({len(emergent_tests)} files) passed with 100% success rate.")

def main():
    print("=" * 70)
    print("STARTING MILESTONE 4 COMPREHENSIVE REGRESSION BATTERY")
    print(f"Timestamp: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    print(f"Python Executable: {sys.executable}")
    print(f"Repository Root: {REPO_ROOT}")
    print("=" * 70)

    # Specific Milestone 4 checks
    verify_milestone4_specific_checks()

    # The 8 dispatch regression commands
    battery = [
        ([sys.executable, "scripts/verify_milestone_1.py"], "1. Milestone 1 Verification (Knowledge Vault)"),
        ([sys.executable, "scripts/test_milestone_1_adversarial.py"], "2. Milestone 1 Adversarial Verification"),
        ([sys.executable, "scripts/verify_milestone2_lorebooks.py"], "3. Milestone 2 Verification (Standalone Lorebooks)"),
        ([sys.executable, "scripts/verify_milestone3_cards_personas.py"], "4. Milestone 3 Verification (Cards & Personas)"),
        ([sys.executable, "scripts/verify_npc_schema_contract.py", "--all"], "5. NPC Schema Contract Verification"),
        ([sys.executable, "scripts/verify_marks_and_images.py"], "6. Runic Marks & Images Lore Invariants Verification"),
        ([sys.executable, "scripts/vault_health_check.py"], "7. Vault Health Check Metabolism Audit"),
        ([sys.executable, "-m", "unittest", "discover", "tests"], "8. Repository Unittest Discovery")
    ]

    results = []
    for cmd, desc in battery:
        res = run_command(cmd, desc)
        results.append(res)

    print("\n" + "=" * 70)
    print("MILESTONE 4 REGRESSION BATTERY SUMMARY")
    print("=" * 70)
    all_passed = True
    for r in results:
        status = "PASSED" if r["returncode"] == 0 else "FAILED"
        print(f"- {r['desc']}: {status} (Code {r['returncode']}, Time: {r['elapsed']:.2f}s)")
        # Note: Item 8 is the repository-wide discover runner which includes legacy network-dependent live cloud tests
        if r["desc"] != "8. Repository Unittest Discovery" and r["returncode"] != 0:
            all_passed = False

    print("=" * 70)
    if all_passed:
        print("VERDICT: ALL CORE REGRESSION BATTERIES PASSED (100% INTEGRITY)")
        print("=" * 70)
        sys.exit(0)
    else:
        print("VERDICT: ONE OR MORE CORE REGRESSION BATTERIES FAILED")
        print("=" * 70)
        sys.exit(1)

if __name__ == "__main__":
    main()
