# -*- coding: utf-8 -*-
"""Localizza i residui 'Alyssa' nei materiali standalone genericizzati."""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STANDALONE = os.path.join(BASE, "scratch", "backup_consolidated_snapshot",
                          "mine_standalone_characters.json")
sys.path.insert(0, os.path.join(BASE, "scripts"))
from genericize_alyssa import walk  # noqa: E402

TARGETS = ["Erik Ulfr Douglas", "Logan Járn Douglas",
           "Malachia Björn Douglas Bloodmoon", "Noah Loki Douglas Bloodmoon"]

with open(STANDALONE, encoding="utf-8") as fh:
    data = json.load(fh)
by_name = {c.get("name"): c for c in data if isinstance(c, dict)}


def scan(node, path=""):
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            out += scan(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out += scan(v, f"{path}[{i}]")
    elif isinstance(node, str) and re.search(r"Alyssa|alyssa|ALYSSA", node):
        for m in re.finditer(r"Alyssa|alyssa|ALYSSA", node):
            s = max(0, m.start() - 90)
            e = min(len(node), m.end() + 90)
            out.append((path, node[s:e]))
    return out


for name in TARGETS:
    c = by_name[name]
    g = walk(json.loads(json.dumps(c)), False)
    hits = scan(g)
    print("\n" + "=" * 78)
    print(f"{name}: {len(hits)} residui")
    for path, ctx in hits:
        print(f"  [{path}] ...{ctx}...")
