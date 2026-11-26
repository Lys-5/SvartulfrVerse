import json
from pathlib import Path

p = Path(r'e:\repository\SvartulfrVerse\FINAL\Svartulfr_NPC_Secondary.json')
data = json.loads(p.read_text(encoding='utf-8'))
e = data['lexicon'][8]
print("Name:", e.get('name'))
print("Keys:", e.get('keys'))
print("Secondary Keys:", e.get('secondary_keys'))
print("Selective:", e.get('selective'))
print("Regex:", e.get('avatar_activation_regex'))
print("NPC Info:", e.get('npc_info'))
