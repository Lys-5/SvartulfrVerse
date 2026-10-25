import json
import pathlib
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

def verify_live():
    print("=" * 70)
    print("EXHAUSTIVE LIVE API VERIFICATION")
    print("=" * 70)

    # 1. 8 CHARACTER CARDS
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

    print("\n--- Verifying 8 Live Character Cards via GET /api/characters/:id ---")
    for cid, fname, expected_age in final_cards:
        st, live_c = api_get(f"{API_APP}/characters/{cid}")
        assert st == 200, f"Failed GET for {fname} ({cid}): status {st}"
        
        desc = live_c.get('description', '')
        line1 = desc.split('\n')[0]
        assert line1.startswith('['), f"Live {fname}: Line 1 does not start with ["
        assert line1.endswith(']'), f"Live {fname}: Line 1 does not end with ]"
        assert expected_age in line1, f"Live {fname}: Expected '{expected_age}' not found in line 1"
        
        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find('FAMILY & PACK:')
        idx_v = desc.find('VOICE & BEHAVIOR:')
        assert idx_b != -1 and idx_f != -1 and idx_v != -1, f"Live {fname}: Missing one of core headers"
        assert idx_b < idx_f < idx_v, f"Live {fname}: Order violation in headers"
        
        pers = live_c.get('personality', '').strip()
        assert pers.startswith('[') and pers.endswith(']'), f"Live {fname}: Personality not in [...]"
        assert not pers.endswith(','), f"Live {fname}: Personality ends with comma"
        assert not pers.endswith('...'), f"Live {fname}: Personality ends with ellipsis"
        assert 'NAME:' in pers, f"Live {fname}: Personality missing NAME:"
        assert 'ROLE:' in pers, f"Live {fname}: Personality missing ROLE:"
        assert 'TRAITS:' in pers, f"Live {fname}: Personality missing TRAITS:"
        assert 'CORE:' in pers, f"Live {fname}: Personality missing CORE:"
        assert expected_age in pers, f"Live {fname}: Expected '{expected_age}' not found in personality"
        
        for field in ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']:
            val = live_c.get(field, '')
            if isinstance(val, str):
                assert '—' not in val, f"Live {fname}: em-dash found in {field}"
                assert '*' not in val, f"Live {fname}: asterisk found in {field}"
                
        print(f"  PASS: Live card {fname} ({cid}) - Name: {live_c.get('name')}")

    # 2. 3 USER PERSONAS
    personas = [
        ('persona_1786335754946', 'Alyssa_Persona.json', 'AGE: 19 (Born April 22, 2005)'),
        ('1792155173728', 'Jasper_Persona.json', 'AGE: 19 (Born April 22, 2005)'),
        ('1791389790053', 'Echo_Persona.json', 'AGE: 3 (Activated November 15, 2021)'),
    ]

    print("\n--- Verifying 3 Live User Personas via GET /api/user-personas/:id ---")
    for pid, fname, expected_age in personas:
        st, live_p = api_get(f"{API_APP}/user-personas/{pid}")
        assert st == 200, f"Failed GET for persona {fname} ({pid}): status {st}"
        
        desc = live_p.get('description', '')
        line1 = desc.split('\n')[0]
        assert line1.startswith('['), f"Live persona {fname}: Line 1 does not start with ["
        assert line1.endswith(']'), f"Live persona {fname}: Line 1 does not end with ]"
        assert expected_age in line1, f"Live persona {fname}: Expected '{expected_age}' not found in line 1"
        
        idx_b = desc.find('BACKSTORY:')
        idx_f = desc.find('FAMILY & PACK:')
        idx_v = desc.find('VOICE & BEHAVIOR:')
        assert idx_b != -1 and idx_f != -1 and idx_v != -1, f"Live persona {fname}: Missing one of core headers"
        assert idx_b < idx_f < idx_v, f"Live persona {fname}: Order violation in headers"
        
        assert live_p.get('can_fork') is True, f"Live persona {fname}: can_fork is not True"
        
        def scan_live_text(obj, path):
            if isinstance(obj, str):
                assert '—' not in obj, f"Live persona {fname}: em-dash in {path}: {obj[:40]}"
                assert '*' not in obj, f"Live persona {fname}: asterisk in {path}: {obj[:40]}"
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    if k not in ['id', '_id', 'avatar', 'backgroundURL', 'image_url']:
                        scan_live_text(v, f"{path}.{k}" if path else k)
            elif isinstance(obj, list):
                for idx, item in enumerate(obj):
                    scan_live_text(item, f"{path}[{idx}]")
        
        scan_live_text(live_p, "")
        
        print(f"  PASS: Live persona {fname} ({pid}) - Name: {live_p.get('name')}")

    # 3. 2 NPC LOREBOOKS
    lorebooks = [
        ('_zwEqgEEzh12X6gHVmMKKC', 99, 'NPC Primary', [
            ('Erik_Douglas_card.json', 'C-JisFj8qA1tsFEqZKevk'),
            ('Malachia_Douglas_Bloodmoon_card.json', 'jDuJtzirlEZC3K_ArIufh'),
            ('Noah_Douglas_Bloodmoon_card.json', 'H2JX-NkHRiJ2FzoekC5ZZ'),
            ('Logan_Douglas_card.json', 'tAcrWLtWSDGf3xJJRwUOM'),
            ('Wulfnic_Bloodmoon_card.json', 'HhuMluMmIIENUei3bX6ed'),
            ('Mackenzie_Sanchez_Rogers_card.json', 'BXi3sENAVYB8OKF80Q9Su'),
        ]),
        ('_Uht3Ckz44JBDrPnUHq7LV', 211, 'NPC Secondary', [
            ('Edric_Douglas_card.json', 'h-ttmlgJYeRXqyDvQjSX7'),
        ])
    ]

    print("\n--- Verifying 2 Live Lorebooks via GET /api/lorebooks/:id ---")
    for lid, expected_count, label, core_targets in lorebooks:
        st, live_lb = api_get(f"{API_APP}/lorebooks/{lid}")
        assert st == 200, f"Failed GET for lorebook {label} ({lid}): status {st}"
        
        entries = live_lb.get('lexicon', live_lb.get('entries', []))
        assert len(entries) == expected_count, f"Lorebook {label} entry count mismatch: {len(entries)} vs {expected_count}"
        
        for card_file, entry_id in core_targets:
            card_desc = json.loads((ROOT / 'FINAL' / card_file).read_text(encoding='utf-8'))['description']
            live_entry = next((e for e in entries if e.get('entry_id') == entry_id), None)
            assert live_entry is not None, f"Entry {entry_id} for {card_file} not found in live lorebook {label}"
            
            live_content = live_entry.get('content', '')
            assert live_content == card_desc, f"1:1 PARITY FAILURE for {card_file} and live entry {entry_id} in {label}!"
            print(f"  PASS: 1:1 Live Parity for {card_file} -> {live_entry.get('name')} ({entry_id}) [len={len(live_content)}]")
            
        print(f"  PASS: Lorebook {label} ({lid}) - Entries: {len(entries)}")

    # 4. LOREBOOK I & II LIVE VERIFICATION
    print("\n--- Verifying Live Lorebook I (_gwwCxCfQ6PQaLEjAQVpJL) ---")
    st, lb1 = api_get(f"{API_APP}/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL")
    assert st == 200
    entries1 = lb1.get('lexicon', lb1.get('entries', []))
    assert len(entries1) == 221, f"Lorebook I count {len(entries1)} != 221"
    e_lb1 = next(e for e in entries1 if e.get('entry_id') == 'HxdpzBtgY_wSx5ZpIDzGK')
    assert "824 d.C." in e_lb1.get('content', '') and "849 d.C." in e_lb1.get('content', '') and "864 d.C." in e_lb1.get('content', '')
    e_lb1_z = next(e for e in entries1 if e.get('entry_id') == 'WTVBwGkRovmXZKfrjYKBw')
    assert "848 d.C." in e_lb1_z.get('content', '') and "864 d.C." in e_lb1_z.get('content', '') and "20-22" in e_lb1_z.get('content', '')
    e_lb1_u = next(e for e in entries1 if e.get('entry_id') == 'pyWwstSbY5IYYvNn-4-hf')
    assert "819 d.C." in e_lb1_u.get('content', '') and "864 d.C." in e_lb1_u.get('content', '') and "60" in e_lb1_u.get('content', '')
    print("  PASS: Live Lorebook I contains canonical 819 / 824 / 848 / 849 / 864 d.C. and apparent ages.")

    print("\n--- Verifying Live Lorebook II (_HfG7TeV6MJyj6bxMwxkpt) ---")
    st, lb2 = api_get(f"{API_APP}/lorebooks/_HfG7TeV6MJyj6bxMwxkpt")
    assert st == 200
    entries2 = lb2.get('lexicon', lb2.get('entries', []))
    assert len(entries2) == 142, f"Lorebook II count {len(entries2)} != 142"
    e51 = next(e for e in entries2 if e.get('entry_id') == 'nbeEd2cvkA5PLke6svWez')
    assert "Born December 21, 824 AD in Iceland." in e51.get('content', '')
    assert "Born May 5, 819 AD in Viking Age Scandinavia; eldest of the Nine at 45 when turned in 864 AD (age 1205 in 2024)." in e51.get('content', '')
    assert "Born 5 February 848 AD. The youngest of the Nine, turned by Fenris at age 16 in 864 AD (age 1176 in 2024)" in e51.get('content', '')
    assert "1005" not in e51.get('content', '')
    e80 = next(e for e in entries2 if e.get('entry_id') == 'qCmzi5J5o-ocZcFJWyovq')
    assert "THE MYTHIC AGE (pre-864 AD)" in e80.get('content', '')
    assert "AGE OF THE FIRSTBORN (~864-1000 AD)" in e80.get('content', '')
    assert "pre-827" not in e80.get('content', '')
    e91 = next(e for e in entries2 if e.get('entry_id') == 'ffB2cSM0T_5MYbddXlzNf')
    assert "Wulfnic nacque nell'824 d.C." in e91.get('content', '')
    assert "Nel 2024, Wulfnic compie 1200 anni." in e91.get('content', '')
    e93 = next(e for e in entries2 if e.get('entry_id') == '21rz_Jv-VaddKBNMya2tf')
    assert "Born December 21, 824 AD" in e93.get('content', '')
    assert "Born May 5, 819 AD; turned at 45 in 864 AD." in e93.get('content', '')
    assert "Born February 5, 848 AD; turned at 16 in 864 AD." in e93.get('content', '')
    print("  PASS: Live Lorebook II contains canonical 819 / 824 / 848 / 849 / 864 AD timeline references across all entries.")

    # 5. LIVE NPC PRIMARY UT BERG & ZEFIR HVITSKOG SPECIFIC CHECKS
    print("\n--- Verifying Live NPC Primary Ut Berg & Zefir Hvitskog ---")
    st_p, lb_p = api_get(f"{API_APP}/lorebooks/_zwEqgEEzh12X6gHVmMKKC")
    assert st_p == 200
    p_entries = lb_p.get('lexicon', lb_p.get('entries', []))
    live_ut = next(e for e in p_entries if e.get('entry_id') == 'QLKp7v-jamdpsEz7GMgqB')
    assert "AGE: 1205 (Born May 5, 819 AD); turned at 45 in 864 AD; presented age: 60;" in live_ut.get('content', '')
    assert "turned by Fenris in 864 AD at age 45, the eldest of the Nine warrior companions" in live_ut.get('content', '')
    print("  PASS: Live Ut Berg has correct 819 AD / 864 AD / presented age 60.")

    live_zef = next(e for e in p_entries if e.get('entry_id') == 'aA5zIYvLivjMts978RWEn')
    assert "AGE: 1176 (Born February 5, 848 AD); turned at 16 in 864 AD; presented age: 20-22;" in live_zef.get('content', '')
    assert "FACE: Youthful, sharp Viking features (16 years old in the 9th century, reading as a 20-22 year old young man to modern eyes)" in live_zef.get('content', '')
    assert "North Sea wind" in live_zef.get('content', '')
    assert "He was born in 848 AD" in live_zef.get('content', '')
    assert "1005" not in live_zef.get('content', '')
    print("  PASS: Live Zefir has correct 848 AD / 864 AD / presented age 20-22 / North Sea Wind.")

    print("\n" + "=" * 70)
    print("ALL LIVE WYVERN API VERIFICATIONS PASSED WITH 100% SUCCESS!")
    print("=" * 70)

if __name__ == '__main__':
    verify_live()
