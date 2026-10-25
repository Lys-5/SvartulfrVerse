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

def scan_obj(obj, path, label, found_issues):
    if isinstance(obj, str):
        if '—' in obj:
            found_issues.append(f"[EM-DASH in {path}] {label}: {repr(obj[:100])}")
        if '*' in obj:
            # Check if it's markdown or emote
            found_issues.append(f"[ASTERISK in {path}] {label}: {repr(obj[:100])}")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            # Skip read-only metadata fields that might contain system hashes
            if k in ['id', '_id', 'avatar', 'backgroundURL', 'image_url']:
                continue
            scan_obj(v, f"{path}.{k}" if path else k, label, found_issues)
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            scan_obj(item, f"{path}[{idx}]", label, found_issues)

def audit_entire_live_state():
    print("=" * 80)
    print("ADVERSARIAL LIVE AUDIT OF ALL ENTITIES")
    print("=" * 80)

    found_issues = []

    # 1. 8 Live Characters
    final_cards = [
        ('_TbRM3EdxDjHFgqztTbCpL', 'Edric'),
        ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik'),
        ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper'),
        ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan'),
        ('_zn24784jfcchQ7EwCyAnm', 'Mackenzie'),
        ('_RDfz7XzTpM23LpPALVXHM', 'Malachia'),
        ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah'),
        ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic'),
    ]

    print("\n--- Auditing 8 Live Characters ---")
    for cid, name in final_cards:
        st, data = api_get(f"{API_APP}/characters/{cid}")
        scan_obj(data, "", f"Character {name} ({cid})", found_issues)

    # 2. 3 Live User Personas
    personas = [
        ('persona_1786335754946', 'Alyssa'),
        ('1792155173728', 'Jasper'),
        ('1791389790053', 'Echo'),
    ]

    print("\n--- Auditing 3 Live Personas ---")
    for pid, name in personas:
        st, data = api_get(f"{API_APP}/user-personas/{pid}")
        scan_obj(data, "", f"Persona {name} ({pid})", found_issues)

    # 3. 2 Live Lorebooks
    lorebooks = [
        ('_zwEqgEEzh12X6gHVmMKKC', 'NPC Primary'),
        ('_Uht3Ckz44JBDrPnUHq7LV', 'NPC Secondary'),
    ]

    print("\n--- Auditing 2 Live Lorebooks ---")
    for lid, name in lorebooks:
        st, data = api_get(f"{API_APP}/lorebooks/{lid}")
        # Only scan the core entries to avoid unrelated entries
        entries = data.get('lexicon', data.get('entries', []))
        core_ids = [
            'C-JisFj8qA1tsFEqZKevk', 'jDuJtzirlEZC3K_ArIufh', 'H2JX-NkHRiJ2FzoekC5ZZ',
            'tAcrWLtWSDGf3xJJRwUOM', 'HhuMluMmIIENUei3bX6ed', 'BXi3sENAVYB8OKF80Q9Su',
            'h-ttmlgJYeRXqyDvQjSX7'
        ]
        for e in entries:
            if e.get('entry_id') in core_ids:
                scan_obj(e.get('content', ''), f"entry[{e.get('entry_id')}].content", f"Lorebook {name} ({e.get('name')})", found_issues)

    print("\n" + "=" * 80)
    print(f"LIVE AUDIT FINISHED: {len(found_issues)} ISSUES FOUND")
    print("=" * 80)
    for iss in found_issues:
        print("  - " + iss)

if __name__ == '__main__':
    audit_entire_live_state()
