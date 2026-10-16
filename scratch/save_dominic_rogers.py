import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
bid = 'b46b3abf-041e-4ac3-a26a-f45f07a9873b'
data = json.loads((ROOT / 'ARCHIVIO' / 'janitor_sources' / 'janitor_following_canon_characters.json').read_text(encoding='utf-8'))

for bot in data.get('characters', []):
    if bot.get('id') == bid:
        (ROOT / 'scratch' / 'dominic_rogers_janitor.json').write_text(json.dumps(bot, indent=2, ensure_ascii=False), encoding='utf-8')
        print("Successfully wrote scratch/dominic_rogers_janitor.json")
        break
