# -*- coding: utf-8 -*-
"""Confronta le card FINAL dei 4 personaggi con il backup consolidato del 14/10."""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SNAP = os.path.join(BASE, "scratch", "backup_consolidated_snapshot", "world_characters.json")
FINAL = os.path.join(BASE, "FINAL")

MAP = {
    "Erik_Douglas_card.json": "_d44gDc8N18kkbEhAcfUCG",
    "Logan_Douglas_card.json": "_JL37wK9PQMNDChULCDrWj",
    "Malachia_Douglas_Bloodmoon_card.json": "_rAcN9GXD1Le4WxY28e49W",
    "Noah_Douglas_Bloodmoon_card.json": "_r42cVzMjcGTAx7bR1DQVt",
}

with open(SNAP, encoding="utf-8") as fh:
    snap = json.load(fh)
by_id = {c["id"]: c for c in snap if isinstance(c, dict) and c.get("id")}


def parse_outfits(v):
    if isinstance(v, str):
        try:
            return json.loads(v)
        except Exception:
            return None
    return v


for fname, cid in MAP.items():
    path = os.path.join(FINAL, fname)
    with open(path, encoding="utf-8") as fh:
        card = json.load(fh)
    wc = by_id[cid]
    print("\n" + "=" * 78)
    print(f"{fname}")
    print(f"  name card      : {card.get('name')!r}")
    print(f"  name snapshot  : {wc.get('display_name')!r}")
    desc = card.get("description") or ""
    ls = wc.get("long_summary") or ""
    print(f"  desc len card  : {len(desc)}   | snapshot: {len(ls)}")
    print(f"  desc header    : {desc.split(chr(10))[0][:160]!r}")
    print(f"  snap header    : {ls.split(chr(10))[0][:160]!r}")
    tags = card.get("tags") or []
    print(f"  tags card      : {tags}")
    print(f"  tags snapshot  : {wc.get('tags')}")
    co = parse_outfits((card.get("extensions") or {}).get("outfits"))
    so = parse_outfits(wc.get("outfits"))
    print(f"  outfits card   : {len(co) if co is not None else 'N/A'}")
    if co:
        for o in co:
            if isinstance(o, dict):
                print("      -", o.get("id"), "|", o.get("name"))
    print(f"  outfits snap   : {len(so) if so is not None else 'N/A'}")
    if so:
        for o in so:
            if isinstance(o, dict):
                print("      -", o.get("id"), "|", o.get("name"))
    print(f"  rpg_stats card : {json.dumps((card.get('extensions') or {}).get('rpg_stats'), ensure_ascii=False)}")
    print(f"  rpg_stats snap : {json.dumps(wc.get('rpg_stats'), ensure_ascii=False)}")
    print(f"  attitudes card : {len((card.get('extensions') or {}).get('attitudes') or [])}")
    sa = wc.get("attitudes")
    if isinstance(sa, str):
        try:
            sa = json.loads(sa)
        except Exception:
            sa = None
    print(f"  attitudes snap : {len(sa) if isinstance(sa, list) else 'N/A'}")
