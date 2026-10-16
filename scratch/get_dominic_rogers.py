import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
bid = 'b46b3abf-041e-4ac3-a26a-f45f07a9873b'
data = json.loads((ROOT / 'ARCHIVIO' / 'janitor_sources' / 'janitor_following_canon_characters.json').read_text(encoding='utf-8'))

for bot in data.get('characters', []):
    if bot.get('id') == bid:
        print("=== FOUND DOMINIC ROGERS BOT ===")
        print(f"Name: {bot.get('name')}")
        print(f"Avatar: {bot.get('avatar')}")
        print(f"Description:\n{bot.get('description')}\n")
        print(f"Personality:\n{bot.get('personality')}\n")
        print(f"Scenario:\n{bot.get('scenario')}\n")
        print(f"First Message:\n{bot.get('first_message')}\n")
        
        # Also write clean JSON to scratch for easy viewing
        (ROOT / 'scratch' / 'dominic_rogers_janitor.json').write_text(json.dumps(bot, indent=2, ensure_ascii=False), encoding='utf-8')
        break
