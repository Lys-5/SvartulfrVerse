import json
import pathlib

p = pathlib.Path('FINAL/Zeera_Darkfire_card.json')
card = json.loads(p.read_text(encoding='utf-8'))

print("Zeera desc:")
for line in card.get('description', '').splitlines():
    if '{{age}}' in line or 'age:' in line.lower():
        print(" ", line[:120])

print("\nLexicon entries with {{age}}:")
for lex in card.get('lexicon', []):
    content = lex.get('content', '')
    if '{{age}}' in content:
        for line in content.splitlines():
            if '{{age}}' in line:
                print(f"  {lex.get('name')}: {line[:120]}")
