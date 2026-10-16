# -*- coding: utf-8 -*-
"""Ispeziona il backup consolidato del 14/10 per i 4 personaggi target."""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SNAP = os.path.join(BASE, "scratch", "backup_consolidated_snapshot", "world_characters.json")

IDS = {
    "_d44gDc8N18kkbEhAcfUCG": "Erik",
    "_JL37wK9PQMNDChULCDrWj": "Logan",
    "_rAcN9GXD1Le4WxY28e49W": "Malachia",
    "_r42cVzMjcGTAx7bR1DQVt": "Noah",
}

with open(SNAP, encoding="utf-8") as fh:
    data = json.load(fh)

if isinstance(data, dict):
    chars = data.get("characters") or data.get("world_characters") or data
else:
    chars = data

print("TIPO ROOT:", type(data).__name__)
if isinstance(chars, dict):
    items = list(chars.values())
else:
    items = chars
print("NUMERO ELEMENTI:", len(items))

by_id = {}
for c in items:
    if isinstance(c, dict) and c.get("id"):
        by_id[c["id"]] = c

for cid, label in IDS.items():
    c = by_id.get(cid)
    print("\n" + "=" * 70)
    if not c:
        print(f"[{label}] id {cid} NON TROVATO")
        continue
    print(f"[{label}] {cid}")
    print("  display_name :", repr(c.get("display_name")))
    print("  first_name   :", repr(c.get("first_name")))
    print("  middle_names :", repr(c.get("middle_names")))
    print("  last_name    :", repr(c.get("last_name")))
    ls = c.get("long_summary") or ""
    print("  long_summary len:", len(ls))
    print("  HEADER       :", ls.split("\n")[0][:400])
    outfits = c.get("outfits")
    if isinstance(outfits, str):
        try:
            outfits = json.loads(outfits)
        except Exception:
            outfits = None
    if isinstance(outfits, list):
        print(f"  OUTFITS      : {len(outfits)} voci")
        for o in outfits:
            if isinstance(o, dict):
                print("     -", o.get("id"), "|", o.get("name"))
    else:
        print("  OUTFITS      :", type(outfits).__name__)
    print("  KEYS/RUNE presenti in summary:", "BIRTH_RUNE" in ls)
