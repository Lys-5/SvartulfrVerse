# -*- coding: utf-8 -*-
"""
Merge generalizzato delle Character Card V2 del Main Cast con gli export
standalone (Mine) aggiornati, rinvenuti nel backup consolidato del 14/10
(scratch/backup_consolidated_snapshot/mine_standalone_characters.json).

Applica le stesse regole approvate per la card di Jasper:
  1) name          -> export standalone (nome con secondo nome di branco)
  2) scenario      -> card V2 (B1)
  3) creator_notes -> card V2 (B1)
  4) mes_example   -> card V2 (B1)
  5) RPG stats     -> export standalone se presente, altrimenti card (B1)
Default: contenitore = card V2; campi nuovi dello standalone in extensions;
genericizzazione (Alyssa -> {{user}}) del materiale importato; first_mes = B1;
tags += forked; outfits = standalone (superset, include Full Shift/Hybrid Shift)
+ default_outfit; file riscritto come JSON valido.

Uso:
  python scratch/inbox/merge_family_cards.py          # dry-run (nessuna scrittura)
  python scratch/inbox/merge_family_cards.py apply    # scrive e fa il backup
"""

import copy
import difflib
import json
import os
import re
import shutil
import sys

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")
STANDALONE = os.path.join(BASE, "scratch", "backup_consolidated_snapshot",
                          "mine_standalone_characters.json")
BACKUP = os.path.join(BASE, "scratch", "backup_final_prefamily")

sys.path.insert(0, os.path.join(BASE, "scripts"))
from genericize_alyssa import process_string, walk  # noqa: E402

# (file card in FINAL, nome del personaggio nello standalone)
TARGETS = [
    ("Erik_Douglas_card.json", "Erik Ulfr Douglas"),
    ("Logan_Douglas_card.json", "Logan Járn Douglas"),
    ("Malachia_Douglas_Bloodmoon_card.json", "Malachia Björn Douglas Bloodmoon"),
    ("Noah_Douglas_Bloodmoon_card.json", "Noah Loki Douglas Bloodmoon"),
]

B2_EXTRA_FIELDS = [
    "avatar", "backgroundURL", "tagline", "character_note",
    "pre_history_instructions", "rating", "visibility",
    "shared_info", "pronouns", "metadata", "lexicon",
]
DATA_KEYS = [
    "name", "description", "personality", "scenario", "first_mes", "mes_example",
    "creator_notes", "system_prompt", "post_history_instructions",
    "alternate_greetings", "tags", "creator", "character_version", "extensions",
]


def is_empty(v):
    return v in (None, "", [], {}, 0, False)


def load_json(path):
    raw = open(path, encoding="utf-8").read()
    dec = json.JSONDecoder()
    obj, end = dec.raw_decode(raw.lstrip())
    tail = raw.lstrip()[end:].strip()
    return obj, tail


def build_merged(b1, b2_raw):
    b2 = copy.deepcopy(b2_raw)
    b2 = walk(b2, False)  # genericizzazione AnyPOV
    resid = len(re.findall(r"Alyssa|alyssa|ALYSSA", json.dumps(b2, ensure_ascii=False)))

    merged = {
        "spec": b1["spec"],
        "spec_version": b1["spec_version"],
        "name": b2["name"],                        # 1) standalone
        "description": b2["description"],          # header aggiornato + adds standalone
        "personality": b1["personality"],
        "scenario": b1["scenario"],                # 2) card
        "first_mes": b1["first_mes"],
        "mes_example": b1["mes_example"],          # 4) card
        "creator_notes": b1["creator_notes"],      # 3) card
        "system_prompt": b1["system_prompt"],
        "post_history_instructions": b1["post_history_instructions"],
        "alternate_greetings": b1["alternate_greetings"],
        "tags": b1["tags"] + ([] if "forked" in b1["tags"] else ["forked"]),
        "creator": b1["creator"],
        "character_version": b1["character_version"],
    }

    ext = copy.deepcopy(b1["extensions"])
    ext["outfits"] = [
        {
            "id": o.get("id"),
            "name": o.get("name"),
            "avatar": o.get("avatar", ""),
            "description": o.get("description", ""),
        }
        for o in b2.get("outfits", [])
    ]
    ext["default_outfit"] = b2.get("default_outfit")

    # 5) RPG stats: lo standalone prevale solo se valorizzato.
    rpg_b2 = b2.get("rpg_stats")
    if isinstance(rpg_b2, dict) and rpg_b2:
        rpg = dict(ext.get("rpg_stats", {}))
        if rpg_b2.get("level") is not None:
            rpg["level"] = rpg_b2["level"]
        if rpg_b2.get("base_stats"):
            rpg["base_stats"] = dict(rpg_b2["base_stats"])
        if rpg_b2.get("species_id"):
            rpg["species_id"] = rpg_b2["species_id"]
        if rpg_b2.get("occupation_id"):
            rpg["occupation_id"] = rpg_b2["occupation_id"]
        ext["rpg_stats"] = rpg
        rpg_src = "standalone"
    else:
        rpg_src = "card (standalone vuoto)"

    skipped = []
    for k in B2_EXTRA_FIELDS:
        v = b2.get(k)
        if k not in b2 or is_empty(v) or v == "[Circular]":
            skipped.append(k)
            continue
        ext[k] = v

    merged["extensions"] = ext
    merged["data"] = {k: merged[k] for k in DATA_KEYS}
    return merged, b2, resid, skipped, rpg_src


