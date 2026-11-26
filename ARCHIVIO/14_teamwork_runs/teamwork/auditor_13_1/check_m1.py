import json
import filecmp

targets = [
    ('Alyssa Card', 'ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json', 'description', "155 cm (5' 1\")"),
    ('Jasper Card', 'FINAL/Jasper_Douglas_Bloodmoon_card.json', 'description', "193 cm (6' 4\")"),
    ('Noah Card', 'FINAL/Noah_Douglas_Bloodmoon_card.json', 'description', "197 cm (6' 5.6\")"),
    ('Malachia Card', 'FINAL/Malachia_Douglas_Bloodmoon_card.json', 'description', "208 cm (6' 9.9\")"),
    ('Erik Card', 'FINAL/Erik_Douglas_card.json', 'description', "213 cm (6' 11.9\")"),
    ('Wulfnic Card', 'FINAL/Wulfnic_Bloodmoon_card.json', 'description', "220 cm (7' 2.6\")"),
    ('Alyssa Persona', 'FINAL/personas/Alyssa_Persona.json', 'description', "155 cm (5' 1\")"),
    ('Jasper Persona', 'FINAL/personas/Jasper_Persona.json', 'description', "193 cm (6' 4\")")
]

for label, path, key, expected_ht in targets:
    data = json.load(open(path, encoding='utf-8'))
    text = data[key]
    lines = text.split('\n')
    line0 = lines[0]
    assert line0.startswith('['), f'{label} line 0 does not start with ['
    assert line0.endswith(']'), f'{label} line 0 does not end with ]'
    assert expected_ht in line0, f'{label} line 0 does not contain {expected_ht}'
    print(f'[PASS] {label}: valid bracket line 0, contains {expected_ht}')

# Check Lorebook Primary entries == lexicon and target heights
lb1 = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
lb2 = json.load(open('lorebooks/optimized/Svartulfr_NPC_Primary.json', encoding='utf-8'))

assert lb1['entries'] == lb1['lexicon'], "FINAL lorebook entries != lexicon"
assert lb2['entries'] == lb2['lexicon'], "Optimized lorebook entries != lexicon"
assert filecmp.cmp('FINAL/Svartulfr_NPC_Primary.json', 'lorebooks/optimized/Svartulfr_NPC_Primary.json', shallow=False), "FINAL != Optimized"

print("[PASS] Lorebook internal entries == lexicon and mirror filecmp verified byte-for-byte!")

# Check entries count and target entry heights
print(f"Total entries in Primary Lorebook: {len(lb1['entries'])}")
assert len(lb1['entries']) == 99, f"Expected 99 entries, got {len(lb1['entries'])}"

target_ids = {
    'alyssa_world_dossier_2b54a223': ("Alyssa", "155 cm (5' 1\")"),
    'Vcj4h2TL4Usola2A4OOl6': ("Jasper", "193 cm (6' 4\")"),
    'H2JX-NkHRiJ2FzoekC5ZZ': ("Noah", "197 cm (6' 5.6\")"),
    'jDuJtzirlEZC3K_ArIufh': ("Malachia", "208 cm (6' 9.9\")"),
    'C-JisFj8qA1tsFEqZKevk': ("Erik", "213 cm (6' 11.9\")"),
    'HhuMluMmIIENUei3bX6ed': ("Wulfnic", "220 cm (7' 2.6\")")
}

for entry in lb1['entries']:
    eid = entry.get('entry_id')
    if eid in target_ids:
        cname, expected_ht = target_ids[eid]
        lines = entry['content'].split('\n')
        line0 = lines[0]
        assert line0.startswith('[') and line0.endswith(']'), f"Lorebook {cname} line 0 bracket error"
        assert expected_ht in line0, f"Lorebook {cname} missing {expected_ht}"
        assert 'PROPORTIONS & SCALE:' in entry['content'], f"Lorebook {cname} missing PROPORTIONS & SCALE"
        print(f"[PASS] Lorebook NPC {cname} ({eid}) verified: {expected_ht}")

# Check style_guide.md
sg = open('database/assets/style_guide.md', encoding='utf-8').read()
clauses = [
    "Alyssa (155 cm) arriva all'altezza della spalla di Jasper (193 cm, -38 cm).",
    "Malachia (208 cm) supera Alyssa di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a metà del torace mastodontico.",
    "Erik (213 cm) e Wulfnic (220 cm) sovrastano Alyssa di 58-65 cm (lei arriva alla parte bassa del petto / sterno)."
]
for clause in clauses:
    assert clause in sg, f"Missing clause in style_guide.md: {clause}"
    print(f"[PASS] Style guide contains clause: {clause[:40]}...")

print("\nALL INDEPENDENT M1 INTEGRITY CHECKS PASSED!")
