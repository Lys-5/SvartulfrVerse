# -*- coding: utf-8 -*-
"""Diff dettagliato description + outfits tra card FINAL e backup consolidato."""
import json
import os
import difflib

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
            return []
    return v or []


for fname, cid in MAP.items():
    with open(os.path.join(FINAL, fname), encoding="utf-8") as fh:
        card = json.load(fh)
    wc = by_id[cid]
    print("\n" + "#" * 80)
    print("#", fname)
    print("#" * 80)
    a = (card.get("description") or "").split("\n")
    b = (wc.get("long_summary") or "").split("\n")
    print("--- DESCRIPTION DIFF (card '-' vs snapshot '+') ---")
    for line in difflib.unified_diff(a, b, lineterm="", n=0):
        if line.startswith("---") or line.startswith("+++"):
            continue
        print(line[:300])
    print(f"  [righe card={len(a)} snap={len(b)}]")

    co = {o.get("id"): o for o in parse_outfits((card.get("extensions") or {}).get("outfits")) if isinstance(o, dict)}
    so = {o.get("id"): o for o in parse_outfits(wc.get("outfits")) if isinstance(o, dict)}
    print("--- OUTFITS: confronto campi ---")
    for oid in set(list(co) + list(so)):
        c = co.get(oid)
        s = so.get(oid)
        if c is None:
            print(f"  [SOLO SNAPSHOT] {oid} {s.get('name')}")
            continue
        if s is None:
            print(f"  [SOLO CARD] {oid} {c.get('name')}")
            continue
        keys = sorted(set(list(c.keys()) + list(s.keys())))
        diffs = []
        for k in keys:
            if c.get(k) != s.get(k):
                diffs.append(k)
        if diffs:
            print(f"  [{oid} | {c.get('name')}] campi diversi: {diffs}")
            for k in diffs:
                print(f"      card.{k} = {json.dumps(c.get(k), ensure_ascii=False)[:220]}")
                print(f"      snap.{k} = {json.dumps(s.get(k), ensure_ascii=False)[:220]}")
        else:
            print(f"  [{oid} | {c.get('name')}] identico")
