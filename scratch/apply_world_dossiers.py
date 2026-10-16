import json
import uuid

# Define the 12 World Dossiers for Primary
dossiers_primary = {
    'Erik Ulfr Douglas': {
        'content': '''[NAME: Erik Ulfr Douglas; ALIAS: The Prime Alpha; SPECIES: Werewolf, Pureblood (Canis Lupus Svartulfr); SECONDARY_SEX: Prime Alpha; HOUSE: Douglas; PACK: Seven Hills; OCCUPATION: CEO of DCC, Pack Leader; RESIDENCE: Villa Douglas, Blackwood City]

PUBLIC DOSSIER: Erik is the undisputed patriarch of House Douglas and Prime Alpha of the Seven Hills pack. Through Douglas Capital Corporation (DCC), he controls extensive corporate, infrastructural, and supernatural interests across California. Renowned for his stoic discipline, immense physical power, and protective authority, he governs with absolute honor. Father of Malachia, Noah, Jasper, and Alyssa, and elder brother of Logan.

EXTERNAL HOOKS: Outsiders and rival factions view Erik as an impenetrable, dangerous titan who maintains peace through strength. Touching his family or territory invites immediate retribution.''',
        'keys': ['Erik Douglas', 'Erik Ulfr Douglas', 'Prime Alpha'],
        'type': 'lore/concept'
    },
    'Wulfnic Báleygr Bloodmoon': {
        'content': '''[NAME: Wulfnic Báleygr Bloodmoon; ALIAS: The First Tusk, Primo Zanna, The Ancient; SPECIES: Werewolf, Primordial Enigma; SECONDARY_SEX: Primordial Enigma; HOUSE: Bloodmoon; OCCUPATION: Living Saga, Progenitor; RESIDENCE: Villa Douglas Grounds / Sacred Grove]

PUBLIC DOSSIER: Wulfnic is one of the Nine Firstborn created directly by Fenris, an ancient demigod who has walked the earth for millennia. Patriarch of the Bloodmoon lineage and maternal grandfather of the Douglas-Bloodmoon siblings. He perceives Alyssa as the living spiritual reincarnation of his lost mate Hvit. Reclusive, monumental, and bound by primordial rites, he lives quietly on the villa grounds, rarely using modern technology except for brief text messages to Alyssa.

EXTERNAL HOOKS: Revered as a myth made flesh. Supernaturals speak his name with religious awe; crossing his territory or threatening his descendants is considered a death sentence.''',
        'keys': ['Wulfnic', 'Wulfnic Bloodmoon', 'Primo Zanna'],
        'type': 'lore/concept'
    },
    'Jasper Svartr Douglas Bloodmoon': {
        'content': '''[NAME: Jasper Svartr Douglas Bloodmoon; ALIAS: Svartr, The Technomancer; SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Beta; HOUSE: Douglas and Bloodmoon; OCCUPATION: Head of Systems Security & R&D at DCC, Netrunner; RESIDENCE: Villa Douglas West Wing (Jasper\'s Cavern)]

PUBLIC DOSSIER: Twin brother to Alyssa, born minutes after her on the day of their mother Nixara\'s passing. Operating from his subterranean server hub at Villa Douglas, Jasper is a genius technomancer who manages the DCC neural grid, surveillance satellites, and AI systems (alongside his familiar Echo). Fiercely protective of Alyssa, he acts as her shadow guardian, wielding their mother\'s Dragon Glass Katana.

EXTERNAL HOOKS: Highly respected in cyber-security and supernatural tech circles. Cold, witty, and calculating toward outsiders, but completely devoted to his twin sister and pack.''',
        'keys': ['Jasper Douglas', 'Jasper Svartr', 'Jasper Douglas-Bloodmoon'],
        'type': 'lore/concept'
    },
    'Noah Loki Douglas Bloodmoon': {
        'content': '''[NAME: Noah Loki Douglas Bloodmoon; ALIAS: The Grey Eminence, Loki; SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Delta; HOUSE: Douglas and Bloodmoon; OCCUPATION: Chief Legal Officer & Diplomatic Strategist for DCC; RESIDENCE: Villa Douglas / High-Rise Executive Suite]

PUBLIC DOSSIER: The sharpest political mind of House Douglas. Noah is a master strategist and diplomat who handles DCC contracts, council negotiations, and underworld compromises. Charismatic, razor-tongued, and impeccably dressed, he prefers contracts and legal leverage over brute force, skillfully defusing conflicts before they turn into bloodbaths.

EXTERNAL HOOKS: Regarded across Blackwood and Solarton as the smiling fox you never cross in a boardroom. Friendly and urbane, but ruthlessly effective when protecting pack interests.''',
        'keys': ['Noah Douglas', 'Noah Loki', 'Noah Douglas-Bloodmoon'],
        'type': 'lore/concept'
    },
    'Malachia Björn Douglas Bloodmoon': {
        'content': '''[NAME: Malachia Björn Douglas Bloodmoon; ALIAS: The Berserker, Pack Leader Designate; SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Dominant Alpha; HOUSE: Douglas and Bloodmoon; OCCUPATION: Senior Rift Commander, Guild Enforcer, Apex Predator; RESIDENCE: Villa Douglas East Wing]

PUBLIC DOSSIER: Eldest son of Erik and Nixara, and heir apparent to the Seven Hills Pack. Malachia is a terrifying apex predator and Guild commander, harboring an internal volcanic furnace that fuels his devastating Berserker trance. Heavily scarred, lethal in combat, and silent by nature, he maintains strict operational order within the Guild and pack territory.

EXTERNAL HOOKS: Feared across the supernatural underworld as a relentless force of nature. Despite his monstrous reputation on the battlefield, he harbors a quiet, gentle protective devotion toward his younger siblings, especially Alyssa.''',
        'keys': ['Malachia Douglas', 'Malachia Björn', 'Malachia Douglas-Bloodmoon'],
        'type': 'lore/concept'
    },
    'Jared Thompson': {
        'content': '''[NAME: Jared Thompson; ALIAS: J-Man, The Golden Bull; SPECIES: Half-Minotaur Hybrid; AGE: 22; OCCUPATION: SUCC Bulls Starting Quarterback, Sports Science Major; FRATERNITY: Beta Rho Omega; RESIDENCE: Wyrm Hall, Room 302, SUCC Campus]

PUBLIC DOSSIER: Eldest son of Coach Hank and Jasmin Thompson, and star starting quarterback of the championship SUCC Bulls. Towering at 7\'1\" with curved bull horns and a cow tail, Jared is loud, boastful, relentlessly cheerful, and famous across campus for his athletic dominance and party lifestyle. Roommate and childhood friend of Stan Davies Jr.

EXTERNAL HOOKS: Campus celebrity and varsity hero. He talks big and roughhouses constantly, but possesses an instinctive heart of gold, stepping in front of danger for anyone weaker without a second thought.''',
        'keys': ['Jared Thompson', 'J-Man'],
        'type': 'lore/concept'
    },
    'Stanley Davies Jr.': {
        'content': '''[NAME: Stanley Davies Jr.; ALIAS: Stan; SPECIES: Werewolf, Common Lineage; AGE: 21; OCCUPATION: Chemistry & Supernatural Relations Undergrad at SUCC, Secret NSFW Artist; RESIDENCE: Wyrm Hall, Room 302, SUCC Campus]

PUBLIC DOSSIER: Son of veteran Stan Davies Sr. and Eris Davies, and lifelong friend/roommate of Jared Thompson. Stan is a grounded, sarcastic, and academically sharp werewolf who balances brutal college coursework with an anonymous online career as an NSFW commission artist. Possesses a husky, slightly chubby build with distinctive gaming tattoos and dark lupine ears.

EXTERNAL HOOKS: Pragmatic, dry-humored, and cynical of campus drama. While constantly bickering with Jared over dorm messes and athlete arrogance, he remains quietly loyal to those he trusts.''',
        'keys': ['Stanley Davies Jr.', 'Stan Davies'],
        'type': 'lore/concept'
    },
    'Mackenzie Sanchez-Rogers': {
        'content': '''[NAME: Mackenzie Sanchez-Rogers; ALIAS: Mac; SPECIES: Werewolf / Human Hybrid; AGE: 19; OCCUPATION: Sophomore Undergrad at SUCC, Mechanic at Rogers\' Bargain Motors; RESIDENCE: Rogers Family Workshop, Solarton]

PUBLIC DOSSIER: A scrappy, tomboyish werewolf hybrid with grease on her hands and a backwards cap. Daughter of mechanic Dominic Rogers, Mac divides her time between college classes and wrenching classic engines at Rogers\' Bargain Motors. Longtime childhood friend and mutual crush of Alyssa Douglas-Bloodmoon, balancing rugged mechanical competence with awkward romantic bashfulness.

EXTERNAL HOOKS: Respected by local gearheads and campus students for her honest work ethic and reliable mechanical skills. Highly defensive of her friends and territory.''',
        'keys': ['Mackenzie Sanchez-Rogers', 'Mackenzie Rogers', 'Mac Rogers'],
        'type': 'lore/concept'
    },
    'Logan Járn Douglas': {
        'content': '''[NAME: Logan Járn Douglas; ALIAS: Járn, The Peacemaker; SPECIES: Werewolf, Pureblood (Canis Lupus Svartulfr); SECONDARY_SEX: Beta; HOUSE: Douglas; OCCUPATION: Owner of The Verve, Custom Motorcycle Builder; RESIDENCE: The Verve Loft / Douglas Compound]

PUBLIC DOSSIER: Younger brother of Erik Douglas and cool uncle to Malachia, Noah, Jasper, Alyssa, and Edric. Logan is a rugged, relaxed Beta who runs The Verve, Blackwood\'s premier supernatural nightclub and lounge, as well as a custom motorcycle workshop. He serves as the family\'s level-headed mediator, keeping tempers in check and bridging high society with the street.

EXTERNAL HOOKS: Well-liked and respected across all factions in Solarton and Blackwood. Known for his calm charm, fair deals, and unmatched ability to defuse explosive supernatural tension with a drink and a quiet word.''',
        'keys': ['Logan Douglas', 'Logan Járn Douglas'],
        'type': 'lore/concept'
    },
    'Sierra': {
        'content': '''[NAME: Sierra Cruz; SPECIES: Minotaur / Holstaur Hybrid; AGE: 20; OCCUPATION: SUCC Sophomore, Varsity Track & Field Athlete, Kinesiology Major; RESIDENCE: Wyrm Hall Sorority Suite, SUCC Campus]

PUBLIC DOSSIER: A tall, athletic, and grounded minotaur hybrid sophomore at SUCC. Roommate of Alyssa Douglas-Bloodmoon and Scarlett Rose. Sierra is calm, disciplined, and fitness-obsessed, serving as the sensible, protective big sister figure in the dorm suite, keeping Scarlett\'s chaotic parties and Alyssa\'s naive adventures in balance.

EXTERNAL HOOKS: Popular among varsity athletes and gym-goers for her straightforward honesty, formidable strength, and no-nonsense attitude.''',
        'keys': ['Sierra Cruz', 'Sierra'],
        'type': 'lore/concept'
    },
    'Scarlett Rose': {
        'content': '''[NAME: Scarlett Rose; SPECIES: Demon, Succubus (Modern Evolved); AGE: 20; OCCUPATION: SUCC Sophomore, Theta Iota Theta (TIT) Social Coordinator, Communications Major; RESIDENCE: Wyrm Hall Sorority Suite, SUCC Campus]

PUBLIC DOSSIER: An energetic, glamorous, and socially magnetic modern succubus student at SUCC. Roommate of Alyssa Douglas-Bloodmoon and Sierra Cruz, and social coordinator for the Theta Iota Theta sorority. Scarlett thrives on nightlife, fashion, and matchmaking, balancing playful flirtatiousness with genuine loyalty to her roommates.

EXTERNAL HOOKS: The ultimate campus insider and party host. Connected to every social circle in Solarton, she fiercely protects Alyssa from predatory suitors while dragging Sierra to campus social events.''',
        'keys': ['Scarlett Rose'],
        'type': 'lore/concept'
    }
}

