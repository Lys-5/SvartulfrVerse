import json
import re

primary_data = json.load(open("FINAL/Svartulfr_NPC_Primary.json", encoding="utf-8"))
entries = primary_data["lexicon"]

TITLES_PATTERNS = {
    "Professor": r"\bProfessor\b|\bProf\b",
    "Dr.": r"\bDr\.?\b|\bDoctor\b",
    "Jarl": r"\bJarl\b",
    "Lord": r"\bLord\b",
    "Lady": r"\bLady\b",
    "Alpha": r"\bAlpha\b",
    "Chancellor": r"\bChancellor\b",
    "Coach": r"\bCoach\b",
    "Councilman": r"\bCouncilman\b",
    "Commander": r"\bCommander\b",
    "Chief": r"\bChief\b",
    "Captain": r"\bCaptain\b",
    "Mr.": r"\bMr\.?\b",
    "Ms.": r"\bMs\.?\b",
    "Mrs.": r"\bMrs\.?\b"
}

results = []

for idx, e in enumerate(entries):
    name = e.get("name", "")
    content = e.get("content", "")
    regex = e.get("avatar_activation_regex", "")
    keys = e.get("keys", [])
    
    bracket_m = re.search(r"\[([^\]]+)\]", content)
    bracket_str = bracket_m.group(1) if bracket_m else ""
    name_m = re.search(r"NAME:\s*([^;]+)", bracket_str)
    jed_name = name_m.group(1).strip() if name_m else name
    role_m = re.search(r"ROLE:\s*([^;]+)", bracket_str)
    jed_role = role_m.group(1).strip() if role_m else ""

    found_titles = set()
    combined_text = f"{name} | {jed_name} | {jed_role} | {regex} | {' '.join(keys)}"
    
    for t, pat in TITLES_PATTERNS.items():
        if re.search(pat, combined_text, re.IGNORECASE):
            # Check context: for instance 'Dean' as a first name vs title
            if t == "Alpha" and "Alpha Rho Omega" in combined_text and name == "Finnegan Novak":
                continue # Fraternity name
            found_titles.add(t)

    if found_titles:
        results.append((idx, name, jed_name, list(found_titles), regex))

print(f"Entries with detected title references ({len(results)}):")
for r in results:
    print(f"[{r[0]:02d}] {r[1]} -> Titles: {r[3]}")
