import json
import re
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from scripts.verify_npc_schema_contract import (
    validate_avatar_gallery_contract,
    validate_anti_collision_contract,
    validate_entries_lexicon_parity
)

def normalize_pattern(pattern_str: str) -> str:
    norm = re.sub(r'\\+\s+', ' ', pattern_str)
    norm = re.sub(r'\\+s[+*]?', ' ', norm)
    norm = re.sub(r"\[['‘’ʼ‛′]+\]", "'", norm)
    norm = re.sub(r"\[[-‐‑‒–—−]+\]", "-", norm)
    norm = re.sub(r"\\+([.'\"\-_&()])", r"\1", norm)
    norm = re.sub(r'\s+', ' ', norm)
    return norm

def detect_duplicate_surnames_fixed(pattern_str: str, last_name: str = None):
    defects = []
    norm = normalize_pattern(pattern_str)

    known_dupes = [
        "Rivers Rivers", "Rogers Rogers", "Boone Boone", "Black Black",
        "O'Connor O'Connor", "Virtuoso Virtuoso", "Cirillo Cirillo",
        "Bishop Bishop", "Thompson Thompson", "DeVille DeVille"
    ]
    for kd in known_dupes:
        if kd.lower() in norm.lower() and not any(kd.lower() == d.lower() for d in defects):
            defects.append(kd)

    if last_name and last_name.strip():
        ln = last_name.strip()
        double_ln = f"{ln} {ln}"
        if double_ln.lower() in norm.lower() and not any(double_ln.lower() == d.lower() for d in defects):
            defects.append(double_ln)

    generic_matches = re.finditer(r"\b([A-Za-z]+(?:['\-][A-Za-z]+)*)\s+\1\b", norm, flags=re.IGNORECASE)
    for gm in generic_matches:
        word = gm.group(1)
        if len(word) >= 3:
            dupe_str = f"{word} {word}"
            if not any(dupe_str.lower() == d.lower() for d in defects):
                defects.append(dupe_str)

    return defects

def validate_npc_info_schema_fixed(npc_info):
    errors = []
    if not isinstance(npc_info, dict):
        return False, ["npc_info must be a dictionary"]

    # first_name
    fn = npc_info.get("first_name")
    if fn is None:
        errors.append("first_name is required and cannot be null/missing")
    elif not isinstance(fn, str):
        errors.append(f"first_name must be a string, got {type(fn).__name__}")
    elif not fn.strip():
        errors.append("first_name cannot be empty or whitespace only")

    # middle_names (STRICTLY REQUIRED: must be present in dict, cannot be null, must be a list of strings)
    if "middle_names" not in npc_info:
        errors.append("middle_names is required in npc_info (must be a list of strings)")
    else:
        mn = npc_info["middle_names"]
        if mn is None or not isinstance(mn, list):
            errors.append(f"middle_names must be a list of strings, got {type(mn).__name__ if mn is not None else 'null'}")
        else:
            for i, item in enumerate(mn):
                if not isinstance(item, str):
                    errors.append(f"middle_names[{i}] must be a string, got {type(item).__name__}")

    # last_name
    ln = npc_info.get("last_name")
    if ln is not None and not isinstance(ln, str):
        errors.append(f"last_name must be a string or None, got {type(ln).__name__}")

    # nicknames
    nn = npc_info.get("nicknames")
    if nn is not None:
        if not isinstance(nn, list):
            errors.append(f"nicknames must be a list of strings, got {type(nn).__name__}")
        else:
            for i, item in enumerate(nn):
                if not isinstance(item, str):
                    errors.append(f"nicknames[{i}] must be a string, got {type(item).__name__}")

    # titles
    ti = npc_info.get("titles")
    if ti is not None:
        if not isinstance(ti, list):
            errors.append(f"titles must be a list of strings, got {type(ti).__name__}")
        else:
            for i, item in enumerate(ti):
                if not isinstance(item, str):
                    errors.append(f"titles[{i}] must be a string, got {type(item).__name__}")

    # npc_prefix
    np = npc_info.get("npc_prefix")
    if np is not None and not isinstance(np, str):
        errors.append(f"npc_prefix must be a string or None, got {type(np).__name__}")

    return len(errors) == 0, errors

def audit_simulated(path):
    data = json.load(open(path, encoding="utf-8"))
    npc_count = 0
    npc_info_valid = 0
    dupes_found = 0
    dupe_list = []
    for e in data["lexicon"]:
        if e.get("type") == "npc":
            npc_count += 1
            ok, errs = validate_npc_info_schema_fixed(e.get("npc_info"))
            if ok:
                npc_info_valid += 1
            reg = e.get("avatar_activation_regex", "")
            ln = e.get("npc_info", {}).get("last_name") if isinstance(e.get("npc_info"), dict) else None
            d = detect_duplicate_surnames_fixed(reg, ln)
            if d:
                dupes_found += 1
                dupe_list.append((e.get("name"), d))
    print(f"Audit {path.name}:")
    print(f"  NPC Entries Checked: {npc_count}")
    print(f"  Valid npc_info: {npc_info_valid}/{npc_count}")
    print(f"  Legacy Duplicate Surname Defects: {dupes_found}")
    for name, d in dupe_list:
        print(f"    - {name}: {d}")

audit_simulated(repo_root / "FINAL/Svartulfr_NPC_Primary.json")
audit_simulated(repo_root / "FINAL/Svartulfr_NPC_Secondary.json")
