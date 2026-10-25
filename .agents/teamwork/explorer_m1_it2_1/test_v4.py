import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

tests = [
    ("Alpha Rivers Rivers", "Rivers"),
    (r"Alpha\ Rivers\ Rivers", "Rivers"),
    (r"Mrs\ Virtuoso\ Virtuoso", "Virtuoso"),
    (r"O['‘’ʼ‛′]Connor\ O['‘’ʼ‛′]Connor", "O'Connor"),
    (r"Mr\.\ DeVille\ DeVille", "DeVille"),
    (r"Sanchez\-Rogers\ Sanchez\-Rogers", "Sanchez-Rogers"),
    ("D'Angelo D'Angelo", None),
]

def normalize_pattern(pattern_str: str) -> str:
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
    return norm

def detect_duplicate_surnames_v4(pattern_str: str, last_name: str = None):
    defects = []
    norm = normalize_pattern(pattern_str)

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

for pat, ln in tests:
    res = detect_duplicate_surnames_v4(pat, ln)
    print(f"last_name: {repr(ln)} --> {res}")
