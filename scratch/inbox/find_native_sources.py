# -*- coding: utf-8 -*-
"""Cerca i 4 personaggi nelle fonti candidate (standalone/Mine/native) e ne mostra la forma."""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CANDIDATES = [
    "scratch/backup_consolidated_snapshot/mine_standalone_characters.json",
    "exports/Mine_Characters_Export.json",
    "scratch/source_cards_dump.json",
    "scratch/mine_chars_raw.json",
    "scratch/world_characters.json",
]

TARGETS = ["Erik", "Logan", "Malachia", "Noah", "Jasper"]


def walk_find(node, path=""):
    """Trova dict con chiave 'name' o 'display_name' contenente un target."""
    out = []
    if isinstance(node, dict):
        nm = node.get("name") or node.get("display_name")
        if isinstance(nm, str) and any(t in nm for t in TARGETS):
            out.append((path, node))
        for k, v in node.items():
            out += walk_find(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out += walk_find(v, f"{path}[{i}]")
    return out


for rel in CANDIDATES:
    p = os.path.join(BASE, rel)
    if not os.path.exists(p):
        print(f"\n[MANCANTE] {rel}")
        continue
    size = os.path.getsize(p)
    print("\n" + "=" * 80)
    print(f"FILE: {rel}  ({size} byte)")
    try:
        with open(p, encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as e:
        print("  ERRORE JSON:", e)
        continue
    print("  root type:", type(data).__name__)
    if isinstance(data, dict):
        print("  root keys:", list(data.keys())[:30])
    hits = walk_find(data)
    seen = set()
    for path, node in hits:
        key = (node.get("name") or node.get("display_name"), path.split(".")[-1])
        if key in seen:
            continue
        seen.add(key)
        print(f"  - path={path}")
        print(f"      name={node.get('name')!r} display_name={node.get('display_name')!r}")
        print(f"      first={node.get('first_name')!r} middle={node.get('middle_names')!r} last={node.get('last_name')!r}")
        print(f"      has backgroundURL={'backgroundURL' in node} tagline={'tagline' in node} lexicon={'lexicon' in node} outfits={'outfits' in node}")
        o = node.get("outfits")
        if isinstance(o, str):
            try:
                o = json.loads(o)
            except Exception:
                o = None
        if isinstance(o, list):
            print(f"      outfits({len(o)}): {[x.get('name') for x in o if isinstance(x, dict)]}")
