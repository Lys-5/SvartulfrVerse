# -*- coding: utf-8 -*-
"""Elenca, per ogni lorebook, le entry che sono schede personaggio (content inizia con [NAME:)."""
import json, glob, os, re

NAME_RE = re.compile(r'^\s*\[NAME:', re.IGNORECASE)
for f in sorted(glob.glob('FINAL/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    entries = d['entries']
    chars = [(uid, e.get('comment'), e.get('disable')) for uid, e in entries.items()
             if NAME_RE.match(e.get('content') or '')]
    print(f'{os.path.basename(f)}: {len(chars)}/{len(entries)} schede personaggio')
    for uid, c, dis in chars:
        print(f'   [{uid}] {c!r} dis={dis}')
