import urllib.request
import json
import re
import pathlib

token = pathlib.Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
req = urllib.request.Request(
    'https://app.wyvern.chat/api/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H',
    headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
)
resp = urllib.request.urlopen(req)
sc = json.loads(resp.read().decode('utf-8'))

print("Live Scenario:", sc.get('name'))
print("Scenario ID:", sc.get('_id') or sc.get('id'))
print("Updated At:", sc.get('updated_at'))
print("Premade scenes count:", len(sc.get('premade_scenes', [])))

for i, s in enumerate(sc.get('premade_scenes', [])):
    tags = re.findall(r'^=>([^:\n]+):', s.get('scene_text', ''), flags=re.MULTILINE)
    plain = re.findall(r'^([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', s.get('scene_text', ''), flags=re.MULTILINE)
    plain = [p for p in plain if not p.startswith('=>')]
    print(f"\nScene {i} [{s.get('id')}]:")
    print("  =>Speaker tags:", tags)
    print("  Plain Speaker: tags:", plain)
