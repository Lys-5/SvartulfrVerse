import json

with open('FINAL/Edric_Douglas_card.json', 'r', encoding='utf-8') as f:
    card = json.load(f)

desc = card.get('description', '')
print("=== FULL DESCRIPTION OF EDRIC ===")
print(desc)
print("\n=== SYSTEM PROMPT / POST HISTORY ===")
print("system_prompt:", card.get('system_prompt', ''))
print("post_history_instructions:", card.get('post_history_instructions', ''))
