"""
scripts/deploy_scenarios_anti_collision_and_sync.py
Deploy Anti-Collision Lua Startup Script, Starting Equipment, Currencies, Attitudes,
and transport/sync Standalone Character Scenarios into World _YpX47fNraQFw2dD7TdycJ.
"""

import os
import sys
import json
import urllib.request
import urllib.error

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.sync_from_wyvern_web import get_auth_token

WORLD_ID = "_YpX47fNraQFw2dD7TdycJ"
LUNAR_QUAD_ID = "_aPqjQX8UBNTC9y2tEUdX3"
CAMPUS_ENV_ID = "_38JCUykN4wwRfgGjQyjLr"

USD_CURRENCY_ID = "fbecc738-f9f7-4426-b8a1-a237b8ad922c"
DMHA_CR_CURRENCY_ID = "8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a"

ALYSSA_CHAR_ID = "_6exg3yPfe2eCDK4hTftkh"
JASPER_CHAR_ID = "_t4J9aQNJM36cUKAP4wB4U"

STANDALONE_6_LBS = [
    '_gwwCxCfQ6PQaLEjAQVpJL', # Lorebook I
    '_HfG7TeV6MJyj6bxMwxkpt', # Lorebook II
    '_9zWTGqYJNJ4BCDMj8gfcD', # Lorebook III
    '_EjXxkmPVhpCXg8xABpFkK', # Location
    '_zwEqgEEzh12X6gHVmMKKC', # NPC Primary
    '_Uht3Ckz44JBDrPnUHq7LV'  # NPC Secondary
]

