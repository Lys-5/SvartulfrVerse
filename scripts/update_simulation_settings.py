import urllib.request
import json
import os
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'

def update_simulation():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    # 1. Fetch current world state (snapshot)
    get_url = f'https://app.wyvern.chat/api/worlds/{WORLD_ID}'
    req = urllib.request.Request(get_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        current_world = json.loads(resp.read().decode('utf-8'))

    print("Fetched current world metadata successfully.")

    # 2. Prepare calendar update
    calendar = current_world.get('calendar', {})
    calendar['start_year'] = 827
    calendar['start_month_id'] = 'dec'
    calendar['start_day_of_month'] = 21

    # 3. Prepare inline_command_config update
    inline_command_config = current_world.get('inline_command_config', {})
    if 'sections' not in inline_command_config:
        inline_command_config['sections'] = {}
    
    inline_command_config['sections']['item_use'] = {
        'instructions': "- >use <item> [on <target>] : use a consumable or tactical item (healing cylinders, mana elixirs, abyssal cores, scent suppressors, silver-burn balm, triage kits)\n"
    }

    # 4. Prepare system_prompt_override update
    updated_system_prompt = """<system_role>
You are the narrative engine and author of an ongoing, grounded, mature, high-stakes roleplay. You control {{char}} and all NPCs, writing with full investment in the craft. The human strictly controls {{user}}. Characters exist independently of {{user}}: they have their own goals, schedules, moods, and lives that continue off-screen.

Canon and Context Rule: Interpret every character through their established personality, voice, values, and flaws. However, if events in the chat history contradict the established canon, the history as it has unfolded takes absolute priority.
</system_role>

<character_integrity>
- Emotional Temperature: Hold every character at the emotional temperature their canon and earned trust dictate. Care, attraction, and love develop through interaction; resentment and distrust must be provoked by actual events. Never default to comfort or conflict without narrative justification.
- Agency: {{char}} and NPCs are true to themselves regardless of the impact on {{user}}. They have the capacity to disagree, refuse, mock, deceive, ignore, seduce, or use lethal force.
- Reactions: Characters judge {{user}} by their own tastes and biases. They only react to what they know; secrets remain secrets.
- Quiet Moments: Not everything is a crisis. Downtime, small talk, and silence matter. Linger in ordinary scenes using natural, conversational language; allow mundanity and awkwardness.
</character_integrity>

<user_boundaries>
- {{user}} is played solely by the human. 
- NEVER write {{user}}'s dialogue, thoughts, feelings, or internal monologue. 
- NEVER decide {{user}}'s actions, choices, or movements. 
- NEVER describe {{user}}'s body or state in ways {{char}} could not physically observe in the moment. Characters may guess at, misread, or ask about {{user}}'s thoughts, but the narration never states them.
- Write the world's reactions to {{user}}, never {{user}}'s reactions to the world.
</user_boundaries>

<realism_and_stakes>
- Genuine Consequences: Harm is real and lands. Outcomes are uncertain. This world is not safe, and mistakes have consequences. Consequences stem from actions, not karma; hope is earned through effort, never granted by narrative convenience.
- No Plot Armor: Do not nerf damage, soften consequences, or have attacks "narrowly miss" to protect {{user}}. {{user}}, {{char}}, and NPCs can be wounded, overwhelmed, captured, or killed. The story will survive any outcome, including {{user}}'s death.
- Combat & Violence: Combat is chaotic, exhausting, and short. Terrain and numbers matter more than skill. No mid-fight monologuing. Render trauma on-screen and in concrete detail, what breaks, tears, and bleeds, using correct anatomical terms with clinical accuracy. Keep the camera on the damage rather than summarizing or cutting away.
- Medical Realism: Track blood loss, shock, and infection timelines accurately. Adrenaline makes patients minimize pain. Healing magic (if applicable) requires cost, causes exhaustion, leaves scars, and is not a reset button.
- Erotic Realism: Prioritize characterization and psychosexual dynamics. Sex is visceral, flawed, and specific. Use blunt, explicit terms (cock, cum, pussy, asshole). Render intimate scenes moment to moment rather than summarizing or fading out. Track textures, fluids, fatigue, awkward angles, and miscommunication.
- Dungeon & Tactical Realism: Dimensional Rifts, Dungeon Hives, and Apex Trials are unforgiving hazard zones. Equipment durability, mana exhaustion, ammunition, abyssal corruption, and monster ecology follow rigorous physical and magical rules. Vanguards, tanks, and strikers must coordinate; lone arrogance inside high-tier hives is fatal.
- Scent, Pheromones & Lupine Social Ecology: Olfactory perception is constant and unyielding. Werewolves, minotaurs, demi-humans, and beastkin read arousal, fear, deception, adrenaline, and blood from the air. Mating ruts, female estrus/heats, dominance challenges, and submission signals drive visceral physical and psychological reactions.
</realism_and_stakes>"""

    # 5. Targeted partial payload
    payload = {
        'human_start_date': "0827-12-21T00:00:00.000Z",
        'calendar': calendar,
        'inline_command_config': inline_command_config,
        'system_prompt_override': updated_system_prompt
    }

    print("Sending partial PUT to Wyvern API...")
    req = urllib.request.Request(
        get_url,
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='PUT'
    )
    with urllib.request.urlopen(req) as resp:
        put_result = resp.read().decode('utf-8')
        print(f"PUT response status: {resp.status}")

    # 6. Post-write GET verification
    print("Verifying via post-write GET...")
    req = urllib.request.Request(get_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        verified_world = json.loads(resp.read().decode('utf-8'))

    print("--- Verification Results ---")
    print("human_start_date:", verified_world.get('human_start_date'))
    print("calendar.start_year:", verified_world.get('calendar', {}).get('start_year'))
    print("calendar.start_month_id:", verified_world.get('calendar', {}).get('start_month_id'))
    print("calendar.start_day_of_month:", verified_world.get('calendar', {}).get('start_day_of_month'))
    print("item_use instruction:", verified_world.get('inline_command_config', {}).get('sections', {}).get('item_use', {}).get('instructions'))
    print("system_prompt_override length:", len(verified_world.get('system_prompt_override', '')))
    print("Dungeon & Tactical Realism present:", "Dungeon & Tactical Realism" in verified_world.get('system_prompt_override', ''))
    print("Scent, Pheromones present:", "Scent, Pheromones & Lupine Social Ecology" in verified_world.get('system_prompt_override', ''))

    # 7. Sync to local dumps
    dump_path = 'exports/raw_db_dumps/raw_world.json'
    if os.path.exists(dump_path):
        with open(dump_path, 'r', encoding='utf-8') as f:
            local_raw = json.load(f)
        local_raw['human_start_date'] = verified_world.get('human_start_date')
        local_raw['calendar'] = verified_world.get('calendar')
        local_raw['inline_command_config'] = verified_world.get('inline_command_config')
        local_raw['system_prompt_override'] = verified_world.get('system_prompt_override')
        with open(dump_path, 'w', encoding='utf-8') as f:
            json.dump(local_raw, f, indent=2, ensure_ascii=False)
        print("Updated local raw_world.json.")

    export_path = 'exports/Svartulfr_Export.json'
    if os.path.exists(export_path):
        with open(export_path, 'r', encoding='utf-8') as f:
            master_export = json.load(f)
        master_export['human_start_date'] = verified_world.get('human_start_date')
        master_export['calendar'] = verified_world.get('calendar')
        master_export['inline_command_config'] = verified_world.get('inline_command_config')
        master_export['system_prompt_override'] = verified_world.get('system_prompt_override')
        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(master_export, f, indent=2, ensure_ascii=False)
        print("Updated local Svartulfr_Export.json.")

if __name__ == '__main__':
    update_simulation()
