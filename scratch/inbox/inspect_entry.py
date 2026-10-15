# -*- coding: utf-8 -*-
"""Ispeziona entry rappresentative per cercare un campo di classificazione."""
import json

def show(f, uid):
    d = json.load(open(f, encoding='utf-8'))
    e = d['entries'][uid]
    slim = {k: v for k, v in e.items() if k not in ('content',)}
    print('---', f, uid, '---')
    print(json.dumps(slim, ensure_ascii=False, indent=1)[:1200])
    print('content head:', repr(e['content'][:120]))

# NPC (LB-I), Item (LB-I), Kink (LB-I)
show('FINAL/Svartulfr_Lorebook_I.json', '0')     # Jet Thompson (NPC)
show('FINAL/Svartulfr_Lorebook_I.json', '18')    # item
show('FINAL/Svartulfr_Lorebook_I.json', '219')   # kink
# NPC enabled (LB-III), disabled NPC (LB-III)
show('FINAL/Svartulfr_Lorebook_III.json', '110') # Adrian Locke
show('FINAL/Svartulfr_Lorebook_III.json', '0')   # Valentine Rossfeld (disabled)
# NPC primary
show('FINAL/Svartulfr_NPC_Primary.json', '111')  # Alyssa
