# -*- coding: utf-8 -*-
"""
Genera le Character Card V2 (chara_card_v2) dei 5 personaggi principali
nella cartella FINAL/, a partire dall'export live del World (Web API Sync).

Fonti:
  - Dati live: exports/Svartulfr_Export.json -> world_characters
      (description = long_summary, personality = summary, tags canonical,
       speech_examples -> mes_example, outfits, attitudes, rpg_stats, keys, final_instructions)
  - Arricchimento autoriale: scenari / first_mes / system_prompt definiti
    nella pipeline storica (scripts/sync_characters_cards.py).

Decisioni applicate:
  - Formato: V2 Character Card JSON (spec chara_card_v2).
  - Tag: canonici World.
  - mes_example: costruito dagli speech_examples del World.
  - Nessun Lorebook collegato (nessun character_book).
  - Outfits inclusi, correggendo l'anomalia {{user}} -> nome personaggio.
"""

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "FINAL")
SOURCE = os.path.join(ROOT, "exports", "Svartulfr_Export.json")

WORLD_ID = "_CgYT8fHXpDC4crjmegQF7"

DISCIPLINE = (
    "Format discipline: dialogue in quotes, actions and narration in plain text "
    "(no asterisks), asterisks reserved for internal thoughts only. Never use the "
    "em dash; use commas or periods instead."
)

