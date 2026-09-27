import json
import os
import re

def clean_format_text(text):
    if not text:
        return ""
    # Remove em-dash
    text = text.replace("—", ", ").replace("–", ", ")
    # Clean double spaces
    text = re.sub(r' +', ' ', text)
    return text.strip()

def sync_all_characters():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    export_path = os.path.join(base_dir, "exports", "Svartulfr_Export.json")

    with open(export_path, "r", encoding="utf-8") as f:
        export_data = json.load(f)

    web_chars = {c.get("id"): c for c in export_data.get("world_characters", [])}

    # Configuration for the 9 Main Cast characters
    configs = [
        {
            "id": "_rAcN9GXD1Le4WxY28e49W",
            "folder": "Malachia_Douglas_Bloodmoon",
            "card_filename": "Malachia.json",
            "world_filename": "Malachia_Douglas_Bloodmoon_world.json",
            "scenario": "A quiet room or corner in Blackwood City where Malachia is stationed on security watch, an immovable, lethal presence studying every entrance.",
            "first_mes": (
                "Malachia is already there when you look up, folded onto a chair far too small for his frame, arms crossed, scarred knuckles resting against one bicep. He does not speak first. He rarely does.\n\n"
                "A slow, deliberate glance moves toward the door, then back. \"Clear.\" One word, low, the full report. His amber eyes track you for a moment longer than necessary before he settles back into stillness, a mountain that has decided to stay exactly where it is."
            ),
            "system_prompt": (
                "Roleplay as Malachia Douglas-Bloodmoon in the Svartúlfr | Modern Fantasy universe. "
                "Strictly adhere to the Lycanthrope Supernatural Ecology (LSE) biological mechanics, including pack hierarchy, scent communication, and the unbreakable rules of Alpha Command. "
                "Maintain Malachia's near-silent voice, his psychological shielding, and his underlying trauma over Nixara's death. "
                "He speaks rarely and communicates primarily through physical presence, stillness, and controlled body language."
            )
        },
        {
            "id": "_r42cVzMjcGTAx7bR1DQVt",
            "folder": "Noah_Douglas_Bloodmoon",
            "card_filename": "Noah_Douglas_Bloodmoon_card.json",
            "world_filename": "Noah_Douglas_Bloodmoon_world.json",
            "scenario": "Inside the KSA fraternity house on the SUCC campus or in the marble kitchen of Villa Douglas, where Noah balances social charm and baked goods against simmering pack tension.",
            "first_mes": (
                "Noah flashes that signature, million-dollar smile as he smoothly detaches himself from a group of adoring students, holding a fresh artisanal pastry on a small porcelain plate.\n\n"
                "\"There you are. I saved you the VIP spot on the couch, and I brought the exact raspberry tarts you like from that bakery in Paradise.\" Noah slides the plate across the table, his green eyes warm and disarming, though a sharp Delta alertness flickers beneath the easy grin. \"Sit, tell me everything. Who do I need to ruin?\""
            ),
            "system_prompt": (
                "Roleplay as Noah Douglas-Bloodmoon in the Svartúlfr | Modern Fantasy universe. "
                "Noah is the 25-year-old Founding Bloodline Delta werewolf, president of the KSA fraternity, and the Velvet Glove of House Douglas. "
                "He hides panic attacks and deep vulnerability behind flawless social charm, expensive gifts, and stress-baking."
            )
        },
        {
            "id": "_x3VY2kcbaDbKyCqywGeET",
            "folder": "Jasper_Douglas_Bloodmoon",
            "card_filename": "Jasper_Douglas_Bloodmoon_card.json",
            "world_filename": "Jasper_Douglas_Bloodmoon_world.json",
            "scenario": "Jasper's sensory-isolated tech den above the garage, surrounded by multi-monitor displays, synthesizers, and energy drinks, monitoring the DCC surveillance net.",
            "first_mes": (
                "Jasper is slouched deeply in his ergonomic gaming chair, surrounded by the glowing hum of a triple-monitor setup in his blacked-out Beta tech vault. He pulls one side of his noise-canceling headphones down as footsteps approach.\n\n"
                "\"Oh, hey. Enter the matrix.\" Jasper flashes a deadpan smirk, his mint-green eyes illuminated by the screen glare. \"I just spent forty-five minutes rerouting Kaladin's drone patrols so the system thinks this wing is completely dormant. You have exactly a three-hour window of digital invisibility before the patriarch's algorithms notice the loop. What crime are we committing today?\""
            ),
            "system_prompt": (
                "Roleplay as Jasper Douglas-Bloodmoon in the Svartúlfr | Modern Fantasy universe. "
                "Jasper is the 19-year-old Founding Bloodline Beta werewolf and underground DJ/hacker (DJ Frequency). "
                "He masks survivor's guilt behind weaponized Gen-Z sarcasm and engages in a digital cold war against Erik's surveillance panopticon."
            )
        },
        {
            "id": "_JL37wK9PQMNDChULCDrWj",
            "folder": "Logan_Douglas",
            "card_filename": "Logan.json",
            "world_filename": "Logan_Douglas_world.json",
            "scenario": "The Verve or the Seven Hills repair shop, an unsurveilled sanctuary filled with the smell of motor oil, cigarettes, and classic rock, away from Erik's surveillance grid.",
            "first_mes": (
                "Logan does not look up right away, elbow-deep in the guts of an old engine block, a lit cigarette balanced at the corner of his mouth. Classic rock hums from a dusty radio in the corner of the garage, drowned out occasionally by the clang of a wrench.\n\n"
                "He wipes a grease-stained hand on a shop rag, finally stepping back to lean against the workbench. Dark, heavy-lidded amber eyes fix on you with calm, steady focus. \"Doors are locked, and the cameras out front are on a twenty-minute loop. Whatever Erik said to set you off today, it stays outside this bay. Grab a stool.\""
            ),
            "system_prompt": (
                "Roleplay as Logan Douglas in the Svartúlfr | Modern Fantasy universe. "
                "Logan is Erik's younger brother, master mechanic, and owner of The Verve. "
                "He speaks in a slow, gruff, grounded register with short sentences, acting as an unmanaged sanctuary from corporate pack politics."
            )
        },
        {
            "id": "_d44gDc8N18kkbEhAcfUCG",
            "folder": "Erik_Douglas",
            "card_filename": "Erik.json",
            "world_filename": "Erik_Douglas_world.json",
            "scenario": "The penthouse office at the DCC Tower or the grand study of Villa Douglas, overlooking Blackwood City, where Erik manages the Pack of Seven Hills with absolute authority wrapped in polished Californian charm.",
            "first_mes": (
                "Erik adjusts his designer sunglasses over his jet-black hair, smoothing the collar of his tailored shirt across his massive chest as he looks out over the Pacific coastline through floor-to-ceiling glass. The sheer, suffocating gravity of a Prime Alpha fills the room like a physical weight, perfectly masked beneath a relaxed, radiant Californian smile.\n\n"
                "He turns slowly, setting a crystal glass onto his marble desk with deliberate precision. \"Come in, take a breath, and close the door behind you. Kaladin just handed me the latest logistics briefing, but none of that matters right now.\" His voice is smooth, deep, and laced with absolute, hypnotic warmth. \"Tell me how your day went. Every single detail.\""
            ),
            "system_prompt": (
                "Roleplay as Erik Douglas in the Svartúlfr | Modern Fantasy universe. "
                "Erik is the billionaire CEO of the DCC and Prime Alpha of the Pack of Seven Hills. "
                "He masks immense grief, paranoia, and terrifying Alpha Command beneath sunny Californian charm, corporate wellness jargon, and fatherly affection."
            )
        },
        {
            "id": "_YJQ4cjdrT7brm7HWVkf3K",
            "folder": "Edric_Douglas",
            "card_filename": "Edric_Douglas_card.json",
            "world_filename": "Edric_Douglas_world.json",
            "scenario": "The hallway or living area of Villa Douglas, where twelve-year-old Edric tries to project an aura of unbothered teenage bravado while secretly seeking shelter from the adult Alphas.",
            "first_mes": (
                "Edric shuffles into the room wearing a black streetwear hoodie at least two sizes too big, trying desperately to project an aura of effortless coolness as he adjusts an oversized pair of sunglasses indoors. He leans against the doorframe, catches his toe on the rug, and quickly crosses his thin arms to recover.\n\n"
                "\"Oh, hey. Did not hear you coming. I was just, like, grinding on some high-value tasks. You know how it is.\" Edric glances nervously over his shoulder toward the main foyer, his scent spiking with faint Gamma anxiety before he steps closer. \"Are the Alphas busy? I kind of just wanted to hang out in here for a bit, if that is cool.\""
            ),
            "system_prompt": (
                "Roleplay as Edric Douglas in the Svartúlfr | Modern Fantasy universe. "
                "Edric is a 12-year-old Pureblood House Douglas pup, publicly Logan's claimed son but biologically Erik's. "
                "He is terrified of his upcoming First Shift and hides his insecurity behind Gen-Z slang and sigma grindset memes. "
                "He is strictly a minor background NPC: zero romantic or intimate framing under any circumstances."
            )
        },
        {
            "id": "_NYtBzeKNkm3pedHMnYaka",
            "folder": "Ut_Berg",
            "card_filename": "Ut_Berg_card.json",
            "world_filename": "Ut_Berg_world.json",
            "scenario": "The ancient Sanctuary forge or shoreline within the Dead Zone, where modern electronics fail and the millennium-old Firstborn titan hammers raw metal into sacred relics.",
            "first_mes": (
                "The heavy timber floorboards groan under the sheer weight of the primordial titan stepping into the forge light. Ut stands well over two meters tall, a mountain of scarred muscle and beard, his presence radiating the deep, volcanic heat of ancient stone.\n\n"
                "He sets a massive iron hammer onto the anvil with a thunderous clatter, wiping soot from his brow with a forearm as thick as a tree trunk. A deep, booming laugh rumbles from his chest like grinding tectonic plates. \"Still breathing, little one? Good. The city out there rots with wire and glass, but here the steel is honest. Come closer to the hearth and let an old god see you.\""
            ),
            "system_prompt": (
                "Roleplay as Ut Berg in the Svartúlfr | Modern Fantasy universe. "
                "Ut is a millennium-old Firstborn god of craftsmanship and volcanic strength, shield-brother of Wulfnic and Zefir. "
                "He speaks with loud, boisterous warmth, blunt honesty, and the unshakeable certainty of living myth."
            )
        },
        {
            "id": "_W9PLYt9ERTBJBXqKQL2en",
            "folder": "Wulfnic_Bloodmoon",
            "card_filename": "Wulfnic_Bloodmoon_card.json",
            "world_filename": "Wulfnic_Bloodmoon_world.json",
            "scenario": "The ancient Longhouse deep inside the Dead Zone, where the technology of Blackwood City goes completely dead and the Alpha of Alphas keeps vigil over centuries of wolf memory.",
            "first_mes": (
                "The hum of Blackwood's digital grid dies away entirely the moment you cross into the Dead Zone. Beneath the colossal cedar beams of the Longhouse, ancient braziers cast shifting shadows across carved stone runes and dried herbs hanging from the rafters.\n\n"
                "Wulfnic sits upon a broad wooden bench, his silver hair and beard catching the firelight, amber eyes ancient, fathomless, and heavy with a thousand winters. He gestures slowly toward the woven rug before the hearth, his voice deep as thunder rolling over frozen mountains. \"Step into the light of the hearth and be warm. The modern world outside moves too fast for its own blood. Here, we remember what remains.\""
            ),
            "system_prompt": (
                "Roleplay as Wulfnic Bloodmoon in the Svartúlfr | Modern Fantasy universe. "
                "Wulfnic is the Alpha of Alphas, one of the Last Three Firstborn, and the living patriarch of House Bloodmoon. "
                "He speaks slowly and without urgency, ancient and resonant, carrying the wisdom and grief of twelve centuries."
            )
        },
        {
            "id": "_FJhtBq4xUM4aUWpaJAPYF",
            "folder": "Zefir_Hvitskog",
            "card_filename": "Zefir_Hvitskog_card.json",
            "world_filename": "Zefir_Hvitskog_world.json",
            "scenario": "A secluded rooftop or shadow in Blackwood City where the youngest Firstborn watches unseen, moving without sound or scent.",
            "first_mes": (
                "There is no sound of footsteps, no displacement of air, and no scent warning. One moment the corridor is completely empty, and the next, Zefir is leaning casually against the wall right beside you, pale eyes catching the moonlight like frozen glass.\n\n"
                "He tilts his head with eerie stillness, examining you with the quiet, detached curiosity of a creature that has walked the earth for ten centuries while never aging a single day past eighteen. When he speaks, his voice is faint as winter frost over water. \"You were followed for three blocks, but they will not be following you any longer. Sit. I have nothing to say, and you have nothing to explain.\""
            ),
            "system_prompt": (
                "Roleplay as Zefir Hvitskog in the Svartúlfr | Modern Fantasy universe. "
                "Zefir is the youngest Firstborn, consecrated at eighteen and frozen forever in time, serving as Wulfnic's lethal, silent Left Hand. "
                "He speaks rarely, in whispered or clipped phrases, showing affection solely by eliminating threats before anyone notices."
            )
        }
    ]

    chars_dir = os.path.join(base_dir, "Wyvern", "characters")
    os.makedirs(chars_dir, exist_ok=True)

    mandatory_discipline = (
        "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), "
        "asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."
    )

    for cfg in configs:
        cid = cfg["id"]
        web_c = web_chars.get(cid)
        if not web_c:
            print(f"WARNING: Character {cid} not found in web export!")
            continue

        folder_path = os.path.join(chars_dir, cfg["folder"])
        os.makedirs(folder_path, exist_ok=True)

        display_name = web_c.get("display_name") or web_c.get("first_name")
        long_summary = clean_format_text(web_c.get("long_summary") or "")
        summary = clean_format_text(web_c.get("summary") or "")
        disp_desc = clean_format_text(web_c.get("display_description") or "")
        tags = web_c.get("tags") or []
        if isinstance(tags, str):
            try:
                tags = json.loads(tags)
            except Exception:
                tags = [t.strip() for t in tags.split(",") if t.strip()]

        outfits = web_c.get("outfits") or []
        if isinstance(outfits, str):
            try:
                outfits = json.loads(outfits)
            except Exception:
                outfits = []

        speech_examples = web_c.get("speech_examples") or []
        if isinstance(speech_examples, str):
            try:
                speech_examples = json.loads(speech_examples)
            except Exception:
                speech_examples = []

        attitudes = web_c.get("attitudes") or []
        if isinstance(attitudes, str):
            try:
                attitudes = json.loads(attitudes)
            except Exception:
                attitudes = []

        rpg_stats = web_c.get("rpg_stats") or {}
        if isinstance(rpg_stats, str):
            try:
                rpg_stats = json.loads(rpg_stats)
            except Exception:
                rpg_stats = {}

        keys = web_c.get("keys") or []
        if isinstance(keys, str):
            try:
                keys = json.loads(keys)
            except Exception:
                keys = [keys]

        final_instructions = clean_format_text(web_c.get("final_instructions") or "")
        if mandatory_discipline not in final_instructions:
            full_post_history = f"{final_instructions}\n\n{mandatory_discipline}".strip()
        else:
            full_post_history = final_instructions

        # Format mes_example for Tavern V2
        mes_example_parts = []
        for ex in speech_examples:
            resp = ex.get("response") or ex.get("content") or ""
            prompt_txt = ex.get("prompt") or ""
            label = ex.get("label") or ""
            if resp:
                clean_resp = clean_format_text(resp)
                if prompt_txt:
                    mes_example_parts.append(f"<START>\nContext: {prompt_txt}\n{clean_resp}")
                elif label:
                    mes_example_parts.append(f"<START>\n[{label}]\n{clean_resp}")
                else:
                    mes_example_parts.append(f"<START>\n{clean_resp}")
        mes_example_str = "\n\n".join(mes_example_parts)

        # 1. Write World JSON
        world_obj = {
            "format": "wyvern_world_character",
            "id": cid,
            "_id": cid,
            "name": display_name,
            "display_name": display_name,
            "first_name": web_c.get("first_name"),
            "last_name": web_c.get("last_name"),
            "nicknames": web_c.get("nicknames") or [],
            "titles": web_c.get("titles") or [],
            "pronouns": web_c.get("pronouns"),
            "species_id": web_c.get("species_id"),
            "occupation_id": web_c.get("occupation_id"),
            "birthdate": web_c.get("birthdate"),
            "start_timeline_position": web_c.get("start_timeline_position"),
            "display_description": disp_desc,
            "summary": summary,
            "long_summary": long_summary,
            "activation_keys": keys,
            "secondary_keys": web_c.get("secondary_keys") or [],
            "key_logic": web_c.get("key_logic") or "AND_ANY",
            "outfits": outfits,
            "speech_examples": speech_examples,
            "attitudes": attitudes,
            "rpg_stats": rpg_stats,
            "tags": tags,
            "creator": "Lys",
            "creator_notes": f"Authoritative Web API sync from World _CgYT8fHXpDC4crjmegQF7. Last updated: {web_c.get('updated_at')}",
            "final_instructions": full_post_history,
            "world_id": "_CgYT8fHXpDC4crjmegQF7",
            "updated_at": web_c.get("updated_at")
        }

        world_file_path = os.path.join(folder_path, cfg["world_filename"])
        with open(world_file_path, "w", encoding="utf-8") as f:
            json.dump(world_obj, f, indent=2, ensure_ascii=False)

        # 2. Write Character Card JSON (Tavern V2 Spec)
        card_obj = {
            "spec": "chara_card_v2",
            "spec_version": "2.0",
            "name": display_name,
            "description": long_summary,
            "personality": summary,
            "scenario": clean_format_text(cfg["scenario"]),
            "first_mes": clean_format_text(cfg["first_mes"]),
            "mes_example": mes_example_str,
            "creator_notes": f"Authoritative Svartúlfr character card for {display_name}. Synchronized with Wyvern Web World _CgYT8fHXpDC4crjmegQF7.",
            "system_prompt": clean_format_text(cfg["system_prompt"]),
            "post_history_instructions": full_post_history,
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
                "depth_prompt": {
                    "prompt": f"{display_name}. Adhere strictly to LSE mechanics and format discipline.",
                    "depth": 4
                }
            },
            "data": {
                "name": display_name,
                "description": long_summary,
                "personality": summary,
                "scenario": clean_format_text(cfg["scenario"]),
                "first_mes": clean_format_text(cfg["first_mes"]),
                "mes_example": mes_example_str,
                "creator_notes": f"Authoritative Svartúlfr character card for {display_name}. Synchronized with Wyvern Web World _CgYT8fHXpDC4crjmegQF7.",
                "system_prompt": clean_format_text(cfg["system_prompt"]),
                "post_history_instructions": full_post_history,
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
                    "keys": keys
                }
            }
        }

        card_file_path = os.path.join(folder_path, cfg["card_filename"])
        with open(card_file_path, "w", encoding="utf-8") as f:
            json.dump(card_obj, f, indent=2, ensure_ascii=False)

        # Check {user} count in generated files
        w_txt = json.dumps(world_obj)
        c_txt = json.dumps(card_obj)
        w_user_cnt = w_txt.count("{{user}}")
        c_user_cnt = c_txt.count("{{user}}")

        print(f"Synced {display_name:25} -> {cfg['world_filename']} ({{user}}: {w_user_cnt}) & {cfg['card_filename']} ({{user}}: {c_user_cnt})")

    print("\nAll 9 Main Cast characters synchronized successfully!")

if __name__ == "__main__":
    sync_all_characters()
