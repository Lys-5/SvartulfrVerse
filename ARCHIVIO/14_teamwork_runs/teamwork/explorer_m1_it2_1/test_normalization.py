import json
import re
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from scripts.verify_npc_schema_contract import compile_wyvern_avatar_regex

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

def detect_duplicate_surnames_v3(pattern_str: str, last_name: str = None):
    defects = []
    norm = normalize_pattern(pattern_str)

    # 1. Check known legacy duplicate surname catalog
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

    # 3. Generic adjacent duplicate word check: r'\b([A-Za-z]{3,})\s+\1\b'
    generic_dupes = re.findall(r"\b([A-Za-z]{3,})\s+\1\b", norm, flags=re.IGNORECASE)
    for gd in generic_dupes:
        dupe_str = f"{gd} {gd}"
        if not any(dupe_str.lower() == d.lower() for d in defects):
            defects.append(dupe_str)

    return defects

print("=== TESTING ON FINAL LOREBOOKS (v3) ===")
for p in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    data = json.load(open(repo_root / p, encoding='utf-8'))
    found = []
    for e in data['lexicon']:
        reg = e.get('avatar_activation_regex', '')
        ln = e.get('npc_info', {}).get('last_name')
        d = detect_duplicate_surnames_v3(reg, ln)
        if d:
            found.append((e.get('name'), d))
    print(f"\n{p}: {len(found)} defects found:")
    for name, d in found:
        print(f"  - {name}: {d}")

print("\n=== TESTING FRESHLY COMPILED REGEXES FOR ALL 310 NPCS ===")
compiled_defects = []
for p in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    data = json.load(open(repo_root / p, encoding='utf-8'))
    for e in data['lexicon']:
        npc_info = e.get('npc_info')
        if not npc_info or not npc_info.get('first_name'):
            continue
        compiled = compile_wyvern_avatar_regex(npc_info)
        d = detect_duplicate_surnames_v3(compiled, npc_info.get('last_name'))
        if d:
            compiled_defects.append((e.get('name'), d))

print(f"Total defects on freshly compiled regexes: {len(compiled_defects)}")
