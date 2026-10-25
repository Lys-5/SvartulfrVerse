import json

with open('FINAL/assistants/Svartulfr_Game_Master_Assistant.json', 'r', encoding='utf-8') as f:
    asst = json.load(f)

with open('scratch/asst_prompts.txt', 'w', encoding='utf-8') as f:
    f.write('=== SYSTEM PROMPT ===\n')
    f.write(asst.get('system_prompt', ''))
    f.write('\n\n=== FINAL INSTRUCTIONS ===\n')
    f.write(asst.get('final_instructions', ''))

print('Saved to scratch/asst_prompts.txt')
