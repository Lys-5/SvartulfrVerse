import unittest
import re
from typing import Any, Dict, List, Optional, Tuple

def normalize_wyvern_regex_pattern(pattern_str: str) -> str:
    """
    Normalizes a regex pattern by unescaping escaped whitespace, stripping
    character classes for quotes/hyphens, and unescaping punctuation.
    """
    if not pattern_str:
        return ""
    # 1. Normalize backslash-escaped whitespace (e.g. '\ ' or '\\ ')
    norm = re.sub(r'\\+\s+', ' ', pattern_str)
    # 2. Normalize literal regex whitespace tokens (e.g. '\s+' or '\s*')
    norm = re.sub(r'\\+s[+*]?', ' ', norm)
    # 3. Normalize quote and hyphen character classes to canonical ASCII
    norm = re.sub(r"\[['‘’ʼ‛′]+\]", "'", norm)
    norm = re.sub(r"\[[-‐‑‒–—−]+\]", "-", norm)
    # 4. Unescape escaped punctuation (\., \-, \', \", etc.)
    norm = re.sub(r"\\+([.'\"\-_&()])", r"\1", norm)
    # 5. Collapse consecutive spaces
    norm = re.sub(r'\s+', ' ', norm)
    return norm.strip()

def detect_duplicate_surnames(pattern_str: str, last_name: Optional[str] = None) -> List[str]:
    """
    Detects duplicate surname patterns produced by legacy scripts (e.g. 'Rivers Rivers', 'Rogers Rogers').
    Handles escaped whitespace, character classes, and unescaped strings.
    """
    if not pattern_str:
        return []

    defects = []
    norm = normalize_wyvern_regex_pattern(pattern_str)

    # 1. Known legacy duplicate surname anomalies catalog
    known_dupes = [
        "Rivers Rivers", "Rogers Rogers", "Boone Boone", "Black Black",
        "O'Connor O'Connor", "Virtuoso Virtuoso", "Cirillo Cirillo",
        "Bishop Bishop", "Thompson Thompson", "DeVille DeVille"
    ]
    for kd in known_dupes:
        if kd.lower() in norm.lower() and not any(kd.lower() == d.lower() for d in defects):
            defects.append(kd)

    # 2. Check explicitly provided last_name doubled
    if last_name and last_name.strip():
        ln = last_name.strip()
        double_ln = f"{ln} {ln}"
        if double_ln.lower() in norm.lower() and not any(double_ln.lower() == d.lower() for d in defects):
            defects.append(double_ln)

    # 3. Generic adjacent duplicate word check (supporting hyphens and apostrophes)
    generic_matches = re.finditer(r"\b([A-Za-z]+(?:['\-][A-Za-z]+)*)\s+\1\b", norm, flags=re.IGNORECASE)
    for gm in generic_matches:
        word = gm.group(1)
        if len(word) >= 3:
            dupe_str = f"{word} {word}"
            if not any(dupe_str.lower() == d.lower() for d in defects):
                defects.append(dupe_str)

    return defects

def validate_npc_info_schema(npc_info: Any) -> Tuple[bool, List[str]]:
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

    # middle_names (strictly required: must be present in dict, cannot be null, must be a list of strings)
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


