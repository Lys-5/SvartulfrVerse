import re
import sys

sys.path.append(r'e:\repository\SvartulfrVerse')
from scripts.verify_npc_schema_contract import detect_duplicate_surnames

def build_clean_regex(first_name: str, middle_names: list, last_name: str, nicknames: list, titles: list) -> str:
    variants = []
    
    # 1. Full formal name with titles and middle names
    m_str = " ".join(middle_names).strip()
    if titles:
        for t in titles:
            if m_str and last_name:
                variants.append(f"{t} {first_name} {m_str} {last_name}")
            elif last_name:
                variants.append(f"{t} {first_name} {last_name}")
            else:
                variants.append(f"{t} {first_name}")
                
    if m_str and last_name:
        variants.append(f"{first_name} {m_str} {last_name}")
        
    if last_name:
        variants.append(f"{first_name} {last_name}")
        
    # 2. Nicknames
    for nick in nicknames:
        if not nick or not nick.strip():
            continue
        n = nick.strip()
        # Avoid duplicate surname: if n already ends with or equals last_name, don't append last_name
        if last_name and last_name.strip():
            ln = last_name.strip()
            # check if n ends with ln
            ends_with_ln = re.search(rf"\b{re.escape(ln)}$", n, re.IGNORECASE)
            equals_ln = (n.lower() == ln.lower())
            if not ends_with_ln and not equals_ln:
                variants.append(f"{n} {ln}")
        variants.append(n)
        
    # 3. First name
    if first_name and first_name.strip():
        variants.append(first_name.strip())
        
    # Deduplicate variants while preserving order
    unique_variants = []
    seen = set()
    for v in variants:
        v_clean = re.sub(r'\s+', ' ', v).strip()
        if v_clean and v_clean.lower() not in seen:
            seen.add(v_clean.lower())
            unique_variants.append(v_clean)
            
    # Escape for Wyvern format: e.g. replace space with r'\ ' and special chars
    escaped_items = []
    for uv in unique_variants:
        # Escape regex special chars except we want literal space as '\ '
        esc = ""
        for ch in uv:
            if ch == ' ':
                esc += r'\ '
            elif ch in r".*+?^${}()|[]\-":
                esc += "\\" + ch
            elif ch == '"':
                esc += r'\"'
            else:
                esc += ch
        escaped_items.append(esc)
        
    pattern = rf"(?:^|\n)\s*(?:{'|'.join(escaped_items)})\s*:"
    return pattern

def test_dupe_fixes():
    test_cases = [
        ("Hugh", [], "Rivers", ["Alpha Rivers", "The Mountain Sovereign"], []),
        ("Dominic", ["Wayne"], "Rogers", ["Dom", "Mr. Rogers", "Mr Rogers", "Bailey's Dad"], []),
        ("Daniel", [], "Boone", ["Danny", "Boone"], []),
        ("Harrison", [], "Black", ["Harry", "Councilman Black"], []),
        ("Marcus", [], "O'Connor", ["Mark O'Connor", "Oldtown"], []),
        ("Helena", [], "Weiss", ["Professor Weiss", "Arcadia"], []),
        ("Harlan", [], "Beaumont", ["Huck Beaumont", "Huck"], []),
        ("Federico", [], "Savini", ["Riki", "Federico Savini", "Riki Savini"], []),
        ("Eris", [], "Davies", ["Stan's Mom", "ms davies", "mrs davies"], []),
        ("Elizabeth", [], "Duskwood", ["Lady Duskwood", "nonna"], []),
        ("Alicia", [], "Virtuoso", ["Mrs Virtuoso", "Jean-Luc's wife"], []),
        ("Ariadne", [], "Cirillo", ["Nurse Cirillo", "nurse"], []),
        ("Luisa", [], "Rogers", ["Mac's older sister", "Sanchez Rogers"], []),
        ("Alistair", ["Ambrose"], "DeVille", ["The Collector", "Mr. DeVille", "Ambrose"], []),
        ("Damien", [], "Bishop", ["Bishop", "The Hellhound Detective"], []),
        ("Adelin", [], "Coso", ["Coach Coso"], []),
        ("Marit", [], "Christiansen", ["Professor Marit", "Professor M"], ["Professor"]),
        ("Mollusk", [], "Moreau", ["Professor Mollusk"], ["Professor"]),
        ("Campus", ["Staff"], "Rat", ["Rodent Campus Worker", "SUCC Facilities Staff"], []),
        ("Graham", [], "Purcell", ["Grizzly", "Major Purcell"], []),
    ]
    
    for fn, mn, ln, nicks, titles in test_cases:
        p = build_clean_regex(fn, mn, ln, nicks, titles)
        dupes = detect_duplicate_surnames(p, ln)
        assert len(dupes) == 0, f"Failed for {fn} {ln}: detected {dupes} in {p}"
        print(f"[PASS] Clean regex for {fn} {ln}: {p[:65]}...")

if __name__ == '__main__':
    test_dupe_fixes()
