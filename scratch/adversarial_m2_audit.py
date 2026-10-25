#!/usr/bin/env python3
"""
scratch/adversarial_m2_audit.py
Adversarial data integrity verification script for Milestone 2 (challenger_m2_2).
"""

import json
import hashlib
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

FILES_TO_CHECK = [
    Path("FINAL/Svartulfr_NPC_Primary.json"),
    Path("FINAL/Svartulfr_NPC_Secondary.json"),
    Path("lorebooks/optimized/Svartulfr_NPC_Primary.json"),
    Path("lorebooks/optimized/Svartulfr_NPC_Secondary.json"),
]

BROAD_KEYS = {
    "solarton",
    "succ",
    "blackwood",
    "losangeles",
    "underworld",
    "vampire",
    "werewolf",
    "human",
    "demihuman",
    "demi-human",
    "demon",
    "college",
    "student",
    "alpha",
    "beta",
    "omega",
    "pack",
}

KNOWN_DUPE_SURNAMES = [
    "Rivers Rivers", "Rogers Rogers", "Boone Boone", "Black Black",
    "O'Connor O'Connor", "Virtuoso Virtuoso", "Cirillo Cirillo",
    "Bishop Bishop", "Thompson Thompson", "DeVille DeVille"
]

def normalize_regex(pattern_str: str) -> str:
    if not pattern_str:
        return ""
    norm = re.sub(r'\\+\s+', ' ', pattern_str)
    norm = re.sub(r'\\+s[+*]?', ' ', norm)
    norm = re.sub(r"\[['‘’ʼ‛′]+\]", "'", norm)
    norm = re.sub(r"\[[-‐‑‒–—−]+\]", "-", norm)
    norm = re.sub(r"\\+([.'\"\-_&()])", r"\1", norm)
    norm = re.sub(r'\s+', ' ', norm)
    return norm.strip()

def check_file_sha(p1: Path, p2: Path):
    h1 = hashlib.sha256(p1.read_bytes()).hexdigest()
    h2 = hashlib.sha256(p2.read_bytes()).hexdigest()
    return h1, h2, h1 == h2

