# -*- coding: utf-8 -*-
"""Ispeziona lo schema delle entry Lexicon (world_lexicon.json)."""
import json

d = json.load(open('scratch/world_lexicon.json', encoding='utf-8'))
print('total:', len(d))
print('keys union:', sorted({k for e in d for k in e.keys()}))

# trova una entry NPC
def looks_npc(e):
    s = json.dumps(e).lower()
    return '"npc"' in s or 'npc' in (str(e.get('type', '')) + str(e.get('kind', '')) + str(e.get('entryType',''))).lower()

npc = [e for e in d if looks_npc(e)][:3]
print('\nfounded npc-like:', len([e for e in d if looks_npc(e)]))
for e in npc:
    print('\n===== ENTRY =====')
    print(json.dumps(e, ensure_ascii=False, indent=1)[:2500])
