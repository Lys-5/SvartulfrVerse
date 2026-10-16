# -*- coding: utf-8 -*-
import json, difflib

p = r'e:\repository\SvartulfrVerse\FINAL\Jasper_Douglas_Bloodmoon_card.json'
raw = open(p, encoding='utf-8').read()
dec = json.JSONDecoder()
obj1, end1 = dec.raw_decode(raw.lstrip())
rest = raw[len(raw) - len(raw.lstrip()) + end1:]
obj2, _ = dec.raw_decode(rest.lstrip())

for f in ['description', 'mes_example']:
    a = obj1.get(f) or ''
    b = obj2.get(f) or ''
    print('#' * 70)
    print('FIELD:', f, '  B1 len', len(a), ' B2 len', len(b))
    diff = list(difflib.unified_diff(a.splitlines(), b.splitlines(), 'B1', 'B2', lineterm='', n=0))
    if not diff:
        print('  (identical)')
    for ln in diff:
        print('  ' + ln[:400])

# B1 data duplication check
print('#' * 70)
print('B1.data == B1 top-level content?')
d = obj1.get('data', {})
for k in ['name', 'description', 'personality', 'scenario', 'first_mes', 'mes_example']:
    print('  ', k, 'equal:', d.get(k) == obj1.get(k))

# B2 extra readable fields
print('#' * 70)
for k in ['tagline', 'character_note', 'pre_history_instructions']:
    print('---', k, '---')
    print(obj2.get(k))
