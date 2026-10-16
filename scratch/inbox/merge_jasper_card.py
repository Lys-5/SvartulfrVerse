# -*- coding: utf-8 -*-
"""
Merge one-off della card di Jasper.

Il file FINAL/Jasper_Douglas_Bloodmoon_card.json contiene DUE blocchi JSON accodati:
  - B1: la card V2 (chara_card_v2) genericizzata, generata da generate_main_cast_cards.py
  - B2: l'export nativo Wyvern del personaggio, accodato dall'utente come "aggiornamenti"

Scelte dell'utente:
  1) name           -> B2  ("Jasper Svartr Douglas Bloodmoon")
  2) scenario       -> B1
  3) creator_notes  -> B1
  4) mes_example    -> B1
  5) RPG stats      -> B2  (LV 3, INT 18)
Default: contenitore = B1 (V2), campi nuovi di B2 in extensions, genericizzazione
(Alyssa -> {{user}}) del materiale importato, first_mes = B1, tags += forked,
outfits = B2 (10 voci) + default_outfit, file riscritto come JSON valido.

Backup del file originale in scratch/backup_final_premerge/.
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
CARD = os.path.join(FINAL, "Jasper_Douglas_Bloodmoon_card.json")
BACKUP = os.path.join(BASE, "scratch", "backup_final_premerge")

sys.path.insert(0, os.path.join(BASE, "scripts"))
from genericize_alyssa import process_string, walk  # noqa: E402

RPG_BASE_STATS = {
    "strength": 8, "perception": 14, "endurance": 10, "charisma": 8,
    "intelligence": 18, "agility": 13, "luck": 10,
}
RPG_LEVEL = 3

# Campi presenti solo in B2 da importare in extensions (i vuoti vengono saltati).
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


def load_blocks(path):
    raw = open(path, encoding="utf-8").read()
    dec = json.JSONDecoder()
    obj1, end1 = dec.raw_decode(raw.lstrip())
    lead = len(raw) - len(raw.lstrip())
    rest = raw[lead + end1:]
    obj2, end2 = dec.raw_decode(rest.lstrip())
    tail = rest.lstrip()[end2:].strip()
    return raw, obj1, obj2, tail


def is_empty(v):
    return v in (None, "", [], {}, 0, False)


def main():
    raw, b1, b2, tail = load_blocks(CARD)
    assert tail == "", "Contenuto extra imprevisto dopo il secondo blocco: %r" % tail[:80]

    # Backup del file originale (non valido) prima di riscrivere.
    if not os.path.isdir(BACKUP):
        os.makedirs(BACKUP)
    shutil.copy2(CARD, os.path.join(BACKUP, os.path.basename(CARD)))

    # --- Genericizzazione del blocco B2 -------------------------------------
    b2g = copy.deepcopy(b2)
    b2g = walk(b2g, False)
    resid = len(re.findall(r"Alyssa|alyssa|ALYSSA", json.dumps(b2g, ensure_ascii=False)))
    print("Residui 'Alyssa' in B2 genericizzato:", resid)

    # --- Sanity check: B1.description == genericize(B2.description) + 2 diff? -
    merged_desc = process_string(b2["description"], False)
    diff = list(difflib.unified_diff(
        b1["description"].splitlines(), merged_desc.splitlines(),
        "B1-desc", "B2-desc-genericized", lineterm="", n=0))
    print("Diff B1.description vs genericize(B2.description): %d righe di diff" % len(diff))

    # --- Costruzione card unificata -----------------------------------------
    merged = {
        "spec": b1["spec"],
        "spec_version": b1["spec_version"],
        "name": b2g["name"],                       # 1) B2
        "description": b2g["description"],         # B1-genericizzata + aggiunte B2
        "personality": b1["personality"],          # B1
        "scenario": b1["scenario"],                # 2) B1
        "first_mes": b1["first_mes"],              # B1
        "mes_example": b1["mes_example"],          # 4) B1
        "creator_notes": b1["creator_notes"],      # 3) B1
        "system_prompt": b1["system_prompt"],
        "post_history_instructions": b1["post_history_instructions"],
        "alternate_greetings": b1["alternate_greetings"],
        "tags": b1["tags"] + ([] if "forked" in b1["tags"] else ["forked"]),
        "creator": b1["creator"],
        "character_version": b1["character_version"],
    }

    ext = copy.deepcopy(b1["extensions"])

    # outfits: 10 voci di B2, con schema coerente alle card sorelle (id,name,avatar,description)
    ext["outfits"] = [
        {
            "id": o.get("id"),
            "name": o.get("name"),
            "avatar": o.get("avatar", ""),
            "description": o.get("description", ""),
        }
        for o in b2g.get("outfits", [])
    ]
    ext["default_outfit"] = b2g.get("default_outfit")

    # rpg_stats: 5) prevale B2 (livello + base_stats), id specie/occupazione invariati
    rpg = dict(ext.get("rpg_stats", {}))
    rpg["level"] = RPG_LEVEL
    rpg["base_stats"] = dict(RPG_BASE_STATS)
    ext["rpg_stats"] = rpg

    # Campi nuovi di B2 -> extensions (saltando i vuoti)
    skipped = []
    for k in B2_EXTRA_FIELDS:
        v = b2g.get(k)
        if k not in b2g or is_empty(v):
            skipped.append(k)
            continue
        ext[k] = v

    merged["extensions"] = ext
    merged["data"] = {k: merged[k] for k in DATA_KEYS}

    # --- Scrittura ----------------------------------------------------------
    with open(CARD, "w", encoding="utf-8") as fh:
        json.dump(merged, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    # --- Report -------------------------------------------------------------
    s = json.dumps(merged, ensure_ascii=False)
    print("Scritto:", CARD)
    print("JSON valido:", bool(json.loads(open(CARD, encoding='utf-8').read())))
    print("Residui 'Alyssa':", len(re.findall(r"Alyssa|alyssa|ALYSSA", s)))
    print("{{user}} count:", s.count("{{user}}"))
    print("name:", merged["name"])
    print("tags:", merged["tags"])
    print("outfits:", len(merged["extensions"]["outfits"]),
          [o["name"] for o in merged["extensions"]["outfits"]])
    print("default_outfit:", merged["extensions"]["default_outfit"])
    print("rpg_stats:", merged["extensions"]["rpg_stats"])
    print("extensions keys:", list(merged["extensions"].keys()))
    print("campi B2 saltati (vuoti/assenti):", skipped)


if __name__ == "__main__":
    main()
