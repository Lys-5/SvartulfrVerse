# -*- coding: utf-8 -*-
"""Verifica finale delle card del Main Cast in FINAL."""
import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")

FILES = [
    "Erik_Douglas_card.json",
    "Logan_Douglas_card.json",
    "Jasper_Douglas_Bloodmoon_card.json",
    "Malachia_Douglas_Bloodmoon_card.json",
    "Noah_Douglas_Bloodmoon_card.json",
]
TOP_KEYS = ["spec", "spec_version", "name", "description", "personality", "scenario",
            "first_mes", "mes_example", "creator_notes", "system_prompt",
            "post_history_instructions", "alternate_greetings", "tags", "creator",
            "character_version", "extensions", "data"]

for f in FILES:
    p = os.path.join(FINAL, f)
    raw = open(p, encoding="utf-8").read()
    try:
        card = json.loads(raw)
        valid = True
    except Exception as e:
        print(f"{f}: JSON NON VALIDO: {e}")
        continue
    missing = [k for k in TOP_KEYS if k not in card]
    ext = card.get("extensions") or {}
    outfits = ext.get("outfits") or []
    alyssa = len(re.findall(r"Alyssa|alyssa|ALYSSA", raw))
    rune = "BIRTH_RUNE" in (card.get("description") or "")
    print(f"{f}")
    print(f"   valid={valid}  missing_top_keys={missing}")
    print(f"   name={card.get('name')!r}  data.name={card.get('data', {}).get('name')!r}")
    print(f"   desc_len={len(card.get('description') or '')}  BIRTH_RUNE={rune}  Alyssa_residui={alyssa}")
    print(f"   {{user}} count={raw.count('{{user}}')}  marcatore_entry_alyssa={'Alyssa Hvit Douglas Bloodmoon' in raw}")
    print(f"   outfits={len(outfits)} -> {[o.get('name') for o in outfits]}")
    print(f"   default_outfit={ext.get('default_outfit')}")
    print(f"   extensions keys={sorted(ext.keys())}")
    print(f"   tags={card.get('tags')}")
    print()
