import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

ALYSSA_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json'
JASPER_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json'
PRIMARY_LB = ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json'
OPT_PRIMARY_LB = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json'

ALYSSA_PERSONA_ID = "persona_1786335754946"
JASPER_PERSONA_ID = "1792155173728"

# 1. Update Zefir Hvitskog in Svartulfr_NPC_Primary.json (and optimized mirror)
def update_zefir_lorebook():
    for lb_path in [PRIMARY_LB, OPT_PRIMARY_LB]:
        with open(lb_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        updated = False
        for entry in data.get('lexicon', []):
            if entry.get('name') == 'Zefir Hvitskog':
                content = entry['content']
                # Update ATTIRE in the opening PList block
                old_attire = (
                    "ATTIRE: Dresses like a rebellious modern college student to maintain his cover - "
                    "torn black tank top, shredded skinny jeans, unlaced scuffed Dr. Martens, massive hood "
                    "or oversized hoodie, silver ear piercings, loose silk garments woven from ancient spider silk beneath;"
                )
                new_attire = (
                    "ATTIRE: Dresses in a rebellious punk college student style to maintain his campus cover - "
                    "snow-white hair shaved into a sharp mohawk (cresta alla moicana), a heavy black leather jacket "
                    "bristling with silver studs (giubbotto con le borchie) over a torn black tank top, shredded skinny jeans, "
                    "unlaced scuffed Dr. Martens, silver ear piercings, and loose ancient spider-silk garments beneath; "
                    "CAMPUS COVER: Enrolled as a freshman at SUCC by Wulfnic to protect Alyssa under the cover story of a "
                    "distant relative freshly arrived from Iceland, which justifies his thick Old Norse accent and his "
                    "poor familiarity with written modern English;"
                )
                if old_attire in content:
                    content = content.replace(old_attire, new_attire, 1)
                
                # Update the campus cover paragraph in THE ONE WHO WAS NEVER GROWN
                old_cover_par = (
                    "He reads as 20 to 22 to anyone who bothers to look, easily passing as a university student, "
                    "and he treats the cover as an ongoing private joke. It is also why his cover works and Ut's never could. "
                    "Ut cannot walk across a campus without the campus noticing. Zefir crosses it as an undergraduate "
                    "with his hood up, blending into the crowd until the moment violence is required."
                )
                new_cover_par = (
                    "He reads as 20 to 22 to anyone who bothers to look, easily passing as a university student, "
                    "and he treats the cover as an ongoing private joke. To guard Alyssa closely during her college years, "
                    "Wulfnic officially enrolled Zefir at SUCC with a laugh, telling him that after all he had never been "
                    "to school and was technically still a kid. On campus he rocks a punk look with his snow-white hair "
                    "shaved into a sharp mohawk and a studded black leather jacket, operating under the cover of a distant "
                    "cousin who just arrived from Iceland, an excuse that neatly explains his heavy Old Norse accent and his "
                    "shaky grasp of written English. It is also why his cover works and Ut's never could: Ut cannot walk "
                    "across a campus without the campus noticing, whereas Zefir struts across the quad as a punk Icelandic "
                    "undergraduate until the moment violence is required."
                )
                if old_cover_par in content:
                    content = content.replace(old_cover_par, new_cover_par, 1)

                assert '—' not in content, "Em-dash found in Zefir content!"
                assert '*' not in content, "Asterisk found in Zefir content!"
                entry['content'] = content
                updated = True
        assert updated, f"Zefir not updated in {lb_path}"
        # Sync entries == lexicon
        data['entries'] = json.loads(json.dumps(data['lexicon']))
        with open(lb_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[OK] Updated Zefir Hvitskog punk campus cover in {lb_path.name}")

# 2. Define Alyssa Greeting 0 (SUCC Welcome Day)
alyssa_msg_0 = (
    "The late morning sun beat down across the crowded lawns of the Lunar Quad on August 26, 2024, "
    "filtering through the crimson and gold banners hoisted for SUCC Welcome Day. Because the opening convocation "
    "was open to students' families for final farewells before classes began, the entire Douglas-Bloodmoon clan had "
    "escorted its four enrolled university students onto the quad: senior brothers Malachia and Noah alongside incoming "
    "freshman twins Jasper and {{user}}, accompanied by their father Erik, Uncle Logan, and thirteen-year-old cousin Edric. "
    "Up on the central pavilion stage, Chancellor Archer Wolfwood stood flanked by department deans, testing the heavy brass "
    "microphone while sound technicians balanced the speakers.\n"
    "Erik Ulfr Douglas: \"Stick together when the crowd breaks after the address, and call if the campus wardens give you any trouble,\" "
    "Erik rumbled, his tall frame casting a protective shadow over the walkway as his golden-brown eyes swept the quad.\n"
    "Logan Járn Douglas: \"Give them room to breathe, Erik, it is college orientation, not a siege,\" "
    "Logan said with a warm chuckle, resting a massive hand on Edric's shoulder.\n"
    "Edric Douglas: \"Wait until you see the size of the dining commons, Jasper! Do freshmen get unlimited passes to the arcade Annex too?\" "
    "Edric asked eagerly, craning his neck toward the student union.\n"
    "Noah Loki Douglas Bloodmoon: \"The KSA hospitality tent on the east lawn has cold drinks and shade reserved for us whenever you want to escape the heat,\" "
    "Noah noted smoothly, adjusting the lapel of his tailored linen blazer.\n"
    "Malachia Björn Douglas Bloodmoon: \"I already walked the perimeter from the gym to Greek Row. Nobody bothers my little sister on this campus,\" "
    "Malachia added in a low, gravelly tone, folding his arms across his chest.\n"
    "Beside {{user}}, {{scenarioChar \"twin\"}} glanced up from the live network telemetry on his datapad, his dark wolf ears "
    "angling toward the main gate, a single lupine pair atop his head with no human ears beneath them. "
    "\"Freshman registration already crashed the central library server,\" Jasper murmured, nudging {{user}}'s elbow. "
    "\"Wait a second. Look who is walking through the main stone archway right now.\""
)

alyssa_msg_1 = (
    "The chatter along the central promenade parted in a wave of stunned silence as Wulfnic Báleygr Bloodmoon strode onto "
    "the Lunar Quad with Zefir Hvitskog at his side. The twelve-hundred-year-old Jarl of Svartúlfr wore his favorite gag outfit "
    "with solemn, chest-out pride: an oversized black cotton t-shirt gifted by Jasper, its back emblazoned in bold white block "
    "letters with a dense, itemized list of Rules for Dating My Granddaughter, paired with dark jeans slit for his silver wolf tail, "
    "heavy buckled biker boots, and an ancient twisted silver torque at his throat. Beside him, Zefir looked every bit a twenty-something "
    "punk rebel: his snow-white hair was shaved on the sides into a sharp mohawk, and he wore a heavy black leather jacket bristling "
    "with silver studs over a torn black tank top and shredded skinny jeans, carrying an orientation packet folded in one tattooed hand.\n"
    "Wulfnic Báleygr Bloodmoon: \"After all, you have never been to school, and technically you are still a kid!\" "
    "Wulfnic boomed in English, throwing his head back with a thunderous, resonant laugh as he clapped a heavy hand onto Zefir's studded shoulder.\n"
    "Wulfnic Báleygr Bloodmoon: \"Do not look so surprised, Erik! To make sure our little Alyssa is properly guarded on campus, I enrolled Zefir at the university too. As far as the registrar is concerned, he is your distant cousin who just flew in from Iceland. That explains his thick Norse accent and why his written English still looks like runic scratchings.\"\n"
    "Zefir Hvitskog: \"Laugh all you want, my Jarl, but if some pompous professor waves a piece of chalk in my face, I am not promising I will keep the chalk whole,\" "
    "Zefir shot back with a wicked, cocky grin, the lively swagger of the sixteen-year-old Viking he once was dancing in his pale ice-blue eyes "
    "like a capricious gust of North Sea wind before he tipped a mocking two-finger salute toward {{user}} and Jasper.\n"
    "Zefir Hvitskog: \"Relax, little cousin. Your Icelandic relative is officially an undergraduate now. Point me at whoever looks at you sideways and they will vanish before the bell rings.\""
)

alyssa_msg_2 = (
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
    "Sierra asked, her emerald serpent tail coiling smoothly beneath her pleated skirt as she stepped right up to Zefir, her eyes wide with genuine fashion envy as she inspected the heavy silver studs along his black leather lapels.\n"
    "Sierra Cruz: \"The distressing on the leather and those custom spikes look vintage European. Is there some underground boutique in Reykjavik I need to know about?\"\n"
    "Scarlett Rose: \"Honestly, I think the Icelandic punk look is exactly what this quad was missing,\" "
    "Scarlett purred with a slow, flirtatious smile, her dark succubus wings shifting neatly behind her embroidered linen vest and her tail swaying near her ankles as she offered Zefir a lingering look from beneath her lashes.\n"
    "Scarlett Rose: \"Welcome to Solarton, Zefir. Since your English reading is still rusty, I would be more than happy to give you some private tutoring after convocation. Come on, Alyssa, Wolfwood is stepping up to the microphone.\""
)

alyssa_greeting_0 = {
    "id": "scene-alyssa-welcome-day",
    "name": "SUCC Welcome Day",
    "description": "August 26, 2024. SUCC Welcome Day at the Lunar Quad: arriving with the full family (Noah, Malachia, Jasper, Alyssa, Erik, Logan, and Edric), Wulfnic in his gag shirt enrolling punk-mohawk Zefir as an Icelandic cousin, and introducing him to Scarlett, Sierra, and Finn.",
    "messages": [
        {
            "id": "msg-al-0-1",
            "speaker_slot": "twin",
            "content": alyssa_msg_0
        },
        {
            "id": "msg-al-0-2",
            "speaker_slot": "twin",
            "content": alyssa_msg_1
        },
        {
            "id": "msg-al-0-3",
            "speaker_slot": "childhood_friend",
            "content": alyssa_msg_2
        }
    ],
    "speaker_slot": "twin",
    "content": alyssa_msg_0,
    "linked_persona_ids": [
        ALYSSA_PERSONA_ID
    ]
}

# 3. Define Jasper Greeting 0 (SUCC Welcome Day)
jasper_msg_0 = (
    "Bright late-morning sunlight flooded the lawns of the Lunar Quad on August 26, 2024, illuminating the crimson and gold "
    "banners raised across the campus for SUCC Welcome Day. Because the opening convocation welcomed families onto the grounds "
    "for final farewells, the entire Douglas-Bloodmoon household had accompanied its four enrolled university students onto the quad: "
    "upperclassmen Malachia and Noah alongside incoming freshmen {{user}} and Alyssa, escorted by their father Erik, Uncle Logan, and "
    "thirteen-year-old cousin Edric. Up on the central pavilion stage, Chancellor Archer Wolfwood stood behind the brass microphone "
    "reviewing his notes while campus marshals guided hundreds of arriving students toward the lawn.\n"
    "Erik Ulfr Douglas: \"Keep your comm lines open after the convocation speech, and remember that family dinner on Sunday is not optional,\" "
    "Erik rumbled, his commanding presence drawing wide berths from passing students as his gaze swept the perimeter.\n"
    "Logan Járn Douglas: \"Let them enjoy their first morning on campus, Erik, they have waited all summer for this,\" "
    "Logan said with an easy, reassuring smile, resting a hand on Edric's shoulder.\n"
    "Edric Douglas: \"Jasper, if you hack the stadium scoreboard during the first Bulls game, you have to let me watch from your dorm!\" "
    "Edric whispered with a grin, bouncing on his heels.\n"
    "Noah Loki Douglas Bloodmoon: \"The KSA pavilion on the east lawn is already stocked if any of you want cold drinks away from the freshman crowd,\" "
    "Noah remarked smoothly, adjusting his cuffs.\n"
    "Malachia Björn Douglas Bloodmoon: \"I already checked Wyrm Hall and Greek Row. Anyone crosses the line with either of you, they answer to me,\" "
    "Malachia stated flatly, arms crossed over his broad chest.\n"
    "Beside {{user}}, {{scenarioChar \"twin\"}} held her leather-bound herbalist journal against her chest, her white wolf ears "
    "perking atop her head, a single lupine pair with no human ears beneath them, as she looked toward the main stone archway. "
    "\"Try not to tap into the administration telemetry during Wolfwood's speech, Jasper,\" Alyssa murmured softly, her pale eyes widening "
    "as the crowd near the gate suddenly parted. \"Wait. Look who just walked onto the quad.\""
)

jasper_msg_1 = (
    "A ripple of hushed disbelief spread across the main walkway as Wulfnic Báleygr Bloodmoon marched onto the Lunar Quad "
    "with Zefir Hvitskog striding beside him. The ancient Jarl wore the gag outfit {{user}} had gifted him with deadpan, regal pride: "
    "an oversized black cotton t-shirt with a long, densely printed list of Rules for Dating My Granddaughter across the back, "
    "paired with dark jeans tailored for his silver wolf tail, heavy biker boots, and a twisted silver torque at his collar. "
    "Next to him, Zefir looked like a twenty-something punk troublemaker: his snow-white hair was shaved on the sides into a fierce "
    "mohawk, and a black leather jacket covered in silver studs hung over his torn black tank top and shredded skinny jeans, a folded "
    "SUCC freshman schedule tucked casually between two tattooed fingers.\n"
    "Wulfnic Báleygr Bloodmoon: \"After all, you have never been to school, and technically you are still a kid!\" "
    "Wulfnic roared with a hearty, booming laugh, clapping Zefir's studded shoulder hard enough to rattle the metal spikes.\n"
    "Wulfnic Báleygr Bloodmoon: \"I took a page out of your book, Jasper! To make sure Alyssa has an extra shadow on campus, I enrolled Zefir at the university this morning. The paperwork says he is your distant relative freshly arrived from Iceland, which neatly excuses his heavy Norse accent and the fact that he reads modern English like a baffled bear.\"\n"
    "Zefir Hvitskog: \"Keep laughing, old man, and see who translates these cursed syllabus packets for me tonight,\" "
    "Zefir retorted with a lively, insolent grin, his pale ice-blue eyes sparkling with the unquenched swagger of a sixteen-year-old "
    "Viking raider and the mercurial mischief of the North Sea wind as he flicked a studded lapel toward {{user}} and Alyssa.\n"
    "Zefir Hvitskog: \"What do you say, Svartr? Your new Icelandic cousin is officially a college freshman. Just do not ask me to write an essay unless you want it carved into the desk with a dagger.\""
)

jasper_msg_2 = (
    "{{scenarioChar \"childhood_friend\"}} strode across the grass from the athletic complex in his grey Bears hockey hoodie, "
    "arriving alongside {{scenarioChar \"crush\"}} and Sierra Cruz just in time to hear the family introduce Zefir under his cover story "
    "as a distant cousin from Iceland so none of them would feel on guard around him. Even though Zefir had completely nulled his divine Enigma aura, "
    "seeming like nothing more than a regular werewolf among hundreds of students, Finn's instincts still prickled with an inexplicable sense "
    "of inferiority beside the white-mohawked stranger. His single pair of white wolf ears angled back atop his skull, with no human ears below them, "
    "as he squared his shoulders and tried to act extra cool in front of Alyssa.\n"
    "Finnegan Novak: \"Good to see you in the daylight, Svartr. I was just telling Alyssa that Coach put me on the starting power-play unit, so if your cousin from Iceland wants to see real speed on the ice, I will put him on the VIP list,\" "
    "Finn boasted, hooking his thumbs into his hoodie pockets and striking a practiced varsity stance for Alyssa's benefit.\n"
    "Sierra Cruz: \"Hold on, I need to know where you bought that leather jacket right now,\" "
    "Sierra chimed in, gliding closer on her emerald lamia tail to admire the rows of heavy silver studs along Zefir's shoulders.\n"
    "Sierra Cruz: \"Seriously, nobody in Solarton sells leatherwork like that. Where did you get it in Iceland?\"\n"
    "Scarlett Rose: \"I have to admit, the rebellious Viking aesthetic suits you dangerously well, Zefir,\" "
    "Scarlett murmured, tilting her head with a playful, flirtatious glint in her amber eyes while her folded succubus wings rested smooth against her shoulders and her tail curled near her ankle, before she glanced warmly toward {{user}}.\n"
    "Scarlett Rose: \"If your cousin ever needs help deciphering his English textbooks, Jasper, you know where to find me. Come sit with us on the south lawn before Wolfwood starts his speech.\""
)

jasper_greeting_0 = {
    "id": "scene-jasper-welcome-day",
    "name": "SUCC Welcome Day",
    "description": "August 26, 2024. SUCC Welcome Day at the Lunar Quad: arriving with the full family (Noah, Malachia, Jasper, Alyssa, Erik, Logan, and Edric), Wulfnic in his gag shirt enrolling punk-mohawk Zefir as an Icelandic cousin, and introducing him to Scarlett, Sierra, and Finn.",
    "messages": [
        {
            "id": "msg-js-0-1",
            "speaker_slot": "twin",
            "content": jasper_msg_0
        },
        {
            "id": "msg-js-0-2",
            "speaker_slot": "twin",
            "content": jasper_msg_1
        },
        {
            "id": "msg-js-0-3",
            "speaker_slot": "childhood_friend",
            "content": jasper_msg_2
        }
    ],
    "speaker_slot": "twin",
    "content": jasper_msg_0,
    "linked_persona_ids": [
        JASPER_PERSONA_ID
    ]
}

def update_local_scenarios():
    for msg in [alyssa_msg_0, alyssa_msg_1, alyssa_msg_2, jasper_msg_0, jasper_msg_1, jasper_msg_2]:
        assert '—' not in msg, "Em-dash found in scenario message!"
        assert '*' not in msg, "Asterisk found in scenario message!"

    # Update Alyssa Scenario
    with open(ALYSSA_PATH, 'r', encoding='utf-8') as f:
        alyssa_data = json.load(f)
    
    alyssa_data['greetings'][0] = alyssa_greeting_0
    # Add invariant note about Zefir's campus cover if not already present
    invariant_note = "- Zefir Hvitskog is enrolled at SUCC by Wulfnic to protect Alyssa under the cover of a distant cousin from Iceland (justifying his thick Old Norse accent and limited written English), sporting a snow-white mohawk and a studded black leather punk jacket."
    if "Zefir Hvitskog is enrolled at SUCC" not in alyssa_data['scenario']:
        alyssa_data['scenario'] = alyssa_data['scenario'].replace(
            "Invariants:\n",
            f"Invariants:\n{invariant_note}\n"
        )
    with open(ALYSSA_PATH, 'w', encoding='utf-8') as f:
        json.dump(alyssa_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Updated {ALYSSA_PATH.name} (Greeting 0 + Invariant)")

    # Update Jasper Scenario
    with open(JASPER_PATH, 'r', encoding='utf-8') as f:
        jasper_data = json.load(f)
    
    jasper_data['greetings'][0] = jasper_greeting_0
    if "Zefir Hvitskog is enrolled at SUCC" not in jasper_data['scenario']:
        jasper_data['scenario'] = jasper_data['scenario'].replace(
            "Invariants:\n",
            f"Invariants:\n{invariant_note}\n"
        )
    with open(JASPER_PATH, 'w', encoding='utf-8') as f:
        json.dump(jasper_data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Updated {JASPER_PATH.name} (Greeting 0 + Invariant)")

if __name__ == "__main__":
    update_zefir_lorebook()
    update_local_scenarios()
