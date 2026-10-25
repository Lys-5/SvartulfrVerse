import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
local_path = ROOT / 'FINAL' / 'prompts' / 'Svartulfr_Master_TTRPG_Prompt_Assembly.json'
live_path = ROOT / '.agents' / 'teamwork' / 'explorer_m3_2' / 'live_prompt_assembly.json'

with open(local_path, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

with open(live_path, 'r', encoding='utf-8') as f:
    live_data = json.load(f)

print("=== 1. Core Top-Level Fields Comparison ===")
for k in ['name', 'description', 'visibility', 'floating_depth_percent', 'floating_role', 'start_reply_with', 'show_reply_prefix', 'join_final_instructions', 'join_string', 'prefix', 'suffix']:
    print(f"{k}: Local = {repr(local_data.get(k))} | Live = {repr(live_data.get(k))}")

print("\n=== 2. Template Strings Inspection ===")
for t in ['main_prompt_template', 'floating_prompt_template', 'lore_template', 'lore_template_header', 'lore_template_footer', 'lore_entry_separator', 'whisper_template']:
    loc_val = local_data.get(t, '')
    liv_val = live_data.get(t, '')
    identical = loc_val == liv_val
    print(f"Template '{t}': identical={identical}, loc_len={len(loc_val)}, liv_len={len(liv_val)}")
    if not identical:
        print(f"  Diff in {t}!")

print("\n=== 3. Blocks Inspection ===")
print("Local blocks count:", len(local_data.get('blocks', [])))
print("Live blocks count:", len(live_data.get('blocks', [])))
for i, b in enumerate(local_data.get('blocks', [])):
    liv_b = live_data.get('blocks', [])[i] if i < len(live_data.get('blocks', [])) else {}
    print(f"Block {i} ({b.get('block_id')}): identical={b == liv_b}")

print("\n=== 4. Check for Date-Forcing or March 15 in templates and blocks ===")
all_text = json.dumps(local_data)
for kw in ['15', 'march', 'marzo', '2024', 'date', 'current_date', 'clock', 'time']:
    count = all_text.lower().count(kw)
    print(f"Keyword '{kw}' in local assembly: {count}")
