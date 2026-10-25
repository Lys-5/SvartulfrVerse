import json
from urllib.parse import urlparse
from collections import Counter

for name, path in [('Primary', 'FINAL/Svartulfr_NPC_Primary.json'), ('Secondary', 'FINAL/Svartulfr_NPC_Secondary.json')]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    entries = data.get('entries', [])
    domains = Counter()
    schemes = Counter()
    for e in entries:
        av = e.get('avatar', '')
        p = urlparse(av)
        schemes[p.scheme] += 1
        domains[p.netloc] += 1
    print(f"=== {name} ({len(entries)} entries) ===")
    print("Schemes:", dict(schemes))
    print("Domains:", dict(domains))
    print()