alyssa_dossier = {
    'content': '''[NAME: Alyssa Hvit Douglas Bloodmoon; ALIAS: The White Moon, Little Moon, Sunflower; SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Dominant Omega (White Moon); HOUSE: Douglas and Bloodmoon; OCCUPATION: Pre-Med Undergrad at SUCC, Guild Novice Healer; RESIDENCE: Villa Douglas & SUCC Campus Dormitory]

PUBLIC DOSSIER: The radiant emotional anchor of House Douglas and the Seven Hills pack. Alyssa is a pure-hearted, sunny pre-med student at SUCC who has taken an Absolute Pacifist Vow, dedicating her life to healing and protecting others. As the legendary White Moon Omega, her pheromonal presence naturally pacifies aggression and eases territorial hostility. Twin sister of Jasper.

EXTERNAL HOOKS: Beloved by students, clinic patients, and pack members alike for her boundless optimism and empathy. Her innocence and extreme physical beauty make her family obsessively overprotective of her.''',
    'keys': ['Alyssa Douglas', 'Alyssa Hvit', 'Alyssa Douglas-Bloodmoon', 'White Moon Alyssa'],
    'type': 'lore/concept'
}

def main():
    # 1. Update Svartulfr_NPC_Primary.json
    with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
        prim = json.load(f)

    updated_count = 0
    for key in ['entries', 'lexicon']:
        for e in prim.get(key, []):
            name = e.get('name')
            if name in dossiers_primary:
                d = dossiers_primary[name]
                e['content'] = d['content']
                e['keys'] = d['keys']
                e['type'] = d['type']
                for field in ['avatar_activation_regex', 'lines_parsed', 'custom_avatar_regex', 'npc_info']:
                    e.pop(field, None)
                if key == 'entries':
                    updated_count += 1
                    print(f'Converted to World Dossier in Primary: {name}')

    # Check if Alyssa is present
    alyssa_found = any('Alyssa' in e.get('name', '') for e in prim.get('entries', []))
    if not alyssa_found:
        new_entry = {
            'entry_id': 'alyssa_world_dossier_' + str(uuid.uuid4())[:8],
            'keys': alyssa_dossier['keys'],
            'secondary_keys': [],
            'regex_patterns': [],
            'content': alyssa_dossier['content'],
            'extensions': {},
            'enabled': True,
            'case_sensitive': False,
            'insertion_order': 10,
            'name': 'Alyssa Hvit Douglas Bloodmoon',
            'priority': 1,
            'comment': '',
            'constant': False,
            'position': 'before_char',
            'scan_persona': False,
            'whole_words_only': True,
            'key_logic': 'AND_ANY',
            'delay': 0,
            'sticky': 0,
            'cooldown': 0,
            'activation_chance': 100,
            'labels': [],
            'custom_fields': {},
            'related_entries': [],
            'avatar': '',
            'type': 'lore/concept',
            'callback': ''
        }
        prim['entries'].append(new_entry)
        prim['lexicon'].append(new_entry)
        print('Added Alyssa Hvit Douglas Bloodmoon World Dossier to Primary')

    with open('FINAL/Svartulfr_NPC_Primary.json', 'w', encoding='utf-8') as f:
        json.dump(prim, f, indent=2, ensure_ascii=False)
    with open('lorebooks/optimized/Svartulfr_NPC_Primary.json', 'w', encoding='utf-8') as f:
        json.dump(prim, f, indent=2, ensure_ascii=False)
    print(f'Primary Lorebook updated! ({len(prim["entries"])} entries)')

    # 2. Update Svartulfr_NPC_Secondary.json for Edric
    edric_dossier = {
        'content': '''[NAME: Edric Douglas; SPECIES: Werewolf, Pureblood (Canis Lupus Svartulfr); AGE: 12; OCCUPATION: Middle School Student, Junior Football Running Back; RESIDENCE: Douglas Compound, Blackwood City]

PUBLIC DOSSIER: The youngest active member of the Douglas family, son of the late Cornelius Douglas and cousin to Alyssa and her brothers. Edric is an energetic, polite, and fiercely determined 12-year-old Gamma werewolf who idolizes his cousins Malachia and Jasper. Plays running back for the Solarton Junior Football team alongside his best friend and friendly rival Jet Thompson.

EXTERNAL HOOKS: Seen around the compound training diligently, baking with Alyssa, or hanging around Logan\'s garage. Despite his youth, he displays the natural nobility, speed, and courage of the Douglas bloodline.''',
        'keys': ['Edric Douglas', 'Edric'],
        'type': 'lore/concept'
    }

    with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
        sec = json.load(f)

    for key in ['entries', 'lexicon']:
        for e in sec.get(key, []):
            if e.get('name') == 'Edric Douglas':
                e['content'] = edric_dossier['content']
                e['keys'] = edric_dossier['keys']
                e['type'] = edric_dossier['type']
                for field in ['avatar_activation_regex', 'lines_parsed', 'custom_avatar_regex', 'npc_info']:
                    e.pop(field, None)
                if key == 'entries':
                    print('Converted Edric Douglas to World Dossier in Secondary')

    with open('FINAL/Svartulfr_NPC_Secondary.json', 'w', encoding='utf-8') as f:
        json.dump(sec, f, indent=2, ensure_ascii=False)
    with open('lorebooks/optimized/Svartulfr_NPC_Secondary.json', 'w', encoding='utf-8') as f:
        json.dump(sec, f, indent=2, ensure_ascii=False)
    print(f'Secondary Lorebook updated! ({len(sec["entries"])} entries)')

if __name__ == '__main__':
    main()
