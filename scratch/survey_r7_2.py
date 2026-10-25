import json
import re
from collections import Counter

primary_path = r"e:\repository\SvartulfrVerse\FINAL\Svartulfr_NPC_Primary.json"
secondary_path = r"e:\repository\SvartulfrVerse\FINAL\Svartulfr_NPC_Secondary.json"

with open(primary_path, "r", encoding="utf-8") as f:
    primary_data = json.load(f)

with open(secondary_path, "r", encoding="utf-8") as f:
    secondary_data = json.load(f)

p_entries = primary_data.get("lexicon", [])
s_entries = secondary_data.get("lexicon", [])

all_entries = [("Primary", e) for e in p_entries] + [("Secondary", e) for e in s_entries]

BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

print("=== 1. JED+ BRACKET BLOCK CHECK ===")
p_starts_bracket = []
p_no_bracket = []
for e in p_entries:
    desc = e.get("description", "").strip()
    eid = e.get("id", "")
    name = e.get("name", "")
    if desc.startswith("["):
        p_starts_bracket.append((eid, name))
    else:
        p_no_bracket.append((eid, name, desc[:60]))

s_starts_bracket = []
s_no_bracket = []
for e in s_entries:
    desc = e.get("description", "").strip()
    eid = e.get("id", "")
    name = e.get("name", "")
    if desc.startswith("["):
        s_starts_bracket.append((eid, name))
    else:
        s_no_bracket.append((eid, name, desc[:60]))

print(f"Primary: {len(p_starts_bracket)}/{len(p_entries)} start with '['")
print(f"Primary without '[': {len(p_no_bracket)}")
for x in p_no_bracket:
    print(f"  {x[0]} - {x[1]}: {repr(x[2])}")

print(f"Secondary: {len(s_starts_bracket)}/{len(s_entries)} start with '['")
print(f"Secondary without '[': {len(s_no_bracket)}")
for x in s_no_bracket:
    print(f"  {x[0]} - {x[1]}: {repr(x[2])}")

print("\n=== 2. SECTION HEADERS AUDIT ===")
# Standard headers expected:
# BACKSTORY:
# FAMILY & PACK: or CLAN AND COMPANY: (or similar)
# VOICE & BEHAVIOR:
# thematic closure: uppercase section or [THEME...]

def extract_headers(text):
    # Match headers like `FOO BAR:` or `[FOO BAR]` at line start
    lines = text.split("\n")
    headers = []
    for line in lines:
        line_s = line.strip()
        # Header like ALL_CAPS_AND_AMP: ...
        m = re.match(r"^([A-Z0-9\s&/\-]+):", line_s)
        if m:
            h = m.group(1).strip()
            # filter out false positives if line is very long or bracket attributes
            if len(h) < 40 and not line_s.startswith("["):
                headers.append(h + ":")
        m_lower = re.match(r"^([A-Za-z0-9\s&/\-]+):", line_s)
        if m_lower and not m:
            h = m_lower.group(1).strip()
            if len(h) < 40 and not line_s.startswith("["):
                headers.append(h + ": (mixed/lower)")
    return headers

all_header_counts = Counter()
non_standard_headers = []

for origin, e in all_entries:
    desc = e.get("description", "")
    eid = e.get("id", "")
    name = e.get("name", "")
    lines = [l.strip() for l in desc.split("\n") if l.strip()]
    
    # Check headers
    entry_headers = []
    for line in lines:
        m = re.match(r"^([A-Za-z0-9\s&/\-'\"]+):", line)
        if m:
            h = m.group(1).strip()
            if len(h) <= 35 and not line.startswith("["):
                entry_headers.append(h)
                all_header_counts[h] += 1
                if any(c.islower() for c in h) or "PERSONALITY" in h or h not in ["BACKSTORY", "FAMILY & PACK", "CLAN AND COMPANY", "FAMILY & CLAN", "VOICE & BEHAVIOR", "VOICE & MANNERISMS"]:
                    pass

print("Top headers found across all 310 entries:")
for h, c in all_header_counts.most_common(25):
    print(f"  {h}: {c}")

print("\n=== 3. SPECIFIC 3 IRREGULAR ENTRIES IN SECONDARY ===")
target_ids = {
    "NQd7n3QacMcK-TzowQ2LE": "Bruce",
    "oov5UWuVhZ3RGgoxMkaTS": "Campus Staff Rat",
    "Og7V6v67guXXAaP0_PsTM": "Adrian"
}

for e in s_entries:
    eid = e.get("id", "")
    if eid in target_ids:
        print(f"\n--- Entry: {target_ids[eid]} ({eid}) ---")
        print(f"Name: {e.get('name')}")
        print(f"Keys: {e.get('keys')}")
        print(f"Type: {e.get('type')}")
        print(f"Selective: {e.get('selective')}")
        print(f"Exclude recursion: {e.get('exclude_from_recursion')}")
        print(f"Avatar: {e.get('avatar')}")
        print("Description:")
        print(e.get("description", ""))

print("\n=== 4. FORMATTING DISCIPLINE AUDIT ===")
em_dash_entries = []
asterisk_entries = []
age_macro_entries = []
broad_keys_entries = []
recursion_false_entries = []

for origin, e in all_entries:
    eid = e.get("id", "")
    name = e.get("name", "")
    desc = e.get("description", "")
    keys = e.get("keys", [])
    exclude_rec = e.get("exclude_from_recursion", None)
    
    # 1. Em-dash
    em_dashes = desc.count("—")
    if em_dashes > 0:
        em_dash_entries.append((origin, eid, name, em_dashes))
        
    # 2. Asterisks
    # Check if asterisks *...* or **...** appear
    if "*" in desc:
        asterisk_entries.append((origin, eid, name, desc.count("*")))
        
    # 3. {{age}} macros
    if "{{age}}" in desc or "{{age " in desc or "{{age}" in desc:
        age_macro_entries.append((origin, eid, name))
    # Also check keys or name
    for k in keys:
        if "{{age" in k:
            age_macro_entries.append((origin, eid, name + " (in keys)"))
            
    # 4. Broad keys
    matched_broad = [k for k in keys if k.lower().strip() in BROAD_KEYS]
    if matched_broad:
        broad_keys_entries.append((origin, eid, name, matched_broad))
        
    # 5. Exclude recursion
    if exclude_rec is not True:
        recursion_false_entries.append((origin, eid, name, exclude_rec))

print(f"Total entries with em-dash (—): {len(em_dash_entries)} (Total em-dashes: {sum(x[3] for x in em_dash_entries)})")
for origin, eid, name, cnt in em_dash_entries[:10]:
    print(f"  [{origin}] {eid} - {name}: {cnt} em-dashes")

print(f"\nTotal entries with asterisks (*): {len(asterisk_entries)} (Total asterisks: {sum(x[3] for x in asterisk_entries)})")
for origin, eid, name, cnt in asterisk_entries[:10]:
    print(f"  [{origin}] {eid} - {name}: {cnt} asterisks")

print(f"\nTotal entries with residual {{{{age}}}}: {len(age_macro_entries)}")
for x in age_macro_entries:
    print(f"  {x}")

print(f"\nTotal entries with BROAD_KEYS: {len(broad_keys_entries)}")
for origin, eid, name, bk in broad_keys_entries:
    print(f"  [{origin}] {eid} - {name}: {bk}")

print(f"\nTotal entries where exclude_from_recursion is not True: {len(recursion_false_entries)}")
for origin, eid, name, val in recursion_false_entries[:15]:
    print(f"  [{origin}] {eid} - {name}: val={val}")
