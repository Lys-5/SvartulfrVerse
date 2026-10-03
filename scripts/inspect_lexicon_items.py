import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
items = [e for e in data['world_lexicon_entries'] if e.get('type') == 'item']
print(f"Total items in lexicon: {len(items)}")
for it in items:
    safe_name = it['name'].encode('ascii', 'replace').decode('ascii')
    cfg = it.get('item_config')
    print(f"{it['id']} | {safe_name[:40]:40} | cfg: {bool(cfg)}")
