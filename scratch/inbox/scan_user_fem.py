# -*- coding: utf-8 -*-
"""Scan esaustivo: frasi con pronome femminile che contengono anche {{user}} (gap ad alta confidenza)."""
import json, os, re, glob

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")
FEM = re.compile(r"\b(she|her|hers|herself|She|Her|Hers|Herself)\b")
USER = re.compile(r"\{\{user\}\}")
ALY = re.compile(r"Alyssa|alyssa|ALYSSA")

def split_sent(t):
    return re.split(r"(?<=[.!?])\s+", t)

for p in sorted(glob.glob(os.path.join(FINAL, "*.json"))):
    fn = os.path.basename(p)
    d = json.load(open(p, encoding="utf-8"))
    hits = []
    def scan(obj, pathid=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                scan(v, pathid + "/" + str(k))
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                scan(v, pathid + "[%d]" % i)
        elif isinstance(obj, str):
            for s in split_sent(obj):
                if FEM.search(s) and USER.search(s):
                    hits.append((pathid, s))
    scan(d)
    if hits:
        print("=" * 100)
        print("FILE:", fn, "| hits:", len(hits))
        for pid, s in hits:
            print("  @%s :: %s" % (pid, repr(s)))
