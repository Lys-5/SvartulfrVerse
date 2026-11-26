import json
import pathlib
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

def check_forensics():
    print("=" * 60)
    print("INDEPENDENT FORENSIC & CANONICAL INVARIANT CHECK")
    print("=" * 60)

    # 1. Noah Douglas Bloodmoon
    noah = json.loads((ROOT / 'FINAL' / 'Noah_Douglas_Bloodmoon_card.json').read_text(encoding='utf-8'))
    desc = noah['description']
    lines = desc.split('\n')
    assert lines[0].startswith('[') and lines[0].endswith(']'), "Noah line 1 not [...]"
    assert '\n' not in lines[0], "Noah line 1 contains newline"
    assert lines[0].count('BIRTH_RUNE:') == 1, f"Noah line 1 has {lines[0].count('BIRTH_RUNE:')} BIRTH_RUNE: entries"
    assert desc.count('BACKSTORY:') == 1, f"Noah description has {desc.count('BACKSTORY:')} BACKSTORY: headers"
    for nested in ['BACKSTORY:', 'PERSONALITY:', 'WEAKNESSES:', 'SPACES:']:
        assert nested not in lines[0], f"Noah line 1 still has nested section '{nested}'"
    print("PASS: Noah Douglas Bloodmoon card clean single-line PList & single BACKSTORY header.")

    # 2. Malachia Douglas Bloodmoon
    mal = json.loads((ROOT / 'FINAL' / 'Malachia_Douglas_Bloodmoon_card.json').read_text(encoding='utf-8'))
    m_desc = mal['description']
    idx_b = m_desc.find('BACKSTORY:')
    idx_v = m_desc.find('VOICE & BEHAVIOR:')
    idx_dist = m_desc.find('THE DISTANCE HE HAS ALREADY CLOSED:')
    assert idx_dist != -1, "Malachia missing THE DISTANCE HE HAS ALREADY CLOSED:"
    assert idx_v < idx_dist, f"THE DISTANCE HE HAS ALREADY CLOSED ({idx_dist}) should be after VOICE & BEHAVIOR ({idx_v})"
    assert '*' not in mal.get('mes_example', ''), f"Asterisk found in Malachia mes_example: {mal.get('mes_example')}"
    print("PASS: Malachia section order and mes_example clean.")

    # 3. Echo Persona
    echo = json.loads((ROOT / 'FINAL' / 'personas' / 'Echo_Persona.json').read_text(encoding='utf-8'))
    e_desc = echo['description']
    e_line1 = e_desc.split('\n')[0]
    assert "AGE: 3 (Activated November 15, 2021)" in e_line1, f"Echo line 1 missing expected age: {e_line1}"
    assert "BACKSTORY:" in e_desc, "Echo missing BACKSTORY:"
    assert "FAMILY & PACK:" in e_desc, "Echo missing FAMILY & PACK:"
    assert "VOICE & BEHAVIOR:" in e_desc, "Echo missing VOICE & BEHAVIOR:"
    assert "CORE FUNCTIONS & CYBERSPACE WARFARE:" not in e_desc, "Echo still has CORE FUNCTIONS header"
    assert "MONITORING SYSTEM & FAMILIAR PROTOCOLS:" not in e_desc, "Echo still has MONITORING SYSTEM header"
    assert "PERSONALITY & HUMOR:" not in e_desc, "Echo still has PERSONALITY & HUMOR header"
    print("PASS: Echo Persona 4-block schema and activation date verified.")

    # 4. Russ card & Legacy
    russ = json.loads((ROOT / 'ARCHIVIO' / 'cards_legacy' / 'Russ_card.json').read_text(encoding='utf-8'))
    r_desc = russ['description']
    assert "CLAN AND COMPANY:" in r_desc, "Russ missing CLAN AND COMPANY:"
    idx_rb = r_desc.find('BACKSTORY:')
    idx_rc = r_desc.find('CLAN AND COMPANY:')
    idx_rv = r_desc.find('VOICE & BEHAVIOR:')
    assert idx_rb < idx_rc < idx_rv, "Russ order violation"
    print("PASS: Russ legacy card CLAN AND COMPANY insertion verified.")

    scarlett = json.loads((ROOT / 'ARCHIVIO' / 'cards_legacy' / 'Scarlett_Rose_card.json').read_text(encoding='utf-8'))
    assert "CLAN AND COMPANY:" in scarlett['description'], "Scarlett missing CLAN AND COMPANY:"
    assert "DORM DYNAMICS & ROOMMATES:" not in scarlett['description'], "Scarlett still has DORM DYNAMICS"
    print("PASS: Scarlett Rose legacy card CLAN AND COMPANY verified.")

    sierra = json.loads((ROOT / 'ARCHIVIO' / 'cards_legacy' / 'Sierra_Cruz_card.json').read_text(encoding='utf-8'))
    assert "CLAN AND COMPANY:" in sierra['description'], "Sierra missing CLAN AND COMPANY:"
    assert "DORM DYNAMICS & ROOMMATES:" not in sierra['description'], "Sierra still has DORM DYNAMICS"
    print("PASS: Sierra Cruz legacy card CLAN AND COMPANY verified.")

    jared = json.loads((ROOT / 'ARCHIVIO' / 'cards_legacy' / 'Jared_Thompson_card.json').read_text(encoding='utf-8'))
    assert jared['description'].count('FAMILY & PACK:') == 1, "Jared has duplicate FAMILY & PACK:"
    assert "FAMILY:" not in jared['description'].replace('FAMILY & PACK:', ''), "Jared still has standalone FAMILY:"
    print("PASS: Jared Thompson legacy card FAMILY consolidation verified.")

    # 5. Core Lorebook Ignored Characters
    p_lb = json.loads((ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
    core_ign = {
        'C-JisFj8qA1tsFEqZKevk': '_QPea6g4Q1QfeYCVHCLMPR', # Erik
        'jDuJtzirlEZC3K_ArIufh': '_RDfz7XzTpM23LpPALVXHM', # Malachia
        'H2JX-NkHRiJ2FzoekC5ZZ': '_zFLUjV8aVxQRAfQxGcAcY', # Noah
        'tAcrWLtWSDGf3xJJRwUOM': '_T8Ywcr9FEqNf9JxbK6eHP', # Logan
        'HhuMluMmIIENUei3bX6ed': '_HEQQbbRFwKdG8QE2Fh1z1', # Wulfnic
        'BXi3sENAVYB8OKF80Q9Su': '_zn24784jfcchQ7EwCyAnm', # Mackenzie
    }
    for eid, cid in core_ign.items():
        entry = next(e for e in p_lb['lexicon'] if e.get('entry_id') == eid)
        assert cid in entry.get('ignored_characters', []), f"{entry.get('name')} missing {cid} in ignored_characters"
    print("PASS: Svartulfr_NPC_Primary ignored_characters correctly configured.")

    s_lb = json.loads((ROOT / 'FINAL' / 'Svartulfr_NPC_Secondary.json').read_text(encoding='utf-8'))
    edric_e = next(e for e in s_lb['lexicon'] if e.get('entry_id') == 'h-ttmlgJYeRXqyDvQjSX7')
    assert '_TbRM3EdxDjHFgqztTbCpL' in edric_e.get('ignored_characters', []), "Edric missing card id in ignored_characters"
    assert edric_e.get('type') == 'npc', "Edric is not type npc"
    assert edric_e.get('selective') is False, "Edric is not selective false"
    print("PASS: Svartulfr_NPC_Secondary Edric entry verified.")

    # 6. Check that FINAL/ contains ONLY the 8 approved cards and no legacy cards
    final_card_files = sorted([f.name for f in (ROOT / 'FINAL').glob('*_card.json')])
    expected_8_cards = sorted([
        'Edric_Douglas_card.json',
        'Erik_Douglas_card.json',
        'Jasper_Douglas_Bloodmoon_card.json',
        'Logan_Douglas_card.json',
        'Mackenzie_Sanchez_Rogers_card.json',
        'Malachia_Douglas_Bloodmoon_card.json',
        'Noah_Douglas_Bloodmoon_card.json',
        'Wulfnic_Bloodmoon_card.json'
    ])
    assert final_card_files == expected_8_cards, f"FINAL/*_card.json files mismatch: {final_card_files} vs {expected_8_cards}"
    print("PASS: FINAL directory contains strictly the 8 canonical character cards.")

    print("\nALL FORENSIC CHECKS PASSED!")

if __name__ == '__main__':
    check_forensics()
