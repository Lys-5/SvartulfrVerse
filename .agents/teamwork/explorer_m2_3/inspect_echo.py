import json
from pathlib import Path

p = Path(r'e:\repository\SvartulfrVerse\FINAL\Svartulfr_NPC_Primary.json')
data = json.loads(p.read_text(encoding='utf-8'))
e = data['lexicon'][9]
print("Name:", e.get('name'))
print("Content snippet:", e.get('content', '')[:300])
print("NPC info:", e.get('npc_info'))
print("Regex:", e.get('avatar_activation_regex'))
