import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

for p in [
    ROOT / 'scratch' / 'world_locations.json',
    ROOT / 'exports' / 'Svartulfr_Export.json',
    ROOT / 'lorebooks' / 'source' / 'Svartulfr_Location.json',
    ROOT / 'ARCHIVIO' / 'janitor_sources' / 'janitor_lorebooks_all_14.json'
]:
    if not p.exists():
        continue
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = data.get('locations') or data.get('world_locations') or data.get('entries') or []
            if isinstance(items, dict):
                items = list(items.values())
        else:
            continue
            
        for it in items:
            if not isinstance(it, dict):
                continue
            name = it.get('name') or it.get('display_name') or ''
            if "Rogers" in name and "Bargain" in name:
                desc = it.get('description') or it.get('content') or ''
                print(f"Found in {p.name}: name={name}, length={len(desc)}")
                if desc:
                    print(f"  Content: {desc[:200]}...")
    except Exception as ex:
        print(f"Error checking {p.name}: {ex}")