LUA_STARTUP_SCRIPT = """-- Svartulfr Scenario Anti-Collision & Persona Setup Script
-- 1. Anti-Collision & Slot Resolution
--    Suppresses entity corresponding to {{user}} from being duplicated as companion or slot NPC.
--    Assigns the twin slot to the opposite twin.
-- 2. Inject Starting Currencies into party / world_party:
--    USD (fbecc738-f9f7-4426-b8a1-a237b8ad922c): 500
--    DMHA Credits (8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a): 250
-- 3. Inject Starting Inventory & Equipment for {{user}}
-- 4. Initialize Family & Companion Attitudes / Relationship Bonds

local alyssa_id = '_6exg3yPfe2eCDK4hTftkh'
local jasper_id = '_t4J9aQNJM36cUKAP4wB4U'

local p_id = (user and (user.persona_id or user.id)) or (memory and memory._scenario and memory._scenario.persona_id) or ''
local u_name = string.lower((user and user.name) or '')
local sub = string.lower((user and (user.pronoun_subjective or (user.pronouns and user.pronouns.subjective))) or '')
local obj = string.lower((user and (user.pronoun_objective or (user.pronouns and user.pronouns.objective))) or '')

local is_alyssa = (p_id == 'persona_1786335754946' or p_id == 'user_persona_VnRF2xGeG1C4xByDF9h9R' or string.find(u_name, 'alyssa') ~= nil)
local is_jasper = (p_id == '1792155173728' or p_id == 'user_persona_bGDFCEtKDzVmgbCmHJWEW' or string.find(u_name, 'jasper') ~= nil)

if not is_alyssa and not is_jasper then
    if sub == 'he' or obj == 'him' or string.find(u_name, 'maschio') or string.find(u_name, 'male') then
        is_jasper = true
    elseif sub == 'she' or obj == 'her' or string.find(u_name, 'femmina') or string.find(u_name, 'female') then
        is_alyssa = true
    else
        math.randomseed(os.time())
        if math.random(1, 2) == 1 then is_alyssa = true else is_jasper = true end
    end
end

-- 1. Anti-Collision & Slot Assignment
if memory and memory._scenario and memory._scenario.assignments then
    if is_alyssa then
        memory._scenario.assignments['twin'] = jasper_id
        memory._scenario.suppressed_character_id = alyssa_id
    else
        memory._scenario.assignments['twin'] = alyssa_id
        memory._scenario.suppressed_character_id = jasper_id
    end
end

-- 2. Inject Starting Currencies (USD 500, DMHA Cr 250)
local function apply_currencies(target)
    if target then
        if not target.currency_balances then target.currency_balances = {} end
        target.currency_balances['fbecc738-f9f7-4426-b8a1-a237b8ad922c'] = 500
        target.currency_balances['8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a'] = 250
    end
end

apply_currencies(world_party)
apply_currencies(party)
if memory and memory._scenario then
    apply_currencies(memory._scenario)
end

-- 3. Inject Starting Equipment & Inventory
local function get_starter_inventory(for_alyssa)
    if for_alyssa then
        return {
            { id = 'item_pochette', name = 'Dimensional Medicine Pochette', description = 'Enchanted velvet pochette containing silver-threaded trauma bandages, moonstone restorative tincture, diagnostic stylus, and botanical salves.', quantity = 1, equipped = true },
            { id = 'item_succ_id_alyssa', name = 'SUCC Student Smart Card (Alyssa)', description = 'Official collegiate NFC smart badge granting access to Theta Iota Theta Sorority House, Hydra Hall, and Aetheris Clinic laboratories.', quantity = 1, equipped = true },
            { id = 'item_dcc_commlink_alyssa', name = 'DCC Encrypted Comm-Link', description = 'Hardened Douglas Commercial Coalition smartphone with dual-band biometric encryption and direct pack-priority frequency.', quantity = 1, equipped = true }
        }
    else
        return {
            { id = 'item_cyberdeck_jasper', name = 'Custom Arcane Cyberdeck HUD Rig', description = 'Hand-modified holographic neural cyberdeck with integrated RF spectrum scanner, sub-dermal audio jack interface, and DJ Frequency scrambler.', quantity = 1, equipped = true },
            { id = 'item_succ_id_jasper', name = 'SUCC Student Smart Card (Jasper)', description = 'Official collegiate NFC smart badge granting access to Wyrm Hall Suite 304, Arcane Engineering server rooms, and campus antenna hubs.', quantity = 1, equipped = true },
            { id = 'item_dcc_phone_jasper', name = 'DCC Encrypted Smartphone', description = 'Military-spec corporate device running custom rooted OS with packet sniffing daemons and direct line to Villa Douglas.', quantity = 1, equipped = true }
        }
    end
end

local starter_items = get_starter_inventory(is_alyssa)

local function apply_inventory(target)
    if target then
        if not target.inventory then target.inventory = {} end
        for _, item in ipairs(starter_items) do
            table.insert(target.inventory, item)
        end
    end
end

apply_inventory(world_party)
apply_inventory(party)
if memory and memory._scenario then
    apply_inventory(memory._scenario)
end

-- 4. Initial Attitudes & Relationship Pacing Bonds
local function apply_attitudes(target)
    if target then
        if not target.attitudes then target.attitudes = {} end
        target.attitudes['pack_family'] = { bond = 'Deep Unbreakable Pack Loyalty', trust = 100, romantic_interest = 0, familial_respect = 100 }
        target.attitudes['campus_peers'] = { bond = 'Warm Collegiate Fellowship', trust = 70, romantic_interest = 10, respect = 75 }
    end
end

apply_attitudes(world_party)
apply_attitudes(party)
if memory and memory._scenario then
    apply_attitudes(memory._scenario)
end
"""

def clean_formatting(text: str) -> str:
    """Enforces no em-dash."""
    return text.replace("—", ", ")

