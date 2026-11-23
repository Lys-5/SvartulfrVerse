#!/usr/bin/env python3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import scripts.wyvern_api_client as c

tok = c.get_auth_token()
req = ['Abbigliamento:', 'Accessori:', 'Scarpe:', 'Gioielli:', 'Trucco:', 'Acconciatura:']

for cid in ['_nUkjqtKz9RrP7CJCxXnCL', '_zn24784jfcchQ7EwCyAnm']:
    st, data = c.get_character(cid, token=tok)
    nude = [o for o in data.get('outfits', []) if any(w in o.get('name', '').lower() for w in ['nude', 'nudo'])][0]
    desc = nude.get('description', '')
    missing = [s for s in req if s not in desc]
    print(f"{cid}: HTTP {st}, name={data.get('name')}, nude_len={len(desc)}, missing={missing}")
