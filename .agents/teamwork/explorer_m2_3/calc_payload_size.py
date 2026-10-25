import json
from pathlib import Path

for fn, lid in [('FINAL/Svartulfr_NPC_Primary.json', '_zwEqgEEzh12X6gHVmMKKC'), 
                ('FINAL/Svartulfr_NPC_Secondary.json', '_Uht3Ckz44JBDrPnUHq7LV')]:
    p = Path(r'e:\repository\SvartulfrVerse') / fn
    data = json.loads(p.read_text(encoding='utf-8'))
    
    compact_payload = {
        'name': data.get('name'),
        'description': data.get('description', ''),
        'photoURL': data.get('photoURL'),
        'token_budget': data.get('token_budget'),
        'visibility': data.get('visibility', 'private'),
        'rating': data.get('rating', 'explicit'),
        'scan_depth': data.get('scan_depth', 5),
        'recursive_scanning': data.get('recursive_scanning', True),
        'gallery': data.get('gallery', []),
        'gallery_count': len(data.get('gallery', [])),
        'lexicon': data.get('lexicon', [])
    }
    
    compact_bytes = json.dumps(compact_payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    full_bytes = json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8')
    
    print(f"{fn}:")
    print(f"  Full file with entries & indent: {len(full_bytes):,} bytes ({len(full_bytes)/(1024*1024):.2f} MB)")
    print(f"  Compact PUT payload (lexicon only): {len(compact_bytes):,} bytes ({len(compact_bytes)/(1024*1024):.2f} MB)")
    print(f"  Reduction: {(1 - len(compact_bytes)/len(full_bytes))*100:.1f}%")
