# -*- coding: utf-8 -*-
import json, difflib, re

CARD = r'e:\repository\SvartulfrVerse\FINAL\Jasper_Douglas_Bloodmoon_card.json'
raw_bak = open(r'e:\repository\SvartulfrVerse\scratch\backup_final_premerge\Jasper_Douglas_Bloodmoon_card.json', encoding='utf-8').read()
dec = json.JSONDecoder()
b1, e1 = dec.raw_decode(raw_bak.lstrip())
lead = len(raw_bak) - len(raw_bak.lstrip())
b2, _ = dec.raw_decode(raw_bak[lead + e1:].lstrip())

m = json.load(open(CARD, encoding='utf-8'))

# Descrizione: atteso = b1.desc con header B2 + blocco RPG in coda
print('=== DIFF description: B1(originale) -> merged ===')
d = list(difflib.unified_diff(b1['description'].splitlines(), m['description'].splitlines(),
                              'B1', 'MERGED', lineterm='', n=0))
for ln in d:
    print(ln[:300])

print()
print('=== Verifiche chiave ===')
print('spec:', m['spec'], m['spec_version'])
print('top-level keys ==', list(m.keys()))
print('data keys  ==', list(m['data'].keys()))
print('data.name == name:', m['data']['name'] == m['name'])
print('data.extensions is extensions:', m['data']['extensions'] is m['extensions'])
print('first_mes[:80]:', repr(m['first_mes'][:80]))
print('scenario[:80]:', repr(m['scenario'][:80]))
print('creator_notes[:80]:', repr(m['creator_notes'][:80]))
print('mes_example startswith <START>:', m['mes_example'].lstrip().startswith('<START>'))
print('shared_info:', repr(m['extensions']['shared_info'][:100]))
print('tagline:', repr(m['extensions']['tagline'][:100]))
print('pre_history_instructions[:80]:', repr(m['extensions']['pre_history_instructions'][:80]))
print('lexicon entry keys:', m['extensions']['lexicon'][0]['keys'], '| type:', m['extensions']['lexicon'][0]['type'])
print('pronouns:', m['extensions']['pronouns'])
print('metadata:', m['extensions']['metadata'])
print('attitudes count:', len(m['extensions']['attitudes']))
print('depth_prompt:', m['extensions']['depth_prompt'])
print('RPG block present in description:', 'RPG STATS & TRAITS' in m['description'])
print('Alyssa residui (tutto il file):', len(re.findall(r'Alyssa|alyssa|ALYSSA', json.dumps(m, ensure_ascii=False))))
