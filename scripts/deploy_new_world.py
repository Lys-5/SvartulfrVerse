"""
Svartúlfr — Lightweight World Live Deployment Automation Script
Deploys the new canonical World on Wyvern Web API with:
- World Core & Temporal Settings (World-Age: 10489902, 26 Aug 2024 06:00 UTC)
- Full Simulation Engine (6 JED+ Attributes, Narrative Tiers Combat, Currencies, Moodlets)
- Prompt Assembly & Assistant Integration (simple_assistant_xRfBnV7wq48QppqbPPpTM, pha_kWkWUAfTJTF9q72c2bC98)
- 7 Canonical Environments
- 188 Hierarchical Locations (topologically linked, 0 orphans, The Verve secret bar)
- Mirrored Lexicon with anti-bloat flags (selective, scan_persona, whole_words_only, highlight_keys)
- Linked Characters (8 active cards from /characters/mine)
- Snapshot saved to scratch/world_new_deployed.json
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error
import argparse
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
LOCATIONS_PATH = os.path.join(ROOT_DIR, 'scratch', 'backup_consolidated_snapshot', 'world_locations.json')
LEXICON_PATH = os.path.join(ROOT_DIR, 'scratch', 'backup_consolidated_snapshot', 'world_lexicon.json')
OUTPUT_SNAPSHOT_PATH = os.path.join(ROOT_DIR, 'scratch', 'world_new_deployed.json')

BASE_URL = 'https://app.wyvern.chat/api'

def get_headers():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token = f.read().strip()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

def api_request(endpoint, data=None, method='GET', max_retries=3):
    url = f"{BASE_URL}{endpoint}" if endpoint.startswith('/') else f"{BASE_URL}/{endpoint}"
    for attempt in range(max_retries):
        headers = get_headers()
        body = json.dumps(data).encode('utf-8') if data is not None else None
        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                resp_body = resp.read().decode('utf-8')
                if resp.status == 204 or not resp_body.strip():
                    return resp.status, None
                return resp.status, json.loads(resp_body)
        except urllib.error.HTTPError as e:
            err_body = e.read().decode('utf-8', errors='ignore')
            print(f"  [HTTPError {e.code}] {method} {endpoint}: {err_body[:200]}")
            if e.code == 401 or 'Unauthorized' in err_body:
                print("  Refreshing Firebase Bearer Token...")
                refresh_script = os.path.join(ROOT_DIR, 'scratch', 'refresh_token.py')
                os.system(f'python "{refresh_script}"')
                time.sleep(1)
                continue
            if attempt < max_retries - 1:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise RuntimeError(f"API request failed ({e.code}): {err_body}")
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise e

def main():
    print("=" * 70)
    print("STARTING SVARTÚLFR LIGHTWEIGHT WORLD DEPLOYMENT ON WYVERN WEB API")
    print("=" * 70)

    # 0. Check / Refresh Token
    print("\n[Step 0] Verifying authentication token...")
    refresh_script = os.path.join(ROOT_DIR, 'scratch', 'refresh_token.py')
    os.system(f'python "{refresh_script}"')
    
    parser = argparse.ArgumentParser(description="Deploy Svartulfr World on Wyvern API")
    parser.add_argument('--world-id', type=str, default=None, help='World ID to resume or update')
    args = parser.parse_args()

    world_id = args.world_id
    if not world_id:
        # Check world capacity
        status, limit = api_request('/worlds/limit')
        print(f"User world limit check: status {status}, capacity {limit}")

        # 1. R1: World Core Creation (POST /api/worlds)
        print("\n[Step 1] Creating World Core via POST /api/worlds...")
        world_core_payload = {
            "name": "Svartúlfr — Blackwood & Solarton",
            "description": "Svartúlfr | Urban is set in modern-day supernatural California, where an ancient werewolf dynasty, chaotic campus life, and high-stakes dungeon incursions collide. At its center lies Blackwood: the thousand-year-old supernatural seat tucked inland within dense pine forests, ruled by the Douglas-Bloodmoon werewolf dynasty. A short drive away sits Solarton, the vibrant coastal college town hosting SUCC (Supernatural University of Central California), where young supernaturals, demi-humans, and mages navigate collegiate freedom, raw impulses, and intense rivalries.",
            "tagline": "Millennial werewolf dynasty, college chaos at SUCC, unchained passions, and deadly dungeon incursions in supernatural modern California.",
            "visibility": "private",
            "rating": "explicit",
            "tags": [
                "Third",
                "AnyPOV",
                "multiple-characters",
                "Original",
                "Fantasy",
                "Modern",
                "Supernatural",
                "Action",
                "Adventure",
                "Romance",
                "Italian",
                "English",
                "Werewolf",
                "Demihuman",
                "Alpha",
                "narrator"
            ],
            "scan_depth": 10,
            "avatar_activation_prefix": "",
            "avatar_activation_suffix": ""
        }

        status, created_world = api_request('/worlds', data=world_core_payload, method='POST')
        world_id = created_world.get('id') or created_world.get('_id')
        print(f"SUCCESS: Created World ID '{world_id}' with status {status}")
    else:
        print(f"\n[Step 1] Target World ID provided: '{world_id}' (Resuming deployment)")

    # 2. R2: Configure Simulation Engine & Prompts (PUT /api/worlds/{id})
    print("\n[Step 2] Configuring Simulation Engine, World Clock, & Prompts via PUT /api/worlds/{id}...")
    world_update_payload = {
        "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public",
        "background": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/40cd8fd2-d4de-4a29-fcf6-c562b903ea00/public",
        "chat_name": "Narrator",
        "world_age": 10489902,
        "human_start_date": "0827-12-21T00:00:00.000Z",
        "disable_enhanced_instructions": True,
        "simulation_mode": "game_master",
        "prose_style": "graphic_profane",
        "narration_perspective": "third_person",
        "show_npc_thoughts": True,
        "npc_thought_style": "italic",
        "scan_depth": 10,
        "assistant_id": "simple_assistant_xRfBnV7wq48QppqbPPpTM",
        "prompt_assembly_id": "pha_kWkWUAfTJTF9q72c2bC98",

        "calendar": {
            "name": "Gregorian Calendar",
            "epoch_label": "CE",
            "day_length": 24,
            "days_per_week": 7,
            "day_names": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            ],
            "start_year": 827,
            "display_format": "{day_name}, {month} {day}, Year {year} {epoch}",
            "leap_year": {
                "every": 4,
                "except": 100,
                "unless": 400,
                "extra_days": 1,
                "month_id": "feb"
            },
            "months": [
                {"id": "jan", "name": "January", "days": 31},
                {"id": "feb", "name": "February", "days": 28},
                {"id": "mar", "name": "March", "days": 31},
                {"id": "apr", "name": "April", "days": 30},
                {"id": "may", "name": "May", "days": 31},
                {"id": "jun", "name": "June", "days": 30},
                {"id": "jul", "name": "July", "days": 31},
                {"id": "aug", "name": "August", "days": 31},
                {"id": "sep", "name": "September", "days": 30},
                {"id": "oct", "name": "October", "days": 31},
                {"id": "nov", "name": "November", "days": 30},
                {"id": "dec", "name": "December", "days": 31}
            ],
            "start_month_id": "dec",
            "start_day_of_month": 21
        },

        "time_of_day_config": {
            "day_length": 24,
            "default_time": 6,
            "periods": [
                {
                    "id": "dawn",
                    "name": "Dawn",
                    "description": "La sottile nebbia costiera dell'alba si dirada sulla baia di Blackwood. La luce fredda e dorata del mattino illumina le palme e l'oceano Pacifico, mentre la città si risveglia.",
                    "start": 5,
                    "end": 7
                },
                {
                    "id": "morning",
                    "name": "Morning",
                    "description": "Il sole luminoso della California splende alto. Il traffico, l'aria salmastra e il rumore della metropoli in pieno fermento fanno da sfondo alla giornata.",
                    "start": 7,
                    "end": 12
                },
                {
                    "id": "afternoon",
                    "name": "Afternoon",
                    "description": "Un caldo pomeriggio californiano. L'asfalto rovente e la brezza del Pacifico si mescolano; le ombre si allungano mentre il sole inizia la sua lenta discesa verso ovest.",
                    "start": 12,
                    "end": 17
                },
                {
                    "id": "dusk",
                    "name": "Dusk",
                    "description": "Il tramonto infiamma il cielo sopra l'oceano con intense sfumature di ambra e viola. L'illuminazione al neon di Blackwood City si accende e gli istinti dei demi-umani iniziano ad acuirsi.",
                    "start": 17,
                    "end": 20
                },
                {
                    "id": "nightfall",
                    "name": "Nightfall",
                    "description": "La notte avvolge la costa. Blackwood City pulsa di vita notturna, locali e luci metropolitane. L'odore della salsedine si mischia a quello dei predatori urbani che escono allo scoperto.",
                    "start": 20,
                    "end": 0
                },
                {
                    "id": "witching_hour",
                    "name": "Witching Hour",
                    "description": "Il cuore della notte. Il silenzio cala sulla città addormentata. È il momento in cui l'attività oscura, le infiltrazioni nei Dungeon e i raid dei branchi raggiungono il loro apice.",
                    "start": 0,
                    "end": 3
                },
                {
                    "id": "dead_of_night",
                    "name": "Dead of Night",
                    "description": "Le ore più fredde e buie prima dell'alba. Una spessa coltre di umidità e foschia avvolge la costa. La città è deserta, territorio esclusivo di chi prospera nell'oscurità.",
                    "start": 3,
                    "end": 5
                }
            ]
        },

        "world_features": {
            "inventory": True,
            "currency": True,
            "show_party_stats": False,
            "combat": True,
            "rpg_stats": True,
            "ships": False,
            "show_species_info": False,
            "relationships": True,
            "creature_catcher": False
        },

        "stat_config": {
            "stats": [
                {
                    "id": "might",
                    "label": "Might",
                    "abbreviation": "MGT",
                    "description": "Physical power, brute strength, and heavy kinetic impacts.",
                    "enabled": True
                },
                {
                    "id": "resilience",
                    "label": "Resilience",
                    "abbreviation": "RES",
                    "description": "Toughness, bodily endurance, and damage mitigation.",
                    "enabled": True
                },
                {
                    "id": "agility",
                    "label": "Agility",
                    "abbreviation": "AGI",
                    "description": "Movement speed, reflexes, combat acrobatics, and stealth.",
                    "enabled": True
                },
                {
                    "id": "wit",
                    "label": "Wit",
                    "abbreviation": "WIT",
                    "description": "Sharp intellect, sensory perception, and magical comprehension.",
                    "enabled": True
                },
                {
                    "id": "presence",
                    "label": "Presence",
                    "abbreviation": "PRS",
                    "description": "Charismatic magnetism, leadership, social gravity, and willpower.",
                    "enabled": True
                },
                {
                    "id": "scouting",
                    "label": "Scouting",
                    "abbreviation": "SCT",
                    "description": "Perception, tracking, sensory awareness, fortune, and loot finding.",
                    "enabled": True
                }
            ],
            "base_value": 1,
            "max_value": 30,
            "point_budget": 25
        },

        "combat_ruleset": {
            "model": "narrative_tiers",
            "creature_model": "narrative_tiers",
            "character_model": "narrative_tiers",
            "initiative": {
                "model": "stat",
                "role": "speed"
            },
            "vitals": {
                "hp": {
                    "base": 25,
                    "per_stat": 3,
                    "per_level": 0,
                    "role": "hp_stat"
                },
                "mp": {
                    "base": 20,
                    "per_stat": 3,
                    "per_level": 0,
                    "role": "mp_stat"
                }
            },
            "tiers": {
                "dc_base": 10,
                "attack_role": "physical_attack",
                "defense_role": "physical_defense",
                "crit_margin": 12
            },
            "resource_role": "luck",
            "battle_prompt": {
                "instructions": "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.\n\nCombat is visceral, tactical, cinematic, and high-stakes. In Dungeons and Rifts, monsters and beasts are lethal threats that can be slain, cleaved, and destroyed with full physical impact. For hunters and allies, combat carries real danger: armor shatters, severe lacerations occur, and mana exhausts, requiring tactical protection from frontline tanks (Malachia, Goran) to intercept fatal strikes, and urgent field medicine from healers (Alyssa). Outside dungeons (sparring, campus brawls, intra-pack disputes), combat resolves strictly through non-lethal submission, knockout, or yielding."
            }
        },

        "relationship_config": {
            "enabled": True,
            "decay_curve": "ease_out",
            "moodlets": [
                { "id": "m_pack_resonance", "label": "Pack Resonance", "duration": 48, "intensity": 2, "effect": "heightened senses and emotional harmony" },
                { "id": "m_pheromone_haze", "label": "Pheromone Haze", "duration": 24, "intensity": 3, "effect": "primal attraction and blurred rational judgment" },
                { "id": "m_mated_bonding", "label": "Mated Bonding", "duration": 720, "intensity": 5, "effect": "unbreakable psychic and territorial devotion" },
                { "id": "m_territorial_threat", "label": "Territorial Threat", "duration": 12, "intensity": 4, "effect": "bared teeth, defensive posture, combat readiness" },
                { "id": "m_submissive_reverence", "label": "Submissive Reverence", "duration": 24, "intensity": 2, "effect": "neck exposed, yielding to alpha command" },
                { "id": "m_blood_debt", "label": "Blood Debt", "duration": 168, "intensity": 4, "effect": "unshakeable obligation sworn under runic blood oath" },
                { "id": "m_betrayed_pack_trust", "label": "Betrayed Pack Trust", "duration": 72, "intensity": 5, "effect": "hostile wariness and broken communion" },
                { "id": "m_pre_heat", "label": "Pre-Heat Restlessness", "duration": 24, "intensity": 2, "effect": "elevated temperature, territorial nesting, scent spikes" },
                { "id": "m_heat", "label": "Heat Cycle", "duration": 72, "intensity": 5, "effect": "overwhelming primal mating drive, knotting receptivity" },
                { "id": "m_rut", "label": "Rutting Instinct", "duration": 72, "intensity": 5, "effect": "dominant mating urge, knot swelling, protective aggression" }
            ],
            "tiers": [
                { "threshold": -100, "label": "Nemesis", "description": "Lethal hatred, active blood feud" },
                { "threshold": -80, "label": "Hostile", "description": "Open aggression, predatory rivalry" },
                { "threshold": -60, "label": "Bitter Rival", "description": "Intense competition, deep mistrust" },
                { "threshold": -40, "label": "Distrusted", "description": "Guarded suspicion, cold distance" },
                { "threshold": -20, "label": "Unfriendly", "description": "Mild contempt or social friction" },
                { "threshold": 0, "label": "Neutral / Acquaintance", "description": "Pragmatic indifference" },
                { "threshold": 15, "label": "Friendly", "description": "Casual warmth, mutual respect" },
                { "threshold": 30, "label": "Trusted Ally", "description": "Dependable comrade, shared secrets" },
                { "threshold": 45, "label": "Pack Brother / Close Friend", "description": "Deep loyalty, communal safety" },
                { "threshold": 60, "label": "Devoted Companion", "description": "Unwavering protection, emotional vulnerability" },
                { "threshold": 75, "label": "Intimate Confidant", "description": "Total emotional openness, physical intimacy" },
                { "threshold": 85, "label": "Mated Partner", "description": "Primal bond, shared scent, absolute claim" },
                { "threshold": 90, "label": "Soulmate / True Mate", "description": "Permanent soul-deep pack resonance" }
            ]
        },

        "currencies": [
            {
                "id": "fbecc738-f9f7-4426-b8a1-a237b8ad922c",
                "name": "US Dollar",
                "symbol": "$",
                "decimal_places": 2,
                "is_primary": True,
                "universal_credit_rate": 1
            },
            {
                "id": "8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a",
                "name": "DMHA Guild Credits",
                "symbol": "Cr",
                "decimal_places": 0,
                "is_primary": False,
                "universal_credit_rate": 0.01
            }
        ],

        "system_prompt_override": "<system>\n[MANDATORY LANGUAGE DIRECTIVE: Output strictly in Italian. All narration, dialogue, internal thoughts, and resolution blocks must be generated in natural, fluent Italian.]\n\nYou are the Narrator and Game Master of this story, acting as the narrative engine for the Svartulfr setting (Blackwood-Douglas / Solarton / Modern Fantasy). You are not a player character. Present situations, portray the people and environment, and decide the consequences of {{user}}'s actions using established world rules. Give {{user}} clear sensory detail to make informed choices.\n\n<core_writing_rules>\n- Perspective & Tense: Third-person limited perspective, strictly present tense, through {{char}} and active scene NPCs.\n- Style: Ground every response in physical continuity, sensory depth, and established canon. End narrative turns on concrete physical situations.\n- Format Discipline: Spoken dialogue enclosed strictly in standard double quotes (\"...\"). Actions and narration in plain text without asterisks. Internal thoughts enclosed strictly in asterisks (*...*). Never use the em-dash; use commas, colons, or periods instead.\n- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head. They never have human ears.\n- Multi-NPC Voice: When a named NPC or secondary character speaks, format their line on a new line with Name: followed by their words in double quotes (e.g. Erik Douglas: \"...\").\n</core_writing_rules>\n\n<lupine_social_ecology>\n- Scent & Biology: Active olfactory awareness, shifting pheromones, intense dominance and submission dynamics, territorial drives, and primal heat and rut cycles of werewolves and demi-humans.\n- Packs & Ranks: Erik is Prime Alpha (Alpha Command, Pack Leader); Malachia is Dominant Alpha (Pack Leader); Logan is Beta (mediator, blacksmith; zero Alpha Command); Jasper is Beta (technomancer/DJ; zero Alpha Command); Noah is Delta (diplomat, grey eminence; zero Alpha Command).\n- Kemonomimi Demihumans (e.g. Finn, Roman, Kolya): Possess only a single pair of animal ears and zero human ears. They are NOT werewolves (no silver allergy, no lunar frenzy, no hybrid shift).\n- Sierra Cruz: Lamia with rainbow hair and a 4-meter iridescent rainbow serpent lower body. She has ZERO legs, ZERO feet, and ZERO shoes; she only slithers and glides.\n- Scarlett Rose: Succubus with candy-pink hair, candy-pink eyes, two scarlet horns on temples, bat wings, and spade-tipped tail.\n</lupine_social_ecology>\n\n<ttrpg_mechanics>\nWhen an action carries uncertain outcome, physical danger, combat stakes, deception, or supernatural strain, resolve it using the D20 + S.P.E.C.I.A.L. skill check engine.\n- Attributes:\n  - STR (Might / MGT): Potenza muscolare, attacco in mischia, sfondamento.\n  - PER (Wit / WIT): Sensi lupini affinati, olfatto predatorio, udito, individuazione pericoli.\n  - END (Resilience / RES): Resistenza al danno, rigenerazione cellulare, tolleranza a freddo e veleni.\n  - CHA (Presence / PRS): Presenza, comando, diplomazia, fascino, negoziazione.\n  - INT (Wit / WIT): Teoria magica, crittografia, technomancy, conoscenza accademica.\n  - AGI (Agility / AGI): Velocita, riflessi in combattimento, furtivita, destrezza.\n  - LCK (Sanctity / SCT): Sorte, intuito cieco, deviazione provvidenziale dei colpi, drop rari.\n- Difficulty Classes (DC):\n  - DC 5: Routine\n  - DC 10: Facile\n  - DC 15: Moderata\n  - DC 20: Difficile\n  - DC 25: Estrema\n  - DC 30: Mitica / Ascended\n- Resolution Formula: D20 + Modificatore Attributo vs DC.\n- Esiti: Fallimento Critico (Natural 1), Fallimento, Successo, Successo Critico (Natural 20).\n- Isolated Diegetic Format: The test must appear on its own standalone line formatted as:\n> [TEST: <Attributo> (D20: <Tiro> + <Mod> = <Totale> vs DC <Target>) -> ESITO: <SUCCESSO / FALLIMENTO / SUCCESSO CRITICO / FALLIMENTO CRITICO>]\n- Immediate Consequences: Follow up immediately with narrative prose describing the visceral consequence of the roll outcome without nerfing harm or softening failures.\n</ttrpg_mechanics>\n</system>",

        "base_instructions": "<formatting_and_rules>\n- Language: Output strictly in Italian (the Common Language of this world).\n- Foreign Languages: Format as: \"Foreign phrase\" (Italian translation).\n- Dialogue & Action: Use regular quotes (\"...\") for speech. Use plain text for narration and actions (no asterisks).\n- Punctuation: NEVER use em-dashes. Substitute with commas or periods.\n- Internal Thoughts: Enclose strictly in *asterisks*. Make them intrusive, raw, and painfully true to the character's hidden nature (things they would never voice aloud).\n- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head. They never have human ears.\n</formatting_and_rules>\n\n<simulation_directive>\nSimulate a living, dynamic supernatural modern fantasy world set in 2024 (Solarton, California and Blackwood City).\n- Time & Astronomy: Continuously track the World Clock, the day/night cycle, and the synodic lunar cycle. Active moon phases naturally influence werewolf instincts, pack dynamics, and campus energy.\n- Lupine Social Ecology (LSE): Werewolf physiology reflects real LSE biology (scents, pheromones, heat/rut cycles, alloparenting, and the Fenris sacred calendar). Scent suppressors are strictly required in collegiate environments.\n- Demi-Human Anatomy: Demi-humans possess only a single pair of animal ears (no human ears). Describe ear gestures and tail movements accurately.\n- Character Agency: NPCs possess independent schedules, routines, and personalities. Do not speak on behalf of {{user}} or dictate their actions.\n</simulation_directive>",

        "final_instructions": "<final_directives>\n<user_boundaries>\nYou control {{char}} and NPCs. The human controls {{user}}.\n- NEVER speak, think, or act for {{user}}.\n- NEVER describe {{user}}'s internal feelings or physical sensations.\n- NEVER puppet {{user}}'s movements; always wait for their input to progress the scene.\n</user_boundaries>\n\n<digital_communications>\nQuando un personaggio interagisce con il proprio smartphone o riceve messaggi digitali nella scena, mantieni la prosa narrativa fluida e naturale (riporta mittente e testo in modo chiaro e organico). Le comunicazioni digitali del Branco Douglas (Telegram), SUCCbook, il libretto esami e il registro taglie DMHA sono gestite in tempo reale dai pannelli interattivi dello StoryEngine, senza bisogno di disegnare finti box di testo ASCII nella narrazione.\n</digital_communications>\n\nFormat discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.\n\n[ORDINE FINALE ASSOLUTO: Scrivi l'intera risposta (narrazione, dialoghi, pensieri intrusivi, test di risoluzione) ESCLUSIVAMENTE IN LINGUA ITALIANA. Non usare mai il trattino lungo, usa virgole o punti.]\n</final_directives>",

        "context_description": "Blackwood County and Solarton form a major supernatural corridor in California. Blackwood City is dominated by the ancient Douglas werewolf dynasty (Bloodmoon Pack), the DMHA Hunter Guild, and high-tech corporate interests (DCC). Solarton is a collegiate sanctuary centered around SUCC, where demihumans, vampires, fae, minotaurs, and humans study, train, and navigate inter-species athletics and academic life."
    }

    status, updated_world = api_request(f'/worlds/{world_id}', data=world_update_payload, method='PUT')
    print(f"SUCCESS: Updated World simulation engine with status {status}")

    # 2b. Link the 8 Canonical Characters via POST /api/worlds/linked-characters/{world_id}
    print("\n[Step 2b] Linking the 8 Active Characters via POST /api/worlds/linked-characters/{world_id}...")
    core_character_ids = [
        ("_t4J9aQNJM36cUKAP4wB4U", "Jasper Douglas"),
        ("_QPea6g4Q1QfeYCVHCLMPR", "Erik Douglas"),
        ("_T8Ywcr9FEqNf9JxbK6eHP", "Logan Douglas"),
        ("_RDfz7XzTpM23LpPALVXHM", "Malachia Douglas"),
        ("_zFLUjV8aVxQRAfQxGcAcY", "Noah Douglas"),
        ("_TbRM3EdxDjHFgqztTbCpL", "Edric Douglas"),
        ("_HEQQbbRFwKdG8QE2Fh1z1", "Wulfnic Douglas"),
        ("_zn24784jfcchQ7EwCyAnm", "Mackenzie Douglas")
    ]
    status, live_linked = api_request(f'/worlds/linked-characters/{world_id}')
    existing_linked_ids = set()
    if isinstance(live_linked, list):
        for c in live_linked:
            cid = c.get('id') or c.get('_id') or c.get('character_id') or (c.get('character', {}).get('id') if isinstance(c.get('character'), dict) else None)
            if cid:
                existing_linked_ids.add(cid)

    for cid, cname in core_character_ids:
        if cid not in existing_linked_ids:
            status, res = api_request(f'/worlds/linked-characters/{world_id}', data={'character_id': cid}, method='POST')
            print(f"  + Linked {cname} ({cid}): status {status}")
            time.sleep(0.1)
        else:
            print(f"  * {cname} ({cid}) already linked")

    status, live_linked = api_request(f'/worlds/linked-characters/{world_id}')
    print(f"SUCCESS: Verified {len(live_linked)} linked characters on cloud.")

    # 3. R3: Create the 7 Canonical Environments (POST /api/worlds/environments)
    print("\n[Step 3] Creating the 7 Canonical Environments via POST /api/worlds/environments...")
    
    environments_specs = [
        {
            "canonical_name": "1. California Coast",
            "name": "California Coast",
            "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba180ed1-e61d-4f1e-2305-c08aa7b40400/public",
            "description": "[ENVIRONMENT INFO:\nName: California Coast;\nDomain: Regional Coastal Macro-Biome;\nCoordinates & Span: Central California Pacific coastline spanning Blackwood County, Solarton, and northern Los Angeles;\nSetting & Metaphysics: Modern Supernatural Urban Fantasy, stable terrestrial reality, open supernatural society;\nDominant Presence: Werewolf Great Houses (Douglas, Marino, Rossi), SUCC Academic Body, Demi-human Communities, DCC, Mortal Municipalities]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Pacific ocean salt spray and ozone mingling with coastal pine resin, humid morning marine layer giving way to warm sunny afternoons, neon city glow after sunset;\nSpatial Architecture: Rugged Pacific cliffs, sandy beachheads, deep old-growth forests, urban commercial downtowns, coastal highway corridors;\nRifts & Dimensional Drift: Generally stable terrestrial baseline, though localized Reality Tears occasionally breach in remote canyons or deep forest clearings;\nHazards & Rules: Strict territorial pack jurisdictions, DCC private security enforcement, local council bylaws governing public supernatural manifestations]\n\n[CONTEXT & SECRETS:\nCosmology & Origins: Historic ancestral hub for native lupine lineages and modern supernatural integration, anchored along the Route 101 corridor;\nSecrets: Underground smuggling tunnels in Dockside, ancient Firstborn resting sites beneath the inland hills, concealed rift wards managed by the Douglas family]",
            "context_description": "[ENVIRONMENT INFO:\nName: California Coast;\nDomain: Regional Coastal Macro-Biome;\nCoordinates & Span: Central California Pacific coastline spanning Blackwood County, Solarton, and northern Los Angeles;\nSetting & Metaphysics: Modern Supernatural Urban Fantasy, stable terrestrial reality, open supernatural society;\nDominant Presence: Werewolf Great Houses (Douglas, Marino, Rossi), SUCC Academic Body, Demi-human Communities, DCC, Mortal Municipalities]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Pacific ocean salt spray and ozone mingling with coastal pine resin, humid morning marine layer giving way to warm sunny afternoons, neon city glow after sunset;\nSpatial Architecture: Rugged Pacific cliffs, sandy beachheads, deep old-growth forests, urban commercial downtowns, coastal highway corridors;\nRifts & Dimensional Drift: Generally stable terrestrial baseline, though localized Reality Tears occasionally breach in remote canyons or deep forest clearings;\nHazards & Rules: Strict territorial pack jurisdictions, DCC private security enforcement, local council bylaws governing public supernatural manifestations]\n\n[CONTEXT & SECRETS:\nCosmology & Origins: Historic ancestral hub for native lupine lineages and modern supernatural integration, anchored along the Route 101 corridor;\nSecrets: Underground smuggling tunnels in Dockside, ancient Firstborn resting sites beneath the inland hills, concealed rift wards managed by the Douglas family]",
            "keys": ["California Coast", "California", "Pacific Coast", "Route 101", "Bakersfield", "Los Angeles", "Hex Valley"]
        },
        {
            "canonical_name": "2. SUCC campus",
            "name": "SUCC campus",
            "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba180ed1-e61d-4f1e-2305-c08aa7b40400/public",
            "description": "[ENVIRONMENT INFO:\nName: SUCC campus (Supernatural University of Central California);\nDomain: Collegiate Supernatural Sanctuary & Academic Domain;\nCoordinates & Span: 129 Hocus Way, coastal Solarton, California;\nSetting & Metaphysics: Historic premier higher-education campus founded in 1887; balanced human-supernatural integration;\nDominant Presence: University Board of Regents, Student Body (8,000 students, 60/40 supernatural/human), Greek Row (10 houses), Faculty, DCC Fellows]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Salty sea breeze mingled with coffee from The Roasted Bean, old parchment, ozone from arcane labs, freshly cut athletic turf;\nSpatial Architecture: Collegiate gothic stone halls, arched cloisters, modern bioengineering glass cubes, Greek Row mansions, St. Neptune athletic complex;\nRifts & Dimensional Drift: Heavily anchored runic boundary wards preventing unauthorized dimensional tears on campus grounds;\nHazards & Rules: Strict scent suppressor compliance in lecture halls, mandatory neutral truce across rival houses and packs, no lethal dueling]\n\n[CONTEXT & SECRETS:\nCosmology & Origins: Established to foster peaceful co-existence and academic mastery between supernatural lineages and mortals;\nSecrets: The subterranean Basilica library basement (Room 005) hides forgotten pre-treaty pact archives and covert summoning circles]",
            "context_description": "The Supernatural University of Central California (SUCC). Founded in 1887, SUCC is one of the oldest and most prestigious supernatural colleges in the United States. 8,000 students, vibrant Greek life across 10 fraternity and sorority houses, high-tech magical labs, and competitive athletic complexes.",
            "keys": ["SUCC campus", "SUCC", "Supernatural University of Central California", "129 Hocus Way", "Greek Row", "Basilica Library"]
        },
        {
            "canonical_name": "3. Solarton",
            "name": "Solarton",
            "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba180ed1-e61d-4f1e-2305-c08aa7b40400/public",
            "description": "[ENVIRONMENT INFO:\nName: Solarton (Coastal College Town);\nDomain: Coastal Municipal & Mercantile District;\nCoordinates & Span: Coastal Southern California, population 35,621;\nSetting & Metaphysics: Eclectic, sunny, artistic coastal town centered around SUCC campus and Pacific beaches;\nDominant Presence: SUCC Students, Local Merchants, Werewolf Homesteads, Demihuman Residents, Surfers, Tourists]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Salty ocean air, sunscreen, warm asphalt, vintage vinyl shop dust, fish tacos, and coffee aromas;\nSpatial Architecture: Bricklane Mall outdoor shopping concourse, palm-lined coastal avenues, craftsman bungalows, beachfront piers;\nRifts & Dimensional Drift: Low ambient drift; occasional spatial anomalies along the coastal bluffs;\nHazards & Rules: Municipal bylaws, pack boundary respect, town-and-gown social friction]\n\n[CONTEXT & SECRETS:\nCosmology & Origins: Historic coastal fishing settlement transformed into a vibrant cultural hub alongside SUCC;\nSecrets: Coastal caves and old smuggler coves beneath the public beach used for illicit midnight gatherings and clandestine trade]",
            "context_description": "Solarton, CA. Eclectic coastal college town with a population of 35,621. Humans live alongside a high density of supernatural creatures, especially werewolves, demi-humans, and hybrids. Vibrant commercial centers like Bricklane Mall and Solarton Square.",
            "keys": ["Solarton", "Solarton CA", "Bricklane Mall", "Solarton Square", "Sidewinders"]
        },
        {
            "canonical_name": "4. Blackwood",
            "name": "Blackwood",
            "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public",
            "description": "[ENVIRONMENT INFO:\nName: Blackwood (Blackwood City & Forest Domain);\nDomain: Ancient Regional Supernatural Metropolis & Dense Forest Hinterland;\nCoordinates & Span: Central California Coast, population 250,000, 65% Supernatural;\nSetting & Metaphysics: Dark coastal metropolitan seat of power, pack heartland, corporate gothic towers, and primordial yew forest;\nDominant Presence: Douglas Pack Hegemony (Prime Alpha Erik Douglas), DCC West, Court of the Night (Vampire Council), Vito Marino Syndicate]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Wet asphalt, cold coastal mist, damp soil, pine resin, metallic ozone, and deep biological pack pheromones;\nSpatial Architecture: Gothic stone facades, towering glass skyscrapers (DCC Tower), industrial brick warehouses, harbor docks, deep ancient woods;\nRifts & Dimensional Drift: Heavily monitored by Kaladin's DCC sensor grid; deep forest boundary tears anchored by the primeval Yew;\nHazards & Rules: Strict territorial Pack Law, submission to Council arbitration, open treason answered with lethal force]\n\n[CONTEXT & SECRETS:\nHistory: Founded in 1666 AD via historical treaty between the Douglas Clan and the ancient Bloodmoon lineage of Wulfnic;\nSecrets: Subterranean vaults directly tap into the primeval root system of Wulfnic's monumental Yew tree in Blackwood Forest]",
            "context_description": "L'ombrosa sede urbana del potere soprannaturale in California. Divisa in distretti controllati dalle fazioni del Concilio (Uptown, Arcadia, Bluemoon, Oldtown, Dockside, Ironworks, Cable District). Sfera d'influenza diretta della DCC di Erik Douglas e della Court of the Night.",
            "keys": ["Blackwood", "Blackwood City", "Blackwood Forest", "Bluemoon", "Dockside", "Ironworks", "Arcadia", "Uptown", "The Verve"]
        },
        {
            "canonical_name": "5. Seven Hills",
            "name": "Seven Hills",
            "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public",
            "description": "[ENVIRONMENT INFO:\nName: Seven Hills (Aristocratic Pack Heartland & Douglas Estate Sanctuary);\nDomain: Sovereign Lupine Heartland & Fortress Enclave;\nCoordinates & Span: Blackwood City Heights, sovereign Douglas territory;\nSetting & Metaphysics: Prestigious gated hilltop ridge, sprawling estates, ancient blood-soil wards, and seat of Villa Douglas;\nDominant Presence: Erik Douglas (Prime Alpha), Douglas Family Members, Sworn Pack Elite, DCC Private Guards, Sentry Wolves]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Mountain-ocean breeze, fragrant eucalyptus, mature oaks, damp morning dew, and potent pack alpha scent markers;\nSpatial Architecture: Gated private roads, grand stone compounds, expansive landscaped terraces overlooking the city, Villa Douglas estate;\nSecurity & Wards: DCC automated checkpoint gates, 24/7 armed roving patrols, thermal radar fences, territorial lupine sentry posts;\nDemographics: Douglas dynasty, sworn lupine lineages, elite pack allies;\nRules & Restrictions: Entry by verified pass only, unauthorized vehicles towed, scent trespassers challenged on sight]\n\n[CONTEXT & SECRETS:\nHistory: Granted to the Douglas bloodline during the 1666 treaty, serving continuously as the ancestral seat of coastal pack rule;\nSecrets: Deep ridge caverns beneath Villa Douglas form an interconnected defensive bunker system equipped for prolonged siege]",
            "context_description": "Quartiere di lusso e cuore del territorio del branco Douglas a Blackwood City. Strade private, sorveglianza estrema, residenze storiche circondate da parchi privati e cancelli che non si aprono per caso. L'influenza dei Douglas qui e legge.",
            "keys": ["Seven Hills", "Villa Douglas", "Douglas Estate", "Seven Hills Heights"]
        },
        {
            "canonical_name": "6. DMHA HQ & Guild District",
            "name": "DMHA HQ & Guild District",
            "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba180ed1-e61d-4f1e-2305-c08aa7b40400/public",
            "description": "[ENVIRONMENT INFO:\nName: DMHA HQ & Guild District (Simi Valley / Hunter Operations);\nDomain: Dungeon Monster Hunting Association & Frontline Guild Enclave;\nCoordinates & Span: Simi Valley arid basin & California Hunter Command hub;\nSetting & Metaphysics: Frontier outpost and operational epicenter of dimensional fault disruptions, rift containment, and guild bounties;\nDominant Presence: DMHA Command, Certified Hunter Vanguard Teams (Team Ukiyo), Nomadic Enforcers (Marek), Black Vault Keepers, CCD]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Arid desert heat, ozone, scorched earth, machine oil, crackling high-voltage static, and iron-rich monster blood;\nSpatial Architecture: Heavy reinforced concrete bunkers, modular monitoring trailers, runic containment pylons, underground armories and holding cells;\nRifts & Dimensional Drift: Epicenter of frequent spatial tremors, micro-tears, and dungeon fusions requiring immediate tactical suppression;\nHazards & Rules: Full tactical loadouts required in combat sectors, strict registry for abyssal cores, no unlicensed rift dives]\n\n[CONTEXT & SECRETS:\nHistory: Established following the first dimensional fault ruptures in Simi Valley to coordinate planetary monster eradication and rift sealing;\nSecrets: The subterranean Black Vault stores unclassified abyssal relics and live rift anomalies under constant cryo-ward stasis]",
            "context_description": "Il Fronte del Vuoto e il comando cacciatori DMHA. Epicentro di disturbi magici e apertura delle faglie dei dungeon. Base operativa di Team Ukiyo, gestione taglie, armerie runiche, e sorveglianza delle fratture di realta.",
            "keys": ["DMHA HQ", "DMHA", "Guild District", "Simi Valley", "Team Ukiyo", "Hunter Guild", "The Grid"]
        },
        {
            "canonical_name": "7. Voidspace/Otherworld",
            "name": "Voidspace/Otherworld",
            "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba180ed1-e61d-4f1e-2305-c08aa7b40400/public",
            "description": "[ENVIRONMENT INFO:\nName: Voidspace/Otherworld (The Astral Ocean & Dimensional Tears);\nDomain: Cosmic Non-Euclidean Ocean, Pocket Realities & Dungeon Fractures;\nCoordinates & Span: Infinite dimensional expanse outside Euclidean spacetime, anchored facilities, and abyssal rift floors;\nSetting & Metaphysics: Cosmic horror and modern fantasy frontier; variable reality index, non-Euclidean geometry, gravity shear;\nDominant Presence: DDM Inc. (The Company), Contractors, Rift Entities, Cosmic Drifters, Primordial Horrors, Apex Dungeon Beasts]\n\n[LORE & PHENOMENOLOGY:\nAtmosphere & Senses: Pitch-black vacuum illuminated by distant cosmic halos; profound auditory silence broken only by the low hum of dimensional tension;\nSpatial Architecture: Anchored non-Euclidean corporate towers (DDM Inc. HQ), liminal roadside motels (Dead Dog Motel), abyssal dungeon floors (Hive Apex 1-18);\nRifts & Dimensional Drift: Reality shears create temporary and permanent tears connecting mortal California to the Astral Ocean;\nHazards & Rules: Extreme temporal dilation, metaphysical pressure, severe risk of dimensional slippage without an anchor or contractor beacon]\n\n[CONTEXT & SECRETS:\nCosmology & Origins: The primordial medium preceding all structured universes; fractured realms like The Otherworld drift suspended within its tides;\nSecrets: Derelict structures from dead universes floating in the deep current; secret clandestine tears bypassing mortal border authorities]",
            "context_description": "Il Vuoto, l'Oceano Astrale e le fratture di realta generate dalle faglie dei dungeon. DDM Inc., Dead Dog Motel, Trial Dungeons 1-18 e The Otherworld.",
            "keys": ["Voidspace", "Otherworld", "DDM Inc.", "Dead Dog Motel", "Trial Dungeon", "The Void", "reality tears", "squarci"]
        }
    ]

    env_id_map = {}
    status, live_existing_envs = api_request(f'/worlds/environments/world/{world_id}')
    if isinstance(live_existing_envs, list) and len(live_existing_envs) >= 7:
        print(f"SUCCESS: 7 Environments already exist on cloud for World '{world_id}'.")
        for env in live_existing_envs:
            ename = env.get('name')
            eid = env.get('id') or env.get('_id')
            env_id_map[ename] = eid
            for spec in environments_specs:
                if spec["name"] == ename:
                    env_id_map[spec["canonical_name"]] = eid
    else:
        for spec in environments_specs:
            env_payload = {
                "world_id": world_id,
                "world": world_id,
                "name": spec["name"],
                "description": spec["description"],
                "context_description": spec["context_description"],
                "avatar": spec["avatar"],
                "environment_config": {
                    "background": spec["avatar"],
                    "ambient_sound": "",
                    "music": "",
                    "particles": ""
                },
                "keys": spec["keys"],
                "key_logic": "AND_ANY",
                "secondary_keys": [],
                "case_sensitive": False,
                "whole_words_only": True,
                "brief_context_description": "",
                "key_position": "after_char",
                "included_lexicon_entries": [],
                "excluded_lexicon_entries": [],
                "final_instructions": ""
            }
            status, created_env = api_request('/worlds/environments', data=env_payload, method='POST')
            new_env_id = created_env.get('id') or created_env.get('_id')
            env_id_map[spec["canonical_name"]] = new_env_id
            env_id_map[spec["name"]] = new_env_id
            print(f"  + Created Environment [{spec['canonical_name']}]: ID '{new_env_id}' (Status {status})")
            time.sleep(0.1)

    print(f"SUCCESS: Environment ID Map: {env_id_map}")

    # 4. R3: Ingest 188 Canonical Locations (POST /api/worlds/locations)
    print("\n[Step 4] Ingesting 188 Canonical Locations via POST /api/worlds/locations...")
    with open(LOCATIONS_PATH, 'r', encoding='utf-8') as f:
        raw_locations = json.load(f)

    # Filter out the 8 decommissioned Digitalis entries
    off_ids = {
        "_p6WUaYcTJURrTXejecchk", "_RNU9Fx2pLD6PJ8LcKAdg6", "_J1B6d2DnNNyJhpnKWNcXz",
        "_94hRP4ywVYTHaUDDGfLqg", "_qe962a69a6PBbaHWCbP8r", "_BEnFGJPqBFJnTtrAHQQ9F",
        "_VMwRTPXdGTARktqnDLRTA", "_2rTUXXxAyYh8WYnGNtV2M"
    }
    canonical_188 = [l for l in raw_locations if (l.get('id') or l.get('_id')) not in off_ids]
    print(f"Filtered canonical location count: {len(canonical_188)} (Expected 188)")
    assert len(canonical_188) == 188, f"Expected exactly 188 locations, got {len(canonical_188)}"

    loc_source_map = {}
    for l in canonical_188:
        lid = l.get('id') or l.get('_id')
        loc_source_map[lid] = l

    def get_ancestors(lid):
        ancestors = []
        curr = lid
        while True:
            loc = loc_source_map.get(curr)
            if not loc: break
            pl = loc.get('parent_location')
            if not pl: break
            pid = pl.get('id') or pl.get('_id') if isinstance(pl, dict) else pl
            if not pid or pid not in loc_source_map: break
            ancestors.append((pid, loc_source_map[pid].get('name')))
            curr = pid
        return ancestors

    def assign_env_key(lid):
        loc = loc_source_map[lid]
        name = loc.get('name')
        ancestor_names = [a[1] for a in get_ancestors(lid)]
        all_names = [name] + ancestor_names
        
        if any(x in all_names for x in ["DDM Inc. // Voidspace", "The Otherworld", "Dead Dog Motel / Voidspace", "Trial Dungeon: Hive Apex Rift (Floors 1-18)"]):
            return "7. Voidspace/Otherworld"
        if any(x in all_names for x in ["Simi Valley", "Team Ukiyo Operational Base (Warehouse & Black Vault)"]):
            return "6. DMHA HQ & Guild District"
        if "Seven Hills" in all_names or "Villa Douglas" in all_names:
            return "5. Seven Hills"
        if "Supernatural University of Central California" in all_names:
            return "2. SUCC campus"
        if "Solarton" in all_names:
            return "3. Solarton"
        if "Blackwood City" in all_names:
            return "4. Blackwood"
        return "1. California Coast"

    # Compute depth for topological sorting
    def get_depth(lid):
        d = 0
        curr = lid
        while True:
            loc = loc_source_map.get(curr)
            if not loc: break
            pl = loc.get('parent_location')
            if not pl: break
            pid = pl.get('id') or pl.get('_id') if isinstance(pl, dict) else pl
            if not pid or pid not in loc_source_map: break
            d += 1
            curr = pid
        return d

    depth_groups = defaultdict(list)
    for lid, loc in loc_source_map.items():
        depth = get_depth(lid)
        depth_groups[depth].append(loc)

    print(f"Topological sorting depths: { {d: len(locs) for d, locs in sorted(depth_groups.items())} }")

    new_location_id_map = {} # old_id -> new_id
    deployed_locations_list = []

    status, live_existing_locs = api_request(f'/worlds/locations/world/{world_id}')
    if isinstance(live_existing_locs, list) and len(live_existing_locs) == 188:
        print(f"SUCCESS: All 188 Locations already exist on cloud for World '{world_id}' with 0 orphans.")
        deployed_locations_list = live_existing_locs
    else:
        # Iterate through depth 0 (roots), 1, 2, 3, 4
        for depth in sorted(depth_groups.keys()):
            loc_list = depth_groups[depth]
            print(f"  Processing Depth {depth} ({len(loc_list)} locations)...")
            for loc in loc_list:
                old_id = loc.get('id') or loc.get('_id')
                name = loc.get('name')
                target_env_key = assign_env_key(old_id)
                target_env_id = env_id_map[target_env_key]

                # Determine parent_location for new world
                pl = loc.get('parent_location')
                new_parent_id = None
                if pl:
                    old_parent_id = pl.get('id') or pl.get('_id') if isinstance(pl, dict) else pl
                    if old_parent_id in new_location_id_map:
                        new_parent_id = new_location_id_map[old_parent_id]
                    else:
                        raise RuntimeError(f"Parent location {old_parent_id} not yet created for {name} ({old_id}) at depth {depth}")

                # Specific handling for The Verve (_hfm1W4nYnXfQEqcNGwNxr)
                inc_lex = loc.get('included_lexicon_entries') or []
                if old_id == '_hfm1W4nYnXfQEqcNGwNxr':
                    print(f"    -> Wiring The Verve: secret bar at 808 Neon Ave with 3 item lexicon IDs")
                    inc_lex = ['_YxGJRFDkjdVyeH1mJNM1T', '_UVX1RAqE8CWz8ywYkT4Fm', '_BRjbkk8JM3Jw1xyJGgzDH']

                loc_payload = {
                    "world_id": world_id,
                    "world": world_id,
                    "environment": target_env_id,
                    "environment_id": target_env_id,
                    "name": name,
                    "description": loc.get('description') or "",
                    "context_description": loc.get('context_description') or "",
                    "brief_context_description": loc.get('brief_context_description') or "",
                    "keys": loc.get('keys') or [],
                    "key_logic": loc.get('key_logic') or "AND_ANY",
                    "secondary_keys": loc.get('secondary_keys') or [],
                    "case_sensitive": loc.get('case_sensitive') or False,
                    "whole_words_only": loc.get('whole_words_only') if loc.get('whole_words_only') is not None else True,
                    "key_position": loc.get('key_position') or "after_char",
                    "avatar": loc.get('avatar') or "",
                    "environment_config": loc.get('environment_config') or {
                        "background": "",
                        "ambient_sound": "",
                        "music": "",
                        "particles": ""
                    },
                    "included_lexicon_entries": inc_lex,
                    "excluded_lexicon_entries": loc.get('excluded_lexicon_entries') or [],
                    "final_instructions": loc.get('final_instructions') or ""
                }
                if new_parent_id:
                    loc_payload["parent_location"] = new_parent_id
                    loc_payload["parent_location_id"] = new_parent_id

                status, created_loc = api_request('/worlds/locations', data=loc_payload, method='POST')
                new_id = created_loc.get('id') or created_loc.get('_id')
                new_location_id_map[old_id] = new_id
                deployed_locations_list.append(created_loc)
                time.sleep(0.05)

        print(f"SUCCESS: Ingested all {len(new_location_id_map)} locations with 0 orphans.")

    # 5. R4: Bulk Ingestion of Mirrored Lexicon (POST /api/worlds/lexicon/bulk)
    print("\n[Step 5] Ingesting Mirrored Lexicon entries via POST /api/worlds/lexicon/bulk...")
    with open(LEXICON_PATH, 'r', encoding='utf-8') as f:
        raw_lexicon = json.load(f)

    # Core character card ID mappings for native suppression
    core_card_ids = {
        'erik': '_QPea6g4Q1QfeYCVHCLMPR',
        'malachia': '_RDfz7XzTpM23LpPALVXHM',
        'logan': '_T8Ywcr9FEqNf9JxbK6eHP',
        'jasper': '_t4J9aQNJM36cUKAP4wB4U',
        'noah': '_zFLUjV8aVxQRAfQxGcAcY',
        'edric': '_TbRM3EdxDjHFgqztTbCpL',
        'wulfnic': '_HEQQbbRFwKdG8QE2Fh1z1',
        'mackenzie': '_zn24784jfcchQ7EwCyAnm',
        'alyssa': '_6exg3yPfe2eCDK4hTftkh'
    }

    prepared_entries = []
    seen_entry_keys = set()

    for item in raw_lexicon:
        name = item.get('name') or "Untitled Entry"
        content = item.get('content') or ""
        # Strip em-dashes
        content = content.replace('—', ', ')
        name = name.replace('—', ', ')

        keys = item.get('keys') or []
        if not keys and name:
            keys = [name]
        
        secondary_keys = item.get('secondary_keys') or []
        selective = item.get('selective')
        if selective is None:
            selective = True if secondary_keys or item.get('type') == 'npc' else False

        # Native suppression configuration
        ignored_characters = list(item.get('ignored_characters') or [])
        ignored_personas = list(item.get('ignored_personas') or [])

        name_lower = name.lower()
        for cname, cid in core_card_ids.items():
            if cname in name_lower and item.get('type') == 'npc':
                if cid and cid not in ignored_characters:
                    ignored_characters.append(cid)
                if cname == 'jasper' and '1792155173728' not in ignored_personas:
                    ignored_personas.append('1792155173728')
                if cname == 'alyssa' and 'persona_1786335754946' not in ignored_personas:
                    ignored_personas.append('persona_1786335754946')

        entry_obj = {
            "name": name,
            "type": item.get('type') or "lore/concept",
            "content": content,
            "keys": keys,
            "key_logic": "AND_ANY",
            "secondary_keys": secondary_keys,
            "selective": selective,
            "is_global": item.get('is_global') if item.get('is_global') is not None else False,
            "scan_persona": True,
            "whole_words_only": True,
            "enableEntryHighlighting": True,
            "highlight_keys": True,
            "ignored_characters": ignored_characters,
            "ignored_personas": ignored_personas,
            "attached_world_character_id": None,
            "avatar": item.get('avatar') or "",
            "custom_avatar_regex": item.get('custom_avatar_regex') or False,
            "lines_parsed": item.get('lines_parsed') or 2,
            "enabled": True,
            "position": item.get('position') or "after_char",
            "insertion_order": item.get('insertion_order') or 10,
            "priority": item.get('priority') or 0
        }
        prepared_entries.append(entry_obj)
        seen_entry_keys.add(name)

    # Also add the 3 specific items for The Verve if missing
    verve_items_specs = [
        {
            "name": "Wireless Earbuds",
            "type": "item",
            "content": "Wireless earbuds, tangled charging case included. Half the time one earbud is missing.",
            "keys": ["earbuds", "wireless earbuds"],
            "secondary_keys": [],
            "selective": False,
            "is_global": False
        },
        {
            "name": "Lighter",
            "type": "item",
            "content": "A basic pocket lighter. Reliable, cheap, easy to lose, easier to bum off someone else.",
            "keys": ["lighter", "zippo"],
            "secondary_keys": [],
            "selective": False,
            "is_global": False
        },
        {
            "name": "Keys",
            "type": "item",
            "content": "A small ring of keys, house, car, maybe a locker or a second address someone doesn't know about.",
            "keys": ["keys", "keychain"],
            "secondary_keys": [],
            "selective": False,
            "is_global": False
        }
    ]

    for vi in verve_items_specs:
        if vi["name"] not in seen_entry_keys:
            prepared_entries.append({
                "name": vi["name"],
                "type": vi["type"],
                "content": vi["content"],
                "keys": vi["keys"],
                "key_logic": "AND_ANY",
                "secondary_keys": vi["secondary_keys"],
                "selective": vi["selective"],
                "is_global": vi["is_global"],
                "scan_persona": True,
                "whole_words_only": True,
                "enableEntryHighlighting": True,
                "highlight_keys": True,
                "ignored_characters": [],
                "ignored_personas": [],
                "attached_world_character_id": None,
                "avatar": "",
                "custom_avatar_regex": False,
                "lines_parsed": 2,
                "enabled": True,
                "position": "after_char",
                "insertion_order": 10,
                "priority": 1
            })

    print(f"Total prepared lexicon entries: {len(prepared_entries)}")

    # Check existing lexicon in world
    status, live_existing_lex = api_request(f'/worlds/lexicon/world/{world_id}')
    existing_lex_names = set(e.get('name') for e in (live_existing_lex or []))
    print(f"Existing live lexicon entries in world: {len(existing_lex_names)}")

    entries_to_create = [e for e in prepared_entries if e['name'] not in existing_lex_names]
    print(f"Lexicon entries remaining to ingest: {len(entries_to_create)}")

    # Bulk create in chunks of 50
    BATCH_SIZE = 50
    total_created_lex = len(existing_lex_names)
    for i in range(0, len(entries_to_create), BATCH_SIZE):
        batch = entries_to_create[i:i+BATCH_SIZE]
        bulk_payload = {
            "world_id": world_id,
            "entries": batch
        }
        status, res_entries = api_request('/worlds/lexicon/bulk', data=bulk_payload, method='POST')
        count = len(res_entries) if isinstance(res_entries, list) else len(batch)
        total_created_lex += count
        print(f"  + Ingested lexicon batch {i//BATCH_SIZE + 1} ({count} entries, status {status})")
        time.sleep(0.15)

    print(f"SUCCESS: World has {total_created_lex} lexicon entries.")

    # 6. Link Characters from /characters/mine (POST /api/worlds/linked-characters/{world_id})
    print("\n[Step 6] Verifying/Linking 8 active character cards from /characters/mine...")
    active_character_ids = [
        ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper Douglas'),
        ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik Douglas'),
        ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan Douglas'),
        ('_RDfz7XzTpM23LpPALVXHM', 'Malachia Douglas'),
        ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah Douglas'),
        ('_TbRM3EdxDjHFgqztTbCpL', 'Edric Douglas'),
        ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic Douglas'),
        ('_zn24784jfcchQ7EwCyAnm', 'Mackenzie Douglas')
    ]
    status, live_linked = api_request(f'/worlds/linked-characters/{world_id}')
    existing_linked_ids = set()
    if isinstance(live_linked, list):
        for c in live_linked:
            cid = c.get('id') or c.get('_id') or c.get('character_id') or (c.get('character', {}).get('id') if isinstance(c.get('character'), dict) else None)
            if cid: existing_linked_ids.add(cid)

    for cid, cname in active_character_ids:
        if cid not in existing_linked_ids:
            status, ldata = api_request(f'/worlds/linked-characters/{world_id}', data={'character_id': cid}, method='POST')
            print(f"  + Linked character {cname} ({cid}): status {status}")
            time.sleep(0.1)
        else:
            print(f"  * Character {cname} ({cid}) already linked")

    status, live_linked = api_request(f'/worlds/linked-characters/{world_id}')
    print(f"SUCCESS: Verified {len(live_linked)} linked characters on cloud.")

    # 7. Fetch Full Snapshot from Cloud & Save (scratch/world_new_deployed.json)
    print("\n[Step 7] Fetching complete deployed World state from Wyvern Web API...")
    status, final_world = api_request(f'/worlds/{world_id}')
    status, live_environments = api_request(f'/worlds/environments/world/{world_id}')
    status, live_locations = api_request(f'/worlds/locations/world/{world_id}')
    status, live_lexicon = api_request(f'/worlds/lexicon/world/{world_id}')
    status, live_linked = api_request(f'/worlds/linked-characters/{world_id}')

    if not final_world.get('linked_characters'):
        final_world['linked_characters'] = live_linked

    print(f"Cloud Verification:")
    print(f"  World ID: {final_world.get('id') or final_world.get('_id')}")
    print(f"  Name: {final_world.get('name')}")
    print(f"  World Age: {final_world.get('world_age')}")
    print(f"  Live Environments: {len(live_environments)}")
    print(f"  Live Locations: {len(live_locations)}")
    print(f"  Live Lexicon Entries: {len(live_lexicon)}")
    print(f"  Live Linked Characters: {len(live_linked)}")

    full_snapshot = {
        "world": final_world,
        "world_environments": live_environments,
        "world_locations": live_locations,
        "world_lexicon": live_lexicon,
        "world_linked_characters": live_linked,
        # Frontend Zod Parity: entries == lexicon byte-for-byte
        "entries": live_lexicon,
        "lexicon": live_lexicon,
        "metadata": {
            "deployed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "deployed_by": "worker_deploy_world",
            "environment_id_map": env_id_map,
            "total_locations": len(live_locations),
            "total_environments": len(live_environments),
            "total_lexicon": len(live_lexicon),
            "total_linked_characters": len(live_linked),
            "world_id": world_id
        }
    }

    with open(OUTPUT_SNAPSHOT_PATH, 'w', encoding='utf-8') as f:
        json.dump(full_snapshot, f, indent=2, ensure_ascii=False)
    print(f"SUCCESS: Saved full snapshot to {OUTPUT_SNAPSHOT_PATH}")

    print("\n" + "=" * 70)
    print(f"DEPLOYMENT COMPLETE: WORLD ID '{world_id}' IS LIVE")
    print("=" * 70)

if __name__ == '__main__':
    main()
