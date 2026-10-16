# -*- coding: utf-8 -*-
import json, glob, os

FINAL = r'e:\repository\SvartulfrVerse\FINAL'
dec = json.JSONDecoder()
for p in sorted(glob.glob(os.path.join(FINAL, '*_card.json'))):
    raw = open(p, encoding='utf-8').read()
    lead = len(raw) - len(raw.lstrip())
    try:
        obj1, end1 = dec.raw_decode(raw.lstrip())
    except Exception as e:
        print(os.path.basename(p), 'PARSE FAIL', e)
        continue
    rest = raw[lead + end1:]
    has_extra = rest.strip() != ''
    extra_keys = []
    if has_extra:
        try:
            obj2, _ = dec.raw_decode(rest.lstrip())
            extra_keys = list(obj2.keys()) if isinstance(obj2, dict) else [type(obj2).__name__]
        except Exception as e:
            extra_keys = ['<UNPARSEABLE: %s>' % e]
    print('=' * 70)
    print(os.path.basename(p), 'chars', len(raw), 'EXTRA BLOCK:', has_extra)
    print('  B1 top-level keys:', list(obj1.keys()))
    ext = obj1.get('extensions', {})
    print('  B1 extensions keys:', list(ext.keys()))
    o = ext.get('outfits')
    if isinstance(o, list):
        print('  B1 outfits:', len(o), [x.get('name') for x in o if isinstance(x, dict)])
    if has_extra:
        print('  B2 keys:', extra_keys)
        try:
            o2 = obj2.get('outfits')
            if isinstance(o2, list):
                print('  B2 outfits:', len(o2), [x.get('name') for x in o2 if isinstance(x, dict)])
        except Exception:
            pass
