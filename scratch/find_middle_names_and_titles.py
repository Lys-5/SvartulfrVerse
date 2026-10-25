import json
import re

primary_data = json.load(open("FINAL/Svartulfr_NPC_Primary.json", encoding="utf-8"))
entries = primary_data["lexicon"]

candidates_with_middle = []
candidates_with_titles = []

for idx, e in enumerate(entries):
    name = e.get("name", "")
    content = e.get("content", "")
    bracket_m = re.search(r"\[([^\]]+)\]", content)
    bracket_str = bracket_m.group(1) if bracket_m else ""
    name_m = re.search(r"NAME:\s*([^;]+)", bracket_str)
    jed_name = name_m.group(1).strip() if name_m else name
    role_m = re.search(r"ROLE:\s*([^;]+)", bracket_str)
    jed_role = role_m.group(1).strip() if role_m else ""

    # Split jed_name into tokens before commas or parenthesis
    clean_jname = re.split(r"[,(]", jed_name)[0].strip()
    # Remove quotes
    clean_jname_noquotes = re.sub(r'["\'][^"\']+["\']', '', clean_jname).strip()
    tokens = clean_jname_noquotes.split()
    
    # Check if > 2 tokens (excluding titles like Lord, Dr., Professor)
    title_words = {"Professor", "Prof.", "Dr.", "Doctor", "Jarl", "Lord", "Lady", "Alpha", "Chancellor", "Coach", "Councilman"}
    lead_titles = [t for t in title_words if t in clean_jname.split()]
    non_title_tokens = [tok for tok in tokens if tok not in title_words]
    
    if len(non_title_tokens) > 2:
        candidates_with_middle.append((idx, name, jed_name, non_title_tokens))
    if lead_titles or any(t in name or t in jed_name or t in jed_role for t in title_words):
        candidates_with_titles.append((idx, name, jed_name, jed_role, lead_titles))

print(f"Candidates with > 2 name tokens ({len(candidates_with_middle)}):")
for c in candidates_with_middle:
    print(f"[{c[0]:02d}] {c[1]} -> JED: '{c[2]}' -> Tokens: {c[3]}")

print(f"\nCandidates with titles ({len(candidates_with_titles)}):")
for c in candidates_with_titles:
    print(f"[{c[0]:02d}] {c[1]} -> JED: '{c[2]}' -> Lead: {c[4]} -> Role: '{c[3]}'")
