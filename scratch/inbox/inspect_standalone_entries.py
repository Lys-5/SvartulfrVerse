# -*- coding: utf-8 -*-
"""Dettaglio dei 5 export standalone (Mine) nel backup consolidato del 14/10."""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "scratch", "backup_consolidated_snapshot", "mine_standalone_characters.json")

with open(SRC, encoding="utf-8") as fh:
    data = json.load(fh)

print("root type:", type(data).__name__, "len:", len(data))
for i, c in enumerate(data):
    if not isinstance(c, dict):
        continue
    print("\n" + "#" * 80)
    print(f"# [{i}] {c.get('name')!r}")
    print("#" * 80)
    print("  TOP-LEVEL KEYS:", sorted(c.keys()))
    for f in ["description", "personality", "scenario", "first_mes", "mes_example",
              "creator_notes", "system_prompt", "post_history_instructions"]:
        v = c.get(f)
        ln = len(v) if isinstance(v, str) else ("N/A" if v is None else type(v).__name__)
        print(f"  {f:26}: {ln}")
    print(f"  tags: {c.get('tags')}")
    print(f"  Alyssa in description: {'Alyssa' in (c.get('description') or '')}")
    print(f"  HEADER: {(c.get('description') or '').split(chr(10))[0][:280]}")
    print(f"  first_mes: {json.dumps(c.get('first_mes'), ensure_ascii=False)[:200]}")
    print(f"  keys: {c.get('keys')}")
    print(f"  rpg_stats: {json.dumps(c.get('rpg_stats'), ensure_ascii=False)}")
    print(f"  default_outfit: {c.get('default_outfit')}")
    print(f"  avatar: {c.get('avatar')}")
    print(f"  shared_info type: {type(c.get('shared_info')).__name__}  pronouns: {json.dumps(c.get('pronouns'), ensure_ascii=False)[:120]}")
    print(f"  metadata: {json.dumps(c.get('metadata'), ensure_ascii=False)[:200]}")
    print(f"  rating/visibility: {c.get('rating')} / {c.get('visibility')}")
    o = c.get("outfits")
    if isinstance(o, str):
        try:
            o = json.loads(o)
        except Exception:
            o = []
    if isinstance(o, list):
        print(f"  outfits ({len(o)}):")
        for x in o:
            if isinstance(x, dict):
                print(f"     - {x.get('id')} | {x.get('name')}")
    lex = c.get("lexicon")
    if isinstance(lex, str):
        try:
            lex = json.loads(lex)
        except Exception:
            lex = None
    if isinstance(lex, list):
        print(f"  lexicon ({len(lex)}): {[e.get('name') for e in lex if isinstance(e, dict)]}")
    else:
        print(f"  lexicon: {type(lex).__name__}")
    fi = c.get("final_instructions")
    print(f"  final_instructions: {len(fi) if isinstance(fi, str) else 'N/A'}")
    print(f"  pre_history_instructions: {len(c.get('pre_history_instructions') or '') if isinstance(c.get('pre_history_instructions'), str) else 'N/A'}")
    print(f"  character_note: {json.dumps(c.get('character_note'), ensure_ascii=False)[:160]}")
