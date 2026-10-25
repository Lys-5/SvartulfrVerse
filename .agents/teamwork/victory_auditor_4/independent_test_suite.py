import json
import pathlib
import sys
import urllib.request
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
MY_DIR = ROOT / '.agents' / 'teamwork' / 'victory_auditor_4'

# Import refresh_token to get live token
sys.path.insert(0, str(ROOT / 'scratch'))
import refresh_token

results = {
    "phase_a_local": {"status": "NOT_RUN", "details": []},
    "phase_b_cheating": {"status": "NOT_RUN", "details": []},
    "phase_c_live_api": {"status": "NOT_RUN", "details": []},
}

def log(phase, msg):
    print(f"[{phase}] {msg}")
    results[phase]["details"].append(msg)

def run_phase_a_and_b_local():
    print("=" * 80)
    print("INDEPENDENT VICTORY AUDITOR — LOCAL CODEBASE & REQUISITES AUDIT")
    print("=" * 80)
    failures = []

    # 1. 8 FINAL CHARACTER CARDS
    final_cards = [
        ('Edric_Douglas_card.json', '_TbRM3EdxDjHFgqztTbCpL', 'AGE: 13 (Born February 25, 2011)'),
        ('Erik_Douglas_card.json', '_QPea6g4Q1QfeYCVHCLMPR', 'AGE: 55 (Born October 31, 1969)'),
        ('Jasper_Douglas_Bloodmoon_card.json', '_t4J9aQNJM36cUKAP4wB4U', 'AGE: 19 (Born April 22, 2005)'),
        ('Logan_Douglas_card.json', '_T8Ywcr9FEqNf9JxbK6eHP', 'AGE: 49 (Born January 12, 1975)'),
        ('Mackenzie_Sanchez_Rogers_card.json', '_zn24784jfcchQ7EwCyAnm', 'AGE: 19 (Born November 14, 2004)'),
        ('Malachia_Douglas_Bloodmoon_card.json', '_RDfz7XzTpM23LpPALVXHM', 'AGE: 28 (Born August 10, 1996)'),
        ('Noah_Douglas_Bloodmoon_card.json', '_zFLUjV8aVxQRAfQxGcAcY', 'AGE: 25 (Born October 5, 1998)'),
        ('Wulfnic_Bloodmoon_card.json', '_HEQQbbRFwKdG8QE2Fh1z1', 'AGE: 1200 (Born December 21, 824 AD)'),
    ]

    for fname, cid, expected_age in final_cards:
        p = ROOT / 'FINAL' / fname
        if not p.exists():
            failures.append(f"Missing card file: {p}")
            continue
        data = json.loads(p.read_text(encoding='utf-8'))
        desc = data.get('description', '')
        lines = desc.split('\n')
        line1 = lines[0]

        # Line 1 single line bracket check
        if not (line1.startswith('[') and line1.endswith(']')):
            failures.append(f"{fname}: Line 1 not enclosed in [...] brackets")
        if '\n' in line1:
            failures.append(f"{fname}: Line 1 contains newline")
        if expected_age not in line1:
            failures.append(f"{fname}: Line 1 does not contain expected age '{expected_age}'")

        # 4 Canonical Headers
        b_idx = desc.find('BACKSTORY:')
        f_idx = desc.find('FAMILY & PACK:')
        v_idx = desc.find('VOICE & BEHAVIOR:')
        if b_idx == -1: failures.append(f"{fname}: Missing BACKSTORY:")
        if f_idx == -1: failures.append(f"{fname}: Missing FAMILY & PACK:")
        if v_idx == -1: failures.append(f"{fname}: Missing VOICE & BEHAVIOR:")
        if not (b_idx < f_idx < v_idx):
            failures.append(f"{fname}: Header order mismatch: BACKSTORY({b_idx}) < FAMILY({f_idx}) < VOICE({v_idx})")

        # Specific Noah checks
        if 'Noah' in fname:
            if 'BIRTH_RUNE: Berkana; BIRTH_RUNE:' in desc or desc.count('BIRTH_RUNE:') > 1:
                failures.append("Noah card has duplicate BIRTH_RUNE:")
            if 'SPACES:' in line1 or 'WEAKNESSES:' in line1:
                failures.append("Noah line 1 still has nested SPACES: or WEAKNESSES:")
            if desc.count('BACKSTORY:') > 1:
                failures.append(f"Noah card has multiple BACKSTORY: headers ({desc.count('BACKSTORY:')})")

        # Specific Malachia check
        if 'Malachia' in fname:
            d_idx = desc.find('THE DISTANCE HE HAS ALREADY CLOSED:')
            if d_idx != -1 and d_idx < v_idx:
                failures.append("Malachia: THE DISTANCE HE HAS ALREADY CLOSED is placed before VOICE & BEHAVIOR:")

        # Personality PList
        pers = data.get('personality', '').strip()
        if not (pers.startswith('[') and pers.endswith(']')):
            failures.append(f"{fname}: personality is not enclosed in [...]")
        if pers.endswith(',') or pers.endswith('...'):
            failures.append(f"{fname}: personality ends with truncation characters")
        for k in ['NAME:', 'ROLE:', 'TRAITS:', 'CORE:']:
            if k not in pers:
                failures.append(f"{fname}: personality missing key '{k}'")
        if expected_age not in pers:
            failures.append(f"{fname}: personality missing '{expected_age}'")

        # Formatting discipline
        for field in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = data.get(field, '')
            if isinstance(val, str):
                if '—' in val:
                    failures.append(f"{fname}: em-dash found in {field}")
                if '*' in val:
                    failures.append(f"{fname}: asterisk found in {field}")

        phi = data.get('post_history_instructions', '')
        if 'Format discipline:' not in phi and 'Format discipline' not in phi:
            failures.append(f"{fname}: post_history_instructions missing Format Discipline clause")

    log("phase_a_local", f"Tested 8 final cards. Failures so far: {len(failures)}")

    # 2. 3 USER PERSONAS
    personas = [
        ('Alyssa_Persona.json', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
        ('Echo_Persona.json', 'AGE: 3 (Activated November 15, 2021)', 'FAMILY & PACK:'),
        ('Jasper_Persona.json', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
    ]

    for fname, expected_age, fam_header in personas:
        p = ROOT / 'FINAL' / 'personas' / fname
        if not p.exists():
            failures.append(f"Missing persona file: {p}")
            continue
        data = json.loads(p.read_text(encoding='utf-8'))
        desc = data.get('description', '')
        line1 = desc.split('\n')[0]
        if not (line1.startswith('[') and line1.endswith(']')):
            failures.append(f"Persona {fname}: Line 1 not in [...]")
        if expected_age not in line1:
            failures.append(f"Persona {fname}: Missing '{expected_age}' in line 1")

        b_idx = desc.find('BACKSTORY:')
        f_idx = desc.find(fam_header)
        v_idx = desc.find('VOICE & BEHAVIOR:')
        if b_idx == -1 or f_idx == -1 or v_idx == -1 or not (b_idx < f_idx < v_idx):
            failures.append(f"Persona {fname}: Canonical header order violated")

        if data.get('can_fork') is not True:
            failures.append(f"Persona {fname}: can_fork is not True")

        # Deep text scan for em-dash and asterisks
        def scan_obj(obj, path):
            if isinstance(obj, str):
                if '—' in obj:
                    failures.append(f"Persona {fname}: em-dash in {path}: {obj[:40]}")
                if '*' in obj:
                    failures.append(f"Persona {fname}: asterisk in {path}: {obj[:40]}")
                if '`' in obj:
                    failures.append(f"Persona {fname}: backtick in {path}: {obj[:40]}")
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    if k not in ['id', '_id', 'avatar', 'backgroundURL', 'image_url']:
                        scan_obj(v, f"{path}.{k}" if path else k)
            elif isinstance(obj, list):
                for idx, item in enumerate(obj):
                    scan_obj(item, f"{path}[{idx}]")

        scan_obj(data, "")

    log("phase_a_local", f"Tested 3 user personas. Failures so far: {len(failures)}")

    # 3. 6 LEGACY CARDS
    legacy = [
        ('Alyssa_Douglas_Bloodmoon_card.json', 'AGE: 19 (Born April 22, 2005)', 'FAMILY & PACK:'),
        ('Jared_Thompson_card.json', 'AGE: 22 (Born March 24, 2002)', 'FAMILY & PACK:'),
        ('Russ_card.json', 'AGE: 21 (Born March 14, 2003)', 'CLAN AND COMPANY:'),
        ('Scarlett_Rose_card.json', 'AGE: 20 (Born November 18, 2003)', 'CLAN AND COMPANY:'),
        ('Sierra_Cruz_card.json', 'AGE: 18 (Born September 8, 2005)', 'CLAN AND COMPANY:'),
        ('Stan_Davies_Jr_card.json', 'AGE: 21 (Born September 14, 2002)', 'FAMILY & PACK:'),
    ]

    for fname, expected_age, fam_header in legacy:
        p = ROOT / 'ARCHIVIO' / 'cards_legacy' / fname
        if not p.exists():
            failures.append(f"Missing legacy card file: {p}")
            continue
        data = json.loads(p.read_text(encoding='utf-8'))
        desc = data.get('description', '')
        line1 = desc.split('\n')[0]
        if not (line1.startswith('[') and line1.endswith(']')):
            failures.append(f"Legacy {fname}: Line 1 not in [...]")
        if expected_age not in line1:
            failures.append(f"Legacy {fname}: Missing '{expected_age}' in line 1")

        b_idx = desc.find('BACKSTORY:')
        f_idx = desc.find(fam_header)
        v_idx = desc.find('VOICE & BEHAVIOR:')
        if b_idx == -1 or f_idx == -1 or v_idx == -1 or not (b_idx < f_idx < v_idx):
            failures.append(f"Legacy {fname}: Header order violation: BACKSTORY < {fam_header} < VOICE & BEHAVIOR")

        if 'Jared' in fname and desc.count('FAMILY & PACK:') != 1:
            failures.append("Legacy Jared: Multiple FAMILY & PACK: headers")

        pers = data.get('personality', '').strip()
        if not (pers.startswith('[') and pers.endswith(']')):
            failures.append(f"Legacy {fname}: Personality not in [...]")

        for fld in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = data.get(fld, '')
            if isinstance(val, str):
                if '—' in val: failures.append(f"Legacy {fname}: em-dash in {fld}")
                if '*' in val: failures.append(f"Legacy {fname}: asterisk in {fld}")

    log("phase_a_local", f"Tested 6 legacy cards. Failures so far: {len(failures)}")

    # 4. 1:1 PARITY FOR 7 CORE CARDS ACROSS ENTRIES & LEXICON & MIRROR
    core_cards = [
        ('Erik_Douglas_card.json', 'C-JisFj8qA1tsFEqZKevk', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Malachia_Douglas_Bloodmoon_card.json', 'jDuJtzirlEZC3K_ArIufh', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Noah_Douglas_Bloodmoon_card.json', 'H2JX-NkHRiJ2FzoekC5ZZ', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Logan_Douglas_card.json', 'tAcrWLtWSDGf3xJJRwUOM', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Wulfnic_Bloodmoon_card.json', 'HhuMluMmIIENUei3bX6ed', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Mackenzie_Sanchez_Rogers_card.json', 'BXi3sENAVYB8OKF80Q9Su', 'FINAL/Svartulfr_NPC_Primary.json'),
        ('Edric_Douglas_card.json', 'h-ttmlgJYeRXqyDvQjSX7', 'FINAL/Svartulfr_NPC_Secondary.json'),
    ]

    for card_file, entry_id, lb_file in core_cards:
        c_desc = json.loads((ROOT / 'FINAL' / card_file).read_text(encoding='utf-8'))['description']
        
        # Check in FINAL
        lb_final = json.loads((ROOT / lb_file).read_text(encoding='utf-8'))
        e_lex = next((e for e in lb_final['lexicon'] if e.get('entry_id') == entry_id), None)
        e_ent = next((e for e in lb_final['entries'] if e.get('entry_id') == entry_id), None)
        if not e_lex or e_lex.get('content') != c_desc:
            failures.append(f"1:1 mismatch in {lb_file} lexicon for {card_file}")
        if not e_ent or e_ent.get('content') != c_desc:
            failures.append(f"1:1 mismatch in {lb_file} entries for {card_file}")

        # Check in optimized mirror
        opt_path = ROOT / 'lorebooks' / 'optimized' / pathlib.Path(lb_file).name
        lb_opt = json.loads(opt_path.read_text(encoding='utf-8'))
        o_lex = next((e for e in lb_opt['lexicon'] if e.get('entry_id') == entry_id), None)
        o_ent = next((e for e in lb_opt['entries'] if e.get('entry_id') == entry_id), None)
        if not o_lex or o_lex.get('content') != c_desc:
            failures.append(f"1:1 mismatch in {opt_path} lexicon for {card_file}")
        if not o_ent or o_ent.get('content') != c_desc:
            failures.append(f"1:1 mismatch in {opt_path} entries for {card_file}")

    log("phase_a_local", f"Tested 1:1 parity for 7 core cards. Failures so far: {len(failures)}")

    # 5. INVARIANT ENTRIES == LEXICON ACROSS ALL 6 LOREBOOKS IN FINAL & OPTIMIZED
    all_lorebooks = [
        'Svartulfr_Location.json',
        'Svartulfr_Lorebook_I.json',
        'Svartulfr_Lorebook_II.json',
        'Svartulfr_Lorebook_III.json',
        'Svartulfr_NPC_Primary.json',
        'Svartulfr_NPC_Secondary.json'
    ]

    for lb_name in all_lorebooks:
        for folder in ['FINAL', 'lorebooks/optimized']:
            p = ROOT / folder / lb_name
            d = json.loads(p.read_text(encoding='utf-8'))
            if d['entries'] != d['lexicon']:
                failures.append(f"Invariant entries == lexicon violated in {p}")

    log("phase_a_local", f"Tested entries == lexicon across all 6 lorebooks in 2 directories. Failures so far: {len(failures)}")

    # 6. FIRSTBORN TIMELINE & DATES & APPARENT AGE & ZEFIR PERSONALITY
    # Wulfnic
    w_card = json.loads((ROOT / 'FINAL' / 'Wulfnic_Bloodmoon_card.json').read_text(encoding='utf-8'))
    w_desc = w_card['description']
    if "Born December 21, 824 AD" not in w_desc: failures.append("Wulfnic missing Born December 21, 824 AD")
    if "Jarl of the Svartulfr clan at age 25 in 849 AD" not in w_desc: failures.append("Wulfnic missing Jarl at 25 in 849 AD")
    if "age 40 in 864 AD, Fenris turned him and his eight warrior companions" not in w_desc: failures.append("Wulfnic missing turned at 40 in 864 AD")
    if "reads as ~60 to modern eyes" not in w_desc: failures.append("Wulfnic missing reads as ~60 to modern eyes")

    # Ut Berg & Zefir in NPC Primary
    pri_data = json.loads((ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
    ut_e = next((e for e in pri_data['lexicon'] if e.get('entry_id') == 'QLKp7v-jamdpsEz7GMgqB'), None)
    if not ut_e: failures.append("Ut Berg entry QLKp7v-jamdpsEz7GMgqB not found in NPC Primary")
    else:
        if "AGE: 1205 (Born May 5, 819 AD); turned at 45 in 864 AD; presented age: 60;" not in ut_e['content']:
            failures.append("Ut Berg missing canonical AGE header")
        if "turned by Fenris in 864 AD at age 45, the eldest of the Nine warrior companions" not in ut_e['content']:
            failures.append("Ut Berg missing canonical backstory turned in 864 AD at 45")

    zef_e = next((e for e in pri_data['lexicon'] if e.get('entry_id') == 'aA5zIYvLivjMts978RWEn'), None)
    if not zef_e: failures.append("Zefir entry aA5zIYvLivjMts978RWEn not found in NPC Primary")
    else:
        zc = zef_e['content']
        if "AGE: 1176 (Born February 5, 848 AD); turned at 16 in 864 AD; presented age: 20-22;" not in zc:
            failures.append("Zefir missing canonical AGE header")
        if "taken by Fenris at age 16 in 864 AD while his body was still unfinished" not in zc:
            failures.append("Zefir missing canonical backstory turned at 16 in 864 AD")
        if "North Sea wind" not in zc:
            failures.append("Zefir missing 'North Sea wind' personality metaphor")
        if "He was born in 848 AD" not in zc:
            failures.append("Zefir missing 'He was born in 848 AD'")
        if "1005" in zc:
            failures.append("Zefir still contains obsolete '1005'")

    # Lorebook I & II
    lb1 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json').read_text(encoding='utf-8'))
    e_lb1 = next(e for e in lb1['lexicon'] if e.get('entry_id') == 'HxdpzBtgY_wSx5ZpIDzGK')
    if "824 d.C." not in e_lb1['content'] or "849 d.C." not in e_lb1['content'] or "864 d.C." not in e_lb1['content']:
        failures.append("Lorebook I entry HxdpzBtgY_wSx5ZpIDzGK missing 824/849/864 d.C.")

    lb2 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_II.json').read_text(encoding='utf-8'))
    e51 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'nbeEd2cvkA5PLke6svWez')
    if "Born December 21, 824 AD in Iceland." not in e51['content']: failures.append("LB2 e51 missing Wulfnic 824 AD")
    if "Born May 5, 819 AD in Viking Age Scandinavia; eldest of the Nine at 45 when turned in 864 AD (age 1205 in 2024)." not in e51['content']:
        failures.append("LB2 e51 missing Ut 819/864 AD")
    if "Born 5 February 848 AD. The youngest of the Nine, turned by Fenris at age 16 in 864 AD (age 1176 in 2024)" not in e51['content']:
        failures.append("LB2 e51 missing Zefir 848/864 AD")

    e80 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'qCmzi5J5o-ocZcFJWyovq')
    if "THE MYTHIC AGE (pre-864 AD)" not in e80['content']: failures.append("LB2 e80 missing pre-864 AD")
    if "AGE OF THE FIRSTBORN (~864-1000 AD)" not in e80['content']: failures.append("LB2 e80 missing ~864-1000 AD")
    if "pre-827" in e80['content']: failures.append("LB2 e80 contains obsolete pre-827")

    e91 = next(e for e in lb2['lexicon'] if e.get('entry_id') == 'ffB2cSM0T_5MYbddXlzNf')
    if "Wulfnic nacque nell'824 d.C." not in e91['content'] or "1200 anni" not in e91['content']:
        failures.append("LB2 e91 missing Wulfnic 824 d.C. or 1200 anni")

    e93 = next(e for e in lb2['lexicon'] if e.get('entry_id') == '21rz_Jv-VaddKBNMya2tf')
    if "Born December 21, 824 AD" not in e93['content'] or "864 AD" not in e93['content']:
        failures.append("LB2 e93 missing 824 AD or 864 AD")

    # Svartulfr_Master_Scenario.json
    ms_txt = (ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json').read_text(encoding='utf-8')
    if '—' in ms_txt: failures.append("Svartulfr_Master_Scenario.json contains em-dash")
    if '1,200-year-old' not in ms_txt: failures.append("Svartulfr_Master_Scenario.json missing 1,200-year-old Wulfnic")

    log("phase_a_local", f"Tested Firstborn timeline and master scenario. Total local failures: {len(failures)}")

    if failures:
        results["phase_a_local"]["status"] = "FAIL"
        for f in failures:
            log("phase_a_local", f"  FAILURE: {f}")
        return False
    else:
        results["phase_a_local"]["status"] = "PASS"
        log("phase_a_local", "ALL LOCAL CHECKS PASSED (100% SUCCESS)")
        return True

def run_phase_b_cheating_audit():
    print("=" * 80)
    print("INDEPENDENT VICTORY AUDITOR — INTEGRITY & CHEATING DETECTION")
    print("=" * 80)
    cheating_flags = []

    # 1. Hardcoded / mock bypasses
    # Check that verification scripts don't just 'return True' unconditionally
    scripts = [
        ROOT / 'scratch' / 'verify_local_suite.py',
        ROOT / 'scratch' / 'verify_live_api.py',
        ROOT / 'scratch' / 'reviewer3_adversarial_check.py'
    ]
    for s in scripts:
        code = s.read_text(encoding='utf-8')
        if "def verify" in code and "return True" in code:
            lines = [l.strip() for l in code.split('\n')]
            for i, l in enumerate(lines):
                if l.startswith("def verify") and i + 1 < len(lines) and lines[i+1] == "return True":
                    cheating_flags.append(f"Hardcoded bypass detected in {s.name}")

    # 2. Check token validity and freshness
    token_p = ROOT / 'scratch' / 'wyvern_token.txt'
    if not token_p.exists():
        cheating_flags.append("wyvern_token.txt does not exist")
    else:
        token = token_p.read_text(encoding='utf-8').strip()
        if len(token) < 100 or not token.startswith('eyJ'):
            cheating_flags.append("wyvern_token.txt does not appear to be a genuine JWT token")

    # 3. Check git diff for real work vs dummy placeholders
    p = ROOT / 'FINAL' / 'Noah_Douglas_Bloodmoon_card.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    if len(d['description']) < 5000:
        cheating_flags.append("Noah description is suspiciously small (<5000 chars)")

    if cheating_flags:
        results["phase_b_cheating"]["status"] = "FAIL"
        for cf in cheating_flags:
            log("phase_b_cheating", f"  FLAG: {cf}")
        return False
    else:
        results["phase_b_cheating"]["status"] = "PASS"
        log("phase_b_cheating", "ZERO CHEATING OR FACADE PATTERNS DETECTED (PASS)")
        return True

def run_phase_c_independent_live_api():
    print("=" * 80)
    print("INDEPENDENT VICTORY AUDITOR — LIVE WYVERN WEB API EXECUTION")
    print("=" * 80)
    api_failures = []

    # Refresh token fresh
    print("Refreshing live bearer token...")
    token = refresh_token.refresh()
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'IndependentVictoryAuditor/1.0'
    }

    def fetch_api(endpoint):
        url = f"https://app.wyvern.chat/api{endpoint}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode('utf-8'))

    # 1. 8 Character Cards
    final_cards = [
        ('_TbRM3EdxDjHFgqztTbCpL', 'Edric_Douglas_card.json', 'AGE: 13 (Born February 25, 2011)'),
        ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik_Douglas_card.json', 'AGE: 55 (Born October 31, 1969)'),
        ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper_Douglas_Bloodmoon_card.json', 'AGE: 19 (Born April 22, 2005)'),
        ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan_Douglas_card.json', 'AGE: 49 (Born January 12, 1975)'),
        ('_zn24784jfcchQ7EwCyAnm', 'Mackenzie_Sanchez_Rogers_card.json', 'AGE: 19 (Born November 14, 2004)'),
        ('_RDfz7XzTpM23LpPALVXHM', 'Malachia_Douglas_Bloodmoon_card.json', 'AGE: 28 (Born August 10, 1996)'),
        ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah_Douglas_Bloodmoon_card.json', 'AGE: 25 (Born October 5, 1998)'),
        ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic_Bloodmoon_card.json', 'AGE: 1200 (Born December 21, 824 AD)'),
    ]

    for cid, fname, expected_age in final_cards:
        try:
            status, data = fetch_api(f"/characters/{cid}")
            if status != 200:
                api_failures.append(f"GET /characters/{cid} returned status {status}")
                continue
            desc = data.get('description', '')
            line1 = desc.split('\n')[0]
            if expected_age not in line1:
                api_failures.append(f"Live card {cid} ({fname}): expected '{expected_age}' not found in line 1")
            pers = data.get('personality', '').strip()
            if not (pers.startswith('[') and pers.endswith(']')):
                api_failures.append(f"Live card {cid} ({fname}): personality not enclosed in [...]")
            if '—' in desc or '—' in pers:
                api_failures.append(f"Live card {cid} ({fname}): em-dash found in live text")
            if '*' in desc or '*' in pers:
                api_failures.append(f"Live card {cid} ({fname}): asterisk found in live text")
            log("phase_c_live_api", f"Live Card Verified: {fname} ({cid}) - HTTP 200")
        except Exception as e:
            api_failures.append(f"Exception during GET /characters/{cid}: {e}")

    # 2. 3 User Personas
    personas = [
        ('persona_1786335754946', 'Alyssa_Persona.json', 'AGE: 19 (Born April 22, 2005)'),
        ('1792155173728', 'Jasper_Persona.json', 'AGE: 19 (Born April 22, 2005)'),
        ('1791389790053', 'Echo_Persona.json', 'AGE: 3 (Activated November 15, 2021)'),
    ]

    for pid, fname, expected_age in personas:
        try:
            status, data = fetch_api(f"/user-personas/{pid}")
            if status != 200:
                api_failures.append(f"GET /user-personas/{pid} returned status {status}")
                continue
            desc = data.get('description', '')
            line1 = desc.split('\n')[0]
            if expected_age not in line1:
                api_failures.append(f"Live persona {pid} ({fname}): expected '{expected_age}' not found in line 1")
            if data.get('can_fork') is not True:
                api_failures.append(f"Live persona {pid} ({fname}): can_fork is not True")
            log("phase_c_live_api", f"Live Persona Verified: {fname} ({pid}) - HTTP 200")
        except Exception as e:
            api_failures.append(f"Exception during GET /user-personas/{pid}: {e}")

    # 3. 4 Lorebooks
    # NPC Primary
    try:
        status, lb_pri = fetch_api("/lorebooks/_zwEqgEEzh12X6gHVmMKKC")
        if status != 200:
            api_failures.append(f"GET /lorebooks/_zwEqgEEzh12X6gHVmMKKC returned {status}")
        else:
            entries = lb_pri.get('lexicon', lb_pri.get('entries', []))
            if len(entries) != 99:
                api_failures.append(f"Live NPC Primary entry count mismatch: {len(entries)} != 99")
            
            # Check 1:1 match for Erik, Malachia, Noah, Logan, Wulfnic, Mackenzie
            core_primary = [
                ('Erik_Douglas_card.json', 'C-JisFj8qA1tsFEqZKevk'),
                ('Malachia_Douglas_Bloodmoon_card.json', 'jDuJtzirlEZC3K_ArIufh'),
                ('Noah_Douglas_Bloodmoon_card.json', 'H2JX-NkHRiJ2FzoekC5ZZ'),
                ('Logan_Douglas_card.json', 'tAcrWLtWSDGf3xJJRwUOM'),
                ('Wulfnic_Bloodmoon_card.json', 'HhuMluMmIIENUei3bX6ed'),
                ('Mackenzie_Sanchez_Rogers_card.json', 'BXi3sENAVYB8OKF80Q9Su'),
            ]
            for cfile, eid in core_primary:
                cdesc = json.loads((ROOT / 'FINAL' / cfile).read_text(encoding='utf-8'))['description']
                live_e = next((e for e in entries if e.get('entry_id') == eid), None)
                if not live_e or live_e.get('content') != cdesc:
                    api_failures.append(f"Live 1:1 mismatch in NPC Primary for {cfile}")

            # Check Ut Berg & Zefir
            ut_live = next((e for e in entries if e.get('entry_id') == 'QLKp7v-jamdpsEz7GMgqB'), None)
            if not ut_live or "AGE: 1205 (Born May 5, 819 AD); turned at 45 in 864 AD; presented age: 60;" not in ut_live.get('content', ''):
                api_failures.append("Live Ut Berg in NPC Primary missing canonical dates/apparent age")

            zef_live = next((e for e in entries if e.get('entry_id') == 'aA5zIYvLivjMts978RWEn'), None)
            if not zef_live or "AGE: 1176 (Born February 5, 848 AD); turned at 16 in 864 AD; presented age: 20-22;" not in zef_live.get('content', ''):
                api_failures.append("Live Zefir in NPC Primary missing canonical dates/apparent age")
            if not zef_live or "North Sea wind" not in zef_live.get('content', ''):
                api_failures.append("Live Zefir in NPC Primary missing North Sea Wind personality")

            log("phase_c_live_api", f"Live Lorebook NPC Primary (_zwEqgEEzh12X6gHVmMKKC) Verified - 99 entries - HTTP 200")
    except Exception as e:
        api_failures.append(f"Exception during NPC Primary live check: {e}")

    # NPC Secondary
    try:
        status, lb_sec = fetch_api("/lorebooks/_Uht3Ckz44JBDrPnUHq7LV")
        if status != 200:
            api_failures.append(f"GET /lorebooks/_Uht3Ckz44JBDrPnUHq7LV returned {status}")
        else:
            entries = lb_sec.get('lexicon', lb_sec.get('entries', []))
            if len(entries) != 211:
                api_failures.append(f"Live NPC Secondary entry count mismatch: {len(entries)} != 211")
            edric_desc = json.loads((ROOT / 'FINAL' / 'Edric_Douglas_card.json').read_text(encoding='utf-8'))['description']
            live_edric = next((e for e in entries if e.get('entry_id') == 'h-ttmlgJYeRXqyDvQjSX7'), None)
            if not live_edric or live_edric.get('content') != edric_desc:
                api_failures.append("Live 1:1 mismatch in NPC Secondary for Edric_Douglas_card.json")
            log("phase_c_live_api", f"Live Lorebook NPC Secondary (_Uht3Ckz44JBDrPnUHq7LV) Verified - 211 entries - HTTP 200")
    except Exception as e:
        api_failures.append(f"Exception during NPC Secondary live check: {e}")

    # Lorebook I
    try:
        status, lb1 = fetch_api("/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL")
        if status != 200:
            api_failures.append(f"GET /lorebooks/_gwwCxCfQ6PQaLEjAQVpJL returned {status}")
        else:
            entries = lb1.get('lexicon', lb1.get('entries', []))
            if len(entries) != 221:
                api_failures.append(f"Live Lorebook I count mismatch: {len(entries)} != 221")
            e_lb1 = next((e for e in entries if e.get('entry_id') == 'HxdpzBtgY_wSx5ZpIDzGK'), None)
            if not e_lb1 or "824 d.C." not in e_lb1.get('content', '') or "849 d.C." not in e_lb1.get('content', '') or "864 d.C." not in e_lb1.get('content', ''):
                api_failures.append("Live Lorebook I entry HxdpzBtgY_wSx5ZpIDzGK missing canonical dates")
            log("phase_c_live_api", f"Live Lorebook I (_gwwCxCfQ6PQaLEjAQVpJL) Verified - 221 entries - HTTP 200")
    except Exception as e:
        api_failures.append(f"Exception during Lorebook I live check: {e}")

    # Lorebook II
    try:
        status, lb2 = fetch_api("/lorebooks/_HfG7TeV6MJyj6bxMwxkpt")
        if status != 200:
            api_failures.append(f"GET /lorebooks/_HfG7TeV6MJyj6bxMwxkpt returned {status}")
        else:
            entries = lb2.get('lexicon', lb2.get('entries', []))
            if len(entries) != 142:
                api_failures.append(f"Live Lorebook II count mismatch: {len(entries)} != 142")
            e51 = next((e for e in entries if e.get('entry_id') == 'nbeEd2cvkA5PLke6svWez'), None)
            if not e51 or "Born December 21, 824 AD in Iceland." not in e51.get('content', ''):
                api_failures.append("Live Lorebook II entry nbeEd2cvkA5PLke6svWez missing canonical dates")
            log("phase_c_live_api", f"Live Lorebook II (_HfG7TeV6MJyj6bxMwxkpt) Verified - 142 entries - HTTP 200")
    except Exception as e:
        api_failures.append(f"Exception during Lorebook II live check: {e}")

    if api_failures:
        results["phase_c_live_api"]["status"] = "FAIL"
        for af in api_failures:
            log("phase_c_live_api", f"  API FAILURE: {af}")
        return False
    else:
        results["phase_c_live_api"]["status"] = "PASS"
        log("phase_c_live_api", "ALL LIVE API ENDPOINTS INDEPENDENTLY VERIFIED (100% SUCCESS)")
        return True

if __name__ == '__main__':
    ok_a = run_phase_a_and_b_local()
    ok_b = run_phase_b_cheating_audit()
    ok_c = run_phase_c_independent_live_api()
    overall = ok_a and ok_b and ok_c
    print("\n" + "=" * 80)
    print(f"OVERALL AUDIT VERDICT: {'VICTORY CONFIRMED' if overall else 'VICTORY REJECTED'}")
    print("=" * 80)
    sys.exit(0 if overall else 1)
