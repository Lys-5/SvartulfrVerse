import json
import pathlib
import shutil
import urllib.request

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
final_dir = ROOT / 'FINAL'
archivio_cards_dir = ROOT / 'ARCHIVIO' / 'cards_legacy'
backup_dir = ROOT / 'scratch' / 'backup_deleted_cards_20261021'

backup_dir.mkdir(parents=True, exist_ok=True)
archivio_cards_dir.mkdir(parents=True, exist_ok=True)

token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

jared_id = '_xJVPtBLL3dxy69RLKL9X9'

# Step 1: Pre-delete snapshot of Jared
get_req = urllib.request.Request(f'https://app.wyvern.chat/api/characters/{jared_id}', headers=headers)
with urllib.request.urlopen(get_req, timeout=30) as resp:
    assert resp.status == 200, f"Failed to GET Jared: {resp.status}"
    jared_live = json.loads(resp.read().decode('utf-8'))

snapshot_file = backup_dir / f'DELETED_Jared_Thompson_{jared_id}.json'
snapshot_file.write_text(json.dumps(jared_live, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"Saved snapshot of Jared Thompson to {snapshot_file} ({snapshot_file.stat().st_size} bytes)")

# Step 2: Execute DELETE
del_req = urllib.request.Request(f'https://app.wyvern.chat/api/characters/{jared_id}', headers=headers, method='DELETE')
try:
    with urllib.request.urlopen(del_req, timeout=30) as resp:
        print(f"DELETE Jared Thompson -> HTTP {resp.status}")
        assert resp.status in (200, 204), f"Expected 200 or 204, got {resp.status}"
except urllib.error.HTTPError as e:
    print(f"DELETE Jared Thompson error: HTTP {e.code} - {e.read().decode('utf-8')}")
    raise

# Step 3: Verify /characters/mine has exactly 8 approved cards
mine_req = urllib.request.Request('https://app.wyvern.chat/api/characters/mine', headers=headers)
with urllib.request.urlopen(mine_req, timeout=30) as resp:
    assert resp.status == 200
    mine_data = json.loads(resp.read().decode('utf-8'))

mine_chars = mine_data.get('characters', [])
print(f"\nCharacters remaining in /characters/mine: {len(mine_chars)}")
for c in mine_chars:
    print(f"  {c.get('id')} | {c.get('name')}")

assert len(mine_chars) == 8, f"Expected exactly 8 characters, got {len(mine_chars)}"

approved_ids = {
    '_QPea6g4Q1QfeYCVHCLMPR': 'Erik Ulfr Douglas',
    '_RDfz7XzTpM23LpPALVXHM': 'Malachia Björn Douglas Bloodmoon',
    '_t4J9aQNJM36cUKAP4wB4U': 'Jasper Svartr Douglas Bloodmoon',
    '_zFLUjV8aVxQRAfQxGcAcY': 'Noah Loki Douglas Bloodmoon',
    '_TbRM3EdxDjHFgqztTbCpL': 'Edric Douglas',
    '_T8Ywcr9FEqNf9JxbK6eHP': 'Logan Dominic Járn Douglas',
    '_HEQQbbRFwKdG8QE2Fh1z1': 'Wulfnic Báleygr Bloodmoon',
    '_zn24784jfcchQ7EwCyAnm': 'Mackenzie Sanchez-Rogers'
}

live_ids = {c.get('id') for c in mine_chars}
assert live_ids == set(approved_ids.keys()), f"Mismatch in approved IDs! Diff: {live_ids ^ set(approved_ids.keys())}"
print("Live /characters/mine contains exactly the 8 approved cards!")

# Step 4: Move 6 disused card files to ARCHIVIO/cards_legacy/
disused_cards = [
    'Alyssa_Douglas_Bloodmoon_card.json',
    'Jared_Thompson_card.json',
    'Russ_card.json',
    'Scarlett_Rose_card.json',
    'Sierra_Cruz_card.json',
    'Stan_Davies_Jr_card.json'
]

for card_name in disused_cards:
    src = final_dir / card_name
    dst = archivio_cards_dir / card_name
    if src.exists():
        shutil.move(str(src), str(dst))
        print(f"Moved {card_name} -> ARCHIVIO/cards_legacy/")
    else:
        print(f"{card_name} not in FINAL/, check ARCHIVIO: {dst.exists()}")

# Step 5: Verify FINAL/ contains only the 8 approved cards
remaining_cards = sorted([f.name for f in final_dir.glob('*_card.json')])
print(f"\nRemaining card files in FINAL/ ({len(remaining_cards)}):")
for f in remaining_cards:
    print(f"  {f}")

assert len(remaining_cards) == 8, f"Expected 8 card files, got {len(remaining_cards)}"

expected_final_cards = [
    'Edric_Douglas_card.json',
    'Erik_Douglas_card.json',
    'Jasper_Douglas_Bloodmoon_card.json',
    'Logan_Douglas_card.json',
    'Mackenzie_Sanchez_Rogers_card.json',
    'Malachia_Douglas_Bloodmoon_card.json',
    'Noah_Douglas_Bloodmoon_card.json',
    'Wulfnic_Bloodmoon_card.json'
]

assert remaining_cards == expected_final_cards, f"Mismatch in FINAL/ card files: {remaining_cards}"

archived_cards = sorted([f.name for f in archivio_cards_dir.glob('*_card.json')])
print(f"\nArchived card files in ARCHIVIO/cards_legacy/ ({len(archived_cards)}):")
for f in archived_cards:
    print(f"  {f}")
assert len(archived_cards) == 6, f"Expected 6 archived files, got {len(archived_cards)}"

print("\nTask 3 finished successfully!")