def run_adversarial_audit():
    print("=" * 80)
    print("STARTING ADVERSARIAL AUDIT FOR MILESTONE 2 (challenger_m2_2)")
    print("=" * 80)

    total_failures = 0

    # 1. Check Mirroring Between FINAL and lorebooks/optimized
    print("\n--- 1. FILE MIRRORING INTEGRITY ---")
    pairs = [
        (Path("FINAL/Svartulfr_NPC_Primary.json"), Path("lorebooks/optimized/Svartulfr_NPC_Primary.json")),
        (Path("FINAL/Svartulfr_NPC_Secondary.json"), Path("lorebooks/optimized/Svartulfr_NPC_Secondary.json"))
    ]
    for p1, p2 in pairs:
        h1, h2, match = check_file_sha(p1, p2)
        status = "MATCH" if match else "MISMATCH"
        print(f"[{status}] {p1.name}:")
        print(f"  {p1}: {h1}")
        print(f"  {p2}: {h2}")
        if not match:
            total_failures += 1

    # 2. File-by-File Detailed Invariant Verification
    all_npc_keys = set()
    total_entries_scanned = 0

    for fpath in FILES_TO_CHECK:
        print(f"\n--- AUDITING: {fpath} ---")
        if not fpath.exists():
            print(f"[ERROR] File does not exist: {fpath}")
            total_failures += 1
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        entries = data.get("entries", [])
        lexicon = data.get("lexicon", [])
        expected_count = 99 if "Primary" in fpath.name else 211

        print(f"Entry counts: entries={len(entries)}, lexicon={len(lexicon)} (Expected: {expected_count})")
        if len(entries) != expected_count:
            print(f"[FAIL] entries length {len(entries)} != {expected_count}")
            total_failures += 1
        if len(lexicon) != expected_count:
            print(f"[FAIL] lexicon length {len(lexicon)} != {expected_count}")
            total_failures += 1

        # Parity check: Python object equality
        if entries != lexicon:
            print(f"[FAIL] entries != lexicon (Python object comparison)")
            total_failures += 1
        else:
            print("[PASS] Python object parity: entries == lexicon")

        # Parity check: exact JSON serialization
        e_dump = json.dumps(entries, sort_keys=True)
        l_dump = json.dumps(lexicon, sort_keys=True)
        if e_dump != l_dump:
            print(f"[FAIL] Serialization parity mismatch! Lengths: {len(e_dump)} vs {len(l_dump)}")
            total_failures += 1
        else:
            print(f"[PASS] Byte-for-byte serialization parity: 100% match ({len(e_dump)} bytes)")

        # Root level toggles and gallery
        root_highlight = data.get("enableEntryHighlighting")
        print(f"Root enableEntryHighlighting: {root_highlight}")
        if root_highlight is not True:
            print(f"[FAIL] Root enableEntryHighlighting is not True: {root_highlight}")
            total_failures += 1
        else:
            print("[PASS] Root enableEntryHighlighting is True")

        gallery = data.get("gallery")
        gallery_count = data.get("gallery_count")
        if not isinstance(gallery, list) or gallery_count != len(gallery):
            print(f"[FAIL] Gallery root invalid: gallery={type(gallery)}, gallery_count={gallery_count}")
            total_failures += 1
        else:
            print(f"[PASS] Root gallery valid (count={gallery_count})")

        # Inspect every entry in entries
        file_toggle_failures = 0
        file_broad_key_failures = 0
        file_dupe_surname_failures = 0
        file_npc_info_failures = 0
        file_avatar_failures = 0
        file_collision_failures = 0

        for idx, entry in enumerate(entries):
            total_entries_scanned += 1
            name = entry.get("name", f"Index {idx}")

            # Check 3 Toggles
            sp = entry.get("scan_persona")
            wwo = entry.get("whole_words_only")
            hk = entry.get("highlight_keys")
            eh = entry.get("enable_highlighting")

            if sp is not True:
                print(f"[FAIL][Toggle] Entry '{name}' (idx {idx}) scan_persona={sp} (expected True)")
                file_toggle_failures += 1
            if wwo is not True:
                print(f"[FAIL][Toggle] Entry '{name}' (idx {idx}) whole_words_only={wwo} (expected True)")
                file_toggle_failures += 1
            if hk is not True:
                print(f"[FAIL][Toggle] Entry '{name}' (idx {idx}) highlight_keys={hk} (expected True)")
                file_toggle_failures += 1
            if eh is not True:
                print(f"[FAIL][Toggle] Entry '{name}' (idx {idx}) enable_highlighting={eh} (expected True)")
                file_toggle_failures += 1

            # Check Duplicate Surnames in Regex
            av_regex = entry.get("avatar_activation_regex", "")
            norm_regex = normalize_regex(av_regex)
            
            # Check known duplicates
            for kd in KNOWN_DUPE_SURNAMES:
                if kd.lower() in norm_regex.lower():
                    print(f"[FAIL][DupeSurname] Entry '{name}' matched known dupe '{kd}' in regex: {norm_regex[:100]}...")
                    file_dupe_surname_failures += 1

            # Check adjacent duplicate words
            adjacent_matches = list(re.finditer(r"\b([A-Za-z]+(?:['\-][A-Za-z]+)*)\s+\1\b", norm_regex, flags=re.IGNORECASE))
            for m in adjacent_matches:
                matched_word = m.group(1)
                # Ignore trivial single/two letter noise if any, but any surname/word >= 3 chars is a bug
                if len(matched_word) >= 3:
                    print(f"[FAIL][DupeSurname] Entry '{name}' adjacent duplicate '{matched_word} {matched_word}' in regex: {norm_regex[:100]}...")
                    file_dupe_surname_failures += 1

            # Check if last_name is doubled
            npc_info = entry.get("npc_info", {})
            if isinstance(npc_info, dict):
                last_name = npc_info.get("last_name")
                if last_name and isinstance(last_name, str) and last_name.strip():
                    double_ln = f"{last_name.strip()} {last_name.strip()}"
                    if double_ln.lower() in norm_regex.lower():
                        print(f"[FAIL][DupeSurname] Entry '{name}' last_name doubled '{double_ln}' in regex")
                        file_dupe_surname_failures += 1

            # Check BROAD_KEYS in keys, secondary_keys, nicknames
            entry_keys = entry.get("keys", [])
            sec_keys = entry.get("secondary_keys", [])
            nicks = entry.get("nicknames", [])
            info_nicks = npc_info.get("nicknames", []) if isinstance(npc_info, dict) else []

            all_checked_keys = [("keys", k) for k in entry_keys] + \
                               [("secondary_keys", k) for k in sec_keys] + \
                               [("nicknames", k) for k in nicks] + \
                               [("npc_info.nicknames", k) for k in info_nicks]

            for field_name, k in all_checked_keys:
                if not isinstance(k, str):
                    print(f"[FAIL][BroadKey] Entry '{name}' {field_name} element is not a string: {k}")
                    file_broad_key_failures += 1
                    continue
                k_norm = k.strip().lower()
                if k_norm in BROAD_KEYS:
                    print(f"[FAIL][BroadKey] Entry '{name}' has prohibited umbrella keyword '{k_norm}' in {field_name}")
                    file_broad_key_failures += 1

            # Check npc_info schema
            if not isinstance(npc_info, dict):
                print(f"[FAIL][npc_info] Entry '{name}' npc_info is not dict")
                file_npc_info_failures += 1
            else:
                fn = npc_info.get("first_name")
                if not fn or not isinstance(fn, str) or not fn.strip():
                    print(f"[FAIL][npc_info] Entry '{name}' invalid first_name: {fn}")
                    file_npc_info_failures += 1
                mn = npc_info.get("middle_names")
                if not isinstance(mn, list) or not all(isinstance(x, str) for x in mn):
                    print(f"[FAIL][npc_info] Entry '{name}' invalid middle_names: {mn}")
                    file_npc_info_failures += 1
                ln = npc_info.get("last_name")
                if ln is not None and not isinstance(ln, str):
                    print(f"[FAIL][npc_info] Entry '{name}' invalid last_name: {ln}")
                    file_npc_info_failures += 1
                nn = npc_info.get("nicknames")
                if not isinstance(nn, list) or not all(isinstance(x, str) for x in nn):
                    print(f"[FAIL][npc_info] Entry '{name}' invalid nicknames: {nn}")
                    file_npc_info_failures += 1
                ti = npc_info.get("titles")
                if not isinstance(ti, list) or not all(isinstance(x, str) for x in ti):
                    print(f"[FAIL][npc_info] Entry '{name}' invalid titles: {ti}")
                    file_npc_info_failures += 1

            # Check avatar URL
            avatar = entry.get("avatar")
            if not avatar or not isinstance(avatar, str) or not avatar.startswith("https://") or "://" not in avatar:
                print(f"[FAIL][Avatar] Entry '{name}' invalid avatar: {avatar}")
                file_avatar_failures += 1
            else:
                parsed = urlparse(avatar)
                if parsed.scheme != "https" or not parsed.netloc or "." not in parsed.netloc:
                    print(f"[FAIL][Avatar] Entry '{name}' malformed avatar URL: {avatar}")
                    file_avatar_failures += 1

            # Check anti-collision
            selective = entry.get("selective", False)
            if selective and len(sec_keys) == 0:
                print(f"[FAIL][AntiCollision] Entry '{name}' has selective: true but empty secondary_keys")
                file_collision_failures += 1
            ic = entry.get("ignored_characters")
            if ic is not None and (not isinstance(ic, list) or not all(isinstance(x, str) for x in ic)):
                print(f"[FAIL][AntiCollision] Entry '{name}' invalid ignored_characters: {ic}")
                file_collision_failures += 1
            ip = entry.get("ignored_personas")
            if ip is not None and (not isinstance(ip, list) or not all(isinstance(x, str) for x in ip)):
                print(f"[FAIL][AntiCollision] Entry '{name}' invalid ignored_personas: {ip}")
                file_collision_failures += 1

        print(f"Summary for {fpath.name}:")
        print(f"  Toggle failures: {file_toggle_failures}")
        print(f"  Duplicate surname failures: {file_dupe_surname_failures}")
        print(f"  Broad umbrella key failures: {file_broad_key_failures}")
        print(f"  npc_info schema failures: {file_npc_info_failures}")
        print(f"  Avatar failures: {file_avatar_failures}")
        print(f"  Anti-collision failures: {file_collision_failures}")

        total_failures += (file_toggle_failures + file_dupe_surname_failures +
                           file_broad_key_failures + file_npc_info_failures +
                           file_avatar_failures + file_collision_failures)

    print("\n" + "=" * 80)
    print(f"AUDIT COMPLETE. Total failures detected: {total_failures}")
    print("=" * 80)
    return total_failures

if __name__ == "__main__":
    failures = run_adversarial_audit()
    sys.exit(failures)
