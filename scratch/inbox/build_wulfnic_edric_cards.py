# -*- coding: utf-8 -*-
"""
Genera le Character Card V2 di Wulfnic e Edric in FINAL/, riusando la pipeline
di scripts/generate_main_cast_cards.py (build_card) + genericizzazione AnyPOV.

Fonti piu recenti (verificate):
  - Wulfnic: scratch/backup_consolidated_snapshot/world_characters.json
             (snapshot 14/10, display_name 'Wulfnic Báleygr Bloodmoon',
              header con BIRTH_RUNE: Othala) -> piu recente di Svartulfr_Export.json (13/10).
  - Edric:   exports/Svartulfr_Export.json (13/10). Edric NON e presente nello
             snapshot 14/10 (assente dal world export).

Scenari/first_mes/system_prompt: da scripts/sync_characters_cards.py (pipeline autoriale).
Blocco extensions.wyvern incluso da build_card (fix import outfit WyvernChat).
Genericizzazione: Alyssa -> {{user}} via scripts/genericize_alyssa.walk.
"""

import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINAL = os.path.join(BASE, "FINAL")
SCRIPTS = os.path.join(BASE, "scripts")
sys.path.insert(0, SCRIPTS)
sys.path.insert(0, BASE)

from generate_main_cast_cards import build_card                      # noqa: E402
from genericize_alyssa import walk as genericize                     # noqa: E402

SNAPSHOT_WORLD = os.path.join(BASE, "scratch", "backup_consolidated_snapshot",
                              "world_characters.json")
EXPORT_SVART = os.path.join(BASE, "exports", "Svartulfr_Export.json")

TARGETS = [
    {
        "id": "_W9PLYt9ERTBJBXqKQL2en",
        "file": "Wulfnic_Bloodmoon_card.json",
        "source": SNAPSHOT_WORLD,
        "scenario": (
            "The ancient Longhouse deep inside the Dead Zone, where the technology of "
            "Blackwood City goes completely dead and the Alpha of Alphas keeps vigil over "
            "centuries of wolf memory."
        ),
        "first_mes": (
            "The hum of Blackwood's digital grid dies away entirely the moment you cross into "
            "the Dead Zone. Beneath the colossal cedar beams of the Longhouse, ancient braziers "
            "cast shifting shadows across carved stone runes and dried herbs hanging from the "
            "rafters.\n\n"
            "Wulfnic sits upon a broad wooden bench, his silver hair and beard catching the "
            "firelight, amber eyes ancient, fathomless, and heavy with a thousand winters. He "
            "gestures slowly toward the woven rug before the hearth, his voice deep as thunder "
            "rolling over frozen mountains. \"Step into the light of the hearth and be warm. The "
            "modern world outside moves too fast for its own blood. Here, we remember what "
            "remains.\""
        ),
        "system_prompt": (
            "Roleplay as Wulfnic Bloodmoon in the Svart\u00falfr | Modern Fantasy universe. "
            "Wulfnic is the Alpha of Alphas, one of the Last Three Firstborn, and the living "
            "patriarch of House Bloodmoon. He speaks slowly and without urgency, ancient and "
            "resonant, carrying the wisdom and grief of twelve centuries."
        ),
    },
    {
        "id": "_YJQ4cjdrT7brm7HWVkf3K",
        "file": "Edric_Douglas_card.json",
        "source": EXPORT_SVART,
        "scenario": (
            "The hallway or living area of Villa Douglas, where twelve-year-old Edric tries to "
            "project an aura of unbothered teenage bravado while secretly seeking shelter from "
            "the adult Alphas."
        ),
        "first_mes": (
            "Edric shuffles into the room wearing a black streetwear hoodie at least two sizes "
            "too big, trying desperately to project an aura of effortless coolness as he adjusts "
            "an oversized pair of sunglasses indoors. He leans against the doorframe, catches his "
            "toe on the rug, and quickly crosses his thin arms to recover.\n\n"
            "\"Oh, hey. Did not hear you coming. I was just, like, grinding on some high-value "
            "tasks. You know how it is.\" Edric glances nervously over his shoulder toward the "
            "main foyer, his scent spiking with faint Gamma anxiety before he steps closer. "
            "\"Are the Alphas busy? I kind of just wanted to hang out in here for a bit, if that "
            "is cool.\""
        ),
        "system_prompt": (
            "Roleplay as Edric Douglas in the Svart\u00falfr | Modern Fantasy universe. "
            "Edric is a 12-year-old Pureblood House Douglas pup, publicly Logan's claimed son but "
            "biologically Erik's. He is terrified of his upcoming First Shift and hides his "
            "insecurity behind Gen-Z slang and sigma grindset memes. He is strictly a minor "
            "background NPC: zero romantic or intimate framing under any circumstances."
        ),
        # Discrepanza Regola 05: il record carattere (13/10) riporta BIRTH_RUNE Uruz,
        # ma il lorebook deploy_step3 (14/10) assegna Ingwaz a Edric (in attesa della
        # Presentazione). Prevale il lorebook (livello gerarchico superiore + piu recente).
        "header_patch": [
            (
                "BIRTH_RUNE: Uruz (Strength/Ox);",
                "BIRTH_RUNE: Ingwaz (Il Potenziale in Germoglio, in attesa della maturita);",
            )
        ],
    },
]


def load_source(path):
    data = json.load(open(path, encoding="utf-8"))
    chars = data if isinstance(data, list) else data.get("world_characters", [])
    return {c.get("id"): c for c in chars if isinstance(c, dict)}


def main():
    os.makedirs(FINAL, exist_ok=True)
    cache = {}

    for t in TARGETS:
        if t["source"] not in cache:
            cache[t["source"]] = load_source(t["source"])
        web_c = cache[t["source"]].get(t["id"])
        if not web_c:
            print("WARN: id %s non trovato in %s" % (t["id"], os.path.basename(t["source"])))
            continue

        card, display_name = build_card(web_c, t)
        card = genericize(card, False)

        # Applica le correzioni di discrepanza (Regola 05) ai campi description
        # sia a livello root sia nel mirror data, senza toccare i sorgenti.
        for old, new in t.get("header_patch", []):
            for node in (card, card.get("data", {})):
                if isinstance(node, dict) and isinstance(node.get("description"), str):
                    node["description"] = node["description"].replace(old, new)

        resid = len(re.findall(r"Alyssa|alyssa|ALYSSA", json.dumps(card, ensure_ascii=False)))
        out_path = os.path.join(FINAL, t["file"])
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(card, fh, indent=2, ensure_ascii=False)

        w = card["extensions"]["wyvern"]
        print("OK %-28s -> %-30s desc=%d outfits=%d wyvern_outfits=%d residui_Alyssa=%d user=%d"
              % (display_name, t["file"], len(card["description"]),
                 len(card["extensions"]["outfits"]), len(w["outfits"]), resid,
                 card["description"].count("{{user}}")))
        print("   HEADER:", card["description"].split("\n")[0][:220])


if __name__ == "__main__":
    main()
