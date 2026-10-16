# -*- coding: utf-8 -*-
import json
import os
import re
from compute_final_rpg_stats import CHARACTERS_RPG, build_rpg_block

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FINAL_DIR = os.path.join(ROOT, "FINAL")

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

# Full redundant [INSTRUCTIONS: Format discipline...] block
FULL_INSTR_RE = re.compile(
    r"\s*\[INSTRUCTIONS:\s*Format discipline:\s*dialogue in quotes,\s*actions and narration in plain text(?:\s*\(no asterisks\))?,\s*asterisks reserved for internal thoughts only\.\s*Never use the em dash[;,]\s*use commas or periods instead\.(?:\s*Focus on character-specific tone\.)?\]",
    re.IGNORECASE,
)

# Inline Format discipline sentence inside a character-specific [INSTRUCTIONS: ...] block
INLINE_FORMAT_RE = re.compile(
    r"\s*Format discipline:\s*dialogue in quotes,\s*actions and narration in plain text(?:\s*\(no asterisks\))?,\s*asterisks reserved for internal thoughts only\.\s*Never use the em dash[;,]\s*use commas or periods instead\.",
    re.IGNORECASE,
)

# Source: LSE_*.md / Fonte: LSE_*.md lines
MD_SOURCE_RE = re.compile(
    r"\n*(?:Source|Fonte):\s*LSE_[A-Za-z0-9_]+\.md[^\n]*",
    re.IGNORECASE,
)

def fix_merged_character_sheets(name, content):
    fixed = False
    # 1. Alicia Virtuoso
    if name == "Alicia Virtuoso" and "WARDROBE & NOTABLE OUTFITS:\n- Faculty Daily:" in content:
        content = content.split("WARDROBE & NOTABLE OUTFITS:\n- Faculty Daily:")[0].strip()
        fixed = True

    # 2. Daniel "Danny" Boone
    elif name == 'Daniel "Danny" Boone' and "FAMILY & PACK: Descended from rural frontier wolf stock." in content:
        parts = content.split("FAMILY & PACK: Descended from rural frontier wolf stock.")
        if "[INSTRUCTIONS:" in parts[1]:
            instr_part = "[INSTRUCTIONS:" + parts[1].split("[INSTRUCTIONS:", 1)[1]
            content = parts[0].strip() + "\n\n" + instr_part.strip()
        else:
            content = parts[0].strip()
        fixed = True

    # 3. Dean
    elif name == "Dean" and "FAMILY & PACK: Independent campus presence. Dean values brotherhood and sports camaraderie" in content:
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

    # 4. Vito Marino
    elif name == "Vito Marino" and "FAMILY & PACK: Veteran enforcer tied to old-school Los Angeles" in content:
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

    # 5. Zero
    elif name == "Zero" and "FAMILY & PACK: Raised in the brutal underground fight pits of Los Angeles" in content:
        content = content.replace(
            "FAMILY & PACK: Raised in the brutal underground fight pits of Los Angeles, Zero carries no pack and knows no family. His only allegiance is to the Sinners organization, serving as their feared hitman and enforcer. He views other people with profound distrust, treating survival as a perpetual war.\n\n",
            ""
        )
        fixed = True

    return content, fixed

def inject_rpg_block_into_entry(content, rpg_block):
    if "RPG STATS & TRAITS:" in content:
        parts = content.split("RPG STATS & TRAITS:")
        after = ""
        if "SYSTEM & ENGINE KEYS:" in parts[1]:
            after = "\n\nSYSTEM & ENGINE KEYS:" + parts[1].split("SYSTEM & ENGINE KEYS:", 1)[1]
        elif "[INSTRUCTIONS:" in parts[1]:
            after = "\n\n[INSTRUCTIONS:" + parts[1].split("[INSTRUCTIONS:", 1)[1]
        content = parts[0].strip() + "\n\n" + rpg_block + after
    elif "SYSTEM & ENGINE KEYS:" in content:
        parts = content.split("SYSTEM & ENGINE KEYS:", 1)
        content = parts[0].strip() + "\n\n" + rpg_block + "\n\nSYSTEM & ENGINE KEYS:" + parts[1]
    elif "[INSTRUCTIONS:" in content:
        parts = content.split("[INSTRUCTIONS:", 1)
        content = parts[0].strip() + "\n\n" + rpg_block + "\n\n[INSTRUCTIONS:" + parts[1]
    else:
        content = content.strip() + "\n\n" + rpg_block
    return content

