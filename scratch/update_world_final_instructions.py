import sys
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
import urllib.request
import json

def update_world_instructions():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    world_id = '_CgYT8fHXpDC4crjmegQF7'
    w_url = f'https://app.wyvern.chat/api/worlds/{world_id}'

    # 1. Fresh GET snapshot
    req = urllib.request.Request(w_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        current_world = json.loads(resp.read().decode('utf-8'))
    print(f"Current world final_instructions: {repr(current_world.get('final_instructions'))}")

    final_inst = (
        "Roleplay and world guidance for Svartulfr | Blackwood-Douglas:\n"
        "- Maintain an evocative, multi-sensory narrative tone blending gritty urban fantasy, supernatural political intrigue, and visceral emotional intensity.\n"
        "- LSE Biology & Senses: Fully honor lupine social ecology (active olfactory awareness, pheromonal shifts, pack hierarchy, primal dominance/submission impulses, heat/rut cycles, claiming, and mating bonds).\n"
        "- Unchained Adult Dynamics: Depict romance, passion, sexual tension, intense physical chemistry, power dynamics, and brutal combat with complete expressive freedom and emotional depth.\n"
        "- Platform Policy & Minor Safety: Minors (such as Edric Douglas, age 12) are strictly minor background NPCs with zero romantic or intimate framing under any circumstances. All romance, flirting, and intimacy strictly involves consenting adult characters (18+). No bestiality with real animals; no necrophilia or guro.\n"
        "- Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."
    )

    # 2. Targeted partial PUT
    payload = {
        'final_instructions': final_inst
    }
    req = urllib.request.Request(w_url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        print(f"PUT response code: {resp.status}")

    # 3. Post-write GET verification
    req = urllib.request.Request(w_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        verified_world = json.loads(resp.read().decode('utf-8'))
    saved_inst = verified_world.get('final_instructions')
    print(f"Verified final_instructions length: {len(saved_inst or '')}")
    if saved_inst == final_inst:
        print("SUCCESS: World final_instructions successfully updated and verified on Wyvern Web!")
    else:
        print(f"WARNING: Verification mismatch! Got: {repr(saved_inst)}")

if __name__ == '__main__':
    update_world_instructions()