class TestNpcSchemaSuitePreview(unittest.TestCase):
    # Tests for normalizer
    def test_normalize_wyvern_regex_pattern(self):
        self.assertEqual(normalize_wyvern_regex_pattern(r"Alpha\ Rivers\ Rivers"), "Alpha Rivers Rivers")
        self.assertEqual(normalize_wyvern_regex_pattern(r"Mr\.\ Rogers\ Rogers"), "Mr. Rogers Rogers")
        self.assertEqual(normalize_wyvern_regex_pattern(r"O['‘’ʼ‛′]Connor"), "O'Connor")
        self.assertEqual(normalize_wyvern_regex_pattern(r"Jean[-‐‑‒–—−]Luc"), "Jean-Luc")
        self.assertEqual(normalize_wyvern_regex_pattern(r"Hugh\s+Rivers"), "Hugh Rivers")
        self.assertEqual(normalize_wyvern_regex_pattern(""), "")
        self.assertEqual(normalize_wyvern_regex_pattern(None), "")

    # Tests for middle_names
    def test_missing_middle_names_fails(self):
        payload = {"first_name": "Erik", "last_name": "Douglas"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("middle_names is required in npc_info" in e for e in errors))

    def test_middle_names_none_fails(self):
        payload = {"first_name": "Erik", "middle_names": None, "last_name": "Douglas"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("middle_names must be a list of strings, got null" in e for e in errors))

    def test_middle_names_string_fails(self):
        payload = {"first_name": "Erik", "middle_names": "Ulfr", "last_name": "Douglas"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("middle_names must be a list of strings, got str" in e for e in errors))

    def test_middle_names_non_string_element_fails(self):
        payload = {"first_name": "Erik", "middle_names": ["Ulfr", 123], "last_name": "Douglas"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("middle_names[1] must be a string, got int" in e for e in errors))

    def test_valid_empty_middle_names_passes(self):
        payload = {"first_name": "Scarlett", "middle_names": [], "last_name": "Rose"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertTrue(valid, f"Unexpected errors: {errors}")

    def test_valid_populated_middle_names_passes(self):
        payload = {"first_name": "Erik", "middle_names": ["Ulfr"], "last_name": "Douglas"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertTrue(valid, f"Unexpected errors: {errors}")

    # Tests for duplicate surnames (legacy and escaped)
    def test_detect_duplicate_surnames_escaped_whitespace(self):
        test_cases = [
            (r"(?:^|\n)\s*(?:Alpha\ Rivers\ Rivers|Alpha\ Rivers)\s*:", "Rivers", "Rivers Rivers"),
            (r"(?:^|\n)\s*(?:Mr\.\ Rogers\ Rogers|Mr\.\ Rogers)\s*:", "Rogers", "Rogers Rogers"),
            (r"(?:^|\n)\s*(?:Boone\ Boone)\s*:", "Boone", "Boone Boone"),
            (r"(?:^|\n)\s*(?:Councilman\ Black\ Black)\s*:", "Black", "Black Black"),
            (r"(?:^|\n)\s*(?:O['‘’ʼ‛′]Connor\ O['‘’ʼ‛′]Connor)\s*:", "O'Connor", "O'Connor O'Connor"),
            (r"(?:^|\n)\s*(?:Mrs\ Virtuoso\ Virtuoso)\s*:", "Virtuoso", "Virtuoso Virtuoso"),
            (r"(?:^|\n)\s*(?:Nurse\ Cirillo\ Cirillo)\s*:", "Cirillo", "Cirillo Cirillo"),
            (r"(?:^|\n)\s*(?:Bishop\ Bishop)\s*:", "Bishop", "Bishop Bishop"),
            (r"(?:^|\n)\s*(?:Mr\.\ DeVille\ DeVille)\s*:", "DeVille", "DeVille DeVille"),
            (r"(?:^|\n)\s*(?:rat\ Rat)\s*:", "Rat", "Rat Rat"),
            (r"(?:^|\n)\s*(?:Professor\ Weiss\ Weiss)\s*:", "Weiss", "Weiss Weiss"),
            (r"(?:^|\n)\s*(?:Major\ Purcell\ Purcell)\s*:", "Purcell", "Purcell Purcell"),
            (r"Hugh\s+Rivers\s+Rivers", "Rivers", "Rivers Rivers"),
        ]
        for pat, last_name, expected in test_cases:
            defects = detect_duplicate_surnames(pat, last_name)
            self.assertIn(expected, defects, f"Expected {expected} in {pat}")

    def test_clean_patterns_with_escaped_whitespace_produce_no_defects(self):
        clean_cases = [
            (r"(?:^|\n)\s*(?:Alpha\ Rivers|The\ Mountain\ Sovereign)\s*:", "Rivers"),
            (r"(?:^|\n)\s*(?:Dominic\ Rogers|Dom\ Rogers)\s*:", "Rogers"),
            (r"(?:^|\n)\s*(?:Alicia\ Virtuoso|Mrs\ Virtuoso)\s*:", "Virtuoso"),
            (r"(?:^|\n)\s*(?:Marcus\ O['‘’ʼ‛′]Connor|Oldtown)\s*:", "O'Connor"),
            (r"(?:^|\n)\s*(?:Alistair\ Ambrose\ DeVille|Mr\.\ DeVille)\s*:", "DeVille"),
            (r"Hugh\s+Rivers", "Rivers"),
        ]
        for pat, last_name in clean_cases:
            defects = detect_duplicate_surnames(pat, last_name)
            self.assertEqual(len(defects), 0, f"False positive in {pat}: {defects}")

if __name__ == "__main__":
    unittest.main()
