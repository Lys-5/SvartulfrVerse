# -*- coding: utf-8 -*-
"""Estrae le stringhe esatte dei gap (pronomi Alyssa) dai file FINAL, per estendere CURATED."""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")

FEM = re.compile(r"\b(she|her|hers|herself|She|Her|Hers|Herself)\b")

def sentences(text, needles):
    # split keeping delimiters
    parts = re.split(r"(?<=[.!?])\s+", text)
    out = []
    for p in parts:
        for n in needles:
            if n in p:
                out.append((n, p))
                break
    return out

targets = {
    "Erik_Douglas_card.json": ["tells him the version of her life",
        "doubles the watch on the north perimeter",
        "LEVEL TWO containment protocol",
        "buried her mother",
        "a tracker and a perimeter"],
    "Jasper_Douglas_Bloodmoon_card.json": ["He is her alibi"],
    "Malachia_Douglas_Bloodmoon_card.json": [
        "turns up at her dorm unannounced", "carries things she is perfectly capable",
        "knows her timetable, her route", "She knows he is lying",
        "incapable of being normal about anyone she likes", "soft with her and only with her",
        "lets her talk without interrupting", "notices before anybody else that she has gone quiet"],
    "Noah_Douglas_Bloodmoon_card.json": ["For two years leading up to her first semester"],
    "Logan_Douglas_card.json": ["She's fine. You're not fine."],
    "Svartulfr_Lorebook_II.json": [
        "By anchoring her healing Source into subterranean stone",
        "her spirit acts as a Boundless Vital Conduit",
        "She can continuously channel sacred healing magic",
        "She is at the nursery daily",
        "Dressing a White Moon is not something she does alone",
        "It is done for her, by the household",
        "Neither does Kaladin, and neither does she",
        "The reason is that she is the White Moon"],
    "Svartulfr_NPC_Primary.json": ["Hank Thompson"],
}

for fn, needles in targets.items():
    path = os.path.join(FINAL, fn)
    d = json.load(open(path, encoding="utf-8"))
    blob = json.dumps(d, ensure_ascii=False)
    print("=" * 100)
    print("FILE:", fn)
    # section-by-section
    def scan(obj, pathid=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                scan(v, pathid + "/" + str(k))
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                scan(v, pathid + "[%d]" % i)
        elif isinstance(obj, str):
            if FEM.search(obj):
                for n in needles:
                    if n in obj:
                        for s, sent in sentences(obj, [n]):
                            print("  @%s :: %s" % (pathid, repr(sent)))
                        break
    scan(d)
