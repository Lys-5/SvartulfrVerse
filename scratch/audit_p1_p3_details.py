import json
import pathlib
import urllib.request

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}

# 1. Check live Alyssa Persona via persona_1786335754946
req_p = urllib.request.Request('https://app.wyvern.chat/api/user-personas/persona_1786335754946', headers=headers)
live_p = json.loads(urllib.request.urlopen(req_p).read().decode('utf-8'))
local_p = json.loads((FINAL / 'personas' / 'Alyssa_Persona.json').read_text(encoding='utf-8'))
print(f"Alyssa Persona live keys: {list(live_p.keys())}")
print(f"Alyssa Persona outfits: local={len(local_p.get('outfits', []))} vs live={len(live_p.get('outfits', []))}")
for o in live_p.get('outfits', []):
    print(f"  Live Alyssa outfit: {o.get('name')!r} (id={o.get('id')})")

# 2. Inspect Russ Sinclair (#24) in NPC Primary
npc_prim = json.loads((FINAL / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
print("\n=== Russ Sinclair (#24) in NPC Primary ===")
print(json.dumps(npc_prim['lexicon'][24], indent=2, ensure_ascii=False))

# 3. Check for [INSTRUCTIONS in all 6 Lorebooks
for lb_name in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json', 'Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json']:
    lb = json.loads((FINAL / lb_name).read_text(encoding='utf-8'))
    hits = []
    for idx, e in enumerate(lb.get('lexicon', [])):
        c = e.get('content', e.get('text', ''))
        if '[INSTRUCTIONS' in c:
            hits.append((idx, e.get('name')))
    print(f"\n{lb_name}: total lexicon={len(lb.get('lexicon', []))} | [INSTRUCTIONS hits={len(hits)}: {hits}")
