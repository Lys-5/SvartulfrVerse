import json
import pathlib
import urllib.request

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}

# 1. Inspect NPC Primary for Russ and {{user}} Hvit
npc_prim = json.loads((FINAL / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
print(f"NPC Primary local entries={len(npc_prim.get('entries', []))} lexicon={len(npc_prim.get('lexicon', []))}")
for idx, e in enumerate(npc_prim.get('lexicon', [])):
    name = e.get('name', '')
    if 'russ' in name.lower() or 'alyssa' in name.lower() or 'hvit' in name.lower() or '{{user}}' in name.lower():
        print(f"  [NPC Primary lex #{idx}] id={e.get('id') or e.get('uid')} name={name!r} type={e.get('type')} enabled={e.get('enabled', not e.get('disable', False))} len={len(e.get('content', e.get('text', '')))}")

# Check live NPC Primary
req = urllib.request.Request('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
live_prim = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
print(f"NPC Primary LIVE entries={len(live_prim.get('entries', []))} lexicon={len(live_prim.get('lexicon', []))}")
for idx, e in enumerate(live_prim.get('lexicon', [])):
    name = e.get('name', '')
    if 'russ' in name.lower() or 'alyssa' in name.lower() or 'hvit' in name.lower() or '{{user}}' in name.lower():
        print(f"  [LIVE NPC Primary lex #{idx}] id={e.get('id') or e.get('uid')} name={name!r} type={e.get('type')} len={len(e.get('content', e.get('text', '')))}")

# 2. Inspect NPC Secondary for Thrakgor, Crowe, Morgeth, Thorvald, Harald
npc_sec = json.loads((FINAL / 'Svartulfr_NPC_Secondary.json').read_text(encoding='utf-8'))
print(f"\nNPC Secondary local entries={len(npc_sec.get('entries', []))} lexicon={len(npc_sec.get('lexicon', []))}")
targets = ['thrakgor', 'crowe', 'morgeth', 'thorvald', 'harald']
for idx, e in enumerate(npc_sec.get('lexicon', [])):
    name = e.get('name', '')
    if any(t in name.lower() for t in targets):
        print(f"  [NPC Secondary lex #{idx}] name={name!r} type={e.get('type')}")
        c = e.get('content', e.get('text', ''))
        for line in c.splitlines():
            if 'RPG' in line or 'STATS' in line or 'LEVEL' in line:
                print(f"    {line}")

# 3. Check Wulfnic & Alyssa Persona on Wyvern API
req_w = urllib.request.Request('https://app.wyvern.chat/api/characters/_HEQQbbRFwKdG8QE2Fh1z1', headers=headers)
live_w = json.loads(urllib.request.urlopen(req_w).read().decode('utf-8'))
local_w = json.loads((FINAL / 'Wulfnic_Bloodmoon_card.json').read_text(encoding='utf-8'))
print(f"\nWulfnic outfits: local={len(local_w.get('outfits', []))} vs live={len(live_w.get('outfits', []))}")
for o in live_w.get('outfits', []):
    print(f"  Live Wulfnic outfit: {o.get('name')!r} (id={o.get('id')})")

# Check Alyssa Persona ID
print("\nChecking FINAL/personas:")
for pfile in (FINAL / 'personas').glob('*.json'):
    pdata = json.loads(pfile.read_text(encoding='utf-8'))
    print(f"  {pfile.name}: id={pdata.get('id')} _id={pdata.get('_id')} outfits={len(pdata.get('outfits', pdata.get('appearances', [])))}")