def report(fname, b1, b2, merged, resid, skipped, rpg_src):
    print("\n" + "=" * 82)
    print(f"CARD: {fname}")
    print("=" * 82)
    print(f"  name        : {b1['name']!r}  ->  {merged['name']!r}")
    print(f"  personalities: card {len(b1['personality'])} / standalone {len(b2.get('personality') or '')}")
    print(f"  scenarios    : card {len(b1['scenario'])} / standalone {len(b2.get('scenario') or '')} (mantengo card)")
    print(f"  first_mes    : card {len(b1['first_mes'])} / standalone {b2.get('first_mes')!r} (mantengo card)")
    print(f"  mes_example  : card {len(b1['mes_example'])} / standalone {len(b2.get('mes_example') or '')} (mantengo card)")
    print(f"  creator_notes: card {len(b1['creator_notes'])} / standalone {len(b2.get('creator_notes') or '')} (mantengo card)")
    print(f"  tags         : {merged['tags']}")
    print(f"  alt_greetings: card {len(b1.get('alternate_greetings') or [])} / standalone {len(b2.get('alternate_greetings') or [])} (mantengo card)")
    print(f"  rpg_stats    : {rpg_src} -> {json.dumps(merged['extensions']['rpg_stats'], ensure_ascii=False)}")
    co = (b1.get("extensions") or {}).get("outfits") or []
    so = merged["extensions"]["outfits"]
    print(f"  outfits      : card {len(co)} -> standalone {len(so)}")
    print(f"     card : {[o.get('name') for o in co]}")
    print(f"     new  : {[o.get('name') for o in so]}")
    print(f"  default_outfit: {merged['extensions']['default_outfit']}")
    print(f"  campi standalone importati in extensions: "
          f"{[k for k in B2_EXTRA_FIELDS if k in merged['extensions']]}")
    print(f"  campi saltati (vuoti/assenti): {skipped}")
    print(f"  residui 'Alyssa' dopo genericizzazione: {resid}")
    print(f"  {{user}} nella card unita: {json.dumps(merged, ensure_ascii=False).count('{{user}}')}")
    d = list(difflib.unified_diff(
        (b1.get("description") or "").splitlines(),
        merged["description"].splitlines(),
        "card-desc", "merged-desc", lineterm="", n=0))
    print(f"  diff description: {len(d)} righe")
    for line in d[2:8]:
        print("     " + line[:200])


def main():
    apply = len(sys.argv) > 1 and sys.argv[1] == "apply"

    with open(STANDALONE, encoding="utf-8") as fh:
        standalone = json.load(fh)
    by_name = {c.get("name"): c for c in standalone if isinstance(c, dict)}

    if apply and not os.path.isdir(BACKUP):
        os.makedirs(BACKUP)

    for fname, sname in TARGETS:
        card_path = os.path.join(FINAL, fname)
        b1, tail = load_json(card_path)
        if tail:
            print(f"!! {fname}: contenuto extra dopo il blocco JSON: {tail[:60]!r}")
        b2 = by_name.get(sname)
        if b2 is None:
            print(f"!! {sname} non trovato nello standalone")
            continue
        merged, b2g, resid, skipped, rpg_src = build_merged(b1, b2)
        report(fname, b1, b2g, merged, resid, skipped, rpg_src)
        if apply:
            shutil.copy2(card_path, os.path.join(BACKUP, fname))
            with open(card_path, "w", encoding="utf-8") as fh:
                json.dump(merged, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
            ok = bool(json.loads(open(card_path, encoding="utf-8").read()))
            print(f"  -> SCRITTO {card_path} (JSON valido: {ok})")

    print("\nMODALITA':", "APPLY (scritto)" if apply else "DRY-RUN (nessuna scrittura)")
    if apply:
        print("Backup in:", BACKUP)


if __name__ == "__main__":
    main()
