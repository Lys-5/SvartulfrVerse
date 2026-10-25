import json
import re

primary_data = json.load(open("FINAL/Svartulfr_NPC_Primary.json", encoding="utf-8"))
entries = primary_data["lexicon"]

TITLES_LIST = [
    "Professor", "Prof.", "Dr.", "Doctor", "Jarl", "Lord", "Lady",
    "Alpha", "Beta", "Delta", "Elder", "Chancellor", "Dean",
    "Detective", "Officer", "Captain", "Lieutenant", "Agent",
    "Father", "Reverend", "Pastor", "Coach", "Councilman", "Judge", "Mayor"
]

def parse_npc(entry, idx):
    name = entry.get("name", "").strip()
    content = entry.get("content", "")
    keys = entry.get("keys", [])
    regex = entry.get("avatar_activation_regex", "")
    
    # 1. Parse JED+ bracket block
    bracket_m = re.search(r"\[([^\]]+)\]", content)
    bracket_text = bracket_m.group(1) if bracket_m else ""
    attrs = {}
    if bracket_text:
        for part in re.split(r";\s*", bracket_text):
            if ":" in part:
                k, v = part.split(":", 1)
                attrs[k.strip().upper()] = v.strip()
    
    jed_name = attrs.get("NAME", name).strip()
    
    # Extract titles from name / jed_name / keys / regex
    found_titles = []
    
    # Check regex for titles (e.g. Professor\ Weiss)
    for t in TITLES_LIST:
        escaped_t = t.replace(".", r"\.")
        if re.search(rf"\b{t}\b", jed_name, re.IGNORECASE) or re.search(rf"\b{t}\b", name, re.IGNORECASE) or re.search(rf"\b{escaped_t}\b", regex, re.IGNORECASE):
            if t not in found_titles:
                found_titles.append(t)
    
    # Clean titles out of base name
    clean_name = jed_name
    for t in TITLES_LIST:
        clean_name = re.sub(rf"^\s*{re.escape(t)}\s+", "", clean_name, flags=re.IGNORECASE).strip()
    
    # Extract nicknames from quotes or parentheses, or keys
    nicknames = []
    # Check for quotes in jed_name or name: e.g. Daniel "Danny" Boone, Russell 'Russ' Sinclair
    quote_matches = re.findall(r'["\']([^"\']+)["\']', jed_name) or re.findall(r'["\']([^"\']+)["\']', name)
    for q in quote_matches:
        if q not in nicknames:
            nicknames.append(q)
            
    # Remove quotes from clean_name
    clean_name = re.sub(r'["\'][^"\']+["\']\s*', "", clean_name).strip()
    
    return {
        "index": idx,
        "entry_name": name,
        "jed_name": jed_name,
        "clean_name": clean_name,
        "titles": found_titles,
        "nicknames": nicknames,
        "keys": keys,
        "regex": regex
    }

parsed_all = [parse_npc(e, i) for i, e in enumerate(entries)]

print(f"Total entries: {len(parsed_all)}")
for p in parsed_all:
    print(f"[{p['index']:02d}] Entry: '{p['entry_name']}' | JED: '{p['jed_name']}' | Clean: '{p['clean_name']}' | Titles: {p['titles']} | Nicks: {p['nicknames']}")
