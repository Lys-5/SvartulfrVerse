#!/usr/bin/env python3
"""
scripts/verify_npc_schema_contract.py

Authoritative verification script and reference validator for Wyvern NPC Schema Contracts:
- Milestone 1 (R1) reverse-engineering contracts codified:
  1. `npc_info` schema validation (first_name, middle_names, last_name, nicknames, titles, npc_prefix).
  2. Avatar gallery contract (HTTPS Cloudflare/Janitor URLs, root gallery array, gallery_count).
  3. Wyvern Module 93312 compilation logic (replicated native compiler, duplicate surname elimination).
  4. Anti-collision preservation (ignored_characters, ignored_personas, selective/secondary_keys rules).
  5. Byte-for-byte parity contract between entries and lexicon.

Usage:
  python scripts/verify_npc_schema_contract.py --self-test
  python scripts/verify_npc_schema_contract.py --check-files
  python scripts/verify_npc_schema_contract.py --all
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

try:
    import regex as pcre_regex
except ImportError:
    pcre_regex = None


# ==============================================================================
# 1. Module 93312 Replicated Compiler
# ==============================================================================

def escape_wyvern(text: str) -> str:
    """
    Replicates Module 93312's string escaping and character class substitutions:
    u = e => s(e).replace(/[.*+?^${}()|[\\]\\]/g, "\\$&")
                 .replace(/['\\u2018\\u2019\\u02BC\\u201B\\u2032]/g, "['‘’ʼ‛′]")
                 .replace(/[-\\u2010\\u2011\\u2012\\u2013\\u2014\\u2212]/g, "[-‐‑‒–—−]")
    """
    if not text:
        return ""
    normalized = unicodedata.normalize("NFC", text)
    special_chars = set(r".*+?^${}()|[]\\")
    quote_chars = set("'\u2018\u2019\u02BC\u201B\u2032")
    hyphen_chars = set("-\u2010\u2011\u2012\u2013\u2014\u2212")

    # Step 1: Escape regex meta-characters
    escaped_chars = []
    for ch in normalized:
        if ch in special_chars:
            escaped_chars.append("\\" + ch)
        else:
            escaped_chars.append(ch)
    s = "".join(escaped_chars)

    # Step 2 & 3: Replace quotes and hyphens with respective character classes
    out = []
    for ch in s:
        if ch in quote_chars:
            out.append("['‘’ʼ‛′]")
        elif ch in hyphen_chars:
            out.append("[-‐‑‒–—−]")
        else:
            out.append(ch)
    return "".join(out)


def compile_wyvern_avatar_regex(npc_info: Optional[Dict[str, Any]], prefix: str = "", delimiter: str = ":") -> str:
    """
    1:1 Exact Python replication of Wyvern Module 93312 WH(npc_info, prefix, delimiter).
    
    Returns the auto-generated regular expression string used by Wyvern client to split
    multi-character chat messages into individual speaker turns and match NPC avatars.
    """
    if not npc_info:
        return ""
    first_name_raw = npc_info.get("first_name")
    if not first_name_raw or not isinstance(first_name_raw, str) or not first_name_raw.strip():
        return ""

    u = escape_wyvern
    p = r"(?:\*\*)?"
    h = []

    prefix_trimmed = prefix.strip() if prefix else ""
    d = r"(?<=^|[^\p{L}\p{N}_])" if prefix_trimmed else ""

    if prefix_trimmed:
        h.append(f"{p}{u(prefix_trimmed)}\\s*{p}")
    else:
        h.append(rf"(?<=^|\n)\s*{p}")

    titles = npc_info.get("titles")
    if isinstance(titles, list) and len(titles) > 0:
        cleaned_titles = [u(t.strip()) for t in titles if isinstance(t, str) and t.strip()]
        if cleaned_titles:
            h.append(f"(({'|'.join(cleaned_titles)})\\s+)?")

    v = []
    def add_pattern(pattern: str, weight_factor: int, length: int):
        v.append({"pattern": pattern, "weight": 10000 * weight_factor + length})

    g = first_name_raw.strip()
    last_name_raw = npc_info.get("last_name")
    m = last_name_raw.strip() if (last_name_raw and isinstance(last_name_raw, str) and last_name_raw.strip()) else None

    middle_names_raw = npc_info.get("middle_names")
    if isinstance(middle_names_raw, list):
        y = [x.strip() for x in middle_names_raw if isinstance(x, str) and x.strip()]
    else:
        y = []

    max_mid_len = max((len(x) for x in y), default=0)
    w = u(g)
    c_last = u(m) if m else None
    x_mid = "|".join(u(x) for x in y) if y else None

    m_len = len(m) if m else 0

    if x_mid and c_last:
        add_pattern(f"{w}\\s+({x_mid})\\s+{c_last}", 3, len(g) + max_mid_len + m_len + 2)
    if c_last:
        add_pattern(f"{w}\\s+{c_last}", 2, len(g) + m_len + 1)
        add_pattern(f"{c_last}\\s+{w}", 2, len(g) + m_len + 1)
    if x_mid and c_last:
        add_pattern(f"{c_last}\\s+({x_mid})\\s+{w}", 3, len(g) + max_mid_len + m_len + 2)
    if x_mid:
        add_pattern(f"{w}\\s+({x_mid})", 2, len(g) + max_mid_len + 1)

    add_pattern(w, 1, len(g))
    if c_last:
        add_pattern(c_last, 1, m_len)

    nicknames_raw = npc_info.get("nicknames")
    if isinstance(nicknames_raw, list) and len(nicknames_raw) > 0:
        for nick in nicknames_raw:
            if not isinstance(nick, str) or not nick.strip():
                continue
            nick_stripped = nick.strip()
            words_count = len(nick_stripped.split()) or 1
            u_nick = u(nick)
            if "'" in nick or '"' in nick:
                add_pattern(u_nick, words_count, len(nick_stripped))
            else:
                add_pattern(u_nick, words_count, len(nick_stripped))
                add_pattern(f"'{u_nick}'", words_count, len(nick_stripped) + 2)
                add_pattern(f'"{u_nick}"', words_count, len(nick_stripped) + 2)

    # Sort stably by weight descending
    v.sort(key=lambda item: item["weight"], reverse=True)
    core_joined = "|".join(item["pattern"] for item in v)
    h.append(fr"{d}(?<coreName>{core_joined})(?=$|[^\p{{L}}\p{{N}}_])")

    if isinstance(titles, list) and len(titles) > 0:
        cleaned_titles = [u(t.strip()) for t in titles if isinstance(t, str) and t.strip()]
        if cleaned_titles:
            h.append(f"(\\s+({'|'.join(cleaned_titles)}))?")

    # Suffix particles and bracketed descriptors
    s_bracket = r"(?:\([^()\[\]:\r\n]{1,80}\)|\[[^()\[\]:\r\n]{1,80}\])"
    b_particle = (
        r"""(?:["'‘’“”][^"'‘’“”:\n]{1,40}["'‘’“”]|"""
        + s_bracket
        + r"""|\p{Lu}[\p{L}\p{N}.'’\-]*|(?:de|del|della|der|den|van|von|di|da|do|dos|das|la|le|les|du|bin|ibn|al|el|af|av|of|the|y|e|saint|st))"""
    )
    h.append(rf"(?:\s+{b_particle}){{0,6}}")

    if delimiter and delimiter.strip():
        h.append(rf"(?:\*\*)?\s*{u(delimiter.strip())}(?:\*\*(?=\s|$))?")

    return "".join(h)


def normalize_wyvern_regex_pattern(pattern_str: str) -> str:
    """
    Normalizes a Wyvern regex pattern by unescaping escaped whitespace, stripping
    character classes for quotes/hyphens, and unescaping common punctuation.
    Converts patterns like 'Alpha\\ Rivers\\ Rivers' or 'Mr\\.\\ Rogers\\ Rogers'
    into clean plain text for reliable defect auditing.
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
    Pre-normalizes escaped whitespace, character classes, and punctuation so that both legacy
    and compiled patterns are audited reliably.
    Returns list of defect instances found.
    """
    if not pattern_str:
        return []

    defects = []
    norm = normalize_wyvern_regex_pattern(pattern_str)

    # 1. Known legacy duplicate surname anomalies cataloged in Milestone 1 Explorer audit
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


# ==============================================================================
# 2. Schema and Contract Validation Functions
# ==============================================================================

CANONICAL_BROAD_KEYS = frozenset({
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
})


def is_valid_https_url(url: Any) -> bool:
    """
    Validates that url is a well-formed HTTPS URL with an explicit domain and path.
    Rejects bare schemes ('https://'), empty hostnames, invalid characters, and non-HTTPS protocols.
    """
    if not isinstance(url, str):
        return False
    s = url.strip()
    if not s.startswith("https://") or len(s) <= 8:
        return False
    try:
        parsed = urlparse(s)
        if parsed.scheme != "https" or not parsed.netloc:
            return False
        if "." not in parsed.netloc:
            return False
        labels = parsed.netloc.split(".")
        if any(len(label) == 0 for label in labels):
            return False
        return True
    except Exception:
        return False


@dataclass
class NpcInfoSchema:
    first_name: str
    middle_names: List[str] = field(default_factory=list)
    last_name: Optional[str] = None
    nicknames: List[str] = field(default_factory=list)
    titles: List[str] = field(default_factory=list)
    npc_prefix: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "first_name": self.first_name,
            "middle_names": self.middle_names,
            "last_name": self.last_name,
            "nicknames": self.nicknames,
            "titles": self.titles,
            "npc_prefix": self.npc_prefix,
        }


def validate_npc_info_schema(npc_info: Any) -> Tuple[bool, List[str]]:
    """
    Validates the `npc_info` object against Wyvern frontend schema requirements:
    - first_name: str (required, non-empty when stripped)
    - middle_names: list of str
    - last_name: str or None
    - nicknames: list of str
    - titles: list of str
    - npc_prefix: str or None
    """
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

    # middle_names (strictly required: must be present in dict, cannot be None, must be a list of strings)
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


def validate_avatar_gallery_contract(lorebook_root: Optional[Dict[str, Any]] = None, entry: Optional[Dict[str, Any]] = None) -> Tuple[bool, List[str]]:
    """
    Validates avatar gallery contracts:
    1. Root lorebook must contain `gallery` (list) and `gallery_count` (int >= 0 matching len(gallery)).
    2. Entry avatar must be a valid HTTPS URL (Cloudflare Images or Janitor CDN format).
    3. Alternate avatars, if present, must be valid HTTPS URLs.
    """
    errors = []

    # Check lorebook root gallery
    if lorebook_root is not None:
        if not isinstance(lorebook_root, dict):
            errors.append(f"Lorebook root must be a dictionary, got {type(lorebook_root).__name__}")
        else:
            if "gallery" not in lorebook_root:
                errors.append("Lorebook root missing 'gallery' array property")
            elif not isinstance(lorebook_root["gallery"], list):
                errors.append(f"Lorebook root 'gallery' must be a list, got {type(lorebook_root['gallery']).__name__}")

            if "gallery_count" not in lorebook_root:
                errors.append("Lorebook root missing 'gallery_count' property")
            else:
                gc = lorebook_root["gallery_count"]
                if isinstance(gc, bool) or not isinstance(gc, int) or gc < 0:
                    errors.append(f"Lorebook root 'gallery_count' must be a non-negative integer, got {type(gc).__name__} ({gc})")
                elif isinstance(lorebook_root.get("gallery"), list) and gc != len(lorebook_root["gallery"]):
                    errors.append(f"Lorebook root 'gallery_count' ({gc}) does not match len(gallery) ({len(lorebook_root['gallery'])})")

    # Check entry avatar
    if entry is not None:
        if not isinstance(entry, dict):
            errors.append(f"Entry must be a dictionary, got {type(entry).__name__}")
        else:
            avatar = entry.get("avatar")
            if not avatar:
                errors.append("Entry missing 'avatar' field or avatar is empty")
            elif not isinstance(avatar, str):
                errors.append(f"Entry 'avatar' must be a string URL, got {type(avatar).__name__}")
            elif not is_valid_https_url(avatar):
                errors.append(f"Entry 'avatar' must be an HTTPS URL with a valid domain and path, got: {avatar}")

            alt_avatars = entry.get("alternate_avatars")
            if alt_avatars is not None:
                if not isinstance(alt_avatars, list):
                    errors.append(f"'alternate_avatars' must be a list of strings, got {type(alt_avatars).__name__}")
                else:
                    for idx, alt in enumerate(alt_avatars):
                        if not is_valid_https_url(alt):
                            errors.append(f"'alternate_avatars[{idx}]' must be a valid HTTPS URL with a valid domain and path, got: {alt}")

    return len(errors) == 0, errors


def validate_anti_collision_contract(entry: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates anti-collision preservation:
    - ignored_characters: list of str (Character Card IDs)
    - ignored_personas: list of str (Persona IDs)
    - selective: bool
    - secondary_keys: list of str
    - keys: list of str (no CANONICAL_BROAD_KEYS)
    - nicknames / npc_info.nicknames: list of str (no CANONICAL_BROAD_KEYS)
    Rules:
      * ignored_characters and ignored_personas must be lists of strings.
      * selective must be False unless secondary_keys is populated.
      * keys, secondary_keys, and nicknames must not contain generic umbrella keywords (GEMINI.md §7).
    """
    errors = []
    if not isinstance(entry, dict):
        return False, ["Entry must be a dictionary"]

    # 1. ignored_characters
    ic = entry.get("ignored_characters")
    if ic is not None:
        if not isinstance(ic, list):
            errors.append(f"'ignored_characters' must be a list, got {type(ic).__name__}")
        else:
            for i, item in enumerate(ic):
                if not isinstance(item, str):
                    errors.append(f"'ignored_characters[{i}]' must be a string card ID, got {type(item).__name__}")

    # 2. ignored_personas
    ip = entry.get("ignored_personas")
    if ip is not None:
        if not isinstance(ip, list):
            errors.append(f"'ignored_personas' must be a list, got {type(ip).__name__}")
        else:
            for i, item in enumerate(ip):
                if not isinstance(item, str):
                    errors.append(f"'ignored_personas[{i}]' must be a string persona ID, got {type(item).__name__}")

    # 3. selective vs secondary_keys
    selective = entry.get("selective", False)
    sec_keys = entry.get("secondary_keys", [])
    if not isinstance(sec_keys, list):
        errors.append(f"'secondary_keys' must be a list, got {type(sec_keys).__name__}")
    else:
        if selective and len(sec_keys) == 0:
            errors.append("Entry has 'selective: true' but 'secondary_keys' is empty (prohibited by GEMINI.md §7)")
        for i, k in enumerate(sec_keys):
            if not isinstance(k, str):
                errors.append(f"'secondary_keys[{i}]' must be a string, got {type(k).__name__}")
            elif k.strip().lower() in CANONICAL_BROAD_KEYS:
                errors.append(f"Prohibited broad umbrella keyword '{k.strip()}' found in 'secondary_keys' (GEMINI.md §7 violation)")

    # 4. keys inspection
    keys = entry.get("keys")
    if keys is not None:
        if not isinstance(keys, list):
            errors.append(f"'keys' must be a list, got {type(keys).__name__}")
        else:
            for i, k in enumerate(keys):
                if not isinstance(k, str):
                    errors.append(f"'keys[{i}]' must be a string, got {type(k).__name__}")
                elif k.strip().lower() in CANONICAL_BROAD_KEYS:
                    errors.append(f"Prohibited broad umbrella keyword '{k.strip()}' found in 'keys' (GEMINI.md §7 violation)")

    # 5. nicknames inspection (top-level and inside npc_info)
    nicknames = entry.get("nicknames")
    if nicknames is not None:
        if not isinstance(nicknames, list):
            errors.append(f"'nicknames' must be a list, got {type(nicknames).__name__}")
        else:
            for i, n in enumerate(nicknames):
                if not isinstance(n, str):
                    errors.append(f"'nicknames[{i}]' must be a string, got {type(n).__name__}")
                elif n.strip().lower() in CANONICAL_BROAD_KEYS:
                    errors.append(f"Prohibited broad umbrella keyword '{n.strip()}' found in 'nicknames' (GEMINI.md §7 violation)")

    npc_info = entry.get("npc_info")
    if isinstance(npc_info, dict):
        info_nicks = npc_info.get("nicknames")
        if isinstance(info_nicks, list):
            for i, n in enumerate(info_nicks):
                if isinstance(n, str) and n.strip().lower() in CANONICAL_BROAD_KEYS:
                    errors.append(f"Prohibited broad umbrella keyword '{n.strip()}' found in 'npc_info.nicknames' (GEMINI.md §7 violation)")

    return len(errors) == 0, errors


def validate_entries_lexicon_parity(lorebook_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates that lorebook['entries'] and lorebook['lexicon'] arrays are 100% byte-for-byte identical.
    """
    errors = []
    if not isinstance(lorebook_data, dict):
        return False, [f"Lorebook data must be a dictionary, got {type(lorebook_data).__name__}"]

    if "entries" not in lorebook_data:
        errors.append("Lorebook missing 'entries' array")
    if "lexicon" not in lorebook_data:
        errors.append("Lorebook missing 'lexicon' array")

    if errors:
        return False, errors

    entries = lorebook_data["entries"]
    lexicon = lorebook_data["lexicon"]

    if not isinstance(entries, list):
        errors.append(f"'entries' must be a list, got {type(entries).__name__}")
    if not isinstance(lexicon, list):
        errors.append(f"'lexicon' must be a list, got {type(lexicon).__name__}")

    if errors:
        return False, errors

    if len(entries) != len(lexicon):
        errors.append(f"Length mismatch: entries has {len(entries)} items, lexicon has {len(lexicon)} items")
        return False, errors

    entries_dump = json.dumps(entries, sort_keys=True)
    lexicon_dump = json.dumps(lexicon, sort_keys=True)

    if entries_dump != lexicon_dump:
        errors.append(f"Byte-for-byte mismatch: entries serialization length ({len(entries_dump)}) != lexicon ({len(lexicon_dump)})")
        # Identify first diverging index
        for idx in range(len(entries)):
            e_dump = json.dumps(entries[idx], sort_keys=True)
            l_dump = json.dumps(lexicon[idx], sort_keys=True)
            if e_dump != l_dump:
                e_name = entries[idx].get("name", f"Index {idx}")
                errors.append(f"First mismatch at entry index {idx} ('{e_name}')")
                break
        return False, errors

    return True, []


# ==============================================================================
# 3. File Audit Runner
# ==============================================================================

def audit_file(filepath: Path, verbose: bool = False) -> Dict[str, Any]:
    """
    Performs comprehensive contract audit on a single lorebook JSON file.
    """
    report = {
        "file": str(filepath),
        "exists": False,
        "entry_count": 0,
        "root_gallery_valid": False,
        "root_gallery_errors": [],
        "parity_valid": False,
        "parity_errors": [],
        "npc_entries_count": 0,
        "npc_info_valid_count": 0,
        "npc_info_errors": [],
        "duplicate_surname_defects": [],
        "anti_collision_valid_count": 0,
        "anti_collision_errors": [],
        "avatar_valid_count": 0,
        "avatar_errors": [],
    }

    if not filepath.exists():
        report["root_gallery_errors"].append(f"File not found: {filepath}")
        return report

    report["exists"] = True
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        report["root_gallery_errors"].append(f"JSON load error: {e}")
        return report

    # 1. Root Gallery check
    g_valid, g_errors = validate_avatar_gallery_contract(lorebook_root=data)
    report["root_gallery_valid"] = g_valid
    report["root_gallery_errors"] = g_errors

    # 2. Parity check
    p_valid, p_errors = validate_entries_lexicon_parity(data)
    report["parity_valid"] = p_valid
    report["parity_errors"] = p_errors

    lexicon = data.get("lexicon", [])
    report["entry_count"] = len(lexicon)

    for idx, entry in enumerate(lexicon):
        entry_type = entry.get("type")
        name = entry.get("name", f"Entry_{idx}")

        if entry_type == "npc":
            report["npc_entries_count"] += 1

            # Avatar check
            a_valid, a_errs = validate_avatar_gallery_contract(entry=entry)
            if a_valid:
                report["avatar_valid_count"] += 1
            else:
                report["avatar_errors"].append(f"{name}: {'; '.join(a_errs)}")

            # npc_info check
            npc_info = entry.get("npc_info")
            if npc_info is not None:
                n_valid, n_errs = validate_npc_info_schema(npc_info)
                if n_valid:
                    report["npc_info_valid_count"] += 1
                else:
                    report["npc_info_errors"].append(f"{name}: {'; '.join(n_errs)}")
            else:
                report["npc_info_errors"].append(f"{name}: missing npc_info")

            # Duplicate surname defect check in custom regex
            custom_regex = entry.get("avatar_activation_regex", "")
            last_name = npc_info.get("last_name") if isinstance(npc_info, dict) else None
            dupes = detect_duplicate_surnames(custom_regex, last_name)
            if dupes:
                report["duplicate_surname_defects"].append({
                    "entry_name": name,
                    "defects": dupes,
                    "regex_snippet": custom_regex[:80] + "..." if len(custom_regex) > 80 else custom_regex
                })

            # Anti-collision check
            ac_valid, ac_errs = validate_anti_collision_contract(entry)
            if ac_valid:
                report["anti_collision_valid_count"] += 1
            else:
                report["anti_collision_errors"].append(f"{name}: {'; '.join(ac_errs)}")

    return report


# ==============================================================================
# 4. Self-Contained Test Suite Execution
# ==============================================================================

def run_self_tests() -> bool:
    """
    Executes self-contained validation tests across all 5 contract areas.
    Returns True if all assertions hold.
    """
    print("\n" + "=" * 70)
    print("RUNNING CONTRACT VERIFICATION SELF-TESTS (MILESTONE 1 / R1)")
    print("=" * 70)

    # 1. Test NpcInfoSchema validation
    print("\n[Contract 1: npc_info Schema Validation]")
    valid_erik = {
        "first_name": "Erik",
        "middle_names": ["Ulfr"],
        "last_name": "Douglas",
        "nicknames": ["The Old Wolf", "Pack Leader"],
        "titles": ["Lord", "Alpha"],
        "npc_prefix": ""
    }
    ok, errs = validate_npc_info_schema(valid_erik)
    assert ok, f"Expected Erik to be valid, got: {errs}"
    print("  [PASS] Full valid Erik schema passed.")

    valid_scarlett = {
        "first_name": "Scarlett",
        "middle_names": [],
        "last_name": "Rose",
        "nicknames": ["Red"],
        "titles": [],
        "npc_prefix": None
    }
    ok, errs = validate_npc_info_schema(valid_scarlett)
    assert ok, f"Expected Scarlett to be valid, got: {errs}"
    print("  [PASS] Minimal valid Scarlett schema passed.")

    # Invalids
    invalid_cases = [
        ({"middle_names": [], "last_name": "Doe"}, "missing first_name"),
        ({"first_name": "", "middle_names": []}, "empty first_name"),
        ({"first_name": "   ", "middle_names": []}, "whitespace first_name"),
        ({"first_name": 123, "middle_names": []}, "non-string first_name"),
        ({"first_name": "John"}, "missing middle_names"),
        ({"first_name": "John", "middle_names": None}, "null middle_names"),
        ({"first_name": "John", "middle_names": "NotAList"}, "string middle_names"),
        ({"first_name": "John", "middle_names": [123]}, "non-string in middle_names"),
        ({"first_name": "John", "middle_names": [], "last_name": 456}, "non-string last_name"),
        ({"first_name": "John", "middle_names": [], "nicknames": "Johnny"}, "string nicknames"),
        ({"first_name": "John", "middle_names": [], "titles": "Sir"}, "string titles"),
        ({"first_name": "John", "middle_names": [], "npc_prefix": 789}, "non-string npc_prefix"),
    ]
    for case, label in invalid_cases:
        ok, errs = validate_npc_info_schema(case)
        assert not ok, f"Expected invalid case '{label}' to fail, but it passed."
        print(f"  [PASS] Invalid case '{label}' correctly rejected: {errs[0]}")

    # 2. Test Avatar Gallery Contract
    print("\n[Contract 2: Avatar Gallery Contract]")
    valid_root_empty = {"gallery": [], "gallery_count": 0}
    ok, errs = validate_avatar_gallery_contract(lorebook_root=valid_root_empty)
    assert ok, f"Expected empty gallery root to pass: {errs}"
    print("  [PASS] Valid empty root gallery passed.")

    valid_root_populated = {
        "gallery": [{"id": "1", "imageURL": "https://imagedelivery.net/abc/123/public", "title": "Pic", "type": "avatar"}],
        "gallery_count": 1
    }
    ok, errs = validate_avatar_gallery_contract(lorebook_root=valid_root_populated)
    assert ok, f"Expected populated gallery root to pass: {errs}"
    print("  [PASS] Valid populated root gallery passed.")

    # Invalids
    bad_roots = [
        ({}, "missing gallery and gallery_count"),
        ({"gallery": "not_a_list", "gallery_count": 0}, "gallery not a list"),
        ({"gallery": [], "gallery_count": -1}, "negative gallery_count"),
        ({"gallery": [1, 2], "gallery_count": 1}, "gallery_count mismatch"),
        ({"gallery": [{"id": "1"}], "gallery_count": True}, "boolean gallery_count True"),
        ({"gallery": [], "gallery_count": False}, "boolean gallery_count False"),
        (123, "non-dict lorebook root"),
        ("not_a_dict", "string lorebook root"),
    ]
    for b_root, label in bad_roots:
        ok, errs = validate_avatar_gallery_contract(lorebook_root=b_root)
        assert not ok, f"Expected '{label}' to fail: {errs}"
        print(f"  [PASS] Invalid gallery root '{label}' correctly rejected.")

    # Avatar entry checks
    valid_avatar_cf = {"avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d/public"}
    ok, errs = validate_avatar_gallery_contract(entry=valid_avatar_cf)
    assert ok, f"Valid Cloudflare avatar failed: {errs}"
    print("  [PASS] Valid Cloudflare HTTPS avatar URL passed.")

    invalid_avatars = [
        ({"avatar": "http://insecure.com/pic.jpg"}, "insecure HTTP"),
        ({"avatar": ""}, "empty avatar"),
        ({"avatar": None}, "null avatar"),
        ({"avatar": "https://"}, "bare https scheme"),
        ({"avatar": "https://   "}, "whitespace bare https"),
        ({"avatar": "https:///"}, "bare https slash"),
        ({"avatar": "https://bad"}, "invalid domain fragment"),
        ({"avatar": "https://.com"}, "missing domain label"),
        ({"avatar": "https://valid.com/pic.png", "alternate_avatars": ["http://bad.com"]}, "insecure alternate avatar"),
        ({"avatar": "https://valid.com/pic.png", "alternate_avatars": ["https://"]}, "bare https alternate avatar"),
    ]
    for b_entry, label in invalid_avatars:
        ok, errs = validate_avatar_gallery_contract(entry=b_entry)
        assert not ok, f"Expected '{label}' to fail: {errs}"
        print(f"  [PASS] Invalid avatar '{label}' correctly rejected.")

    ok, errs = validate_avatar_gallery_contract(entry="not_a_dict")
    assert not ok, "Expected non-dict entry to fail"
    print("  [PASS] Non-dict entry handled gracefully.")

    # 3. Test Module 93312 Compilation Logic
    print("\n[Contract 3: Wyvern Module 93312 Compilation Logic]")
    # Erik regex
    erik_regex = compile_wyvern_avatar_regex(valid_erik, prefix="", delimiter=":")
    assert "Erik" in erik_regex
    assert "Douglas" in erik_regex
    assert "(?<coreName>" in erik_regex
    assert "Lord|Alpha" in erik_regex
    print(f"  [PASS] Erik Ulfr Douglas compiled successfully ({len(erik_regex)} chars).")

    # Scarlett regex
    scarlett_regex = compile_wyvern_avatar_regex(valid_scarlett, prefix="", delimiter=":")
    assert "Scarlett\\s+Rose" in scarlett_regex
    assert "Rose\\s+Scarlett" in scarlett_regex
    assert "'Red'" in scarlett_regex
    print(f"  [PASS] Scarlett Rose compiled successfully ({len(scarlett_regex)} chars).")

    # Prefix handling
    sierra_with_prefix = compile_wyvern_avatar_regex({"first_name": "Sierra", "middle_names": [], "last_name": "Cruz"}, prefix="=>", delimiter=":")
    assert "=>" in sierra_with_prefix
    print("  [PASS] Custom prefix '=>' integrated properly.")

    # Normalization & duplicate surname detection
    assert normalize_wyvern_regex_pattern(r"Alpha\ Rivers\ Rivers") == "Alpha Rivers Rivers"
    assert normalize_wyvern_regex_pattern(r"O['‘’ʼ‛′]Connor") == "O'Connor"
    assert normalize_wyvern_regex_pattern(r"Jean[-‐‑‒–—−]Luc") == "Jean-Luc"

    dupe_sample = r"(?:^|\n)\s*(?:Alpha\ Rivers\ Rivers|Alpha\ Rivers)\s*:"
    detected = detect_duplicate_surnames(dupe_sample, "Rivers")
    assert "Rivers Rivers" in detected, f"Failed to detect in {dupe_sample}"
    print(f"  [PASS] Duplicate surname correctly detected in legacy escaped regex: {detected}")

    clean_sample = r"(?:^|\n)\s*(?:Alpha\ Rivers|The\ Mountain\ Sovereign)\s*:"
    detected_clean = detect_duplicate_surnames(clean_sample, "Rivers")
    assert len(detected_clean) == 0, f"Expected no dupes in clean sample, got {detected_clean}"
    print("  [PASS] Clean pattern verified without false duplicate detection.")

    # Verify matching with PCRE regex if available
    if pcre_regex:
        pat = pcre_regex.compile(scarlett_regex, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
        m = pat.search('Scarlett Rose: "Hello there."')
        assert m is not None, "Failed to match valid dialogue turn for Scarlett Rose"
        assert m.group("coreName").lower() == "scarlett rose"
        print(f"  [PASS] Compiled regex matched real dialogue speaker turn: '{m.group('coreName')}'")

    # 4. Test Anti-Collision Contract
    print("\n[Contract 4: Anti-Collision Contract]")
    valid_ac_entry = {
        "ignored_characters": ["_HEQQbbRFwKdG8QE2Fh1z1"],
        "ignored_personas": ["persona_1786335754946"],
        "selective": False,
        "secondary_keys": []
    }
    ok, errs = validate_anti_collision_contract(valid_ac_entry)
    assert ok, f"Valid anti-collision entry failed: {errs}"
    print("  [PASS] Valid anti-collision entry passed.")

    invalid_ac_cases = [
        ({"ignored_characters": "not_a_list"}, "ignored_characters string"),
        ({"ignored_personas": [123]}, "ignored_personas non-string"),
        ({"selective": True, "secondary_keys": []}, "selective without secondary_keys"),
        ({"keys": ["alpha"]}, "broad umbrella key in keys"),
        ({"secondary_keys": ["werewolf"]}, "broad umbrella key in secondary_keys"),
        ({"nicknames": ["student"]}, "broad umbrella key in nicknames"),
        ({"keys": "not_a_list"}, "keys string"),
        ({"keys": [123]}, "keys non-string element"),
        ({"npc_info": {"nicknames": ["college"]}}, "broad key in npc_info.nicknames"),
    ]
    for b_ac, label in invalid_ac_cases:
        ok, errs = validate_anti_collision_contract(b_ac)
        assert not ok, f"Expected '{label}' to fail: {errs}"
        print(f"  [PASS] Invalid anti-collision '{label}' correctly rejected.")

    valid_compound_entry = {
        "keys": ["Roman Blackwood", "Alpha Rivers"],
        "secondary_keys": ["Blackwood Heir", "Douglas Pack"],
        "selective": False
    }
    ok, errs = validate_anti_collision_contract(valid_compound_entry)
    assert ok, f"Expected valid compound entry to pass, got: {errs}"
    print("  [PASS] Legitimate compound names with broad substrings passed without false positives.")

    # 5. Test Parity Contract
    print("\n[Contract 5: Entries == Lexicon Parity Contract]")
    dummy_item = {"name": "Test", "id": 1}
    valid_parity = {"entries": [dummy_item], "lexicon": [dummy_item]}
    ok, errs = validate_entries_lexicon_parity(valid_parity)
    assert ok, f"Valid parity failed: {errs}"
    print("  [PASS] Valid identical entries/lexicon parity passed.")

    invalid_parity_cases = [
        ({"entries": [dummy_item], "lexicon": []}, "length mismatch"),
        ({"entries": [{"name": "A"}], "lexicon": [{"name": "B"}]}, "content mismatch"),
        ({"entries": []}, "missing lexicon"),
        (456, "non-dict lorebook data integer"),
        ("string_data", "non-dict lorebook data string"),
    ]
    for b_par, label in invalid_parity_cases:
        ok, errs = validate_entries_lexicon_parity(b_par)
        assert not ok, f"Expected '{label}' to fail: {errs}"
        print(f"  [PASS] Invalid parity case '{label}' correctly rejected.")

    print("\n" + "=" * 70)
    print("ALL CONTRACT SELF-TESTS PASSED SUCCESSFULLY (100% SUCCESS RATE)")
    print("=" * 70 + "\n")
    return True


# ==============================================================================
# 5. Main CLI Entry Point
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Wyvern NPC Schema Contract Verification Tool (Milestone 1 / R1)")
    parser.add_argument("--self-test", action="store_true", help="Run contract verification self-tests")
    parser.add_argument("--check-files", action="store_true", help="Audit local FINAL/ and lorebooks/optimized/ files against contracts")
    parser.add_argument("--all", action="store_true", help="Run self-tests and file audit")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show verbose audit diagnostics")
    args = parser.parse_args()

    # Default to --self-test if no action specified
    if not (args.self_test or args.check_files or args.all):
        args.self_test = True

    overall_success = True

    if args.self_test or args.all:
        try:
            if not run_self_tests():
                overall_success = False
        except Exception as e:
            print(f"[FAIL] Self-test exception: {e}")
            import traceback
            traceback.print_exc()
            overall_success = False

    if args.check_files or args.all:
        print("\n" + "=" * 70)
        print("AUDITING LOCAL LOREBOOK FILES AGAINST CONTRACTS")
        print("=" * 70)
        target_files = [
            Path("FINAL/Svartulfr_NPC_Primary.json"),
            Path("FINAL/Svartulfr_NPC_Secondary.json"),
            Path("lorebooks/optimized/Svartulfr_NPC_Primary.json"),
            Path("lorebooks/optimized/Svartulfr_NPC_Secondary.json"),
        ]
        for tf in target_files:
            rep = audit_file(tf, verbose=args.verbose)
            print(f"\nAudit Report for: {tf}")
            if not rep["exists"]:
                print("  Status: FILE NOT FOUND")
                continue

            print(f"  Total Entries in Lexicon: {rep['entry_count']}")
            print(f"  Root Gallery Valid: {rep['root_gallery_valid']} ({'; '.join(rep['root_gallery_errors']) if rep['root_gallery_errors'] else 'OK'})")
            print(f"  Entries == Lexicon Parity: {rep['parity_valid']} ({'; '.join(rep['parity_errors']) if rep['parity_errors'] else 'OK'})")
            print(f"  NPC Entries Checked: {rep['npc_entries_count']}")
            print(f"  Valid Avatars: {rep['avatar_valid_count']}/{rep['npc_entries_count']}")
            print(f"  Valid npc_info: {rep['npc_info_valid_count']}/{rep['npc_entries_count']}")
            print(f"  Legacy Duplicate Surname Defects in regex: {len(rep['duplicate_surname_defects'])}")
            if rep["duplicate_surname_defects"]:
                for d in rep["duplicate_surname_defects"][:5]:
                    print(f"    - {d['entry_name']}: {d['defects']}")
                if len(rep["duplicate_surname_defects"]) > 5:
                    print(f"    ... and {len(rep['duplicate_surname_defects']) - 5} more defects cataloged for Milestone 2 remediation.")

    sys.exit(0 if overall_success else 1)


if __name__ == "__main__":
    main()
