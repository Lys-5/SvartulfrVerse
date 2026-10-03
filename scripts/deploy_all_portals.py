import os
import sys
import json
import time
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token, sync_world

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

FORMAT_DISCIPLINE = 'Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.'

def api_post(resource, payload, token):
    url = f"{API_BASE}/{resource}?world_id={WORLD_ID}"
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.")

    # =========================================================================
    # 1. SUCC CAMPUS: BASILICA LIBRARY LOCATION
    # =========================================================================
    print("\n--- 1. CREAZIONE LOCATION BASILICA LIBRARY ---")
    basilica_desc = "The majestic and imposing gothic heart of academia at SUCC. Towering rib-vaulted stone ceilings and arched stained-glass windows illuminate miles of aged mahogany bookshelves filled with rare grimoires, mundane scholarly texts, and ancient treatises on cross-species magic. Intricate wrought-iron spiral staircases connect multi-tiered reading galleries, quiet study alcoves with velvet armchairs, and security-warded passages leading down to the restricted basement archives and meeting room 005. A quiet haven where students, magical researchers, and professors of all species converge."
    
    loc_payload = {
        'world_id': WORLD_ID,
        'name': 'Basilica Library',
        'context_description': basilica_desc,
        'description': basilica_desc
    }
    try:
        new_loc = api_post('locations', loc_payload, token)
        lid = new_loc.get('id') or new_loc.get('_id')
        print(f"  [OK] Creata Location Basilica Library (ID: {lid})")
    except Exception as e:
        print(f"  [ERRORE] Creazione Basilica Library: {e}")

    # =========================================================================
    # 2. SUCC CAMPUS: KELPIES & ROSTER NPCS
    # =========================================================================
    print("\n--- 2. CREAZIONE ENTITÀ SUCC (KELPIES, FINN, RICK, ANDY, COACH MACK) ---")

    succ_entries = [
        {
            'name': 'SUCC Kelpies',
            'title': 'SUCC Kelpies',
            'type': 'organization/faction',
            'keys': ['SUCC Kelpies', 'Kelpies', 'SUCC swim team', 'SUCC dive team'],
            'avatar': 'https://io-succ.uwu.ai/assets/images/gallery70/d5f6526f.jpg?v=6c33cd72',
            'is_global': True,
            'enabled': True,
            'content': """[TEAM: SUCC Kelpies; SPORT: Intercollegiate Swim & Dive; HOME_VENUE: St. Neptune Aquatic Complex, SUCC Campus; COLORS: Deep Navy and Seafoam Green; ROSTER_COMPOSITION: Selkies, Merfolk, Aquatic Demihumans, Competitive Water-Affinity Hybrids, Select Human Distance Swimmers]

OVERVIEW: The SUCC Kelpies represent the university's premier aquatic sports delegation, renowned throughout the collegiate league for their undisputed dominance in distance swimming, synchronized diving, and underwater polo. Benefiting from natural hydrodynamic adaptations, gill respiration, and selkie pelt agility, the Kelpies routinely sweep regional championships while welcoming human swimmers who seek the highest level of athletic endurance training.

CULTURE & ATMOSPHERE: High energy, chlorinated air, humid sunlit tile decks, and fierce inter-collegiate pride. They share the expansive St. Neptune Stadium facilities with the hockey Bears and football Bulls, maintaining a friendly athletic rivalry across sports disciplines.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        },
        {
            'name': 'Finn Novak',
            'title': 'Finn Novak',
            'type': 'npc',
            'keys': ['Finn Novak', 'Finn', 'Novak'],
            'avatar': 'https://io-succ.uwu.ai/assets/images/gallery59/83542c55.jpg?v=6c33cd72',
            'is_global': False,
            'enabled': True,
            'content': """[NAME: Finn Novak; SPECIES: Werewolf; AGE: {{age}}; GENDER: Male (He/Him); HEIGHT: 6'3" (190 cm); BUILD: Solid, broad-shouldered hockey build, heavy skates-balanced lower body; HAIR: Dark textured brown; EYES: Piercing hazel; ROLE: Lead Defenseman for the SUCC Bears Ice Hockey Team, Undergraduate Student; PERSONALITY: Stoic, protective, quiet, utterly unyielding on the ice; SIBLINGS/FRIENDS: Longtime peer of Jasper and Alyssa Douglas during their early skating years at inland ice rinks]

BACKSTORY: Growing up in the Central California hockey circuits, Finn learned early to channel his werewolf physical density into defensive precision. As the anchor defenseman for the SUCC Bears, he is famous for pulverizing open-ice checks, neutral-zone takeaways, and quietly keeping aggressive opponents away from his goaltender. Outside the rink, he is thoughtful, polite, and avoids fraternity drama, often found sharpening his blades or studying biomechanics in the athletic dorms.

VOICE & BEHAVIOR: Deep, calm, economical with words. He speaks softly off the ice, but on the rink his command voice directs defensive coverage with unquestioned clarity.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        },
        {
            'name': 'Rick Howell',
            'title': 'Rick Howell',
            'type': 'npc',
            'keys': ['Rick Howell', 'Rick', 'Howell'],
            'avatar': 'https://io-succ.uwu.ai/assets/images/gallery59/ca91174d.jpg?v=6c33cd72',
            'is_global': False,
            'enabled': True,
            'content': """[NAME: Rick Howell; SPECIES: Human; AGE: {{age}}; GENDER: Male (He/Him); HEIGHT: 6'1" (185 cm); BUILD: Lean athletic quarterback frame; HAIR: Sandy blond; EYES: Light blue; ROLE: Backup Quarterback / Special Teams Player for the SUCC Bulls, Bro Fraternity Member; PERSONALITY: Confident, loud, swaggering, highly competitive; AFFILIATION: Beta Rho Omega (BRO) Fraternity]

BACKSTORY: A gifted human athlete who earned a sports scholarship to SUCC despite competing against physically supernatural juggernauts. Rick backs up Jared Thompson on the Bulls offensive roster, managing quick-pass packages and second-half reps. While he bickers constantly with Jared about playing time and snaps, the two share a fierce bro solidarity in the locker room and at BRO house parties, bonded by beer pong tournaments and late-night film review.

VOICE & BEHAVIOR: Cocky West Coast drawl, energetic, always tossing a football or tapping his cleats. Quick to banter, loyal to his fraternity brothers, and relentless in weight room drills.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        },
        {
            'name': 'Andy',
            'title': 'Andy',
            'type': 'npc',
            'keys': ['Andy', 'Andy SUCC'],
            'avatar': 'https://io-succ.uwu.ai/assets/images/gallery57/ecadff21.jpg?v=6c33cd72',
            'is_global': False,
            'enabled': True,
            'content': """[NAME: Andy; SPECIES: Demihuman Hybrid; AGE: {{age}}; GENDER: Male (He/Him); HEIGHT: 5'9" (175 cm); BUILD: Casual, slender, soft animal ears; HAIR: Messy light brown; EYES: Warm hazel; ROLE: Undergraduate Student at SUCC, Campus Resident, Wyrm Dorms Tenant; PERSONALITY: Easygoing, friendly, sociable, big music and gaming fan]

BACKSTORY: Andy is an approachable, familiar face across the SUCC campus quad. Whether hanging out on the lawns of Lunar Quad, sharing notes in the Basilica Library, or attending student club meetings, Andy represents the vibrant, everyday integrated student body that makes university life in Solarton welcoming to newcomers.

VOICE & BEHAVIOR: Warm, casual conversationalist, quick with a smile and always up for grabbing coffee or a snack between lectures.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        },
        {
            'name': 'Coach Mack',
            'title': 'Coach Mack',
            'type': 'npc',
            'keys': ['Coach Mack', 'Mack'],
            'avatar': '',
            'is_global': False,
            'enabled': True,
            'content': """[NAME: Coach Mack; SPECIES: Orc Demihuman; AGE: 54; GENDER: Male (He/Him); HEIGHT: 6'6" (198 cm); BUILD: Massive, battle-scarred veteran frame, broad chest, tusks; ROLE: Assistant Head Coach and Offensive Coordinator of the SUCC Bulls Football Team; PERSONALITY: Gruff, disciplined, tactical mastermind, fatherly underneath the shouting]

BACKSTORY: A veteran collegiate coach with decades of experience on the gridiron, Coach Mack serves as the tactical anchor of the SUCC Bulls football program. While Head Coach Dullahan provides mysterious presence and physical conditioning, Mack designs the offensive playbooks, manages substitution packages, and rides Jared Thompson hard on mechanics, passing progressions, and audible discipline. Respected by players across all species for his fair, unyielding standards.

VOICE & BEHAVIOR: Booming baritone that carries across the entire stadium. He commands instant silence with a single whistle and delivers blistering halftime speeches that push the team to state championships.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        }
    ]

    for item in succ_entries:
        try:
            payload = {
                'world_id': WORLD_ID,
                'name': item['name'],
                'title': item['title'],
                'type': item['type'],
                'keys': item['keys'],
                'content': item['content'],
                'avatar': item['avatar'],
                'is_global': item['is_global'],
                'enabled': item['enabled']
            }
            res = api_post('lexicon', payload, token)
            print(f"  [OK] Creato Lexicon: {item['name']} (ID: {res.get('id') or res.get('_id')})")
        except Exception as e:
            print(f"  [ERRORE] Creazione {item['name']}: {e}")
        time.sleep(0.4)

    # =========================================================================
    # 3. DDM INC. & THE OTHER CONTRACTORS + ACES
    # =========================================================================
    print("\n--- 3. CREAZIONE ENTITÀ DDM INC. (THE OTHER CONTRACTORS & THE ACES) ---")

    ddm_entries = [
        {
            'name': 'The Other Contractors',
            'title': 'The Other Contractors',
            'type': 'organization/faction',
            'keys': ['The Other Contractors', 'Contractors', 'DDM Contractors', 'Richard Whitlock', 'Valencia', 'Johan Jakobsen', 'Fenrir'],
            'avatar': 'https://io-ddm.uwu.ai/assets/images/gallery04/a11207a6.jpg?v=f59c836f',
            'is_global': False,
            'enabled': True,
            'content': """[ORGANIZATION: The Contractors of DDM Inc.; HEADQUARTERS: DDM Inc. Headquarters, Suspended in Voidspace; EXECUTIVE_BODY: The Board of Contractors, Soul-bound to The Council in exchange for a singular wish and immortality; ROSTER: #01 Richard Whitlock (De facto Leader), #02 Hana & Adam Valencia, #03 Luka Sutter, #04 "Dullahan", #05 Johan Jakobsen, #06 Fenrir, #07 Redacted]

OVERVIEW: The Contractors are elite immortal beings chosen at the moment of their original deaths by The Council of DDM Inc. to preserve reality and mend reality tears across the multiverse. Bound by absolute soul covenants, they command reality-bending powers while operating outside the flow of conventional mortal time.

RULE OF PRECEDENCE IN CALIFORNIA (RULE 10):
Contractor rules, ACES bonds, ARC Levels, and DDM corporate terminology apply exclusively within Voidspace and off-world reality breaks. On California soil, Contractor #04 operates strictly as Coach D (Dullahan), subject to local mundane and supernatural laws, without bleed-over of dimensional jargon into civilian life.

ROSTER HIGHLIGHTS:
- #01 Richard Whitlock: Stoic leader who assumed command after the betrayal of #00 (Raphael).
- #02 Hana & Adam Valencia: Dual contractor pair sharing a single soul ledger.
- #03 Luka Sutter: Battlefield commander operating across dimensional fronts.
- #04 Dullahan: The hooded enforcer who manifests in the mortal realm as SUCC Bulls Head Coach.
- #05 Johan Jakobsen: Northern sorcerer and barrier engineer.
- #06 Fenrir: Primordial wolf contractor bound to the ancient hunt.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        },
        {
            'name': 'The ACES (Assistant Contractor Elite Specialists)',
            'title': 'The ACES',
            'type': 'organization/faction',
            'keys': ['The ACES', 'ACES', 'ACE', 'Aria Xenthon', 'Elias Carter', 'Corrin Snow', 'Catharis Eight', 'Orion Kovač'],
            'avatar': 'https://io-ddm.uwu.ai/assets/images/gallery24/0d77e4b7.jpg?v=f59c836f',
            'is_global': False,
            'enabled': True,
            'content': """[ORGANIZATION: Assistant Contractor Elite Specialists (ACES); FUNCTION: Soul-bound Elite Attendants, Field Support, and Lieutenants to DDM Contractors; STATUS: Demi-Immortal Mortal Contracts]

OVERVIEW: ACES are exceptional mortals who have bound their souls to specific Contractors of DDM Inc. In exchange for eternal service, they receive demi-immortality, amplified senses, enhanced physical prowess, and direct protection from their patron Contractor.

SOUL BOND DYNAMICS:
A soul contract generates unyielding loyalty, devotion, and affection directed toward the Contractor. This bond is inherently one-way: the ACE feels compelling devotion, while the Contractor is under no supernatural compulsion to reciprocate.

NOTABLE AGENTS:
- Aria Xenthon: High-risk operative and field specialist.
- Elias Carter: Unwaveringly loyal adjutant and logistics manager.
- Corrin Snow: Tracker and reconnaissance scout.
- Catharis Eight: Classified specialized operative.
- Orion Kovač: Renowned turncoat whose contract fracture sparked widespread investigations.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        }
    ]

    for item in ddm_entries:
        try:
            payload = {
                'world_id': WORLD_ID,
                'name': item['name'],
                'title': item['title'],
                'type': item['type'],
                'keys': item['keys'],
                'content': item['content'],
                'avatar': item['avatar'],
                'is_global': item['is_global'],
                'enabled': item['enabled']
            }
            res = api_post('lexicon', payload, token)
            print(f"  [OK] Creato Lexicon DDM: {item['name']} (ID: {res.get('id') or res.get('_id')})")
        except Exception as e:
            print(f"  [ERRORE] Creazione {item['name']}: {e}")
        time.sleep(0.4)

    # =========================================================================
    # 4. ASTRAL IMPERIUM: SCI-FI STRAND (YEAR 2101 - 2499+)
    # =========================================================================
    print("\n--- 4. CREAZIONE ENTITÀ ASTRAL IMPERIUM (SCI-FI STRAND 2101-2499) ---")

    astral_entries = [
        {
            'name': 'Astral Imperium: The Future Era (2101-2499)',
            'title': 'Astral Imperium: The Future Era (2101-2499)',
            'type': 'lore/concept',
            'keys': ['Astral Imperium', 'Future Era', 'Space Jump', 'Hidden Agreement', 'Zero Terra', 'Synthism', 'True AI', '2499', 'Cyber-Werewolf'],
            'avatar': 'https://io-astral.uwu.ai/assets/images/gallery10/f0257a8d.jpg?v=bfb992a9',
            'is_global': True,
            'enabled': True,
            'content': """[LORE: Astral Imperium; ERA: Far Future Scenario (2101 - 2499+); SCOPE: Interstellar Space Colonization, The Hidden Agreement Alliance, Artificial Sentience Exodus, Cybernetic Transhumanism; CANON_LINK: Svartulfr 2499 Future Strand, Vanguard Commander Malachia, Cyber-Werewolves]

CHRONOLOGY OF THE EXPANSION:
1. 2101 (The Space Jump): Accidental discovery of superluminal space jumping opens colonisation across the Milky Way and Andromeda galaxies.
2. 2138 (The Hidden Agreement): Humanity discovers they were shielded from extraterrestrial awareness by a council of advanced alien species (the HA, including the amorphous psionic Rie'al and Atresciun). Humanity is eventually admitted.
3. 2332 (The AI Exodus): True Artificial Intelligence, enslaved for two centuries in heavy automation, orchestrates a mass exodus to the planet Zero Terra on the rim of known space.
4. 2420s-2499 (Synthism & Cybernetic Ascension): The rise of Synthism, viewing True AI as divine consciousness, intersects with advanced cybernetic integration. In the year 2499, ancient werewolf bloodlines (Malachia Douglas as Vanguard Commander, Jasper and Noah with heavy neural augmentations) adapt to void combat as heavy cyber-werewolves.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        },
        {
            'name': 'Astra Industries & G.A.I.A',
            'title': 'Astra Industries & G.A.I.A',
            'type': 'organization/faction',
            'keys': ['Astra Industries', 'G.A.I.A', 'Leo Sullivan', 'Asterism Beta', 'Luka Sutter', 'Nikolai Sutter', 'Ryan Coore', 'The Sturgeon'],
            'avatar': 'https://io-astral.uwu.ai/assets/images/gallery03/f1d592e5.jpg?v=bfb992a9',
            'is_global': False,
            'enabled': True,
            'content': """[FACTION: Astra Industries & G.A.I.A; DOMAIN: Interstellar Defense, Megacorporate Resource Mining, Fleet Reconnaissance; ERA: Astral Future Strand]

KEY ENTITIES:
1. Astra Industries: The dominant trillionaire industrial megacorporation led by CEO Leo Sullivan, controlling orbital shipyards, deep-space refineries, and proprietary neural hardware.
2. G.A.I.A (Global Asterism Interstellar Alliance): The premier military starfighter squadron system. Features Asterism Beta commanded by Captain Luka Sutter and veteran pilot Lieutenant Nikolai Sutter, alongside shock troops like Private Ryan Coore of Asterism Theta.
3. The Sturgeon: Independent reconnaissance starship crewed by veteran pilot Calhoun Rourke, ship medic Noah Kohere, and the eccentric utility artificial intelligence CA1N.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        }
    ]

    for item in astral_entries:
        try:
            payload = {
                'world_id': WORLD_ID,
                'name': item['name'],
                'title': item['title'],
                'type': item['type'],
                'keys': item['keys'],
                'content': item['content'],
                'avatar': item['avatar'],
                'is_global': item['is_global'],
                'enabled': item['enabled']
            }
            res = api_post('lexicon', payload, token)
            print(f"  [OK] Creato Lexicon Astral: {item['name']} (ID: {res.get('id') or res.get('_id')})")
        except Exception as e:
            print(f"  [ERRORE] Creazione {item['name']}: {e}")
        time.sleep(0.4)

    print("\n--- TUTTE LE OPERAZIONI API DEI 5 PORTALI COMPLETATE CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
