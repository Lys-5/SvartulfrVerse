# -*- coding: utf-8 -*-
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")

def dump(fn, names=None, idxs=None):
    d = json.load(open(os.path.join(FINAL, fn), encoding="utf-8"))
    lex = d["lexicon"] if isinstance(d, dict) and "lexicon" in d else d
    print("#" * 100); print("FILE:", fn, "n=", len(lex))
    for i, e in enumerate(lex):
        nm = e.get("name", "")
        if idxs is not None and i not in idxs:
            continue
        if names is not None:
            if not any(n in nm for n in names):
                continue
        print("-" * 90)
        print("IDX %d | NAME: %r | KEYS: %r" % (i, nm, e.get("keys")))
        print("CONTENT:")
        print(e.get("content", ""))
    print()

# Lorebook II: ricerca per nome
dump("Svartulfr_Lorebook_II.json", names=[
    "Barriere a Permeabilità Selettiva", "Pacifist Vow", "Pack Authority",
    "White Moon Ceremonial", "Vélhati"])
dump("Svartulfr_NPC_Primary.json", idxs=[83])
