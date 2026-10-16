#!/usr/bin/env python3
"""
optimize_lorebooks.py — Pulizia non-distruttiva dei 5 Lorebook Svartúlfr esportati da WyvernChat.

Operazioni eseguite (allineate a 'Suite di Ottimizzazione WyvernChat & Script di Pulizia Lorebook.md'):
  1. Disabilita le 110 schede placeholder / vuote e il duplicato Sugar Moon (uid 58 in Lorebook I).
  2. Disabilita tutte le voci intruse del setting Digitalis / Cuttings / Jun (19 voci totali).
  3. Ripara chirurgicamente le 5 schede con merge accidentali (Alicia Virtuoso, Danny Boone, Dean, Vito Marino, Zero).
  4. Rimuove le keyword "ombrello" dalle schede dei singoli NPC (inclusi [NAME:, [ENTITY:, NPC-Primary e Lorebook-III).
  5. Rimuove il testo [INSTRUCTIONS: ... Format discipline...] ridondante e i leak a file .md locali.
  6. Corregge selective=True quando keysecondary è vuoto (impostando selective=False).
  7. Imposta priority di sicurezza a 10 se è a 0 nelle estensioni Wyvern.
"""

import json
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_DIR = BASE_DIR / "lorebooks" / "source"
OUTPUT_DIR = BASE_DIR / "lorebooks" / "optimized"

FILES = [
    "[WyvernChat] Svartlfr---Lorebook-I-lorebook-export.json",
    "[WyvernChat] Svartlfr---Lorebook-II-lorebook-export.json",
    "[WyvernChat] Svartlfr---Lorebook-III-lorebook-export.json",
    "[WyvernChat] Svartlfr---Location--lorebook-export.json",
    "[WyvernChat] Svartlfr---NPC-Primary-lorebook-export.json",
]

BROAD_KEYS = {
    "solarton", "succ", "blackwood", "losangeles", "underworld",
    "vampire", "werewolf", "human", "demihuman", "demon",
    "college", "student", "alpha", "beta", "omega", "pack"
}

DIGITALIS_MARKERS = [
    "Cutting 01",
    "Cutting 02",
    "Cutting 03",
    "Tendril (HM-7)",
    "The Hothouse:",
    "Seedpod (the Closet):",
    "Narcissus (the Mirror Room):",
    "Taproot (the Confession Room):",
    "Digitalis: Cold War missile silo",
    "The Ovary: the Host's bedroom",
    "Nectary (the Rain Room):",
    "Graft (the Cuff Room):",
    "Cuttings and {{user}} the Host",
    "Jun's beloved Shiba Inu",
    "younger half sister of Jun",
    "Jun traits(Tendril keyed his body",
    "Hemlock Biosciences: Delaware biotech",
    "drone Rene named Gnat",
    "Jun dies if he orgasms within three metres",
    "Rene/Keisuke's red triggers",
    "industrial walk in freezer at minus 10 degrees",
    "Industrial walk in freezer at minus 10 degrees",
    "strictly between Jun and {{user}}",
    "the only unmedicated person in Digitalis",
    "forty anonymous paying viewers",
]

FULL_INSTR_RE = re.compile(
    r"\s*\[INSTRUCTIONS:\s*Format discipline:\s*dialogue in quotes,\s*actions and narration in plain text(?:\s*\(no asterisks\))?,\s*asterisks reserved for internal thoughts only\.\s*Never use the em dash[;,]\s*use commas or periods instead\.(?:\s*Focus on character-specific tone\.)?\]",
    re.IGNORECASE,
)

INLINE_FORMAT_RE = re.compile(
    r"\s*Format discipline:\s*dialogue in quotes,\s*actions and narration in plain text(?:\s*\(no asterisks\))?,\s*asterisks reserved for internal thoughts only\.\s*Never use the em dash[;,]\s*use commas or periods instead\.",
    re.IGNORECASE,
)

MD_SOURCE_RE = re.compile(
    r"\n*(?:Source|Fonte):\s*LSE_[A-Za-z0-9_]+\.md[^\n]*",
    re.IGNORECASE,
)


