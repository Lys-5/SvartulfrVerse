"""
Independent Victory Audit Script for Svartúlfr Lorebooks Project
Authored by Victory Auditor (independent agent)
"""
import os
import sys
import json
import hashlib
import re
import urllib.request
import urllib.error

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
LOREBOOKS = [
    {
        "id": "_gwwCxCfQ6PQaLEjAQVpJL",
        "title": "Svartúlfr - Lorebook I",
        "file": "Svartulfr_Lorebook_I.json",
        "expected_count": 219,
        "is_npc": False
    },
    {
        "id": "_HfG7TeV6MJyj6bxMwxkpt",
        "title": "Svartúlfr - Lorebook II",
        "file": "Svartulfr_Lorebook_II.json",
        "expected_count": 143,
        "is_npc": False
    },
    {
        "id": "_9zWTGqYJNJ4BCDMj8gfcD",
        "title": "Svartúlfr - Lorebook III",
        "file": "Svartulfr_Lorebook_III.json",
        "expected_count": 35,
        "is_npc": False
    },
    {
        "id": "_EjXxkmPVhpCXg8xABpFkK",
        "title": "Svartúlfr - Location",
        "file": "Svartulfr_Location.json",
        "expected_count": 196,
        "is_npc": False
    },
    {
        "id": "_zwEqgEEzh12X6gHVmMKKC",
        "title": "Svartúlfr - NPC Primary",
        "file": "Svartulfr_NPC_Primary.json",
        "expected_count": 106,
        "is_npc": True
    },
    {
        "id": "_Uht3Ckz44JBDrPnUHq7LV",
        "title": "Svartúlfr - NPC Secondary",
        "file": "Svartulfr_NPC_Secondary.json",
        "expected_count": 310,
        "is_npc": True
    }
]

CANONICAL_FALLBACK_AVATAR = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"
BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