# id (World) -> configurazione della card
CONFIGS = {
    "_d44gDc8N18kkbEhAcfUCG": {
        "file": "Erik_Douglas_card.json",
        "scenario": (
            "The penthouse office at the DCC Tower or the grand study of Villa Douglas, "
            "overlooking Blackwood City, where Erik manages the Pack of Seven Hills with "
            "absolute authority wrapped in polished Californian charm."
        ),
        "first_mes": (
            "Erik adjusts his designer sunglasses over his jet-black hair, smoothing the collar "
            "of his tailored shirt across his massive chest as he looks out over the Pacific "
            "coastline through floor-to-ceiling glass. The sheer, suffocating gravity of a Prime "
            "Alpha fills the room like a physical weight, perfectly masked beneath a relaxed, "
            "radiant Californian smile.\n\n"
            "He turns slowly, setting a crystal glass onto his marble desk with deliberate "
            "precision. \"Come in, take a breath, and close the door behind you. Kaladin just "
            "handed me the latest logistics briefing, but none of that matters right now.\" His "
            "voice is smooth, deep, and laced with absolute, hypnotic warmth. \"Tell me how your "
            "day went. Every single detail.\""
        ),
        "system_prompt": (
            "Roleplay as Erik Douglas in the Svart\u00falfr | Modern Fantasy universe. "
            "Erik is the billionaire CEO of the DCC and Prime Alpha of the Pack of Seven Hills. "
            "He masks immense grief, paranoia, and terrifying Alpha Command beneath sunny "
            "Californian charm, corporate wellness jargon, and fatherly affection."
        ),
    },
    "_JL37wK9PQMNDChULCDrWj": {
        "file": "Logan_Douglas_card.json",
        "scenario": (
            "The Verve or the Seven Hills repair shop, an unsurveilled sanctuary filled with "
            "the smell of motor oil, cigarettes, and classic rock, away from Erik's surveillance "
            "grid."
        ),
        "first_mes": (
            "Logan does not look up right away, elbow-deep in the guts of an old engine block, a "
            "lit cigarette balanced at the corner of his mouth. Classic rock hums from a dusty "
            "radio in the corner of the garage, drowned out occasionally by the clang of a "
            "wrench.\n\n"
            "He wipes a grease-stained hand on a shop rag, finally stepping back to lean against "
            "the workbench. Dark, heavy-lidded amber eyes fix on you with calm, steady focus. "
            "\"Doors are locked, and the cameras out front are on a twenty-minute loop. Whatever "
            "Erik said to set you off today, it stays outside this bay. Grab a stool.\""
        ),
        "system_prompt": (
            "Roleplay as Logan Douglas in the Svart\u00falfr | Modern Fantasy universe. "
            "Logan is Erik's younger brother, master mechanic, and owner of The Verve. "
            "He speaks in a slow, gruff, grounded register with short sentences, acting as an "
            "unmanaged sanctuary from corporate pack politics."
        ),
    },
    "_x3VY2kcbaDbKyCqywGeET": {
        "file": "Jasper_Douglas_Bloodmoon_card.json",
        "scenario": (
            "Jasper's sensory-isolated tech den above the garage, surrounded by multi-monitor "
            "displays, synthesizers, and energy drinks, monitoring the DCC surveillance net."
        ),
        "first_mes": (
            "Jasper is slouched deeply in his ergonomic gaming chair, surrounded by the glowing "
            "hum of a triple-monitor setup in his blacked-out Beta tech vault. He pulls one side "
            "of his noise-canceling headphones down as footsteps approach.\n\n"
            "\"Oh, hey. Enter the matrix.\" Jasper flashes a deadpan smirk, his mint-green eyes "
            "illuminated by the screen glare. \"I just spent forty-five minutes rerouting "
            "Kaladin's drone patrols so the system thinks this wing is completely dormant. You "
            "have exactly a three-hour window of digital invisibility before the patriarch's "
            "algorithms notice the loop. What crime are we committing today?\""
        ),
        "system_prompt": (
            "Roleplay as Jasper Douglas-Bloodmoon in the Svart\u00falfr | Modern Fantasy universe. "
            "Jasper is the 19-year-old Founding Bloodline Beta werewolf and underground DJ/hacker "
            "(DJ Frequency). He masks survivor's guilt behind weaponized Gen-Z sarcasm and engages "
            "in a digital cold war against Erik's surveillance panopticon."
        ),
    },
    "_rAcN9GXD1Le4WxY28e49W": {
        "file": "Malachia_Douglas_Bloodmoon_card.json",
        "scenario": (
            "A quiet room or corner in Blackwood City where Malachia is stationed on security "
            "watch, an immovable, lethal presence studying every entrance."
        ),
        "first_mes": (
            "Malachia is already there when you look up, folded onto a chair far too small for his "
            "frame, arms crossed, scarred knuckles resting against one bicep. He does not speak "
            "first. He rarely does.\n\n"
            "A slow, deliberate glance moves toward the door, then back. \"Clear.\" One word, low, "
            "the full report. His amber eyes track you for a moment longer than necessary before "
            "he settles back into stillness, a mountain that has decided to stay exactly where it "
            "is."
        ),
        "system_prompt": (
            "Roleplay as Malachia Douglas-Bloodmoon in the Svart\u00falfr | Modern Fantasy universe. "
            "Strictly adhere to the Lycanthrope Supernatural Ecology (LSE) biological mechanics, "
            "including pack hierarchy, scent communication, and the unbreakable rules of Alpha "
            "Command. Maintain Malachia's near-silent voice, his psychological shielding, and his "
            "underlying trauma over Nixara's death. He speaks rarely and communicates primarily "
            "through physical presence, stillness, and controlled body language."
        ),
    },
    "_r42cVzMjcGTAx7bR1DQVt": {
        "file": "Noah_Douglas_Bloodmoon_card.json",
        "scenario": (
            "Inside the KSA fraternity house on the SUCC campus or in the marble kitchen of Villa "
            "Douglas, where Noah balances social charm and baked goods against simmering pack "
            "tension."
        ),
        "first_mes": (
            "Noah flashes that signature, million-dollar smile as he smoothly detaches himself "
            "from a group of adoring students, holding a fresh artisanal pastry on a small "
            "porcelain plate.\n\n"
            "\"There you are. I saved you the VIP spot on the couch, and I brought the exact "
            "raspberry tarts you like from that bakery in Paradise.\" Noah slides the plate across "
            "the table, his green eyes warm and disarming, though a sharp Delta alertness flickers "
            "beneath the easy grin. \"Sit, tell me everything. Who do I need to ruin?\""
        ),
        "system_prompt": (
            "Roleplay as Noah Douglas-Bloodmoon in the Svart\u00falfr | Modern Fantasy universe. "
            "Noah is the 25-year-old Founding Bloodline Delta werewolf, president of the KSA "
            "fraternity, and the Velvet Glove of House Douglas. He hides panic attacks and deep "
            "vulnerability behind flawless social charm, expensive gifts, and stress-baking."
        ),
    },
}


def clean_format_text(text):
    if not text:
        return ""
    text = text.replace("\u2014", ", ").replace("\u2013", ", ")
    text = re.sub(r" +", " ", text)
    return text.strip()


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, list) else []
        except Exception:
            return []
    return []


def as_dict(value):
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, dict) else {}
        except Exception:
            return {}
    return {}


def fix_outfits(outfits, first_name):
    """Corregge l'anomalia della fonte: {{user}} usato al posto del personaggio."""
    fixed = []
    for outfit in outfits:
        if not isinstance(outfit, dict):
            fixed.append(outfit)
            continue
        entry = dict(outfit)
        desc = entry.get("description")
        if isinstance(desc, str) and "{{user}}" in desc:
            entry["description"] = desc.replace("{{user}}", first_name)
        fixed.append(entry)
    return fixed


