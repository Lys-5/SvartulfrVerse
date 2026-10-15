# -*- coding: utf-8 -*-
"""Inventario read-only: elenca uid, comment e key di tutte le entry dei lorebook."""
import json
import glob
import os

out = []
for f in sorted(glob.glob('FINAL/*.json')):
    name = os.path.basename(f)
    data = json.load(open(f, encoding='utf-8'))
    entries = data['entries']
    out.append('=' * 100)
    out.append(f'FILE: {name} ({len(entries)} entries)')
    out.append('=' * 100)
    for uid, e in entries.items():
        keys = e.get('key') or []
        keys = keys if isinstance(keys, list) else [keys]
        out.append(f"[{uid}] {e.get('comment')!r} | dis={e.get('disable')} | keys={keys}")

open('scratch/inbox/npc_inventory.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written', len(out), 'lines')
