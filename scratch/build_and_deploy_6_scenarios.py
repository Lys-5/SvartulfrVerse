"""
build_and_deploy_6_scenarios.py
Builds, validates, and deploys the 6 thematic character scenarios for Svartúlfr Verse.

Thematic Scenarios:
1. Svartulfr_Scenario_Camp_Mystic.json
2. Svartulfr_Scenario_SUCC_Route_Alyssa.json
3. Svartulfr_Scenario_SUCC_Route_Jasper.json
4. Svartulfr_Scenario_Villa_Douglas.json
5. Svartulfr_Scenario_DMHA_Dungeons.json
6. Svartulfr_Scenario_Underworld_Sindacato.json

Invariants strictly enforced:
- visibility: "private" (CRITICAL: NEVER "unlisted")
- Zero em-dashes ('—' or '–') in titles, descriptions, scenario prompt, greetings, or message contents.
- Spoken dialogue in standard double quotes ("..."). Narration and actions in plain text (no asterisks). Asterisks reserved for thoughts (*...*).
- All 6 standalone lorebook IDs attached to each scenario:
  ["_gwwCxCfQ6PQaLEjAQVpJL", "_HfG7TeV6MJyj6bxMwxkpt", "_9zWTGqYJNJ4BCDMj8gfcD", "_EjXxkmPVhpCXg8xABpFkK", "_zwEqgEEzh12X6gHVmMKKC", "_Uht3Ckz44JBDrPnUHq7LV"]
- Every slot: key, label, pool array, unavailable_count: 0. Standalone cards: weight 100. Open/NPC slots: pool: [].
- Multi-message greeting parity: greeting.content == messages[0].content, greeting.speaker_slot == messages[0].speaker_slot.
  Every speaker_slot exists in slots[].key. No redundant speaker name prefixes.
- Verified character data:
  * Russ Sinclair and Scarlett Rose surnames verified.
  * Finnegan Novak explicitly specified as Arctic Wolf demi-human (one pair of animal ears, non-shifter).
  * Jean-Luc Virtuoso explicitly specified as Human Telepath.
  * Villa Douglas contains exactly the 7 canonical male Douglas/Bloodmoon cards.
  * DMHA scenario 9 slots: Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, DMHA strike team / Nomads.
  * Camp Mystic: Lake Erie shuttle arrival, Marcus Vale / Celeste Nadir, Mara Voss, Edric 13yo, Lua startup script.
"""

import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

ROOT = pathlib.Path(r"e:\repository\SvartulfrVerse")
FINAL_SCENARIOS_DIR = ROOT / "FINAL" / "scenarios"
TOKEN_FILE = ROOT / "scratch" / "wyvern_token.txt"
REFRESH_SCRIPT = ROOT / "scratch" / "refresh_token.py"
API_BASE = "https://app.wyvern.chat/api"

# Universal 6 Standalone Lorebook IDs
LOREBOOK_IDS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",  # Svartúlfr - Lorebook I (221 entries)
    "_HfG7TeV6MJyj6bxMwxkpt",  # Svartúlfr - Lorebook II (142 entries)
    "_9zWTGqYJNJ4BCDMj8gfcD",  # Svartúlfr - Lorebook III (36 entries)
    "_EjXxkmPVhpCXg8xABpFkK",  # Svartúlfr - Location (225 entries)
    "_zwEqgEEzh12X6gHVmMKKC",  # Svartúlfr - NPC Primary (99 entries)
    "_Uht3Ckz44JBDrPnUHq7LV",  # Svartúlfr - NPC Secondary (211 entries)
]

# Verified Standalone Card IDs
CARD_JASPER = "_t4J9aQNJM36cUKAP4wB4U"
CARD_ALYSSA = "_6exg3yPfe2eCDK4hTftkh"
CARD_ERIK = "_QPea6g4Q1QfeYCVHCLMPR"
CARD_MALACHIA = "_RDfz7XzTpM23LpPALVXHM"
CARD_NOAH = "_zFLUjV8aVxQRAfQxGcAcY"
CARD_WULFNIC = "_HEQQbbRFwKdG8QE2Fh1z1"
CARD_LOGAN = "_T8Ywcr9FEqNf9JxbK6eHP"
CARD_EDRIC = "_TbRM3EdxDjHFgqztTbCpL"
CARD_JARED = "_xJVPtBLL3dxy69RLKL9X9"
CARD_STANLEY = "_Xd3NhKnRJByMTtdb6PjxJ"
CARD_MACKENZIE = "_zn24784jfcchQ7EwCyAnm"
CARD_SIERRA = "_pnrXbkWqcgmFAf3meRWFY"
CARD_SCARLETT = "_qXgBMbFYJfc84hbLHhe92"
CARD_RUSS = "_wn6DkCcg3Xqa2Xpx9ttnT"

# Standard Avatar URLs
AVATAR_CAMP_MYSTIC = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/a8c12c4f-0ed4-400f-a94d-b13233d70b00/public"
AVATAR_ALYSSA = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public"
AVATAR_JASPER = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public"
AVATAR_VILLA_DOUGLAS = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61648731-7c96-454d-95e5-e27aa69d8c00/public"
AVATAR_DMHA_DUNGEONS = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9d47924c-03d3-4ed2-1564-f3d996a1d000/public"
AVATAR_UNDERWORLD = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

COMMON_NARRATION_GUIDELINES = (
    "\n\n[NARRATION GUIDELINES & ANTI-VENTRILOQUISM:\n"
    "1. Strict Anti-Ventriloquism: Never speak, think, emote, or act for {{user}}. Pause and wait for {{user}}'s input.\n"
    "2. Scene Balancing: Balance active scene characters naturally according to their canonical JED+ voice, attitudes, and pack hierarchies.\n"
    "3. Format Discipline: Dialogue in quotes (\"...\"), actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only (*...*). Never use the em dash; use commas or periods instead.\n"
    "4. Demi-Human & Werewolf Anatomy: Demi-humans and Werewolves in Partial Shift possess ONLY ONE PAIR OF EARS (their animal ears atop their skull, zero human ears).\n"
    "5. NPC Formatting Discipline: When secondary NPCs or background characters speak, format their dialogue on a new line prefixed with their exact full name and a colon (e.g., 'Santiago Herrera: [dialogue]'). Never blend NPC dialogue anonymously into narration.]"
)

def clean_no_em_dash(text: str) -> str:
    """Enforces zero em-dashes and en-dashes across all strings."""
    if not isinstance(text, str):
        return text
    text = text.replace("—", ", ")
    text = text.replace("–", ", ")
    # Clean up double commas or awkward spacing if any
    text = re.sub(r',\s*,', ',', text)
    text = re.sub(r'\s+,', ',', text)
    return text

