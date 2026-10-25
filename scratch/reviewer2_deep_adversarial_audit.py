import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.insert(0, str(ROOT / 'scratch'))
import refresh_token

TOKEN = refresh_token.refresh()
API_APP = 'https://app.wyvern.chat/api'
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/json',
    'User-Agent': 'AuditorBot/1.0'
}

def api_get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.status, json.loads(resp.read().decode('utf-8'))

def run_adversarial_audit():
    print("=" * 80)
    print("REVIEWER 2 INDEPENDENT ADVERSARIAL AUDIT")
    print("=" * 80)

    errors = []

    # =========================================================================
    # PART 1: 8 FINAL CARDS
    # =========================================================================
    print("\n[PART 1] Auditing 8 Final Character Cards...")
    final_cards = [
        ('Edric_Douglas_card.json', '_TbRM3EdxDjHFgqztTbCpL', 'AGE: 13 (Born February 25, 2011)', 'FAMILY & PACK:'),
        ('Erik_Douglas_card.json', '_QPea6g4Q1QfeYCVHCLMPR', 'AGE: 55 (Born October 31, 1969)', 'FAMILY & PACK:'),
        ('Jasper_Douglas_Bloodmoon_card.json', '_t4J9aQNJM36cUKAP4wB4U', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
        ('Logan_Douglas_card.json', '_T8Ywcr9FEqNf9JxbK6eHP', 'AGE: 49 (Born January 12, 1975)', 'FAMILY & PACK:'),
        ('Mackenzie_Sanchez_Rogers_card.json', '_zn24784jfcchQ7EwCyAnm', 'AGE: 19 (Born November 14, 2004)', 'FAMILY & PACK:'),
        ('Malachia_Douglas_Bloodmoon_card.json', '_RDfz7XzTpM23LpPALVXHM', 'AGE: 28 (Born August 10, 1996)', 'FAMILY & PACK:'),
        ('Noah_Douglas_Bloodmoon_card.json', '_zFLUjV8aVxQRAfQxGcAcY', 'AGE: 25 (Born October 5, 1998)', 'FAMILY & PACK:'),
        ('Wulfnic_Bloodmoon_card.json', '_HEQQbbRFwKdG8QE2Fh1z1', 'AGE: 1200 (Born December 21, 824 AD)', 'FAMILY & PACK:'),
    ]

    for fname, cid, expected_age, fam_block in final_cards:
        p = ROOT / 'FINAL' / fname
        try:
            d = json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            errors.append(f"{fname}: JSON load failed: {e}")
            continue

        desc = d.get('description', '')
        lines = desc.split('\n')
        line1 = lines[0]

        # Line 1 single line PList
        if not line1.startswith('[') or not line1.endswith(']'):
            errors.append(f"{fname}: Line 1 does not start with [ and end with ]")
        if '\n' in line1:
            errors.append(f"{fname}: Line 1 contains newline")
        if expected_age not in line1:
            errors.append(f"{fname}: Expected '{expected_age}' not found in Line 1")

        # Invariants in Noah
        if 'Noah' in fname:
            if 'BIRTH_RUNE' in line1 and line1.count('BIRTH_RUNE:') > 1:
                errors.append(f"Noah: duplicate BIRTH_RUNE in line 1 PList!")
            for forbidden in ['SPACES:', 'WEAKNESSES:']:
                if forbidden in line1:
                    errors.append(f"Noah: forbidden nested {forbidden} inside Line 1 PList!")

        # 4 Blocks Order
        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find(fam_block)
        idx_v = desc.find('VOICE & BEHAVIOR:')
        if idx_b == -1 or idx_f == -1 or idx_v == -1:
            errors.append(f"{fname}: Missing one of core headers: B={idx_b}, F={idx_f}, V={idx_v}")
        elif not (idx_b < idx_f < idx_v):
            errors.append(f"{fname}: Header order violation: B({idx_b}) < F({idx_f}) < V({idx_v})")

        # Malachia specific check
        if 'Malachia' in fname:
            idx_closed = desc.find('THE DISTANCE HE HAS ALREADY CLOSED:')
            if idx_closed == -1:
                errors.append("Malachia: THE DISTANCE HE HAS ALREADY CLOSED not found")
            elif idx_closed < idx_v:
                errors.append("Malachia: THE DISTANCE HE HAS ALREADY CLOSED is before VOICE & BEHAVIOR!")

        # Personality PList
        pers = d.get('personality', '').strip()
        if not pers.startswith('[') or not pers.endswith(']'):
            errors.append(f"{fname}: Personality not wrapped in [...]")
        if pers.endswith(',') or pers.endswith('...'):
            errors.append(f"{fname}: Personality ends with comma or ellipsis (truncated)")
        for required_key in ['NAME:', 'ROLE:', 'TRAITS:', 'CORE:']:
            if required_key not in pers:
                errors.append(f"{fname}: Personality missing required key {required_key}")
        if expected_age not in pers:
            errors.append(f"{fname}: Personality missing expected age '{expected_age}'")

        # Format discipline
        for field in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = d.get(field, '')
            if isinstance(val, str):
                if '—' in val:
                    errors.append(f"{fname}: em-dash found in {field}")
                if '*' in val:
                    errors.append(f"{fname}: asterisk found in {field}")

        phi = d.get('post_history_instructions', '')
        if 'Format discipline' not in phi:
            errors.append(f"{fname}: Format discipline clause missing in post_history_instructions")

        print(f"  OK: {fname}")

    # =========================================================================
    # PART 2: 3 USER PERSONAS
    # =========================================================================
    print("\n[PART 2] Auditing 3 User Personas...")
    personas = [
        ('Alyssa_Persona.json', 'persona_1786335754946', 'AGE: 19 (Born April 22, 2005)'),
        ('Jasper_Persona.json', '1792155173728', 'AGE: 19 (Born April 22, 2005)'),
        ('Echo_Persona.json', '1791389790053', 'AGE: 3 (Activated November 15, 2021)'),
    ]

    for fname, pid, expected_age in personas:
        p = ROOT / 'FINAL' / 'personas' / fname
        try:
            d = json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            errors.append(f"{fname}: JSON load failed: {e}")
            continue

        desc = d.get('description', '')
        lines = desc.split('\n')
        line1 = lines[0]
        if not line1.startswith('[') or not line1.endswith(']'):
            errors.append(f"{fname}: Line 1 does not start with [ and end with ]")
        if expected_age not in line1:
            errors.append(f"{fname}: Expected '{expected_age}' not found in Line 1")

        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find('FAMILY & PACK:')
        idx_v = desc.find('VOICE & BEHAVIOR:')
        if idx_b == -1 or idx_f == -1 or idx_v == -1:
            errors.append(f"{fname}: Missing core headers")
        elif not (idx_b < idx_f < idx_v):
            errors.append(f"{fname}: Header order violation")

        if d.get('can_fork') is not True:
            errors.append(f"{fname}: can_fork is not True")

        # Recursive text audit
        def check_persona_text(obj, path):
            if isinstance(obj, str):
                if '—' in obj:
                    errors.append(f"{fname}: em-dash found in {path}: {obj[:40]}")
                if '*' in obj:
                    errors.append(f"{fname}: asterisk found in {path}: {obj[:40]}")
                if '`' in obj:
                    errors.append(f"{fname}: backtick markdown found in {path}: {obj[:40]}")
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    if k not in ['id', '_id', 'avatar', 'backgroundURL', 'image_url']:
                        check_persona_text(v, f"{path}.{k}" if path else k)
            elif isinstance(obj, list):
                for idx, it in enumerate(obj):
                    check_persona_text(it, f"{path}[{idx}]")

        check_persona_text(d, "")
        print(f"  OK: {fname}")

    # =========================================================================
    # PART 3: 6 LEGACY CARDS
    # =========================================================================
    print("\n[PART 3] Auditing 6 Legacy Cards...")
    legacy_cards = [
        ('Alyssa_Douglas_Bloodmoon_card.json', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
        ('Jared_Thompson_card.json', 'AGE: 22 (Born March 24, 2002)', 'FAMILY & PACK:'),
        ('Russ_card.json', 'AGE: 21 (Born March 14, 2003)', 'CLAN AND COMPANY:'),
        ('Scarlett_Rose_card.json', 'AGE: 20 (Born November 18, 2003)', 'CLAN AND COMPANY:'),
        ('Sierra_Cruz_card.json', 'AGE: 18 (Born September 8, 2005)', 'CLAN AND COMPANY:'),
        ('Stan_Davies_Jr_card.json', 'AGE: 21 (Born September 14, 2002)', 'FAMILY & PACK:'),
    ]

    for fname, expected_age, fam_block in legacy_cards:
        p = ROOT / 'ARCHIVIO' / 'cards_legacy' / fname
        try:
            d = json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            errors.append(f"{fname}: JSON load failed: {e}")
            continue

        desc = d.get('description', '')
        line1 = desc.split('\n')[0]
        if not line1.startswith('[') or not line1.endswith(']'):
            errors.append(f"{fname}: Line 1 does not start with [ and end with ]")
        if expected_age not in line1:
            errors.append(f"{fname}: Expected '{expected_age}' not found in Line 1")

        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find(fam_block)
        idx_v = desc.find('VOICE & BEHAVIOR:')
        if idx_b == -1 or idx_f == -1 or idx_v == -1:
            errors.append(f"{fname}: Missing core headers")
        elif not (idx_b < idx_f < idx_v):
            errors.append(f"{fname}: Header order violation")

        if 'Jared' in fname:
            if desc.count('FAMILY & PACK:') != 1:
                errors.append("Jared: Multiple FAMILY & PACK: found")
            if re.findall(r'^FAMILY:\s*', desc, flags=re.M):
                errors.append("Jared: Standalone FAMILY: found")

        pers = d.get('personality', '').strip()
        if not pers.startswith('[') or not pers.endswith(']'):
            errors.append(f"{fname}: Personality not wrapped in [...]")
        if pers.endswith(','):
            errors.append(f"{fname}: Personality ends with comma")

        for field in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = d.get(field, '')
            if isinstance(val, str):
                if '—' in val:
                    errors.append(f"{fname}: em-dash found in {field}")
                if '*' in val:
                    errors.append(f"{fname}: asterisk found in {field}")

        print(f"  OK: {fname}")

    # =========================================================================
    # PART 4: LOREBOOK 1:1 SYNC & ENTRIES == LEXICON PARITY
    # =========================================================================
    print("\n[PART 4] Auditing Lorebooks 1:1 Parity and Structural Identity...")
    for lb_name in ['Svartulfr_Location.json', 'Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
        for folder in ['FINAL', 'lorebooks/optimized']:
            p = ROOT / folder / lb_name
            d = json.loads(p.read_text(encoding='utf-8'))
            if d.get('entries') != d.get('lexicon'):
                errors.append(f"{p}: entries != lexicon!")

    core_sync_checks = [
        ('Erik_Douglas_card.json', 'C-JisFj8qA1tsFEqZKevk', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Malachia_Douglas_Bloodmoon_card.json', 'jDuJtzirlEZC3K_ArIufh', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Noah_Douglas_Bloodmoon_card.json', 'H2JX-NkHRiJ2FzoekC5ZZ', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Logan_Douglas_card.json', 'tAcrWLtWSDGf3xJJRwUOM', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Wulfnic_Bloodmoon_card.json', 'HhuMluMmIIENUei3bX6ed', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Mackenzie_Sanchez_Rogers_card.json', 'BXi3sENAVYB8OKF80Q9Su', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Edric_Douglas_card.json', 'h-ttmlgJYeRXqyDvQjSX7', 'FINAL/Svartulfr_NPC_Secondary.json'),
    ]

    for card_fname, eid, lb_relpath in core_sync_checks:
        c_desc = json.loads((ROOT / 'FINAL' / card_fname).read_text(encoding='utf-8'))['description']
        lb_main = json.loads((ROOT / lb_relpath).read_text(encoding='utf-8'))
        e_lex = next((e for e in lb_main['lexicon'] if e.get('entry_id') == eid), None)
        e_ent = next((e for e in lb_main['entries'] if e.get('entry_id') == eid), None)
        if not e_lex or e_lex['content'] != c_desc:
            errors.append(f"{lb_relpath} lexicon mismatch for {card_fname}")
        if not e_ent or e_ent['content'] != c_desc:
            errors.append(f"{lb_relpath} entries mismatch for {card_fname}")

        opt_path = ROOT / 'lorebooks' / 'optimized' / pathlib.Path(lb_relpath).name
        lb_opt = json.loads(opt_path.read_text(encoding='utf-8'))
        opt_lex = next((e for e in lb_opt['lexicon'] if e.get('entry_id') == eid), None)
        opt_ent = next((e for e in lb_opt['entries'] if e.get('entry_id') == eid), None)
        if not opt_lex or opt_lex['content'] != c_desc:
            errors.append(f"{opt_path} lexicon mismatch for {card_fname}")
        if not opt_ent or opt_ent['content'] != c_desc:
            errors.append(f"{opt_path} entries mismatch for {card_fname}")

        print(f"  OK 1:1 Parity: {card_fname} -> {eid}")

    # =========================================================================
    # PART 5: WULFNIC 824 AD LEDGER INVARIANTS & MASTER SCENARIO
    # =========================================================================
    print("\n[PART 5] Auditing Wulfnic 824 AD Invariants & Master Scenario...")
    w_card = json.loads((ROOT / 'FINAL' / 'Wulfnic_Bloodmoon_card.json').read_text(encoding='utf-8'))
    if 'AGE: 1200 (Born December 21, 824 AD)' not in w_card['description']:
        errors.append("Wulfnic card description missing AGE: 1200 (Born December 21, 824 AD)")
    if 'AGE: 1200 (Born December 21, 824 AD)' not in w_card['personality']:
        errors.append("Wulfnic card personality missing AGE: 1200 (Born December 21, 824 AD)")
    if '1,200-year-old' not in w_card.get('character_note', ''):
        errors.append("Wulfnic character_note missing 1,200-year-old")

    lb1 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json').read_text(encoding='utf-8'))
    e_lb1 = next(e for e in lb1['lexicon'] if e.get('entry_id') == 'HxdpzBtgY_wSx5ZpIDzGK')
    if "nell'824 d.C." not in e_lb1['content']:
        errors.append("Lorebook I missing nell'824 d.C. in Apex entry")

    lb2 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_II.json').read_text(encoding='utf-8'))
    e51 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'nbeEd2cvkA5PLke6svWez')
    if "Born circa 824 AD in Iceland." not in e51['content']:
        errors.append("Lorebook II entry 51 missing Born circa 824 AD in Iceland.")

    e80 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'qCmzi5J5o-ocZcFJWyovq')
    if "(born circa 824 AD, Iceland)" not in e80['content']:
        errors.append("Lorebook II entry 80 missing (born circa 824 AD, Iceland)")

    e91 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'ffB2cSM0T_5MYbddXlzNf')
    if "Wulfnic nacque nell'824 d.C." not in e91['content']:
        errors.append("Lorebook II entry 91 missing Wulfnic nacque nell'824 d.C.")
    if "Nel 2024, Wulfnic compie 1200 anni." not in e91['content']:
        errors.append("Lorebook II entry 91 missing Nel 2024, Wulfnic compie 1200 anni.")

    e93 = next(e for e in lb2['lexicon'] if e.get('entry_id') == '21rz_Jv-VaddKBNMya2tf')
    if "Born circa 824 AD." not in e93['content']:
        errors.append("Lorebook II entry 93 missing Born circa 824 AD.")

    scen_raw = (ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json').read_text(encoding='utf-8')
    if '—' in scen_raw:
        errors.append("Svartulfr_Master_Scenario.json contains em-dash!")
    if '1,200-year-old' not in scen_raw:
        errors.append("Svartulfr_Master_Scenario.json missing 1,200-year-old!")

    print("  OK: Local 824 AD and Master Scenario invariants verified.")

    # =========================================================================
    # PART 6: LIVE API DEEP AUDIT
    # =========================================================================
    print("\n[PART 6] Auditing Live Wyvern API State...")
    for fname, cid, expected_age, _ in final_cards:
        st, live_c = api_get(f"{API_APP}/characters/{cid}")
        if st != 200:
            errors.append(f"Live GET /characters/{cid} ({fname}) returned status {st}")
            continue
        l1 = live_c.get('description', '').split('\n')[0]
        if expected_age not in l1:
            errors.append(f"Live card {fname} ({cid}) description line 1 missing '{expected_age}'")
        pers = live_c.get('personality', '')
        if expected_age not in pers:
            errors.append(f"Live card {fname} ({cid}) personality missing '{expected_age}'")
        for fld in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = live_c.get(fld, '')
            if isinstance(val, str) and ('—' in val or '*' in val):
                errors.append(f"Live card {fname} ({cid}) contains em-dash or asterisk in {fld}")
        print(f"  OK Live Character Card: {fname} ({cid})")

    for fname, pid, expected_age in personas:
        st, live_p = api_get(f"{API_APP}/user-personas/{pid}")
        if st != 200:
            errors.append(f"Live GET /user-personas/{pid} ({fname}) returned status {st}")
            continue
        l1 = live_p.get('description', '').split('\n')[0]
        if expected_age not in l1:
            errors.append(f"Live persona {fname} ({pid}) line 1 missing '{expected_age}'")
        if live_p.get('can_fork') is not True:
            errors.append(f"Live persona {fname} ({pid}) can_fork != True")
        print(f"  OK Live Persona: {fname} ({pid})")

    # Live Lorebooks
    st, live_prim = api_get(f"{API_APP}/lorebooks/_zwEqgEEzh12X6gHVmMKKC")
    if st != 200:
        errors.append(f"Live GET /lorebooks/_zwEqgEEzh12X6gHVmMKKC returned {st}")
    else:
        entries = live_prim.get('lexicon', live_prim.get('entries', []))
        if len(entries) != 99:
            errors.append(f"Live Primary entries count {len(entries)} != 99")
        for cf, eid, _ in core_sync_checks[:6]:
            cd = json.loads((ROOT / 'FINAL' / cf).read_text(encoding='utf-8'))['description']
            le = next((e for e in entries if e.get('entry_id') == eid), None)
            if not le or le.get('content') != cd:
                errors.append(f"Live Primary lorebook parity mismatch for {cf} ({eid})")
            else:
                print(f"  OK Live Primary 1:1 Match: {cf}")

    st, live_sec = api_get(f"{API_APP}/lorebooks/_Uht3Ckz44JBDrPnUHq7LV")
    if st != 200:
        errors.append(f"Live GET /lorebooks/_Uht3Ckz44JBDrPnUHq7LV returned {st}")
    else:
        entries = live_sec.get('lexicon', live_sec.get('entries', []))
        if len(entries) != 211:
            errors.append(f"Live Secondary entries count {len(entries)} != 211")
        ed_desc = json.loads((ROOT / 'FINAL' / 'Edric_Douglas_card.json').read_text(encoding='utf-8'))['description']
        le = next((e for e in entries if e.get('entry_id') == 'h-ttmlgJYeRXqyDvQjSX7'), None)
        if not le or le.get('content') != ed_desc:
            errors.append(f"Live Secondary lorebook parity mismatch for Edric")
        else:
            print(f"  OK Live Secondary 1:1 Match: Edric_Douglas_card.json")

    st, live_lb1 = api_get(f"{API_APP}/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL")
    if st != 200:
        errors.append(f"Live GET Lorebook I returned {st}")
    else:
        entries = live_lb1.get('lexicon', live_lb1.get('entries', []))
        e = next(e for e in entries if e.get('entry_id') == 'HxdpzBtgY_wSx5ZpIDzGK')
        if "nell'824 d.C." not in e.get('content', ''):
            errors.append("Live Lorebook I missing nell'824 d.C. in Apex entry")
        else:
            print("  OK Live Lorebook I: nell'824 d.C. verified")

    st, live_lb2 = api_get(f"{API_APP}/lorebooks/_HfG7TeV6MJyj6bxMwxkpt")
    if st != 200:
        errors.append(f"Live GET Lorebook II returned {st}")
    else:
        entries = live_lb2.get('lexicon', live_lb2.get('entries', []))
        e51 = next(e for e in entries if e.get('entry_id') == 'nbeEd2cvkA5PLke6svWez')
        if "Born circa 824 AD in Iceland." not in e51.get('content', ''):
            errors.append("Live Lorebook II missing Born circa 824 AD in Iceland.")
        e80 = next(e for e in entries if e.get('entry_id') == 'qCmzi5J5o-ocZcFJWyovq')
        if "(born circa 824 AD, Iceland)" not in e80.get('content', ''):
            errors.append("Live Lorebook II missing (born circa 824 AD, Iceland)")
        e91 = next(e for e in entries if e.get('entry_id') == 'ffB2cSM0T_5MYbddXlzNf')
        if "Wulfnic nacque nell'824 d.C." not in e91.get('content', ''):
            errors.append("Live Lorebook II missing Wulfnic nacque nell'824 d.C.")
        if "Nel 2024, Wulfnic compie 1200 anni." not in e91.get('content', ''):
            errors.append("Live Lorebook II missing Nel 2024, Wulfnic compie 1200 anni.")
        e93 = next(e for e in entries if e.get('entry_id') == '21rz_Jv-VaddKBNMya2tf')
        if "Born circa 824 AD." not in e93.get('content', ''):
            errors.append("Live Lorebook II missing Born circa 824 AD.")
        print("  OK Live Lorebook II: All 824 AD & 1200 years invariants verified")

    print("\n" + "=" * 80)
    if errors:
        print(f"AUDIT FAILED WITH {len(errors)} ERRORS:")
        for err in errors:
            print(f"  [X] {err}")
        sys.exit(1)
    else:
        print("AUDIT FINISHED: 0 ISSUES FOUND! 100% SUCCESS ACROSS LOCAL AND REMOTE STATE.")
    print("=" * 80)

if __name__ == '__main__':
    run_adversarial_audit()
