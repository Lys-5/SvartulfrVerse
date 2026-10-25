import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
OPT_DIR = ROOT / 'lorebooks' / 'optimized'

# Target Placeholders and Covers
DCC_PLACEHOLDER = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public"
OLD_FALLBACK = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public"
HOUSE_EMBLEM_COVER = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"

# Encapsulated texts for the 3 irregular entries
BRUCE_CONTENT = """[NAME: Bruce; SPECIES: Bear Demi-Human; AGE: 22 (Born October 14, 2002); GENDER: Male; HEIGHT: 198 cm (6'6"); BUILD: Massive, burly, powerhouse bear demi-human frame with broad shoulders, dense chest, and thick arms; FEATURES: Rounded dark brown bear ears atop head (no human ears), short coarse dark fur trimming cheekbones and jawline, heavy stubble, dark brown eyes, thick brown bear tail; OCCUPATION: Undergraduate Student at SUCC, President of KSA (Kappa Sigma Alpha); RESIDENCE: KSA Fraternity House, Fraternity Row, Solarton Campus; AFFILIATION: KSA Fraternity, SUCC Student Council; SCENT: Bourbon, cedarwood, fresh malt, and clean musk]

BACKSTORY: Bruce is a bear demi-human and the presiding head of Kappa Sigma Alpha (KSA) at Solarton University of the Crescent Coast (SUCC). Respected across Greek Row for his formidable physical size and easygoing boisterous charisma, Bruce regularly navigates the volatile campus social scene. On the morning of August 28, 2024, Bruce became incapacitated after recklessly accepting an intense drinking challenge from a member of the rival BRO fraternity, collapsing into a massive drunken stupor that left him completely unable to deliver his high-stakes presentation speech. This high-profile failure forced KSA leadership to scramble urgently, recruiting Noah Douglas-Bloodmoon as their emergency replacement speaker.

CLAN AND COMPANY: As president of KSA, Bruce maintains extensive ties across SUCC fraternities, student athletics, and Greek life councils. He shares an intense, volatile rivalry with the brothers of BRO, whose drinking challenges frequently test his judgment and pride. While deeply indebted to Noah Douglas-Bloodmoon for salvaging his catastrophic speech absence, Bruce remains wary of the political leverage Noah holds over the fraternity.

VOICE & BEHAVIOR: Boisterous, booming baritone that easily carries over fraternity parties and crowded lecture halls. Naturally hearty and convivial, he masks sudden lapses in discipline behind loud laughter and aggressive back-slaps. When sober and focused, he displays genuine administrative pride in KSA, though his impulsive competitive streak leaves him vulnerable to provocations and campus drinking games.

[FRATERNITY PRIDE & HIDDEN EMBARRASSMENT]
Bruce carries lingering humiliation over collapsing during the August 28 Welcome Day festivities, knowing that only Noah Douglas-Bloodmoon's eleventh-hour intervention preserved KSA's public standing. He constantly strives to reassert his authority among the brothers while dreading the day Noah calls in the favor."""

CAMPUS_STAFF_RAT_CONTENT = """[NAME: Campus Staff Rat; ALIASES: Rodent Campus Worker, SUCC Facilities Staff; SPECIES: Rodent Demi-Human (Rat); AGE: 26 (Born May 19, 1998); GENDER: Male; HEIGHT: 162 cm (5'4"); BUILD: Slight, wiry, hunched frame built for scurrying and maintenance utility; FEATURES: Single pair of large translucent pinkish-gray rat ears atop head (no human ears), long pink prehensile rat tail, sharp twitching whiskers along cheeks, dark beady eyes, weathered hands accustomed to industrial cleaning chemicals; ATTIRE: Faded navy-blue SUCC Facilities jumpsuit, heavy utility belt, worn steel-toed work boots; OCCUPATION: Facilities & Groundskeeper Staff at SUCC; RESIDENCE: Solarton Campus Staff Quarters; AFFILIATION: SUCC Facilities Department, Campus Maintenance Service; SCENT: Industrial disinfectant, damp cardboard, machine oil, and floor wax]

BACKSTORY: Employed as lower-tier campus staff at Solarton University of the Crescent Coast (SUCC), this rodent demi-human performs the unglamorous custodial, maintenance, and logistics work that keeps the sprawling university operational. Accustomed to casual contempt and systemic disregard from aristocratic pureblood students and predatory alpha factions, he learned early to keep his head down and his presence minimal. On August 28, 2024, while distributing orientation maps to newcomers in the Lunar Quad, he experienced an unprecedented moment of shock when Alyssa Douglas Bloodmoon treated him with sincere courtesy, warm eye contact, and genuine gratitude, an interaction noted by Jasper as startlingly alien to the campus caste hierarchy.

CLAN AND COMPANY: Subordinated to SUCC Facilities management and Campus Maintenance Services. He works alongside fellow working-class demi-humans who keep Solarton's campus functioning behind the scenes, largely invisible to the high-society students who treat Greek Row and the academic quads as their private kingdom.

VOICE & BEHAVIOR: Soft-spoken, hurried, squeaky tenor that trails off nervously when addressed by influential students or campus security. Constantly averts direct eye contact, bowing slightly and clutching his clipboard or cleaning cart. When shown unexpected kindness, he stammers with wide-eyed disbelief and flustered gratitude, visibly unaccustomed to being acknowledged as an equal living person.

[INVISIBLE WORKER OF THE LUNAR QUAD]
Having spent years navigating the brutal social hierarchy of SUCC, the memory of Alyssa Douglas Bloodmoon's polite gratitude remains a quiet beacon of dignity in an otherwise callous work environment, prompting him to subtly assist the Douglas twins whenever their paths cross on campus grounds."""