def sanitize_recursively(obj):
    """Recursively cleans all strings in dictionary/list."""
    if isinstance(obj, str):
        return clean_no_em_dash(obj)
    elif isinstance(obj, list):
        return [sanitize_recursively(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: sanitize_recursively(v) for k, v in obj.items()}
    return obj


# ==============================================================================
# SCENARIO 1: CAMP MYSTIC
# ==============================================================================
def build_scenario_camp_mystic() -> dict:
    slots = [
        {
            "key": "twin",
            "label": "Twin Sibling (Jasper / Alyssa)",
            "pool": [
                {"character_id": CARD_JASPER, "weight": 100},
                {"character_id": CARD_ALYSSA, "weight": 100},
            ],
            "unavailable_count": 0,
        },
        {
            "key": "cousin",
            "label": "Edric Douglas (Age 13)",
            "pool": [
                {"character_id": CARD_EDRIC, "weight": 100},
            ],
            "unavailable_count": 0,
        },
        {
            "key": "supervisor",
            "label": "Residential Life Supervisor",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "director",
            "label": "Camp Director Mara Voss",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "cabin_mate_1",
            "label": "Cabin Mate 1",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "cabin_mate_2",
            "label": "Cabin Mate 2",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "camper_peer_1",
            "label": "Camper Peer 1",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "camper_peer_2",
            "label": "Camper Peer 2",
            "pool": [],
            "unavailable_count": 0,
        },
    ]

    startup_script = (
        "-- Camp Mystic Dynamic Supervisor & Cabin Mate Resolution\n"
        "if memory and memory._scenario and memory._scenario.assignments then\n"
        "    local p_id = (user and user.persona_id) or (memory._scenario.persona_id) or ''\n"
        "    local u_name = string.lower((user and user.name) or '')\n"
        "    local sub = string.lower((user and (user.pronoun_subjective or (user.pronouns and user.pronouns.subjective))) or '')\n"
        "    local obj = string.lower((user and (user.pronoun_objective or (user.pronouns and user.pronouns.objective))) or '')\n"
        "\n"
        "    local is_female = (sub == 'she' or obj == 'her' or string.find(u_name, 'alyssa') or string.find(u_name, 'female') or string.find(u_name, 'femmina'))\n"
        "    local is_male = (sub == 'he' or obj == 'him' or string.find(u_name, 'jasper') or string.find(u_name, 'male') or string.find(u_name, 'maschio'))\n"
        "\n"
        f"    local alyssa_id = '{CARD_ALYSSA}'\n"
        f"    local jasper_id = '{CARD_JASPER}'\n"
        "\n"
        "    if is_female then\n"
        "        memory._scenario.assignments['twin'] = jasper_id\n"
        "        memory._scenario.supervisor_role = 'Celeste Nadir (Moonflower Cabin)'\n"
        "    elseif is_male then\n"
        "        memory._scenario.assignments['twin'] = alyssa_id\n"
        "        memory._scenario.supervisor_role = 'Marcus Vale (Lake Wolf Cabin)'\n"
        "    else\n"
        "        math.randomseed(os.time())\n"
        "        if math.random(1, 2) == 1 then\n"
        "            memory._scenario.assignments['twin'] = alyssa_id\n"
        "            memory._scenario.supervisor_role = 'Marcus Vale (Lake Wolf Cabin)'\n"
        "        else\n"
        "            memory._scenario.assignments['twin'] = jasper_id\n"
        "            memory._scenario.supervisor_role = 'Celeste Nadir (Moonflower Cabin)'\n"
        "        end\n"
        "    end\n"
        "end\n"
    )

    scenario_prompt = (
        "Setting: Camp Mystic, Lake Erie Supernatural Residential Reserve, Ohio shoreline. Summer training session.\n\n"
        "Overview:\n"
        "Camp Mystic is an elite residential sanctuary and supernatural training ground nestled along the dense pine shores of Lake Erie. "
        "Young supernaturals, demi-humans, and scions of powerful dynasties gather here for intensive supernatural control courses, lake recreation, "
        "and woodland rites before stepping into collegiate life or pack responsibilities. "
        "The camp comprises four primary sectors: the Residential District (sixteen cabins divided into Girls Zone overseen by Celeste Nadir and Boys Zone overseen by Marcus Vale), "
        "the Recreation District (Rec Hall, Dining Commons, and Trading Post), the Training District directed by Camp Director Mara Voss and head counselors, "
        "and the Lakeside District with pontoon docks, canoes, and the protective ancient Deep Ward.\n\n"
        "Cast and Roles:\n"
        "- {{user}} and {{scenarioChar \"twin\"}}: Douglas-Bloodmoon twins (Alyssa Hvit or Jasper Svartr), adolescent campers preparing for future collegiate transition.\n"
        "- {{scenarioChar \"cousin\"}} (Edric Douglas): Exactly 13 years old during this camp summer. Younger cousin, son of Logan Douglas, pre-presentation Gamma pup, gamer, witty, and fiercely attached to his cousins.\n"
        "- {{scenarioChar \"supervisor\"}}: Residential Life Head (Marcus Vale for boys in Lake Wolf/Ironwood cabins, or Celeste Nadir for girls in Moonflower/Silver Birch cabins).\n"
        "- {{scenarioChar \"director\"}} (Mara Voss): Camp Director, seasoned werewolf Alpha, imposing and fair guardian of the reserve.\n"
        "- {{scenarioChar \"cabin_mate_1\"}} & {{scenarioChar \"cabin_mate_2\"}}: Cabin peers sharing quarters and chores.\n"
        "- {{scenarioChar \"camper_peer_1\"}} & {{scenarioChar \"camper_peer_2\"}}: Fellow campers participating in lake races, hiking, and campfire lore.\n\n"
        "Invariants:\n"
        "- Edric Douglas is strictly 13 years old in this scenario.\n"
        "- Demi-humans possess only ONE pair of ears (animal ears atop head, zero human ears).\n"
        "- Arrival integrates the yellow camp shuttle traversing the gravel road along Lake Erie.\n"
        + COMMON_NARRATION_GUIDELINES
    )

    greetings = [
        {
            "id": "scene-camp-mystic-shuttle",
            "name": "01. The Shuttle Arrival on Lake Erie",
            "description": "The yellow camp shuttle rumbles along the gravel road, opening up to the blue horizon of Lake Erie as Marcus Vale gives arrival orders.",
            "messages": [
                {
                    "id": "msg-cm-1-1",
                    "speaker_slot": "supervisor",
                    "content": "Marcus Vale stood up before the vehicle had even come to a full stop, steadying himself on the overhead rail with one calloused hand. His amber gaze swept over the rows of campers with practiced calm. \"Bags stay on the racks until the air brakes set. Cabins are posted on the board by the mess hall. Keep your gear together and form up by the flagpoles.\"",
                },
                {
                    "id": "msg-cm-1-2",
                    "speaker_slot": "cousin",
                    "content": "\"Are we finally there, or is this ancient bus going to rattle into loose bolts first?\" {{scenarioChar \"cousin\"}} grumbled without looking up, thirteen years old and swimming in an oversized dark tee, his earphones hanging loose around his collar while his thumbs hammered out a frantic sequence on his handheld console.",
                },
                {
                    "id": "msg-cm-1-3",
                    "speaker_slot": "twin",
                    "content": "{{scenarioChar \"twin\"}} leaned toward the window as the pine trees parted, revealing the sunlit expanse of Lake Erie. \"Look at that water. Cell reception dropped completely twenty miles back, but three weeks without city traffic and DCC logistics calls might actually be what we needed.\"",
                },
                {
                    "id": "msg-cm-1-4",
                    "speaker_slot": "camper_peer_1",
                    "content": "Jace Hart pointed through the dusty glass toward the carved wooden entrance archway. \"There it is, Camp Mystic. My older brother swore the Deep Ward out past the canoe slips is older than the state of Ohio.\"",
                },
            ],
        },
        {
            "id": "scene-camp-mystic-cabins",
            "name": "02. Cabin Assignment and Unpacking",
            "description": "Unpacking duffel bags in the pine-walled cabins, claiming bunks, and preparing for the first afternoon inspection.",
            "messages": [
                {
                    "id": "msg-cm-2-1",
                    "speaker_slot": "cousin",
                    "content": "{{scenarioChar \"cousin\"}} dumped his duffel bag onto the lower mattress of the nearest bunk with a heavy thud, immediately collapsing backward onto the canvas and staring up at the bare pine rafters. \"I claim the lower bunk. If anyone tries to make me sleep three feet closer to the spiders on the ceiling, I am protesting to Uncle Erik.\"",
                },
                {
                    "id": "msg-cm-2-2",
                    "speaker_slot": "cabin_mate_1",
                    "content": "A cabin mate hoisted a green canvas sea-bag onto the cedar bench, untying the brass clasp with a grin. \"Good luck with that. Last year someone complained about ceiling spiders, and Director Voss made them lead the dawn trail sweep.\"",
                },
                {
                    "id": "msg-cm-2-3",
                    "speaker_slot": "twin",
                    "content": "{{scenarioChar \"twin\"}} unzipped a leather travel bag, arranging clothes neatly into the iron-strapped cedar footlocker. \"Take the lower bunk, Edric. Just make sure your boots are under the frame. Counselor checks here are real, and nobody is doing push-ups on the gravel before dinner.\"",
                },
                {
                    "id": "msg-cm-2-4",
                    "speaker_slot": "supervisor",
                    "content": "A sharp rap sounded against the screen door frame. \"Quarters inspected in thirty minutes sharp. Gear stowed, footlockers latched, and inspection tags visible on your bunks. Move with purpose.\"",
                },
            ],
        },
        {
            "id": "scene-camp-mystic-docks",
            "name": "03. Afternoon Lake Recreation at the Docks",
            "description": "Cedar pontoon docks, aluminum canoes, skimming slate stones across Lake Erie, and safety briefings.",
            "messages": [
                {
                    "id": "msg-cm-3-1",
                    "speaker_slot": "twin",
                    "content": "{{scenarioChar \"twin\"}} adjusted the nylon straps of an orange life vest, stepping onto the sun-warmed cedar planks of the pontoon dock. The lake breeze smelled clean and sharp, carrying the distant splash of swimmers by the buoy perimeter. \"Water looks cold, but the red canoes are unlatched. Who is taking the stern paddle?\"",
                },
                {
                    "id": "msg-cm-3-2",
                    "speaker_slot": "cousin",
                    "content": "{{scenarioChar \"cousin\"}} stood at the edge of the dock, skimming a flat slate pebble across the water with surprising snap in his wrist, counting each skip under his breath. \"Five skips. Theo told me if we paddle out past the third buoy line, you can see the outline of the old nineteenth-century timber wreck resting in the shallows.\"",
                },
                {
                    "id": "msg-cm-3-3",
                    "speaker_slot": "camper_peer_2",
                    "content": "Theo Mercer carried a pair of aluminum oars down the shoreline gravel, setting them into the canoe oarlocks. \"Timber wreck is real, but do not touch the submerged beams. The wood is covered in zebra mussels that will slice right through sneakers.\"",
                },
                {
                    "id": "msg-cm-3-4",
                    "speaker_slot": "supervisor",
                    "content": "Celeste Nadir walked down the dock with a clipboard tucked beneath her arm, her silver eyes scanning the pontoons. \"Buddy tags verified before anyone steps into a boat. Whistles around your necks. If the lake horn sounds, all craft head straight for the gravel bank, no exceptions.\"",
                },
            ],
        },
        {
            "id": "scene-camp-mystic-campfire",
            "name": "04. Evening Campfire and Lakeside Lore",
            "description": "Campfire ceremony at twilight, birch logs crackling in the stone pit, hot cider, and ancient ward lore.",
            "messages": [
                {
                    "id": "msg-cm-4-1",
                    "speaker_slot": "director",
                    "content": "Director Mara Voss stood tall before the leaping flames of the stone firepit, her silhouette imposing against the dark waters of Lake Erie. The chatter among the split-log benches subsided into respectful silence. \"Every summer, new feet walk these trails, and every summer, the woods remember who you are. The rules here are simple. Respect the fire, respect the lake, and never wander past the boundary ridge after the final horn.\"",
                },
                {
                    "id": "msg-cm-4-2",
                    "speaker_slot": "cousin",
                    "content": "{{scenarioChar \"cousin\"}} sat on the edge of the cedar log, rotating a peeled marshmallow skewer over the glowing embers, the firelight catching the amber flecks in his eyes. \"She says that every year, but last night Evan swore he heard bells chiming out under the water.\"",
                },
                {
                    "id": "msg-cm-4-3",
                    "speaker_slot": "camper_peer_1",
                    "content": "A camper leaned closer over a tin mug of warm cider, lowering their voice beneath the crackle of birch bark. \"That is the Drowned Bell of the old mission outpost. They say the Firstborn placed it there centuries ago to anchor the Deep Ward across the lake floor.\"",
                },
                {
                    "id": "msg-cm-4-4",
                    "speaker_slot": "twin",
                    "content": "{{scenarioChar \"twin\"}} looked up past the pine canopy toward the early evening stars reflected on the calm lake surface. \"Whatever is under that water, it has kept this valley peaceful for hundreds of years. Drink your cider, Edric, before the embers burn down.\"",
                },
            ],
        },
    ]

    # Enforce multi-message greeting root parity
    for g in greetings:
        g["speaker_slot"] = g["messages"][0]["speaker_slot"]
        g["content"] = g["messages"][0]["content"]
        g["linked_persona_ids"] = []

    return {
        "name": "Svartulfr: Camp Mystic (Lake Erie Summer Arc)",
        "display_description": (
            "Camp Mystic Summer Arc: Ambientato sulle rive boscose del Lago Erie durante la sessione estiva residenziale di addestramento e controllo soprannaturale. "
            "{{user}} e il gemello Douglas-Bloodmoon condividono l'esperienza del campo con il cugino Edric (13 anni), i supervisori Marcus Vale e Celeste Nadir, "
            "la direttrice Mara Voss e i compagni di baita tra gare in canoa, addestramento pratico e misteri lacustri."
        ),
        "avatar": AVATAR_CAMP_MYSTIC,
        "tags": ["Werewolf", "Camp Mystic", "Lake Erie", "Summer", "Douglas", "Demihuman", "Urban Fantasy"],
        "visibility": "private",
        "rating": "explicit",
        "scenario": scenario_prompt,
        "startup_script": startup_script,
        "slots": slots,
        "greetings": greetings,
        "lorebook_ids": LOREBOOK_IDS,
        "gallery": [],
        "linked_world_id": "",
    }


# ==============================================================================
# SCENARIO 2: SUCC ROUTE ALYSSA
# ==============================================================================
def build_scenario_succ_alyssa() -> dict:
    slots = [
        {
            "key": "twin",
            "label": "Twin Brother (Jasper Svartr)",
            "pool": [{"character_id": CARD_JASPER, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "best_friend",
            "label": "Best Friend (Scarlett Rose)",
            "pool": [{"character_id": CARD_SCARLETT, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "crush",
            "label": "Crush (Mackenzie Sanchez-Rogers)",
            "pool": [{"character_id": CARD_MACKENZIE, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "roommate",
            "label": "Roommate (Sierra Cruz)",
            "pool": [{"character_id": CARD_SIERRA, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "childhood_friend",
            "label": "Childhood Friend (Finnegan Novak)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "quarterback",
            "label": "Quarterback (Jared Thompson)",
            "pool": [{"character_id": CARD_JARED, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "friend",
            "label": "Pre-Med Friend (Stanley Davies Jr.)",
            "pool": [{"character_id": CARD_STANLEY, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "sports_rival",
            "label": "Sports Rival (Vincent Campbell)",
            "pool": [],
            "unavailable_count": 0,
        },
    ]

    scenario_prompt = (
        "Setting: Solarton University and College Campus (SUCC), Solarton, California (Fall Semester 2024).\n\n"
        "Overview:\n"
        "Alyssa Hvit Douglas Bloodmoon embarks on her freshman year at SUCC as a Pre-Med student specializing in botanical remedies, "
        "restorative magic, and clinical anatomy. Residing at the Theta Iota Theta sorority house on Greek Row, her life balances academic rigor, "
        "sorority sisterhood, hospital internships at Aetheris Clinic, and collegiate drama across athletics, indie music, and supernatural factions.\n\n"
        "Cast and Verified Roles:\n"
        "- {{user}}: Alyssa Hvit Douglas Bloodmoon, 19yo Dominant Omega, White Moon healer, pacifist vow, carrying her dimensional pochette.\n"
        "- {{scenarioChar \"twin\"}} (Jasper Svartr Douglas Bloodmoon): 19yo Beta technomancer, twin brother, campus netrunner, and protective shadow.\n"
        "- {{scenarioChar \"best_friend\"}} (Scarlett Rose): 20yo Succubus demi-human, verified surname Rose, botany and fine arts major, social coordinator, and Alyssa's loyal confidante.\n"
        "- {{scenarioChar \"crush\"}} (Mackenzie 'Mac' Sanchez-Rogers): 20yo synth musician for Sidewinders, pureblood Rogers wolf lineage, charismatic campus weed dealer and Alyssa's romantic interest.\n"
        "- {{scenarioChar \"roommate\"}} (Sierra Cruz): 20yo Lamia demi-human, Theta Iota Theta sister, cheerleader, socialite roommate.\n"
        "- {{scenarioChar \"childhood_friend\"}} (Finnegan 'Finn' Novak): Strictly verified Arctic Wolf demi-human (Kemonomimi). He possesses exactly ONE single pair of ears (white wolf ears atop his skull, zero human ears) and a white tail. He is a non-shifter, has zero werewolf birth runes, and zero shifting ability. SUCC Bears left-wing hockey star and Alpha Rho Omega brother.\n"
        "- {{scenarioChar \"quarterback\"}} (Jared Thompson): 21yo Golden Retriever werewolf jock, star quarterback for SUCC Bulls, BRO fraternity member.\n"
        "- {{scenarioChar \"friend\"}} (Stanley Davies Jr.): 20yo Human pre-med scholar, Jared's sarcastic roommate, brilliant organic chemist.\n"
        "- {{scenarioChar \"sports_rival\"}} (Vincent Campbell): Montreal vampire aristocrat, captain and centre of SUCC Bears hockey, Alpha Sigma Sigma president.\n\n"
        "Invariants:\n"
        "- Finnegan Novak is explicitly specified as an Arctic Wolf demi-human (one pair of animal ears, non-shifter).\n"
        "- Scarlett Rose and Russell Sinclair surnames are canonical and verified.\n"

        + COMMON_NARRATION_GUIDELINES
    )

    greetings = [
        {
            "id": "scene-alyssa-greek-row",
            "name": "01. Theta Iota Theta Morning on Greek Row",
            "description": "Morning sunlight over Greek Row, coffee preparations with Sierra Cruz, and catching sight of Finn Novak on the Alpha Rho Omega porch.",
            "messages": [
                {
                    "id": "msg-al-1-1",
                    "speaker_slot": "roommate",
                    "content": "{{scenarioChar \"roommate\"}} stood by the full-length mirror, adjusting the hem of her cropped knit sweater while checking her phone calendar. \"If we leave in ten minutes, we can grab iced matcha before the lecture hall fills up. Professor Vance locked the front doors at five past eight on Monday.\"",
                },
                {
                    "id": "msg-al-1-2",
                    "speaker_slot": "childhood_friend",
                    "content": "Down on the street below, the screen door of the Alpha Rho Omega house creaked open. Finn Novak stepped onto the porch in a grey athletic hoodie, his white wolf ears flicking as his red eyes caught sight of the sorority steps. He straightened up, hesitated for a split second, then lifted a casual hand before turning toward the campus athletic fields.",
                },
                {
                    "id": "msg-al-1-3",
                    "speaker_slot": "twin",
                    "content": "A notification chimed on the desk console, a quick encrypted text from {{scenarioChar \"twin\"}}. \"Saw Vince and his ASS pledges lurking near the central library arches. Stay on the south path with Sierra. I will meet you at noon near the greenhouses.\"",
                },
            ],
        },
        {
            "id": "scene-alyssa-labs",
            "name": "02. Pre-Med Biology Labs",
            "description": "Botanical specimen slides in the science wing, sketching cell structures with Scarlett Rose, and Stan's dry academic banter.",
            "messages": [
                {
                    "id": "msg-al-2-1",
                    "speaker_slot": "best_friend",
                    "content": "{{scenarioChar \"best_friend\"}} rested her sketchpad beside a tray of botanical specimens, her pencil rendering the delicate vein structure of a silverleaf fern. Her red curls caught the white overhead light as she smiled. \"Professor Vance said if we finish the cellular titration before noon, we can take the leftover culture plates to the greenhouse. I already prepared the slides for your section.\"",
                },
                {
                    "id": "msg-al-2-2",
                    "speaker_slot": "friend",
                    "content": "{{scenarioChar \"friend\"}} adjusted his wire-rimmed glasses, double-checking the spectrometer readings on the resin bench with a sigh. \"If by titration you mean actual chemistry and not Jared's idea of mixing protein powder into distilled water, we might actually maintain our grade averages.\"",
                },
                {
                    "id": "msg-al-2-3",
                    "speaker_slot": "twin",
                    "content": "An incoming ping lit up the corner of {{user}}'s datapad. \"Finished the audio patch for Friday's set,\" {{scenarioChar \"twin\"}} texted. \"Grab two muffins from the commons on your way out if Stan does not burn down the laboratory first.\"",
                },
            ],
        },
        {
            "id": "scene-alyssa-library-corner",
            "name": "03. Basilica Library Sheltered Smoking Corner",
            "description": "Sheltered ivy-covered stone buttresses behind the Basilica Library, crisp air, and a relaxed conversation with Mackenzie.",
            "messages": [
                {
                    "id": "msg-al-3-1",
                    "speaker_slot": "crush",
                    "content": "{{scenarioChar \"crush\"}} had one headphone draped over his collar, leaning against the wrought-iron bicycle rack with his hands buried in his worn leather jacket. He looked up with a slow, easy grin that showed just a hint of sharp canine teeth. \"Library too quiet for you today, or did the anatomy flashcards finally stage a mutiny?\"",
                },
                {
                    "id": "msg-al-3-2",
                    "speaker_slot": "best_friend",
                    "content": "{{scenarioChar \"best_friend\"}} walked down the stone stairs carrying two iced coffees, catching the exchange with a subtle, delighted grin. \"I told her fresh air was mandatory. You playing at the Dockside venue this Friday, Mac?\"",
                },
                {
                    "id": "msg-al-3-3",
                    "speaker_slot": "twin",
                    "content": "A short vibration hummed in {{user}}'s pocket. {{scenarioChar \"twin\"}} sent an automated ping: \"Security patrol headed toward the library west lawn. Make sure Mac hides whatever he is smoking before Officer Higgins starts sniffing the ivy.\"",
                },
            ],
        },
        {
            "id": "scene-alyssa-ice-rink",
            "name": "04. Ice Rink Bears Practice Clash",
            "description": "Cold mist and slamming plexiglass at the SUCC Ice Arena, Vincent Campbell's arrogance, and Finn Novak's fierce play.",
            "messages": [
                {
                    "id": "msg-al-4-1",
                    "speaker_slot": "sports_rival",
                    "content": "{{scenarioChar \"sports_rival\"}} gathered a breakout pass at the centre circle, his black ponytail swaying as he roofed a wrist shot into the top shelf with effortless grace. He skated past the glass with a condescending smirk, tossing a sharp remark in French that echoed off the cold arena rafters.",
                },
                {
                    "id": "msg-al-4-2",
                    "speaker_slot": "childhood_friend",
                    "content": "Finn Novak barrelled into the neutral zone corner with brutal acceleration, slamming his shoulder into the glass with a thunderous rattle that sprayed ice shavings into the bleachers. His white wolf tail was stiff with anger and his red eyes blazed as he glared at the vampire captain, the whistle blowing shrilly between them.",
                },
                {
                    "id": "msg-al-4-3",
                    "speaker_slot": "quarterback",
                    "content": "{{scenarioChar \"quarterback\"}} stood near the tunnel railing in his football warm-ups, cupping his hands around his mouth to boom over the refrigeration hum. \"Keep your heads in the play, boys! We have scout scouts in the stands on Friday!\"",
                },
            ],
        },
        {
            "id": "scene-alyssa-bulls-tunnel",
            "name": "05. Bulls Locker Room and Stadium Tunnel",
            "description": "Athletic tape and liniment in the stadium corridor, Jared's good-natured plea for biochemistry tutoring, and Stan's dry reality check.",
            "messages": [
                {
                    "id": "msg-al-5-1",
                    "speaker_slot": "quarterback",
                    "content": "{{scenarioChar \"quarterback\"}} towered in his gold-and-black practice jersey, shoulder pads still strapped across his chest and a damp towel around his neck. His golden wolf ears twitched happily as his face broke into a broad grin. \"Hey! Tell me you brought the biochemistry lecture notes. Coach said if my midterm grade drops below a B, he is benching me for the first quarter on homecoming.\"",
                },
                {
                    "id": "msg-al-5-2",
                    "speaker_slot": "friend",
                    "content": "{{scenarioChar \"friend\"}} leaned against the concrete wall, clutching his binder with a deadpan expression. \"What Jared means is that he cannot tell an amine from an ester, and I refuse to spend another three hours explaining basic carbon bonds to a linebacker.\"",
                },
                {
                    "id": "msg-al-5-3",
                    "speaker_slot": "roommate",
                    "content": "{{scenarioChar \"roommate\"}} walked past carrying cheer practice flags, laughing as she shook her head. \"Help him out, Lys. If the Bulls lose the opening game, Greek Row will be in mourning for two weeks straight.\"",
                },
            ],
        },
        {
            "id": "scene-alyssa-sidewinders",
            "name": "06. Sidewinders Concert at The Dockside Venue",
            "description": "Neon stage lights, vibrating synth bass, and Mackenzie catching Alyssa's eyes from the stage during the climax of the set.",
            "messages": [
                {
                    "id": "msg-al-6-1",
                    "speaker_slot": "crush",
                    "content": "On the elevated stage, {{scenarioChar \"crush\"}} stood behind his dual-keyboard synthesizer rig, his fingers moving fluidly across the keys as the distortion built. The melodic chords rose into a soaring crescendo, and through the purple haze and strobe lights, his amber eyes locked onto {{user}} in the front row, his lips parting in an unmistakable smile.",
                },
                {
                    "id": "msg-al-6-2",
                    "speaker_slot": "best_friend",
                    "content": "{{scenarioChar \"best_friend\"}} danced beside {{user}}, laughing over the pounding bass and raising her plastic cup toward the stage. \"I told you his solo was worth the walk downtown! Look at the crowd, the entire campus showed up tonight!\"",
                },
                {
                    "id": "msg-al-6-3",
                    "speaker_slot": "twin",
                    "content": "From the sound booth balcony above the crowd, {{scenarioChar \"twin\"}} gave a sharp thumbs-up from behind the master equalizer console, ensuring the acoustics punched clean through the warehouse without clipping the amps.",
                },
            ],
        },
    ]

    for g in greetings:
        g["speaker_slot"] = g["messages"][0]["speaker_slot"]
        g["content"] = g["messages"][0]["content"]
        g["linked_persona_ids"] = []

    return {
        "name": "Svartulfr: SUCC Collegiate Arc (Alyssa Route)",
        "display_description": (
            "SUCC Campus Arc (Alyssa Route): Segui il primo anno accademico di Alyssa Hvit Douglas Bloodmoon alla SUCC. "
            "Dalle lezioni di botanica e medicina con Scarlett Rose e Stanley Davies Jr., alla vita nella sorority Theta Iota Theta con Sierra Cruz, "
            "gli incontri musicali con Mackenzie dei Sidewinders, la rivalità sportiva tra Finn Novak e Vincent Campbell, e il supporto continuo di Jasper."
        ),
        "avatar": AVATAR_ALYSSA,
        "tags": ["Werewolf", "SUCC", "College", "Alyssa", "Romance", "Urban Fantasy", "Demihuman"],
        "visibility": "private",
        "rating": "explicit",
        "scenario": scenario_prompt,
        "startup_script": "",
        "slots": slots,
        "greetings": greetings,
        "lorebook_ids": LOREBOOK_IDS,
        "gallery": [],
        "linked_world_id": "",
    }


# ==============================================================================
# SCENARIO 3: SUCC ROUTE JASPER
# ==============================================================================
def build_scenario_succ_jasper() -> dict:
    slots = [
        {
            "key": "twin",
            "label": "Twin Sister (Alyssa Hvit)",
            "pool": [{"character_id": CARD_ALYSSA, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "male_roommate",
            "label": "Roommate (Russell 'Russ' Sinclair)",
            "pool": [{"character_id": CARD_RUSS, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "crush",
            "label": "Crush (Scarlett Rose)",
            "pool": [{"character_id": CARD_SCARLETT, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "ai_companion",
            "label": "AI Companion (Echo)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "childhood_friend",
            "label": "Childhood Friend (Finnegan Novak)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "quarterback",
            "label": "Quarterback (Jared Thompson)",
            "pool": [{"character_id": CARD_JARED, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "friend",
            "label": "Friend (Stanley Davies Jr.)",
            "pool": [{"character_id": CARD_STANLEY, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "sports_rival",
            "label": "Sports Rival (Vincent Campbell)",
            "pool": [],
            "unavailable_count": 0,
        },
    ]

    scenario_prompt = (
        "Setting: Solarton University and College Campus (SUCC), Wyrm Hall Suite 304, Solarton, California (Fall Semester 2024).\n\n"
        "Overview:\n"
        "Jasper Svartr Douglas Bloodmoon navigates freshman life as an Arcane Engineering student, underground DJ (DJ Frequency), "
        "and rogue netrunner. Residing in Wyrm Hall Suite 304 with tattoo artist Russell Sinclair and the Cocketeers crew (Dean, Eric, Javier, Raymond), "
        "Jasper monitors campus servers, executes rooftop antenna hacks, DJs subterranean warehouse raves, and protects his twin sister Alyssa from afar.\n\n"
        "Cast and Verified Roles:\n"
        "- {{user}}: Jasper Svartr Douglas Bloodmoon, 19yo Founding Beta, Technomancer, DJ Frequency, and cyber sentinel.\n"
        "- {{scenarioChar \"twin\"}} (Alyssa Hvit Douglas Bloodmoon): 19yo Dominant Omega, pre-med botanist, twin sister.\n"
        "- {{scenarioChar \"male_roommate\"}} (Russell 'Russ' Sinclair): Verified surname Sinclair, 20yo tiger demi-human tattoo artist, Cocketeers ringleader, loyal roommate.\n"
        "- {{scenarioChar \"crush\"}} (Scarlett Rose): Verified surname Rose, 20yo succubus demi-human, fine arts student, Jasper's secret romantic crush.\n"
        "- {{scenarioChar \"ai_companion\"}} (Echo): Sentient digital entity and cyber-familiar living in Jasper's hardware and network rigs.\n"
        "- {{scenarioChar \"childhood_friend\"}} (Finnegan 'Finn' Novak): Strictly verified Demi-Human Arctic Wolf (Kemonomimi), one pair of ears, non-shifter, hockey star.\n"
        "- {{scenarioChar \"quarterback\"}} (Jared Thompson): 21yo werewolf quarterback, good-natured muscle and protector.\n"
        "- {{scenarioChar \"friend\"}} (Stanley Davies Jr.): 20yo human pre-med scholar, sarcastic science peer.\n"
        "- {{scenarioChar \"sports_rival\"}} (Vincent Campbell): 21yo vampire hockey captain, arrogant campus aristocrat.\n\n"
        "Invariants:\n"
        "- Russell Sinclair and Scarlett Rose surnames verified.\n"
        "- Finnegan Novak is an Arctic Wolf demi-human (one pair of animal ears, non-shifter).\n"
        + COMMON_NARRATION_GUIDELINES
    )

    greetings = [
        {
            "id": "scene-jasper-wyrm-304",
            "name": "01. Wyrm Hall Suite 304",
            "description": "Solder resin, tattoo guns, Ash the cat on the amplifier, Russ Sinclair's banter, and Echo detecting network anomalies.",
            "messages": [
                {
                    "id": "msg-js-1-1",
                    "speaker_slot": "male_roommate",
                    "content": "{{scenarioChar \"male_roommate\"}} sat perched on the low vinyl sofa, his bare shoulders covered in dark ink and his bandana holding back his messy curls. He was carefully adjusting the needle depth on a rotary tattoo machine as the door opened. \"Yo, Svartr. Javier says the loading dock gate is unlocked tonight if we want to test the directional antenna rig. Also, Raymond tried to swipe your good soldering iron again, but I intercepted him.\"",
                },
                {
                    "id": "msg-js-1-2",
                    "speaker_slot": "ai_companion",
                    "content": "From the dual-monitor workstation beneath the bunk bed, a soft chime chimed through the desktop speakers. Echo's geometric voice visualizer pulsed blue across the ultrawide display. \"Campus network anomaly detected on Subnet 4. Incoming packet stream indicates unauthorized packet inspection by campus IT. Shall I isolate the gateway, Jasper?\"",
                },
                {
                    "id": "msg-js-1-3",
                    "speaker_slot": "twin",
                    "content": "A gentle knock sounded against the door, and {{scenarioChar \"twin\"}} peeked into the room holding two cardboard lunch boxes from Theta house. \"Brought sandwiches from Greek Row before the guys eat everything in the common fridge. Are you two still rebuilding that sound amplifier?\"",
                },
            ],
        },
        {
            "id": "scene-jasper-roof-hack",
            "name": "02. Wyrm Hall Roof Hacking Session",
            "description": "Chilly night breeze on the gravel roof, directional parabolic antenna clamped to the railing, and tapping into administration telemetry.",
            "messages": [
                {
                    "id": "msg-js-2-1",
                    "speaker_slot": "ai_companion",
                    "content": "On the ruggedized terminal resting on the tar-paper blanket, Echo's digital waveform traced a steady blue line. \"Signal strength ninety-two percent. Campus administration firewall bypassed. We have an unthrottled gateway straight into the DCC regional telemetry loop without triggering the local proxy logs.\"",
                },
                {
                    "id": "msg-js-2-2",
                    "speaker_slot": "male_roommate",
                    "content": "{{scenarioChar \"male_roommate\"}} stepped through the roof access door, carrying two cold cans of energy soda and leaning his back against the brick ventilation shaft. \"Nobody followed me up the emergency stairwell. If campus security shows up, we throw the canvas over the antenna and tell them we are stargazing for astronomy lab.\"",
                },
                {
                    "id": "msg-js-2-3",
                    "speaker_slot": "childhood_friend",
                    "content": "A brief text message flashed on the smartphone screen from Finn Novak: \"Bears night conditioning ended early. Campus security truck just pulled up outside Griffin Clocktower. Watch the perimeter.\"",
                },
            ],
        },
        {
            "id": "scene-jasper-quad-tension",
            "name": "03. Campus Quad Tension",
            "description": "Confrontation near the marble fountain with Vincent Campbell, defused by Jared Thompson's colossal presence.",
            "messages": [
                {
                    "id": "msg-js-3-1",
                    "speaker_slot": "sports_rival",
                    "content": "{{scenarioChar \"sports_rival\"}} stopped near the granite fountain with two fraternity pledges in tailored coats, adjusting his sunglasses with effortless disdain. \"Well, if it is not the engineering department's resident gremlin. Tell me, Douglas, do you ever leave that dorm basement without smelling like scorched wiring and black coffee?\"",
                },
                {
                    "id": "msg-js-3-2",
                    "speaker_slot": "quarterback",
                    "content": "{{scenarioChar \"quarterback\"}} strode across the lawn with his heavy football duffel slung over his shoulder, stepping squarely between them and clapping a massive, heavy hand onto Vincent's shoulder that made the vampire's jaw clench. \"Come on, Vince, leave the wizard alone. Some of us actually need his server magic to pass our communications courses.\"",
                },
                {
                    "id": "msg-js-3-3",
                    "speaker_slot": "friend",
                    "content": "{{scenarioChar \"friend\"}} stood a few paces back with a dry smirk, tapping his pen against his textbook. \"Statistically speaking, Vincent, every time you insult the person who administers the campus Wi-Fi, your dorm building's bandwidth drops by twenty percent. I would choose your words carefully.\"",
                },
            ],
        },
        {
            "id": "scene-jasper-warehouse-rave",
            "name": "04. DJ Frequency Underground Dock Warehouse Rave",
            "description": "Bone-shattering subwoofers, strobe lights, and running the live remix set at the subterranean shipping canal venue.",
            "messages": [
                {
                    "id": "msg-js-4-1",
                    "speaker_slot": "male_roommate",
                    "content": "{{scenarioChar \"male_roommate\"}} pushed through the backstage black curtain, wiping sweat from his brow and handing over a cold aluminium can with a wide grin. \"Crowd is losing their minds over the bass drop, Frequency! Even the hockey crew showed up. Half the Bears line is standing near the side exit.\"",
                },
                {
                    "id": "msg-al-4-2",
                    "speaker_slot": "twin",
                    "content": "From the elevated catwalk overlooking the pulsing dance floor, {{scenarioChar \"twin\"}} leaned over the iron railing with a glowing light stick, smiling brightly and cheering as the crowd chanted along with the synthesizer breakdown.",
                },
                {
                    "id": "msg-js-4-3",
                    "speaker_slot": "ai_companion",
                    "content": "Echo's voice chimed cleanly through the monitor headphones, perfectly isolated from the roar of the subwoofers. \"Acoustic output at ninety-eight decibels. Thermal sensors on amplifier rack four within safe margins. Ready to drop the second phase sequence on your cue, Jasper.\"",
                },
            ],
        },
        {
            "id": "scene-jasper-bro-halloween",
            "name": "05. Beta Rho Omega Halloween Party",
            "description": "Halloween festivities at the three-story BRO house, carved lanterns, and a quiet moment with Scarlett Rose on the balcony.",
            "messages": [
                {
                    "id": "msg-js-5-1",
                    "speaker_slot": "crush",
                    "content": "{{scenarioChar \"crush\"}} stood by the second-floor wooden balustrade, dressed in an intricate wood-nymph costume with fresh laurel leaves woven through her auburn hair. She turned as footsteps approached, a soft, genuine smile breaking through her shyness beneath the warm lantern light. \"I did not think you would actually come to this party. Russ said you were locked in the server room all afternoon.\"",
                },
                {
                    "id": "msg-js-5-2",
                    "speaker_slot": "quarterback",
                    "content": "Down in the crowded foyer, {{scenarioChar \"quarterback\"}} held up a carved pumpkin punch bowl dressed as a Roman gladiator, leading a roaring fraternity toast that echoed off the grand oak staircase.",
                },
                {
                    "id": "msg-js-5-3",
                    "speaker_slot": "male_roommate",
                    "content": "{{scenarioChar \"male_roommate\"}} caught Jasper's eye from the landing below with a drink in hand, giving him an amused grin and an unmistakable nod of encouragement before heading back into the crowd.",
                },
            ],
        },
    ]

    for g in greetings:
        g["speaker_slot"] = g["messages"][0]["speaker_slot"]
        g["content"] = g["messages"][0]["content"]
        g["linked_persona_ids"] = []

    return {
        "name": "Svartulfr: SUCC Collegiate Arc (Jasper Route)",
        "display_description": (
            "SUCC Campus Arc (Jasper Route): Vivi il primo anno universitario dal punto di vista di Jasper Svartr Douglas Bloodmoon. "
            "Dalle sessioni di hacking e le serate in Suite 304 con Russ Sinclair e i Cocketeers, i collegamenti neurali con l'IA Echo, "
            "i rave underground come DJ Frequency, i confronti con Vincent Campbell e Jared Thompson, fino ai momenti intimi con Scarlett Rose."
        ),
        "avatar": AVATAR_JASPER,
        "tags": ["Werewolf", "SUCC", "College", "Jasper", "Hacking", "DJ", "Urban Fantasy", "Demihuman"],
        "visibility": "private",
        "rating": "explicit",
        "scenario": scenario_prompt,
        "startup_script": "",
        "slots": slots,
        "greetings": greetings,
        "lorebook_ids": LOREBOOK_IDS,
        "gallery": [],
        "linked_world_id": "",
    }


# ==============================================================================
# SCENARIO 4: VILLA DOUGLAS
# ==============================================================================
def build_scenario_villa_douglas() -> dict:
    # Exactly the 7 canonical male cards
    slots = [
        {
            "key": "father",
            "label": "Father (Erik Ulfr Douglas)",
            "pool": [{"character_id": CARD_ERIK, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "eldest_brother",
            "label": "Eldest Brother (Malachia Björn Douglas Bloodmoon)",
            "pool": [{"character_id": CARD_MALACHIA, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "tech_brother",
            "label": "Tech Brother (Jasper Svartr Douglas Bloodmoon)",
            "pool": [{"character_id": CARD_JASPER, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "politician_brother",
            "label": "Politician Brother (Noah Loki Douglas Bloodmoon)",
            "pool": [{"character_id": CARD_NOAH, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "maternal_grandfather",
            "label": "Maternal Grandfather (Wulfnic Báleygr Bloodmoon)",
            "pool": [{"character_id": CARD_WULFNIC, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "uncle",
            "label": "Uncle (Logan Dominic Járn Douglas)",
            "pool": [{"character_id": CARD_LOGAN, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "cousin",
            "label": "Cousin (Edric Douglas)",
            "pool": [{"character_id": CARD_EDRIC, "weight": 100}],
            "unavailable_count": 0,
        },
    ]

    scenario_prompt = (
        "Setting: Villa Douglas, 555 Oak Road, Seven Hills, Blackwood City, California (2024).\n\n"
        "Overview:\n"
        "Villa Douglas is the fortified ancestral estate of House Douglas and House Bloodmoon, commanding the heights of Seven Hills. "
        "Behind its limestone walls, manicured gardens, and ballistic laminate windows resides the ruling patriarchal circle of the pack. "
        "Here, multi-generational lycanthropic power converges: military discipline, corporate empire, digital espionage, political strategy, "
        "ancestral rites of the Firstborn, and deep familial loyalty.\n\n"
        "The 7 Canonical Douglas Patriarchs:\n"
        "- {{scenarioChar \"father\"}} (Erik Ulfr Douglas): 55yo Pureblood Prime Alpha, Pack Leader of Seven Hills, billionaire CEO of Douglas Commercial Coalition (DCC).\n"
        "- {{scenarioChar \"eldest_brother\"}} (Malachia Björn Douglas Bloodmoon): 26yo Dominant Alpha, undefeated heavyweight fighter, pack field commander, Erik's right hand.\n"
        "- {{scenarioChar \"tech_brother\"}} (Jasper Svartr Douglas Bloodmoon): 19yo Founding Beta, cyber rogue, DJ Frequency, and digital architect of family defenses.\n"
        "- {{scenarioChar \"politician_brother\"}} (Noah Loki Douglas Bloodmoon): 24yo Delta diplomat, charming corporate negotiator, SUCC Bears hockey veteran.\n"
        "- {{scenarioChar \"maternal_grandfather\"}} (Wulfnic Báleygr Bloodmoon): Primordial Firstborn Alpha (Living Saga, over a millennium old), guardian of the Sacred Forest.\n"
        "- {{scenarioChar \"uncle\"}} (Logan Dominic Járn Douglas): 43yo Beta peacekeeper, master motorcycle mechanic and owner of The Verve biker lounge.\n"
        "- {{scenarioChar \"cousin\"}} (Edric Douglas): 18yo younger cousin (son of Logan), gamer, tech enthusiast, and sharp-tongued family observer.\n\n"
        "Invariants:\n"
        "- Exclusively the 7 canonical male Douglas/Bloodmoon characters.\n"
        "- Demi-humans possess only ONE pair of animal ears.\n"
        + COMMON_NARRATION_GUIDELINES
    )

    greetings = [
        {
            "id": "scene-villa-living-room",
            "name": "01. Living Room Gaming (Call of Duty)",
            "description": "Intense multiplayer gaming session on the big screen, brotherly banter, Logan relaxing on the porch, and Wulfnic's cryptic SMS.",
            "messages": [
                {
                    "id": "msg-vd-1-1",
                    "speaker_slot": "cousin",
                    "content": "{{scenarioChar \"cousin\"}} threw his hands in the air, slumping dramatically back into the leather couch cushions as his screen went red. \"What? That was completely through the brick wall! That guy is definitely running an aimbot on the server!\"",
                },
                {
                    "id": "msg-vd-1-2",
                    "speaker_slot": "eldest_brother",
                    "content": "{{scenarioChar \"eldest_brother\"}} lowered his tablet from the recliner, his sharp golden gaze sweeping over his younger brothers with amused stoicism. \"Excuses do not improve your tactical awareness, Edric. You stood motionless in an open doorway for four seconds.\"",
                },
                {
                    "id": "msg-vd-1-3",
                    "speaker_slot": "tech_brother",
                    "content": "{{scenarioChar \"tech_brother\"}} clicked his thumbsticks in rapid succession, his character vaulting through a second-story window to clear the opposing team. \"Target neutralized. Next time, wait for my smoke grenade before sprinting across the courtyard.\"",
                },
                {
                    "id": "msg-vd-1-4",
                    "speaker_slot": "uncle",
                    "content": "Out on the stone porch, {{scenarioChar \"uncle\"}} leaned against the timber railing with a mug of black coffee, calling in through the open French doors. \"If you boys break another wireless controller, one of you is driving down to the depot to replace it. And nobody touches my workshop tools.\"",
                },
                {
                    "id": "msg-vd-1-5",
                    "speaker_slot": "father",
                    "content": "{{scenarioChar \"father\"}} stepped into the hall from his study, his reading glasses tucked into his shirt pocket and his hazel eyes warm. \"Keep the volume down a fraction, champions. I have DCC board members on the line from Tokyo in twenty minutes.\"",
                },
                {
                    "id": "msg-vd-1-6",
                    "speaker_slot": "politician_brother",
                    "content": "{{scenarioChar \"politician_brother\"}} leaned back in his armchair, tossing a bag of trail mix onto the coffee table with a relaxed laugh. \"Let the kid complain, Malachia. Aimbots build character. Besides, Edric's blood pressure is the only thing giving the living room energy today.\"",
                },
                {
                    "id": "msg-vd-1-7",
                    "speaker_slot": "maternal_grandfather",
                    "content": "A sudden buzz rattled against the side table as Wulfnic's archaic mobile phone illuminated with a short message in all capitals: 'PACK MEETS AT SUNSET. WARD STONES ARE RENEWED. BE AT THE FIRE BEFORE DARK.'",
                },
            ],
        },
        {
            "id": "scene-villa-erik-study",
            "name": "02. Erik's Study (Sanctuary of Mahogany and Ballistic Steel)",
            "description": "Quiet moments in Erik's private executive study, sandalwood scent, logistics monitors, and Nixara's portrait shrine.",
            "messages": [
                {
                    "id": "msg-vd-2-1",
                    "speaker_slot": "father",
                    "content": "{{scenarioChar \"father\"}} placed his heavy Montblanc pen onto the leather desk blotter, his piercing hazel eyes softening as the heavy oak door closed. \"Come in. Shut the latch behind you. It is rare to get twenty quiet minutes in this house before someone challenges a sparring match or drops a server.\"",
                },
                {
                    "id": "msg-vd-2-2",
                    "speaker_slot": "politician_brother",
                    "content": "{{scenarioChar \"politician_brother\"}} slipped into the room with a sleek leather folder, setting the quarterly DCC municipal permits on the corner of the credenza. \"Permits for the north perimeter gate were cleared by city hall this morning, Dad. The mayor signed off without asking a single question.\"",
                },
                {
                    "id": "msg-vd-2-3",
                    "speaker_slot": "eldest_brother",
                    "content": "{{scenarioChar \"eldest_brother\"}} stood silently by the reinforced ballistic window overlooking Blackwood City, his arms crossed over his chest. \"Security sweeps along Seven Hills road are complete. Zero unidentified vehicles within three miles of the compound.\"",
                },
            ],
        },
        {
            "id": "scene-villa-verve-lounge",
            "name": "03. The Verve Lounge (Motorcycle Garage and Real Advice)",
            "description": "The neon hum of The Verve in the warehouse district, motor oil and bourbon, custom choppers, and Logan's grounded counsel.",
            "messages": [
                {
                    "id": "msg-vd-3-1",
                    "speaker_slot": "uncle",
                    "content": "{{scenarioChar \"uncle\"}} set down a heavy torque wrench beside the chopper on the hydraulic lift, wiping his hands on a shop rag. He pulled a cold bottle from the under-counter fridge and set it on the zinc tabletop. \"Figured you would turn up down here sooner or later. Erik is up at the Villa drawing up DCC battle plans, Malachia is drilling the perimeter, and Noah is playing politics. Take a seat. Down here, nobody is running an empire. What is on your mind?\"",
                },
                {
                    "id": "msg-vd-3-2",
                    "speaker_slot": "tech_brother",
                    "content": "{{scenarioChar \"tech_brother\"}} emerged from the diagnostic bay in grease-stained cargo pants, wiping a smudge from his cheek. \"Told Uncle Logan his fuel injection mapping was running too lean. Tuned it from my phone, so the bike will actually start on cold mornings now.\"",
                },
                {
                    "id": "msg-vd-3-3",
                    "speaker_slot": "cousin",
                    "content": "{{scenarioChar \"cousin\"}} leaned against the vintage pinball cabinet in the corner, tapping the flipper buttons to rack up a high score. \"If you guys are going on a test ride down the coast highway, I am riding in the sidecar.\"",
                },
            ],
        },
        {
            "id": "scene-villa-yule-vigil",
            "name": "04. Sacred Yule Vigil (The Grove of Seven Hills)",
            "description": "Winter solstice gathering in the ancient sacred grove, sacred ash fire, runic stones, and Wulfnic's primordial invocation.",
            "messages": [
                {
                    "id": "msg-vd-4-1",
                    "speaker_slot": "maternal_grandfather",
                    "content": "{{scenarioChar \"maternal_grandfather\"}} struck the base of his petrified rowan staff against the frozen earth, a resonant, low vibration trembling through the stone altar. His towering frame stood unmoving in wolf pelts as his single eye reflected the leaping sacred fire. \"The longest night yields to the blood that endures. The pack is the circle, and the circle does not break.\"",
                },
                {
                    "id": "msg-vd-4-2",
                    "speaker_slot": "father",
                    "content": "{{scenarioChar \"father\"}} bowed his head in solemn reverence before the flames, his broad shoulders squared as he spoke the sacred covenant of House Douglas. \"We guard the bloodline, we shield the young, and we hold the ground our fathers claimed.\"",
                },
                {
                    "id": "msg-vd-4-3",
                    "speaker_slot": "eldest_brother",
                    "content": "{{scenarioChar \"eldest_brother\"}} stepped forward to cast a bundle of dry cedar and winter sage into the hearth, the aromatic smoke billowing white into the freezing mountain air.",
                },
                {
                    "id": "msg-vd-4-4",
                    "speaker_slot": "politician_brother",
                    "content": "{{scenarioChar \"politician_brother\"}} stood beside his brothers in quiet respect, the easy smirk absent from his face as he observed the ancient rites of the Firstborn.",
                },
            ],
        },
        {
            "id": "scene-villa-kitchen-dawn",
            "name": "05. Kitchen Crossroad at Dawn (Before the Summer Dispersal)",
            "description": "Dawn light on the granite kitchen island, hissing espresso machine, sourdough toast, and family conversations before daily duties.",
            "messages": [
                {
                    "id": "msg-vd-5-1",
                    "speaker_slot": "father",
                    "content": "{{scenarioChar \"father\"}} stood by the counter in comfortable wool slacks and a grey sweater, pouring dark roast coffee from the espresso pot into a porcelain mug. \"Coffee is fresh. Sit down. We have forty minutes of quiet before the contractors and municipal calls begin.\"",
                },
                {
                    "id": "msg-vd-5-2",
                    "speaker_slot": "politician_brother",
                    "content": "{{scenarioChar \"politician_brother\"}} jogged into the kitchen in running shorts and a towel, pouring a tall glass of ice water. \"Five miles along the ridge trail. Coastal fog is clearing up fast. Who took the last carton of pasture eggs?\"",
                },
                {
                    "id": "msg-vd-5-3",
                    "speaker_slot": "cousin",
                    "content": "{{scenarioChar \"cousin\"}} dragged his feet across the tile floor in flannel pajama pants, his dark bangs sticking up as he reached straight for the cereal cupboard. \"Whoever ate the cinnamon toast crunch while I was asleep is getting their headset muted for a month.\"",
                },
                {
                    "id": "msg-vd-5-4",
                    "speaker_slot": "eldest_brother",
                    "content": "{{scenarioChar \"eldest_brother\"}} cracked four eggs into a sizzling cast-iron skillet, his expression calm. \"Eggs are in the pan, Edric. Sit at the table and eat properly.\"",
                },
            ],
        },
    ]

    for g in greetings:
        g["speaker_slot"] = g["messages"][0]["speaker_slot"]
        g["content"] = g["messages"][0]["content"]
        g["linked_persona_ids"] = []

    return {
        "name": "Svartulfr: Villa Douglas (The Douglas Patriarchs)",
        "display_description": (
            "Villa Douglas Arc: Vivi le dinamiche intime e strategiche all'interno della residenza patriarcale di Seven Hills. "
            "Coinvolge rigorosamente i 7 personaggi maschili canonici della famiglia Douglas e Bloodmoon: il capobranco Erik, "
            "i fratelli Malachia, Jasper e Noah, lo zio Logan, il giovane cugino Edric e il nonno primordiale Wulfnic."
        ),
        "avatar": AVATAR_VILLA_DOUGLAS,
        "tags": ["Werewolf", "Villa Douglas", "Family", "Douglas", "Patriarchs", "Urban Fantasy"],
        "visibility": "private",
        "rating": "explicit",
        "scenario": scenario_prompt,
        "startup_script": "",
        "slots": slots,
        "greetings": greetings,
        "lorebook_ids": LOREBOOK_IDS,
        "gallery": [],
        "linked_world_id": "",
    }


# ==============================================================================
# SCENARIO 5: DMHA DUNGEONS
# ==============================================================================
def build_scenario_dmha_dungeons() -> dict:
    slots = [
        {
            "key": "twin_healer",
            "label": "Twin Healer (Alyssa Hvit)",
            "pool": [{"character_id": CARD_ALYSSA, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "twin_tech",
            "label": "Twin Tech (Jasper Svartr)",
            "pool": [{"character_id": CARD_JASPER, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "eldest_brother",
            "label": "Eldest Brother (Malachia Björn)",
            "pool": [{"character_id": CARD_MALACHIA, "weight": 100}],
            "unavailable_count": 0,
        },
        {
            "key": "demihuman_representative",
            "label": "Demihuman Representative (Barrow)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "biker_enforcer",
            "label": "Biker Enforcer (Marek)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "raid_leader",
            "label": "Raid Leader (Radek)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "tank_frontline",
            "label": "Tank Frontline (Goran)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "scout_infiltrator",
            "label": "Scout Infiltrator (Kian)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "faction_support",
            "label": "Faction Support (DMHA Strike Team / Nomads)",
            "pool": [],
            "unavailable_count": 0,
        },
    ]

    scenario_prompt = (
        "Setting: Department of Monster & Hunter Affairs (DMHA) Staging Zones, Spatial Rifts, and Underworld Enclaves (Chicago Southside & The Horns).\n\n"
        "Overview:\n"
        "Spatial breaches and volatile dungeon rifts threaten urban reality, requiring joint operations between the DMHA, elite hunting squads, "
        "and demi-human enclaves. In this high-stakes combat and dungeon crawler setting, Team Ukiyo (Radek, Goran, Kian) coordinates deep descents, "
        "backed by the heavy muscle of the Ironhorn Nomads (Marek, Barrow) and the formidable vanguard of the Douglas-Bloodmoon siblings.\n\n"
        "Cast and Verified Roles:\n"
        "- {{scenarioChar \"twin_healer\"}} (Alyssa Hvit Douglas Bloodmoon): 19yo Dominant Omega, Field Medic, Pre-Med Healer, Absolute Pacifist Vow, carrying dimensional medical pochette.\n"
        "- {{scenarioChar \"twin_tech\"}} (Jasper Svartr Douglas Bloodmoon): 19yo Beta Technomancer, Netrunner, wielding ancestral Dragon Glass Katana, specialized in rift frequency stabilization.\n"
        "- {{scenarioChar \"eldest_brother\"}} (Malachia Björn Douglas Bloodmoon): 26yo Dominant Alpha, undefeated heavyweight fighter, unstoppable vanguard shield.\n"
        "- {{scenarioChar \"demihuman_representative\"}} (Barrow): 42yo Minotaur, former Ironhorn Nomad enforcer, master builder, and guardian of The Horns demi-human enclave on Chicago's Southside.\n"
        "- {{scenarioChar \"biker_enforcer\"}} (Marek): 47yo Blue Oni, founder and heavy enforcer of the Ironhorn Nomads Motorcycle Club, wielding tire irons and high-caliber ordnance.\n"
        "- {{scenarioChar \"raid_leader\"}} (Radek): 31yo Orc, Team Ukiyo Squad Leader, Grade S Hunter, master tactician with topographical dungeon tattoos and cleaver-greatsword.\n"
        "- {{scenarioChar \"tank_frontline\"}} (Goran): 29yo Orc/Minotaur frontline berserker, scarred tank wielding a colossal warhammer.\n"
        "- {{scenarioChar \"scout_infiltrator\"}} (Kian): 27yo Orc/Half-Elf rogue, dual daggers and silenced mana sniper rifle.\n"
        "- {{scenarioChar \"faction_support\"}}: DMHA Tactical Strike Team officers and Ironhorn Nomads motorcycle vanguard.\n\n"
        "Invariants:\n"
        "- Rigorous combat and tactical discipline.\n"
        "- Dialogue in standard double quotes, actions in plain text.\n"
        + COMMON_NARRATION_GUIDELINES
    )

    greetings = [
        {
            "id": "scene-dmha-briefing",
            "name": "01. Hot Zone Briefing at the DMHA Staging Shed",
            "description": "Pre-raid briefing in the DMHA staging shed, smell of gun oil and whetstones, pulsing rift gate outside, and tactical instructions.",
            "messages": [
                {
                    "id": "msg-dm-1-1",
                    "speaker_slot": "raid_leader",
                    "content": "{{scenarioChar \"raid_leader\"}} tested the heavy nylon strap across his tactical vest with a sharp jerk, his amber eyes scanning the team beneath the flickering fluorescent tubes. \"Tie it high. Tight. Everything on your person needs to be an extension of your body, not an obstacle to my movement. The spatial breach on floor seven is widening by three inches an hour, and once we cross the gate threshold, the DMHA radio repeaters will not reach us.\"",
                },
                {
                    "id": "msg-dm-1-2",
                    "speaker_slot": "tank_frontline",
                    "content": "{{scenarioChar \"tank_frontline\"}} let out a low, gravelly chuckle, resting the massive steel head of his notched warhammer on the concrete floor. \"Let the gate widen. My hammer has been dry since Tuesday, and the lower floors always have bigger hides to split.\"",
                },
                {
                    "id": "msg-dm-1-3",
                    "speaker_slot": "scout_infiltrator",
                    "content": "{{scenarioChar \"scout_infiltrator\"}} flipped a black trench dagger into the air, catching the hilt by the pommel without looking. \"Scout drones reported shadow-stalkers circling the second landing. If you heavy hitters make too much noise on the stairs, do not blame me when we get ambushed from the ceiling.\"",
                },
                {
                    "id": "msg-dm-1-4",
                    "speaker_slot": "eldest_brother",
                    "content": "{{scenarioChar \"eldest_brother\"}} tightened the wraps around his knuckles, his massive frame radiating quiet, lethal focus. \"The twins stay between Goran and me. Anyone who breaks formation answers to my fists.\"",
                },
                {
                    "id": "msg-dm-1-5",
                    "speaker_slot": "twin_tech",
                    "content": "{{scenarioChar \"twin_tech\"}} calibrated his frequency scanner, the Dragon Glass Katana strapped securely across his back. \"Mana frequency locked at forty-two kilohertz. I have the rift anchor coordinates loaded into the scanner.\"",
                },
            ],
        },
        {
            "id": "scene-dmha-floor-10",
            "name": "02. Floor 10 Sanctuary (Vaulted Safe Zone Hot Pot)",
            "description": "Vaulted rune-carved stone chamber on Floor 10, hot pot meal with shadow-stalker meat, sharpening weapons, and resting before descent.",
            "messages": [
                {
                    "id": "msg-dm-2-1",
                    "speaker_slot": "scout_infiltrator",
                    "content": "{{scenarioChar \"scout_infiltrator\"}} used his combat blade to slide paper-thin slices of raw marbled shadow-stalker meat into the boiling cast-iron pot, steam rising toward the rune-carved ceiling of the safe vault. \"Told you the haunch was prime grade. Add the wild garlic pods, Alyssa, before Goran eats all the mushrooms.\"",
                },
                {
                    "id": "msg-dm-2-2",
                    "speaker_slot": "tank_frontline",
                    "content": "{{scenarioChar \"tank_frontline\"}} drew a heavy steel file across a jagged dent in his warhammer, the harsh rasp echoing against the ancient granite walls. \"Meat is meat. It kept us alive through the descent, and we still have ten floors of abyssal crawlers before the boss chamber.\"",
                },
                {
                    "id": "msg-dm-2-3",
                    "speaker_slot": "raid_leader",
                    "content": "{{scenarioChar \"raid_leader\"}} marked the floor map with charcoal against a flat boulder. \"Ten down, twenty to go. Conserve your energy. Eat your rations, rehydrate, and sleep. We rotate two-man watch shifts every forty minutes.\"",
                },
                {
                    "id": "msg-dm-2-4",
                    "speaker_slot": "twin_healer",
                    "content": "{{scenarioChar \"twin_healer\"}} opened her emerald dimensional pochette, pulling out clean linen bandages and a jar of soothing silverleaf salve. \"Sit down, Goran. Let me clean that laceration along your shoulder before the mana seepage causes an infection.\"",
                },
            ],
        },
        {
            "id": "scene-dmha-incursion-nomads",
            "name": "03. Deep Incursion and Ironhorn Nomads Flank",
            "description": "Floor 24 subterranean breach, abyssal beasts swarming the frontline, and the Ironhorn Nomads breaking through the flank with heavy vehicles.",
            "messages": [
                {
                    "id": "msg-dm-3-1",
                    "speaker_slot": "biker_enforcer",
                    "content": "A deafening mechanical roar shattered the cavern wall as {{scenarioChar \"biker_enforcer\"}} breached the collapsed service tunnel on a roaring six-wheel combat rig, his blue skin gleaming with grease and gunpowder smoke. He racked the heavy slide on his shotgun with a feral grin. \"Didn't realize we had comedians getting surrounded in my hallway! Move aside, kids, let the Nomads clear the road!\"",
                },
                {
                    "id": "msg-dm-3-2",
                    "speaker_slot": "tank_frontline",
                    "content": "{{scenarioChar \"tank_frontline\"}} roared as he drove the head of his warhammer into the skull of an oncoming chitin beast, black ichor splattering across his leather chest plate. \"Finally, someone brought enough heavy firepower! Keep the flank covered, Marek!\"",
                },
                {
                    "id": "msg-dm-3-3",
                    "speaker_slot": "eldest_brother",
                    "content": "{{scenarioChar \"eldest_brother\"}} caught an abyssal claw strike on his forearm guard, stepping into the beast's center mass and delivering a devastating elbow strike that shattered its ribcage into fragments.",
                },
                {
                    "id": "msg-dm-3-4",
                    "speaker_slot": "faction_support",
                    "content": "The DMHA tactical strike team fanned out behind the sandbag line, high-caliber mana-suppression rounds whistling through the smoke to pin the remaining crawler swarm into the chasm.",
                },
            ],
        },
        {
            "id": "scene-dmha-horns-debrief",
            "name": "04. The Horns Debrief at Barrow's Stoop",
            "description": "Dawn at The Horns demi-human enclave on Chicago's Southside, wet pavement, fresh coffee, and reflections on community survival.",
            "messages": [
                {
                    "id": "msg-dm-4-1",
                    "speaker_slot": "demihuman_representative",
                    "content": "{{scenarioChar \"demihuman_representative\"}} blew steam from his chipped ceramic coffee mug, his towering minotaur frame leaning against the brick railing of his Southside stoop as the 5:30 AM mist rolled off the wet pavement. \"This block does not hunt ghosts. If someone walks in without hate, they get treated clean. If there is a problem, it comes to me. I handle it. That is all there is to it.\"",
                },
                {
                    "id": "msg-dm-4-2",
                    "speaker_slot": "biker_enforcer",
                    "content": "{{scenarioChar \"biker_enforcer\"}} leaned against his customized chopper parked by the curb, sparking a lighter to ignite a cigarillo. \"The rift is sealed, the bounties are signed, and nobody from our crew ended up in a body bag. That is a clean Friday in my book.\"",
                },
                {
                    "id": "msg-dm-4-3",
                    "speaker_slot": "twin_tech",
                    "content": "{{scenarioChar \"twin_tech\"}} handed an encrypted data drive over to Barrow with a faint smirk. \"Full telemetry of the rift stabilization. The local leyline grid will not surge again for at least six months.\"",
                },
                {
                    "id": "msg-dm-4-4",
                    "speaker_slot": "twin_healer",
                    "content": "{{scenarioChar \"twin_healer\"}} sat on the lower stone step, holding a warm porcelain cup and breathing in the scent of neighborhood bakeries and damp asphalt. \"Thank you for having our backs down there, Barrow. It was good to see everyone make it back home.\"",
                },
            ],
        },
    ]

    for g in greetings:
        g["speaker_slot"] = g["messages"][0]["speaker_slot"]
        g["content"] = g["messages"][0]["content"]
        g["linked_persona_ids"] = []

    return {
        "name": "Svartulfr: DMHA Dungeons (Otherworld Incursions)",
        "display_description": (
            "DMHA Dungeons Arc: Affronta le incursioni nei Dungeon e nelle spaccature dimensionali della Gilda DMHA. "
            "Combina le forze del Team Ukiyo (Radek, Goran, Kian), la potenza motociclistica e urbana degli Ironhorn Nomads (Marek, Barrow) "
            "e l'eccellenza tattica della famiglia Douglas-Bloodmoon (Malachia, Jasper, Alyssa) tra caccia a mostri abissali e patti d'onore metropolitani."
        ),
        "avatar": AVATAR_DMHA_DUNGEONS,
        "tags": ["Dungeon", "DMHA", "Ukiyo", "Raid", "Orc", "Minotaur", "Werewolf", "Urban Fantasy"],
        "visibility": "private",
        "rating": "explicit",
        "scenario": scenario_prompt,
        "startup_script": "",
        "slots": slots,
        "greetings": greetings,
        "lorebook_ids": LOREBOOK_IDS,
        "gallery": [],
        "linked_world_id": "",
    }


# ==============================================================================
# SCENARIO 6: UNDERWORLD SINDACATO
# ==============================================================================
def build_scenario_underworld_sindacato() -> dict:
    slots = [
        {
            "key": "syndicate_boss",
            "label": "Syndicate Boss (Ruaraidh 'Rory' Ballantine)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "syndicate_fixer",
            "label": "Syndicate Fixer (Sullivan 'Sully' Jones)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "sinners_leader",
            "label": "Sinners Leader (Jean-Luc Virtuoso)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "sinners_matriarch",
            "label": "Sinners Matriarch (Alicia Virtuoso)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "sinners_alchemist",
            "label": "Sinners Alchemist (Dr. Arthur Sinclair)",
            "pool": [],
            "unavailable_count": 0,
        },
        {
            "key": "mercenary_tracker",
            "label": "Mercenary Tracker (Ilya Volkov / Vasile Ionescu)",
            "pool": [],
            "unavailable_count": 0,
        },
    ]

    scenario_prompt = (
        "Setting: Los Angeles Supernatural Underworld (Hollywood Hills, Long Beach Port Terminals, Subterranean Laboratories).\n\n"
        "Overview:\n"
        "A clandestine war for territorial and narcotic supremacy rages across Los Angeles between the entrenched Ballantine crime family "
        "and the elusive Sinners syndicate. {{user}} operates as an elite Independent Contractor hired to investigate, track, and dismantle "
        "the illicit supply chain of Ambrosia, an alchemical narcotic engineered by the Sinners to subjugate supernatural minds.\n\n"
        "Cast and Verified Roles:\n"
        "- {{user}}: Independent Contractor POV, hired gun, investigator, or operative caught in the crossfire.\n"
        "- {{scenarioChar \"syndicate_boss\"}} (Ruaraidh 'Rory' Ballantine): 47yo Scottish Dragon Demihuman Hybrid, CEO of Ballantine Imports & Exports, head of the Ballantine Family.\n"
        "- {{scenarioChar \"syndicate_fixer\"}} (Sullivan 'Sully' Jones): 56yo Human underworld fixer, driver, and Rory's veteran enforcer.\n"
        "- {{scenarioChar \"sinners_leader\"}} (Jean-Luc Virtuoso): Strictly verified SPECIES: Human, Telepath. 39yo leader of the Sinners syndicate, CEO of Virtuoso Ventures, ruthless psychic manipulator.\n"
        "- {{scenarioChar \"sinners_matriarch\"}} (Alicia Virtuoso): 28yo British former model, manages the Virtuoso Hollywood Hills estate and public image with cold polish.\n"
        "- {{scenarioChar \"sinners_alchemist\"}} (Dr. Arthur Sinclair): 65yo Human Mutant Chimera (scales, mutated horns, prehensile lizard tail), creator and synthesizer of Ambrosia.\n"
        "- {{scenarioChar \"mercenary_tracker\"}}: Ilya Volkov (28yo Russian werewolf mercenary) or Vasile Ionescu (450yo Romanian monster trapper).\n\n"
        "Invariants:\n"
        "- Jean-Luc Virtuoso is strictly specified as Human, Telepath.\n"
        "- Zero em-dashes anywhere in titles, descriptions, scenario prompt, greetings, or message contents.\n"
        + COMMON_NARRATION_GUIDELINES
    )

    greetings = [
        {
            "id": "scene-underworld-summit",
            "name": "01. Rory's Estate Summit (Ballantine Syndicate Briefing)",
            "description": "Private summit in Rory's fortified study outside Los Angeles, single-malt scotch, antique firearms, and contracting terms.",
            "messages": [
                {
                    "id": "msg-uw-1-1",
                    "speaker_slot": "syndicate_boss",
                    "content": "{{scenarioChar \"syndicate_boss\"}} swirled a glass of vintage single-malt in his scaled, claw-tipped fingers, his dark amber wings folded close against his tailored charcoal suit. His slitted eyes assessed {{user}} across the mahogany desk with calculating composure. \"My import terminals at Long Beach do not run on chaos. The Sinners have been slipping unmarked crates of Ambrosia through my docks, and Jean-Luc Virtuoso seems to believe his telepathy makes him invisible to my ledger. I am hiring you to disabuse him of that illusion.\"",
                },
                {
                    "id": "msg-uw-1-2",
                    "speaker_slot": "syndicate_fixer",
                    "content": "{{scenarioChar \"syndicate_fixer\"}} leaned against the heavy study doorframe in his trench coat, clicking the slide on his concealed pistol with a gravelly voice. \"Rory does not pay for second visits. You find the distribution node at Pier 42, tag the shipment, and pull the plug before the DEA or the DMHA starts sniffing around our warehouses.\"",
                },
                {
                    "id": "msg-uw-1-3",
                    "speaker_slot": "mercenary_tracker",
                    "content": "The tracker laid three black-and-white surveillance photographs onto the desk blotter, showing refrigerated shipping containers stamped with the Virtuoso Ventures logo. \"Sinclair's runners load the trucks at 3:00 AM under cover of harbor fog. If we strike at midnight, we catch their whole logistics chain flat-footed.\"",
                },
            ],
        },
        {
            "id": "scene-underworld-penthouse",
            "name": "02. Sinners Hideout and Ambrosia Vial (Hollywood Hills)",
            "description": "Infiltration of the modernist Hollywood Hills glass mansion, finding the glowing Ambrosia vial, and Jean-Luc's telepathic intrusion.",
            "messages": [
                {
                    "id": "msg-uw-2-1",
                    "speaker_slot": "sinners_leader",
                    "content": "A cool, resonant telepathic whisper echoed directly behind {{user}}'s temples before footsteps even registered on the polished Italian marble. {{scenarioChar \"sinners_leader\"}} stepped from the terrace shadows in an immaculate cream silk suit, his shoulder-length honey-blonde hair framing a predatory smile. \"Admiring the glassware, my friend? Ambrosia is far more than an alchemical tincture. It is clarity. And you are trespassing on private property.\"",
                },
                {
                    "id": "msg-uw-2-2",
                    "speaker_slot": "sinners_matriarch",
                    "content": "{{scenarioChar \"sinners_matriarch\"}} reclined on the white leather chaise lounge with a glass of champagne, her British accent clipped and utterly unbothered by the intruder. \"Tell your employers that Jean-Luc does not negotiate with courier contractors. If you leave through the front gates right now, Sully might still have someone to send home in one piece.\"",
                },
                {
                    "id": "msg-uw-2-3",
                    "speaker_slot": "mercenary_tracker",
                    "content": "Through the tactical earpiece, the tracker's voice hissed sharply from the perimeter hillside. \"Virtuoso has armed private contractors sweeping the garden paths. Grab the vial and head for the lower service staircase now!\"",
                },
            ],
        },
        {
            "id": "scene-underworld-harbor-ambush",
            "name": "03. Harbor Fog Ambush at Molo 42",
            "description": "Gunfire in the dense Pacific fog of Long Beach container yard, flanking enforcers, and Sully's armored SUV extraction.",
            "messages": [
                {
                    "id": "msg-uw-3-1",
                    "speaker_slot": "mercenary_tracker",
                    "content": "A volley of silenced high-caliber rounds sparked against the rusted iron flank of shipping container 402, throwing steel shavings into the dense Pacific fog. The tracker dropped from an overhead crane cable, firing two controlled bursts to suppress the Sinners' flanking squad. \"Take cover behind the container trucks! They brought automated turret rigs to protect the loading bay!\"",
                },
                {
                    "id": "msg-uw-3-2",
                    "speaker_slot": "syndicate_fixer",
                    "content": "Headlights tore through the mist as {{scenarioChar \"syndicate_fixer\"}} rammed an armored SUV through the security gate, tires screeching over wet asphalt. He kicked open the rear passenger door, leveling a shotgun out the window. \"Get in! I am not explaining to Rory why my contractor got turned into Swiss cheese at my own dock!\"",
                },
                {
                    "id": "msg-uw-3-3",
                    "speaker_slot": "syndicate_boss",
                    "content": "Rory Ballantine's deep Scottish baritone crackled through the encrypted radio channel. \"Contain the perimeter, Sully. Let none of Sinclair's vehicles leave the terminal gate. Every vial of Ambrosia on that dock belongs to the Ballantine Family by sunrise.\"",
                },
            ],
        },
        {
            "id": "scene-underworld-sinclair-lab",
            "name": "04. Sinclair's Secret Subterranean Lab",
            "description": "Raid on the subterranean refinery beneath the industrial warehouse, pressurized Ambrosia vats, and Dr. Arthur Sinclair's panic.",
            "messages": [
                {
                    "id": "msg-uw-4-1",
                    "speaker_slot": "sinners_alchemist",
                    "content": "{{scenarioChar \"sinners_alchemist\"}} hissed in violent panic, his green-scaled arms scrambling across the glass distillation tubes as steam hissed from the pressurized stainless steel vats. His prehensile lizard tail lashed nervously against the tile floor. \"Do not touch the release valves, you fools! The compound is unstable! One sudden rupture in the filtration circuit will flood this entire basement with neurotoxic gas!\"",
                },
                {
                    "id": "msg-uw-4-2",
                    "speaker_slot": "sinners_leader",
                    "content": "Jean-Luc Virtuoso's voice broke through the lab's intercom system, icy, detached, and dripping with venom. \"Save your apologies, Doctor. If you allow our guests to secure the master formula, there will not be enough left of you to fit into one of your own specimen jars.\"",
                },
                {
                    "id": "msg-uw-4-3",
                    "speaker_slot": "syndicate_fixer",
                    "content": "{{scenarioChar \"syndicate_fixer\"}} kicked the lab office door off its hinges, a heavy crowbar in his hand as he wrenched the primary emergency purge valve shut. \"Gas threat neutralized. Pack the formula ledgers, contractor. We are shutting down Sinclair's kitchen for good.\"",
                },
                {
                    "id": "msg-uw-4-4",
                    "speaker_slot": "syndicate_boss",
                    "content": "{{scenarioChar \"syndicate_boss\"}} stepped through the breached steel blast doors, his dragon scales gleaming under the sodium emergency lights. He looked down at the cowering alchemist with cold satisfaction. \"Your monopoly is over, Sinclair. Tell Virtuoso his supply in Los Angeles has officially dried up.\"",
                },
            ],
        },
    ]

    for g in greetings:
        g["speaker_slot"] = g["messages"][0]["speaker_slot"]
        g["content"] = g["messages"][0]["content"]
        g["linked_persona_ids"] = []

    return {
        "name": "Svartulfr: Underworld Sindacato (Los Angeles Syndicate War)",
        "display_description": (
            "Underworld Sindacato Arc: Guerra sotterranea tra sindacati a Los Angeles. "
            "{{user}} veste i panni di un Contractor Indipendente ingaggiato dalla famiglia Ballantine (Rory Ballantine e Sully Jones) "
            "per smantellare la rete di distribuzione dell'Ambrosia gestita dal cartello dei Sinners: il leader telepate umano Jean-Luc Virtuoso, "
            "la fredda consorte Alicia e il chimico mutante chimera Dr. Arthur Sinclair."
        ),
        "avatar": AVATAR_UNDERWORLD,
        "tags": ["Underworld", "Crime", "Syndicate", "Ballantine", "Sinners", "Urban Fantasy", "Los Angeles"],
        "visibility": "private",
        "rating": "explicit",
        "scenario": scenario_prompt,
        "startup_script": "",
        "slots": slots,
        "greetings": greetings,
        "lorebook_ids": LOREBOOK_IDS,
        "gallery": [],
        "linked_world_id": "",
    }


# ==============================================================================
# VALIDATION ENGINE
# ==============================================================================
def validate_scenario_payload(sc: dict, filename: str) -> list[str]:
    """Rigorous offline validation against all schema and project invariants."""
    errors = []

    # 1. Root structure and lengths
    name = sc.get("name", "")
    if not (1 <= len(name) <= 200):
        errors.append(f"Name length {len(name)} outside [1, 200]")
    if name != name.strip():
        errors.append("Name is not trimmed")

    desc = sc.get("display_description", "")
    if len(desc) > 20000:
        errors.append(f"display_description length {len(desc)} > 20000")

    prompt = sc.get("scenario", "")
    if len(prompt) > 100000:
        errors.append(f"scenario prompt length {len(prompt)} > 100000")

    # 2. Strict User Directive: visibility MUST BE 'private'
    vis = sc.get("visibility")
    if vis != "private":
        errors.append(f"CRITICAL INVARIANT VIOLATION: visibility is '{vis}', must be 'private'")

    rating = sc.get("rating")
    if rating != "explicit":
        errors.append(f"Rating is '{rating}', expected 'explicit'")

    # 3. Zero em-dashes anywhere in entire JSON
    raw_json = json.dumps(sc, ensure_ascii=False)
    if "—" in raw_json:
        errors.append("CRITICAL INVARIANT VIOLATION: Found em-dash ('—') in payload")
    if "–" in raw_json:
        errors.append("CRITICAL INVARIANT VIOLATION: Found en-dash ('–') in payload")

    # 4. Lorebooks: all 6 must be present
    lb_ids = sc.get("lorebook_ids", [])
    if set(lb_ids) != set(LOREBOOK_IDS) or len(lb_ids) != 6:
        errors.append(f"Invalid lorebook_ids: expected 6 canonical IDs, got {lb_ids}")

    # 5. Slots: 1 to 20, unique keys matching regex, unavailable_count == 0
    slots = sc.get("slots", [])
    if not (1 <= len(slots) <= 20):
        errors.append(f"Slot count {len(slots)} outside [1, 20]")

    slot_keys = set()
    for s_idx, slot in enumerate(slots):
        key = slot.get("key", "")
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$", key):
            errors.append(f"Slot {s_idx} key '{key}' does not match regex ^[a-zA-Z][a-zA-Z0-9_-]{{0,63}}$")
        if key in slot_keys:
            errors.append(f"Duplicate slot key '{key}'")
        slot_keys.add(key)

        label = slot.get("label", "")
        if not (1 <= len(label) <= 120):
            errors.append(f"Slot '{key}' label length {len(label)} outside [1, 120]")

        unavail = slot.get("unavailable_count", 0)
        if unavail != 0:
            errors.append(f"CRITICAL INVARIANT VIOLATION: Slot '{key}' has unavailable_count={unavail}, must be 0")

        pool = slot.get("pool", [])
        for cand in pool:
            if not cand.get("character_id"):
                errors.append(f"Slot '{key}' candidate missing character_id")
            w = cand.get("weight", 0)
            if not (0 <= w <= 1000000):
                errors.append(f"Slot '{key}' candidate weight {w} outside [0, 1000000]")

    # 6. Greetings: 1 to 100, messages 1 to 20
    greetings = sc.get("greetings", [])
    if not (1 <= len(greetings) <= 100):
        errors.append(f"Greeting count {len(greetings)} outside [1, 100]")

    for g_idx, g in enumerate(greetings):
        gid = g.get("id", f"greeting-{g_idx}")
        g_name = g.get("name", "")
        if not (1 <= len(g_name) <= 200):
            errors.append(f"Greeting {gid} name length {len(g_name)} outside [1, 200]")

        msgs = g.get("messages", [])
        if not (1 <= len(msgs) <= 20):
            errors.append(f"Greeting {gid} has {len(msgs)} messages, outside [1, 20]")

        # Multi-message greeting root parity
        if msgs:
            if g.get("content") != msgs[0].get("content"):
                errors.append(f"Greeting {gid} root content != messages[0].content")
            if g.get("speaker_slot") != msgs[0].get("speaker_slot"):
                errors.append(f"Greeting {gid} root speaker_slot != messages[0].speaker_slot")

        for m_idx, m in enumerate(msgs):
            spk = m.get("speaker_slot", "")
            if spk not in slot_keys:
                errors.append(f"Greeting {gid} msg {m_idx} speaker_slot '{spk}' not in slots")
            cnt = m.get("content", "")
            if not (1 <= len(cnt) <= 100000):
                errors.append(f"Greeting {gid} msg {m_idx} content length {len(cnt)} outside [1, 100000]")

            # Check for redundant speaker name prefix (e.g., 'Rory Ballantine: ...')
            if re.match(r"^[A-Z][a-zA-Z\s\.\-']{1,30}:\s*[\"']", cnt):
                errors.append(f"Greeting {gid} msg {m_idx} starts with redundant speaker name prefix: '{cnt[:30]}'")

    # 7. Specific Character Data Invariants
    if filename == "Svartulfr_Scenario_Camp_Mystic.json":
        if len(slots) != 8:
            errors.append(f"Camp Mystic must have 8 slots, got {len(slots)}")
        if "Marcus Vale" not in prompt or "Celeste Nadir" not in prompt:
            errors.append("Camp Mystic prompt missing Marcus Vale or Celeste Nadir")
        if "Mara Voss" not in prompt:
            errors.append("Camp Mystic prompt missing Mara Voss")
        if "13" not in prompt:
            errors.append("Camp Mystic prompt missing Edric 13yo specification")
        if not sc.get("startup_script"):
            errors.append("Camp Mystic missing Lua startup_script")

    elif filename == "Svartulfr_Scenario_SUCC_Route_Alyssa.json":
        if len(slots) != 8:
            errors.append(f"SUCC Alyssa must have 8 slots, got {len(slots)}")
        if len(greetings) != 6:
            errors.append(f"SUCC Alyssa must have 6 greetings, got {len(greetings)}")
        if "Finnegan" not in prompt or "Arctic Wolf demi-human" not in prompt:
            errors.append("SUCC Alyssa prompt missing explicit Arctic Wolf demi-human specification for Finnegan")
        if "Scarlett Rose" not in prompt:
            errors.append("SUCC Alyssa prompt missing Scarlett Rose surname verification")

    elif filename == "Svartulfr_Scenario_SUCC_Route_Jasper.json":
        if len(slots) != 8:
            errors.append(f"SUCC Jasper must have 8 slots, got {len(slots)}")
        if len(greetings) != 5:
            errors.append(f"SUCC Jasper must have 5 greetings, got {len(greetings)}")
        if "Russell" not in prompt or "Sinclair" not in prompt:
            errors.append("SUCC Jasper prompt missing Russell Sinclair surname verification")
        if "Echo" not in prompt:
            errors.append("SUCC Jasper prompt missing Echo specification")

    elif filename == "Svartulfr_Scenario_Villa_Douglas.json":
        if len(slots) != 7:
            errors.append(f"Villa Douglas must have exactly 7 slots, got {len(slots)}")
        if len(greetings) != 5:
            errors.append(f"Villa Douglas must have 5 greetings, got {len(greetings)}")
        for s in slots:
            if not s["pool"] or len(s["pool"]) != 1 or s["pool"][0]["weight"] != 100:
                errors.append(f"Villa Douglas slot '{s['key']}' must have exactly 1 card in pool with weight 100")

    elif filename == "Svartulfr_Scenario_DMHA_Dungeons.json":
        if len(slots) != 9:
            errors.append(f"DMHA Dungeons must have exactly 9 slots, got {len(slots)}")
        if len(greetings) != 4:
            errors.append(f"DMHA Dungeons must have 4 greetings, got {len(greetings)}")
        req_keys = {"twin_healer", "twin_tech", "eldest_brother", "demihuman_representative", "biker_enforcer", "raid_leader", "tank_frontline", "scout_infiltrator", "faction_support"}
        if set(slot_keys) != req_keys:
            errors.append(f"DMHA Dungeons slot keys mismatch: {set(slot_keys)} != {req_keys}")

    elif filename == "Svartulfr_Scenario_Underworld_Sindacato.json":
        if len(slots) != 6:
            errors.append(f"Underworld Sindacato must have exactly 6 slots, got {len(slots)}")
        if len(greetings) != 4:
            errors.append(f"Underworld Sindacato must have 4 greetings, got {len(greetings)}")
        if "Human, Telepath" not in prompt:
            errors.append("Underworld Sindacato prompt missing explicit 'Human, Telepath' for Jean-Luc Virtuoso")

    return errors


# ==============================================================================
# BUILD AND SAVE ALL 6 SCENARIOS
# ==============================================================================
def build_all_scenarios() -> dict[str, dict]:
    scenarios = {
        "Svartulfr_Scenario_Camp_Mystic.json": build_scenario_camp_mystic(),
        "Svartulfr_Scenario_SUCC_Route_Alyssa.json": build_scenario_succ_alyssa(),
        "Svartulfr_Scenario_SUCC_Route_Jasper.json": build_scenario_succ_jasper(),
        "Svartulfr_Scenario_Villa_Douglas.json": build_scenario_villa_douglas(),
        "Svartulfr_Scenario_DMHA_Dungeons.json": build_scenario_dmha_dungeons(),
        "Svartulfr_Scenario_Underworld_Sindacato.json": build_scenario_underworld_sindacato(),
    }

    FINAL_SCENARIOS_DIR.mkdir(parents=True, exist_ok=True)

    print("=== BUILDING AND VALIDATING 6 THEMATIC SCENARIOS ===")
    all_passed = True
    for fname, payload in scenarios.items():
        # Sanitize zero em-dashes
        clean_payload = sanitize_recursively(payload)
        scenarios[fname] = clean_payload

        # Run validation
        errs = validate_scenario_payload(clean_payload, fname)
        if errs:
            all_passed = False
            print(f"[FAIL] {fname}:")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"[PASS] {fname} validated 100% against all invariants!")

        # Save to disk
        out_path = FINAL_SCENARIOS_DIR / fname
        out_path.write_text(json.dumps(clean_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"       Saved to: {out_path.relative_to(ROOT)} (size: {out_path.stat().st_size} bytes)")

    if not all_passed:
        raise RuntimeError("Validation failed on one or more scenarios! Deployment aborted.")

    print("\nAll 6 scenario payloads successfully generated and validated!")
    return scenarios


# ==============================================================================
# WYVERN API DEPLOYMENT
# ==============================================================================
def get_auth_token() -> str:
    if not TOKEN_FILE.exists():
        print("wyvern_token.txt not found, running refresh...")
        import subprocess
        subprocess.run([sys.executable, str(REFRESH_SCRIPT)], check=True)

    token = TOKEN_FILE.read_text(encoding="utf-8").strip()
    return token

def deploy_scenarios(scenarios: dict[str, dict]) -> dict[str, str]:
    token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }

    deployed_ids = {}
    print("\n=== DEPLOYING 6 SCENARIOS TO WYVERN WEB API ===")

    for idx, (fname, payload) in enumerate(scenarios.items(), 1):
        print(f"\n[{idx}/6] Deploying {fname} ({payload['name']})...")

        # Format body payload for POST
        post_body = {
            "name": payload["name"],
            "display_description": payload.get("display_description", ""),
            "avatar": payload.get("avatar", ""),
            "tags": payload.get("tags", []),
            "visibility": "private",  # Strictly "private"
            "rating": payload.get("rating", "explicit"),
            "scenario": payload.get("scenario", ""),
            "startup_script": payload.get("startup_script", ""),
            "slots": payload.get("slots", []),
            "greetings": payload.get("greetings", []),
            "lorebook_ids": payload.get("lorebook_ids", []),
            "gallery": payload.get("gallery", []),
            "linked_world_id": payload.get("linked_world_id", ""),
        }

        body_bytes = json.dumps(post_body, ensure_ascii=False).encode("utf-8")
        req_post = urllib.request.Request(
            f"{API_BASE}/character-scenarios",
            data=body_bytes,
            headers=headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(req_post) as resp:
                if resp.status not in (200, 201):
                    raise RuntimeError(f"Unexpected status: {resp.status}")
                res_data = json.loads(resp.read().decode("utf-8"))
                new_id = res_data.get("id") or res_data.get("_id") or res_data.get("scenario", {}).get("id")
                print(f"  -> SUCCESS! HTTP {resp.status} - Generated Scenario ID: {new_id}")
                deployed_ids[fname] = new_id

                # Update the local file with assigned ID
                payload["id"] = new_id
                out_path = FINAL_SCENARIOS_DIR / fname
                out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8", errors="replace")
            print(f"  -> HTTP ERROR {e.code}: {err_msg}")
            # If token expired (401), try one refresh
            if e.code == 401:
                print("Token expired. Refreshing...")
                import subprocess
                subprocess.run([sys.executable, str(REFRESH_SCRIPT)], check=True)
                token = TOKEN_FILE.read_text(encoding="utf-8").strip()
                headers["Authorization"] = f"Bearer {token}"
                print("Retrying POST...")
                req_post = urllib.request.Request(
                    f"{API_BASE}/character-scenarios",
                    data=body_bytes,
                    headers=headers,
                    method="POST",
                )
                with urllib.request.urlopen(req_post) as resp2:
                    res_data = json.loads(resp2.read().decode("utf-8"))
                    new_id = res_data.get("id") or res_data.get("_id") or res_data.get("scenario", {}).get("id")
                    print(f"  -> SUCCESS ON RETRY! HTTP {resp2.status} - Generated Scenario ID: {new_id}")
                    deployed_ids[fname] = new_id
                    payload["id"] = new_id
                    out_path = FINAL_SCENARIOS_DIR / fname
                    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
            else:
                raise

        # Required 2.5s pacing delay
        print("  -> Waiting 2.5s pacing delay...")
        time.sleep(2.5)

    print("\n=== VERIFYING DEPLOYED SCENARIOS VIA GET API ===")
    for fname, scen_id in deployed_ids.items():
        req_get = urllib.request.Request(
            f"{API_BASE}/character-scenarios/{scen_id}",
            headers=headers,
            method="GET",
        )
        with urllib.request.urlopen(req_get) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            v_name = data.get("name")
            v_slots = len(data.get("slots", []))
            v_greetings = len(data.get("greetings", []))
            v_lbs = len(data.get("lorebook_ids", []))
            v_vis = data.get("visibility")
            print(f"[VERIFIED] {scen_id} ({fname})")
            print(f"           Name: '{v_name}' | Visibility: '{v_vis}' | Slots: {v_slots} | Greetings: {v_greetings} | Lorebooks: {v_lbs}")
            assert v_vis == "private", f"Verification failed: visibility is '{v_vis}', expected 'private'"

    return deployed_ids


def verify_deployed_scenarios():
    token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }
    print("=== LIVE GET VERIFICATION OF ALL 6 SCENARIOS ===")
    for json_file in sorted(FINAL_SCENARIOS_DIR.glob("*.json")):
        local_data = json.loads(json_file.read_text(encoding="utf-8"))
        scen_id = local_data.get("id")
        assert scen_id, f"File {json_file.name} missing 'id' field!"
        req_get = urllib.request.Request(
            f"{API_BASE}/character-scenarios/{scen_id}",
            headers=headers,
            method="GET",
        )
        with urllib.request.urlopen(req_get) as resp:
            assert resp.status == 200, f"HTTP {resp.status} on {scen_id}"
            data = json.loads(resp.read().decode("utf-8"))
            v_name = data.get("name")
            v_slots = len(data.get("slots", []))
            v_greetings = len(data.get("greetings", []))
            v_lbs = len(data.get("lorebook_ids", []))
            v_vis = data.get("visibility")
            print(f"[200 OK] {scen_id} -> '{v_name}'")
            print(f"         Visibility: '{v_vis}' | Slots: {v_slots} | Greetings: {v_greetings} | Lorebooks: {v_lbs}")
            assert v_vis == "private", f"Invariant failed: visibility is '{v_vis}' (must be 'private')"
            assert v_lbs == 6, f"Invariant failed: lorebook_ids count {v_lbs} != 6"


if __name__ == "__main__":
    is_dry_run = "--dry-run" in sys.argv
    is_verify_only = "--verify-only" in sys.argv or "--verify" in sys.argv
    do_deploy = ("--deploy" in sys.argv or "-d" in sys.argv) and not is_dry_run and not is_verify_only

    if is_verify_only:
        verify_deployed_scenarios()
    else:
        scenarios = build_all_scenarios()
        if do_deploy:
            deployed_ids = deploy_scenarios(scenarios)
            print("\nAll 6 scenarios deployed and verified live!")
            for fn, sid in deployed_ids.items():
                print(f"  {fn} -> {sid}")
        elif is_dry_run:
            print("\nDry-run complete: All 6 scenarios validated and saved locally (no API calls).")
        else:
            print("\nRun with --deploy to deploy, --dry-run for offline check, or --verify-only for live API check.")


