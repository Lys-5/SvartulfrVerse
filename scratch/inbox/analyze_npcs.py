# -*- coding: utf-8 -*-
"""Analisi read-only: struttura delle entry dei lorebook FINAL."""
import json
import glob
import os

for f in sorted(glob.glob('FINAL/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    entries = data['entries']
    print('=' * 90)
    print(os.path.basename(f), '-> entries:', len(entries))
    # stampa la struttura della prima entry
    first = next(iter(entries.values()))
    print('entry keys:', list(first.keys()))
    print('sample comment:', repr(first.get('comment')))
    print('sample key:', repr(first.get('key')))
    print('extensions:', json.dumps(first.get('extensions'), ensure_ascii=False)[:400])
