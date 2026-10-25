import json

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    npc = json.load(f)

e = npc['entries'][1]
print("=== NPC SECONDARY ENTRY 1 (EDRIC) ===")
print("comment:", e.get('comment'))
print("content:\n", e.get('content'))
print("keys:", e.get('keys'))
