"""
Patch Ariadne Cirillo in FINAL/Svartulfr_NPC_Secondary.json and sync to Wyvern Web API
"""
import os
import sys
import json
import urllib.request
import urllib.error

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.sync_from_wyvern_web import get_auth_token
from scripts.sync_all_characters_rpg import load_all_catalogs, find_best_species, find_best_occupation, select_traits_for_character, generate_base_stats_for_char, compute_rpg_block

def main():
    token = get_auth_token()
    catalogs = load_all_catalogs()
    
    # 1. Load source Ariadne content from exports
    with open(os.path.join(ROOT_DIR, 'exports', 'Svartulfr_Export_pre_web_sync.json'), 'r', encoding='utf-8') as f:
        exp = json.load(f)
    ari_src = [e for e in exp['world_lexicon_entries'] if 'Ariadne' in str(e.get('name'))][0]
    raw_content = ari_src['content'].replace('{{age}}', '30 (Born March 14, 1994)').replace('\u2014', ', ')
    
    sp = find_best_species('Ariadne Cirillo ' + raw_content, catalogs)
    occ = find_best_occupation('Ariadne Cirillo ' + raw_content, catalogs)
    tr = select_traits_for_character('Ariadne Cirillo', raw_content, sp, occ, catalogs)
    base_stats = generate_base_stats_for_char(6, occ, sp)
    cls_name = occ['name'] + ' (' + sp['name'].split()[0] + ')'
    rpg_block, stats = compute_rpg_block('Ariadne Cirillo', 6, sp, occ, tr, base_stats, cls_name)
    full_content = (raw_content.strip() + '\n\n' + rpg_block).replace('\u2014', ', ')
    
    # 2. Update local FINAL/Svartulfr_NPC_Secondary.json
    sec_path = os.path.join(ROOT_DIR, 'FINAL', 'Svartulfr_NPC_Secondary.json')
    with open(sec_path, 'r', encoding='utf-8') as f:
        sec_data = json.load(f)
        
    entries = sec_data.get('entries', [])
    ari_idx = next(i for i, e in enumerate(entries) if e.get('entry_id') == 'CyZknaH7OmYQi5S3ESpNJ' or 'Ariadne' in str(e.get('name')))
    
    entries[ari_idx]['content'] = full_content
    # Parity entries == lexicon
    sec_data['entries'] = list(entries)
    sec_data['lexicon'] = list(entries)
    
    with open(sec_path, 'w', encoding='utf-8') as f:
        json.dump(sec_data, f, indent=2, ensure_ascii=False)
    print(f"Updated Ariadne in {sec_path} (length: {len(full_content)} chars)")
    
    # 3. Also update lorebooks/optimized/Svartulfr_NPC_Secondary.json if it exists
    opt_path = os.path.join(ROOT_DIR, 'lorebooks', 'optimized', 'Svartulfr_NPC_Secondary.json')
    if os.path.exists(opt_path):
        with open(opt_path, 'r', encoding='utf-8') as f:
            opt_data = json.load(f)
        opt_entries = opt_data.get('entries', opt_data.get('lexicon', []))
        for e in opt_entries:
            if e.get('entry_id') == 'CyZknaH7OmYQi5S3ESpNJ' or 'Ariadne' in str(e.get('name')):
                e['content'] = full_content
        opt_data['entries'] = list(opt_entries)
        opt_data['lexicon'] = list(opt_entries)
        with open(opt_path, 'w', encoding='utf-8') as f:
            json.dump(opt_data, f, indent=2, ensure_ascii=False)
        print(f"Updated Ariadne in {opt_path}")

    # 4. Prepare compact remote payload (< 1MB)
    lid = '_Uht3Ckz44JBDrPnUHq7LV'
    clean_lexicon = []
    for e in entries:
        ec = dict(e)
        ec.pop("provenance", None)
        clean_lexicon.append(ec)
        
    compact_payload = {
        "name": sec_data.get("name"),
        "description": sec_data.get("description", ""),
        "scan_depth": sec_data.get("scan_depth", 2),
        "token_budget": sec_data.get("token_budget", 2048),
        "recursive_scanning": sec_data.get("recursive_scanning", False),
        "lexicon": clean_lexicon
    }
    
    payload_bytes = json.dumps(compact_payload, ensure_ascii=False).encode('utf-8')
    print(f"Payload size: {len(payload_bytes)} bytes (Max: 1048576)")
    
    url = f"https://app.wyvern.chat/api/lorebooks/{lid}"
    req = urllib.request.Request(
        url,
        data=payload_bytes,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='PUT'
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"API Response Code: {resp.status}")
            resp_body = resp.read().decode('utf-8')
            print(f"API Response: {resp_body[:200]}")
    except urllib.error.HTTPError as err:
        print(f"HTTP Error {err.code}: {err.read().decode('utf-8')}")
        sys.exit(1)

if __name__ == '__main__':
    main()
