import json
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')
f_prim = ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json'
o_prim = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json'

with open(f_prim, 'r', encoding='utf-8') as f:
    d_f = json.load(f)

with open(o_prim, 'r', encoding='utf-8') as f:
    d_o = json.load(f)

diffs = []
for k in d_f.keys():
    if k not in d_o:
        diffs.append(f"Key {k} in FINAL but not optimized")
for k in d_o.keys():
    if k not in d_f:
        diffs.append(f"Key {k} in optimized but not FINAL")

entries_f = d_f.get('lexicon', [])
entries_o = d_o.get('lexicon', [])
print(f"Entries count: FINAL={len(entries_f)}, opt={len(entries_o)}")

for i, (ef, eo) in enumerate(zip(entries_f, entries_o)):
    if ef.get('name') != eo.get('name'):
        print(f"Entry {i} name mismatch: {ef.get('name')} vs {eo.get('name')}")
    if ef.get('avatar') != eo.get('avatar'):
        print(f"Entry {i} ({ef.get('name')}) avatar diff:\n  FINAL: {ef.get('avatar')}\n  OPT:   {eo.get('avatar')}")
    if ef.get('content') != eo.get('content'):
        print(f"Entry {i} ({ef.get('name')}) content diff! len {len(ef.get('content'))} vs {len(eo.get('content'))}")

f_sec = ROOT / 'FINAL' / 'Svartulfr_NPC_Secondary.json'
o_sec = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Secondary.json'
with open(f_sec, 'r', encoding='utf-8') as f:
    df_sec = json.load(f)
with open(o_sec, 'r', encoding='utf-8') as f:
    do_sec = json.load(f)
print(f"Secondary entries count: FINAL={len(df_sec.get('lexicon', []))}, opt={len(do_sec.get('lexicon', []))}")
sec_diffs = []
for i, (ef, eo) in enumerate(zip(df_sec.get('lexicon', []), do_sec.get('lexicon', []))):
    if ef.get('avatar') != eo.get('avatar'):
        sec_diffs.append(f"Entry {i} ({ef.get('name')}) avatar diff: {ef.get('avatar')} vs {eo.get('avatar')}")
    if ef.get('content') != eo.get('content'):
        sec_diffs.append(f"Entry {i} ({ef.get('name')}) content diff")
print("Secondary diffs:", len(sec_diffs))
