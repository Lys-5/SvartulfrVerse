import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

def deep_audit():
    print("=" * 80)
    print("REVIEWER ADVERSARIAL DEEP AUDIT")
    print("=" * 80)

    # 1. Gather all files
    final_cards = sorted(list((ROOT / 'FINAL').glob('*_card.json')))
    personas = sorted(list((ROOT / 'FINAL' / 'personas').glob('*.json')))
    legacy_cards = sorted(list((ROOT / 'ARCHIVIO' / 'cards_legacy').glob('*_card.json')))
    all_files = final_cards + personas + legacy_cards

    print(f"Total files: {len(all_files)} (8 Final, {len(personas)} Personas, {len(legacy_cards)} Legacy)")

    issues = []

    # Check 1: Format discipline violations across ALL fields
    target_fields = ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']
    
    def check_obj(obj, path, fname):
        if isinstance(obj, str):
            if '—' in obj:
                issues.append(f"[EM-DASH in {path}] {fname} contains '—': {obj[:100]}")
            if '*' in obj and not path.endswith('.png') and not path.endswith('.jpg'):
                # Note: only flag asterisks in text fields, not regex or markdown if intentional, but check
                issues.append(f"[ASTERISK in {path}] {fname} contains '*': {obj[:100]}")
        elif isinstance(obj, dict):
            for k, v in obj.items():
                check_obj(v, f"{path}.{k}" if path else k, fname)
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                check_obj(item, f"{path}[{idx}]", fname)

    for f in all_files:
        d = json.loads(f.read_text(encoding='utf-8'))
        check_obj(d, "", f.name)

    # Check 2: Canonical line 1 bracket
    expected_ages = {
        'Edric_Douglas_card.json': 'AGE: 13 (Born February 25, 2011)',
        'Erik_Douglas_card.json': 'AGE: 55 (Born October 31, 1969)',
        'Jasper_Douglas_Bloodmoon_card.json': 'AGE: 19 (Born April 22, 2005)',
        'Logan_Douglas_card.json': 'AGE: 49 (Born January 12, 1975)',
        'Mackenzie_Sanchez_Rogers_card.json': 'AGE: 19 (Born November 14, 2004)',
        'Malachia_Douglas_Bloodmoon_card.json': 'AGE: 28 (Born August 10, 1996)',
        'Noah_Douglas_Bloodmoon_card.json': 'AGE: 25 (Born October 5, 1998)',
        'Wulfnic_Bloodmoon_card.json': 'AGE: 1197 (Born December 21, 827 AD)',
        'Echo_Persona.json': 'AGE: 3 (Activated November 15, 2021)',
        'Alyssa_Persona.json': 'AGE: 19 (Born April 22, 2005)',
        'Jasper_Persona.json': 'AGE: 19 (Born April 22, 2005)',
        'Alyssa_Douglas_Bloodmoon_card.json': 'AGE: 19 (Born April 22, 2005)',
        'Jared_Thompson_card.json': 'AGE: 22 (Born March 24, 2002)',
        'Russ_card.json': 'AGE: 21 (Born March 14, 2003)',
        'Scarlett_Rose_card.json': 'AGE: 20 (Born November 18, 2003)',
        'Sierra_Cruz_card.json': 'AGE: 18 (Born September 8, 2005)',
        'Stan_Davies_Jr_card.json': 'AGE: 21 (Born September 14, 2002)',
    }

    print("\n--- Checking Canonical Line 1 Bracket and AGE ---")
    for f in all_files:
        d = json.loads(f.read_text(encoding='utf-8'))
        desc = d.get('description', '')
        lines = desc.split('\n')
        line1 = lines[0].strip()
        if not line1.startswith('['):
            issues.append(f"[Line 1 not starting with '['] {f.name}")
        if not line1.endswith(']'):
            issues.append(f"[Line 1 not ending with ']'] {f.name}: {line1[-30:]}")
        if '\n' in line1:
            issues.append(f"[Line 1 contains newline] {f.name}")
            
        exp_age = expected_ages.get(f.name)
        if exp_age:
            if exp_age not in line1:
                issues.append(f"[AGE mismatch in line 1] {f.name}: expected '{exp_age}' not in line 1: {line1[:200]}")
        else:
            issues.append(f"[Unknown file age requirement] {f.name}")

    # Check 3: Canonical 4 Blocks Order
    print("\n--- Checking Canonical 4 Blocks Order ---")
    for f in all_files:
        d = json.loads(f.read_text(encoding='utf-8'))
        desc = d.get('description', '')
        
        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find('FAMILY & PACK:')
        if idx_f == -1:
            idx_f = desc.find('CLAN AND COMPANY:')
            fam_key = 'CLAN AND COMPANY:'
        else:
            fam_key = 'FAMILY & PACK:'
        idx_v = desc.find('VOICE & BEHAVIOR:')
        
        if idx_b == -1:
            issues.append(f"[Missing BACKSTORY:] {f.name}")
        if idx_f == -1:
            issues.append(f"[Missing FAMILY & PACK / CLAN AND COMPANY:] {f.name}")
        if idx_v == -1:
            issues.append(f"[Missing VOICE & BEHAVIOR:] {f.name}")
            
        if idx_b != -1 and idx_f != -1 and idx_v != -1:
            if not (idx_b < idx_f < idx_v):
                issues.append(f"[Order violation] {f.name}: BACKSTORY({idx_b}) < {fam_key}({idx_f}) < VOICE & BEHAVIOR({idx_v})")

        # Check for duplicate headers
        for h in ['BACKSTORY:', 'FAMILY & PACK:', 'CLAN AND COMPANY:', 'VOICE & BEHAVIOR:']:
            cnt = desc.count(h)
            if cnt > 1:
                issues.append(f"[Duplicate header '{h}'] {f.name}: count = {cnt}")

    # Check 4: Personality formatting for cards
    print("\n--- Checking Personality formatting ---")
    for f in final_cards + legacy_cards:
        d = json.loads(f.read_text(encoding='utf-8'))
        pers = d.get('personality', '').strip()
        if not (pers.startswith('[') and pers.endswith(']')):
            issues.append(f"[Personality not enclosed in [...]] {f.name}: {pers[:40]}...{pers[-20:]}")
        if pers.endswith(','):
            issues.append(f"[Personality ends with comma] {f.name}")
        if pers.endswith('...'):
            issues.append(f"[Personality ends with ellipsis] {f.name}")
        for req_k in ['NAME:', 'ROLE:', 'TRAITS:', 'CORE:']:
            if req_k not in pers:
                issues.append(f"[Personality missing key '{req_k}'] {f.name}")

    # Check 5: Lorebook 1:1 Parity
    print("\n--- Checking Lorebook 1:1 Parity ---")
    core_cards = [
        ('Erik_Douglas_card.json', 'C-JisFj8qA1tsFEqZKevk', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Malachia_Douglas_Bloodmoon_card.json', 'jDuJtzirlEZC3K_ArIufh', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Noah_Douglas_Bloodmoon_card.json', 'H2JX-NkHRiJ2FzoekC5ZZ', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Logan_Douglas_card.json', 'tAcrWLtWSDGf3xJJRwUOM', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Wulfnic_Bloodmoon_card.json', 'HhuMluMmIIENUei3bX6ed', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Mackenzie_Sanchez_Rogers_card.json', 'BXi3sENAVYB8OKF80Q9Su', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Edric_Douglas_card.json', 'h-ttmlgJYeRXqyDvQjSX7', 'FINAL/Svartulfr_NPC_Secondary.json'),
    ]

    for card_fname, entry_id, lb_rel in core_cards:
        card_desc = json.loads((ROOT / 'FINAL' / card_fname).read_text(encoding='utf-8'))['description']
        lb_data = json.loads((ROOT / lb_rel).read_text(encoding='utf-8'))
        entry = next((e for e in lb_data['lexicon'] if e['entry_id'] == entry_id), None)
        if not entry:
            issues.append(f"[Lorebook entry missing] {entry_id} in {lb_rel}")
        elif entry['content'] != card_desc:
            issues.append(f"[Lorebook content mismatch] {card_fname} vs {entry_id} in {lb_rel}")

        opt_path = ROOT / 'lorebooks' / 'optimized' / pathlib.Path(lb_rel).name
        opt_data = json.loads(opt_path.read_text(encoding='utf-8'))
        opt_entry = next((e for e in opt_data['lexicon'] if e['entry_id'] == entry_id), None)
        if not opt_entry:
            issues.append(f"[Optimized Lorebook entry missing] {entry_id} in {opt_path}")
        elif opt_entry['content'] != card_desc:
            issues.append(f"[Optimized Lorebook content mismatch] {card_fname} vs {entry_id} in {opt_path}")

    # Summary
    print("\n" + "=" * 80)
    print(f"AUDIT SUMMARY: {len(issues)} ISSUES DETECTED")
    print("=" * 80)
    for iss in issues:
        print("  - " + iss)
    return issues

if __name__ == '__main__':
    deep_audit()
