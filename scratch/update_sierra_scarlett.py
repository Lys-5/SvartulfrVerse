import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

ALYSSA_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json'
JASPER_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json'
MASTER_PATH = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
PRIMARY_LB = ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json'
OPT_PRIMARY_LB = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json'
SCARLETT_LEGACY = ROOT / 'ARCHIVIO' / 'cards_legacy' / 'Scarlett_Rose_card.json'
SIERRA_LEGACY = ROOT / 'ARCHIVIO' / 'cards_legacy' / 'Sierra_Cruz_card.json'

# 1. Update Scarlett Rose and Sierra Cruz in Svartulfr_NPC_Primary.json (+ optimized mirror) and Legacy Cards
def update_scarlett_and_sierra_profiles():
    # Update Legacy Cards first
    with open(SCARLETT_LEGACY, 'r', encoding='utf-8') as f:
        sc_card = json.load(f)
    
    sc_desc = sc_card['description']
    sc_desc = sc_desc.replace(
        "HAIR: Pastel pink, cascading down to mid-back in voluminous soft waves; EYES: Luminous ruby-red that can glow soft pink when channeling charm; FEATURES: Two small elegant dark red horns curling like a ram's above her temples,",
        "HAIR: Candy-pink (rosa confetto), cascading down to mid-back in voluminous soft waves; EYES: Bright candy-pink (rosa confetto) matching her hair; FEATURES: Two sleek scarlet horns protruding visibly through her candy-pink hair above her temples,"
    )
    sc_desc = sc_desc.replace("her ruby eyes flare dangerous crimson", "her candy-pink eyes flare with a hypnotic glow")
    sc_card['description'] = sc_desc
    sc_card['visual_description'] = (
        "Gorgeous 20-year-old modern succubus demihuman, 170cm (5'7\"), flawless hourglass dancer's frame, "
        "cascading candy-pink (rosa confetto) wavy hair, matching bright candy-pink eyes, two sleek scarlet horns "
        "protruding through her hair above her temples, slender prehensile red tail with spade tip, single pair of "
        "pointed demi-human ears (no human ears), golden-toned warm skin."
    )
    sc_card['character_note'] = sc_card['character_note'].replace(
        "pastel pink hair, red eyes, ram horns",
        "candy-pink hair, candy-pink eyes, scarlet horns protruding through her hair"
    )
    sc_card['first_mes'] = sc_card['first_mes'].replace("lo sguardo color rubino", "lo sguardo rosa confetto")
    with open(SCARLETT_LEGACY, 'w', encoding='utf-8') as f:
        json.dump(sc_card, f, indent=2, ensure_ascii=False)
    print("[OK] Updated Scarlett_Rose_card.json in ARCHIVIO/cards_legacy")

    with open(SIERRA_LEGACY, 'r', encoding='utf-8') as f:
        si_card = json.load(f)
    si_desc = si_card['description']
    si_desc = si_desc.replace(
        "BUILD: Adorable, soft, expressive human upper torso and face merging seamlessly at the hips into a colossal, powerfully muscled rainbow-scaled serpentine lower body; HAIR: Iridescent dark rainbow hair with silky sheen falling in messy locks; EYES: Bright candy-pink with serpentine vertical slit pupils; FEATURES: Delicate forked tongue, heat-sensing pits beneath nostrils, small venom fangs behind human teeth, iridescent emerald-violet-indigo scales along her massive 4-meter tail, single pair of pointed demi-human ears (no human ears);",
        "BUILD: Adorable, soft, expressive human upper torso and face merging seamlessly at the hips into a colossal, powerfully muscled 4-meter serpentine lower body (zero human legs, zero feet); HAIR: Rainbow-colored hair with an iridescent sheen falling in messy locks; EYES: Bright candy-pink with serpentine vertical slit pupils; FEATURES: Delicate forked tongue, heat-sensing pits beneath nostrils, small venom fangs behind human teeth, rainbow-colored tail covered in shimmering iridescent scales along her massive 4-meter serpentine lower body, single pair of pointed demi-human ears (no human ears); LOCOMOTION & ANATOMY RULE: As a Lamia, her lower body from the hips down is entirely a giant snake tail. She NEVER walks, steps, stands on feet, kneels, or wears shoes/pants; she slithers, glides, coils, and rises on her muscular serpentine coils to move;"
    )
    si_desc = si_desc.replace(
        "Over 4 meters of dense, muscular obsidian-and-crimson snake coils",
        "Over 4 meters of dense, muscular rainbow-colored snake coils with iridescent scales"
    )
    si_card['description'] = si_desc
    si_card['personality'] = si_card['personality'][:-1] + "; ANATOMY & LOCOMOTION RULE: Lower body is a 4m rainbow-scaled snake tail with iridescent scales (NO legs, NO feet, NO shoes). NEVER use verbs like walk, step, or stand on feet for Sierra; she slithers, glides, and coils]"
    si_card['visual_description'] = (
        "Adorable 18-year-old Lamia demihuman, cute human upper torso and face with messy rainbow-colored hair and bright candy-pink serpentine slitted eyes, "
        "merging at the hips into a 4-meter massive, powerfully muscled rainbow-colored serpentine tail covered in shimmering iridescent scales (zero human legs or feet), "
        "small fangs, delicate forked tongue, single pair of pointed demi-human ears (no human ears)."
    )
    with open(SIERRA_LEGACY, 'w', encoding='utf-8') as f:
        json.dump(si_card, f, indent=2, ensure_ascii=False)
    print("[OK] Updated Sierra_Cruz_card.json in ARCHIVIO/cards_legacy")

    # Update NPC Primary Lorebook + optimized mirror
    for lb_path in [PRIMARY_LB, OPT_PRIMARY_LB]:
        with open(lb_path, 'r', encoding='utf-8') as f:
            lb_data = json.load(f)
        for entry in lb_data.get('lexicon', []):
            if entry.get('name') == 'Scarlett Rose':
                entry['content'] = sc_desc
            elif entry.get('name') == 'Sierra Cruz':
                entry['content'] = si_desc
        lb_data['entries'] = json.loads(json.dumps(lb_data['lexicon']))
        with open(lb_path, 'w', encoding='utf-8') as f:
            json.dump(lb_data, f, indent=2, ensure_ascii=False)
        print(f"[OK] Updated Scarlett Rose & Sierra Cruz in {lb_path.name}")