def file_md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def run_audit():
    results = {}
    failures = []

    print("=" * 60)
    print("PHASE 1: SAFETY BACKUP AUDIT (Milestone R1)")
    print("=" * 60)
    backup_dir = os.path.join(PROJECT_ROOT, "scratch", "backup_pre_audit_lorebooks")
    backup_status = True
    backup_details = []
    if not os.path.isdir(backup_dir):
        backup_status = False
        failures.append("Safety backup directory does not exist: " + backup_dir)
    else:
        for lb in LOREBOOKS:
            b_path = os.path.join(backup_dir, lb["file"])
            if not os.path.isfile(b_path):
                backup_status = False
                failures.append(f"Backup missing file: {lb['file']}")
            else:
                size = os.path.getsize(b_path)
                backup_details.append(f"{lb['file']}: {size} bytes")
    print(f"Safety Backup Result: {'PASS' if backup_status else 'FAIL'}")
    for d in backup_details:
        print("  - " + d)

    print("\n" + "=" * 60)
    print("PHASE 2: PARITY AUDIT (FINAL/ vs lorebooks/optimized/)")
    print("=" * 60)
    parity_status = True
    parity_details = []
    for lb in LOREBOOKS:
        f_path = os.path.join(PROJECT_ROOT, "FINAL", lb["file"])
        o_path = os.path.join(PROJECT_ROOT, "lorebooks", "optimized", lb["file"])
        f_md5 = file_md5(f_path)
        o_md5 = file_md5(o_path)
        if f_md5 != o_md5:
            parity_status = False
            failures.append(f"Hash mismatch between FINAL and optimized for {lb['file']}: {f_md5} != {o_md5}")
        else:
            parity_details.append(f"{lb['file']}: MD5 {f_md5} (MATCH)")
    print(f"Repository Parity Result: {'PASS' if parity_status else 'FAIL'}")
    for d in parity_details:
        print("  - " + d)

    print("\n" + "=" * 60)
    print("PHASE 3: DUAL ARRAY SYNCHRONIZATION (entries == lexicon)")
    print("=" * 60)
    dual_array_status = True
    dual_array_details = []
    total_entries_count = 0
    for lb in LOREBOOKS:
        f_path = os.path.join(PROJECT_ROOT, "FINAL", lb["file"])
        with open(f_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        entries = data.get("entries", [])
        lexicon = data.get("lexicon", [])
        if len(entries) != lb["expected_count"] or len(lexicon) != lb["expected_count"]:
            dual_array_status = False
            failures.append(f"{lb['file']} count mismatch: entries={len(entries)}, lexicon={len(lexicon)}, expected={lb['expected_count']}")
        if entries != lexicon:
            dual_array_status = False
            failures.append(f"{lb['file']} entries and lexicon are not identical!")
        total_entries_count += len(lexicon)
        dual_array_details.append(f"{lb['title']}: {len(entries)} entries == {len(lexicon)} lexicon (Identical: {entries == lexicon})")
    print(f"Dual Array Parity Result: {'PASS' if dual_array_status else 'FAIL'}")
    print(f"Total entries across all 6 lorebooks: {total_entries_count} (Expected: 1009)")
    for d in dual_array_details:
        print("  - " + d)

    print("\n" + "=" * 60)
    print("PHASE 4: PILLAR 1 — NON-NPC SPURIOUS METADATA AUDIT")
    print("=" * 60)
    p1_status = True
    p1_details = []
    spurious_fields_found = []
    empty_avatars_found = []
    decorative_avatars = []
    for lb in LOREBOOKS:
        if lb["is_npc"]:
            continue
        f_path = os.path.join(PROJECT_ROOT, "FINAL", lb["file"])
        with open(f_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for idx, entry in enumerate(data.get("lexicon", [])):
            name = entry.get("name") or entry.get("comment") or f"Entry #{idx}"
            # Check spurious fields
            for field in ["avatar_activation_regex", "custom_avatar_regex", "lines_parsed", "npc_info"]:
                val = entry.get(field)
                if val is not None and val != "" and val is not False:
                    spurious_fields_found.append((lb["file"], name, field, val))
            if "avatar_activation_regex" in entry and entry["avatar_activation_regex"] != "":
                spurious_fields_found.append((lb["file"], name, "avatar_activation_regex", entry["avatar_activation_regex"]))
            # Check empty avatar
            av = entry.get("avatar")
            if av == "":
                empty_avatars_found.append((lb["file"], name))
            elif av and av.startswith("http"):
                decorative_avatars.append((lb["file"], name, av))

    if spurious_fields_found:
        p1_status = False
        failures.append(f"Spurious metadata fields found on non-NPC entries: {len(spurious_fields_found)} items: {spurious_fields_found[:5]}")
    if empty_avatars_found:
        p1_status = False
        failures.append(f"Empty avatar strings found on non-NPC entries: {len(empty_avatars_found)} items: {empty_avatars_found[:5]}")

    print(f"Pillar 1 Result: {'PASS' if p1_status else 'FAIL'}")
    print(f"  - Spurious fields found on non-NPC entries: {len(spurious_fields_found)}")
    print(f"  - Empty avatar strings found: {len(empty_avatars_found)}")
    print(f"  - Legitimate decorative avatars preserved: {len(decorative_avatars)}")
    for file_name in ["Svartulfr_Lorebook_II.json", "Svartulfr_Location.json"]:
        count = sum(1 for d in decorative_avatars if d[0] == file_name)
        print(f"    * {file_name}: {count} decorative avatars")

    print("\n" + "=" * 60)
    print("PHASE 5: PILLAR 2 — NPC UMBRELLA KEYWORDS (BROAD_KEYS) AUDIT")
    print("=" * 60)
    p2_status = True
    umbrella_keys_found = []
    npc_key_stats = []
    selective_inconsistencies = []
    for lb in LOREBOOKS:
        if not lb["is_npc"]:
            continue
        f_path = os.path.join(PROJECT_ROOT, "FINAL", lb["file"])
        with open(f_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for idx, entry in enumerate(data.get("lexicon", [])):
            name = entry.get("name") or f"NPC #{idx}"
            keys = entry.get("keys", [])
            sec_keys = entry.get("secondary_keys", [])
            selective = entry.get("selective", False)

            # Check selective rule: selective: false unless secondary_keys is populated
            if selective and not sec_keys:
                selective_inconsistencies.append((lb["file"], name, "selective is True but secondary_keys is empty"))

            # Check umbrella keywords on trigger keys
            for k in keys:
                k_clean = k.strip().lower()
                if k_clean in BROAD_KEYS:
                    umbrella_keys_found.append((lb["file"], name, k))
            # Also check if banned multi-word triggers remain
            banned_triggers = {"pack leader", "blackwood council", "demon representative", "human representative", "alligator demihuman", "succ student"}
            for k in keys:
                if k.strip().lower() in banned_triggers:
                    umbrella_keys_found.append((lb["file"], name, k))
            # Malachia secondary_keys standalone "Alpha" check
            if "malachia" in name.lower():
                for sk in sec_keys:
                    if sk.strip().lower() == "alpha":
                        umbrella_keys_found.append((lb["file"], name, f"secondary_key: {sk}"))

            npc_key_stats.append((name, len(keys)))

    if umbrella_keys_found:
        p2_status = False
        failures.append(f"Umbrella keywords found on NPCs: {umbrella_keys_found}")
    if selective_inconsistencies:
        p2_status = False
        failures.append(f"Selective inconsistencies found on NPCs: {selective_inconsistencies}")

    print(f"Pillar 2 Result: {'PASS' if p2_status else 'FAIL'}")
    print(f"  - Umbrella keywords on NPC trigger keys: {len(umbrella_keys_found)}")
    print(f"  - Selective inconsistencies: {len(selective_inconsistencies)}")
    min_keys = min(s[1] for s in npc_key_stats) if npc_key_stats else 0
    max_keys = max(s[1] for s in npc_key_stats) if npc_key_stats else 0
    print(f"  - Total NPCs checked: {len(npc_key_stats)} (Keys range: {min_keys} to {max_keys} keys per NPC)")

    print("\n" + "=" * 60)
    print("PHASE 6: PILLAR 3 — RESIDUAL {{age}} MACROS AUDIT")
    print("=" * 60)
    p3_status = True
    age_macro_occurrences = []
    for lb in LOREBOOKS:
        f_path = os.path.join(PROJECT_ROOT, "FINAL", lb["file"])
        with open(f_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        matches = re.findall(r"\{\{age\}\}", raw_text, re.IGNORECASE)
        if matches:
            p3_status = False
            age_macro_occurrences.append((lb["file"], len(matches)))
            failures.append(f"{lb['file']} contains {len(matches)} occurrences of {{{{age}}}}")
    print(f"Pillar 3 Result: {'PASS' if p3_status else 'FAIL'}")
    print(f"  - Total {{{{age}}}} macros across all 6 lorebooks: {len(age_macro_occurrences)}")

    print("\n" + "=" * 60)
    print("PHASE 7: PILLAR 4 — NPC AVATARS & REGEX SPLITTING AUDIT")
    print("=" * 60)
    p4_status = True
    invalid_avatars = []
    invalid_custom_avatar_regex = []
    invalid_lines_parsed = []
    invalid_regex_patterns = []
    avatar_types = {"custom": 0, "fallback": 0}
    for lb in LOREBOOKS:
        if not lb["is_npc"]:
            continue
        f_path = os.path.join(PROJECT_ROOT, "FINAL", lb["file"])
        with open(f_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for idx, entry in enumerate(data.get("lexicon", [])):
            name = entry.get("name") or f"NPC #{idx}"
            av = entry.get("avatar")
            if not av or not (av.startswith("http://") or av.startswith("https://")):
                invalid_avatars.append((lb["file"], name, av))
            else:
                if av == CANONICAL_FALLBACK_AVATAR:
                    avatar_types["fallback"] += 1
                else:
                    avatar_types["custom"] += 1

            if entry.get("custom_avatar_regex") is not True:
                invalid_custom_avatar_regex.append((lb["file"], name, entry.get("custom_avatar_regex")))

            if entry.get("lines_parsed") != 1:
                invalid_lines_parsed.append((lb["file"], name, entry.get("lines_parsed")))

            reg = entry.get("avatar_activation_regex", "")
            if not reg or not re.match(r'^\(\?:\^\|\\n\)\\s\*\(\?:.+\)\\s\*:$', reg):
                invalid_regex_patterns.append((lb["file"], name, reg))

    if invalid_avatars or invalid_custom_avatar_regex or invalid_lines_parsed or invalid_regex_patterns:
        p4_status = False
        failures.append(f"Pillar 4 failures: invalid_avatars={len(invalid_avatars)}, custom_regex={len(invalid_custom_avatar_regex)}, lines_parsed={len(invalid_lines_parsed)}, regex_patterns={len(invalid_regex_patterns)}")

    print(f"Pillar 4 Result: {'PASS' if p4_status else 'FAIL'}")
    print(f"  - Total NPCs verified: {avatar_types['custom'] + avatar_types['fallback']} (Expected 416)")
    print(f"    * Existing custom avatars: {avatar_types['custom']}")
    print(f"    * Canonical Crest fallback avatars: {avatar_types['fallback']}")
    print(f"  - Custom avatar regex flag valid (100% True): {len(invalid_custom_avatar_regex) == 0}")
    print(f"  - Lines parsed flag valid (100% 1): {len(invalid_lines_parsed) == 0}")
    print(f"  - Multiline regex pattern valid (100% match): {len(invalid_regex_patterns) == 0}")

    print("\n" + "=" * 60)
    print("PHASE 8: MISSING NPC AVATARS LOG VERIFICATION (scratch/missing_npc_avatars.json)")
    print("=" * 60)
    missing_json_path = os.path.join(PROJECT_ROOT, "scratch", "missing_npc_avatars.json")
    missing_status = True
    if not os.path.isfile(missing_json_path):
        missing_status = False
        failures.append("Missing missing_npc_avatars.json file!")
    else:
        with open(missing_json_path, 'r', encoding='utf-8') as f:
            m_data = json.load(f)
        tot = m_data.get("total_remediated")
        sum_p = m_data.get("summary", {}).get("Svartulfr_NPC_Primary")
        sum_s = m_data.get("summary", {}).get("Svartulfr_NPC_Secondary")
        entries_list = m_data.get("entries", [])
        if tot != 302 or sum_p != 44 or sum_s != 258 or len(entries_list) != 302:
            missing_status = False
            failures.append(f"missing_npc_avatars.json count mismatch: total={tot}, P={sum_p}, S={sum_s}, list_len={len(entries_list)}")
        print(f"missing_npc_avatars.json Result: {'PASS' if missing_status else 'FAIL'}")
        print(f"  - Total remediated logged: {tot} (Primary: {sum_p}, Secondary: {sum_s})")
        print(f"  - Matches fallback avatars counted in Pillar 4: {avatar_types['fallback'] == tot}")

    print("\n" + "=" * 60)
    print("PHASE 9: LIVE WYVERN WEB API CLOUD AUDIT")
    print("=" * 60)
    token_path = os.path.join(PROJECT_ROOT, "scratch", "wyvern_token.txt")
    token = ""
    if os.path.isfile(token_path):
        with open(token_path, 'r', encoding='utf-8') as f:
            token = f.read().strip()
    
    api_status = True
    api_results = []
    if not token:
        api_status = False
        failures.append("Wyvern token not found in scratch/wyvern_token.txt")
    else:
        headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": "VictoryAuditor/1.0"
        }
        cloud_total_entries = 0
        for lb in LOREBOOKS:
            url = f"https://app.wyvern.chat/api/lorebooks/{lb['id']}"
            req = urllib.request.Request(url, headers=headers, method="GET")
            try:
                with urllib.request.urlopen(req, timeout=15) as resp:
                    code = resp.status
                    body = json.loads(resp.read().decode('utf-8'))
                    cloud_lex = len(body.get("lexicon", []))
                    cloud_ent = len(body.get("entries", []))
                    cloud_count = max(cloud_lex, cloud_ent)
                    cloud_total_entries += cloud_count
                    if code != 200:
                        api_status = False
                        failures.append(f"API {lb['title']} returned status {code}")
                    if cloud_count != lb["expected_count"]:
                        api_status = False
                        failures.append(f"API {lb['title']} returned {cloud_count} entries, expected {lb['expected_count']}")
                    api_results.append(f"{lb['title']} ({lb['id']}): HTTP {code} OK | cloud entries: {cloud_count} (expected {lb['expected_count']})")
            except Exception as e:
                api_status = False
                failures.append(f"API call to {lb['title']} failed: {e}")
                api_results.append(f"{lb['title']}: FAILED ({e})")

        print(f"Live API Query Result: {'PASS' if api_status else 'FAIL'}")
        print(f"Total live cloud entries verified: {cloud_total_entries} / 1009")
        for res in api_results:
            print("  - " + res)

    print("\n" + "=" * 60)
    print("PHASE 10: CHANGELOG.MD VERIFICATION")
    print("=" * 60)
    cl_path = os.path.join(PROJECT_ROOT, "CHANGELOG.md")
    cl_status = True
    with open(cl_path, 'r', encoding='utf-8') as f:
        cl_text = f.read()

    expected_strings = [
        "Audit a 4 Pilastri, Bonifica Strutturale e Deploy Live Wyvern API",
        "scratch/backup_pre_audit_lorebooks/",
        "558",
        "1.009",
        "302",
        "44 in NPC Primary",
        "258 in NPC Secondary",
        "219",
        "143",
        "35",
        "196",
        "106",
        "310"
    ]
    missing_strings = [s for s in expected_strings if s not in cl_text]
    if missing_strings:
        cl_status = False
        failures.append(f"CHANGELOG.md is missing expected strings: {missing_strings}")
    print(f"CHANGELOG.md Audit Result: {'PASS' if cl_status else 'FAIL'}")
    if missing_strings:
        print(f"  - Missing strings: {missing_strings}")
    else:
        print("  - All expected metrics and remediation breakdown strings verified in CHANGELOG.md")

    print("\n" + "=" * 60)
    print("OVERALL VICTORY AUDIT SUMMARY")
    print("=" * 60)
    all_passed = (
        backup_status and
        parity_status and
        dual_array_status and
        p1_status and
        p2_status and
        p3_status and
        p4_status and
        missing_status and
        api_status and
        cl_status
    )
    print(f"VERDICT: {'VICTORY CONFIRMED' if all_passed else 'VICTORY REJECTED'}")
    if failures:
        print("\nFAILURES DETECTED:")
        for fail in failures:
            print(f"  [X] {fail}")
    else:
        print("\nAll 10 verification phases passed with 100% precision. Zero anomalies detected.")

    return all_passed, failures

if __name__ == "__main__":
    success, fails = run_audit()
    sys.exit(0 if success else 1)
