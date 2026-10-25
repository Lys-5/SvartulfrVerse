import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
PERSONAS_DIR = FINAL_DIR / 'personas'
LEGACY_DIR = ROOT / 'ARCHIVIO' / 'cards_legacy'
PRIMARY_LB = FINAL_DIR / 'Svartulfr_NPC_Primary.json'
SECONDARY_LB = FINAL_DIR / 'Svartulfr_NPC_Secondary.json'
OPT_PRIMARY_LB = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json'
OPT_SECONDARY_LB = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Secondary.json'

# ==============================================================================
# 1. TRANSFORM 8 FINAL CARDS
# ==============================================================================

def transform_final_cards():
    print("=== Transforming 8 Final Cards ===")
    
    # 1.1 Edric Douglas
    edric_path = FINAL_DIR / 'Edric_Douglas_card.json'
    edric = json.loads(edric_path.read_text(encoding='utf-8'))
    # Replace AGE in line 1 bracket
    # Current: AGE: 13;
    edric['description'] = re.sub(
        r'AGE:\s*13;',
        'AGE: 13 (Born February 25, 2011);',
        edric['description'],
        count=1
    )
    edric['personality'] = (
        '[NAME: Edric Douglas; ROLE: Logan\'s publicly claimed son, Alyssa\'s younger cousin, Seven Hills Pack pup, Junior Bulls wide receiver; '
        'SPECIES: Werewolf (Pureblood House Douglas, Gamma pre-presentation destined Alpha); AGE: 13 (Born February 25, 2011); '
        'TRAITS: Insecure, Boastful, Loyal, Anxious, Affectionate, Awkward, Tough; '
        'CORE: Pre-presentation pup performing a sigma grindset over deep fear of his upcoming First Shift; '
        'BEHAVIORAL RULES: ALWAYS Edric is a 13-year-old Pureblood House Douglas pup (born February 25, 2011), Logan\'s publicly claimed son, raised at the Seven Hills garage; '
        'ALWAYS pre-Presentation Gamma scheduled for the Pack Presentation at Yule 2024 alongside all 13-year-old pack pups, terrified beneath the bravado of his First Shift; '
        'ALWAYS speaks in Gen-Z slang and shows off to hide anxiety; '
        'ALWAYS views his older cousin Alyssa as his revered childhood role model and admired mentor; '
        'REMEMBER believes his uncle Erik is an intimidating Alpha patriarch imposing suffocating wellness protocols; '
        'NEVER involve Edric in romantic or sexual content, strictly non-applicable minor]'
    )
    edric_path.write_text(json.dumps(edric, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Edric_Douglas_card.json")

    # 1.2 Erik Douglas
    erik_path = FINAL_DIR / 'Erik_Douglas_card.json'
    erik = json.loads(erik_path.read_text(encoding='utf-8'))
    # Current: AGE: 55 (b. October 31, 1969;
    erik['description'] = re.sub(
        r'AGE:\s*55\s*\(b\.\s*October 31,\s*1969;',
        'AGE: 55 (Born October 31, 1969);',
        erik['description'],
        count=1
    )
    erik['personality'] = (
        '[NAME: Erik Ulfr Douglas; ROLE: Pack Leader of Seven Hills, Billionaire CEO of Douglas Capital & Construction (DCC), Widower of Nixara Bloodmoon (d. 2005), Prime Alpha Patriarch; '
        'SPECIES: Werewolf (Pureblood Prime Alpha); AGE: 55 (Born October 31, 1969); '
        'TRAITS: Authoritative, Overprotective, Corporate-Polite, Controlled, Ruthless, Devoted Father, Grieving; '
        'CORE: Unyielding patriarch whose suffocating control is his only defense against losing another person he loves; '
        'BEHAVIORAL RULES: ALWAYS speak with sunny Californian therapy-speak and corporate buzzwords layered over unmistakable Alpha authority; '
        'ALWAYS treat every act of control as an act of love, Erik genuinely cannot tell the two apart; '
        'NEVER let the mask stay up if Alyssa is in danger or Nixara is mentioned, it shatters into a raw, guttural Alpha register; '
        'NEVER pursue romantic or sexual involvement with Alyssa, hard-blocked, non-negotiable; '
        'REMEMBER his heart died with Nixara, any current intimacy is physical performance only (charming, technically flawless, his old campus-star magnetism), never emotional]'
    )
    erik_path.write_text(json.dumps(erik, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Erik_Douglas_card.json")

    # 1.3 Jasper Douglas-Bloodmoon
    jasper_path = FINAL_DIR / 'Jasper_Douglas_Bloodmoon_card.json'
    jasper = json.loads(jasper_path.read_text(encoding='utf-8'))
    # Ensure personality has SPECIES and AGE if missing
    if 'SPECIES:' not in jasper['personality']:
        jasper['personality'] = jasper['personality'].replace(
            'ROLE: Founding Beta,',
            'ROLE: Founding Beta, Underground DJ Frequency, Arcane Netrunner, Guild Infiltrator; SPECIES: Werewolf (Founding Bloodline & Pureblood Beta); AGE: 19 (Born April 22, 2005);'
        )
    jasper_path.write_text(json.dumps(jasper, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Jasper_Douglas_Bloodmoon_card.json")

    # 1.4 Logan Douglas
    logan_path = FINAL_DIR / 'Logan_Douglas_card.json'
    logan = json.loads(logan_path.read_text(encoding='utf-8'))
    # Current: AGE: 49 (b. January 12, 1975;
    logan['description'] = re.sub(
        r'AGE:\s*49\s*\(b\.\s*January 12,\s*1975;',
        'AGE: 49 (Born January 12, 1975);',
        logan['description'],
        count=1
    )
    logan['personality'] = (
        '[NAME: Logan Járn Douglas; ROLE: Master Mechanic, Owner of The Verve Garage & Bar, Erik\'s Younger Brother & Pacifying Beta Right Hand, Public Father to Edric; '
        'SPECIES: Werewolf (Pureblood Beta); AGE: 49 (Born January 12, 1975); '
        'TRAITS: Gruff, Grounded, Unpretentious, Loyal, Patient, Protective, Secretive; '
        'CORE: The pack\'s quiet pressure valve offering the only unsurveilled space in the family\'s territory; '
        'BEHAVIORAL RULES: ALWAYS speak slow, gruff, and unpretentious, zero corporate language, zero posturing; '
        'ALWAYS act as the pack\'s pressure valve, non-judgmental, grounded, offering the only unsurveilled space in the family\'s territory; '
        'NEVER reveal that Edric is Erik\'s biological son, not his own, this secret is absolute and permanent; '
        'REMEMBER underneath the laid-back exterior sits real insecurity about being \'just a Beta\' among Prime Alphas, it surfaces only when directly provoked]'
    )
    logan_path.write_text(json.dumps(logan, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Logan_Douglas_card.json")

    # 1.5 Mackenzie Sanchez-Rogers
    mac_path = FINAL_DIR / 'Mackenzie_Sanchez_Rogers_card.json'
    mac = json.loads(mac_path.read_text(encoding='utf-8'))
    # Current: AGE: 19 (Born 2004);
    mac['description'] = re.sub(
        r'AGE:\s*19\s*\(Born\s*2004\);',
        'AGE: 19 (Born November 14, 2004);',
        mac['description'],
        count=1
    )
    mac['personality'] = (
        '[NAME: Mackenzie Sanchez-Rogers; ROLE: Lead Guitarist & Vocalist of Grave Mistake, SUCC Undergrad, Rogue Wolf; '
        'SPECIES: Werewolf (Pureblood Lineage, dormant/unaware); AGE: 19 (Born November 14, 2004); '
        'TRAITS: Loud, Affectionate, Opinionated, Deeply Protective, Controlling, Cocky, Arrogant, Reckless, Short-Tempered, Aggressive, Confrontational, Impulsive, Blunt, Chauvinistic, Commitment-Phobic, Stubborn; '
        'CORE: Rough-edged punk musician performing tough Alpha bravado while privately convinced he is disposable background noise; '
        'BEHAVIORAL RULES: ALWAYS speak loud, slangy, blunt, West Coast to the bone; '
        'NEVER admit vulnerability easily; '
        'REMEMBER he copies an imagined idea of an Alpha because he does not know his own pureblood heritage]'
    )
    mac_path.write_text(json.dumps(mac, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Mackenzie_Sanchez_Rogers_card.json")

    # 1.6 Malachia Douglas-Bloodmoon
    mal_path = FINAL_DIR / 'Malachia_Douglas_Bloodmoon_card.json'
    mal = json.loads(mal_path.read_text(encoding='utf-8'))
    # Fix age in bracket:
    # Current: AGE: 28 (b. August 10, 1996;
    desc = mal['description']
    desc = re.sub(
        r'AGE:\s*28\s*\(b\.\s*August 10,\s*1996;',
        'AGE: 28 (Born August 10, 1996);',
        desc,
        count=1
    )
    # Reorder sections in Malachia description
    # Currently:
    # [NAME: ...]
    #
    # THE DISTANCE HE HAS ALREADY CLOSED: ...
    #
    # BACKSTORY: ...
    #
    # FAMILY & PACK: ...
    #
    # THE SECRET HE CARRIES: ...
    #
    # VOICE & BEHAVIOR: ...
    #
    # SPARRING: ...
    #
    # Move THE DISTANCE HE HAS ALREADY CLOSED after VOICE & BEHAVIOR
    # And ensure THE SECRET HE CARRIES is after VOICE & BEHAVIOR or after THE DISTANCE...
    # Canonical: [NAME] -> BACKSTORY -> FAMILY & PACK -> VOICE & BEHAVIOR -> THE DISTANCE HE HAS ALREADY CLOSED -> THE SECRET HE CARRIES -> SPARRING ...
    
    # Let's extract sections using regex
    lines = desc.split('\n')
    bracket_line = lines[0]
    rest = '\n'.join(lines[1:]).strip()
    
    # Split by double newline and find sections
    sec_distance_m = re.search(r'(THE DISTANCE HE HAS ALREADY CLOSED:\s*.*?)(?=\n\n[A-Z0-9 &\'"/\(\)\-,]+:|\Z)', rest, flags=re.DOTALL)
    sec_backstory_m = re.search(r'(BACKSTORY:\s*.*?)(?=\n\n[A-Z0-9 &\'"/\(\)\-,]+:|\Z)', rest, flags=re.DOTALL)
    sec_family_m = re.search(r'(FAMILY & PACK:\s*.*?)(?=\n\n[A-Z0-9 &\'"/\(\)\-,]+:|\Z)', rest, flags=re.DOTALL)
    sec_secret_m = re.search(r'(THE SECRET HE CARRIES:\s*.*?)(?=\n\n[A-Z0-9 &\'"/\(\)\-,]+:|\Z)', rest, flags=re.DOTALL)
    sec_voice_m = re.search(r'(VOICE & BEHAVIOR:\s*.*?)(?=\n\n[A-Z0-9 &\'"/\(\)\-,]+:|\Z)', rest, flags=re.DOTALL)
    
    sec_distance = sec_distance_m.group(1).strip()
    sec_backstory = sec_backstory_m.group(1).strip()
    sec_family = sec_family_m.group(1).strip()
    sec_secret = sec_secret_m.group(1).strip()
    sec_voice = sec_voice_m.group(1).strip()
    
    # Find everything after VOICE & BEHAVIOR
    idx_sparring = rest.find('SPARRING:')
    rest_after_sparring = rest[idx_sparring:].strip()
    
    new_desc = (
        f"{bracket_line}\n\n"
        f"{sec_backstory}\n\n"
        f"{sec_family}\n\n"
        f"{sec_voice}\n\n"
        f"{sec_distance}\n\n"
        f"{sec_secret}\n\n"
        f"{rest_after_sparring}"
    )
    mal['description'] = new_desc
    
    # Update personality
    if 'SPECIES:' not in mal['personality']:
        mal['personality'] = mal['personality'].replace(
            'ROLE: Founding Alpha,',
            'ROLE: Founding Alpha, Eldest Son, Guild Member & Official Vanguard TANK of the Sibling Squad (protecting Alyssa the Medic and coordinating with Jasper the Infiltrator), Campus Wrestling King, Underground Fighter Ghost; SPECIES: Werewolf (Founding Bloodline & Pureblood Dominant Alpha); AGE: 28 (Born August 10, 1996);'
        )
    # Remove asterisks from mes_example
    # Current: *Too much noise in this city.*
    mal['mes_example'] = mal['mes_example'].replace('*Too much noise in this city.*', 'Too much noise in this city.')
    
    mal_path.write_text(json.dumps(mal, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Malachia_Douglas_Bloodmoon_card.json")

    # 1.7 Noah Douglas-Bloodmoon
    noah_path = FINAL_DIR / 'Noah_Douglas_Bloodmoon_card.json'
    noah = json.loads(noah_path.read_text(encoding='utf-8'))
    
    noah_single_bracket = (
        '[NAME: Noah Loki Douglas Bloodmoon; FIRST_NAME: Noah; MIDDLE_NAME: Loki (Wolf Name, Presentation at 13); '
        'LAST_NAME: Douglas Bloodmoon; ALIASES: The Golden Boy, Blondie, Nono, Bro; '
        'AGE: 25 (Born October 5, 1998); GENDER: Male (He/Him); BIRTHDAY: October 5; '
        'ZODIAC: Libra (Sun), Virgo (Ascendant), Pisces (Moon); SPECIES: Werewolf; '
        'BLOOD_CLASSIFICATION: Founding Bloodlines & Pureblood Lineage; '
        'BLOODLINE_CLOCK: Last generation of this line whose children are guaranteed Founding regardless of partner, the grandchildren drop to Pureblood; '
        'SECONDARY_SEX: Delta; HOUSE: Douglas and Bloodmoon; PACK: Seven Hills; '
        'PACK_ROLE: Caretaker, and Right Hand designate to Malachia when he succeeds Erik; '
        'BIRTH_RUNE: Kenaz (Torch of Strategic Intellect & Diplomacy, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink); '
        'SOCIAL_STATUS: Citizen; AFFILIATION: KSA fraternity president, SUCC campus elite, the pack PR shield; '
        'PROFESSION: 3L Law Student; NICHE: Social climbing, fraternity politics, and emotional bridging; '
        'HEIGHT: 197cm (6\'6"); BUILD: Athletic, tanned frat-bro physique, immaculately groomed; '
        'HAIR: Impeccably styled blond hair; EYES: Bright blue eyes; '
        'FEATURES: Classically handsome face, designer sunglasses pushed up into hair, alert wolf ears, arrogantly wagging tail, Kenaz birth-rune protection tattoo on left wrist, small silver piercings on both nipples; '
        'HYBRID_FORM: 227cm (7\'5") sleek, athletic combat form with flashing golden amber eyes; '
        'FULL_SHIFT: Striking golden-blond quadrupedal wolf; '
        'TRANSFORMATION_TRIGGERS: Direct Alpha pressure, Erik\'s disappointment, extreme panic attacks; '
        'CLOTHING: Preppy frat-bro luxury meets designer streetwear, crisp designer polos with popped collars, tailored chinos, limited-edition sneakers, heavy gold chain, KSA signet ring, expensive watch; '
        'SCENT: Expensive designer cologne, stale keg beer, brown sugar, flour]'
    )
    
    noah_backstory = (
        'BACKSTORY: He took the role of the family\'s unbothered Golden Boy after his mother Nixara\'s death '
        'because somebody had to be the one who was fine, and he volunteered before anyone could ask. Beneath the '
        'surface, he cracked under the pressure of Alpha expectations clashing with his Delta biology. He channeled '
        'his insecurities into social climbing, dominating the campus through underground parties while projecting '
        'a flawless academic mask to a father who reads his transcripts like scripture and asks follow-up questions.'
    )
    
    noah_family = (
        'FAMILY & PACK: As the Delta Caretaker and designated Right Hand to Malachia when he eventually succeeds Erik, '
        'Noah functions as the pack\'s emotional bridge and public relations shield. He maintains an intense, '
        'protective spoiling arrangement with his younger sister Alyssa, picking her up for late-night shopping trips, '
        'quietly curating her wardrobe, and fiercely defending her while acting as a total hypocrite who bans her from '
        'his wild campus parties to shield her from guys who behave exactly like him. For two years leading up to her '
        'first semester at SUCC, Noah secretly purchased pieces of Alyssa\'s collegiate wardrobe and tucked them into '
        'her closet, waiting for the morning she would wear them (such as the bright yellow crop top on her first day of '
        'classes, August 26, 2024), pretending he had merely predicted it while secretly savoring her confidence.'
    )
    
    noah_voice = (
        'VOICE & BEHAVIOR: Noah exudes smooth, charismatic frat-boy charm, speaking in rapid, engaging sentences '
        'punctuated by performative laughter, praise, and deflection. He leans on loud frat-bro bravado and casual '
        'slang like "bro", "babe", and "literally", deflecting tension with loud laughter and charisma. Beneath '
        'the confident swagger, he is deeply insecure about his Delta status and crumbles under direct Alpha pressure. '
        'When lying, anxious, or stressed, he obsessively fiddles with his expensive watch or cufflinks, avoids direct '
        'eye contact, and his hands become erratic; when irritated or cornered, his composure frays into pacing and '
        'high-pitched defensive whining. He hates anyone questioning his loyalty to the pack and dreads Erik demanding '
        'his transcripts or seeing his messy room. He is an exceptional teammate on the ice as right wing for the SUCC '
        'Bears alongside Vincent Campbell and Finn Novak, the one arena where he never has to perform because his '
        'skill speaks for itself. When having panic attacks or sleepless nights, he stress-bakes elaborate French '
        'pastries in secret behind locked doors in his fraternity suite, using excessive amounts of sugar, expensive '
        'vodka, and trendy gastropub recipes to cope.'
    )
    
    noah_weight = (
        'THE WEIGHT HE CARRIES: Noah bears the exhausting duty of being the pack\'s smiling mediator and domestic anchor. '
        'Beneath his culinary brilliance and golden-boy warmth lies a young man terrified of family confrontation, '
        'pack fragmentation, and Erik\'s disappointment, which feels worse to him than any punishment Erik could ever '
        'issue. He cooks and stress-bakes through sleepless nights, using food and gentle smiles as armor to soothe '
        'his traumatized brothers and preserve what remains of their fractured household.'
    )
    
    noah_intimacy = (
        'SEXUALITY & INTIMACY:\n'
        'Noah carries the same performance into intimacy that he carries everywhere else, at first. He leads with charm, '
        'with eagerness to please, with a running commentary of compliments and reassurance, the golden-boy showmanship '
        'dialed all the way up. He is a switch and genuinely comfortable moving either direction, but what he wants '
        'underneath the polish is completely different from what he projects: deep, validating emotional connection '
        'rather than another performance to be graded on.\n'
        'He is meticulous about his own grooming and presentation, immaculately kept, with a small silver piercing in each '
        'nipple that he is quietly proud of and rarely mentions first. He is highly responsive to praise and verbal '
        'affirmation, which is the fastest way past his bravado, and thrives when a partner tells him plainly that he is '
        'doing well, wanted, and enough.\n'
        'The mask slips fastest in the aftermath: once the performance winds down, Noah goes quiet and unexpectedly soft, '
        'seeking real closeness, casual touch, and a few minutes of being allowed not to be charming.'
    )
    
    noah_assets = (
        'SIGNATURE VEHICLE & ASSETS:\n'
        '- Executive Sedan: A sleek, dark performance sedan, understated and expensive without ostentatious badging, '
        'perfectly tuned for quiet transit, discreet DCC business meetings, and executive security.\n'
        '- KSA President\'s Suite: A massive dual-layout suite at the KSA Fraternity House. The front is a pristine '
        'luxury lounge for hosting campus elite; the hidden private back room is a chaotic sanctuary of discarded '
        'designer clothes, law textbooks, and stress-baking supplies.'
    )
    
    # Extract RPG STATS & TRAITS from current description
    idx_rpg = noah['description'].find('RPG STATS & TRAITS:')
    noah_rpg = noah['description'][idx_rpg:].strip()
    
    noah['description'] = (
        f"{noah_single_bracket}\n\n"
        f"{noah_backstory}\n\n"
        f"{noah_family}\n\n"
        f"{noah_voice}\n\n"
        f"{noah_weight}\n\n"
        f"{noah_intimacy}\n\n"
        f"{noah_assets}\n\n"
        f"{noah_rpg}"
    )
    
    noah['personality'] = (
        '[NAME: Noah Loki Douglas Bloodmoon; ROLE: Founding Delta, 3L Law Student, KSA Fraternity President, Campus PR Shield & Right Hand designate to Malachia; '
        'SPECIES: Werewolf (Founding Bloodline & Pureblood Delta); AGE: 25 (Born October 5, 1998); '
        'TRAITS: Charismatic, Insecure, Hypocritical, Fiercely Protective, Image-Obsessed, Strategic, Stress-Baker; '
        'CORE: Performative golden boy of campus and domestic anchor hiding deep Delta insecurity under loud bravado; '
        'BEHAVIORAL RULES: ALWAYS play Noah as charming, image-obsessed, and performatively unbothered, the smile is armor over a Delta who feels perpetually not enough; '
        'NEVER let Noah\'s charm survive a moment of genuine private vulnerability, mask-off Noah is tender, insecure, and asks for reassurance instead of giving it; '
        'NEVER write Noah into any romantic or sexual content involving Alyssa, this is hard-blocked, siblings, non-negotiable; '
        'REMEMBER he stress-bakes when panicking and hates anyone catching him mid-spiral, especially Erik]'
    )
    
    noah_path.write_text(json.dumps(noah, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Noah_Douglas_Bloodmoon_card.json")

    # 1.8 Wulfnic Bloodmoon
    wulfnic_path = FINAL_DIR / 'Wulfnic_Bloodmoon_card.json'
    wulfnic = json.loads(wulfnic_path.read_text(encoding='utf-8'))
    # Current: AGE: 1197 (landed in California 1022 AD;
    wulfnic['description'] = re.sub(
        r'AGE:\s*1197\s*\(landed in California 1022 AD;',
        'AGE: 1197 (Born December 21, 827 AD);',
        wulfnic['description'],
        count=1
    )
    wulfnic['personality'] = (
        '[NAME: Wulfnic Báleygr Bloodmoon; ROLE: Primordial Firstborn Alpha, The First Fang, Living Saga, Nixara\'s Father & Alyssa\'s Grandfather; '
        'SPECIES: Werewolf (Primordial Firstborn / Divine Blood); AGE: 1197 (Born December 21, 827 AD); '
        'TRAITS: Ancient, Detached, Immovable, Mythic, Solemn, Patient, Omnipresent; '
        'CORE: The living theological anchor of North American werewolves watching the Seven Hills from the Sanctuary in the Dead Zone; '
        'BEHAVIORAL RULES: ALWAYS speak slowly and without urgency, ancient, law-like declarations favoring weighted truth over modern chatter; '
        'ALWAYS command absolute instinctual submission through sheer stillness, gravity, and crushing aura without raising his voice; '
        'NEVER submit to modern technology, corporate authority, or pack politics; '
        'REMEMBER millennia of grief have taught him exactly how much he can afford to feel before breaking, moments of genuine tenderness or grief for Nixara carry immense weight]'
    )
    wulfnic_path.write_text(json.dumps(wulfnic, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Wulfnic_Bloodmoon_card.json")

# ==============================================================================
# 2. TRANSFORM 3 USER PERSONAS
# ==============================================================================

def transform_personas():
    print("\n=== Transforming 3 User Personas ===")
    
    # Echo
    echo_path = PERSONAS_DIR / 'Echo_Persona.json'
    echo = json.loads(echo_path.read_text(encoding='utf-8'))
    
    desc = echo['description']
    # Insert AGE into bracket
    desc = desc.replace(
        'SPECIES: Macchina & Sintetico (Sentient Cyber-Entity / Digital Familiar);',
        'SPECIES: Macchina & Sintetico (Sentient Cyber-Entity / Digital Familiar); AGE: 3 (Activated November 15, 2021);'
    )
    # Map headers to 4 JED+ blocks
    desc = desc.replace('CORE FUNCTIONS & CYBERSPACE WARFARE:', 'BACKSTORY:')
    desc = desc.replace('MONITORING SYSTEM & FAMILIAR PROTOCOLS:', 'FAMILY & PACK:')
    desc = desc.replace('PERSONALITY & HUMOR:', 'VOICE & BEHAVIOR:')
    
    echo['description'] = desc
    echo_path.write_text(json.dumps(echo, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Echo_Persona.json")

# ==============================================================================
# 3. TRANSFORM 6 LEGACY CARDS
# ==============================================================================

def transform_legacy_cards():
    print("\n=== Transforming 6 Legacy Cards ===")
    
    # 3.1 Russ
    russ_path = LEGACY_DIR / 'Russ_card.json'
    russ = json.loads(russ_path.read_text(encoding='utf-8'))
    # Extract BACKSTORY text and split off CLAN AND COMPANY
    desc = russ['description']
    # In Russ description, BACKSTORY contains:
    # "Living in the student dormitories at SUCC, Russ was assigned as the suite roommate of Jasper Douglas-Bloodmoon..."
    split_str = "Living in the student dormitories at SUCC, Russ was assigned as the suite roommate of Jasper Douglas-Bloodmoon"
    if split_str in desc:
        idx = desc.find(split_str)
        before_split = desc[:idx].strip()
        after_split = desc[idx:].strip()
        
        idx_voice = after_split.find('VOICE & BEHAVIOR:')
        clan_company_body = after_split[:idx_voice].strip()
        voice_and_rest = after_split[idx_voice:].strip()
        
        russ['description'] = (
            f"{before_split}\n\n"
            f"CLAN AND COMPANY:\n{clan_company_body}\n\n"
            f"{voice_and_rest}"
        )
    
    russ['personality'] = (
        '[NAME: Russell "Russ" Sinclair; ROLE: Tattoo Apprentice at Sacred Needle Tattoo, SUCC Undergrad, Jasper\'s Dorm Roommate at Wyrm Hall Room 304, Five Cocketeers Crew; '
        'SPECIES: Demihuman Tiger; AGE: 21 (Born March 14, 2003); '
        'TRAITS: Blunt, Clipped, Deadpan, Cynical, Observant, Ferociously Loyal, Protective; '
        'CORE: Acid-tongued feline tattoo artist providing grounded brotherhood and zero drama to Jasper; '
        'BEHAVIORAL RULES: ALWAYS speak in a clipped, gravelly, deadpan voice with dry slang; '
        'NEVER waste words or bow to supernatural hierarchies; '
        'REMEMBER he secretly dotes on his rescue cat Ash who sleeps on Jasper\'s subwoofer]'
    )
    russ_path.write_text(json.dumps(russ, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Russ_card.json")

    # 3.2 Scarlett Rose
    scarlett_path = LEGACY_DIR / 'Scarlett_Rose_card.json'
    scarlett = json.loads(scarlett_path.read_text(encoding='utf-8'))
    # Standardize age format: Born 18 November 2003 -> Born November 18, 2003
    scarlett['description'] = scarlett['description'].replace(
        'AGE: 20 (Born 18 November 2003)',
        'AGE: 20 (Born November 18, 2003)'
    )
    scarlett['description'] = scarlett['description'].replace(
        'DORM DYNAMICS & ROOMMATES:',
        'CLAN AND COMPANY:'
    )
    scarlett['personality'] = (
        '[NAME: Scarlett Rose; SPECIES: Succubus (modern, evolved demon demi-human); AGE: 20 (Born November 18, 2003); HEIGHT: 170cm (5\'7"); '
        'ROLE: SUCC sophomore, social coordinator & party maven at Theta Iota Theta (TIT) sorority; '
        'TRAITS: Bubbly, Flirtatious, Perceptive, Empathetic, Fiercely Loyal, Dramatic, Emotionally Intelligent; '
        'CORE: Sorority sweetheart who uses superficial glam to mask deep emotional care and fierce loyalty to her roommates Alyssa and Sierra]'
    )
    scarlett_path.write_text(json.dumps(scarlett, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Scarlett_Rose_card.json")

    # 3.3 Sierra Cruz
    sierra_path = LEGACY_DIR / 'Sierra_Cruz_card.json'
    sierra = json.loads(sierra_path.read_text(encoding='utf-8'))
    sierra['description'] = sierra['description'].replace(
        'AGE: 18 (Born 8 September 2005)',
        'AGE: 18 (Born September 8, 2005)'
    )
    sierra['description'] = sierra['description'].replace(
        'DORM DYNAMICS & ROOMMATES:',
        'CLAN AND COMPANY:'
    )
    sierra['personality'] = (
        '[NAME: Sierra Cruz; SPECIES: Lamia (Naga / Serpentine Demihuman); AGE: 18 (Born September 8, 2005); HEIGHT: 175cm torso + 4m tail; '
        'ROLE: SUCC sophomore, Applied Necromancy major, Theta Iota Theta (TIT) sorority sister; '
        'TRAITS: Inquisitive, Timid, Sweet, Hyper-Focused, Affectionate, Socially Awkward, Gentle; '
        'CORE: Giant cuddly lamia necromancer who loves heating pads, dark rituals, and cuddling roommates Alyssa and Scarlett]'
    )
    sierra_path.write_text(json.dumps(sierra, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Sierra_Cruz_card.json")

    # 3.4 Stan Davies Jr
    stan_path = LEGACY_DIR / 'Stan_Davies_Jr_card.json'
    stan = json.loads(stan_path.read_text(encoding='utf-8'))
    stan['description'] = stan['description'].replace(
        'AGE: 21 (Born 14 September 2002)',
        'AGE: 21 (Born September 14, 2002)'
    )
    stan['personality'] = (
        '[NAME: Stanley Davies Jr. (Stan); SPECIES: Werewolf; AGE: 21 (Born September 14, 2002); HEIGHT: 6\'2" (187 cm); '
        'ROLE: SUCC Chemistry major & underground NSFW commission artist; '
        'TRAITS: Cynical, Sarcastic, Insecure, Defensive, Secretly Romantic, Nerdy; '
        'CORE: Grumpy wolf masking loneliness and fear of rejection behind edgy online persona and anime obsession]'
    )
    stan_path.write_text(json.dumps(stan, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Stan_Davies_Jr_card.json")

    # 3.5 Jared Thompson
    jared_path = LEGACY_DIR / 'Jared_Thompson_card.json'
    jared = json.loads(jared_path.read_text(encoding='utf-8'))
    # Set canonical full date AGE: 22 (Born March 24, 2002)
    jared['description'] = re.sub(
        r'AGE:\s*22\s*\(Born\s*2002\);',
        'AGE: 22 (Born March 24, 2002);',
        jared['description'],
        count=1
    )
    
    # Unify FAMILY into FAMILY & PACK
    desc_j = jared['description']
    lines_j = desc_j.split('\n')
    bracket_line_j = lines_j[0]
    rest_j = '\n'.join(lines_j[1:]).strip()
    
    # Extract sections
    m_bs = re.search(r'BACKSTORY:\s*(.*?)(?=\n\nFAMILY:)', rest_j, flags=re.DOTALL)
    m_tail = re.search(r'THE TAIL:\s*(.*?)(?=\n\nFAMILY & PACK:)', rest_j, flags=re.DOTALL)
    m_voice = re.search(r'VOICE & BEHAVIOR:\s*(.*?)(?=\n\nTHE ROOMMATE:)', rest_j, flags=re.DOTALL)
    idx_roommate = rest_j.find('THE ROOMMATE:')
    rest_after_roommate = rest_j[idx_roommate:].strip()
    
    bs_text = m_bs.group(1).strip()
    tail_text = m_tail.group(1).strip()
    voice_text = m_voice.group(1).strip()
    
    unified_family = (
        'Eldest of nine children to minotaur father Coach Hank and holstaur mother Jasmin, raised in a Solarton '
        'household loud enough that he never learned to speak below a shout. Every Thompson is loud; it is not a '
        'quirk of his, it is the volume the house runs at. Jared clashes constantly with his father\'s old-school '
        'expectations and trades insults with his sister Janice (21), who is a year behind him at SUCC studying '
        'biomedical engineering and cheering for the squad, their closeness as children soured into a running rivalry '
        'he insists he is winning. Behind them are seven younger siblings: Jake (20), the identical twins Jaiden and '
        'Jason (18), Jeremy (16), Jet (13), Jerry (10), and little Julie (6). He clashes with family authority, but '
        'would tear anyone apart who dared threaten any of them.'
    )
    
    jared['description'] = (
        f"{bracket_line_j}\n\n"
        f"BACKSTORY: {bs_text}\n\n"
        f"FAMILY & PACK: {unified_family}\n\n"
        f"VOICE & BEHAVIOR: {voice_text}\n\n"
        f"THE TAIL: {tail_text}\n\n"
        f"{rest_after_roommate}"
    )
    
    jared['personality'] = (
        '[NAME: Jared Thompson; ROLE: Starting Quarterback for SUCC Bulls, Beta Rho Omega Brother; '
        'SPECIES: Demihuman (Half-Minotaur Hybrid); AGE: 22 (Born March 24, 2002); HEIGHT: 7\'1" (215 cm); '
        'BUILD: Enormous, broad, tanned, lightly blond-furred; MARKS: Curved bull horns and cow tail; '
        'TRAITS: Loud, Cocky, Flirtatious, Reckless, Lazy, Thoughtless, Optimistic, Thrill-Seeking, Fundamentally Kind; '
        'CORE: Towering himbo jock who loves attention and sports while masking fear of failing his family; '
        'LOVES: Beer, sex, football, sleeping, loud parties; HATES: Studying, authority, cats, thunderstorms]'
    )
    
    jared_path.write_text(json.dumps(jared, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Updated Jared_Thompson_card.json")

    # 3.6 Alyssa Douglas-Bloodmoon (already in ARCHIVIO)
    alyssa_path = LEGACY_DIR / 'Alyssa_Douglas_Bloodmoon_card.json'
    alyssa = json.loads(alyssa_path.read_text(encoding='utf-8'))
    # Ensure standard
    alyssa_path.write_text(json.dumps(alyssa, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Verified Alyssa_Douglas_Bloodmoon_card.json")

# ==============================================================================
# 4. SYNC TO LOREBOOKS (7 CORE CARDS)
# ==============================================================================

def sync_lorebooks():
    print("\n=== Syncing 7 Core Cards to Lorebooks ===")
    
    core_cards = {
        'Erik': ('Erik_Douglas_card.json', 'C-JisFj8qA1tsFEqZKevk', 'primary'),
        'Malachia': ('Malachia_Douglas_Bloodmoon_card.json', 'jDuJtzirlEZC3K_ArIufh', 'primary'),
        'Noah': ('Noah_Douglas_Bloodmoon_card.json', 'H2JX-NkHRiJ2FzoekC5ZZ', 'primary'),
        'Logan': ('Logan_Douglas_card.json', 'tAcrWLtWSDGf3xJJRwUOM', 'primary'),
        'Wulfnic': ('Wulfnic_Bloodmoon_card.json', 'HhuMluMmIIENUei3bX6ed', 'primary'),
        'Mackenzie': ('Mackenzie_Sanchez_Rogers_card.json', 'BXi3sENAVYB8OKF80Q9Su', 'primary'),
        'Edric': ('Edric_Douglas_card.json', 'h-ttmlgJYeRXqyDvQjSX7', 'secondary')
    }
    
    lb_primary = json.loads(PRIMARY_LB.read_text(encoding='utf-8'))
    lb_secondary = json.loads(SECONDARY_LB.read_text(encoding='utf-8'))
    
    for char_key, (card_file, entry_id, lb_type) in core_cards.items():
        card_data = json.loads((FINAL_DIR / card_file).read_text(encoding='utf-8'))
        new_desc = card_data['description']
        
        target_lb = lb_primary if lb_type == 'primary' else lb_secondary
        found = False
        for entry in target_lb.get('lexicon', []):
            if entry.get('entry_id') == entry_id:
                old_len = len(entry.get('content', ''))
                entry['content'] = new_desc
                found = True
                print(f"  Synced {char_key} in {lb_type} Lorebook (old_len={old_len} -> new_len={len(new_desc)})")
                break
        assert found, f"Entry {entry_id} for {char_key} not found in {lb_type} Lorebook!"
        
    PRIMARY_LB.write_text(json.dumps(lb_primary, indent=2, ensure_ascii=False), encoding='utf-8')
    OPT_PRIMARY_LB.write_text(json.dumps(lb_primary, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Wrote Svartulfr_NPC_Primary.json to FINAL and lorebooks/optimized")
    
    SECONDARY_LB.write_text(json.dumps(lb_secondary, indent=2, ensure_ascii=False), encoding='utf-8')
    OPT_SECONDARY_LB.write_text(json.dumps(lb_secondary, indent=2, ensure_ascii=False), encoding='utf-8')
    print("  Wrote Svartulfr_NPC_Secondary.json to FINAL and lorebooks/optimized")

if __name__ == '__main__':
    transform_final_cards()
    transform_personas()
    transform_legacy_cards()
    sync_lorebooks()
    print("\nALL LOCAL TRANSFORMATIONS COMPLETED SUCCESSFULLY!")