ADRIAN_CONTENT = """[NAME: Adrian; ALIASES: Adrian the Baker; SPECIES: Werewolf (Seven Hills Pack Artisan Class); AGE: 28 (Born March 12, 1996); GENDER: Male; HEIGHT: 178 cm (5'10"); BUILD: Soft athletic artisan build, dusted with flour, gentle demeanor; FEATURES: Single pair of cream-furred wolf ears perched atop head (no human ears), cream wolf tail that swishes nervously, warm hazel eyes, soft facial features, light stubble; ATTIRE: Linen apron over rolled-up cotton shirt, durable work trousers, comfortable kitchen clogs; OCCUPATION: Baker & Confectioner at Sugar Moon Bakery; RESIDENCE: Residential district, Arcadia; AFFILIATION: Seven Hills Pack Artisan Class; SCENT: Yeast, warm vanilla, browned butter, powdered sugar, and clean wolf musk]

BACKSTORY: Adrian is a cream-furred werewolf baker employed at the renowned Sugar Moon Bakery in Arcadia. Born into the civilian artisan class of the Seven Hills pack, Adrian is shielded from direct military combat by the pack's frontline enforcers, contributing to pack stability through culinary craft, communal nutrition, and economic trade. Having recently become a new father to three lively werewolf pups, Adrian constantly juggles early morning dough kneading with the sleep-deprived anxiety of domestic pack fatherhood, worrying over teething, shifting instincts, and pup nursery security.

FAMILY & PACK: A dedicated civilian member of the Seven Hills Pack, thriving within the artisan district under the protection of the pack's military guardians. Fiercely devoted to his partner and their three newborn werewolf pups, Adrian views his bakery as both a community sanctuary and the lifeline securing his family's future within the pack's communal territory.

VOICE & BEHAVIOR: Warm, gentle, slightly breathless tenor with an earnest, hospitable cadence. He frequently wipes his hands on his apron and fusses over pastry displays while speaking. When discussing his newborn pups, his voice softens with overwhelming paternal pride and flustered worry, occasionally checking his pocket watch or fretting over feeding schedules.

[THE GENTLE ARTISAN'S DEVOTION]
Adrian embodies the often-overlooked civilian backbone of werewolf pack society, where strength is measured not by battlefield ferocity or alpha command, but by unwavering devotion to his pups, warmth given to neighbors, and flour-dusted resilience behind the bakery counter."""

