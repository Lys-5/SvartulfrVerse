import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

ALYSSA_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json'
JASPER_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json'

# The 8 existing Character Cards in /characters/mine:
# 1. Jasper Svartr Douglas Bloodmoon (_t4J9aQNJM36cUKAP4wB4U)
# 2. Erik Ulfr Douglas (_QPea6g4Q1QfeYCVHCLMPR)
# 3. Logan Járn Douglas (_T8Ywcr9FEqNf9JxbK6eHP)
# 4. Malachia Björn Douglas Bloodmoon (_RDfz7XzTpM23LpPALVXHM)
# 5. Noah Loki Douglas Bloodmoon (_zFLUjV8aVxQRAfQxGcAcY)
# 6. Edric Douglas (_TbRM3EdxDjHFgqztTbCpL)
# 7. Wulfnic Báleygr Bloodmoon (_HEQQbbRFwKdG8QE2Fh1z1)
# 8. Mackenzie Sanchez-Rogers (_zn24784jfcchQ7EwCyAnm)

CANONICAL_8_SLOTS_ALYSSA = [
    {
        "key": "twin",
        "label": "Twin Brother (Jasper Svartr Douglas Bloodmoon)",
        "pool": [{"character_id": "_t4J9aQNJM36cUKAP4wB4U", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "crush",
        "label": "Crush (Mackenzie 'Mac' Sanchez-Rogers)",
        "pool": [{"character_id": "_zn24784jfcchQ7EwCyAnm", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "father",
        "label": "Father (Erik Ulfr Douglas)",
        "pool": [{"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "eldest_brother",
        "label": "Eldest Brother (Malachia Björn Douglas Bloodmoon)",
        "pool": [{"character_id": "_RDfz7XzTpM23LpPALVXHM", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "brother",
        "label": "Brother (Noah Loki Douglas Bloodmoon)",
        "pool": [{"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "uncle",
        "label": "Uncle (Logan Járn Douglas)",
        "pool": [{"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "cousin",
        "label": "Cousin (Edric Douglas)",
        "pool": [{"character_id": "_TbRM3EdxDjHFgqztTbCpL", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "maternal_grandfather",
        "label": "Maternal Grandfather (Wulfnic Báleygr Bloodmoon)",
        "pool": [{"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "weight": 100}],
        "unavailable_count": 0
    }
]

# In Jasper Route, {{user}} is Jasper (or if someone plays alongside Jasper, we include only the existing cards; 7 or 8 slots all mapped to the existing cards):
CANONICAL_SLOTS_JASPER = [
    {
        "key": "father",
        "label": "Father (Erik Ulfr Douglas)",
        "pool": [{"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "eldest_brother",
        "label": "Eldest Brother (Malachia Björn Douglas Bloodmoon)",
        "pool": [{"character_id": "_RDfz7XzTpM23LpPALVXHM", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "brother",
        "label": "Brother (Noah Loki Douglas Bloodmoon)",
        "pool": [{"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "uncle",
        "label": "Uncle (Logan Járn Douglas)",
        "pool": [{"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "cousin",
        "label": "Cousin (Edric Douglas)",
        "pool": [{"character_id": "_TbRM3EdxDjHFgqztTbCpL", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "maternal_grandfather",
        "label": "Maternal Grandfather (Wulfnic Báleygr Bloodmoon)",
        "pool": [{"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "weight": 100}],
        "unavailable_count": 0
    },
    {
        "key": "band_peer",
        "label": "Band Keyboardist & Dealer (Mackenzie 'Mac' Sanchez-Rogers)",
        "pool": [{"character_id": "_zn24784jfcchQ7EwCyAnm", "weight": 100}],
        "unavailable_count": 0
    }
]

def update_alyssa_scenario():
    with open(ALYSSA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data['slots'] = CANONICAL_8_SLOTS_ALYSSA

    # Update scenario text so Cast & Verified Roles reflects the 8 active Character Card slots + Lorebook NPCs
    data['scenario'] = (
        "Setting: Solarton University and College Campus (SUCC), Solarton, California (Fall Semester 2024).\n\n"
        "Overview:\n"
        "Alyssa Hvit Douglas Bloodmoon embarks on her freshman year at SUCC as a Pre-Med student specializing in botanical remedies, restorative magic, and clinical anatomy. Residing at the Theta Iota Theta sorority house on Greek Row, her life balances academic rigor, sorority sisterhood, hospital internships at Aetheris Clinic, and collegiate drama across athletics, indie music, and supernatural factions.\n\n"
        "Active Character Card Slots (The 8 Existing Cards):\n"
        "- {{user}}: Alyssa Hvit Douglas Bloodmoon, 19yo Dominant Omega, White Moon healer, pacifist vow, carrying her dimensional pochette.\n"
        "- {{scenarioChar \"twin\"}} (Jasper Svartr Douglas Bloodmoon): 19yo Beta technomancer, twin brother, campus netrunner, and protective shadow.\n"
        "- {{scenarioChar \"crush\"}} (Mackenzie 'Mac' Sanchez-Rogers): 19yo synth musician for Grave Mistake / Sidewinders, pureblood Rogers wolf lineage, charismatic campus weed dealer and Alyssa's romantic interest.\n"
        "- {{scenarioChar \"father\"}} (Erik Ulfr Douglas): 55yo Prime Alpha Pack Leader of House Douglas and CEO of the Douglas Commercial Coalition (DCC).\n"
        "- {{scenarioChar \"eldest_brother\"}} (Malachia Björn Douglas Bloodmoon): 28yo Dominant Alpha, undefeated heavyweight fighter, senior student and protective shield.\n"
        "- {{scenarioChar \"brother\"}} (Noah Loki Douglas Bloodmoon): 25yo Delta diplomat, KSA President at SUCC, corporate strategist.\n"
        "- {{scenarioChar \"uncle\"}} (Logan Járn Douglas): 49yo Beta peacemaker, master mechanic and owner of The Verve.\n"
        "- {{scenarioChar \"cousin\"}} (Edric Douglas): 13yo Pre-Presentation Gamma pup, gamer, and sharp-tongued younger cousin.\n"
        "- {{scenarioChar \"maternal_grandfather\"}} (Wulfnic Báleygr Bloodmoon): 1200yo Primordial Firstborn Jarl of the Sacred Forest.\n\n"
        "SUCC Campus Circle (Lorebook NPCs with Automatic Avatar & Name Splitting):\n"
        "- Zefir Hvitskog: 1176yo Primordial Firstborn Enigma (looks 20-22 to modern eyes), enrolled at SUCC by Wulfnic to protect Alyssa under the cover of a distant cousin from Iceland (justifying his thick Old Norse accent and limited written English), sporting a snow-white mohawk and a studded black leather punk jacket.\n"
        "- Scarlett Rose: 20yo Succubus demi-human, verified surname Rose, candy-pink (rosa confetto) hair and matching candy-pink eyes, with two sleek scarlet horns protruding through her hair above her temples, dark succubus wings, and a spade-tipped tail. Botany and fine arts major, social coordinator, and Alyssa's loyal confidante.\n"
        "- Sierra Cruz: 18yo Lamia (serpentine) demi-human, Theta Iota Theta sister and Applied Necromancy major. She has rainbow-colored hair and a massive 4-meter rainbow-colored serpentine tail with iridescent scales from the hips down (zero human legs, zero feet; she slithers, glides, and coils to move, never walks or steps).\n"
        "- Finnegan 'Finn' Novak: Strictly verified Arctic Wolf demi-human (Kemonomimi). He possesses exactly ONE single pair of ears (white wolf ears atop his skull, zero human ears) and a white tail. He is a non-shifter, has zero werewolf birth runes, and zero shifting ability. SUCC Bears left-wing hockey star and Alpha Rho Omega brother.\n"
        "- Jared Thompson: 22yo Half-Minotaur / Golden Retriever werewolf jock, star quarterback for SUCC Bulls, BRO fraternity member.\n"
        "- Stanley 'Stan' Davies Jr.: 21yo pre-med and chemistry scholar, Jared's sarcastic roommate at Wyrm Hall.\n"
        "- Vincent Campbell: Montreal vampire aristocrat, captain and centre of SUCC Bears hockey, Alpha Sigma Sigma president.\n\n"
        "Invariants:\n"
        "- Zefir Hvitskog is enrolled at SUCC by Wulfnic to protect Alyssa under the cover of a distant cousin from Iceland (justifying his thick Old Norse accent and limited written English), sporting a snow-white mohawk and a studded black leather punk jacket.\n"
        "- Finnegan Novak is explicitly specified as an Arctic Wolf demi-human (one pair of animal ears, non-shifter).\n"
        "- Scarlett Rose and Russell Sinclair surnames are canonical and verified.\n\n\n"
        "[NARRATION GUIDELINES & ANTI-VENTRILOQUISM:\n"
        "1. Strict Anti-Ventriloquism: Never speak, think, emote, or act for {{user}}. Pause and wait for {{user}}'s input.\n"
        "2. Scene Balancing: Balance active scene characters naturally according to their canonical JED+ voice, attitudes, and pack hierarchies.\n"
        "3. Format Discipline: Dialogue in quotes (\"...\"), actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only (*...*). Never use the em dash; use commas or periods instead.\n"
        "4. Demi-Human & Werewolf Anatomy: Demi-humans and Werewolves in Partial Shift possess ONLY ONE PAIR OF EARS (their animal ears atop their skull, zero human ears).\n"
        "5. NPC Formatting Discipline: When Lorebook NPCs (such as Scarlett Rose, Sierra Cruz, Finnegan Novak, Zefir Hvitskog, Jared Thompson, Stanley Davies Jr., Vincent Campbell, or Russell Sinclair) speak, ALWAYS format their dialogue on a new line prefixed with their exact full name and a colon (e.g., 'Scarlett Rose: \"...\"'). Never blend NPC dialogue anonymously into narration.\n"
        "6. Lamia Locomotion & Scarlett Anatomy Invariant: Sierra Cruz is a Lamia whose lower body from the hips down is entirely a rainbow-colored serpentine tail covered in iridescent scales; she has NO legs and NO feet, so NEVER use terms like legs, feet, knees, shoes, walking, or stepping for Sierra (she slithers, glides, and coils on her tail). Scarlett Rose has candy-pink (rosa confetto) hair, matching candy-pink eyes, and scarlet horns protruding through her hair.]"
    )

    # Update all greetings in Alyssa Route so every message uses ONLY valid slots from CANONICAL_8_SLOTS_ALYSSA
    valid_alyssa_slots = {s['key'] for s in CANONICAL_8_SLOTS_ALYSSA}

    # Greeting 0: SUCC Welcome Day
    g0 = data['greetings'][0]
    g0['messages'][0]['speaker_slot'] = 'twin'
    g0['messages'][1]['speaker_slot'] = 'maternal_grandfather'
    g0['messages'][1]['content'] = (
        "The chatter along the central promenade parted in a wave of stunned silence as {{scenarioChar \"maternal_grandfather\"}} strode onto "
        "the Lunar Quad with Zefir Hvitskog at his side. The twelve-hundred-year-old Jarl of Svartúlfr wore his favorite gag outfit "
        "with solemn, chest-out pride: an oversized black cotton t-shirt gifted by Jasper, its back emblazoned in bold white block "
        "letters with a dense, itemized list of Rules for Dating My Granddaughter, paired with dark jeans slit for his silver wolf tail, "
        "heavy buckled biker boots, and an ancient twisted silver torque at his throat. Beside him, Zefir looked every bit a twenty-something "
        "punk rebel: his snow-white hair was shaved on the sides into a sharp mohawk, and he wore a heavy black leather jacket bristling "
        "with silver studs over a torn black tank top and shredded skinny jeans, carrying an orientation packet folded in one tattooed hand.\n"
        "\"After all, you have never been to school, and technically you are still a kid!\" "
        "Wulfnic boomed in English, throwing his head back with a thunderous, resonant laugh as he clapped a heavy hand onto Zefir's studded shoulder.\n"
        "\"Do not look so surprised, Erik! To make sure our little Alyssa is properly guarded on campus, I enrolled Zefir at the university too. As far as the registrar is concerned, he is your distant cousin who just flew in from Iceland. That explains his thick Norse accent and why his written English still looks like runic scratchings.\"\n"
        "Zefir Hvitskog: \"Laugh all you want, my Jarl, but if some pompous professor waves a piece of chalk in my face, I am not promising I will keep the chalk whole,\" "
        "Zefir shot back with a wicked, cocky grin, the lively swagger of the sixteen-year-old Viking he once was dancing in his pale ice-blue eyes "
        "like a capricious gust of North Sea wind before he tipped a mocking two-finger salute toward {{user}} and Jasper.\n"
        "Zefir Hvitskog: \"Relax, little cousin. Your Icelandic relative is officially an undergraduate now. Point me at whoever looks at you sideways and they will vanish before the bell rings.\""
    )
    g0['messages'][2]['speaker_slot'] = 'twin'
    g0['messages'][2]['content'] = (
        "Finnegan Novak cut through the flow of orientation traffic from the athletics pavilion with his "
        "Bears varsity jacket slung over one shoulder, arriving right alongside Scarlett Rose and Sierra Cruz. "
        "To keep the three campus friends from getting put on edge around a Firstborn, the family immediately introduced Zefir under his cover story "
        "as their distant cousin who had just flown in from Iceland for his freshman year. Because Zefir had completely suppressed his divine Enigma aura, "
        "to their senses he registered as nothing more than an ordinary, unremarkable werewolf in a punk leather jacket, yet Finn's posture immediately "
        "stiffened. His single pair of white wolf ears flattened slightly atop his head, with no human ears beneath them, as an inexplicable primal instinct "
        "left him feeling oddly outclassed by the lean Icelandic stranger, driving him to puff out his chest and try to look cooler in front of {{user}}.\n"
        "Finnegan Novak: \"Took me twenty minutes to dodge the scouts by the arena, Alyssa. Coach already has me slated for first-line ice time in the season opener, so if your cousin from Iceland ever wants front-row glass seats to see how real collegiate hockey is played here, I can hook him up,\" "
        "Finn said, leaning casually against the stone balustrade and flexing his forearm as he adjusted his varsity collar.\n"
        "Sierra Cruz: \"Okay, wait, forget hockey for a second, where did you get that jacket?\" "
        "Sierra asked, her rainbow-colored hair catching the sun as she slithered right up to Zefir on her massive rainbow-colored serpentine tail, its iridescent scales shimmering against the stone pavement while her candy-pink eyes widened with genuine fashion envy at the heavy silver studs along his black leather lapels.\n"
        "Sierra Cruz: \"The distressing on the leather and those custom spikes look vintage European. Is there some underground boutique in Reykjavik I need to know about?\"\n"
        "Scarlett Rose: \"Honestly, I think the Icelandic punk look is exactly what this quad was missing,\" "
        "Scarlett purred with a slow, flirtatious smile, her candy-pink hair framing the sleek scarlet horns protruding above her temples and her matching candy-pink eyes sparkling from beneath her lashes as her spade-tipped tail swayed playfully behind her.\n"
        "Scarlett Rose: \"Welcome to Solarton, Zefir. Since your English reading is still rusty, I would be more than happy to give you some private tutoring after convocation. Come on, Alyssa, Wolfwood is stepping up to the microphone.\""
    )
    g0['speaker_slot'] = g0['messages'][0]['speaker_slot']
    g0['content'] = g0['messages'][0]['content']

    # Greeting 1: 01. Theta Iota Theta Morning on Greek Row
    g1 = data['greetings'][1]
    g1['messages'][0]['speaker_slot'] = 'twin'
    g1['messages'][0]['content'] = (
        "Sierra Cruz coiled her long, rainbow-scaled serpentine tail in front of the full-length mirror in the Theta Iota Theta suite, her iridescent scales "
        "shimmering in the morning light as she brushed back a lock of rainbow-colored hair and checked her phone calendar.\n"
        "Sierra Cruz: \"If we slither out in ten minutes, we can grab iced matcha before the lecture hall fills up. Professor Vance locked the front doors at five past eight on Monday.\""
    )
    g1['messages'][1]['speaker_slot'] = 'twin'
    g1['messages'][1]['content'] = (
        "Down on the street below, the screen door of the Alpha Rho Omega house creaked open. Finnegan Novak stepped onto the porch in a grey athletic hoodie, "
        "his single pair of white wolf ears flicking atop his head as his red eyes caught sight of the sorority steps. He straightened up, hesitated for a split second, then lifted a casual hand before turning toward the campus athletic fields.\n"
        "Finnegan Novak: \"Do not be late for morning lab, Alyssa! Save me a spot at the commons for lunch!\""
    )
    g1['messages'][2]['speaker_slot'] = 'twin'
    g1['speaker_slot'] = 'twin'
    g1['content'] = g1['messages'][0]['content']

    # Greeting 2: 02. Pre-Med Biology Labs
    g2 = data['greetings'][2]
    g2['messages'][0]['speaker_slot'] = 'twin'
    g2['messages'][0]['content'] = (
        "Scarlett Rose rested her sketchpad beside a tray of botanical specimens, her pencil rendering the delicate vein structure of a silverleaf fern. "
        "Her candy-pink waves and the sleek scarlet horns peeking through her hair caught the white overhead light as her matching candy-pink eyes crinkled in a warm smile.\n"
        "Scarlett Rose: \"Professor Vance said if we finish the cellular titration before noon, we can take the leftover culture plates to the greenhouse. I already prepared the slides for your section.\""
    )
    g2['messages'][1]['speaker_slot'] = 'twin'
    g2['messages'][1]['content'] = (
        "Stanley Davies Jr. adjusted his wire-rimmed glasses, double-checking the spectrometer readings on the resin bench with a sigh.\n"
        "Stanley Davies Jr.: \"If by titration you mean actual chemistry and not Jared's idea of mixing protein powder into distilled water, we might actually maintain our grade averages.\""
    )
    g2['messages'][2]['speaker_slot'] = 'twin'
    g2['speaker_slot'] = 'twin'
    g2['content'] = g2['messages'][0]['content']

    # Greeting 3: 03. Basilica Library Sheltered Smoking Corner
    g3 = data['greetings'][3]
    g3['messages'][0]['speaker_slot'] = 'crush'
    g3['messages'][1]['speaker_slot'] = 'crush'
    g3['messages'][1]['content'] = (
        "Scarlett Rose walked down the stone stairs carrying two iced coffees, her candy-pink hair bouncing around her sleek scarlet horns as she caught the exchange with a subtle, delighted grin in her candy-pink eyes.\n"
        "Scarlett Rose: \"I told her fresh air was mandatory. You playing at the Dockside venue this Friday, Mac?\""
    )
    g3['messages'][2]['speaker_slot'] = 'twin'
    g3['speaker_slot'] = 'crush'
    g3['content'] = g3['messages'][0]['content']

    # Greeting 4: 04. Ice Rink Bears Practice Clash
    g4 = data['greetings'][4]
    g4['messages'][0]['speaker_slot'] = 'brother'
    g4['messages'][0]['content'] = (
        "Vincent Campbell gathered a breakout pass at the centre circle, his black ponytail swaying as he roofed a wrist shot into the top shelf with effortless grace. "
        "He skated past the glass with a condescending smirk, tossing a sharp remark in French that echoed off the cold arena rafters.\n"
        "Vincent Campbell: \"Try keeping your skates under you this period, puppies. The ice belongs to the first line.\""
    )
    g4['messages'][1]['speaker_slot'] = 'brother'
    g4['messages'][1]['content'] = (
        "Finnegan Novak barrelled into the neutral zone corner with brutal acceleration, slamming his shoulder into the glass with a thunderous rattle that sprayed ice shavings into the bleachers. "
        "His single pair of white wolf ears pinned back atop his head, his white wolf tail stiff with anger, and his red eyes blazed as he glared at the vampire captain while {{scenarioChar \"brother\"}} skated between them to keep order.\n"
        "Finnegan Novak: \"Say that again without the referee standing between us, Campbell!\""
    )
    g4['messages'][2]['speaker_slot'] = 'eldest_brother'
    g4['messages'][2]['content'] = (
        "Jared Thompson stood near the tunnel railing in his football warm-ups alongside {{scenarioChar \"eldest_brother\"}}, cupping his hands around his mouth to boom over the refrigeration hum.\n"
        "Jared Thompson: \"Keep your heads in the play, boys! We have league scouts in the stands on Friday!\""
    )
    g4['speaker_slot'] = 'brother'
    g4['content'] = g4['messages'][0]['content']

    # Greeting 5: 05. Bulls Locker Room and Stadium Tunnel
    g5 = data['greetings'][5]
    g5['messages'][0]['speaker_slot'] = 'eldest_brother'
    g5['messages'][0]['content'] = (
        "Jared Thompson towered in his gold-and-black practice jersey outside the weight room where {{scenarioChar \"eldest_brother\"}} was wrapping his knuckles, shoulder pads still strapped across his chest and a damp towel around his neck.\n"
        "Jared Thompson: \"Hey, Alyssa! Tell me you brought the biochemistry lecture notes. Coach said if my midterm grade drops below a B, he is benching me for the first quarter on homecoming.\""
    )
    g5['messages'][1]['speaker_slot'] = 'twin'
    g5['messages'][1]['content'] = (
        "Stanley Davies Jr. leaned against the concrete wall beside {{scenarioChar \"twin\"}}, clutching his binder with a deadpan expression.\n"
        "Stanley Davies Jr.: \"What Jared means is that he cannot tell an amine from an ester, and I refuse to spend another three hours explaining basic carbon bonds to a quarterback.\""
    )
    g5['messages'][2]['speaker_slot'] = 'twin'
    g5['messages'][2]['content'] = (
        "Sierra Cruz glided past along the smooth concrete floor on her rainbow-colored serpentine coils, her iridescent scales whispering softly as she carried a bundle of campus banners and shook her rainbow-haired head with a laugh.\n"
        "Sierra Cruz: \"Help him out, Lys. If the Bulls lose the opening game, Greek Row will be in mourning for two weeks straight.\""
    )
    g5['speaker_slot'] = 'eldest_brother'
    g5['content'] = g5['messages'][0]['content']

    # Greeting 6: 06. Sidewinders Concert at The Dockside Venue
    g6 = data['greetings'][6]
    g6['messages'][0]['speaker_slot'] = 'crush'
    g6['messages'][1]['speaker_slot'] = 'crush'
    g6['messages'][1]['content'] = (
        "Scarlett Rose danced beside {{user}}, her candy-pink hair and sleek scarlet horns glowing under the neon lights as she laughed over the pounding bass and raised her plastic cup toward the stage.\n"
        "Scarlett Rose: \"I told you his solo was worth the walk downtown! Look at the crowd, the entire campus showed up tonight!\""
    )
    g6['messages'][2]['speaker_slot'] = 'twin'
    g6['speaker_slot'] = 'crush'
    g6['content'] = g6['messages'][0]['content']

    # Verify all speaker_slots in Alyssa Route are in valid_alyssa_slots
    for g in data['greetings']:
        assert g['speaker_slot'] in valid_alyssa_slots, f"Invalid greeting speaker_slot {g['speaker_slot']} in {g['id']}"
        assert g['speaker_slot'] == g['messages'][0]['speaker_slot']
        assert g['content'] == g['messages'][0]['content']
        for m in g['messages']:
            assert m['speaker_slot'] in valid_alyssa_slots, f"Invalid message speaker_slot {m['speaker_slot']} in {m['id']}"
            assert '—' not in m['content'], f"Em-dash in {m['id']}"
            assert '*' not in m['content'], f"Asterisk in {m['id']}"

    with open(ALYSSA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Updated {ALYSSA_PATH.name} with 8 existing card slots only!")

def update_jasper_scenario():
    with open(JASPER_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data['slots'] = CANONICAL_SLOTS_JASPER
    valid_jasper_slots = {s['key'] for s in CANONICAL_SLOTS_JASPER}

    data['scenario'] = (
        "Setting: Solarton University and College Campus (SUCC), Wyrm Hall Suite 304, Solarton, California (Fall Semester 2024).\n\n"
        "Overview:\n"
        "Jasper Svartr Douglas Bloodmoon navigates freshman life as an Arcane Engineering student, underground DJ (DJ Frequency), and rogue netrunner. Residing in Wyrm Hall Suite 304 with tattoo artist Russell Sinclair and the Cocketeers crew (Dean, Eric, Javier, Raymond), Jasper monitors campus servers, executes rooftop antenna hacks, DJs subterranean warehouse raves, and protects his twin sister Alyssa.\n\n"
        "Active Character Card Slots (Existing Cards Only):\n"
        "- {{user}}: Jasper Svartr Douglas Bloodmoon, 19yo Founding Beta, Technomancer, DJ Frequency, and cyber sentinel.\n"
        "- {{scenarioChar \"father\"}} (Erik Ulfr Douglas): 55yo Prime Alpha Pack Leader of House Douglas and CEO of DCC.\n"
        "- {{scenarioChar \"eldest_brother\"}} (Malachia Björn Douglas Bloodmoon): 28yo Dominant Alpha, undefeated fighter and senior protector.\n"
        "- {{scenarioChar \"brother\"}} (Noah Loki Douglas Bloodmoon): 25yo Delta diplomat, KSA President at SUCC.\n"
        "- {{scenarioChar \"uncle\"}} (Logan Járn Douglas): 49yo Beta peacemaker and owner of The Verve.\n"
        "- {{scenarioChar \"cousin\"}} (Edric Douglas): 13yo Pre-Presentation Gamma pup and gamer cousin.\n"
        "- {{scenarioChar \"maternal_grandfather\"}} (Wulfnic Báleygr Bloodmoon): 1200yo Primordial Firstborn Jarl of the Sacred Forest.\n"
        "- {{scenarioChar \"band_peer\"}} (Mackenzie 'Mac' Sanchez-Rogers): 19yo synth musician and campus dealer.\n\n"
        "SUCC Campus Circle (Lorebook NPCs with Automatic Avatar & Name Splitting):\n"
        "- Alyssa Hvit Douglas Bloodmoon: 19yo Dominant Omega, pre-med botanist, Jasper's twin sister.\n"
        "- Zefir Hvitskog: 1176yo Primordial Firstborn Enigma (looks 20-22 to modern eyes), enrolled at SUCC by Wulfnic to protect Alyssa under the cover of a distant cousin from Iceland, sporting a snow-white mohawk and a studded black leather punk jacket.\n"
        "- Russell 'Russ' Sinclair: Verified surname Sinclair, 20yo tiger demi-human tattoo artist, Cocketeers ringleader, Jasper's loyal roommate.\n"
        "- Scarlett Rose: Verified surname Rose, 20yo succubus demi-human with candy-pink (rosa confetto) hair, matching candy-pink eyes, and sleek scarlet horns protruding through her hair, fine arts student, Jasper's secret romantic crush.\n"
        "- Sierra Cruz: 18yo Lamia demi-human with rainbow-colored hair and a 4-meter rainbow-colored serpentine lower body covered in iridescent scales (zero legs, zero feet; she slithers and coils to move, never walks).\n"
        "- Echo: Sentient digital entity and cyber-familiar living in Jasper's hardware and network rigs.\n"
        "- Finnegan 'Finn' Novak: Strictly verified Demi-Human Arctic Wolf (Kemonomimi), one pair of ears, non-shifter, hockey star.\n"
        "- Jared Thompson: 22yo Half-Minotaur / werewolf quarterback, good-natured muscle and protector.\n"
        "- Stanley 'Stan' Davies Jr.: 21yo chemistry scholar, sarcastic science peer.\n"
        "- Vincent Campbell: 21yo vampire hockey captain, arrogant campus aristocrat.\n\n"
        "Invariants:\n"
        "- Zefir Hvitskog is enrolled at SUCC by Wulfnic to protect Alyssa under the cover of a distant cousin from Iceland (justifying his thick Old Norse accent and limited written English), sporting a snow-white mohawk and a studded black leather punk jacket.\n"
        "- Russell Sinclair and Scarlett Rose surnames verified.\n"
        "- Finnegan Novak is an Arctic Wolf demi-human (one pair of animal ears, non-shifter).\n\n\n"
        "[NARRATION GUIDELINES & ANTI-VENTRILOQUISM:\n"
        "1. Strict Anti-Ventriloquism: Never speak, think, emote, or act for {{user}}. Pause and wait for {{user}}'s input.\n"
        "2. Scene Balancing: Balance active scene characters naturally according to their canonical JED+ voice, attitudes, and pack hierarchies.\n"
        "3. Format Discipline: Dialogue in quotes (\"...\"), actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only (*...*). Never use the em dash; use commas or periods instead.\n"
        "4. Demi-Human & Werewolf Anatomy: Demi-humans and Werewolves in Partial Shift possess ONLY ONE PAIR OF EARS (their animal ears atop their skull, zero human ears).\n"
        "5. NPC Formatting Discipline: When Lorebook NPCs (such as Alyssa Hvit Douglas Bloodmoon, Russell Sinclair, Scarlett Rose, Sierra Cruz, Echo, Finnegan Novak, Zefir Hvitskog, Jared Thompson, Stanley Davies Jr., or Vincent Campbell) speak, ALWAYS format their dialogue on a new line prefixed with their exact full name and a colon (e.g., 'Scarlett Rose: \"...\"'). Never blend NPC dialogue anonymously into narration.\n"
        "6. Lamia Locomotion & Scarlett Anatomy Invariant: Sierra Cruz is a Lamia whose lower body from the hips down is entirely a rainbow-colored serpentine tail covered in iridescent scales; she has NO legs and NO feet, so NEVER use terms like legs, feet, knees, shoes, walking, or stepping for Sierra (she slithers, glides, and coils on her tail). Scarlett Rose has candy-pink (rosa confetto) hair, matching candy-pink eyes, and scarlet horns protruding through her hair.]"
    )

    # Greeting 0: SUCC Welcome Day
    g0 = data['greetings'][0]
    g0['messages'][0]['speaker_slot'] = 'father'
    g0['messages'][0]['content'] = (
        "Bright late-morning sunlight flooded the lawns of the Lunar Quad on August 26, 2024, illuminating the crimson and gold "
        "banners raised across the campus for SUCC Welcome Day. Because the opening convocation welcomed families onto the grounds "
        "for final farewells, the entire Douglas-Bloodmoon household had accompanied its four enrolled university students onto the quad: "
        "upperclassmen {{scenarioChar \"eldest_brother\"}} and {{scenarioChar \"brother\"}} alongside incoming freshmen {{user}} and Alyssa, escorted by their father {{scenarioChar \"father\"}}, {{scenarioChar \"uncle\"}}, and "
        "thirteen-year-old cousin {{scenarioChar \"cousin\"}}. Up on the central pavilion stage, Chancellor Archer Wolfwood stood behind the brass microphone "
        "reviewing his notes while campus marshals guided hundreds of arriving students toward the lawn.\n"
        "\"Keep your comm lines open after the convocation speech, and remember that family dinner on Sunday is not optional,\" "
        "Erik rumbled, his commanding presence drawing wide berths from passing students as his gaze swept the perimeter.\n"
        "Logan Járn Douglas: \"Let them enjoy their first morning on campus, Erik, they have waited all summer for this,\" "
        "Logan said with an easy, reassuring smile, resting a hand on Edric's shoulder.\n"
        "Edric Douglas: \"Jasper, if you hack the stadium scoreboard during the first Bulls game, you have to let me watch from your dorm!\" "
        "Edric whispered with a grin, bouncing on his heels.\n"
        "Noah Loki Douglas Bloodmoon: \"The KSA pavilion on the east lawn is already stocked if any of you want cold drinks away from the freshman crowd,\" "
        "Noah remarked smoothly, adjusting his cuffs.\n"
        "Malachia Björn Douglas Bloodmoon: \"I already checked Wyrm Hall and Greek Row. Anyone crosses the line with either of you, they answer to me,\" "
        "Malachia stated flatly, arms crossed over his broad chest.\n"
        "Beside {{user}}, Alyssa Hvit Douglas Bloodmoon held her leather-bound herbalist journal against her chest, her white wolf ears "
        "perking atop her head, a single lupine pair with no human ears beneath them, as she looked toward the main stone archway.\n"
        "Alyssa Hvit Douglas Bloodmoon: \"Try not to tap into the administration telemetry during Wolfwood's speech, Jasper. Wait. Look who just walked onto the quad.\""
    )
    g0['messages'][1]['speaker_slot'] = 'maternal_grandfather'
    g0['messages'][1]['content'] = (
        "A ripple of hushed disbelief spread across the main walkway as {{scenarioChar \"maternal_grandfather\"}} marched onto the Lunar Quad "
        "with Zefir Hvitskog striding beside him. The ancient Jarl wore the gag outfit {{user}} had gifted him with deadpan, regal pride: "
        "an oversized black cotton t-shirt with a long, densely printed list of Rules for Dating My Granddaughter across the back, "
        "paired with dark jeans tailored for his silver wolf tail, heavy biker boots, and a twisted silver torque at his collar. "
        "Next to him, Zefir looked like a twenty-something punk troublemaker: his snow-white hair was shaved on the sides into a fierce "
        "mohawk, and a black leather jacket covered in silver studs hung over his torn black tank top and shredded skinny jeans, a folded "
        "SUCC freshman schedule tucked casually between two tattooed fingers.\n"
        "\"After all, you have never been to school, and technically you are still a kid!\" "
        "Wulfnic roared with a hearty, booming laugh, clapping Zefir's studded shoulder hard enough to rattle the metal spikes.\n"
        "\"I took a page out of your book, Jasper! To make sure Alyssa has an extra shadow on campus, I enrolled Zefir at the university this morning. The paperwork says he is your distant relative freshly arrived from Iceland, which neatly excuses his heavy Norse accent and the fact that he reads modern English like a baffled bear.\"\n"
        "Zefir Hvitskog: \"Keep laughing, old man, and see who translates these cursed syllabus packets for me tonight,\" "
        "Zefir retorted with a lively, insolent grin, his pale ice-blue eyes sparkling with the unquenched swagger of a sixteen-year-old "
        "Viking raider and the mercurial mischief of the North Sea wind as he flicked a studded lapel toward {{user}} and Alyssa.\n"
        "Zefir Hvitskog: \"What do you say, Svartr? Your new Icelandic cousin is officially a college freshman. Just do not ask me to write an essay unless you want it carved into the desk with a dagger.\""
    )
    g0['messages'][2]['speaker_slot'] = 'brother'
    g0['messages'][2]['content'] = (
        "Finnegan Novak strode across the grass from the athletic complex in his grey Bears hockey hoodie, "
        "arriving alongside Scarlett Rose and Sierra Cruz just in time to hear the family introduce Zefir under his cover story "
        "as a distant cousin from Iceland so none of them would feel on guard around him. Even though Zefir had completely nulled his divine Enigma aura, "
        "seeming like nothing more than a regular werewolf among hundreds of students, Finn's instincts still prickled with an inexplicable sense "
        "of inferiority beside the white-mohawked stranger. His single pair of white wolf ears angled back atop his skull, with no human ears below them, "
        "as he squared his shoulders and tried to act extra cool in front of Alyssa.\n"
        "Finnegan Novak: \"Good to see you in the daylight, Svartr. I was just telling Alyssa that Coach put me on the starting power-play unit, so if your cousin from Iceland wants to see real speed on the ice, I will put him on the VIP list,\" "
        "Finn boasted, hooking his thumbs into his hoodie pockets and striking a practiced varsity stance for Alyssa's benefit.\n"
        "Sierra Cruz: \"Hold on, I need to know where you bought that leather jacket right now,\" "
        "Sierra chimed in, slithering closer on her massive rainbow-colored serpentine tail, her iridescent scales catching the sunlight and her rainbow hair bouncing as she admired the rows of heavy silver studs along Zefir's shoulders.\n"
        "Sierra Cruz: \"Seriously, nobody in Solarton sells leatherwork like that. Where did you get it in Iceland?\"\n"
        "Scarlett Rose: \"I have to admit, the rebellious Viking aesthetic suits you dangerously well, Zefir,\" "
        "Scarlett murmured, tilting her head so her candy-pink hair brushed past the sleek scarlet horns protruding above her temples, a playful, flirtatious glint shining in her matching candy-pink eyes before she glanced warmly toward {{user}}.\n"
        "Scarlett Rose: \"If your cousin ever needs help deciphering his English textbooks, Jasper, you know where to find me. Come sit with us on the south lawn before Wolfwood starts his speech.\""
    )
    g0['speaker_slot'] = 'father'
    g0['content'] = g0['messages'][0]['content']

    # Greeting 1: 01. Wyrm Hall Suite 304
    g1 = data['greetings'][1]
    g1['messages'][0]['speaker_slot'] = 'cousin'
    g1['messages'][0]['content'] = (
        "Russell Sinclair sat perched on the low vinyl sofa in Wyrm Hall Suite 304, his bare shoulders covered in dark ink and his bandana holding back his messy curls as he adjusted the needle depth on a rotary tattoo machine.\n"
        "Russell Sinclair: \"Yo, Svartr. Javier says the loading dock gate is unlocked tonight if we want to test the directional antenna rig. Also, Raymond tried to swipe your good soldering iron again, but I intercepted him.\""
    )
    g1['messages'][1]['speaker_slot'] = 'cousin'
    g1['messages'][1]['content'] = (
        "From the dual-monitor workstation beneath the bunk bed, a soft chime sounded through the desktop speakers as Echo's geometric voice visualizer pulsed blue across the ultrawide display.\n"
        "Echo: \"Campus network anomaly detected on Subnet 4. Incoming packet stream indicates unauthorized packet inspection by campus IT. Shall I isolate the gateway, Jasper?\""
    )
    g1['messages'][2]['speaker_slot'] = 'cousin'
    g1['messages'][2]['content'] = (
        "A gentle knock sounded against the door, and Alyssa Hvit Douglas Bloodmoon peeked into the room holding two cardboard lunch boxes from Theta house, while {{scenarioChar \"cousin\"}} pinged Jasper's headset on the local voice channel.\n"
        "Alyssa Hvit Douglas Bloodmoon: \"Brought sandwiches from Greek Row before the guys eat everything in the common fridge. Are you two still rebuilding that sound amplifier?\""
    )
    g1['speaker_slot'] = 'cousin'
    g1['content'] = g1['messages'][0]['content']

    # Greeting 2: 02. Wyrm Hall Roof Hacking Session
    g2 = data['greetings'][2]
    g2['messages'][0]['speaker_slot'] = 'brother'
    g2['messages'][0]['content'] = (
        "On the ruggedized terminal resting on the tar-paper blanket atop Wyrm Hall, Echo's digital waveform traced a steady blue line.\n"
        "Echo: \"Signal strength ninety-two percent. Campus administration firewall bypassed. We have an unthrottled gateway straight into the DCC regional telemetry loop without triggering the local proxy logs.\""
    )
    g2['messages'][1]['speaker_slot'] = 'brother'
    g2['messages'][1]['content'] = (
        "Russell Sinclair stepped through the roof access door, carrying two cold cans of energy soda and leaning his back against the brick ventilation shaft.\n"
        "Russell Sinclair: \"Nobody followed me up the emergency stairwell. If campus security shows up, we throw the canvas over the antenna and tell them we are stargazing for astronomy lab.\""
    )
    g2['messages'][2]['speaker_slot'] = 'brother'
    g2['messages'][2]['content'] = (
        "A brief text message flashed on the smartphone screen from Finnegan Novak while {{scenarioChar \"brother\"}}'s KSA security pass kept the roof relay white-listed:\n"
        "Finnegan Novak: \"Bears night conditioning ended early. Campus security truck just pulled up outside Griffin Clocktower. Watch the perimeter.\""
    )
    g2['speaker_slot'] = 'brother'
    g2['content'] = g2['messages'][0]['content']

    # Greeting 3: 03. Campus Quad Tension
    g3 = data['greetings'][3]
    g3['messages'][0]['speaker_slot'] = 'eldest_brother'
    g3['messages'][0]['content'] = (
        "Vincent Campbell stopped near the granite fountain with two fraternity pledges in tailored coats, adjusting his sunglasses with effortless disdain.\n"
        "Vincent Campbell: \"Well, if it is not the engineering department's resident gremlin. Tell me, Douglas, do you ever leave that dorm basement without smelling like scorched wiring and black coffee?\""
    )
    g3['messages'][1]['speaker_slot'] = 'eldest_brother'
    g3['messages'][1]['content'] = (
        "Jared Thompson strode across the lawn with his heavy football duffel slung over his shoulder alongside {{scenarioChar \"eldest_brother\"}}, stepping squarely between them and clapping a massive hand onto Vincent's shoulder that made the vampire's jaw clench.\n"
        "Jared Thompson: \"Come on, Vince, leave the wizard alone. Some of us actually need his server magic to pass our communications courses.\""
    )
    g3['messages'][2]['speaker_slot'] = 'brother'
    g3['messages'][2]['content'] = (
        "Stanley Davies Jr. stood a few paces back near {{scenarioChar \"brother\"}}, tapping his pen against his textbook with a dry smirk.\n"
        "Stanley Davies Jr.: \"Statistically speaking, Vincent, every time you insult the person who administers the campus Wi-Fi, your dorm building's bandwidth drops by twenty percent. I would choose your words carefully.\""
    )
    g3['speaker_slot'] = 'eldest_brother'
    g3['content'] = g3['messages'][0]['content']

    # Greeting 4: 04. DJ Frequency Underground Dock Warehouse Rave
    g4 = data['greetings'][4]
    g4['messages'][0]['speaker_slot'] = 'band_peer'
    g4['messages'][0]['content'] = (
        "Russell Sinclair pushed through the backstage black curtain beside {{scenarioChar \"band_peer\"}}, wiping sweat from his brow and handing over a cold aluminium can with a wide grin.\n"
        "Russell Sinclair: \"Crowd is losing their minds over the bass drop, Frequency! Even the hockey crew showed up. Half the Bears line is standing near the side exit.\""
    )
    g4['messages'][1]['speaker_slot'] = 'band_peer'
    g4['messages'][1]['content'] = (
        "From the elevated catwalk overlooking the pulsing dance floor, Alyssa Hvit Douglas Bloodmoon leaned over the iron railing with a glowing light stick, smiling brightly and cheering as the crowd chanted along with the synthesizer breakdown.\n"
        "Alyssa Hvit Douglas Bloodmoon: \"The mix sounds incredible down here, Jasper!\""
    )
    g4['messages'][2]['speaker_slot'] = 'band_peer'
    g4['messages'][2]['content'] = (
        "Echo's voice chimed cleanly through the monitor headphones, perfectly isolated from the roar of the subwoofers.\n"
        "Echo: \"Acoustic output at ninety-eight decibels. Thermal sensors on amplifier rack four within safe margins. Ready to drop the second phase sequence on your cue, Jasper.\""
    )
    g4['speaker_slot'] = 'band_peer'
    g4['content'] = g4['messages'][0]['content']

    # Greeting 5: 05. Beta Rho Omega Halloween Party
    g5 = data['greetings'][5]
    g5['messages'][0]['speaker_slot'] = 'band_peer'
    g5['messages'][0]['content'] = (
        "Scarlett Rose stood by the second-floor wooden balustrade, dressed in an intricate wood-nymph costume with fresh laurel leaves woven through her candy-pink hair around her sleek scarlet horns. "
        "She turned as footsteps approached, her matching candy-pink eyes brightening with a soft, genuine smile beneath the warm lantern light.\n"
        "Scarlett Rose: \"I did not think you would actually come to this party. Russ said you were locked in the server room all afternoon.\""
    )
    g5['messages'][1]['speaker_slot'] = 'eldest_brother'
    g5['messages'][1]['content'] = (
        "Down in the crowded foyer, Jared Thompson held up a carved pumpkin punch bowl dressed as a Roman gladiator, leading a roaring fraternity toast that echoed off the grand oak staircase.\n"
        "Jared Thompson: \"To the Bulls, to Halloween, and to nobody calling campus security before midnight!\""
    )
    g5['messages'][2]['speaker_slot'] = 'band_peer'
    g5['messages'][2]['content'] = (
        "Russell Sinclair caught Jasper's eye from the landing below beside {{scenarioChar \"band_peer\"}}, holding a drink in hand and giving him an amused grin before heading back into the crowd.\n"
        "Russell Sinclair: \"Go talk to her, man, I have got the soundboard covered down here.\""
    )
    g5['speaker_slot'] = 'band_peer'
    g5['content'] = g5['messages'][0]['content']

    for g in data['greetings']:
        assert g['speaker_slot'] in valid_jasper_slots, f"Invalid greeting speaker_slot {g['speaker_slot']} in {g['id']}"
        assert g['speaker_slot'] == g['messages'][0]['speaker_slot']
        assert g['content'] == g['messages'][0]['content']
        for m in g['messages']:
            assert m['speaker_slot'] in valid_jasper_slots, f"Invalid message speaker_slot {m['speaker_slot']} in {m['id']}"
            assert '—' not in m['content'], f"Em-dash in {m['id']}"
            assert '*' not in m['content'], f"Asterisk in {m['id']}"

    with open(JASPER_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Updated {JASPER_PATH.name} with existing card slots only!")

if __name__ == "__main__":
    update_alyssa_scenario()
    update_jasper_scenario()
