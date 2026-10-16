# -*- coding: utf-8 -*-
"""
Fix import outfit su WyvernChat per le 5 card del Main Cast in FINAL/.

Causa (da chunk JS WyvernChat, codice di import N(e)):
    e.data !== undefined && (e = e.data);
    let u = e.extensions?.wyvern ?? e;
    d.pronouns = u.pronouns; d.outfits = u.outfits; d.default_outfit = u.default_outfit;

Wyvern legge outfits/pronouns/default_outfit da `extensions.wyvern` (o dal root).
Le nostre card li avevano in `extensions.outfits` (senza nesting `wyvern`) -> non importati.

Fix: aggiungere `extensions.wyvern = {pronouns, outfits, default_outfit,
enable_advanced_greetings, greetings}`, sia nel root sia nel mirror `data.extensions`.
Schema outfit nativo server (snapshot): {id, name, description} (senza `avatar`).

Non distruttivo: la chiave piatta `extensions.outfits` viene mantenuta.
Backup in scratch/backup_final_prewyvern/.
"""

import json
import os
import shutil

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")
BACKUP = os.path.join(BASE, "scratch", "backup_final_prewyvern")

FILES = [
    "Erik_Douglas_card.json",
    "Logan_Douglas_card.json",
    "Jasper_Douglas_Bloodmoon_card.json",
    "Malachia_Douglas_Bloodmoon_card.json",
    "Noah_Douglas_Bloodmoon_card.json",
]


def build_wyvern(ext):
    outfits = [
        {
            "id": o.get("id"),
            "name": o.get("name"),
            "description": o.get("description", ""),
        }
        for o in ext.get("outfits", [])
    ]
    return {
        "pronouns": ext.get("pronouns"),
        "outfits": outfits,
        "default_outfit": ext.get("default_outfit"),
        "enable_advanced_greetings": False,
        "greetings": [],
    }


def main():
    if not os.path.isdir(BACKUP):
        os.makedirs(BACKUP)

    for fn in FILES:
        path = os.path.join(FINAL, fn)
        with open(path, encoding="utf-8") as fh:
            card = json.load(fh)

        shutil.copy2(path, os.path.join(BACKUP, fn))

        touched = []
        if isinstance(card.get("extensions"), dict):
            card["extensions"]["wyvern"] = build_wyvern(card["extensions"])
            touched.append("root")
        data = card.get("data")
        if isinstance(data, dict) and isinstance(data.get("extensions"), dict):
            data["extensions"]["wyvern"] = build_wyvern(data["extensions"])
            touched.append("data")

        with open(path, "w", encoding="utf-8") as fh:
            json.dump(card, fh, ensure_ascii=False, indent=2)

        w = card["extensions"]["wyvern"]
        print("%-42s wyvern@%-9s outfits=%d default=%s pronouns=%s"
              % (fn, "+".join(touched), len(w["outfits"]),
                 w["default_outfit"], bool(w["pronouns"])))

    print("\nBackup: %s" % BACKUP)


if __name__ == "__main__":
    main()
