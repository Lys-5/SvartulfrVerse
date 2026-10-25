import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

def verify_all_local():
    print("=" * 70)
    print("COMPREHENSIVE LOCAL VERIFICATION SUITE")
    print("=" * 70)

    # 1. 8 FINAL CARDS
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

    print("\n--- Testing 8 Final Cards ---")
    for fname, expected_age in final_cards:
        p = ROOT / 'FINAL' / fname
        d = json.loads(p.read_text(encoding='utf-8'))
        desc = d['description']
        lines = desc.split('\n')
        line1 = lines[0]
        
        # Check line 1 starts with [ and ends with ]
        assert line1.startswith('['), f"{fname}: Line 1 does not start with ["
        assert line1.endswith(']'), f"{fname}: Line 1 does not end with ]: {line1[-30:]}"
        assert '\n' not in line1, f"{fname}: Line 1 contains newline"
        
        # Check expected AGE
        assert expected_age in line1, f"{fname}: Expected '{expected_age}' not found in line 1: {line1[:200]}"
        
        # Check canonical 4-block headers
        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find('FAMILY & PACK:')
        idx_v = desc.find('VOICE & BEHAVIOR:')
        assert idx_b != -1, f"{fname}: Missing BACKSTORY:"
        assert idx_f != -1, f"{fname}: Missing FAMILY & PACK:"
        assert idx_v != -1, f"{fname}: Missing VOICE & BEHAVIOR:"
        assert idx_b < idx_f < idx_v, f"{fname}: Order violation: BACKSTORY({idx_b}) < FAMILY & PACK({idx_f}) < VOICE & BEHAVIOR({idx_v})"
        
        # Check personality
        pers = d['personality'].strip()
        assert pers.startswith('[') and pers.endswith(']'), f"{fname}: Personality not in [...]: {pers[:50]}...{pers[-20:]}"
        assert not pers.endswith(','), f"{fname}: Personality ends with comma (truncated): {pers[-30:]}"
        assert not pers.endswith('...'), f"{fname}: Personality ends with ellipsis: {pers[-30:]}"
        assert 'NAME:' in pers, f"{fname}: Personality missing NAME:"
        assert 'ROLE:' in pers, f"{fname}: Personality missing ROLE:"
        assert 'TRAITS:' in pers, f"{fname}: Personality missing TRAITS:"
        assert 'CORE:' in pers, f"{fname}: Personality missing CORE:"
        assert expected_age in pers, f"{fname}: Expected '{expected_age}' not found in personality: {pers[:200]}"
        
        # Formatting discipline
        for field in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = d.get(field, '')
            if isinstance(val, str):
                assert '—' not in val, f"{fname}: em-dash found in {field}"
                assert '*' not in val, f"{fname}: asterisk found in {field}: {val[val.find('*')-20:val.find('*')+20]}"
        
        # Check format clause in phi
        phi = d.get('post_history_instructions', '')
        assert 'Format discipline:' in phi or 'Format discipline' in phi, f"{fname}: Missing format discipline in phi"
        
        print(f"  PASS: {fname}")

    # 2. 3 PERSONAS
    personas = [
        ('Alyssa_Persona.json', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
        ('Echo_Persona.json', 'AGE: 3 (Activated November 15, 2021)', 'FAMILY & PACK:'),
        ('Jasper_Persona.json', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
    ]

    print("\n--- Testing 3 User Personas ---")
    for fname, expected_age, expected_fam in personas:
        p = ROOT / 'FINAL' / 'personas' / fname
        d = json.loads(p.read_text(encoding='utf-8'))
        desc = d['description']
        lines = desc.split('\n')
        line1 = lines[0]
        
        assert line1.startswith('['), f"{fname}: Line 1 does not start with ["
        assert line1.endswith(']'), f"{fname}: Line 1 does not end with ]"
        assert expected_age in line1, f"{fname}: Expected '{expected_age}' not found in line 1"
        
        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find(expected_fam)
        idx_v = desc.find('VOICE & BEHAVIOR:')
        assert idx_b != -1, f"{fname}: Missing BACKSTORY:"
        assert idx_f != -1, f"{fname}: Missing {expected_fam}"
        assert idx_v != -1, f"{fname}: Missing VOICE & BEHAVIOR:"
        assert idx_b < idx_f < idx_v, f"{fname}: Order violation: BACKSTORY < FAMILY/CLAN < VOICE & BEHAVIOR"
        
        assert d.get('can_fork') is True, f"{fname}: can_fork is not True"
        
        def scan_text(obj, path):
            if isinstance(obj, str):
                assert '—' not in obj, f"{fname}: em-dash found in {path}: {obj[:40]}"
                assert '*' not in obj, f"{fname}: asterisk found in {path}: {obj[:40]}"
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    if k not in ['id', '_id', 'avatar', 'backgroundURL', 'image_url']:
                        scan_text(v, f"{path}.{k}" if path else k)
            elif isinstance(obj, list):
                for idx, item in enumerate(obj):
                    scan_text(item, f"{path}[{idx}]")

        scan_text(d, "")
            
        print(f"  PASS: {fname}")

    # 3. 6 LEGACY CARDS
    legacy_cards = [
        ('Alyssa_Douglas_Bloodmoon_card.json', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
        ('Jared_Thompson_card.json', 'AGE: 22 (Born March 24, 2002)', 'FAMILY & PACK:'),
        ('Russ_card.json', 'AGE: 21 (Born March 14, 2003)', 'CLAN AND COMPANY:'),
        ('Scarlett_Rose_card.json', 'AGE: 20 (Born November 18, 2003)', 'CLAN AND COMPANY:'),
        ('Sierra_Cruz_card.json', 'AGE: 18 (Born September 8, 2005)', 'CLAN AND COMPANY:'),
        ('Stan_Davies_Jr_card.json', 'AGE: 21 (Born September 14, 2002)', 'FAMILY & PACK:'),
    ]

    print("\n--- Testing 6 Legacy Cards ---")
    for fname, expected_age, expected_fam in legacy_cards:
        p = ROOT / 'ARCHIVIO' / 'cards_legacy' / fname
        d = json.loads(p.read_text(encoding='utf-8'))
        desc = d['description']
        lines = desc.split('\n')
        line1 = lines[0]
        
        assert line1.startswith('['), f"{fname}: Line 1 does not start with ["
        assert line1.endswith(']'), f"{fname}: Line 1 does not end with ]"
        assert expected_age in line1, f"{fname}: Expected '{expected_age}' not found in line 1"
        
        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find(expected_fam)
        idx_v = desc.find('VOICE & BEHAVIOR:')
        assert idx_b != -1, f"{fname}: Missing BACKSTORY:"
        assert idx_f != -1, f"{fname}: Missing {expected_fam}"
        assert idx_v != -1, f"{fname}: Missing VOICE & BEHAVIOR:"
        assert idx_b < idx_f < idx_v, f"{fname}: Order violation in {fname}: BACKSTORY < {expected_fam} < VOICE & BEHAVIOR"
        
        # Check no duplicate FAMILY in Jared
        if 'Jared' in fname:
            assert desc.count('FAMILY & PACK:') == 1, f"Jared has multiple FAMILY & PACK:"
            m = re.findall(r'^FAMILY:\s*', desc, flags=re.M)
            assert len(m) == 0, f"Jared still has standalone FAMILY: header!"
            
        pers = d['personality'].strip()
        assert pers.startswith('[') and pers.endswith(']'), f"{fname}: Personality not in [...]: {pers[:50]}"
        assert not pers.endswith(','), f"{fname}: Personality ends with comma"
        
        for field in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = d.get(field, '')
            if isinstance(val, str):
                assert '—' not in val, f"{fname}: em-dash found in {field}"
                assert '*' not in val, f"{fname}: asterisk found in {field}"
                
        print(f"  PASS: {fname}")

    # 4. LOREBOOK 1:1 SYNC & ENTRIES/LEXICON INTEGRITY
    core_cards = [
        ('Erik_Douglas_card.json', 'C-JisFj8qA1tsFEqZKevk', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Malachia_Douglas_Bloodmoon_card.json', 'jDuJtzirlEZC3K_ArIufh', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Noah_Douglas_Bloodmoon_card.json', 'H2JX-NkHRiJ2FzoekC5ZZ', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Logan_Douglas_card.json', 'tAcrWLtWSDGf3xJJRwUOM', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Wulfnic_Bloodmoon_card.json', 'HhuMluMmIIENUei3bX6ed', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Mackenzie_Sanchez_Rogers_card.json', 'BXi3sENAVYB8OKF80Q9Su', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Edric_Douglas_card.json', 'h-ttmlgJYeRXqyDvQjSX7', 'FINAL/Svartulfr_NPC_Secondary.json'),
    ]

    print("\n--- Testing 1:1 Parity between 7 Core Cards and Lorebooks (Entries AND Lexicon) ---")
    for card_file, entry_id, lb_file in core_cards:
        card_desc = json.loads((ROOT / card_file).read_text(encoding='utf-8') if (ROOT / card_file).exists() else (ROOT / 'FINAL' / card_file).read_text(encoding='utf-8'))['description']
        lb_data = json.loads((ROOT / lb_file).read_text(encoding='utf-8'))
        
        # Verify in lexicon
        lex_entry = next((e for e in lb_data['lexicon'] if e.get('entry_id') == entry_id), None)
        assert lex_entry is not None, f"Entry {entry_id} not found in {lb_file} lexicon"
        assert lex_entry['content'] == card_desc, f"Mismatch 1:1 for {card_file} in {lb_file} lexicon!"
        
        # Verify in entries
        ent_entry = next((e for e in lb_data['entries'] if e.get('entry_id') == entry_id), None)
        assert ent_entry is not None, f"Entry {entry_id} not found in {lb_file} entries"
        assert ent_entry['content'] == card_desc, f"Mismatch 1:1 for {card_file} in {lb_file} entries!"
        
        # Verify in optimized mirror
        opt_lb_file = ROOT / 'lorebooks' / 'optimized' / pathlib.Path(lb_file).name
        opt_lb_data = json.loads(opt_lb_file.read_text(encoding='utf-8'))
        opt_lex_entry = next((e for e in opt_lb_data['lexicon'] if e.get('entry_id') == entry_id), None)
        assert opt_lex_entry is not None, f"Entry {entry_id} not found in optimized {opt_lb_file} lexicon"
        assert opt_lex_entry['content'] == card_desc, f"Mismatch 1:1 for {card_file} in optimized {opt_lb_file} lexicon!"
        opt_ent_entry = next((e for e in opt_lb_data['entries'] if e.get('entry_id') == entry_id), None)
        assert opt_ent_entry is not None, f"Entry {entry_id} not found in optimized {opt_lb_file} entries"
        assert opt_ent_entry['content'] == card_desc, f"Mismatch 1:1 for {card_file} in optimized {opt_lb_file} entries!"
        
        print(f"  PASS: 1:1 Match for {card_file} -> {lex_entry['name']} ({entry_id}) [lexicon & entries]")

    print("\n--- Testing Lorebook Entries == Lexicon Parity ---")
    for name in ['Svartulfr_Location.json', 'Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
        for folder in ['FINAL', 'lorebooks/optimized']:
            p = ROOT / folder / name
            d = json.loads(p.read_text(encoding='utf-8'))
            assert d['entries'] == d['lexicon'], f"entries != lexicon in {p}!"
            print(f"  PASS: entries == lexicon in {p}")

    print("\n--- Testing Firstborn Timeline (819 / 824 / 848 / 849 / 864 AD) in Lorebooks & Cards ---")
    # Wulfnic Card
    w_card = json.loads((ROOT / 'FINAL' / 'Wulfnic_Bloodmoon_card.json').read_text(encoding='utf-8'))
    assert "Jarl of the Svartulfr clan at age 25 in 849 AD" in w_card['description']
    assert "age 40 in 864 AD, Fenris turned him and his eight warrior companions" in w_card['description']
    assert "from 16-year-old Zefir to 45-year-old Ut" in w_card['description']
    assert "reads as ~60 to modern eyes" in w_card['description']
    print("  PASS: Wulfnic card contains complete timeline and apparent age.")

    # NPC Primary: Ut Berg
    lb_pri = json.loads((ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
    ut_e = next(e for e in lb_pri['lexicon'] if e.get('entry_id') == 'QLKp7v-jamdpsEz7GMgqB')
    assert "AGE: 1205 (Born May 5, 819 AD); turned at 45 in 864 AD; presented age: 60;" in ut_e['content']
    assert "turned by Fenris in 864 AD at age 45, the eldest of the Nine warrior companions" in ut_e['content']
    print("  PASS: Ut Berg in NPC Primary has correct 819 AD / 864 AD / presented age 60.")

    # NPC Primary: Zefir Hvitskog
    zef_e = next(e for e in lb_pri['lexicon'] if e.get('entry_id') == 'aA5zIYvLivjMts978RWEn')
    assert "AGE: 1176 (Born February 5, 848 AD); turned at 16 in 864 AD; presented age: 20-22;" in zef_e['content']
    assert "taken by Fenris at age 16 in 864 AD while his body was still unfinished" in zef_e['content']
    assert "FACE: Youthful, sharp Viking features (16 years old in the 9th century, reading as a 20-22 year old young man to modern eyes)" in zef_e['content']
    assert "North Sea wind" in zef_e['content']
    assert "He was born in 848 AD" in zef_e['content']
    assert "1005" not in zef_e['content']
    print("  PASS: Zefir in NPC Primary has correct 848 AD / 864 AD / presented age 20-22 / North Sea Wind.")

    # Lorebook I
    lb1 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json').read_text(encoding='utf-8'))
    e_lb1 = next(e for e in lb1['lexicon'] if e.get('entry_id') == 'HxdpzBtgY_wSx5ZpIDzGK')
    assert "824 d.C." in e_lb1['content'] and "849 d.C." in e_lb1['content'] and "864 d.C." in e_lb1['content']
    e_lb1_z = next(e for e in lb1['lexicon'] if e.get('entry_id') == 'WTVBwGkRovmXZKfrjYKBw')
    assert "848 d.C." in e_lb1_z['content'] and "864 d.C." in e_lb1_z['content'] and "20-22" in e_lb1_z['content']
    e_lb1_u = next(e for e in lb1['lexicon'] if e.get('entry_id') == 'pyWwstSbY5IYYvNn-4-hf')
    assert "819 d.C." in e_lb1_u['content'] and "864 d.C." in e_lb1_u['content'] and "60" in e_lb1_u['content']
    print("  PASS: Lorebook I Apex Sovereign, Zefir, and Ut contain canonical dates.")

    # Lorebook II
    lb2 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_II.json').read_text(encoding='utf-8'))
    e51 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'nbeEd2cvkA5PLke6svWez')
    assert "Born December 21, 824 AD in Iceland." in e51['content']
    assert "Born May 5, 819 AD in Viking Age Scandinavia; eldest of the Nine at 45 when turned in 864 AD (age 1205 in 2024)." in e51['content']
    assert "Born 5 February 848 AD. The youngest of the Nine, turned by Fenris at age 16 in 864 AD (age 1176 in 2024)" in e51['content']
    assert "1005" not in e51['content']
    print("  PASS: Lorebook II Living Sagas contains canonical 819 / 824 / 848 / 864 AD dates.")

    e80 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'qCmzi5J5o-ocZcFJWyovq')
    assert "THE MYTHIC AGE (pre-864 AD)" in e80['content']
    assert "AGE OF THE FIRSTBORN (~864-1000 AD)" in e80['content']
    assert "pre-827" not in e80['content']
    print("  PASS: Lorebook II Timeline updated to pre-864 AD and ~864-1000 AD.")

    e91 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'ffB2cSM0T_5MYbddXlzNf')
    assert "Wulfnic nacque nell'824 d.C." in e91['content']
    assert "Nel 2024, Wulfnic compie 1200 anni." in e91['content']
    print("  PASS: Lorebook II Viaggio contains 824 d.C. and 1200 anni.")

    e93 = next(e for e in lb2['lexicon'] if e.get('entry_id') == '21rz_Jv-VaddKBNMya2tf')
    assert "Born December 21, 824 AD" in e93['content']
    assert "Born May 5, 819 AD; turned at 45 in 864 AD." in e93['content']
    assert "Born February 5, 848 AD; turned at 16 in 864 AD." in e93['content']
    print("  PASS: Lorebook II Genealogies contains 819 / 824 / 848 / 864 AD dates.")

    print("\n--- Testing Svartulfr_Master_Scenario.json ---")
    scen_txt = (ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json').read_text(encoding='utf-8')
    assert '—' not in scen_txt, "Em-dash found in Master Scenario!"
    assert '1,200-year-old' in scen_txt, "1,200-year-old not found in Master Scenario!"
    print("  PASS: Master Scenario has 0 em-dashes and 1,200-year-old Wulfnic.")

    print("\n" + "=" * 70)
    print("ALL LOCAL TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 70)

if __name__ == '__main__':
    verify_all_local()
