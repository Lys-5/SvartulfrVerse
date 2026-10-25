import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
final_cards = [
    ('Edric_Douglas_card.json', '_TbRM3EdxDjHFgqztTbCpL'),
    ('Erik_Douglas_card.json', '_QPea6g4Q1QfeYCVHCLMPR'),
    ('Jasper_Douglas_Bloodmoon_card.json', '_t4J9aQNJM36cUKAP4wB4U'),
    ('Logan_Douglas_card.json', '_T8Ywcr9FEqNf9JxbK6eHP'),
    ('Mackenzie_Sanchez_Rogers_card.json', '_zn24784jfcchQ7EwCyAnm'),
    ('Malachia_Douglas_Bloodmoon_card.json', '_RDfz7XzTpM23LpPALVXHM'),
    ('Noah_Douglas_Bloodmoon_card.json', '_zFLUjV8aVxQRAfQxGcAcY'),
    ('Wulfnic_Bloodmoon_card.json', '_HEQQbbRFwKdG8QE2Fh1z1')
]

for fname, expected_id in final_cards:
    d = json.loads((ROOT / 'FINAL' / fname).read_text(encoding='utf-8'))
    fid = d.get('id') or d.get('_id')
    assert fid == expected_id, f"{fname} id mismatch: {fid} vs {expected_id}"
    print(f"Match: {fname} -> {fid} ({d.get('name')})")

print("ALL 8 CHARACTER CARD IDS MATCH 100%!")
