import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

def run_adversarial_audit():
    print("=" * 70)
    print("REVIEWER 3 DEEP ADVERSARIAL AUDIT")
    print("=" * 70)
    issues = []

    # 1. FINAL CARDS
    final_cards = [
        ('Edric_Douglas_card.json', 'AGE: 13 (Born February 25, 2011)'),
        ('Erik_Douglas_card.json', 'AGE: 55 (Born October 31, 1969)'),
        ('Jasper_Douglas_Bloodmoon_card.json', 'AGE: 19 (Born April 22, 2005)'),
        ('Logan_Douglas_card.json', 'AGE: 49 (Born January 12, 1975)'),
        ('Mackenzie_Sanchez_Rogers_card.json', 'AGE: 19 (Born November 14, 2004)'),
        ('Malachia_Douglas_Bloodmoon_card.json', 'AGE: 28 (Born August 10, 1996)'),
        ('Noah_Douglas_Bloodmoon_card.json', 'AGE: 25 (Born October 5, 1998)'),
        ('Wulfnic_Bloodmoon_card.json', 'AGE: 1200 (Born December 21, 824 AD)'),
    ]

    for fname, expected_age in final_cards:
        p = ROOT / 'FINAL' / fname
        d = json.loads(p.read_text(encoding='utf-8'))
        desc = d.get('description', '')
        line1 = desc.split('\n')[0]
        if not line1.startswith('[') or not line1.endswith(']'):
            issues.append(f"{fname}: Line 1 not in [...] brackets")
        if expected_age not in line1:
            issues.append(f"{fname}: Expected '{expected_age}' not found in line 1")
        if '\n' in line1:
            issues.append(f"{fname}: Line 1 contains newline")
        
        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find('FAMILY & PACK:')
        idx_v = desc.find('VOICE & BEHAVIOR:')
        if idx_b == -1 or idx_f == -1 or idx_v == -1:
            issues.append(f"{fname}: Missing one of 3 mandatory narrative headers")
        elif not (idx_b < idx_f < idx_v):
            issues.append(f"{fname}: Canonical header order violated")

        pers = d.get('personality', '').strip()
        if not (pers.startswith('[') and pers.endswith(']')):
            issues.append(f"{fname}: Personality not enclosed in [...]")
        if pers.endswith(',') or pers.endswith('...'):
            issues.append(f"{fname}: Personality appears truncated")
        for req_k in ['NAME:', 'ROLE:', 'TRAITS:', 'CORE:']:
            if req_k not in pers:
                issues.append(f"{fname}: Personality missing key '{req_k}'")

        for fld in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = d.get(fld, '')
            if isinstance(val, str):
                if '—' in val:
                    issues.append(f"{fname}: em-dash in {fld}")
                if '*' in val:
                    issues.append(f"{fname}: asterisk in {fld}")

    # 2. PERSONAS
    personas = [
        ('Alyssa_Persona.json', 'AGE: 19 (Born April 22, 2005)'),
        ('Echo_Persona.json', 'AGE: 3 (Activated November 15, 2021)'),
        ('Jasper_Persona.json', 'AGE: 19 (Born April 22, 2005)'),
    ]
    for fname, expected_age in personas:
        p = ROOT / 'FINAL' / 'personas' / fname
        d = json.loads(p.read_text(encoding='utf-8'))
        desc = d.get('description', '')
        line1 = desc.split('\n')[0]
        if not line1.startswith('[') or not line1.endswith(']'):
            issues.append(f"{fname}: Line 1 not in [...] brackets")
        if expected_age not in line1:
            issues.append(f"{fname}: Expected '{expected_age}' not found in line 1")
        if d.get('can_fork') is not True:
            issues.append(f"{fname}: can_fork is not True")
        
        # Scansione testo
        def scan(obj, path):
            if isinstance(obj, str):
                if '—' in obj:
                    issues.append(f"{fname}: em-dash in {path}")
                if '*' in obj:
                    issues.append(f"{fname}: asterisk in {path}")
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    if k not in ['id', '_id', 'avatar', 'backgroundURL', 'image_url']:
                        scan(v, f"{path}.{k}" if path else k)
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    scan(v, f"{path}[{i}]")
        scan(d, "")

    # 3. LEGACY CARDS
    legacy = [
        ('Alyssa_Douglas_Bloodmoon_card.json', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
        ('Jared_Thompson_card.json', 'AGE: 22 (Born March 24, 2002)', 'FAMILY & PACK:'),
        ('Russ_card.json', 'AGE: 21 (Born March 14, 2003)', 'CLAN AND COMPANY:'),
        ('Scarlett_Rose_card.json', 'AGE: 20 (Born November 18, 2003)', 'CLAN AND COMPANY:'),
        ('Sierra_Cruz_card.json', 'AGE: 18 (Born September 8, 2005)', 'CLAN AND COMPANY:'),
        ('Stan_Davies_Jr_card.json', 'AGE: 21 (Born September 14, 2002)', 'FAMILY & PACK:'),
    ]
    for fname, expected_age, expected_fam in legacy:
        p = ROOT / 'ARCHIVIO' / 'cards_legacy' / fname
        d = json.loads(p.read_text(encoding='utf-8'))
        desc = d.get('description', '')
        line1 = desc.split('\n')[0]
        if not line1.startswith('[') or not line1.endswith(']'):
            issues.append(f"Legacy {fname}: Line 1 not in [...]")
        if expected_age not in line1:
            issues.append(f"Legacy {fname}: Missing '{expected_age}' in line 1")
        if expected_fam not in desc:
            issues.append(f"Legacy {fname}: Missing '{expected_fam}'")
        if 'Jared' in fname and desc.count('FAMILY & PACK:') != 1:
            issues.append(f"Legacy {fname}: Duplicate FAMILY & PACK:")
        pers = d.get('personality', '').strip()
        if not (pers.startswith('[') and pers.endswith(']')):
            issues.append(f"Legacy {fname}: Personality not in [...]")

    # 4. LOREBOOKS INVARIANTS & 1:1 MATCHES
    core_cards = [
        ('Erik_Douglas_card.json', 'C-JisFj8qA1tsFEqZKevk', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Malachia_Douglas_Bloodmoon_card.json', 'jDuJtzirlEZC3K_ArIufh', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Noah_Douglas_Bloodmoon_card.json', 'H2JX-NkHRiJ2FzoekC5ZZ', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Logan_Douglas_card.json', 'tAcrWLtWSDGf3xJJRwUOM', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Wulfnic_Bloodmoon_card.json', 'HhuMluMmIIENUei3bX6ed', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Mackenzie_Sanchez_Rogers_card.json', 'BXi3sENAVYB8OKF80Q9Su', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Edric_Douglas_card.json', 'h-ttmlgJYeRXqyDvQjSX7', 'FINAL/Svartulfr_NPC_Secondary.json'),
    ]
    for cfile, eid, lbfile in core_cards:
        c_desc = json.loads((ROOT / 'FINAL' / cfile).read_text(encoding='utf-8'))['description']
        for base in [ROOT, ROOT / 'lorebooks' / 'optimized']:
            target_path = base / pathlib.Path(lbfile).name if base != ROOT else ROOT / lbfile
            lb = json.loads(target_path.read_text(encoding='utf-8'))
            e_lex = next((x for x in lb['lexicon'] if x.get('entry_id') == eid), None)
            e_ent = next((x for x in lb['entries'] if x.get('entry_id') == eid), None)
            if not e_lex or e_lex.get('content') != c_desc:
                issues.append(f"1:1 mismatch in {target_path} lexicon for {cfile}")
            if not e_ent or e_ent.get('content') != c_desc:
                issues.append(f"1:1 mismatch in {target_path} entries for {cfile}")

    for name in ['Svartulfr_Location.json', 'Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
        for folder in ['FINAL', 'lorebooks/optimized']:
            p = ROOT / folder / name
            d = json.loads(p.read_text(encoding='utf-8'))
            if d['entries'] != d['lexicon']:
                issues.append(f"entries != lexicon in {p}")

    # 5. FIRSTBORN DATES & FORBIDDEN STRINGS
    for p in (ROOT / 'FINAL').glob('*.json'):
        txt = p.read_text(encoding='utf-8')
        for forbidden in ['1005 AD', '1005 d.C.', '823 AD', '823 d.C.', 'pre-827 AD']:
            if forbidden in txt:
                issues.append(f"Forbidden string '{forbidden}' found in {p.name}")

    if issues:
        print(f"\nAUDIT FAILED! {len(issues)} ISSUES DETECTED:")
        for idx, iss in enumerate(issues, 1):
            print(f"  {idx}. {iss}")
        return False
    else:
        print("\nALL ADVERSARIAL CHECKS PASSED WITH 0 ISSUES!")
        return True

if __name__ == '__main__':
    ok = run_adversarial_audit()
    exit(0 if ok else 1)