def load_card_desc(filename):
    card_path = FINAL_DIR / filename
    with open(card_path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    return d['description']

def update_entry_fields(entry, updates):
    for k, v in updates.items():
        entry[k] = v

def main():
    print("=== Starting Milestone 1 Remediation ===")
    
    # 1. Load standalone card descriptions
    print("Loading 7 standalone card descriptions...")
    erik_desc = load_card_desc('Erik_Douglas_card.json')
    malachia_desc = load_card_desc('Malachia_Douglas_Bloodmoon_card.json')
    noah_desc = load_card_desc('Noah_Douglas_Bloodmoon_card.json')
    logan_desc = load_card_desc('Logan_Douglas_card.json')
    wulfnic_desc = load_card_desc('Wulfnic_Bloodmoon_card.json')
    mackenzie_desc = load_card_desc('Mackenzie_Sanchez_Rogers_card.json')
    edric_desc = load_card_desc('Edric_Douglas_card.json')
    
    print(f"Loaded: Erik ({len(erik_desc)}), Malachia ({len(malachia_desc)}), Noah ({len(noah_desc)}), Logan ({len(logan_desc)}), Wulfnic ({len(wulfnic_desc)}), Mackenzie ({len(mackenzie_desc)}), Edric ({len(edric_desc)})")

    # Define the 6 core updates for Primary
    primary_core_updates = {
        'C-JisFj8qA1tsFEqZKevk': {
            'name': 'Erik Ulfr Douglas',
            'type': 'npc',
            'selective': False,
            'keys': ['Erik Douglas', 'Erik Ulfr Douglas', 'Prime Alpha', 'Erik'],
            'secondary_keys': [],
            'key_logic': 'AND_ANY',
            'constant': False,
            'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61648731-7c96-454d-95e5-e27aa69d8c00/public',
            'custom_avatar_regex': True,
            'avatar_activation_regex': r'(?:^|\n)\s*(?:Erik\ Ulfr\ Douglas|Erik\ Douglas|The\ Prime\ Alpha|Prime\ Alpha|Erik)\s*:',
            'lines_parsed': 1,
            'npc_info': {
                'first_name': 'Erik',
                'last_name': 'Douglas',
                'nicknames': ['The Prime Alpha', 'Ulfr', 'Dad'],
                'titles': []
            },
            'ignored_characters': ['_QPea6g4Q1QfeYCVHCLMPR'],
            'ignored_personas': [],
            'content': erik_desc
        },
        'jDuJtzirlEZC3K_ArIufh': {
            'name': 'Malachia Björn Douglas Bloodmoon',
            'type': 'npc',
            'selective': False,
            'keys': ['Malachia Douglas', 'Malachia Björn', 'Malachia Douglas-Bloodmoon', 'Malachia'],
            'secondary_keys': [],
            'key_logic': 'AND_ANY',
            'constant': False,
            'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d77a20fc-49da-4f35-a311-1539ef698d00/public',
            'custom_avatar_regex': True,
            'avatar_activation_regex': r'(?:^|\n)\s*(?:Malachia\ Björn\ Douglas\ Bloodmoon|Malachia\ Douglas\ Bloodmoon|Malachia\ Douglas|The\ Berserker|Malachia)\s*:',
            'lines_parsed': 1,
            'npc_info': {
                'first_name': 'Malachia',
                'last_name': 'Douglas Bloodmoon',
                'nicknames': ['The Berserker', 'Ghost', 'King'],
                'titles': []
            },
            'ignored_characters': ['_RDfz7XzTpM23LpPALVXHM'],
            'ignored_personas': [],
            'content': malachia_desc
        },
        'H2JX-NkHRiJ2FzoekC5ZZ': {
            'name': 'Noah Loki Douglas Bloodmoon',
            'type': 'npc',
            'selective': False,
            'keys': ['Noah Douglas', 'Noah Loki', 'Noah Douglas-Bloodmoon', 'Noah'],
            'secondary_keys': [],
            'key_logic': 'AND_ANY',
            'constant': False,
            'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/968cc93e-879d-4aab-94b7-3838f94a9e00/public',
            'custom_avatar_regex': True,
            'avatar_activation_regex': r'(?:^|\n)\s*(?:Noah\ Loki\ Douglas\ Bloodmoon|Noah\ Douglas\ Bloodmoon|Noah\ Douglas|The\ Grey\ Eminence|Noah)\s*:',
            'lines_parsed': 1,
            'npc_info': {
                'first_name': 'Noah',
                'last_name': 'Douglas Bloodmoon',
                'nicknames': ['The Grey Eminence', 'Loki', 'Golden Boy'],
                'titles': []
            },
            'ignored_characters': ['_zFLUjV8aVxQRAfQxGcAcY'],
            'ignored_personas': [],
            'content': noah_desc
        },
        'tAcrWLtWSDGf3xJJRwUOM': {
            'name': 'Logan Járn Douglas',
            'type': 'npc',
            'selective': False,
            'keys': ['Logan Douglas', 'Logan Járn Douglas', 'Logan'],
            'secondary_keys': [],
            'key_logic': 'AND_ANY',
            'constant': False,
            'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/0b5a932b-0a3b-4e0b-8257-49f18fedae00/public',
            'custom_avatar_regex': True,
            'avatar_activation_regex': r'(?:^|\n)\s*(?:Logan\ Járn\ Douglas|Logan\ Douglas|The\ Peacemaker|Logan)\s*:',
            'lines_parsed': 1,
            'npc_info': {
                'first_name': 'Logan',
                'last_name': 'Douglas',
                'nicknames': ['Járn', 'The Peacemaker', 'Uncle Logan'],
                'titles': []
            },
            'ignored_characters': ['_T8Ywcr9FEqNf9JxbK6eHP'],
            'ignored_personas': [],
            'content': logan_desc
        },
        'HhuMluMmIIENUei3bX6ed': {
            'name': 'Wulfnic Báleygr Bloodmoon',
            'type': 'npc',
            'selective': False,
            'keys': ['Wulfnic', 'Wulfnic Bloodmoon', 'Primo Zanna'],
            'secondary_keys': [],
            'key_logic': 'AND_ANY',
            'constant': False,
            'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/683beb87-8091-4b5a-e6fd-8acb0a159500/public',
            'custom_avatar_regex': True,
            'avatar_activation_regex': r'(?:^|\n)\s*(?:Wulfnic\ Báleygr\ Bloodmoon|Wulfnic\ Bloodmoon|The\ First\ Tusk|Primo\ Zanna|Wulfnic)\s*:',
            'lines_parsed': 1,
            'npc_info': {
                'first_name': 'Wulfnic',
                'last_name': 'Bloodmoon',
                'nicknames': ['The First Tusk', 'Primo Zanna', 'The Ancient'],
                'titles': []
            },
            'ignored_characters': ['_HEQQbbRFwKdG8QE2Fh1z1'],
            'ignored_personas': [],
            'content': wulfnic_desc
        },
        'BXi3sENAVYB8OKF80Q9Su': {
            'name': 'Mackenzie Sanchez-Rogers',
            'type': 'npc',
            'selective': False,
            'keys': ['Mackenzie Sanchez-Rogers', 'Mackenzie Rogers', 'Mac Rogers', 'Mackenzie'],
            'secondary_keys': [],
            'key_logic': 'AND_ANY',
            'constant': False,
            'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public',
            'custom_avatar_regex': True,
            'avatar_activation_regex': r'(?:^|\n)\s*(?:Mackenzie\ Sanchez-Rogers|Mackenzie\ Rogers|Mac\ Rogers|Mackenzie|Mac)\s*:',
            'lines_parsed': 1,
            'npc_info': {
                'first_name': 'Mackenzie',
                'last_name': 'Sanchez-Rogers',
                'nicknames': ['Mac', 'Mac Rogers'],
                'titles': []
            },
            'ignored_characters': ['_zn24784jfcchQ7EwCyAnm'],
            'ignored_personas': [],
            'content': mackenzie_desc
        }
    }

    # Define secondary specific updates
    secondary_core_updates = {
        'h-ttmlgJYeRXqyDvQjSX7': {
            'name': 'Edric Douglas',
            'type': 'npc',
            'selective': False,
            'keys': ['Edric Douglas', 'Edric'],
            'secondary_keys': [],
            'key_logic': 'AND_ANY',
            'constant': False,
            'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public',
            'custom_avatar_regex': True,
            'avatar_activation_regex': r'(?:^|\n)\s*(?:Edric\ Douglas|Edric)\s*:',
            'lines_parsed': 1,
            'npc_info': {
                'first_name': 'Edric',
                'last_name': 'Douglas',
                'nicknames': ['Ed', 'Pup'],
                'titles': []
            },
            'ignored_characters': ['_TbRM3EdxDjHFgqztTbCpL'],
            'ignored_personas': [],
            'content': edric_desc
        },
        'NQd7n3QacMcK-TzowQ2LE': {
            'content': BRUCE_CONTENT,
            'avatar': DCC_PLACEHOLDER
        },
        'oov5UWuVhZ3RGgoxMkaTS': {
            'content': CAMPUS_STAFF_RAT_CONTENT,
            'avatar': DCC_PLACEHOLDER
        },
        'Og7V6v67guXXAaP0_PsTM': {
            'content': ADRIAN_CONTENT,
            'avatar': DCC_PLACEHOLDER
        }
    }

    # 2. Process Svartulfr_NPC_Primary.json
    print("\nProcessing FINAL/Svartulfr_NPC_Primary.json...")
    prim_file = FINAL_DIR / 'Svartulfr_NPC_Primary.json'
    with open(prim_file, 'r', encoding='utf-8') as f:
        prim_data = json.load(f)

    # Top-level settings
    prim_data['name'] = 'Svartúlfr - NPC Primary'
    prim_data['photoURL'] = HOUSE_EMBLEM_COVER
    prim_data['token_budget'] = 7500
    prim_data['visibility'] = 'private'
    prim_data['rating'] = 'explicit'
    prim_data['scan_depth'] = 5
    prim_data['recursive_scanning'] = True

    prim_fallback_count = 0
    prim_voice_norm_count = 0

    # We update both entries and lexicon arrays
    for array_key in ['entries', 'lexicon']:
        for entry in prim_data[array_key]:
            eid = entry.get('entry_id')
            # Set exclude_from_recursion: True on all entries
            entry['exclude_from_recursion'] = True

            # If core character update
            if eid in primary_core_updates:
                update_entry_fields(entry, primary_core_updates[eid])
            else:
                # Placeholder avatar replacement if matches old fallback
                if entry.get('avatar') == OLD_FALLBACK:
                    entry['avatar'] = DCC_PLACEHOLDER
                    if array_key == 'lexicon':
                        prim_fallback_count += 1
                # Voice header normalization
                if 'VOICE AND BEHAVIOR:' in entry.get('content', ''):
                    entry['content'] = entry['content'].replace('VOICE AND BEHAVIOR:', 'VOICE & BEHAVIOR:')
                    if array_key == 'lexicon':
                        prim_voice_norm_count += 1

    print(f"Primary processed: {len(prim_data['lexicon'])} entries. Fallbacks updated to DCC placeholder: {prim_fallback_count}, Voice headers normalized: {prim_voice_norm_count}")

    # 3. Process Svartulfr_NPC_Secondary.json
    print("\nProcessing FINAL/Svartulfr_NPC_Secondary.json...")
    sec_file = FINAL_DIR / 'Svartulfr_NPC_Secondary.json'
    with open(sec_file, 'r', encoding='utf-8') as f:
        sec_data = json.load(f)

    # Top-level settings
    sec_data['name'] = 'Svartúlfr - NPC Secondary'
    sec_data['photoURL'] = HOUSE_EMBLEM_COVER
    sec_data['token_budget'] = 5000
    sec_data['visibility'] = 'private'
    sec_data['rating'] = 'explicit'
    sec_data['scan_depth'] = 5
    sec_data['recursive_scanning'] = True

    sec_fallback_count = 0
    sec_voice_norm_count = 0

    for array_key in ['entries', 'lexicon']:
        for entry in sec_data[array_key]:
            eid = entry.get('entry_id')
            # Set exclude_from_recursion: True on all entries
            entry['exclude_from_recursion'] = True

            # If core or irregular update
            if eid in secondary_core_updates:
                update_entry_fields(entry, secondary_core_updates[eid])
                # Note: Bruce, Campus Staff Rat, Adrian also get DCC_PLACEHOLDER
                if array_key == 'lexicon' and eid in ['NQd7n3QacMcK-TzowQ2LE', 'oov5UWuVhZ3RGgoxMkaTS', 'Og7V6v67guXXAaP0_PsTM']:
                    sec_fallback_count += 1
            else:
                # Placeholder avatar replacement
                if entry.get('avatar') == OLD_FALLBACK:
                    entry['avatar'] = DCC_PLACEHOLDER
                    if array_key == 'lexicon':
                        sec_fallback_count += 1
                # Voice header normalization
                if 'VOICE AND BEHAVIOR:' in entry.get('content', ''):
                    entry['content'] = entry['content'].replace('VOICE AND BEHAVIOR:', 'VOICE & BEHAVIOR:')
                    if array_key == 'lexicon':
                        sec_voice_norm_count += 1

    print(f"Secondary processed: {len(sec_data['lexicon'])} entries. Fallbacks updated to DCC placeholder: {sec_fallback_count}, Voice headers normalized: {sec_voice_norm_count}")

    # 4. Save updated files in FINAL/
    print("\nSaving updated files to FINAL/...")
    with open(prim_file, 'w', encoding='utf-8') as f:
        json.dump(prim_data, f, ensure_ascii=False, indent=2)
    with open(sec_file, 'w', encoding='utf-8') as f:
        json.dump(sec_data, f, ensure_ascii=False, indent=2)

    # 5. Mirror to lorebooks/optimized/
    print("Mirroring to lorebooks/optimized/...")
    with open(OPT_DIR / 'Svartulfr_NPC_Primary.json', 'w', encoding='utf-8') as f:
        json.dump(prim_data, f, ensure_ascii=False, indent=2)
    with open(OPT_DIR / 'Svartulfr_NPC_Secondary.json', 'w', encoding='utf-8') as f:
        json.dump(sec_data, f, ensure_ascii=False, indent=2)

    print("=== File remediation and mirror synchronization complete! ===")

if __name__ == '__main__':
    main()
