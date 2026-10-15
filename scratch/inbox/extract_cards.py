# -*- coding: utf-8 -*-
"""Dump ESAUSTIVO delle frasi con pronomi femminili nei campi dei gap (per revisione manuale)."""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")
FEM = re.compile(r"\b(she|her|hers|herself|She|Her|Hers|Herself)\b")

def sentences(text):
    return re.split(r"(?<=[.!?])\s+", text)

CARDS = ["Erik_Douglas_card.json", "Jasper_Douglas_Bloodmoon_card.json",
         "Logan_Douglas_card.json", "Malachia_Douglas_Bloodmoon_card.json",
         "Noah_Douglas_Bloodmoon_card.json"]

for fn in CARDS:
    d = json.load(open(os.path.join(FINAL, fn), encoding="utf-8"))
    print("=" * 100)
    print("FILE:", fn)
    # description only (root), plus mes_example, plus attitude reasoning
    fields = {"description": d.get("description", ""),
              "personality": d.get("personality", ""),
              "scenario": d.get("scenario", ""),
              "first_mes": d.get("first_mes", ""),
              "mes_example": d.get("mes_example", "")}
    for k, v in fields.items():
        if not isinstance(v, str):
            continue
        for s in sentences(v):
            if FEM.search(s):
                print("  [%s] %s" % (k, repr(s)))
    for i, a in enumerate(d.get("extensions", {}).get("attitudes", [])):
        r = a.get("reasoning", "")
        if FEM.search(r):
            print("  [attitude#%d %s] %s" % (i, a.get("target_id"), repr(r)))
