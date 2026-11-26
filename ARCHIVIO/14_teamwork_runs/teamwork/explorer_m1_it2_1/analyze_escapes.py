import json
import re
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent
primary_path = repo_root / "FINAL/Svartulfr_NPC_Primary.json"
secondary_path = repo_root / "FINAL/Svartulfr_NPC_Secondary.json"

escaped_chars = set()
for path in [primary_path, secondary_path]:
    data = json.load(open(path, encoding="utf-8"))
    for entry in data["lexicon"]:
        regex = entry.get("avatar_activation_regex", "")
        # Find all \X where X is not n, s, d, b, etc.
        for m in re.finditer(r"\\(.)", regex):
            escaped_chars.add(m.group(1))

print("All escaped characters after backslash in 310 regexes:")
for c in sorted(escaped_chars):
    print(f"  {repr(c)}")
