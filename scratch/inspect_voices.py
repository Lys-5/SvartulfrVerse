import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])
ids = [
    '_fhfjJ1YkgcBWqxhBTtBhf', # Garrett Locke
    '_maeWVteX4EjhAMjpA31WY', # Roger "Rocky" Mackenzie
    '_ErE1aA4ychtDkNqGYtzpc', # Harlow MacGregor
    '_JRmw4NGgUKF9NVrKgqWxt', # Bram Beaumont
    '_HfbrnbLjQUf2jdptGtaMp', # Atlas Teague
    '_x1mwLndFm3eJr7dzjMEz7', # Arthur Grey
    '_GEM6nCQFFMQ6Raa1kPJHY', # Jake Thompson
    '_LMBDb78CUFJ2wMPpXQgYy', # Professor Kîwêtin
    '_c9yC2E2TcPx6KLUQQXUnm', # Vargus "The Red"
    '_UAfbpEQUywf4eXcp4pjJn'  # Sawyer Shephard
]

for cid in ids:
    c = [x for x in chars if x.get('id') == cid][0]
    dn = c.get('display_name')
    ls = c.get('long_summary') or ''
    # extract last 600 chars (usually speech/voice)
    tail = ls[-600:].replace('\n', ' ')
    print(f"=== {dn} ({cid}) ===")
    print("KEYS:", c.get('keys'))
    print("TAIL:", tail)
    print()
