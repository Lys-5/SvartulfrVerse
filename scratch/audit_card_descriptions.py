import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
final_dir = ROOT / 'FINAL'

cards = {
    'Scarlett Rose': final_dir / 'Scarlett_Rose_card.json',
    'Sierra Cruz': final_dir / 'Sierra_Cruz_card.json',
    "Russell 'Russ' Sinclair": final_dir / 'Russ_card.json',
    'Stanley Davies Jr.': final_dir / 'Stan_Davies_Jr_card.json',
    'Jared Thompson': final_dir / 'Jared_Thompson_card.json',
    'Alyssa Hvit Douglas Bloodmoon': final_dir / 'Alyssa_Douglas_Bloodmoon_card.json'
}

print("=== AUDITING SOURCE CARD DESCRIPTIONS FOR COMPLIANCE ===")

for name, path in cards.items():
    d = json.load(open(path, 'r', encoding='utf-8'))
    desc = d.get('description', '')
    
    print(f"\n--- {name} ({path.name}) ---")
    print(f"Length: {len(desc)} characters")
    
    # 1. Em-dash check
    em_dashes = [m.start() for m in re.finditer(r'—', desc)]
    print(f"Em-dashes found: {len(em_dashes)}")
    if em_dashes:
        for pos in em_dashes[:3]:
            print(f"   Context: {repr(desc[max(0, pos-20):min(len(desc), pos+20)])}")
            
    # 2. Asterisk check (actions or bolding)
    asterisks = [m.start() for m in re.finditer(r'\*', desc)]
    print(f"Asterisks found: {len(asterisks)}")
    if asterisks:
        for pos in asterisks[:3]:
            print(f"   Context: {repr(desc[max(0, pos-20):min(len(desc), pos+20)])}")
            
    # 3. Macro check ({{user}}, {{age}}, {{char}})
    user_macros = re.findall(r'\{\{.*?\}\}', desc)
    print(f"Macros found: {len(user_macros)} -> {user_macros}")
    
    # 4. Non-ASCII or corrupted characters (like )
    corrupted = [m.start() for m in re.finditer(r'', desc)]
    print(f"Corrupted characters (): {len(corrupted)}")
    if corrupted:
        for pos in corrupted[:3]:
            print(f"   Context: {repr(desc[max(0, pos-20):min(len(desc), pos+20)])}")
            
    # 5. Check JED+ structure
    has_bracket = desc.strip().startswith('[')
    has_backstory = 'BACKSTORY:' in desc
    print(f"JED+ bracket start: {has_bracket}, has BACKSTORY: {has_backstory}")
