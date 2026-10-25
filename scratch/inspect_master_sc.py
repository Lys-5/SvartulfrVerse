import json

path_sc = 'FINAL/Svartulfr_Master_Scenario.json'
with open(path_sc, 'r', encoding='utf-8') as f:
    sc = json.load(f)

print(f"Master Scenario ID: {sc.get('id')}")
print(f"Name: {sc.get('name')}")
print(f"Revision: {sc.get('revision')}")
print(f"Lorebook IDs: {sc.get('lorebook_ids')}")

print("\n=== SLOTS IN MASTER SCENARIO ===")
slots = sc.get('slots', [])
print(f"Total slots: {len(slots)}")
for idx, s in enumerate(slots):
    print(f"{idx+1}. key: {s.get('key'):15} | character_id: {s.get('character_id')} | pool: {len(s.get('character_pool', []))} | default: {s.get('default_role')}")

print("\n=== SYSTEM PROMPT PREVIEW ===")
sp = sc.get('system_prompt', '')
print(sp[:300])

print("\n=== FINAL INSTRUCTIONS (POST HISTORY) PREVIEW ===")
fi = sc.get('final_instructions', '')
print(fi[:300])
