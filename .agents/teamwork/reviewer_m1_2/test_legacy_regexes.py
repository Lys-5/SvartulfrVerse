import json
import re
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent

def detect_normalized(pattern_str: str, last_name=None):
    defects = []
    # Normalize backslash-escaped whitespace
    norm = re.sub(r'\\+\s+', ' ', pattern_str)
    # Normalize character classes for quotes and hyphens
    norm = re.sub(r"\[['‘’ʼ‛′]+\]", "'", norm)
    norm = re.sub(r"\[[-‐‑‒–—−]+\]", "-", norm)
    # Normalize escaped punctuation
    norm = re.sub(r"\\+([.'\"])", r"\1", norm)

    known_dupes = [
        "Rivers Rivers", "Rogers Rogers", "Boone Boone", "Black Black",
        "O'Connor O'Connor", "Virtuoso Virtuoso", "Cirillo Cirillo",
        "Bishop Bishop", "Thompson Thompson", "DeVille DeVille"
    ]
    for kd in known_dupes:
        if kd.lower() in norm.lower():
            defects.append(kd)

    generic_dupes = re.findall(r"\b([A-Za-z]{3,})\s+\1\b", norm, flags=re.IGNORECASE)
    for gd in generic_dupes:
        dupe_str = f"{gd} {gd}"
        if dupe_str not in defects:
            defects.append(dupe_str)

    if last_name and last_name.strip():
        ln = last_name.strip()
        double_ln = f"{ln} {ln}"
        if double_ln.lower() in norm.lower() and double_ln not in defects:
            defects.append(double_ln)

    return defects

print("=== NORMALIZED DETECTOR TEST ON FINAL LOREBOOKS ===")
for p in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    data = json.load(open(repo_root / p, encoding='utf-8'))
    found = []
    for e in data['lexicon']:
        reg = e.get('avatar_activation_regex', '')
        ln = e.get('npc_info', {}).get('last_name')
        d = detect_normalized(reg, ln)
        if d:
            found.append((e.get('name'), d))
    print(f"\n{p}: {len(found)} defects found:")
    for name, d in found:
        print(f"  - {name}: {d}")
