import json
import pathlib

MY_DIR = pathlib.Path(__file__).parent
all_macros = json.loads((MY_DIR / 'all_macros_extracted.json').read_text(encoding='utf-8'))

# Exact NPC targets according to requirements:
# Scarlett, Russ, Jared, Stan, Sierra
# Plus we should note other macros like twin, childhood_friend, sports_rival, crush (Mac in Alyssa)

print("=== ALYSSA ROUTE: ALL 26 MACROS ===")
for idx, m in enumerate(all_macros['alyssa']):
    key = m['key']
    loc = m['location']
    g_idx = m['greeting_idx']
    g_name = m['greeting_name']
    ctx = m['context']
    spk = m.get('msg_speaker_slot') or m.get('speaker_slot')
    
    # identify character
    char_map = {
        'twin': 'Jasper Svartr Douglas Bloodmoon',
        'childhood_friend': 'Finnegan Novak',
        'best_friend': 'Scarlett Rose',
        'roommate': 'Sierra Cruz',
        'friend': 'Stanley Davies Jr.',
        'crush': 'Mackenzie Sanchez-Rogers',
        'quarterback': 'Jared Thompson',
        'sports_rival': 'Vincent Campbell'
    }
    char = char_map.get(key, 'UNKNOWN')
    is_target_npc = key in ['best_friend', 'roommate', 'quarterback', 'friend']
    print(f"[{idx+1:02d}] G{g_idx} ({loc}, spk:{spk}) | Key: '{key}' -> Char: {char} (Target NPC: {is_target_npc})")
    print(f"     Context: {repr(ctx)}")

print("\n=== JASPER ROUTE: ALL 19 MACROS ===")
for idx, m in enumerate(all_macros['jasper']):
    key = m['key']
    loc = m['location']
    g_idx = m['greeting_idx']
    g_name = m['greeting_name']
    ctx = m['context']
    spk = m.get('msg_speaker_slot') or m.get('speaker_slot')
    
    char_map = {
        'twin': 'Alyssa Hvit Douglas Bloodmoon',
        'childhood_friend': 'Finnegan Novak',
        'crush': 'Scarlett Rose',
        'male_roommate': 'Russell Sinclair',
        'friend': 'Stanley Davies Jr.',
        'quarterback': 'Jared Thompson',
        'sports_rival': 'Vincent Campbell',
        'ai_companion': 'Echo'
    }
    char = char_map.get(key, 'UNKNOWN')
    is_target_npc = key in ['crush', 'male_roommate', 'quarterback', 'friend']
    print(f"[{idx+1:02d}] G{g_idx} ({loc}, spk:{spk}) | Key: '{key}' -> Char: {char} (Target NPC: {is_target_npc})")
    print(f"     Context: {repr(ctx)}")