def fix_merged_character_sheets(filename: str, uid: str, comment: str, content: str):
    """Ripara chirurgicamente le 5 schede che presentavano testi fusi da altri personaggi."""
    fixed = False

    if comment == "Alicia Virtuoso" and "WARDROBE & NOTABLE OUTFITS:\n- Faculty Daily:" in content:
        content = content.split("WARDROBE & NOTABLE OUTFITS:\n- Faculty Daily:")[0].strip()
        fixed = True

    elif comment == 'Daniel "Danny" Boone' and "FAMILY & PACK: Descended from rural frontier wolf stock." in content:
        parts = content.split("FAMILY & PACK: Descended from rural frontier wolf stock.")
        if "[INSTRUCTIONS:" in parts[1]:
            instr_part = "[INSTRUCTIONS:" + parts[1].split("[INSTRUCTIONS:", 1)[1]
            content = parts[0].strip() + "\n\n" + instr_part.strip()
        else:
            content = parts[0].strip()
        fixed = True

    elif comment == "Dean" and "FAMILY & PACK: Independent campus presence. Dean values brotherhood and sports camaraderie" in content:
        content = content.replace(
            "FAMILY & PACK: Independent campus presence. Dean values brotherhood and sports camaraderie above blood ties, keeping his frat brothers and gym partners close as his chosen family in Solarton.\n\n",
            ""
        )
        athlete_block_start = "THE WEIGHT HE CARRIES: Dean carries the heavy pressure of athletic perfection"
        instr_marker = "[INSTRUCTIONS: Dean talks like he's already mid-thought"
        if athlete_block_start in content and instr_marker in content:
            before = content.split(athlete_block_start)[0]
            after = instr_marker + content.split(instr_marker, 1)[1]
            content = before.strip() + "\n\n" + after.strip()
        fixed = True

    elif comment == "Vito Marino" and "FAMILY & PACK: Veteran enforcer tied to old-school Los Angeles" in content:
        old_vito_tail = content.split("FAMILY & PACK: Veteran enforcer tied to old-school Los Angeles")[0].strip()
        new_vito_tail = (
            "FAMILY & PACK: Absolute boss of the Ironworks Syndicate and Pack Leader of Blackwood City's industrial district. "
            "Vito treats his foundry crews and loyal enforcers as his ironclad pack, demanding tribute and obedience while keeping "
            "Ironworks autonomous under the nose of the DCC.\n\n"
            "VOICE & BEHAVIOR: Deep, gravelly baritone with an old-world Italian rasp. Vito moves with the heavy, unhurried precision "
            "of a century-old Pureblood Alpha who built his industrial empire with his own scarred hands.\n\n"
            "THE WEIGHT HE CARRIES: Vito has held Ironworks for over a century, balancing brutal street dominance with the cold necessity "
            "of bowing only when outmatched by apex forces like Erik Douglas. He guards his territory relentlessly, knowing that any sign "
            "of softness would invite corporate annexation."
        )
        content = old_vito_tail + "\n\n" + new_vito_tail
        fixed = True

    elif comment == "Zero" and "FAMILY & PACK: Raised in the brutal underground fight pits of Los Angeles" in content:
        content = content.replace(
            "FAMILY & PACK: Raised in the brutal underground fight pits of Los Angeles, Zero carries no pack and knows no family. His only allegiance is to the Sinners organization, serving as their feared hitman and enforcer. He views other people with profound distrust, treating survival as a perpetual war.\n\n",
            ""
        )
        fixed = True

    return content, fixed


def process_file(filepath: Path, out_dir: Path) -> dict:
    filename = filepath.name
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries", {})
    stats = {
        "file": filename,
        "total": len(entries),
        "disabled_placeholders": 0,
        "disabled_intruders": 0,
        "merged_sheets_fixed": 0,
        "keys_cleaned": 0,
        "instr_stripped": 0,
        "md_stripped": 0,
        "selective_fixed": 0,
    }

    for uid, entry in entries.items():
        content = entry.get("content", "")
        comment = entry.get("comment", "")
        keys = entry.get("key", [])

        # 1. Disattiva placeholder, vuote o duplicato uid 58 in Lorebook I
        if (
            "STATUS: placeholder" in content
            or content.strip() == ""
            or (filename.endswith("Lorebook-I-lorebook-export.json") and str(uid) == "58")
        ):
            entry["disable"] = True
            stats["disabled_placeholders"] += 1
            continue

        # 2. Disattiva le voci intruse Digitalis / Cuttings / Jun
        if any(marker in content for marker in DIGITALIS_MARKERS):
            entry["disable"] = True
            stats["disabled_intruders"] += 1
            continue

        # 3. Ripara le 5 schede con merge accidentali
        content, was_fixed = fix_merged_character_sheets(filename, str(uid), comment, content)
        if was_fixed:
            entry["content"] = content
            stats["merged_sheets_fixed"] += 1

        # 4. Rimuove le keyword "ombrello" dalle schede dei singoli personaggi
        is_character_sheet = (
            content.startswith("[NAME:")
            or content.startswith("[ENTITY:")
            or "NPC-Primary" in filename
            or "Lorebook-III" in filename
        )
        if is_character_sheet and comment != "Modern Fantasy: Contatti Esterni dell'Underworld" and len(keys) > 1:
            new_keys = [k for k in keys if k.lower().strip() not in BROAD_KEYS]
            if new_keys and len(new_keys) != len(keys):
                entry["key"] = new_keys
                stats["keys_cleaned"] += 1

        # 5. Rimuove Format discipline ridondante e riferimenti .md
        new_content, c1 = FULL_INSTR_RE.subn("", entry["content"])
        new_content, c2 = INLINE_FORMAT_RE.subn("", new_content)
        new_content = re.sub(r"\s*\[INSTRUCTIONS:\s*\]", "", new_content)
        if c1 + c2 > 0:
            entry["content"] = new_content.strip()
            stats["instr_stripped"] += 1

        new_content, c3 = MD_SOURCE_RE.subn("", entry["content"])
        if c3 > 0:
            entry["content"] = new_content.strip()
            stats["md_stripped"] += 1

        # 6. Fix per selective=True quando keysecondary è vuoto
        if entry.get("selective") is True and not entry.get("keysecondary"):
            entry["selective"] = False
            stats["selective_fixed"] += 1

        # 7. Priority di sicurezza su Wyvern
        if "extensions" in entry and "wyvern" in entry["extensions"]:
            if entry["extensions"]["wyvern"].get("priority", 0) == 0:
                entry["extensions"]["wyvern"]["priority"] = 10

    out_path = out_dir / filename
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return stats


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for fname in FILES:
        fpath = SOURCE_DIR / fname
        if fpath.exists():
            s = process_file(fpath, OUTPUT_DIR)
            print(f"[OK] {fname}: {s}")


if __name__ == "__main__":
    main()
