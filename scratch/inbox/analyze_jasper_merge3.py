# -*- coding: utf-8 -*-
import json

p = r'e:\repository\SvartulfrVerse\FINAL\Jasper_Douglas_Bloodmoon_card.json'
raw = open(p, encoding='utf-8').read()
dec = json.JSONDecoder()
obj1, end1 = dec.raw_decode(raw.lstrip())
rest = raw[len(raw) - len(raw.lstrip()) + end1:]
obj2, _ = dec.raw_decode(rest.lstrip())

ext = obj1['extensions']
print('B1 ext.keys:', ext.get('keys'))
print('B1 ext.keys value:', obj1.get('keys'), ext.get('keys'))
print('B1 depth_prompt:', ext.get('depth_prompt'))
print('B1 rpg_stats:', ext.get('rpg_stats'))
print('B1 system_prompt len:', len(obj1.get('system_prompt') or ''))
print('B1 creator:', obj1.get('creator'), '| version:', obj1.get('character_version'))
print('B1 attitudes targets:', [(a.get('target'), a.get('tier')) for a in ext.get('attitudes', [])])
print()
print('B2 metadata:', obj2.get('metadata'))
print('B2 lexicon_config:', obj2.get('lexicon_config'))
lx = obj2.get('lexicon') or []
for it in lx:
    print('B2 lexicon entry:', it.get('keys'), '| enabled:', it.get('enabled'), '| type:', it.get('type'))
    print('   content:', (it.get('content') or '')[:600])
