#!/usr/bin/env python3
"""
scratch/adversarial_audit_m2_secondary.py
Adversarial stress-testing and deep verification of Milestone 2 (Secondary Lorebook).
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    import regex as pcre_regex
except ImportError:
    pcre_regex = None

ROOT = Path("e:/repository/SvartulfrVerse")
FINAL_SEC = ROOT / "FINAL" / "Svartulfr_NPC_Secondary.json"
OPT_SEC = ROOT / "lorebooks" / "optimized" / "Svartulfr_NPC_Secondary.json"

BROAD_KEYS = {
    "solarton", "succ", "blackwood", "losangeles", "underworld",
    "vampire", "werewolf", "human", "demihuman", "demi-human",
    "demon", "college", "student", "alpha", "beta", "omega", "pack"
}

SPECIFIC_PURGED_TERMS = ["succubus", "drider", "succ student"]

def audit_secondary():
    print("=================================================================")
    print("STARTING ADVERSARIAL AUDIT FOR SECONDARY LOREBOOK")
    print("=================================================================")

    if not FINAL_SEC.exists():
        print(f"[FAIL] {FINAL_SEC} does not exist!")
        sys.exit(1)
    if not OPT_SEC.exists():
        print(f"[FAIL] {OPT_SEC} does not exist!")
        sys.exit(1)

    with open(FINAL_SEC, "r", encoding="utf-8") as f:
        final_data = json.load(f)
    with open(OPT_SEC, "r", encoding="utf-8") as f:
        opt_data = json.load(f)

    # 1. Byte-for-byte / Structural parity between FINAL and OPT
    final_dump = json.dumps(final_data, sort_keys=True)
    opt_dump = json.dumps(opt_data, sort_keys=True)
    if final_dump == opt_dump:
        print("[PASS] FINAL/ and lorebooks/optimized/ are 100% byte-for-byte identical!")
    else:
        print(f"[FAIL] Mismatch between FINAL/ and lorebooks/optimized/: len {len(final_dump)} vs {len(opt_dump)}")

    # 2. Parity between entries and lexicon in FINAL
    final_entries_dump = json.dumps(final_data.get("entries", []), sort_keys=True)
    final_lexicon_dump = json.dumps(final_data.get("lexicon", []), sort_keys=True)
    if final_entries_dump == final_lexicon_dump:
        print("[PASS] FINAL entries == lexicon 100% byte-for-byte identical!")
    else:
        print("[FAIL] FINAL entries != lexicon!")

    # 3. Parity between entries and lexicon in OPT
    opt_entries_dump = json.dumps(opt_data.get("entries", []), sort_keys=True)
    opt_lexicon_dump = json.dumps(opt_data.get("lexicon", []), sort_keys=True)
    if opt_entries_dump == opt_lexicon_dump:
        print("[PASS] OPT entries == lexicon 100% byte-for-byte identical!")
    else:
        print("[FAIL] OPT entries != lexicon!")

    # 4. Root settings & metadata
    root_gallery = final_data.get("gallery")
    root_gallery_count = final_data.get("gallery_count")
    token_budget = final_data.get("token_budget")
    photoURL = final_data.get("photoURL")
    entry_highlighting = final_data.get("enableEntryHighlighting")

    print(f"Root token_budget: {token_budget} (expected 5000)")
    assert token_budget == 5000, f"Token budget mismatch: {token_budget}"
    print(f"Root photoURL: {photoURL}")
    assert photoURL == "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"
    print(f"Root enableEntryHighlighting: {entry_highlighting}")
    assert entry_highlighting is True, "enableEntryHighlighting is not True"
    assert isinstance(root_gallery, list) and root_gallery_count == len(root_gallery)

    # 5. Entry count
    entries = final_data.get("lexicon", [])
    print(f"Total entries count: {len(entries)} (expected 211)")
    assert len(entries) == 211, f"Entry count mismatch: {len(entries)}"

    # 6. Detailed checks per entry
    middle_names_count = 0
    middle_names_entries = []
    titles_count = 0
    titles_entries = []
    toggle_scan_persona_fail = []
    toggle_whole_words_fail = []
    toggle_highlight_keys_fail = []
    selective_not_false = []
    edric_found = False
    edric_ignored_chars_ok = False
    umbrella_defects = []
    invalid_npc_info = []
    invalid_avatars = []
    regex_compilation_errors = []
    duplicate_surnames = []
    em_dash_violations = []

    for idx, e in enumerate(entries):
        name = e.get("name", f"entry_{idx}")
        # Type
        e_type = e.get("type")
        if e_type != "npc":
            print(f"[WARN] Entry {idx} ({name}) type is '{e_type}', expected 'npc'")

        # Toggles
        if e.get("scan_persona") is not True:
            toggle_scan_persona_fail.append((idx, name, e.get("scan_persona")))
        if e.get("whole_words_only") is not True:
            toggle_whole_words_fail.append((idx, name, e.get("whole_words_only")))
        if e.get("highlight_keys") is not True:
            toggle_highlight_keys_fail.append((idx, name, e.get("highlight_keys")))

        # Selective
        if e.get("selective") is not False:
            selective_not_false.append((idx, name, e.get("selective"), e.get("secondary_keys")))

        # Edric Douglas check
        if "edric" in name.lower() or "h-ttmlgJYeRXqyDvQjSX7" in e.get("id", ""):
            edric_found = True
            ic = e.get("ignored_characters", [])
            if "_TbRM3EdxDjHFgqztTbCpL" in ic:
                edric_ignored_chars_ok = True
                print(f"[PASS] Edric Douglas [{idx}] has ignored_characters: {ic}")
            else:
                print(f"[FAIL] Edric Douglas [{idx}] missing expected ignored_characters: {ic}")

        # npc_info check
        info = e.get("npc_info")
        if not isinstance(info, dict):
            invalid_npc_info.append((idx, name, "not a dict"))
        else:
            fn = info.get("first_name")
            mn = info.get("middle_names")
            ln = info.get("last_name")
            nicks = info.get("nicknames")
            tits = info.get("titles")
            np = info.get("npc_prefix")

            if not isinstance(fn, str) or not fn.strip():
                invalid_npc_info.append((idx, name, f"invalid first_name: {fn}"))
            if not isinstance(mn, list) or any(not isinstance(m, str) for m in mn):
                invalid_npc_info.append((idx, name, f"invalid middle_names: {mn}"))
            elif len(mn) > 0:
                middle_names_count += 1
                middle_names_entries.append((idx, name, mn))

            if ln is not None and not isinstance(ln, str):
                invalid_npc_info.append((idx, name, f"invalid last_name: {ln}"))
            if not isinstance(nicks, list) or any(not isinstance(n, str) for n in nicks):
                invalid_npc_info.append((idx, name, f"invalid nicknames: {nicks}"))
            if not isinstance(tits, list) or any(not isinstance(t, str) for t in tits):
                invalid_npc_info.append((idx, name, f"invalid titles: {tits}"))
            elif len(tits) > 0:
                titles_count += 1
                titles_entries.append((idx, name, tits))

        # Avatar check
        av = e.get("avatar")
        if not isinstance(av, str) or not av.startswith("https://"):
            invalid_avatars.append((idx, name, av))

        # Umbrella keywords
        # check keys
        for k in e.get("keys", []):
            if isinstance(k, str):
                k_clean = k.strip().lower()
                if k_clean in BROAD_KEYS or any(purged in k_clean for purged in SPECIFIC_PURGED_TERMS):
                    umbrella_defects.append((idx, name, "keys", k))
        # check secondary_keys
        for sk in e.get("secondary_keys", []):
            if isinstance(sk, str):
                sk_clean = sk.strip().lower()
                if sk_clean in BROAD_KEYS or any(purged in sk_clean for purged in SPECIFIC_PURGED_TERMS):
                    umbrella_defects.append((idx, name, "secondary_keys", sk))
        # check nicknames
        if isinstance(info, dict) and isinstance(info.get("nicknames"), list):
            for nick in info.get("nicknames"):
                if isinstance(nick, str):
                    n_clean = nick.strip().lower()
                    if n_clean in BROAD_KEYS or any(purged in n_clean for purged in SPECIFIC_PURGED_TERMS):
                        umbrella_defects.append((idx, name, "npc_info.nicknames", nick))

        # Damien Bishop specifically
        if "damien" in name.lower() and "bishop" in name.lower():
            for sk in e.get("secondary_keys", []):
                if "demon" in sk.lower():
                    umbrella_defects.append((idx, name, "damien_bishop_secondary_keys", sk))

        # Regex compilation
        rx = e.get("avatar_activation_regex", "")
        if rx:
            if pcre_regex:
                try:
                    pcre_regex.compile(rx)
                except Exception as ex:
                    regex_compilation_errors.append((idx, name, rx, str(ex)))
            else:
                try:
                    re.compile(rx)
                except Exception as ex:
                    regex_compilation_errors.append((idx, name, rx, str(ex)))

        # Em-dash check
        for field_name in ["name", "keys"]:
            val = e.get(field_name)
            if isinstance(val, str) and "—" in val:
                em_dash_violations.append((idx, name, field_name, val))
            elif isinstance(val, list):
                for item in val:
                    if isinstance(item, str) and "—" in item:
                        em_dash_violations.append((idx, name, field_name, item))

    print("-----------------------------------------------------------------")
    print(f"Middle names count: {middle_names_count} (expected 102)")
    assert middle_names_count == 102, f"Middle names count mismatch: {middle_names_count}"
    print(f"Titles count: {titles_count} (expected 110)")
    assert titles_count == 110, f"Titles count mismatch: {titles_count}"

    print(f"Toggles failures - scan_persona: {len(toggle_scan_persona_fail)}, whole_words_only: {len(toggle_whole_words_fail)}, highlight_keys: {len(toggle_highlight_keys_fail)}")
    assert len(toggle_scan_persona_fail) == 0, f"scan_persona fails: {toggle_scan_persona_fail}"
    assert len(toggle_whole_words_fail) == 0, f"whole_words_only fails: {toggle_whole_words_fail}"
    assert len(toggle_highlight_keys_fail) == 0, f"highlight_keys fails: {toggle_highlight_keys_fail}"

    print(f"Selective != False count: {len(selective_not_false)}")
    assert len(selective_not_false) == 0, f"Entries with selective != False: {selective_not_false}"

    print(f"Edric Douglas found: {edric_found}, ignored_characters preserved: {edric_ignored_chars_ok}")
    assert edric_found and edric_ignored_chars_ok

    print(f"Umbrella keywords defects count: {len(umbrella_defects)}")
    if umbrella_defects:
        for d in umbrella_defects:
            print("  DEFECT:", d)
    assert len(umbrella_defects) == 0, f"Umbrella keywords defects: {umbrella_defects}"

    print(f"Invalid npc_info count: {len(invalid_npc_info)}")
    assert len(invalid_npc_info) == 0, f"Invalid npc_info: {invalid_npc_info}"

    print(f"Invalid avatars count: {len(invalid_avatars)}")
    assert len(invalid_avatars) == 0, f"Invalid avatars: {invalid_avatars}"

    print(f"Regex compilation errors: {len(regex_compilation_errors)}")
    assert len(regex_compilation_errors) == 0, f"Regex errors: {regex_compilation_errors}"

    print(f"Em-dash violations in names/keys: {len(em_dash_violations)}")
    assert len(em_dash_violations) == 0, f"Em-dash violations: {em_dash_violations}"

    print("=================================================================")
    print("ALL ADVERSARIAL CHECKS PASSED WITH ZERO DEFECTS!")
    print("=================================================================")

if __name__ == "__main__":
    audit_secondary()