def api_request(url, method='GET', data=None, token=None):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    payload = json.dumps(data, ensure_ascii=False).encode('utf-8') if data is not None else None
    req = urllib.request.Request(url, data=payload, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode('utf-8')
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as err:
        err_body = err.read().decode('utf-8')
        return err.code, err_body
    except Exception as e:
        return 500, str(e)

def update_standalone_character_scenarios(token):
    print("\n=== STEP 1: UPDATING STANDALONE CHARACTER SCENARIOS ===")
    
    scenario_files = [
        ('FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'char_scenario_CKgwq246DyCj1NNTBV9rt'),
        ('FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json', 'char_scenario_Kq4mJEBH83j7Q7DdVfFnF'),
        ('FINAL/Svartulfr_Master_Scenario.json', 'char_scenario_1DC43ggb6mB8YLJDJKrU4')
    ]
    
    for filepath, sid in scenario_files:
        full_path = os.path.join(ROOT_DIR, filepath)
        with open(full_path, 'r', encoding='utf-8') as f:
            scen_data = json.load(f)
            
        print(f"\nProcessing {filepath} (ID: {sid})...")
        
        # 1. Update startup_script
        scen_data['startup_script'] = LUA_STARTUP_SCRIPT
        
        # 2. Update linked_world_id
        scen_data['linked_world_id'] = WORLD_ID
        
        # 3. Clean formatting discipline in scenario description / prompt
        if 'scenario' in scen_data:
            scen_data['scenario'] = clean_formatting(scen_data['scenario'])
            
        # 4. Enforce unavailable_count: 0 on all slots
        slots = scen_data.get('slots', [])
        for slot in slots:
            slot['unavailable_count'] = 0
            
        # 5. Ensure 6 Standalone Lorebooks in lorebook_ids
        cur_lb_ids = scen_data.get('lorebook_ids', [])
        for lb in STANDALONE_6_LBS:
            if lb not in cur_lb_ids:
                cur_lb_ids.append(lb)
        scen_data['lorebook_ids'] = cur_lb_ids
        
        # Save locally
        with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(scen_data, f, indent=2, ensure_ascii=False)
        print(f"  [SAVED LOCALLY] {filepath}")
        
        # Sync via Wyvern API if scenario exists live
        url = f"https://app.wyvern.chat/api/character-scenarios/{sid}"
        # Fetch current revision from server first to prevent conflict
        status_get, live_scen = api_request(url, method='GET', token=token)
        if status_get == 200 and isinstance(live_scen, dict):
            live_rev = live_scen.get('revision', scen_data.get('revision', 0))
            payload = dict(scen_data)
            payload['revision'] = live_rev
            status_put, resp = api_request(url, method='PUT', data=payload, token=token)
            print(f"  [API PUT] {sid} (rev {live_rev}) -> HTTP {status_put}")
            if status_put == 200 and isinstance(resp, dict):
                # Update local revision if changed
                scen_data['revision'] = resp.get('revision', live_rev + 1)
                with open(full_path, 'w', encoding='utf-8') as f:
                    json.dump(scen_data, f, indent=2, ensure_ascii=False)
        else:
            print(f"  [API NOTE] Scenario {sid} GET returned {status_get} (standalone archive)")

def sync_world_scenarios(token):
    print("\n=== STEP 2: TRANSPORT & SYNC WORLD SCENARIOS IN WORLD _YpX47fNraQFw2dD7TdycJ ===")
    
    world_url = f"https://app.wyvern.chat/api/worlds/scenarios/world/{WORLD_ID}"
    status_list, live_world_scens = api_request(world_url, method='GET', token=token)
    print(f"Current World Scenarios count: {len(live_world_scens) if isinstance(live_world_scens, list) else 0}")
    
    existing_by_name = {}
    if isinstance(live_world_scens, list):
        for s in live_world_scens:
            name = (s.get('name') or s.get('title') or '').strip().lower()
            existing_by_name[name] = s
            print(f"  Existing World Scenario: '{s.get('name') or s.get('title')}' (ID: {s.get('id')})")
            
    # Definitions for World Scenarios corresponding to standalone collegiate routes & master
    # 1. Alyssa Route
    with open(os.path.join(ROOT_DIR, 'FINAL', 'scenarios', 'Svartulfr_Scenario_SUCC_Route_Alyssa.json'), 'r', encoding='utf-8') as f:
        alyssa_scen = json.load(f)
        
    # 2. Jasper Route
    with open(os.path.join(ROOT_DIR, 'FINAL', 'scenarios', 'Svartulfr_Scenario_SUCC_Route_Jasper.json'), 'r', encoding='utf-8') as f:
        jasper_scen = json.load(f)
        
    # 3. Master Scenario
    with open(os.path.join(ROOT_DIR, 'FINAL', 'Svartulfr_Master_Scenario.json'), 'r', encoding='utf-8') as f:
        master_scen = json.load(f)
        
    active_characters = [
        {"character_id": "_t4J9aQNJM36cUKAP4wB4U", "participation_weight": 50}, # Jasper
        {"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "participation_weight": 50}, # Erik
        {"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "participation_weight": 50}, # Logan
        {"character_id": "_RDfz7XzTpM23LpPALVXHM", "participation_weight": 50}, # Malachia
        {"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "participation_weight": 50}, # Noah
        {"character_id": "_TbRM3EdxDjHFgqztTbCpL", "participation_weight": 50}, # Edric
        {"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "participation_weight": 50}, # Wulfnic
        {"character_id": "_zn24784jfcchQ7EwCyAnm", "participation_weight": 50}, # Mackenzie
        {"character_id": "_CmkCDzCn36CyYUzfPp2UY", "participation_weight": 50}  # Zeera
    ]
    playable_ids = [c["character_id"] for c in active_characters]

    # Convert greetings into premade_scenes format
    def convert_greetings_to_premade(greetings, default_desc):
        scenes = []
        for g in greetings:
            gid = g.get('id') or f"scene-{len(scenes)}"
            text = clean_formatting(g.get('text', ''))
            desc = g.get('title') or default_desc
            scenes.append({
                "id": gid,
                "description": desc,
                "scene_text": text
            })
        return scenes

    world_scenarios_to_deploy = [
        {
            "filename": "Svartulfr_World_Scenario_SUCC_Welcome_Day.json",
            "name": "SUCC: Welcome Day al Lunar Quad",
            "description": "26 agosto 2024. Cerimonia inaugurale del Welcome Day sul Lunar Quad della SUCC con tutta la famiglia Douglas-Bloodmoon (Noah, Malachia, Jasper, Alyssa, Erik, Logan ed Edric), l'arrivo a sorpresa di Wulfnic in maglietta gag che iscrive Zefir in versione punk come cugino islandese, e l'incontro con Scarlett, Sierra e Finn.",
            "scenario_premise": "Il 26 agosto 2024 segna l'inizio ufficiale dell'anno accademico alla Supernatural University of Central California (SUCC). Sul Lunar Quad, gremito di matricole, famiglie e docenti sotto gli stendardi cremisi e oro, l'intero clan Douglas-Bloodmoon accompagna i suoi studenti per la cerimonia d'apertura.",
            "tags": ["succ", "welcome-day", "lunar-quad", "douglas", "bloodmoon", "solarton", "college", "werewolf"],
            "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public",
            "location_id": LUNAR_QUAD_ID,
            "environment_id": CAMPUS_ENV_ID,
            "premade_scenes": [
                s for s in json.load(open(os.path.join(ROOT_DIR, 'FINAL', 'scenarios', 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json'), encoding='utf-8')).get('premade_scenes', [])
            ],
            "scene_instructions": "Capture the collegiate atmosphere, family dynamics, and pack instincts of the Douglas-Bloodmoon clan on the SUCC campus during the Fall 2024 Welcome Day. Highlight protective banter between Erik, Logan, and the older brothers, Wulfnic's comedic yet fierce presence enrolling Zefir as an undercover freshman punk, and the interactions with Scarlett, Sierra, and Finn. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."
        },
        {
            "filename": "Svartulfr_World_Scenario_SUCC_Route_Alyssa.json",
            "name": "SUCC: Collegiate Arc (Alyssa Route)",
            "description": "Segui il primo anno accademico di Alyssa Hvit Douglas Bloodmoon alla SUCC. Dalle lezioni di botanica e medicina con Scarlett Rose e Stanley Davies Jr., alla vita nella sorority Theta Iota Theta con Sierra Cruz, gli incontri musicali con Mackenzie dei Sidewinders, la rivalità sportiva tra Finn Novak e Vincent Campbell, e il supporto continuo di Jasper.",
            "scenario_premise": "Alyssa Hvit Douglas Bloodmoon inizia il suo percorso universitario come matricola Pre-Med alla SUCC. Residente nella sorority Theta Iota Theta, si divide tra lezioni cliniche, il tirocinio alla clinica Aetheris, e le dinamiche complesse del campus sovrannaturale.",
            "tags": ["succ", "alyssa", "college", "romance", "healer", "douglas", "bloodmoon"],
            "avatar": alyssa_scen.get('avatar'),
            "location_id": LUNAR_QUAD_ID,
            "environment_id": CAMPUS_ENV_ID,
            "premade_scenes": convert_greetings_to_premade(alyssa_scen.get('greetings', []), "SUCC Collegiate Scene (Alyssa Route)"),
            "scene_instructions": "Depict Alyssa Hvit Douglas Bloodmoon's collegiate life at SUCC. Maintain strict format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. Respect single-pair ear anatomy for demi-humans and werewolves, and Sierra Cruz's continuous serpentine locomotion (no legs/feet, slithers on iridescent rainbow tail)."
        },
        {
            "filename": "Svartulfr_World_Scenario_SUCC_Route_Jasper.json",
            "name": "SUCC: Collegiate Arc (Jasper Route)",
            "description": "Vivi il primo anno universitario dal punto di vista di Jasper Svartr Douglas Bloodmoon. Dalle sessioni di hacking e le serate in Suite 304 con Russ Sinclair e i Cocketeers, i collegamenti neurali con l'IA Echo, i rave underground come DJ Frequency, i confronti con Vincent Campbell e Jared Thompson, fino ai momenti intimi con Scarlett Rose.",
            "scenario_premise": "Jasper Svartr Douglas Bloodmoon affronta il primo anno di Ingegneria Arcana alla SUCC, tra la residenza Wyrm Hall Suite 304, l'antenna hacker sui tetti del campus, i rave clandestini nel porto e la protezione invisibile della sorella Alyssa.",
            "tags": ["succ", "jasper", "college", "hacking", "cyber-sentinel", "douglas", "bloodmoon"],
            "avatar": jasper_scen.get('avatar'),
            "location_id": LUNAR_QUAD_ID,
            "environment_id": CAMPUS_ENV_ID,
            "premade_scenes": convert_greetings_to_premade(jasper_scen.get('greetings', []), "SUCC Collegiate Scene (Jasper Route)"),
            "scene_instructions": "Depict Jasper Svartr Douglas Bloodmoon's collegiate life at SUCC. Maintain strict format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. Scarlett Rose has candy-pink hair, matching eyes, and scarlet horns; Sierra Cruz is a legless lamia who moves by coiling and slithering."
        },
        {
            "filename": "Svartulfr_World_Scenario_Master_Omnibus.json",
            "name": "Svartúlfr: Vita al Campus SUCC & Missioni di Gilda",
            "description": "Lo scenario corale omnibus dello SvartúlfrVerse: riunisce l'intero clan Douglas-Bloodmoon, le lezioni alla SUCC, le serate a Greek Row, le missioni e contratti nei Rift della Gilda DMHA, i concerti al Sidewinders e le cene di casata a Villa Douglas.",
            "scenario_premise": "L'esperienza completa e convergente dello SvartúlfrVerse nell'anno accademico 2024-2025. Unisce la vita accademica, i legami di branco, e le esplorazioni sovrannaturali in California.",
            "tags": ["svartulfr", "campus", "dmha", "guild", "douglas", "bloodmoon", "master"],
            "avatar": master_scen.get('avatar'),
            "location_id": LUNAR_QUAD_ID,
            "environment_id": CAMPUS_ENV_ID,
            "premade_scenes": convert_greetings_to_premade(master_scen.get('greetings', [])[:5], "Master Omnibus Scene"),
            "scene_instructions": "Master Omnibus Scenario Guidelines: Balance active scene characters naturally according to their canonical JED+ voice, attitudes, and pack hierarchies. Strict anti-ventriloquism for {{user}}. Dialogue in quotes, plain text narration, zero em-dashes."
        }
    ]

    for ws_def in world_scenarios_to_deploy:
        name_key = ws_def['name'].strip().lower()
        matched = existing_by_name.get(name_key)
        
        # Also match if 'welcome day' is in both
        if not matched and 'welcome day' in name_key:
            for k, v in existing_by_name.items():
                if 'welcome day' in k:
                    matched = v
                    break

        payload = {
            "world_id": WORLD_ID,
            "world": WORLD_ID,
            "name": ws_def['name'],
            "description": ws_def['description'],
            "scenario_premise": ws_def['scenario_premise'],
            "tags": ws_def['tags'],
            "community_tags": [],
            "avatar": ws_def['avatar'],
            "location_id": ws_def['location_id'],
            "environment_id": ws_def['environment_id'],
            "insertion_point": 10489906,
            "visibility": "private",
            "rating": "explicit",
            "world_only": False,
            "scenario_type": "any",
            "include_character_select": True,
            "include_rpg_build": False,
            "playable_character_ids": playable_ids,
            "included_character_pool": active_characters,
            "scene_instructions": ws_def['scene_instructions'],
            "premade_scenes": ws_def['premade_scenes']
        }
        
        if matched:
            sid = matched.get('id') or matched.get('_id')
            print(f"\nUpdating existing World Scenario: '{ws_def['name']}' (ID: {sid})...")
            url = f"https://app.wyvern.chat/api/worlds/scenarios/{sid}"
            status, res = api_request(url, method='PUT', data=payload, token=token)
            print(f"  [PUT] {sid} -> HTTP {status}")
            actual_id = sid
            actual_data = res if isinstance(res, dict) and res.get('id') else {**payload, "id": sid}
        else:
            print(f"\nCreating new World Scenario: '{ws_def['name']}' in World {WORLD_ID}...")
            url = "https://app.wyvern.chat/api/worlds/scenarios"
            status, res = api_request(url, method='POST', data=payload, token=token)
            print(f"  [POST] Created -> HTTP {status}")
            if isinstance(res, dict) and res.get('id'):
                actual_id = res['id']
                actual_data = res
            else:
                print(f"  [ERROR] Failed to parse created scenario response: {res}")
                continue

        # Save to FINAL/scenarios/{filename} for Omni-Parity
        target_file = os.path.join(ROOT_DIR, 'FINAL', 'scenarios', ws_def['filename'])
        with open(target_file, 'w', encoding='utf-8') as f:
            json.dump(actual_data, f, indent=2, ensure_ascii=False)
        print(f"  [SAVED WORLD SCENARIO] {target_file} (ID: {actual_id})")

def main():
    token = get_auth_token()
    print("=" * 60)
    print("STARTING SCENARIO ANTI-COLLISION & WORLD PARITY SYNCHRONIZATION")
    print("=" * 60)
    
    update_standalone_character_scenarios(token)
    sync_world_scenarios(token)
    
    print("\n" + "=" * 60)
    print("SYNCHRONIZATION COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == '__main__':
    main()
