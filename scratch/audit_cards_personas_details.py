import json
import glob
import re

print("=== 8 CARDS IN FINAL/ ===")
for p in sorted(glob.glob("FINAL/*_card.json")):
    d = json.load(open(p, encoding="utf-8"))
    desc = d.get("description", "")
    pers = d.get("personality", "")
    first_mes = d.get("first_mes", "")
    mes_ex = d.get("mes_example", "")
    phi = d.get("post_history_instructions", "")
    m_br = re.match(r"^\s*\[(.*?)\]", desc, flags=re.S)
    br_text = m_br.group(1) if m_br else ""
    br_newlines = br_text.count("\n")
    has_emdash = ("—" in desc) or ("—" in pers) or ("—" in first_mes) or ("—" in mes_ex)
    has_ast = ("*" in desc) or ("*" in pers) or ("*" in first_mes) or ("*" in mes_ex)
    print(f"CARD {p}:")
    print(f"  desc_len={len(desc)}, bracket_newlines={br_newlines}, pers_starts_bracket={pers.lstrip().startswith('[')}, pers_len={len(pers)}")
    print(f"  has_emdash={has_emdash}, has_ast={has_ast}, phi_has_format_rule={'Never use the em dash' in phi}")
    # Check AGE format in bracket
    m_age = re.search(r"AGE:\s*([^;\]]+)", br_text)
    print(f"  AGE field in bracket: {m_age.group(0) if m_age else None}")

print("\n=== 3 PERSONAS IN FINAL/personas/ ===")
for p in sorted(glob.glob("FINAL/personas/*.json")):
    d = json.load(open(p, encoding="utf-8"))
    desc = d.get("description", "")
    m_br = re.match(r"^\s*\[(.*?)\]", desc, flags=re.S)
    br_text = m_br.group(1) if m_br else ""
    br_newlines = br_text.count("\n")
    has_bs = "BACKSTORY:" in desc
    has_fp = ("FAMILY & PACK:" in desc) or ("CLAN AND COMPANY:" in desc)
    has_vb = "VOICE & BEHAVIOR:" in desc
    has_emdash = "—" in desc
    has_ast = "*" in desc
    m_age = re.search(r"AGE:\s*([^;\]]+)", br_text)
    print(f"PERSONA {p} ({d.get('name')}):")
    print(f"  desc_len={len(desc)}, bracket_newlines={br_newlines}, bs={has_bs}, fp={has_fp}, vb={has_vb}")
    print(f"  has_emdash={has_emdash}, has_ast={has_ast}, AGE={m_age.group(0) if m_age else None}")
