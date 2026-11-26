import json
import pathlib

MY_DIR = pathlib.Path(__file__).parent
data = json.loads((MY_DIR / 'scenario_deep_analysis.json').read_text(encoding='utf-8'))

print("=== 1. DIFFERENCES BETWEEN LOCAL AND LIVE ===")
for prefix in ['alyssa', 'jasper']:
    live = data[f'live_{prefix}']
    local = data[f'local_{prefix}']
    print(f"\n--- {prefix.upper()} ---")
    print(f"Live rev: {live['revision']}, ID: {live['id']}")
    print(f"Local rev: {local['revision']}, ID: {local['id']}")
    print(f"Live greetings count: {len(live['greetings_analysis'])}, Local greetings count: {len(local['greetings_analysis'])}")
    print(f"Live slots count: {len(live['slots'])}, Local slots count: {len(local['slots'])}")
    
print("\n=== 2. SLOTS & POOLS (LIVE) ===")
for prefix in ['alyssa', 'jasper']:
    live = data[f'live_{prefix}']
    print(f"\n--- {prefix.upper()} SLOTS ---")
    for s in live['slots']:
        pool_str = ', '.join([f"{p['character_id']} (wt:{p.get('weight', 100)})" for p in s['pool_items']]) if s['pool_items'] else 'EMPTY POOL'
        print(f"  Key: '{s['key']:<18}' | Label: '{s['label']:<35}' | Unavail: {s['unavailable_count']} | Pool: [{pool_str}]")

print("\n=== 3. ALL MACRO OCCURRENCES IN GREETINGS & MESSAGES ===")
for prefix in ['alyssa', 'jasper']:
    live = data[f'live_{prefix}']
    print(f"\n--- {prefix.upper()} GREETINGS MACROS ---")
    all_macros = set()
    macro_details = []
    for g in live['greetings_analysis']:
        for m in g['g_macros']:
            all_macros.add(m['key'])
            macro_details.append((g['index'], g['name'], 'greeting.content', m['macro'], m['key'], m['context']))
        for msg in g['messages']:
            for m in msg['macros']:
                all_macros.add(m['key'])
                macro_details.append((g['index'], g['name'], f"msg[{msg['msg_index']}]({msg['speaker_slot']})", m['macro'], m['key'], m['context']))
    print(f"Distinct macro keys found: {all_macros}")
    for item in macro_details:
        print(f"  [G{item[0]}: {item[1][:25]}] in {item[2]}: {item[3]} -> context: {repr(item[5])}")

print("\n=== 4. SPEAKER_SLOT VALIDITY & INVARIANTS ===")
for prefix in ['alyssa', 'jasper']:
    live = data[f'live_{prefix}']
    print(f"\n--- {prefix.upper()} SPEAKER SLOTS ---")
    for g in live['greetings_analysis']:
        print(f"  G{g['index']}: '{g['name']}' | G.speaker_slot: '{g['speaker_slot']}' (valid: {g['speaker_valid_slot']}) | Inv_speaker_m0: {g['invariant_speaker_m0']} | Inv_content_m0: {g['invariant_content_m0']}")
        for m in g['messages']:
            print(f"     M{m['msg_index']}: speaker_slot: '{m['speaker_slot']}' (valid: {m['speaker_valid_slot']}) | content len: {m['content_len']}")
