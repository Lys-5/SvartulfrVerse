import json

with open('e:/repository/SvartulfrVerse/scratch/explore_prompt_assemblies.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('e:/repository/SvartulfrVerse/scratch/assembly_details_dump.txt', 'w', encoding='utf-8') as out:
    for item in data.get('results', []):
        out.write("================================================================================\n")
        out.write(f"ASSEMBLY: {item.get('id')} — {item.get('name')}\n")
        out.write("================================================================================\n")
        out.write(f"floating_depth_percent: {item.get('floating_depth_percent')}\n")
        out.write(f"floating_role: {item.get('floating_role')}\n")
        out.write(f"start_reply_with: {repr(item.get('start_reply_with'))}\n")
        out.write(f"show_reply_prefix: {item.get('show_reply_prefix')}\n")
        out.write(f"join_final_instructions: {item.get('join_final_instructions')}\n")
        out.write("\n--- MAIN PROMPT TEMPLATE ---\n")
        out.write(str(item.get('main_prompt_template')) + "\n")
        out.write("\n--- MAIN PROMPT SECTIONS ---\n")
        for s in item.get('main_prompt_sections', []):
            out.write(f"[{s.get('order')}] {s.get('name')} (role={s.get('role')}, enabled={s.get('enabled')}, marker={s.get('marker')}):\n")
            out.write(str(s.get('content')) + "\n")
        out.write("\n--- FLOATING PROMPT TEMPLATE ---\n")
        out.write(str(item.get('floating_prompt_template')) + "\n")
        out.write("\n--- FLOATING PROMPT SECTIONS ---\n")
        for s in item.get('floating_prompt_sections', []):
            out.write(f"[{s.get('order')}] {s.get('name')} (depth={s.get('depth')}, role={s.get('role')}, enabled={s.get('enabled')}):\n")
            out.write(str(s.get('content')) + "\n")
        out.write("\n--- LORE TEMPLATE HEADER ---\n")
        out.write(str(item.get('lore_template_header')) + "\n")
        out.write("\n--- LORE TEMPLATE ---\n")
        out.write(str(item.get('lore_template')) + "\n")
        out.write("\n--- LORE TEMPLATE FOOTER ---\n")
        out.write(str(item.get('lore_template_footer')) + "\n")
        out.write("\n--- LORE ENTRY SEPARATOR ---\n")
        out.write(str(item.get('lore_entry_separator')) + "\n")
        out.write("\n--- WHISPER TEMPLATE ---\n")
        out.write(str(item.get('whisper_template')) + "\n")
        out.write("\n--- BLOCKS (Final Instructions) ---\n")
        for b in item.get('blocks', []):
            out.write(f"BLOCK: {b.get('label')} (role={b.get('role')}, order={b.get('order')}, enabled={b.get('enabled')}):\n")
            out.write(str(b.get('content')) + "\n")
            out.write("-" * 40 + "\n")
        out.write("\n\n")

print("Dumped all assembly details to scratch/assembly_details_dump.txt successfully")
