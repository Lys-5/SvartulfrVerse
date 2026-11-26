import json
import pathlib

MY_DIR = pathlib.Path(__file__).parent
data = json.loads((MY_DIR / 'scenario_deep_analysis.json').read_text(encoding='utf-8'))

for prefix in ['alyssa', 'jasper']:
    live = data[f'live_{prefix}']
    local = data[f'local_{prefix}']
    print(f"\n==================== {prefix.upper()} ====================")
    print(f"LIVE revision: {live.get('revision')}, LOCAL revision: {local.get('revision')}")
    print(f"LIVE ID: {live.get('id')}, LOCAL ID: {local.get('id')}")
    
    # Check slots
    print("\n--- SLOTS (LIVE) ---")
    for s in live['slots']:
        print(f"  Key: {s['key']} | Label: {s['label']} | Unavail: {s['unavailable_count']} | Pool: {s['pool_items']}")
    
    print("\n--- SLOTS (LOCAL) ---")
    for s in local['slots']:
        print(f"  Key: {s['key']} | Label: {s['label']} | Unavail: {s['unavailable_count']} | Pool: {s['pool_items']}")

    # Check differences in slots
    live_slots = {s['key']: s for s in live['slots']}
    local_slots = {s['key']: s for s in local['slots']}
    
    diff_keys = set(live_slots.keys()) ^ set(local_slots.keys())
    if diff_keys:
        print(f"\nDifference in slot keys: {diff_keys}")
    else:
        print("\nSlot keys match between live and local.")
        for k in live_slots:
            s_live = live_slots[k]
            s_local = local_slots[k]
            if s_live != s_local:
                print(f"Slot '{k}' differs: LIVE={s_live} vs LOCAL={s_local}")
