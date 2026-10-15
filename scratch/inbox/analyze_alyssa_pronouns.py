import os
import re
import glob

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")
pron = re.compile(r"\b(she|her|hers|herself)\b", re.I)

for p in sorted(glob.glob(os.path.join(FINAL, "*.json"))):
    t = open(p, encoding="utf-8").read()
    sents = re.split(r"(?<=[.!?])\s+", t)
    lines = []
    for sent in sents:
        if "Alyssa" not in sent:
            continue
        for m in pron.finditer(sent):
            a = max(0, m.start() - 45)
            b = min(len(sent), m.end() + 45)
            frag = sent[a:b].replace("\n", " ").replace("\\n", " ")
            lines.append("   ..." + frag + "...")
    if lines:
        print("=== " + os.path.basename(p) + " (" + str(len(lines)) + ")")
        for ln in lines:
            print(ln)
