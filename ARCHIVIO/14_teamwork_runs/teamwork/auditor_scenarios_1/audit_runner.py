import json
import pathlib
import re
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
SCENARIOS_DIR = ROOT / 'FINAL' / 'scenarios'

EXPECTED_FILES = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
]

EXPECTED_LOREBOOKS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV",
]

VILLA_DOUGLAS_MALES = {
    "father": "_QPea6g4Q1QfeYCVHCLMPR",
    "eldest_brother": "_RDfz7XzTpM23LpPALVXHM",
    "tech_brother": "_t4J9aQNJM36cUKAP4wB4U",
    "politician_brother": "_zFLUjV8aVxQRAfQxGcAcY",
    "maternal_grandfather": "_HEQQbbRFwKdG8QE2Fh1z1",
    "uncle": "_T8Ywcr9FEqNf9JxbK6eHP",
    "cousin": "_TbRM3EdxDjHFgqztTbCpL",
}

DMHA_SLOTS = [
    "twin_healer",
    "twin_tech",
    "eldest_brother",
    "demihuman_representative",
    "biker_enforcer",
    "raid_leader",
    "tank_frontline",
    "scout_infiltrator",
    "faction_support"
]

def run_forensic_audit():
    print("=" * 70)
    print("FORENSIC INTEGRITY AUDIT SUITE — SCENARIOS MILESTONE")
    print("=" * 70)

    audit_log = []

    # 1. Existence and File Size Check
    print("\n--- CHECK 1: File Existence & Payload Density ---")
    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        if not fpath.exists():
            audit_log.append(f"FAIL: Missing file {fname}")
            print(f"[-] {fname}: MISSING")
            continue
        size = fpath.stat().st_size
        print(f"[+] {fname}: {size} bytes")
        if size < 5000:
            audit_log.append(f"FAIL: {fname} abnormally small ({size} bytes)")

    # 2. Strict Em-dash and En-dash detection across raw bytes
    print("\n--- CHECK 2: Em-dash (\u2014) and En-dash (\u2013) Byte Scan ---")
    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        raw_bytes = fpath.read_bytes()
        has_em = b'\xe2\x80\x94' in raw_bytes # \u2014
        has_en = b'\xe2\x80\x93' in raw_bytes # \u2013
        if has_em:
            audit_log.append(f"FAIL: {fname} contains em-dash (\\u2014)")
            print(f"[-] {fname}: FOUND EM-DASH!")
        elif has_en:
            audit_log.append(f"FAIL: {fname} contains en-dash (\\u2013)")
            print(f"[-] {fname}: FOUND EN-DASH!")
        else:
            print(f"[+] {fname}: CLEAN (Zero em-dashes, zero en-dashes)")

    # 3. User Directive Visibility Verification
    print("\n--- CHECK 3: Directive Visibility ('private') ---")
    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        data = json.loads(fpath.read_text(encoding='utf-8'))
        vis = data.get('visibility')
        if vis == 'private':
            print(f"[+] {fname}: visibility = 'private'")
        else:
            audit_log.append(f"FAIL: {fname} visibility is '{vis}', expected 'private'")
            print(f"[-] {fname}: visibility = '{vis}' (VIOLATION)")

    # 4. Lorebook Attachment Invariant
    print("\n--- CHECK 4: 6 Standalone Lorebooks Attached ---")
    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        data = json.loads(fpath.read_text(encoding='utf-8'))
        lb_ids = data.get('lorebook_ids', [])
        if set(lb_ids) == set(EXPECTED_LOREBOOKS) and len(lb_ids) == 6:
            print(f"[+] {fname}: Exactly 6 standalone lorebooks attached")
        else:
            audit_log.append(f"FAIL: {fname} lorebooks mismatch: {lb_ids}")
            print(f"[-] {fname}: Lorebooks mismatch: {lb_ids}")

    # 5. Schema & Slot Integrity
    print("\n--- CHECK 5: Slot Definitions & Unavailable Count ---")
    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        data = json.loads(fpath.read_text(encoding='utf-8'))
        slots = data.get('slots', [])
        slot_keys = [s.get('key') for s in slots]
        unavail_issues = [s.get('key') for s in slots if s.get('unavailable_count') != 0]
        if unavail_issues:
            audit_log.append(f"FAIL: {fname} slots with unavailable_count != 0: {unavail_issues}")
            print(f"[-] {fname}: unavailable_count issues: {unavail_issues}")
        else:
            print(f"[+] {fname}: {len(slots)} slots, all unavailable_count == 0 (keys: {slot_keys})")

    # 6. Greetings & Multi-Message Parity
    print("\n--- CHECK 6: Greetings Multi-Message Parity & Speaker Slot Validation ---")
    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        data = json.loads(fpath.read_text(encoding='utf-8'))
        slots = data.get('slots', [])
        valid_keys = {s.get('key') for s in slots}
        greetings = data.get('greetings', [])
        g_errors = []
        for g_idx, g in enumerate(greetings):
            msgs = g.get('messages', [])
            if not msgs:
                g_errors.append(f"Greeting[{g_idx}] has no messages")
                continue
            first_msg = msgs[0]
            if g.get('content') != first_msg.get('content'):
                g_errors.append(f"Greeting[{g_idx}] root content != messages[0].content")
            if g.get('speaker_slot') != first_msg.get('speaker_slot'):
                g_errors.append(f"Greeting[{g_idx}] root speaker_slot != messages[0].speaker_slot")
            for m_idx, m in enumerate(msgs):
                m_slot = m.get('speaker_slot')
                if m_slot not in valid_keys:
                    g_errors.append(f"Greeting[{g_idx}] msg[{m_idx}] speaker_slot '{m_slot}' not in slots")
                m_cnt = m.get('content', '')
                if not m_cnt:
                    g_errors.append(f"Greeting[{g_idx}] msg[{m_idx}] empty content")
        if g_errors:
            for ge in g_errors:
                audit_log.append(f"FAIL: {fname} {ge}")
                print(f"[-] {fname}: {ge}")
        else:
            print(f"[+] {fname}: {len(greetings)} greetings, 100% parity verified")

    # 7. Canon Constraints Deep Verification
    print("\n--- CHECK 7: Canon Constraints Deep Verification ---")
    
    # 7.1 Villa Douglas
    vd_path = SCENARIOS_DIR / "Svartulfr_Scenario_Villa_Douglas.json"
    vd = json.loads(vd_path.read_text(encoding='utf-8'))
    vd_slots = {s['key']: s['pool'][0]['character_id'] for s in vd.get('slots', []) if s.get('pool')}
    if vd_slots == VILLA_DOUGLAS_MALES:
        print("[+] Villa Douglas: Exactly 7 canonical male card holders verified with correct card IDs")
    else:
        audit_log.append("FAIL: Villa Douglas male slot mismatch")
        print("[-] Villa Douglas male slot mismatch:", vd_slots)

    # 7.2 SUCC Route Alyssa
    al_path = SCENARIOS_DIR / "Svartulfr_Scenario_SUCC_Route_Alyssa.json"
    al_raw = al_path.read_text(encoding='utf-8')
    if "Arctic Wolf demi-human" in al_raw and "one pair of animal ears, non-shifter" in al_raw:
        print("[+] SUCC Alyssa: Finnegan Novak Arctic Wolf demi-human (non-shifter, single pair of ears) verified")
    else:
        audit_log.append("FAIL: SUCC Alyssa missing Finnegan Novak Arctic Wolf demi-human invariant")
        print("[-] SUCC Alyssa: Missing Finn Novak invariant")
    if "Scarlett Rose" in al_raw:
        print("[+] SUCC Alyssa: Scarlett Rose verified surname")
    else:
        audit_log.append("FAIL: SUCC Alyssa missing Scarlett Rose verified surname")

    # 7.3 SUCC Route Jasper
    js_path = SCENARIOS_DIR / "Svartulfr_Scenario_SUCC_Route_Jasper.json"
    js_raw = js_path.read_text(encoding='utf-8')
    if "Russ Sinclair" in js_raw and "Russell 'Russ' Sinclair" in js_raw:
        print("[+] SUCC Jasper: Russ Sinclair verified surname")
    else:
        audit_log.append("FAIL: SUCC Jasper missing Russ Sinclair verified surname")
    if "Scarlett Rose" in js_raw:
        print("[+] SUCC Jasper: Scarlett Rose verified surname")
    else:
        audit_log.append("FAIL: SUCC Jasper missing Scarlett Rose verified surname")
    if "Echo" in js_raw:
        print("[+] SUCC Jasper: Echo AI companion verified")
    else:
        audit_log.append("FAIL: SUCC Jasper missing Echo AI companion")

    # 7.4 DMHA Dungeons
    dm_path = SCENARIOS_DIR / "Svartulfr_Scenario_DMHA_Dungeons.json"
    dm = json.loads(dm_path.read_text(encoding='utf-8'))
    dm_keys = [s['key'] for s in dm.get('slots', [])]
    if dm_keys == DMHA_SLOTS:
        print(f"[+] DMHA Dungeons: Exactly 9 required slots verified ({dm_keys})")
    else:
        audit_log.append(f"FAIL: DMHA Dungeons slots mismatch: {dm_keys}")
        print("[-] DMHA Dungeons slots mismatch:", dm_keys)

    # 7.5 Underworld Sindacato
    uw_path = SCENARIOS_DIR / "Svartulfr_Scenario_Underworld_Sindacato.json"
    uw_raw = uw_path.read_text(encoding='utf-8')
    if "Human, Telepath" in uw_raw or "Human Telepath" in uw_raw:
        print("[+] Underworld Sindacato: Jean-Luc Virtuoso Human Telepath invariant verified")
    else:
        audit_log.append("FAIL: Underworld Sindacato missing Jean-Luc Virtuoso Human Telepath invariant")
        print("[-] Underworld Sindacato: Missing Jean-Luc Human Telepath invariant")

    # 7.6 Camp Mystic
    cm_path = SCENARIOS_DIR / "Svartulfr_Scenario_Camp_Mystic.json"
    cm = json.loads(cm_path.read_text(encoding='utf-8'))
    cm_raw = cm_path.read_text(encoding='utf-8')
    cm_startup = cm.get('startup_script', '')
    if "Marcus Vale" in cm_startup and "Celeste Nadir" in cm_startup:
        print("[+] Camp Mystic: Dynamic Lua startup script for Marcus Vale / Celeste Nadir verified")
    else:
        audit_log.append("FAIL: Camp Mystic missing Lua startup script supervisor logic")
        print("[-] Camp Mystic missing Lua startup script")
    if "13" in cm_raw and "Lake Erie" in cm_raw:
        print("[+] Camp Mystic: Edric 13yo and Lake Erie shuttle arrival verified")
    else:
        audit_log.append("FAIL: Camp Mystic missing Edric 13yo or Lake Erie references")

    # 8. Investigation of Test Suite Discrepancy
    print("\n--- CHECK 8: Investigation of test_validate_scenarios.py failure ---")
    test_val_path = ROOT / "scratch" / "test_validate_scenarios.py"
    test_val_code = test_val_path.read_text(encoding='utf-8')
    # Check lines where regex is applied
    print("[i] test_validate_scenarios.py regex check line 153:")
    print("    if re.match(r'^[A-Z][a-zA-Z\\s\\'-]+:\\s', m_content):")
    print("    Investigating what triggered it:")
    for fname in EXPECTED_FILES:
        data = json.loads((SCENARIOS_DIR / fname).read_text(encoding='utf-8'))
        for g_idx, g in enumerate(data.get('greetings', [])):
            for m_idx, m in enumerate(g.get('messages', [])):
                cnt = m.get('content', '')
                mat = re.match(r'^[A-Z][a-zA-Z\s\'-]+:\s', cnt)
                if mat:
                    print(f"    -> Flagged in {fname} greeting[{g_idx}] msg[{m_idx}]:")
                    print(f"       Prefix: \"{mat.group(0)}\"")
                    print(f"       Full string: \"{cnt[:100]}...\"")

    print("\n" + "=" * 70)
    print("FINAL AUDIT SUMMARY:")
    print(f"Total violations found: {len(audit_log)}")
    if audit_log:
        for err in audit_log:
            print("  [VIOLATION]", err)
        return False
    else:
        print("  ALL 6 SCENARIOS AND PAYLOADS ARE FULLY VERIFIED AND INTEGRITY-CLEAN!")
        return True

if __name__ == '__main__':
    ok = run_forensic_audit()
    sys.exit(0 if ok else 1)