def remediate_final_lorebooks():
    rpg_lookup = {}
    for c in CHARACTERS_RPG:
        block, final = build_rpg_block(c)
        rpg_lookup[c["lbSearch"]] = (c, block)

    files = [
        "Svartulfr_Lorebook_I.json",
        "Svartulfr_Lorebook_II.json",
        "Svartulfr_Lorebook_III.json",
        "Svartulfr_Location.json",
        "Svartulfr_NPC_Primary.json",
        "Svartulfr_NPC_Secondary.json",
    ]

    for fn in files:
        fpath = os.path.join(FINAL_DIR, fn)
        data = json.load(open(fpath, encoding="utf-8"))
        entries = data.get("entries", [])
        stats = {
            "intruders_disabled": 0,
            "duplicates_disabled": 0,
            "merged_fixed": 0,
            "keys_cleaned": 0,
            "instr_stripped": 0,
            "md_stripped": 0,
            "rpg_updated": 0,
            "em_dash_fixed": 0,
        }

        for idx, e in enumerate(entries):
            name = (e.get("name") or "").strip()
            content = e.get("content") or ""
            keys = e.get("keys") or []

            # 1. Disable Sugar Moon duplicate (entry_id 4z4U5a_XG3gbd0zLzCw9m or index 56 in Lorebook I)
            if fn == "Svartulfr_Lorebook_I.json" and (e.get("entry_id") == "4z4U5a_XG3gbd0zLzCw9m" or (name.startswith("Sugar Moon:") and idx > 20)):
                if e.get("enabled") is not False:
                    e["enabled"] = False
                    stats["duplicates_disabled"] += 1

            # 2. Disable Digitalis / Cuttings / Jun intruders
            if any(m in content for m in DIGITALIS_MARKERS):
                if e.get("enabled") is not False:
                    e["enabled"] = False
                    stats["intruders_disabled"] += 1

            # 3. Fix merged character sheets
            content, was_fixed = fix_merged_character_sheets(name, content)
            if was_fixed:
                stats["merged_fixed"] += 1

            # 4. Clean umbrella keywords on character sheets
            is_char_sheet = (
                content.startswith("[NAME:")
                or content.startswith("[ENTITY:")
                or "NPC_Primary" in fn
                or "NPC_Secondary" in fn
            )
            if is_char_sheet and name != "Modern Fantasy: Contatti Esterni dell'Underworld" and len(keys) > 1:
                new_keys = [k for k in keys if k.lower().strip() not in BROAD_KEYS]
                if new_keys and len(new_keys) != len(keys):
                    e["keys"] = new_keys
                    stats["keys_cleaned"] += 1

            # 5. Strip redundant Format discipline
            new_content, c1 = FULL_INSTR_RE.subn("", content)
            new_content, c2 = INLINE_FORMAT_RE.subn("", new_content)
            # Clean empty [INSTRUCTIONS: ] if left over
            new_content = re.sub(r"\s*\[INSTRUCTIONS:\s*\]", "", new_content)
            if c1 + c2 > 0:
                content = new_content.strip()
                stats["instr_stripped"] += 1

            # 6. Strip Source: LSE_*.md / Fonte: LSE_*.md
            new_content, c3 = MD_SOURCE_RE.subn("", content)
            if c3 > 0:
                content = new_content.strip()
                stats["md_stripped"] += 1

            # 7. Update RPG STATS & TRAITS with Final Stats on NPC_Primary and Edric in NPC_Secondary
            if fn in ("Svartulfr_NPC_Primary.json", "Svartulfr_NPC_Secondary.json"):
                for search_str, (c_def, rpg_block) in rpg_lookup.items():
                    if search_str == "Edric Douglas" and name == "Edric Douglas":
                        content = inject_rpg_block_into_entry(content, rpg_block)
                        stats["rpg_updated"] += 1
                        break
                    elif search_str != "Edric Douglas" and fn == "Svartulfr_NPC_Primary.json":
                        # Avoid matching "Ut" inside other names
                        if search_str == "Ut":
                            if name.startswith("Ut "):
                                content = inject_rpg_block_into_entry(content, rpg_block)
                                stats["rpg_updated"] += 1
                                break
                        elif search_str in name:
                            content = inject_rpg_block_into_entry(content, rpg_block)
                            stats["rpg_updated"] += 1
                            break

            # 8. Em-dash purge
            if "—" in content:
                content = content.replace(" — ", ", ").replace("—", ", ")
                stats["em_dash_fixed"] += 1

            e["content"] = content

        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"[OK] {fn:28} -> {stats}")

if __name__ == "__main__":
    remediate_final_lorebooks()