# 2. Update SUCC Route Alyssa & Jasper Scenarios
def update_succ_scenarios():
    # Update Alyssa Route
    with open(ALYSSA_PATH, 'r', encoding='utf-8') as f:
        al_data = json.load(f)

    # Update scenario overview / cast / guidelines in Alyssa Route
    al_scen = al_data['scenario']
    al_scen = al_scen.replace(
        '- {{scenarioChar "best_friend"}} (Scarlett Rose): 20yo Succubus demi-human, verified surname Rose, botany and fine arts major, social coordinator, and Alyssa\'s loyal confidante.',
        '- {{scenarioChar "best_friend"}} (Scarlett Rose): 20yo Succubus demi-human, verified surname Rose, candy-pink (rosa confetto) hair and matching candy-pink eyes, with two sleek scarlet horns protruding through her hair above her temples, dark succubus wings, and a spade-tipped tail. Botany and fine arts major, social coordinator, and Alyssa\'s loyal confidante.'
    )
    al_scen = al_scen.replace(
        '- {{scenarioChar "roommate"}} (Sierra Cruz): 20yo Lamia demi-human, Theta Iota Theta sister, cheerleader, socialite roommate.',
        '- {{scenarioChar "roommate"}} (Sierra Cruz): 18yo Lamia (serpentine) demi-human, Theta Iota Theta sister and Applied Necromancy major. She has rainbow-colored hair and a massive 4-meter rainbow-colored serpentine tail with iridescent scales from the hips down (zero human legs, zero feet; she slithers, glides, and coils to move, never walks or steps).'
    )
    lamia_rule = (
        "6. Lamia Locomotion & Scarlett Anatomy Invariant: Sierra Cruz is a Lamia whose lower body from the hips down is entirely a rainbow-colored serpentine tail covered in iridescent scales; she has NO legs and NO feet, so NEVER use terms like legs, feet, knees, shoes, walking, or stepping for Sierra (she slithers, glides, and coils on her tail). Scarlett Rose has candy-pink (rosa confetto) hair, matching candy-pink eyes, and scarlet horns protruding through her hair.]"
    )
    if "6. Lamia Locomotion & Scarlett Anatomy Invariant:" not in al_scen:
        al_scen = al_scen.replace(
            "Never blend NPC dialogue anonymously into narration.]",
            "Never blend NPC dialogue anonymously into narration.\n" + lamia_rule
        )
    al_data['scenario'] = al_scen

    # Update Greeting 0 msg-al-0-3 in Alyssa Route
    al_msg_2 = (
        "{{scenarioChar \"childhood_friend\"}} cut through the flow of orientation traffic from the athletics pavilion with his "
        "Bears varsity jacket slung over one shoulder, arriving right alongside {{scenarioChar \"best_friend\"}} and {{scenarioChar \"roommate\"}}. "
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
    al_data['greetings'][0]['messages'][2]['content'] = al_msg_2

    # Fix other greetings in Alyssa Route for Sierra and Scarlett
    for g in al_data['greetings']:
        if g['id'] == 'scene-alyssa-greek-row':
            g['messages'][0]['content'] = (
                "Sierra Cruz coiled her long, rainbow-scaled serpentine tail in front of the full-length mirror, her iridescent scales "
                "shimmering in the morning light as she brushed back a lock of rainbow-colored hair and checked her phone calendar. "
                "\"If we slither out in ten minutes, we can grab iced matcha before the lecture hall fills up. Professor Vance locked the front doors at five past eight on Monday.\""
            )
            g['content'] = g['messages'][0]['content']
        elif g['id'] == 'scene-alyssa-labs':
            g['messages'][0]['content'] = (
                "Scarlett Rose rested her sketchpad beside a tray of botanical specimens, her pencil rendering the delicate vein structure of a silverleaf fern. "
                "Her candy-pink waves and the sleek scarlet horns peeking through her hair caught the white overhead light as her matching candy-pink eyes crinkled in a warm smile. "
                "\"Professor Vance said if we finish the cellular titration before noon, we can take the leftover culture plates to the greenhouse. I already prepared the slides for your section.\""
            )
            g['content'] = g['messages'][0]['content']
        elif g['id'] == 'scene-alyssa-bulls-tunnel':
            g['messages'][2]['content'] = (
                "Sierra Cruz glided past along the smooth concrete floor on her rainbow-colored serpentine coils, her iridescent scales whispering softly as she carried a bundle of campus banners and shook her rainbow-haired head with a laugh. "
                "\"Help him out, Lys. If the Bulls lose the opening game, Greek Row will be in mourning for two weeks straight.\""
            )

    with open(ALYSSA_PATH, 'w', encoding='utf-8') as f:
        json.dump(al_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Updated {ALYSSA_PATH.name}")

    # Update Jasper Route
    with open(JASPER_PATH, 'r', encoding='utf-8') as f:
        js_data = json.load(f)

    js_scen = js_data['scenario']
    js_scen = js_scen.replace(
        '- {{scenarioChar "crush"}} (Scarlett Rose): Verified surname Rose, 20yo succubus demi-human, fine arts student, Jasper\'s secret romantic crush.',
        '- {{scenarioChar "crush"}} (Scarlett Rose): Verified surname Rose, 20yo succubus demi-human with candy-pink (rosa confetto) hair, matching candy-pink eyes, and sleek scarlet horns protruding through her hair, fine arts student, Jasper\'s secret romantic crush.\n- Sierra Cruz (Lorebook NPC): 18yo Lamia demi-human with rainbow-colored hair and a 4-meter rainbow-colored serpentine lower body covered in iridescent scales (zero legs, zero feet; she slithers and coils to move, never walks).'
    )
    if "6. Lamia Locomotion & Scarlett Anatomy Invariant:" not in js_scen:
        js_scen = js_scen.replace(
            "Never blend NPC dialogue anonymously into narration.]",
            "Never blend NPC dialogue anonymously into narration.\n" + lamia_rule
        )
    js_data['scenario'] = js_scen

    # Update Greeting 0 msg-js-0-3 in Jasper Route
    js_msg_2 = (
        "{{scenarioChar \"childhood_friend\"}} strode across the grass from the athletic complex in his grey Bears hockey hoodie, "
        "arriving alongside {{scenarioChar \"crush\"}} and Sierra Cruz just in time to hear the family introduce Zefir under his cover story "
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
    js_data['greetings'][0]['messages'][2]['content'] = js_msg_2

    # Fix Greeting 5 in Jasper Route (BRO Halloween Party)
    for g in js_data['greetings']:
        if g['id'] == 'scene-jasper-bro-halloween':
            g['messages'][0]['content'] = (
                "Scarlett Rose stood by the second-floor wooden balustrade, dressed in an intricate wood-nymph costume with fresh laurel leaves woven through her candy-pink hair around her sleek scarlet horns. "
                "She turned as footsteps approached, her matching candy-pink eyes brightening with a soft, genuine smile beneath the warm lantern light. "
                "\"I did not think you would actually come to this party. Russ said you were locked in the server room all afternoon.\""
            )
            g['content'] = g['messages'][0]['content']

    with open(JASPER_PATH, 'w', encoding='utf-8') as f:
        json.dump(js_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Updated {JASPER_PATH.name}")

    # Also update Master Scenario reference if present
    with open(MASTER_PATH, 'r', encoding='utf-8') as f:
        m_data = json.load(f)
    m_raw = json.dumps(m_data, ensure_ascii=False)
    m_raw = m_raw.replace(
        "le sue lunghe spire serpentine nere e cremisi raccolte vicino alla parete",
        "le sue lunghe spire serpentine color arcobaleno dalle scaglie iridescenti raccolte vicino alla parete"
    )
    m_data = json.loads(m_raw)
    with open(MASTER_PATH, 'w', encoding='utf-8') as f:
        json.dump(m_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Updated {MASTER_PATH.name}")

if __name__ == "__main__":
    update_scarlett_and_sierra_profiles()
    update_succ_scenarios()
