# -*- coding: utf-8 -*-
import json

p = r'e:\repository\SvartulfrVerse\FINAL\Jasper_Douglas_Bloodmoon_card.json'
raw = open(p, encoding='utf-8').read()
dec = json.JSONDecoder()
obj1, end1 = dec.raw_decode(raw.lstrip())
rest = raw[len(raw) - len(raw.lstrip()) + end1:]
obj2, _ = dec.raw_decode(rest.lstrip())

s1 = json.dumps(obj1, ensure_ascii=False)
s2 = json.dumps(obj2, ensure_ascii=False)
print('Alyssa count B1:', s1.count('Alyssa'), ' B2:', s2.count('Alyssa'))
print('{{user}} count B1:', s1.count('{{user}}'), ' B2:', s2.count('{{user}}'))
print()
print('=== B2-only / other fields ===')
for k in ['avatar', 'pre_history_instructions', 'visual_description', 'model_url',
          'character_note', 'tagline', 'backgroundURL', 'soundcloud_url', 'rating', 'visibility']:
    v = obj2.get(k)
    if isinstance(v, str):
        print(k, 'STR len=', len(v), '::', repr(v[:120]))
    else:
        print(k, type(v).__name__, '::', v)
for k in ['scripts', 'commands', 'secrets', 'fields', 'metadata', 'lexicon_config']:
    v = obj2.get(k)
    n = len(v) if hasattr(v, '__len__') else '-'
    print(k, type(v).__name__, 'len=', n)
print()
print('shared_info (B2):')
print(obj2.get('shared_info'))
print()
print('pronouns (B2):', obj2.get('pronouns'))
print()
lex = obj2.get('lexicon')
print('lexicon (B2) type:', type(lex).__name__, 'len:', len(lex) if hasattr(lex, '__len__') else '-')
if isinstance(lex, list) and lex:
    print('  item0 keys:', list(lex[0].keys()) if isinstance(lex[0], dict) else type(lex[0]).__name__)
    for it in lex[:8]:
        if isinstance(it, dict):
            print('   -', it.get('keys') or it.get('key'), '|', str(it.get('content'))[:70])
elif isinstance(lex, dict):
    print('  dict keys sample:', list(lex.keys())[:8])