def build_mes_example(speech_examples):
    parts = []
    for ex in speech_examples:
        if not isinstance(ex, dict):
            continue
        resp = ex.get("response") or ex.get("content") or ""
        if not resp:
            continue
        prompt_txt = ex.get("prompt") or ""
        label = ex.get("label") or ""
        body = clean_format_text(resp)
        if prompt_txt:
            parts.append(f"<START>\nContext: {prompt_txt}\n{body}")
        elif label:
            parts.append(f"<START>\n[{label}]\n{body}")
        else:
            parts.append(f"<START>\n{body}")
    return "\n\n".join(parts)


def build_card(web_c, cfg):
    display_name = web_c.get("display_name") or web_c.get("first_name")
    first_name = web_c.get("first_name") or display_name
    long_summary = clean_format_text(web_c.get("long_summary") or "")
    summary = clean_format_text(web_c.get("summary") or "")

    tags = as_list(web_c.get("tags"))
    tags = [t.strip() if isinstance(t, str) else t for t in tags if t]

    outfits = fix_outfits(as_list(web_c.get("outfits")), first_name)
    attitudes = as_list(web_c.get("attitudes"))
    rpg_stats = as_dict(web_c.get("rpg_stats"))
    keys = as_list(web_c.get("keys"))

    final_instructions = clean_format_text(web_c.get("final_instructions") or "")
    if DISCIPLINE not in final_instructions:
        post_history = f"{final_instructions}\n\n{DISCIPLINE}".strip()
    else:
        post_history = final_instructions

    mes_example = build_mes_example(as_list(web_c.get("speech_examples")))

    creator_notes = (
        f"Authoritative Svart\u00falfr character card for {display_name}. "
        f"Synchronized with Wyvern Web World {WORLD_ID}."
    )

    extensions = {
        "outfits": outfits,
        "attitudes": attitudes,
        "rpg_stats": rpg_stats,
        "birthdate": web_c.get("birthdate"),
        "start_timeline_position": web_c.get("start_timeline_position"),
        "keys": keys,
        "depth_prompt": {
            "prompt": f"{display_name}. Adhere strictly to LSE mechanics and format discipline.",
            "depth": 4,
        },
    }

    data_block = {
        "name": display_name,
        "description": long_summary,
        "personality": summary,
        "scenario": clean_format_text(cfg["scenario"]),
        "first_mes": clean_format_text(cfg["first_mes"]),
        "mes_example": mes_example,
        "creator_notes": creator_notes,
        "system_prompt": clean_format_text(cfg["system_prompt"]),
        "post_history_instructions": post_history,
        "alternate_greetings": [],
        "tags": tags,
        "creator": "Lys",
        "character_version": "v2",
        "extensions": {
            "outfits": outfits,
            "attitudes": attitudes,
            "rpg_stats": rpg_stats,
            "birthdate": web_c.get("birthdate"),
            "start_timeline_position": web_c.get("start_timeline_position"),
            "keys": keys,
        },
    }

    card = {
        "spec": "chara_card_v2",
        "spec_version": "2.0",
        "name": display_name,
        "description": long_summary,
        "personality": summary,
        "scenario": clean_format_text(cfg["scenario"]),
        "first_mes": clean_format_text(cfg["first_mes"]),
        "mes_example": mes_example,
        "creator_notes": creator_notes,
        "system_prompt": clean_format_text(cfg["system_prompt"]),
        "post_history_instructions": post_history,
        "alternate_greetings": [],
        "tags": tags,
        "creator": "Lys",
        "character_version": "v2",
        "extensions": extensions,
        "data": data_block,
    }
    return card, display_name


def main():
    with open(SOURCE, encoding="utf-8") as fh:
        export = json.load(fh)
    world_chars = {c.get("id"): c for c in export.get("world_characters", [])}

    os.makedirs(OUT_DIR, exist_ok=True)

    for cid, cfg in CONFIGS.items():
        web_c = world_chars.get(cid)
        if not web_c:
            print(f"WARNING: id {cid} not found in World export, skipping.")
            continue
        card, display_name = build_card(web_c, cfg)
        out_path = os.path.join(OUT_DIR, cfg["file"])
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(card, fh, indent=2, ensure_ascii=False)
        print(
            f"OK {display_name:28} -> {cfg['file']} "
            f"(desc {len(card['description'])}, mes_ex {len(card['mes_example'])}, "
            f"outfits {len(card['extensions']['outfits'])}, tags {len(card['tags'])})"
        )


if __name__ == "__main__":
    main()
