#!/usr/bin/env python3
"""
Extract verified 6-section outfit text from Explorer 2 handoff and apply to Mackenzie cards.
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPLORER_HANDOFF = Path(r"C:\Users\mande\.gemini\antigravity\scratch\teamwork\1d44e78a-e2f9-4540-bf0e-8718f0dca4cd\.agents\teamwork\explorer_m4_it2_2\handoff.md")

def main():
    content = EXPLORER_HANDOFF.read_text(encoding="utf-8")
    
    # Extract Modern Mackenzie text from section 4.1
    # Between lines starting with "Abbigliamento: Nessuno. Completo nudo anatomico naturale. Mastodontica corporatura maschile da 204 cm"
    # and ending before "```"
    s1_marker = "### 4.1 Solution for `FINAL/Mackenzie_Sanchez_Rogers_card.json`"
    s2_marker = "### 4.2 Solution for `FINAL/Mackenzie_Fantasy_card.json`"
    s3_marker = "### 4.3 Hardening Recommendation"
    
    part_modern = content.split(s1_marker)[1].split(s2_marker)[0]
    modern_code_block = part_modern.split("```text\n")[1].split("\n```")[0]
    
    part_fantasy = content.split(s2_marker)[1].split(s3_marker)[0]
    fantasy_code_block = part_fantasy.split("```text\n")[1].split("\n```")[0]
    
    print(f"Modern text extracted: {len(modern_code_block)} chars")
    print(f"Fantasy text extracted: {len(fantasy_code_block)} chars")
    
    # Validate required headers
    req = ['Abbigliamento:', 'Accessori:', 'Scarpe:', 'Gioielli:', 'Trucco:', 'Acconciatura:']
    for name, text in [("Modern", modern_code_block), ("Fantasy", fantasy_code_block)]:
        missing = [r for r in req if r not in text]
        if missing:
            raise ValueError(f"{name} is missing sections: {missing}")
        if len(text) < 250:
            raise ValueError(f"{name} length too short: {len(text)}")
        if '—' in text or '–' in text:
            raise ValueError(f"{name} contains forbidden dashes")
    
    # Update FINAL/Mackenzie_Sanchez_Rogers_card.json
    modern_path = REPO_ROOT / "FINAL" / "Mackenzie_Sanchez_Rogers_card.json"
    with open(modern_path, "r", encoding="utf-8") as f:
        modern_data = json.load(f)
    
    updated_modern = False
    for outfit in modern_data.get("outfits", []):
        if outfit.get("id") == "nude" or any(w in outfit.get("name", "").lower() for w in ["nude", "nudo"]):
            outfit["description"] = modern_code_block
            updated_modern = True
            break
    if not updated_modern:
        raise ValueError("Could not find nude outfit in Mackenzie_Sanchez_Rogers_card.json")
    
    with open(modern_path, "w", encoding="utf-8") as f:
        json.dump(modern_data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Updated {modern_path}")
    
    # Update FINAL/Mackenzie_Fantasy_card.json
    fantasy_path = REPO_ROOT / "FINAL" / "Mackenzie_Fantasy_card.json"
    with open(fantasy_path, "r", encoding="utf-8") as f:
        fantasy_data = json.load(f)
        
    updated_fantasy = False
    for outfit in fantasy_data.get("outfits", []):
        if outfit.get("id") == "nude" or any(w in outfit.get("name", "").lower() for w in ["nude", "nudo"]):
            outfit["description"] = fantasy_code_block
            updated_fantasy = True
            break
    if not updated_fantasy:
        raise ValueError("Could not find nude outfit in Mackenzie_Fantasy_card.json")
        
    with open(fantasy_path, "w", encoding="utf-8") as f:
        json.dump(fantasy_data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Updated {fantasy_path}")

if __name__ == "__main__":
    main()
