import sys
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.stdout.reconfigure(encoding='utf-8')
with open(ROOT / '.agents' / 'teamwork' / 'explorer_m3_2' / 'live_prompt_assembly.json', encoding='utf-8') as f:
    liv = json.load(f)

for b in liv.get('blocks', []):
    print("=" * 60)
    print(f"Block ID: {b.get('block_id')}")
    print(f"Label: {b.get('label')}")
    print(f"Role: {b.get('role')} -- Order: {b.get('order')}")
    print("TriggerOptions:", b.get('triggerOptions'))
    print(f"Content:\n{b.get('content')}")
