# -*- coding: utf-8 -*-
import json

CARD = r'e:\repository\SvartulfrVerse\FINAL\Jasper_Douglas_Bloodmoon_card.json'
m = json.load(open(CARD, encoding='utf-8'))
lex = m['extensions']['lexicon']
print('lexicon len:', len(lex))
e = lex[0]
for k, v in e.items():
    if isinstance(v, str) and len(v) > 400:
        print(k, '= STR(len=%d)' % len(v))
    else:
        print(k, '=', v)
print()
print('--- FULL CONTENT ---')
print(e['content'])
print()
print('--- OUTFIT 1 (IT) ---')
print(repr(m['extensions']['outfits'][0]['description'][:600]))
